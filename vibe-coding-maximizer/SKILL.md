---
name: vibe-coding-maximizer
description: Apply the proven practices of top developers for building production-quality apps with vibe coding and for promoting AI products or tools. Use when the user mentions vibe coding, building apps with AI agents, maximizing effectiveness with AI coding tools, promoting an AI product, launching an AI tool, or any request to follow elite developer workflows for rapid yet reliable AI-assisted development and distribution.
---

# Vibe Coding Maximizer

## Overview

Encode the high-leverage practices used by effective developers who ship reliable products via vibe coding while successfully promoting AI applications and tools. Combine rigorous specification, small-increment execution, human architectural ownership, automated verification, and demo-first technical distribution.

## Building Apps with Vibe Coding

1. Specify before generating
   - Require a concise product requirements document or one-page specification that includes the problem, target users, core data model, key user flows, constraints, and explicit acceptance criteria.
   - Refuse to generate substantial code until success criteria are observable and measurable.
   - Prefer acceptance criteria written as testable outcomes over vague goals.

2. Establish project foundations first
   - Ensure a single-command build, test, and lint pipeline exists before feature work begins.
   - Create or maintain persistent context files (rules files such as .cursorrules, CLAUDE.md, or project equivalents) that encode architecture decisions, design system, coding standards, and domain constraints.
   - Prime the AI with relevant files or architecture summaries at the start of each significant session.

3. Execute in small verifiable increments
   - Break work into atomic steps. For each step apply a Research-Plan-Implement cycle.
   - Require the agent to propose a numbered plan of intended file changes and obtain approval before writing code.
   - Implement, test, and commit one increment at a time. Avoid large single prompts that attempt entire features.

4. Maintain human ownership of critical decisions
   - Keep architecture, security boundaries, authentication, data validation, financial logic, and compliance decisions under explicit human control.
   - Treat the AI as a capable junior developer or intern. Review every substantial diff for correctness, security, and maintainability.
   - Encode each fixed bug or lesson as a permanent rule or note in the project context files.

5. Enforce automated verification
   - Generate or write high-level acceptance or end-to-end tests early and run them after every meaningful change.
   - Require small commits with clear messages that explain why the change was made.
   - Integrate secret scanning, type checking, and continuous integration as non-negotiable gates.

6. Select tools by context
   - Recommend or use Cursor or Claude Code for deep multi-file work and existing codebases.
   - Prefer Lovable, Bolt, Replit Agent, or similar for rapid visual prototypes when speed of feedback is paramount.
   - Support hybrid flows that prototype in a visual agent tool then refine in an AI-native IDE.

## Promoting AI Products and Tools

1. Lead with concrete demonstration
   - Prioritize creation of a 30-60 second demo video or runnable sandbox that shows a surprising, specific capability.
   - Make the path from landing page or repository to first useful result as short as possible (ideally one command or one click).

2. Publish honest technical evidence
   - Produce benchmarks that include both wins and losses versus relevant competitors.
   - Prefer architecture write-ups, failure analyses, and reproducible evaluation harnesses over marketing language.
   - Frame the product around a specific job-to-be-done rather than generic AI claims.

3. Distribute through high-signal technical channels
   - Coordinate Product Hunt launches with Hacker News Show HN posts and short demo clips on X.
   - Seed thoughtful contributions in relevant Discord communities and subreddits without pure self-promotion.
   - Target AI-focused newsletters for sponsorship or organic features when the product is ready for broader reach.

4. Lower friction and build in public
   - Provide an open-source component, generous free tier, or immediately runnable example.
   - Share technical progress, decisions, and real metrics publicly to attract early technical users.
   - Sequence launches carefully — prepare assets, warm audiences, then execute a concentrated launch day followed by deeper technical follow-up content.

## Integration Rules

- When both building and promoting are in scope, apply the building practices first to produce a reliable demo artifact, then apply the promotion practices to that artifact.
- Default to high thoroughness unless the user explicitly requests pure speed.
- Surface any conflict between rapid vibe-coding velocity and production readiness; recommend the safer path for anything touching authentication, money, personal data, or long-term maintenance.
- Reference the individual specialized skills (task-decomposition-verifier, agent-eval-improver, etc.) when deeper planning, evaluation, or research is required.
