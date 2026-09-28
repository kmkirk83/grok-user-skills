# Rough Cost Estimator (order-of-magnitude)

Even when the user has no budget limits, always surface approximate costs so they know what they are burning.

## Typical ranges (2026)

- Strong LLM (Grok / Claude / GPT-4o class): $0.50 – $5 per 1M input tokens, $1.5 – $15 per 1M output
- Voice (Deepgram + Cartesia or equivalent): $0.005 – $0.03 per minute
- Browser cloud hours: $0.02 – $0.10 per browser-hour
- Modal / Railway / Fly: free tier covers light testing; production usually $5–50 / month for a small always-on service

## How to present

For each option give a one-line estimate:
"Rough cost for 100 interactive turns + 30 min voice: ~$X LLM + $Y voice + $Z infra"
