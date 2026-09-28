# Realtime Voice Agent Options (2026)

## Pipecat (Daily)
- Python, pipeline of frame processors (audio in → STT → LLM → TTS → audio out).
- Excellent for full control, custom VAD, multi-provider (Grok Realtime, OpenAI Realtime, Cartesia, Deepgram, etc.).
- Transports: WebRTC, WebSocket, Daily, Twilio, etc.
- Multi-agent: nest pipelines or use with LangGraph.
- Strength: lowest-level control, great for complex voice+tool loops.

## LiveKit Agents
- Built on LiveKit WebRTC SFU.
- Native multi-participant rooms, telephony (SIP), video.
- Python + Node SDKs.
- Strength: production media infrastructure + agent layer in one.

## OpenAI Realtime API / Grok Voice Agent
- Direct model-native realtime (audio in/out, tool calling, VAD built-in).
- Lowest latency for single-agent voice.
- Pair with orchestration layer for multi-agent.

## Recommended Hybrid
Use Pipecat or LiveKit as the voice transport layer, hand off complex reasoning/tool use to a LangGraph or CrewAI orchestrator via function calls or A2A.
