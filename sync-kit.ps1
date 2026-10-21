<#
  Atualiza o kit no GitHub.
  1. Copia skills, agentes, plugins, .mcp.json e CLAUDE.md atuais (scripts/build_kit.py) e refaz o README.
  2. Roda o Gitleaks e a busca de dados pessoais (scripts/check_personal.py).
  3. Só se estiver tudo limpo e algo tiver mudado: commit "Atualiza kit: <o que mudou>" e push.
  Se achar algo suspeito, não publica e grava o aviso em sync-kit.log.

  Uso: powershell -ExecutionPolicy Bypass -File sync-kit.ps1 [-SemPush]
#>
param([switch]$SemPush)
$ErrorActionPreference = 'Continue'
$Repo = $PSScriptRoot
$Log = Join-Path $Repo 'sync-kit.log'
$Lock = Join-Path $Repo 'sync-kit.lock'
$utf8 = New-Object System.Text.UTF8Encoding($false)
[Console]::OutputEncoding = $utf8
$env:PYTHONIOENCODING = 'utf-8'

function Log([string]$msg) {
    $line = "[{0}] {1}" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $msg
    Write-Host $line
    [IO.File]::AppendAllText($Log, $line + "`r`n", $utf8)
}

# Notificação do Windows (canto da tela) quando o kit NÃO é publicado
function Avisar([string]$texto) {
    try {
        [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] | Out-Null
        [Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom.XmlDocument, ContentType = WindowsRuntime] | Out-Null
        $esc = [Security.SecurityElement]::Escape($texto)
        $xml = New-Object Windows.Data.Xml.Dom.XmlDocument
        $xml.LoadXml("<toast><visual><binding template='ToastGeneric'><text>Kit do Claude NÃO publicado</text><text>$esc</text><text>Veja sync-kit.log</text></binding></visual></toast>")
        $app = '{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\WindowsPowerShell\v1.0\powershell.exe'
        [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier($app).Show([Windows.UI.Notifications.ToastNotification]::new($xml))
    } catch { Log "  (não consegui mostrar a notificação: $($_.Exception.Message))" }
}

# Uma execução por vez (o hook pode disparar várias conversas fechando juntas)
if (Test-Path $Lock) {
    if ((Get-Item $Lock).LastWriteTime -gt (Get-Date).AddMinutes(-30)) { Write-Host 'Outra sincronização em andamento.'; exit 0 }
    Remove-Item $Lock -Force
}
New-Item -ItemType File -Path $Lock -Force | Out-Null

try {
    Set-Location $Repo
    $gitleaks = (Get-Command gitleaks -ErrorAction SilentlyContinue).Source
    if (-not $gitleaks) {
        $gitleaks = Get-ChildItem "$env:LOCALAPPDATA\Microsoft\WinGet\Packages" -Recurse -Filter gitleaks.exe -ErrorAction SilentlyContinue |
            Select-Object -First 1 -ExpandProperty FullName
    }
    if (-not $gitleaks) { Log 'NÃO PUBLICADO: gitleaks não encontrado (winget install Gitleaks.Gitleaks).'; Avisar 'Gitleaks não encontrado.'; exit 2 }

    if (-not $SemPush) {
        $antes = "$(git rev-parse HEAD)".Trim()
        git pull --rebase --quiet 2>&1 | Out-Null
        # Skills que chegaram pelo GitHub (adicionadas fora deste PC) vão para ~/.claude/skills antes de montar o kit.
        # Sem isso o build_kit.py, que refaz skills/ a partir do PC, apagaria essas skills no próximo sync.
        # Só entram skills NOVAS no pull; uma skill que você apagou no PC continua apagada.
        $recebidas = @(git diff --name-only --diff-filter=A "$antes" HEAD -- 'skills/*/*/SKILL.md' 2>$null)
        foreach ($f in $recebidas) {
            $nome = ($f -split '/')[2]
            if (-not (Test-Path (Join-Path $HOME ".claude\skills\$nome"))) {
                & (Join-Path $Repo 'install.ps1') -Skill $nome | Out-Null
                Log "skill recebida do GitHub e instalada no PC: $nome"
            }
        }
    }

    $notas = & python scripts/build_kit.py 2>&1
    if ($LASTEXITCODE -ne 0) { Log "NÃO PUBLICADO: erro ao montar o kit: $($notas -join ' | ')"; Avisar 'Erro ao montar o kit.'; exit 3 }
    foreach ($n in $notas) { if ("$n".Trim()) { Log "$n" } }

    $pessoais = & python scripts/check_personal.py 2>&1
    $okPessoais = ($LASTEXITCODE -eq 0)
    $vaz = & $gitleaks dir . --no-banner --redact --exit-code 1 2>&1
    $okLeaks = ($LASTEXITCODE -eq 0)
    if (-not ($okPessoais -and $okLeaks)) {
        Log 'NÃO PUBLICADO: algo suspeito foi encontrado. Nada foi enviado ao GitHub.'
        if (-not $okPessoais) { foreach ($l in $pessoais) { Log "  $l" } }
        if (-not $okLeaks) { foreach ($l in ($vaz | Select-String -Pattern 'File:|RuleID:|Line:')) { Log "  gitleaks $l" } }
        Avisar 'Achei possível segredo, dado pessoal ou termo privado. Nada foi enviado.'
        exit 1
    }

    git add -A
    $mudancas = @(git diff --cached --name-status | Where-Object { $_ -notmatch "`tREADME\.md$" -and $_ -notmatch "`tkit-meta\.json$" })
    if ($mudancas.Count -eq 0) {
        git reset --quiet
        git checkout --quiet -- README.md kit-meta.json 2>$null
        Log 'Limpo. Nada mudou: nada publicado.'
        exit 0
    }

    # Resume o que mudou: +novo, -removido, ~alterado
    $itens = [ordered]@{}
    foreach ($m in $mudancas) {
        $p = $m -split "`t"
        $st = $p[0].Substring(0, 1); $path = $p[-1]
        $nome = $null
        if ($path -match '^skills/[^/]+/([^/]+)/') { $nome = "skill $($Matches[1])"; $top = "skills/" + ($path -split '/')[1] + "/" + $Matches[1] + "/SKILL.md" }
        elseif ($path -match '^agents/([^/]+)\.md$') { $nome = "agente $($Matches[1])"; $top = $path }
        elseif ($path -like 'plugins/*') { $nome = 'plugins'; $top = $null }
        elseif ($path -like 'mcp/*') { $nome = 'conectores MCP'; $top = $null }
        elseif ($path -eq 'CLAUDE.md') { $nome = 'CLAUDE.md'; $top = $null }
        elseif ($path -match '^commands/(.+)\.md$') { $nome = "comando $($Matches[1])"; $top = $path }
        elseif ($path -eq 'conta-claude-ai.md') { $nome = 'conta claude.ai'; $top = $null }
        elseif ($path -eq 'CHANGELOG.md') { continue }
        else { $nome = 'arquivos do kit'; $top = $null }
        $sinal = '~'
        if ($top -and $path -eq $top -and $st -eq 'A') { $sinal = '+' }
        if ($top -and $path -eq $top -and $st -eq 'D') { $sinal = '-' }
        if (-not $itens.Contains($nome) -or $sinal -ne '~') { $itens[$nome] = $sinal }
    }
    $partes = @($itens.Keys | Sort-Object { if ($_ -like 'skill *' -or $_ -like 'agente *') { 0 } else { 1 } }, { $_ } | ForEach-Object { $itens[$_] + $_ })
    $resumo = ($partes | Select-Object -First 8) -join ', '
    if ($partes.Count -gt 8) { $resumo += " e mais $($partes.Count - 8)" }
    $msgFile = Join-Path $env:TEMP 'kit-commit-msg.txt'
    [IO.File]::WriteAllText($msgFile, "Atualiza kit: $resumo`n`n" + ($partes -join "`n") + "`n", $utf8)
    git commit --quiet -F $msgFile
    if ($LASTEXITCODE -ne 0) { Log 'NÃO PUBLICADO: falha no commit.'; Avisar 'Falha no commit.'; exit 4 }
    if ($SemPush) { Log "Commit feito (sem push): $resumo"; exit 0 }
    $out = git push --quiet 2>&1
    if ($LASTEXITCODE -ne 0) { Log "NÃO PUBLICADO: falha no push: $out"; Avisar 'Falha ao enviar para o GitHub (push).'; exit 5 }
    Log "Publicado: Atualiza kit: $resumo"
}
finally {
    Remove-Item $Lock -Force -ErrorAction SilentlyContinue
}
