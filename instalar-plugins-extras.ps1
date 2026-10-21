<#
  Instala os plugins extras do kit no Claude Code (Windows), sem precisar abrir o Claude.
  O sync-kit.ps1 roda este script sozinho uma vez por versão da lista (marca em ~/.claude/kit-sync).
  Também dá para rodar na mão:  powershell -ExecutionPolicy Bypass -File instalar-plugins-extras.ps1

  Para tirar um plugin da lista, apague a linha dele em $Plugins e aumente $Versao.
  Para desinstalar no PC:  claude plugin uninstall <nome>@<marketplace>
#>
param([switch]$Forcar)
$ErrorActionPreference = 'Continue'
$Versao = 1

# Marketplaces (repositório no GitHub)
$Marketplaces = @(
    'anthropics/claude-plugins-official',
    'thedotmack/claude-mem'
)

# nome@marketplace  |  o que faz
$Plugins = [ordered]@{
    'feature-dev@claude-plugins-official'       = 'Fluxo completo para criar uma funcionalidade: entender, planejar, construir e revisar'
    'code-review@claude-plugins-official'       = 'Revisão de código com vários agentes (/code-review)'
    'pr-review-toolkit@claude-plugins-official' = 'Revisão de pull request: testes, erros silenciosos, tipos e comentários'
    'commit-commands@claude-plugins-official'   = 'Comandos /commit e /commit-push-pr'
    'frontend-design@claude-plugins-official'   = 'Design de interface sem cara de IA (plugin oficial)'
    'playwright@claude-plugins-official'        = 'O Claude abre o navegador, testa o site e tira print'
    'supabase@claude-plugins-official'          = 'Conector do Supabase (pede login na primeira vez)'
    'vercel@claude-plugins-official'            = 'Conector da Vercel: deploy e logs (pede login na primeira vez)'
    'figma@claude-plugins-official'             = 'Conector do Figma (pede login na primeira vez)'
    'hookify@claude-plugins-official'           = 'Cria hooks em português simples ("não deixa apagar a pasta X")'
    'plugin-dev@claude-plugins-official'        = 'Ajuda a criar os seus próprios plugins'
    'skill-creator@claude-plugins-official'     = 'Cria e testa skills novas'
    'agent-sdk-dev@claude-plugins-official'     = 'Ajuda a criar agentes com o Claude Agent SDK (bom para o JARVIS)'
    'claude-mem@thedotmack'                     = 'Memória entre sessões: lembra o que foi feito ontem'
}

$utf8 = New-Object System.Text.UTF8Encoding($false)
$KitSync = Join-Path $HOME '.claude\kit-sync'
$Marca = Join-Path $KitSync "plugins-extras-v$Versao.ok"
if ((Test-Path $Marca) -and -not $Forcar) { Write-Host "Plugins extras v$Versao já instalados."; exit 0 }

$claude = (Get-Command claude -ErrorAction SilentlyContinue).Source
if (-not $claude) { Write-Host 'Claude Code (comando "claude") não encontrado no PATH.' -ForegroundColor Red; exit 2 }

foreach ($m in $Marketplaces) {
    & $claude plugin marketplace add $m 2>&1 | Out-Null
}
$ok = 0; $falhas = @()
foreach ($p in $Plugins.Keys) {
    $saida = & $claude plugin install $p 2>&1
    if ($LASTEXITCODE -eq 0) { $ok++; Write-Host "  + $p" -ForegroundColor Green }
    else { $falhas += $p; Write-Host "  x $p : $($saida | Select-Object -Last 1)" -ForegroundColor Yellow }
}
Write-Host "Plugins: $ok instalados, $($falhas.Count) com erro." -ForegroundColor Cyan
if ($falhas.Count -eq 0) {
    New-Item -ItemType Directory -Force -Path $KitSync | Out-Null
    [IO.File]::WriteAllText($Marca, (Get-Date -Format 'yyyy-MM-dd HH:mm'), $utf8)
}
Write-Host 'Abra uma conversa nova no Claude Code para carregar.'
exit 0
