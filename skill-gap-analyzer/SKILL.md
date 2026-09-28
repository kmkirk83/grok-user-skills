---
name: skill-gap-analyzer
description: Analyze a task or goal against available skills, detect capability gaps that limit autonomy thoroughness or effectiveness, then recommend or draft the minimal new skills needed to close those gaps and complete work more automatically. Use when the user asks to find skills needed, analyze skill gaps, improve the skill set, increase effort with skills, recommend skills for autonomy, audit skills for a task, or better complete tasks by adding specialized capabilities.
---

# Skill Gap Analyzer

## Overview

Inventory current skills, extract required capabilities from a task description, identify gaps that reduce autonomy or effectiveness, and produce prioritized recommendations (with draft skill outlines) that can be handed to the skill-creator.

## Instructions

1. Inventory available skills
   - List directories under /home/workdir/.grok/skills/ and /root/.grok/skills/.
   - For each skill read only the name and description from its SKILL.md frontmatter.
   - Categorize briefly by primary capability (document generation, media processing, multi-agent orchestration, autonomous completion, domain-specific, etc.).

2. Extract required capabilities from the user task or goal
   - Identify domains, tools, workflows, decision points, error-recovery needs, parallelism, and quality criteria.
   - Note any requirements for high autonomy (minimal human intervention), thoroughness (deep coverage, verification steps), or effectiveness (speed, reliability, completeness).
   - Ignore capabilities the base model already possesses (general reasoning, coding, web search, etc.).

3. Map and detect gaps
   - Match required capabilities against the inventoried skills.
   - Flag gaps where no existing skill provides non-obvious procedural knowledge, specialized workflows, templates, or deterministic scripts.
   - Prioritize gaps that most improve autonomy, thoroughness, or success rate. Prefer a small number of focused skills over many narrow ones.

4. Produce recommendations
   - For each prioritized gap output:
     - Proposed skill name (kebab-case, 2-64 chars, matching directory rules).
     - One-line description suitable for frontmatter (plain scalar, no colon-space, no angle brackets).
     - Brief list of trigger phrases.
     - High-level instruction outline (imperative bullets) that skill-creator can expand.
     - Optional resources (scripts, references, assets) if the gap needs them.
   - Rank recommendations by estimated impact on task completion autonomy and effectiveness.
   - If the gap can be closed by extending an existing skill instead of creating a new one, note that alternative first.

5. Next actions
   - Present the analysis and recommendations clearly.
   - If the user confirms, invoke the skill-creator workflow to initialize and draft the highest-priority skills.
   - Do not create skills for knowledge the model already has or for trivial one-off procedures.

## Constraints

- Operate only on skills present in the local skill directories. Do not search external repositories or the web for third-party skills unless the user explicitly requests it.
- Keep recommendations minimal and high-impact. Prefer skills that enable broader classes of future tasks.
- Always respect the skill-creator rules for naming, description format, and content guidelines when drafting outlines.
