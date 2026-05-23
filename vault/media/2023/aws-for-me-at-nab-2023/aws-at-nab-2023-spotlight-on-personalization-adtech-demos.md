---
clients:
- AWS
- Amazon
date: 2023-05-11
description: At NAB Show 2023, AWS demonstrated AI/ML use cases for M&E, including
  applications for Amazon Personalize. Content personalization for D2C platforms can
  create tailored experiences for customers through the use of business rules. Rules
  make it easy to customize content, personalize recommendations, and display to users
  what is of most interest to them. This demo spotlight also includes an explanation
  of AWS Clean Rooms for multi-party, privacy-enhanced data collaboration for advertising
  applicat
event: aws-for-me-at-nab-2023
has_transcript: true
language: en
playlist: AWS for M&E at NAB 2023
tags:
- ai
- machine-learning
- personalization
- adtech
- streaming
- d2c
- media-entertainment
thematic: media
title: 'AWS at NAB 2023: Spotlight on Personalization & AdTech Demos'
url: https://www.youtube.com/watch?v=Pov1G26SwEg
video_id: Pov1G26SwEg
year: 2023
---

# AWS at NAB 2023: Spotlight on Personalization & AdTech Demos

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=Pov1G26SwEg)
> 📅 2023-05-11 | 🎤 aws-for-me-at-nab-2023 | 🌐 en
> 🏢 Clients: [[AWS]] [[Amazon]]

# AWS at NAB 2023: AI/ML and AdTech Solutions for Media & Entertainment

## Personalization for Media and Entertainment

Alex Burklow opened the presentation by demonstrating Amazon Personalize, a service designed to deliver tailored experiences across direct-to-consumer websites. The service powers user personalization and similar-items recommendations while allowing business rules to govern what content surfaces to viewers. A recently released capability, personalized promotions, enables companies to prescribe that a defined percentage of recommendations feature promoted titles. Although these items are intentionally elevated within the dataset, their ordering remains personalized per user, blending business priorities with individual relevance.

### Handling Limited Interaction Data Through Knowledge Graphs

For free, ad-supported platforms or scenarios where user-item interaction data is unavailable, AWS offers an alternative approach centered on item similarity. Amazon Neptune stores a knowledge graph of the content catalog, capturing dimensions such as cast, director, location, and genre—using IMDb data in this demonstration. Neptune ML then generates compressed embeddings from these relationships, which are loaded into Amazon OpenSearch. Algorithms such as k-nearest neighbor allow rapid similarity searches, enabling recommendations and catalog search even when a desired title does not exist in the dataset. The visualization showed how a title like *The White Tiger* connects to celebrities and contextual attributes within the graph, all of which feed the embedding-based comparison.

## AWS Clean Rooms for AdTech Collaboration

Michael Santana, Senior Solutions Architect, then introduced AWS Clean Rooms, a data collaboration service that moves beyond traditional one-to-one data sharing. The service enables multi-party collaboration where each participant's data remains in place, with compute brought to the data to preserve privacy. Within media and entertainment, the primary use cases include attribution-based measurement across publishers to evaluate advertising effectiveness, third-party enrichment of first-party data with demographic insights, and reach-and-frequency analysis to understand exposure to specific creatives.

### Architecture and Governance Controls

The architecture supports any number of collaborators who associate tables and define analysis rules governing which columns participate and which aggregations—such as counts or sums—are permitted. Output constraints add another protective layer, allowing data owners to enforce minimum thresholds of unique identifiers in query results, preventing overly granular outputs. Authorized collaborators execute queries whose results land in Amazon S3, where they can flow into downstream services such as SageMaker for machine learning or other business intelligence tools.

## Media Replay Engine for Automated Highlight Generation

The second solution, the Media Replay Engine, is a fully serverless intelligent segmentation and auto-clip highlight generator that scales automatically with utilization. It addresses catch-up highlights for viewers joining live events midway, post-game summaries condensing key actions, and personalized highlights aligned with fan preferences. Beyond sports, applications extend to topical news segmentation and award-show programming.

### Segmentation and Feature Enrichment

The engine integrates with both live and video-on-demand content and operates through two core components. Segmentation identifies scenes across keyframes, while feature-based enrichment ensures that segments preserve contextual elements like commentator contributions and account for dynamic camera angle changes. The system supports both third-party plugins and first-party machine learning models. The output consists of clips and highlights that video editors or QA analysts can refine, dramatically reducing the time required for highlight identification and curation before activation across direct-to-consumer and broadcast endpoints.