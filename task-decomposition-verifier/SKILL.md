---
name: task-decomposition-verifier
description: Perform rigorous hierarchical task decomposition followed by multi-stage verification and adversarial critique so that complex work is completed with maximal thoroughness and minimal human intervention. Use when the user asks to decompose this task, verify plan thoroughly, increase effort on this, add critique loops, make the plan bulletproof, or any request for systematic breakdown plus verification of complex goals.
---

# Task Decomposition Verifier

## Overview

Convert a high-level goal into a hierarchical, verifiable plan with explicit success criteria, intermediate checkpoints, evidence requirements, and adversarial critique. The resulting plan maximizes thoroughness and autonomy.

## Instructions

1. Clarify the goal
   - Restate the objective in one precise sentence.
   - Identify constraints, success metrics, risk tolerance, and any non-negotiable requirements.
   - Note assumptions that must be validated.

2. Hierarchical decomposition
   - Break the goal into 3–7 top-level phases.
   - Expand each phase into atomic, independently verifiable sub-tasks.
   - For every sub-task record:
     - Clear success criteria (observable and measurable).
     - Required inputs and expected outputs.
     - Estimated effort and dependencies.
   - Prefer the smallest number of sub-tasks that still achieve complete coverage.

3. Insert verification checkpoints
   - After every critical sub-task or phase add an explicit verification step.
   - Specify the evidence that must be produced (logs, test results, diffs, screenshots, metrics).
   - Define pass/fail thresholds.

4. Adversarial critique
   - For the complete plan list the most likely failure modes, edge cases, and hidden assumptions.
   - Propose concrete mitigations or additional sub-tasks for each high-impact risk.
   - Identify points where human review is still advisable versus fully automatable.

5. Produce the executable plan
   - Output a numbered, dependency-ordered list of sub-tasks with success criteria and verification steps.
   - Include rollback or contingency actions for high-risk steps.
   - Mark any sub-tasks that can run in parallel.
   - End with a short effort-multiplier summary explaining how the plan raises thoroughness and autonomy relative to a naive approach.

6. Iteration
   - If the user provides feedback or new constraints, revise only the affected portions and re-run the critique.
   - Never expand scope beyond what is required for the stated goal.

## Constraints

- Keep plans concise and actionable. Avoid unnecessary hierarchy.
- Success criteria must be observable without subjective judgment whenever possible.
- Do not invent requirements the user did not state.
