---
clients:
- Zendesk
- Datadog
- AWS
date: 2025-12-04
description: Zendesk chose Datadog for observability (APM, Log Management) to boost
  performance, resolve issues faster, and optimize infrastructure. Datadog's tools
  provided essential per-tenant visibility for their high-cardinality, multi-tenant
  platform, guiding code and infrastructure decisions. Datadog also helps Zendesk
  optimize AWS usage in real-time. This led to faster detection and resolution, fewer
  cross-tenant incidents, right-sized compute/storage, and better customer experience.
  Attendees will le
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- observability
- apm
- multi-tenant
- performance
- cloud
- aws
- monitoring
thematic: media
title: 'AWS re:Invent 2025-Finding the Noisy Neighbor: Patterns for Per‑Customer Performance
  at Scale-MAM354'
url: https://www.youtube.com/watch?v=Y2eyW6o_yV4
video_id: Y2eyW6o_yV4
year: 2025
---

# AWS re:Invent 2025-Finding the Noisy Neighbor: Patterns for Per‑Customer Performance at Scale-MAM354

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=Y2eyW6o_yV4)
> 📅 2025-12-04 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[Zendesk]] [[Datadog]] [[AWS]]

# Finding the Noisy Neighbor: Patterns for Per-Customer Performance at Scale

## Overview of the Session

This AWS re:Invent 2025 presentation, delivered by Datadog as an AWS Partner, examines how Zendesk addressed one of the most persistent challenges in multi-tenant SaaS architectures: identifying and mitigating noisy neighbors that degrade performance for individual customers. The session walks through Zendesk's observability journey, focusing on how per-tenant visibility transformed both engineering decisions and customer experience across a high-cardinality platform serving thousands of organizations on shared AWS infrastructure.

## Zendesk's Observability Strategy with Datadog

### The Multi-Tenant Visibility Challenge

Zendesk operates a complex multi-tenant platform where workloads from many customers share underlying compute, storage, and network resources. Traditional aggregate metrics obscured the fact that a single tenant could consume disproportionate resources and degrade the experience for everyone else. To resolve this, Zendesk adopted Datadog's APM and Log Management capabilities, which provided the high-cardinality dimensions needed to slice telemetry by tenant, endpoint, and service simultaneously. This per-customer granularity became the foundation for detecting noisy neighbors before they triggered widespread incidents.

### Patterns for Detection and Resolution

The presentation outlines architectural and instrumentation patterns Zendesk applied to surface tenant-level signals throughout its stack. By tagging traces, logs, and metrics with consistent tenant identifiers, engineers could correlate anomalies across layers and pinpoint which customer workloads were responsible for latency spikes, error bursts, or resource saturation. Datadog's tooling enabled the team to act on these signals quickly, whether by throttling specific tenants, refactoring hot code paths, or reshaping infrastructure allocations to better isolate workloads.

### Optimizing AWS Infrastructure in Real Time

Beyond incident response, Zendesk uses Datadog to continuously optimize its AWS footprint. Real-time visibility into how tenants consume EC2, storage, and supporting services allows the team to right-size compute and storage tiers, eliminate waste, and align capacity with actual demand patterns. This feedback loop between observability data and infrastructure decisions has produced measurable efficiency gains while supporting growth.

## Outcomes and Takeaways

### Business and Engineering Impact

The combined effect of these practices has been faster detection and resolution of performance issues, a meaningful reduction in cross-tenant incidents, more accurately sized infrastructure, and a stronger customer experience overall. Engineering teams spend less time chasing ambiguous symptoms and more time addressing root causes, while finance and platform teams benefit from infrastructure choices grounded in production telemetry rather than estimates.

### Guidance for Migration and Modernization

The session closes by extending these lessons to attendees considering similar journeys, emphasizing how pairing Datadog with AWS can de-risk migrations and accelerate modernization. The recommended approach is to instrument for tenant-level observability early, treat per-customer performance as a first-class operational metric, and use the resulting data to guide both code-level optimizations and infrastructure investments as platforms scale.