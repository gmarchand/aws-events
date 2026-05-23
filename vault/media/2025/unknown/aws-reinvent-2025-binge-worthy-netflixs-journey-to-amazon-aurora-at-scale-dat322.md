---
clients:
- Netflix
- AWS
- Amazon Aurora
- Amazon
date: 2025-12-02
description: In this session, learn how Netflix successfully orchestrated the migration
  of terabytes of mission-critical data across 100+ clusters to Amazon Aurora while
  ensuring continuous service for millions of global subscribers. Through a detailed
  examination of their innovative approach combining AWS Database Migration Service
  and Netflix's proprietary Data Streaming Platform, explore how they achieved near-zero
  downtime and maintained data integrity throughout this complex transition. Technical
  leader
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- aurora
- netflix
- database-migration
- streaming
- cloud-migration
- re-invent
thematic: media
title: 'AWS re:Invent 2025 - Binge-worthy: Netflix''s journey to Amazon Aurora at
  scale (DAT322)'
url: https://www.youtube.com/watch?v=cxXG5fZ5wik
video_id: cxXG5fZ5wik
year: 2025
---

# AWS re:Invent 2025 - Binge-worthy: Netflix's journey to Amazon Aurora at scale (DAT322)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=cxXG5fZ5wik)
> 📅 2025-12-02 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[Netflix]] [[AWS]] [[Amazon Aurora]] [[Amazon]]

# Netflix's Journey to Amazon Aurora at Scale

## Overview of the Migration Initiative

Netflix undertook one of its most ambitious database modernization efforts to date, migrating terabytes of mission-critical data across more than 100 clusters to Amazon Aurora. The session details how the streaming giant orchestrated this transition while continuing to serve millions of subscribers worldwide without disruption. The migration was driven by the need for greater scalability, improved performance, and operational efficiency, all while preserving the rigorous reliability standards Netflix's global audience expects. Achieving near-zero downtime across such a vast and varied database fleet required a carefully engineered strategy that balanced speed, safety, and data integrity.

## Architecting a Migration at Netflix Scale

### Combining AWS DMS with Netflix's Data Streaming Platform

At the core of Netflix's approach was a hybrid architecture that paired AWS Database Migration Service (DMS) with the company's proprietary Data Streaming Platform. DMS handled the heavy lifting of bulk data transfer and ongoing change data capture between source databases and Aurora targets, while Netflix's internal streaming infrastructure provided the flexibility needed to handle edge cases, custom transformations, and the unique operational patterns of its services. This combination allowed engineering teams to synchronize data continuously, validate consistency in real time, and cut over workloads with minimal impact on end users. By leveraging both managed AWS tooling and purpose-built internal systems, Netflix avoided the limitations of any single solution and tailored the migration pipeline to the demands of each cluster.

### Ensuring Data Integrity and Near-Zero Downtime

Maintaining data integrity throughout the transition was treated as a non-negotiable requirement. Netflix implemented validation layers that compared source and target datasets at multiple stages of the migration, catching discrepancies before they could affect production traffic. The team designed cutover procedures that minimized service interruption, leveraging dual-write patterns, replication lag monitoring, and automated rollback capabilities to protect against unforeseen issues. These practices enabled the migration of even the most sensitive workloads without measurable degradation in customer experience.

### Managing Risk Across More Than 100 Clusters

Operating at this scale introduced significant risk management challenges, since each cluster carried distinct schemas, traffic patterns, and dependencies. Netflix addressed this by standardizing migration playbooks, automating repetitive steps, and creating observability tooling that gave engineers clear visibility into the health of each migration in flight. Teams progressively migrated clusters in waves, applying lessons learned from earlier moves to refine the process for subsequent ones. This iterative approach allowed Netflix to scale the migration effort efficiently while containing the blast radius of any individual issue.

## Key Takeaways for Database Modernization

The session closes with practical guidance for technical leaders contemplating similar journeys. Netflix's experience underscores the value of combining managed AWS services with internal platforms to address scale-specific challenges, the importance of investing heavily in validation and observability, and the benefits of treating migration as a repeatable engineering discipline rather than a one-time project. Organizations planning their own moves to Aurora can draw on these insights to architect migrations that are safe, efficient, and well-suited to the realities of running mission-critical workloads in the cloud.