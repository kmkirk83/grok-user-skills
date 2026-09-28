# Multi-User Room + Auth Patterns

## Simple Token Pattern (recommended default)

- On join, client receives a short-lived JWT or random room token.
- All WebSocket / WebRTC messages carry the token.
- Server maintains a room registry: room_id → set of connected sessions + shared state.
- Agents are scoped to a single room.

## OAuth Stub

- Provide a placeholder `/auth/login` that can later be wired to Auth0, Clerk, or GitHub OAuth.
- After login, issue the room token.

## Hybrid Voice + Text

- Same room can have both text WebSocket clients and Pipecat / LiveKit voice participants.
- Shared LangGraph state or CrewAI memory is keyed by room_id.
- Text and voice both stream into the same orchestrator.
