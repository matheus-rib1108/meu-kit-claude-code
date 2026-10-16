<#
  Instala o kit no Claude Code (Windows).
  Uso:
    .\install.ps1                         # tudo em ~/.claude
    .\install.ps1 -Skill site-fortress    # só uma skill
    .\install.ps1 -Destino C:\teste       # outra pasta (para testar)
    .\install.ps1 -Force                  # sobrescreve o que já existe
#>
param(
    [string]$Destino = (Join-Path $HOME '.claude'),
    [string]$Skill = '',
    [switch]$SemAgentes,
    [switch]$Force
)
$ErrorActionPreference = 'Stop'
$Kit = $PSScriptRoot
$skillsDst = Join-Path $Destino 'skills'
$agentsDst = Join-Path $Destino 'agents'
New-Item -ItemType Directory -Force -Path $skillsDst | Out-Null

$todas = Get-ChildItem (Join-Path $Kit 'skills') -Directory | ForEach-Object { Get-ChildItem $_.FullName -Directory }
if ($Skill) {
    $todas = @($todas | Where-Object { $_.Name -eq $Skill })
    if ($todas.Count -eq 0) { Write-Host "Skill '$Skill' não encontrada no kit." -ForegroundColor Red; exit 1 }
}

$novas = 0; $puladas = 0
foreach ($s in $todas) {
    $alvo = Join-Path $skillsDst $s.Name
    if ((Test-Path $alvo) -and -not $Force) { $puladas++; continue }
    if (Test-Path $alvo) { Remove-Item -Recurse -Force $alvo }
    Copy-Item -Recurse $s.FullName $alvo
    $novas++
}
Write-Host "Skills: $novas instaladas, $puladas já existiam em $skillsDst" -ForegroundColor Green

if (-not $Skill -and -not $SemAgentes) {
    New-Item -ItemType Directory -Force -Path $agentsDst | Out-Null
    $an = 0; $ap = 0
    foreach ($a in Get-ChildItem (Join-Path $Kit 'agents') -Filter *.md) {
        $alvo = Join-Path $agentsDst $a.Name
        if ((Test-Path $alvo) -and -not $Force) { $ap++; continue }
        Copy-Item $a.FullName $alvo -Force
        $an++
    }
    Write-Host "Agentes: $an instalados, $ap já existiam em $agentsDst" -ForegroundColor Green

    $p = Get-Content (Join-Path $Kit 'plugins\plugins.json') -Raw -Encoding UTF8 | ConvertFrom-Json
    Write-Host "`nPlugins: cole no Claude Code:" -ForegroundColor Cyan
    Write-Host "  /plugin marketplace add anthropics/claude-plugins-official"
    foreach ($prop in $p.enabledPlugins.PSObject.Properties) {
        $obs = ''
        if (-not $prop.Value) { $obs = '   (opcional, fica desligado)' }
        Write-Host "  /plugin install $($prop.Name)$obs"
    }
    Write-Host "`nCLAUDE.md e mcp\.mcp.json não foram copiados: veja o README e copie o que quiser." -ForegroundColor Yellow
}
Write-Host "Pronto. Abra uma conversa nova no Claude Code para carregar." -ForegroundColor Green
