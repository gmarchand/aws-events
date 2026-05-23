---
clients:
- AWS
- Decile
- Snowflake
- Shopify
- Acxiom
- Luma AI
date: 2025-12-02
description: The future of e-commerce demands instant, data-driven decisions. Discover
  how Decile, an e-commerce analytics platform, built its Luma AI analyst into its
  service using Snowflake Intelligence. Learn how Decile built a multi-tenant architecture
  to create custom agents for each brand. Decile unifies client data (from Shopify,
  Acxiom, and more) and enables users from marketers to executives to ask complex
  business questions in natural language. Luma immediately unlocks insights previously
  trapped b
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- ai
- ecommerce
- analytics
- snowflake
- multi-tenant
- aws
- data
thematic: media
title: AWS re:Invent 2025 - Accelerating E-commerce Insights with Snowflake Intelligence
  (AIM113)
url: https://www.youtube.com/watch?v=DxWKG1HTgeE
video_id: DxWKG1HTgeE
year: 2025
---

# AWS re:Invent 2025 - Accelerating E-commerce Insights with Snowflake Intelligence (AIM113)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=DxWKG1HTgeE)
> 📅 2025-12-02 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[AWS]] [[Decile]] [[Snowflake]] [[Shopify]] [[Acxiom]] [[Luma AI]]

# Accelerating E-commerce Insights with Snowflake Intelligence

## Overview of the Session

At AWS re:Invent 2025, Snowflake presented a session highlighting how Decile, a specialized e-commerce analytics platform, transformed the way brands interact with their data by embedding a conversational AI analyst named Luma directly into its service. Built on top of Snowflake Intelligence, Luma represents a shift away from static dashboards and predefined BI reports toward natural language exploration of complex business data. The presentation focused on the architectural decisions, integration patterns, and tangible business outcomes that enable e-commerce leaders to make instant, data-driven decisions in an increasingly competitive marketplace.

## Building Luma AI on Snowflake Intelligence

### Unifying Fragmented E-commerce Data

The foundation of Decile's value proposition lies in consolidating data from disparate sources that e-commerce brands typically rely on, including Shopify for transactional and storefront data, Acxiom for enriched consumer attributes, and various marketing, advertising, and customer service platforms. By bringing these sources together into a unified data layer within Snowflake, Decile establishes a single source of truth for each brand. This unification is essential because meaningful e-commerce insights — such as customer lifetime value, cohort behavior, and channel attribution — require joining signals across systems that historically operate in silos. With the data centralized and modeled consistently, Luma can answer cross-domain questions that previously required analysts to manually stitch reports together.

### Designing a Multi-Tenant Agent Architecture

A central technical theme of the session was Decile's multi-tenant architecture, which provisions custom AI agents tailored to each brand. Rather than offering a single generic assistant, Decile uses Snowflake Intelligence to create per-tenant agents that understand the specific schemas, metrics definitions, product catalogs, and business vocabulary of each client. This approach ensures that when a marketer at one brand asks about "repeat purchase rate" or "VIP customers," the agent interprets those terms in the context of that brand's data model and definitions. The multi-tenant design also addresses data isolation and governance, leveraging Snowflake's native security boundaries so that each brand's information remains protected while still benefiting from a shared platform of capabilities.

### Natural Language Access for Diverse Users

Luma is designed to serve a wide spectrum of users, from frontline marketers running campaigns to executives setting strategy. By accepting natural language questions, the assistant removes the technical barrier that traditionally limited deep data exploration to analysts and BI specialists. Users can ask complex business questions — about customer segmentation, channel performance, retention trends, or product mix — and receive immediate answers grounded in their own data. This democratization of insight changes the rhythm of decision-making, allowing teams to iterate on questions in real time rather than waiting on report cycles.

## Business Outcomes and Strategic Impact

### Unlocking Insights Previously Trapped in Reports

A key outcome highlighted in the presentation is that Luma surfaces insights that previously remained hidden behind static BI dashboards or required custom analyst engagements to extract. Because the agent can traverse the unified data model dynamically, it answers ad hoc questions that no predefined report anticipated. This capability not only saves significant time for clients but also expands the range of decisions that can be informed by data, including nuanced inquiries that brands previously would not have prioritized due to the cost and delay of custom analysis.

### Transforming How E-commerce Leaders Work with Data

The broader strategic message of the session is that embedded conversational AI, when grounded in well-governed and unified data, fundamentally changes the relationship between business leaders and their analytics. Instead of consuming pre-packaged metrics, executives and operators engage in a dialogue with their data. Decile's implementation on Snowflake Intelligence demonstrates a replicable pattern for SaaS providers: unify customer data, define clear semantic models, deploy tenant-specific agents, and expose them through a natural language interface to deliver immediate, contextual, and trustworthy insights at scale.