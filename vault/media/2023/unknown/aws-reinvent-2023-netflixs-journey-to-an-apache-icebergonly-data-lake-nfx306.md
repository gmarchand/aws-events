---
clients:
- Netflix
- AWS
- Apache
date: 2023-12-05
description: Netflix operates a data lake of approximately one exabyte. Despite this,
  a portion of data (about 300 petabytes) remained in the legacy Apache Hive table
  format. Motivated by the well-known benefits Apache Iceberg provides, such as time
  travel and schema evolution, Netflix fully phased out Hive and transitioned existing
  data to Iceberg. In this session, learn how Netflix managed this task at the appropriate
  scale with custom tooling and how they developed unique in-house features like secure
  Ice
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- data-lake
- apache-iceberg
- apache-hive
- netflix
- aws
- migration
- big-data
thematic: media
title: AWS re:Invent 2023 - Netflix’s journey to an Apache Iceberg–only data lake
  (NFX306)
url: https://www.youtube.com/watch?v=jMFMEk8jFu8
video_id: jMFMEk8jFu8
year: 2023
---

# AWS re:Invent 2023 - Netflix’s journey to an Apache Iceberg–only data lake (NFX306)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=jMFMEk8jFu8)
> 📅 2023-12-05 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[Netflix]] [[AWS]] [[Apache]]

# Netflix's Journey to an Apache Iceberg–Only Data Lake

## Overview of Netflix's Data Lake Transformation

Netflix operates one of the largest data lakes in the world, comprising roughly one exabyte of data that powers analytics, recommendations, and operational decision-making across the streaming giant's business. For years, a substantial portion of this data—approximately 300 petabytes—remained locked in the legacy Apache Hive table format, even as the broader industry began shifting toward more modern table formats. Recognizing the limitations of Hive and the substantial advantages offered by Apache Iceberg, Netflix embarked on an ambitious initiative to fully retire Hive and consolidate its entire data warehouse on Iceberg. This session details how the company executed that migration at scale, the custom tooling it built along the way, and the in-house innovations that emerged from the effort.

## Motivations and Strategic Drivers

### Why Iceberg Over Hive

The decision to abandon Hive was driven by Iceberg's well-documented technical advantages, which directly addressed long-standing pain points Netflix engineers experienced when working with Hive tables. Iceberg provides robust schema evolution, allowing data teams to modify table structures without rewriting underlying data or breaking downstream consumers. Time travel capabilities give analysts and engineers the ability to query historical snapshots of data, simplifying debugging, auditing, and reproducible analytics. Iceberg also delivers stronger transactional guarantees, better performance through advanced metadata handling, and hidden partitioning that eliminates many of the operational headaches associated with Hive's directory-based partitioning model. Together, these benefits made Iceberg an obvious strategic choice for a company whose business depends on reliable, large-scale data processing.

## Executing the Migration at Scale

### Custom Tooling for a Massive Transition

Migrating 300 petabytes of production data while keeping pipelines, dashboards, and machine learning workloads running was not a task that could be accomplished with off-the-shelf utilities. Netflix invested in custom tooling specifically designed to automate and orchestrate the conversion of Hive tables to Iceberg at scale. This tooling handled the mechanics of rewriting metadata, validating data integrity, and coordinating cutovers so that consumers of the data experienced minimal disruption. By systematizing the migration process, Netflix was able to retire Hive completely rather than letting legacy formats linger indefinitely, which is a common failure mode in large enterprise data platforms.

### Overcoming Transition Challenges

The journey was not without significant obstacles. Coordinating the migration across countless tables, pipelines, and teams required careful planning to avoid breaking dependent workloads. Compatibility concerns, performance regressions, and the sheer operational complexity of moving exabyte-scale data all had to be managed thoughtfully. Netflix's approach emphasized incremental progress, automated validation, and close collaboration with internal data consumers to ensure that the transition delivered real value rather than simply trading one set of problems for another.

## In-House Innovations Built Along the Way

### Secure Iceberg Tables

One notable innovation Netflix developed during this journey is the concept of secure Iceberg tables. As data governance, privacy regulations, and internal access controls have grown more demanding, the company recognized the need for a table-level security model that integrates natively with Iceberg. Secure Iceberg tables allow Netflix to enforce fine-grained access policies on sensitive data while preserving the performance and flexibility that Iceberg provides, addressing a gap that existed in the open-source ecosystem.

### The Iceberg REST Catalog

Netflix also contributed to and helped pioneer the Iceberg REST catalog, a service-oriented approach to catalog management that decouples clients from the underlying metastore implementation. This architecture simplifies client integration, improves security by centralizing access control, and makes it easier to evolve catalog capabilities without forcing every consumer to upgrade in lockstep. The REST catalog has become a meaningful contribution to the broader Iceberg community and reflects Netflix's commitment to advancing open standards.

## Outcomes and Takeaways

By committing to a complete migration rather than a partial modernization, Netflix unified its data warehouse on a single, modern table format, eliminating the operational overhead of supporting two systems and unlocking Iceberg's full feature set across all data assets. The custom tooling, secure table implementation, and REST catalog work demonstrate how a determined engineering organization can not only adopt a new technology at exabyte scale but also extend it to meet enterprise requirements. For other organizations contemplating similar migrations, Netflix's experience underscores the importance of investing in automation, planning for security and governance from the outset, and treating large-scale format transitions as a strategic priority rather than a perpetual side project.