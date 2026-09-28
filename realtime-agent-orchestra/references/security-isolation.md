# Security & Isolation Rules

## Mandatory for every scaffold

1. **Browser / Computer-use agents**
   - Must run inside Docker containers or cloud browser services (Browserbase, Stagehand, Browser Use Cloud).
   - Never mount host filesystem unless the user explicitly requests and confirms.
   - Prefer accessibility-tree + screenshot approaches over raw pixel control when possible.

2. **Secrets**
   - All API keys, tokens, and credentials live only in environment variables or secret managers.
   - .env.example must list every required key with dummy values.
   - Never commit real secrets.

3. **Multi-user isolation**
   - Each room / session has its own conversation state and short-lived auth token.
   - Agents cannot see or act on other rooms.
   - Rate-limit and timeout idle sessions.

4. **Human-in-the-loop**
   - Any action that writes to external systems, spends money, or modifies files outside the sandbox requires an explicit approval node.

5. **Network**
   - Default to allow-list of domains if the agent has outbound access.
   - Document the allow-list in the README.
