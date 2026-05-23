---
clients:
- Amazon
- AWS
- IAB
- GARM
- Amazon Bedrock
- AWS Elemental
date: 2025-09-29
description: Media companies and broadcasters need to monetize news content while
  avoiding poorly timed ad breaks and potentially inappropriate ad placements during
  a broadcast or live stream. The live news advertising with brand safety demonstration
  analyzes live streams in near real-time and maps content to IAB and GARM taxonomies
  to create video ad server signals that indicate ad break suitability before programmatic
  ad insertion. Powered by Amazon AI/ML services, Amazon Bedrock, AWS Elemental Media
  Servi
event: ibc-2025-demo-showcase
has_transcript: true
language: en
playlist: IBC 2025 Demo Showcase
tags:
- live
- news
- advertising
- brand-safety
- monetization
- streaming
- broadcast
thematic: media
title: Live news advertising with brand safety
url: https://www.youtube.com/watch?v=-t8TTMrU068
video_id: -t8TTMrU068
year: 2025
---

# Live news advertising with brand safety

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=-t8TTMrU068)
> 📅 2025-09-29 | 🎤 ibc-2025-demo-showcase | 🌐 en
> 🏢 Clients: [[Amazon]] [[AWS]] [[IAB]] [[GARM]] [[Amazon Bedrock]] [[AWS Elemental]]

# Live News Advertising with Brand Safety on AWS

## Overview of the Challenge

Media companies and broadcasters face a persistent dilemma when monetizing live news content. While news programming represents valuable advertising inventory, the unpredictable nature of live broadcasts creates significant risks for advertisers. Poorly timed ad breaks or inappropriate ad placements adjacent to sensitive or distressing news content can damage brand reputation and undermine advertiser confidence. As a result, substantial portions of news inventory remain unmonetized, representing a significant lost revenue opportunity for broadcasters and streaming platforms.

This AWS demonstration addresses that challenge directly by showcasing how cloud-native AI and machine learning services can analyze live streams in near real-time, classify content against industry-standard taxonomies, and generate signals that guide programmatic ad insertion decisions. The result is a system that protects advertiser brands while unlocking previously inaccessible ad inventory for media organizations.

## How the Solution Works

### Real-Time Content Analysis and Taxonomy Mapping

At the heart of the demonstration is a pipeline that ingests live news streams and analyzes them as they air. The solution leverages Amazon AI and machine learning services along with Amazon Bedrock to interpret video and audio content, then maps that content to the Interactive Advertising Bureau (IAB) and Global Alliance for Responsible Media (GARM) taxonomies. These industry-standard frameworks provide a common language for describing content categories and brand safety risk levels, allowing advertisers and publishers to align on what constitutes a safe placement.

By performing this classification with low latency, the system can produce ad break suitability signals before programmatic ad insertion occurs. This means that when a news segment covers sensitive topics, the platform can flag the upcoming ad break as unsuitable for certain advertiser categories, while clearly identifying segments where placements are safe and appropriate.

### Underlying AWS Architecture

The demonstration is built on a cohesive set of AWS services that handle ingestion, processing, storage, and visualization. AWS Elemental Media Services manage the live video workflow, handling stream ingestion and preparing content for downstream analysis and ad insertion. Amazon Bedrock and other AI/ML services perform the content classification and reasoning required to map scenes to the IAB and GARM taxonomies. Amazon S3 Tables provide structured, queryable storage for the resulting metadata and classification signals, while Amazon QuickSight delivers dashboards and analytics that allow operators to monitor inventory, brand safety performance, and revenue opportunities.

## Business Outcomes for Media Organizations

The combined effect of this architecture is that broadcasters and streaming providers can confidently offer news inventory to programmatic advertisers with transparent, automated brand safety guarantees. Advertisers receive assurance that their creatives will not appear next to content misaligned with their brand values, and publishers gain a mechanism to monetize previously unrealized inventory. By turning live news from a risk-laden environment into a measurable, taxonomy-aligned ad opportunity, the solution demonstrates a practical path for media companies to grow advertising revenue while maintaining editorial integrity and advertiser trust.