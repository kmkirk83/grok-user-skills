---
name: agent-eval-improver
description: Define, run, and act on evaluations of agent outputs to measure thoroughness, autonomy, and effectiveness, then recommend concrete skill or process improvements. Use when the user asks to evaluate this output, score thoroughness, run agent evals, improve from failures, measure effort quality, or any request to assess and raise the quality of autonomous work.
---

# Agent Eval Improver

## Overview

Turn agent outputs into measurable signals of thoroughness, autonomy, and effectiveness. Produce failure analysis and ranked improvement proposals that feed directly into skill creation or process refinement.

## Instructions

1. Define evaluation criteria
   - Extract the original goal and any explicit success metrics supplied by the user.
   - Add standard dimensions when relevant: completeness, correctness, evidence quality, risk coverage, autonomy (degree of human intervention required), and efficiency.
   - Make every criterion observable and scorable (binary, numeric scale, or checklist).

2. Score the output
   - Apply the criteria to the concrete artifact or transcript under review.
   - Record a numeric or categorical score plus a short justification for each criterion.
   - Highlight the highest-impact failures first.

3. Perform failure analysis
   - For every low-scoring criterion identify the root cause (missing skill, weak plan, insufficient verification, tool limitation, ambiguous requirements, etc.).
   - Distinguish one-off mistakes from systematic gaps.

4. Generate improvement proposals
   - Rank proposals by expected gain in autonomy or thoroughness versus implementation cost.
   - Prefer proposals that can be realized by:
     - Updating an existing skill,
     - Creating a focused new skill (hand off to skill-creator),
     - Adding a reusable checklist or verification step,
     - Changing process order or adding a critique loop.
   - For each proposal state the expected measurable improvement.

5. Produce the report
   - Summary scores.
   - Ranked failure list with root causes.
   - Ranked improvement proposals with concrete next actions.
   - Optional one-sentence recommendation for the single highest-leverage change.

6. Iteration
   - When the user supplies a revised output, re-score only the changed portions and update the improvement list.
   - Never invent metrics the user has not endorsed.

## Constraints

- Keep scoring transparent and reproducible.
- Focus on actionable gaps rather than vague quality statements.
- Do not expand the original goal while evaluating.
