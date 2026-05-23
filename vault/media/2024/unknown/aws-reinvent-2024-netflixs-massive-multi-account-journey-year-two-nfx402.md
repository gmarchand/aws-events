---
clients:
- Netflix
- AWS
date: 2024-12-08
description: 'Two years ago, Netflix introduced the idea of decoupling AWS Identity
  and Access Management roles from applications’ underlying compute infrastructure
  in order to house those identities in workload-specific AWS accounts. This session
  will describe our approach for transparently replacing workloads’ AWS IAM identities
  without involvement from application owners, as well as the data and tools needed.
  Based on Netflix’s learnings from the past two years of implementation and migration
  work to make '
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- netflix
- iam
- cloud
- multi-account
- reinvent
- security
thematic: media
title: 'AWS re:Invent 2024 - Netflix''s massive multi-account journey: Year two (NFX402)'
url: https://www.youtube.com/watch?v=7eSZj3D9NRE
video_id: 7eSZj3D9NRE
year: 2024
---

# AWS re:Invent 2024 - Netflix's massive multi-account journey: Year two (NFX402)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=7eSZj3D9NRE)
> 📅 2024-12-08 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[Netflix]] [[AWS]]

# Netflix's Massive Multi-Account Journey: Year Two

## Overview of the Multi-Account Vision

Netflix has spent the past two years executing on an ambitious vision first introduced at AWS re:Invent: decoupling AWS Identity and Access Management (IAM) roles from the underlying compute infrastructure that runs application workloads. The core principle behind this work is that workload identities should live in dedicated, workload-specific AWS accounts rather than being tightly coupled to the EC2 instances, containers, or other compute resources that happen to execute them. By separating identity from infrastructure, Netflix aims to establish stronger isolation boundaries between workloads, reduce blast radius when security incidents occur, and create a more sustainable operating model as the company's AWS footprint continues to scale.

This session represents a progress report on that multi-year initiative, sharing both the conceptual framework Netflix has refined and the practical lessons learned from migrating real production systems. The presentation is aimed at AWS customers contemplating similar multi-account strategies, providing guidance on which capabilities to invest in early and how to quantify the risk reduction such efforts can deliver.

## Transparent Identity Replacement at Scale

### Decoupling Identity from Compute

A central theme of the session is Netflix's approach to transparently replacing workload IAM identities without requiring action from individual application owners. Rather than asking thousands of engineers to rewrite code, update configurations, or migrate their services manually, Netflix built platform-level mechanisms that swap underlying identities behind the scenes. This transparency is essential at Netflix's scale, where any migration approach requiring per-team involvement would be prohibitively slow and disruptive.

Achieving this transparency required investment in foundational tooling and data systems. Netflix needed comprehensive visibility into which workloads existed, which IAM roles they assumed, what those roles were actually permitted to do, and how those permissions were exercised in practice. Only with this rich telemetry could the platform team confidently reassign identities and create new workload-specific accounts without breaking production services. The data layer—capturing role usage, access patterns, and dependencies—proved to be just as important as the migration mechanics themselves.

### Lessons from Two Years of Migration

The presenters emphasized that the migration work surfaced practical challenges that would not have been obvious from the original architectural vision. Edge cases involving cross-account access, legacy permission patterns, and workloads with unusual identity behaviors all required careful handling. Netflix's experience suggests that organizations attempting similar journeys should expect this discovery work and plan for iterative refinement of their tooling rather than a one-shot migration.

## Recommendations and Quantified Outcomes

### Capabilities to Prioritize

Drawing on its experience, Netflix offered guidance to other AWS customers on where to focus investment. Foundational identity inventory and access analytics come first, because without understanding the current state, migrations cannot proceed safely. Automation that can perform identity swaps without application owner involvement is the next critical capability, followed by robust account provisioning and governance tooling that scales with the proliferation of workload-specific accounts. Customers who attempt to skip these foundational investments tend to find their multi-account efforts stall or generate excessive operational toil.

### Measured Risk Reduction

The session also addressed the question of return on investment by quantifying the risk reduction Netflix has achieved through this work. By placing each workload's identity in its own account, the potential blast radius of a compromised credential or misconfigured permission shrinks dramatically compared to the prior model where many workloads shared identity boundaries. This quantification helps justify continued investment and provides a template for other organizations to measure their own progress in similar initiatives.

The overall message is that multi-account strategies, while demanding significant platform engineering investment, deliver meaningful and measurable security benefits when executed with the right tooling, data, and transparency to application teams.