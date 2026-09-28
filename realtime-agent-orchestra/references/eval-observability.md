# Eval & Observability Templates

## Minimum included in every project

1. **LangSmith tracing** (or OpenTelemetry equivalent)
   - Wrap the main graph / crew with tracing.
   - Tag runs with room_id and user_id.

2. **Success-rate counter**
   - Simple in-memory or Redis counter for:
     - Tool call success / failure
     - End-to-end task completion
     - Human escalation rate

3. **Latency logging**
   - Per-node or per-agent timing.
   - p50 / p95 printed or pushed to a metrics endpoint.

4. **Feedback endpoint**
   - POST /feedback with {run_id, score, comment}
   - Store for later analysis.

## Optional advanced

- Automated eval suite using a small set of golden tasks.
- Dashboard stub (Gradio or Streamlit) that shows live success rates.
