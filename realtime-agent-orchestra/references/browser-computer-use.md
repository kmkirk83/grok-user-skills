# Browser & Computer-Use Agents (2026)

## Top Open Options
- **browser-use**: Python, Playwright-based, accessibility tree + screenshots. Highest open-source Mind2Web scores. Easy to wrap as a tool or MCP server.
- **Playwright MCP**: Official Microsoft MCP server exposing browser control as tools. Drop-in for any MCP-compatible agent.
- **Stagehand** (Browserbase): Higher-level, natural language actions + cloud browsers.
- **Claude / Gemini / OpenAI Computer Use APIs**: Screenshot → pixel/action loops. Best for visual/legacy UIs.

## Integration Patterns
1. Treat browser agent as a specialized worker node inside LangGraph/CrewAI.
2. Expose via MCP so any orchestrator can call "browse", "click", "extract", "fill_form".
3. For full computer use (desktop), combine with OS-level tools (e.g., via Anthropic computer-use or custom sandboxes).

## Security Notes
Always run browser agents in isolated containers or cloud browser services. Never give them unrestricted host access without explicit user approval.
