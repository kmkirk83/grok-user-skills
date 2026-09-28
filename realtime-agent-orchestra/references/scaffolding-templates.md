# Common Scaffolding Patterns

## Minimal LangGraph Supervisor
- State: TypedDict with messages, next_agent, shared_data
- Nodes: supervisor (router), worker agents, tools
- Edges: conditional on supervisor decision
- Checkpointer: MemorySaver or PostgresSaver
- Streaming: astream_events or astream

## CrewAI Hierarchical
- Agents with role/goal/backstory
- Tasks with expected_output
- Hierarchical process + manager LLM
- Tools attached per agent

## Pipecat Voice Pipeline Skeleton
```python
pipeline = Pipeline([
    transport.input(),
    stt,
    user_aggregator,
    llm,          # or orchestrator call
    tts,
    transport.output(),
    assistant_aggregator,
])
```

## Docker Compose Skeleton
```yaml
services:
  orchestrator:
    build: .
    ports: ["8000:8000"]
    env_file: .env
    volumes: ["./:/app"]
  # optional: redis, postgres, ollama
```

## FastAPI + WebSocket Chat
- /ws endpoint for bidirectional streaming
- Session state per connection
- Broadcast or private multi-user rooms
