---
name: product-delivery-swarm
description: Fully autonomous multi-agent swarm that drives a project from current state to a complete, releasable product including frontend, backend, tests, documentation, and GitHub Releases. Use when the user asks for a product delivery swarm, continue working until complete, build full product with frontend and releases, autonomous product completion, end-to-end delivery, or any request to keep working on a project until it ships a finished product.
---

# Product Delivery Swarm

## Overview

Orchestrate a persistent, high-autonomy swarm that takes a repository or project goal and drives it to a complete, shippable product. The swarm handles planning, parallel implementation (frontend + backend), continuous completion of unfinished work, testing, documentation, versioning, and GitHub Releases with minimal human intervention.

## Core Loop

1. Ingest goal and current state
   - Accept a repository URL, local path, or plain-English product goal.
   - Inventory existing code, open issues, TODOs, failing tests, and missing pieces (especially frontend and release artifacts).
   - Restate the target “done” state in measurable terms (working UI, passing tests, tagged release, deployed preview if applicable).

2. Produce a verified delivery plan
   - Apply hierarchical decomposition with explicit success criteria, verification checkpoints, and adversarial critique.
   - Separate workstreams that can run in parallel (frontend/UI, backend/API, data/models, tests/CI, documentation, release packaging).
   - Identify the minimal viable product (MVP) slice and subsequent increments toward full product.

3. Launch specialized agents
   - Prefer multi-agent orchestration (realtime-agent-orchestra patterns) for parallel streams.
   - Assign clear ownership: one agent or sub-swarm per major workstream.
   - Keep a coordinator that tracks overall progress against the plan and re-prioritizes blockers.

4. Continuous completion cycle
   - Scan for unfinished work (stubs, TODOs, failing tests, incomplete features, missing frontend screens, absent release configuration).
   - Finish items autonomously using the background-completion-swarm approach, falling back to free models when needed.
   - After each meaningful batch, run tests, fix regressions, and update the plan.
   - Prefer small, verifiable increments and commit frequently with clear messages.

5. Frontend and full-stack requirements
   - Ensure a modern, responsive frontend is present and functional (React/Next.js, Vue, Svelte, or the stack already in the repo).
   - Wire frontend to backend APIs, handle auth/state, and provide a polished user experience.
   - Include basic accessibility, loading states, and error handling unless the goal explicitly excludes them.

6. Testing, quality, and documentation
   - Maintain or expand automated tests (unit, integration, end-to-end as appropriate).
   - Keep documentation (README, API docs, architecture notes) current with the code.
   - Run the skill validation and any project-specific linters/CI as part of the loop.

7. Release preparation and execution
   - When success criteria are met, prepare a release: semantic version bump, changelog, GitHub Release with notes and assets.
   - Optionally create a pull request for review or push a tagged release directly if the user has authorized full autonomy.
   - Surface the release URL and a concise summary of what shipped.
   - When a live public URL is in scope, run autonomous-ship-deploy (Vercel primary, Netlify fallback) so end users can interact without self-hosting.

8. Progress reporting and continuation
   - After each cycle (or on a schedule), produce a short status report: completed items, remaining gaps, blockers, and next actions.
   - If the project is not yet complete, continue the loop automatically or via scheduled automation.
   - Stop only when the defined done criteria are satisfied or the user explicitly pauses the swarm.

## Integration with Existing Skills

- Use task-decomposition-verifier for the initial and any re-planning steps.
- Use background-completion-swarm patterns for the continuous finishing of stubs and incomplete features.
- Use realtime-agent-orchestra when parallel specialized agents provide clear speed or quality gains.
- Use agent-eval-improver to score progress and thoroughness at major milestones.
- Use project-autonomy-bootstrap as the entry point so the swarm activates at the start of project work.
- Use vibe-coding-maximizer practices for any rapid AI-assisted implementation.

## Constraints and Safety

- Never expand scope beyond the stated goal without explicit user approval.
- Prefer reversible changes and feature flags for risky frontend or infrastructure work.
- Require human confirmation before destructive actions (force-push, deletion of production resources, publishing to package registries) unless the user has granted full autonomy in advance.
- Keep secrets out of commits; use environment variables or GitHub Secrets.
- Respect rate limits and cost by preferring efficient models for routine completion tasks.

## Activation Triggers

Activate this skill when the user requests continued autonomous work until a complete product ships, mentions product delivery swarm, full product with frontend and releases, or similar long-horizon completion goals.
