#!/bin/sh
# Starts the Playwright MCP browser server.
# In the Claude Code cloud container, use the pre-installed Chromium and the agent proxy;
# on a normal computer, Playwright uses its own browser.
VERSION=0.0.82
if [ -x /opt/pw-browsers/chromium ]; then
  set -- --executable-path /opt/pw-browsers/chromium --no-sandbox "$@"
  [ -n "$HTTPS_PROXY" ] && set -- --proxy-server "$HTTPS_PROXY" "$@"
fi
exec npx -y "@playwright/mcp@$VERSION" --headless "$@"
