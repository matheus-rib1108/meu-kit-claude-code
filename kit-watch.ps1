<#
  Vigia do kit: observa as pastas e arquivos do Claude Code e, quando algo muda,
  espera 2 minutos sem novas mudanças e roda o sync-kit.ps1 (escondido).

  Observa: ~/.claude/skills, agents, commands, CLAUDE.md e settings.json (plugins, hooks, configuração),
  ~/.claude/plugins/installed_plugins.json, ~/.claude.json (só a lista "mcpServers"),
  ~/.claude/kit-sync/conta-claude-ai.json e o .mcp.json dos projetos (~/repos e Área de Trabalho).

  Pausar: crie o arquivo ~/.claude/kit-sync/PAUSADO (apague para voltar).
  Inicia com o Windows pela tarefa "MeuKitClaudeCode-Vigia" do Agendador de Tarefas.

  Uso: powershell -NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File kit-watch.ps1 [-EsperaSegundos 120]
#>
param([int]$EsperaSegundos = 120)
$ErrorActionPreference = 'Continue'
$Repo = $PSScriptRoot
$Sync = Join-Path $Repo 'sync-kit.ps1'
$Log = Join-Path $Repo 'sync-kit.log'
$Claude = Join-Path $HOME '.claude'
$KitSync = Join-Path $Claude 'kit-sync'
$Pausa = Join-Path $KitSync 'PAUSADO'
$utf8 = New-Object System.Text.UTF8Encoding($false)

function Log([string]$msg) {
    $line = "[{0}] vigia: {1}" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $msg
    [IO.File]::AppendAllText($Log, $line + "`r`n", $utf8)
}

# Só um vigia por vez
$mutex = New-Object Threading.Mutex($false, 'Local\MeuKitClaudeCode-Vigia')
if (-not $mutex.WaitOne(0)) { exit 0 }

# Impressão digital só da parte que interessa de arquivos que mudam o tempo todo
function Digital([string]$path) {
    try {
        $j = Get-Content -LiteralPath $path -Raw -Encoding UTF8 | ConvertFrom-Json
        if ($path -like '*\.claude.json') { $parte = $j.mcpServers } else { $parte = $j }
        $txt = $parte | ConvertTo-Json -Depth 20 -Compress
        $sha = [Security.Cryptography.SHA1]::Create()
        return [BitConverter]::ToString($sha.ComputeHash($utf8.GetBytes([string]$txt)))
    } catch { return $null }   # arquivo no meio da gravação: tenta de novo no próximo evento
}

$UserJson = Join-Path $HOME '.claude.json'
$Settings = Join-Path $Claude 'settings.json'
$digitais = @{ $UserJson = (Digital $UserJson); $Settings = (Digital $Settings) }

$Ignorar = '\\(\.git|node_modules|__pycache__|graphify-out|\.remember)(\\|$)|\.(tmp|swp|log|pyc)$|~$'

# (pasta, filtro, subpastas?)
$alvos = @(
    @((Join-Path $Claude 'skills'), '*', $true),
    @((Join-Path $Claude 'agents'), '*', $true),
    @($Claude, '*', $false),                                   # settings.json, CLAUDE.md, pasta commands
    @((Join-Path $Claude 'plugins'), 'installed_plugins.json', $false),
    @($HOME, '.claude.json', $false),
    @($KitSync, 'conta-claude-ai.json', $false),
    @((Join-Path $HOME 'repos'), '.mcp.json', $true),
    @([Environment]::GetFolderPath('Desktop'), '.mcp.json', $true)
)
$cmds = Join-Path $Claude 'commands'
if (Test-Path $cmds) { $alvos += , @($cmds, '*', $true) }

$watchers = @()
$i = 0
foreach ($a in $alvos) {
    if (-not (Test-Path -LiteralPath $a[0])) { continue }
    $w = New-Object IO.FileSystemWatcher
    $w.Path = $a[0]; $w.Filter = $a[1]; $w.IncludeSubdirectories = $a[2]
    $w.NotifyFilter = [IO.NotifyFilters]'FileName, DirectoryName, LastWrite, Size'
    $w.InternalBufferSize = 65536
    foreach ($ev in 'Changed', 'Created', 'Deleted', 'Renamed') {
        Register-ObjectEvent -InputObject $w -EventName $ev -SourceIdentifier "kitw$i-$ev" | Out-Null
    }
    $w.EnableRaisingEvents = $true
    $watchers += $w; $i++
}
Log "iniciado (observando $($watchers.Count) lugares, espera de $EsperaSegundos s)"

$TopoOk = @('settings.json', 'CLAUDE.md', 'commands', 'skills', 'agents')
$ate = $null
$ultimo = ''
while ($true) {
    $e = Wait-Event -Timeout 5
    while ($e) {
        $p = [string]$e.SourceEventArgs.FullPath
        Remove-Event -EventIdentifier $e.EventIdentifier
        $relevante = $p -and ($p -notmatch $Ignorar)
        if ($relevante -and (Split-Path $p -Parent) -eq $Claude) {
            $relevante = $TopoOk -contains (Split-Path $p -Leaf)
        }
        if ($relevante -and ($p -eq $UserJson -or $p -eq $Settings)) {
            $d = Digital $p
            if (-not $d -or $d -eq $digitais[$p]) { $relevante = $false } else { $digitais[$p] = $d }
        }
        if ($relevante) {
            $ate = (Get-Date).AddSeconds($EsperaSegundos)
            if ($p -ne $ultimo) { Log "mudança: $($p.Replace($HOME, '~'))"; $ultimo = $p }
        }
        $e = Get-Event | Select-Object -First 1
    }
    if ($ate -and (Get-Date) -ge $ate) {
        $ate = $null; $ultimo = ''
        if (Test-Path $Pausa) { Log 'pausado (arquivo PAUSADO existe): sync não rodou'; continue }
        Log 'sem mudanças há 2 min: rodando sync-kit.ps1'
        Start-Process powershell.exe -WindowStyle Hidden -Wait -ArgumentList @(
            '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', "`"$Sync`"")
    }
}
