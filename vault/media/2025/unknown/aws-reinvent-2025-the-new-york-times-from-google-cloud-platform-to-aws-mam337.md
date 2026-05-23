---
clients:
- The New York Times
- Amazon Web Services
- Google
date: 2025-12-04
description: 'Discover how The New York Times overhauled its gaming platform by migrating
  critical gaming workloads from Google Cloud Platform to Amazon Web Services. Learn
  why this media giant chose to make the switch and explore the best practices that
  ensured a seamless transition of some of the internet''s most popular pages and
  games. We''ll delve into the journey from Google''s Datastore, App Engine, and GKE
  to Amazon Elastic Kubernetes Service(EKS) and Amazon DynamoDB. Uncover how this
  strategic move not '
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- cloud-migration
- aws
- gaming
- media
- gcp
- reinvent
- best-practices
thematic: media
title: 'AWS re:Invent 2025 - The New York Times: From Google Cloud Platform to AWS
  (MAM337)'
url: https://www.youtube.com/watch?v=87O2r1br_ns
video_id: 87O2r1br_ns
year: 2025
---

# AWS re:Invent 2025 - The New York Times: From Google Cloud Platform to AWS (MAM337)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=87O2r1br_ns)
> 📅 2025-12-04 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[The New York Times]] [[Amazon Web Services]] [[Google]]

# The New York Times: Migrating Gaming Workloads from Google Cloud Platform to AWS

## Overview of the Migration Initiative

The New York Times undertook a substantial cloud migration effort, transitioning its gaming platform — home to some of the internet's most heavily trafficked pages and beloved puzzles — from Google Cloud Platform to Amazon Web Services. This session, presented at AWS re:Invent 2025, walked through the strategic rationale and technical execution behind the move, offering a detailed look at how a major media organization modernized its technology stack while keeping millions of daily players engaged without disruption. The migration represented more than a simple lift-and-shift; it was a deliberate effort to consolidate infrastructure, improve operational efficiency, and align the gaming platform with the broader technology direction of the company.

## Strategic Rationale and Technical Execution

### Why The Times Chose to Switch Cloud Providers

The decision to leave Google Cloud Platform stemmed from a combination of strategic, operational, and performance considerations. The New York Times sought to unify its cloud footprint, reduce the complexity of managing workloads across multiple providers, and take advantage of AWS services that better matched its scalability and reliability requirements. By concentrating gaming workloads on AWS, the engineering teams gained access to a richer ecosystem of managed services and could leverage existing organizational expertise, ultimately lowering operational overhead and accelerating the pace at which new features could be delivered to players.

### Re-Architecting the Gaming Platform

The technical heart of the migration involved replacing several foundational Google Cloud services with AWS equivalents. Workloads previously running on Google App Engine and Google Kubernetes Engine were moved to Amazon Elastic Kubernetes Service, giving the team a consistent, container-based runtime that aligned with modern operational practices. The data layer underwent an equally significant transformation, with Google Datastore being replaced by Amazon DynamoDB to provide the low-latency, highly scalable NoSQL backbone required by games such as Wordle, Spelling Bee, and the Crossword. This re-platforming required careful attention to data modeling, since the move between NoSQL systems demanded adaptation rather than direct translation of schemas and access patterns.

### Best Practices for a Seamless Transition

To ensure that players experienced no degradation in service during the cutover, The Times adopted migration practices designed around incremental change, thorough validation, and minimal user-visible risk. Teams emphasized rigorous testing, parallel running of systems where appropriate, and careful traffic shifting to validate behavior under real load before fully committing to the new environment. The session highlighted how disciplined planning, close collaboration between platform and product engineering teams, and a strong observability posture combined to make the transition smooth despite the scale and visibility of the workloads involved.

## Outcomes and Lessons Learned

The completed migration delivered measurable improvements in performance, scalability, and operational efficiency for The New York Times' gaming platform. By standardizing on EKS and DynamoDB, the engineering organization simplified its operating model, gained better elasticity to handle traffic spikes driven by viral puzzle moments, and positioned itself to innovate more rapidly on top of a modernized foundation. The broader takeaway shared with the audience was that even mission-critical, high-traffic consumer experiences can be successfully replatformed across cloud providers when the effort is grounded in clear strategic goals, thoughtful architectural choices, and disciplined execution.