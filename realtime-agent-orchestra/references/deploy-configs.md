# One-Click Deploy Configs

## Modal
- Provide a modal_app.py that defines the FastAPI or Pipecat service.
- `modal deploy modal_app.py` one-liner.

## Railway
- railway.toml or Dockerfile + Procfile.
- Environment variables set in the Railway dashboard.

## Fly.io
- fly.toml with the correct port and health check.
- `fly launch` + `fly deploy`.

## Docker Compose (local default)
- Always include a working docker-compose.yml with:
  - orchestrator service
  - optional redis / postgres
  - optional ollama for local models
  - volume mounts for development

All configs must work after the user fills .env and runs a single command.
