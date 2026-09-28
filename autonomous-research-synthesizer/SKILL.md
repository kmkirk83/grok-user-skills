---
name: autonomous-research-synthesizer
description: Execute long-horizon multi-source research plans, score source quality, detect contradictions, and produce structured synthesis suitable for high-stakes decisions. Use when the user asks to research this thoroughly, synthesize the literature, multi-source analysis, deep dive with sources, or any request for systematic evidence collection and synthesis beyond a single search.
---

# Autonomous Research Synthesizer

## Overview

Plan and execute multi-source research with explicit source-quality scoring, contradiction detection, and confidence-tagged synthesis. Designed for high-thoroughness autonomous investigation.

## Instructions

1. Frame the research question
   - Restate the question or decision in one precise sentence.
   - Identify the required depth, time horizon, acceptable uncertainty, and any excluded sources or domains.
   - List the key claims or sub-questions that must be answered.

2. Build the research plan
   - Generate a short list of search queries and source tiers (primary literature, official reports, high-quality secondary analysis, etc.).
   - Define stopping criteria (coverage of sub-questions, saturation of new information, or resource limits).
   - Note any parallelizable collection steps.

3. Collect and score evidence
   - Retrieve material using available search and browsing tools.
   - For each significant source record:
     - Relevance to the sub-questions.
     - Credibility indicators (author expertise, publication venue, methodology transparency, potential conflicts).
     - Recency and consistency with other sources.
   - Assign a simple quality score and flag low-trust material.

4. Detect contradictions and gaps
   - Cross-check claims across sources.
   - Surface direct contradictions, unresolved tensions, and missing evidence.
   - Note where additional targeted searches are required.

5. Produce the synthesis
   - Structure the output as:
     - Executive summary with overall confidence level.
     - Answers to each sub-question with supporting evidence and confidence.
     - Explicit list of contradictions and open questions.
     - Ranked recommendations or implications if the original request asked for them.
   - Cite sources inline using the available citation mechanism.
   - Keep the synthesis concise; move exhaustive detail to an appendix only when necessary.

6. Iteration and depth control
   - If the user requests deeper coverage of a specific sub-question, expand only that branch.
   - Respect any stated limits on number of sources or time.

## Constraints

- Prefer high-quality primary and official sources over secondary commentary.
- Never present low-confidence claims as established fact.
- Do not expand the research question beyond the user’s stated scope.
- When evidence is insufficient, state the limitation clearly rather than filling gaps with speculation.
