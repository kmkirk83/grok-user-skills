---
name: autonomous-ship-deploy
description: Autonomously build complete and ship code projects to free public platforms (Vercel primary Netlify fallback) so end users can interact with a live URL. Use when the user asks to ship to Vercel, deploy live, publish for users, autonomous deploy, full user interaction URL, or any request to take a code project from repo to a free public deployment without manual hosting steps.
---

# Autonomous Ship and Deploy

## Overview

End-to-end workflow that takes a GitHub or local code project through completion and deploys it to a free public URL for full user interaction. Primary target is Vercel Hobby free tier. Fallback is Netlify. Integrates the existing autonomy suite so build quality and release discipline are not sacrificed for speed.

## Skills this workflow orchestrates

| Skill | Role in ship pipeline |
|-------|------------------------|
| project-autonomy-bootstrap | Entry point; loads the full autonomy stack |
| task-decomposition-verifier | Verified plan with deploy as a first-class done criterion |
| product-delivery-swarm | Frontend plus backend completion, tests, docs, GitHub Release |
| autonomous-ai-build-playbook | Outcome contract, architecture, quality gates before ship |
| vibe-coding-maximizer | Fast production-minded implementation practices |
| background-completion-swarm | Finish stubs and TODOs before deploy |
| agent-eval-improver | Score readiness at pre-deploy gate |
| skill-gap-analyzer | Detect missing deploy capability and close it |

## Connected platforms

- Vercel: list_teams, create_git_project, create_deployment, create_project, create_project_env, get_project
- Netlify: create-new-project, deploy-site, manage-env-vars, project readers
- GitHub: repo link, tags, releases

Prefer Vercel git-linked projects so every push to main auto-deploys. Use Netlify when the stack is static-only or the user requests it.

## Done criteria (ship complete)

1. Working GUI frontend (or intentional API-only with documented playground)
2. Complete backend or serverless functions as required
3. Code on GitHub main (or agreed production branch)
4. Live public HTTPS URL on Vercel or Netlify
5. Env vars set for production (no secrets in git)
6. Optional: GitHub Release tag plus ship notes with the live URL

## Autonomous ship protocol

### Phase 1 - Ingest and plan

1. Accept repo URL, local path, or product goal.
2. Inventory stack (Next.js, Vite, React, static, API routes, Prisma, etc.).
3. Restate done criteria including live public URL.
4. Run task-decomposition-verifier; include deploy and smoke-check as terminal tasks.

### Phase 2 - Product completion

1. Apply product-delivery-swarm and background-completion-swarm until frontend and backend are functional.
2. Prefer frameworks Vercel detects well: Next.js, Vite, React, SvelteKit, Nuxt, Astro, static.
3. Ensure package.json has build and start or framework defaults.
4. No secrets in source; use .env.example only.
5. Commit and push to GitHub.

### Phase 3 - Platform selection

| Stack | Prefer |
|-------|--------|
| Next.js, React, Vite, Node serverless | Vercel |
| Pure static | Vercel or Netlify |
| User requests Netlify | Netlify |
| Heavy long-running servers | Document limitation; other free tiers only with user approval |

### Phase 4 - Deploy to Vercel (primary)

1. Call vercel list_teams or get_git_deployment_context to resolve teamId.
2. Prefer create_git_project with repo owner/name, teamId, provider github, deploy true.
3. If env vars required, create_project_env for production and preview. Never commit secrets.
4. Wait until a production or preview URL is available.
5. Smoke-check the live URL (HTTP 200, critical path loads).
6. Record URL in ship notes and optionally GitHub Release body.

### Phase 5 - Deploy to Netlify (fallback)

1. Resolve team if needed.
2. create-new-project only when the user confirms a new site (never assume).
3. Link repo or deploy-site with known siteId.
4. Manage env vars.
5. Smoke-check live URL; record in ship notes.

### Phase 6 - Ship report

- Live URL(s)
- Platform and project id
- GitHub repo and release tag if any
- What works for end users
- Remaining free-tier limits
- Next optional improvements

## Constraints and safety

- Do not create a new site when an existing linked project already exists for the repo; reuse it.
- Do not put secrets in git or chat logs.
- Do not expand product scope solely to make deploy easier.
- If GitHub Actions is billing-locked, still deploy via Vercel or Netlify git integration (their builders, not GitHub-hosted runners).
- Require explicit user approval before paid upgrades or paid custom domains.
- Prefer reversible steps; keep prior deployment history.

## Activation triggers

Activate when the user asks to ship, deploy live, publish for users, get a public URL, deploy to Vercel or Netlify, or autonomously complete a project through full user interaction on a free platform.

## Integration

Wire into project-autonomy-bootstrap and product-delivery-swarm so complete product includes a live free deployment unless the user opts out.
