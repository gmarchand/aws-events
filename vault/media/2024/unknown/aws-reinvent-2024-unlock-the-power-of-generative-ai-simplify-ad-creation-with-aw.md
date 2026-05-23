---
clients:
- AWS
- Amazon Ads
- Amazon Bedrock
- Amazon SageMaker
date: 2024-12-05
description: In this insightful session, Amazon Ads experts unveil how they leverage
  AWS technologies to unlock generative AI’s full potential, revolutionizing the advertising
  creative process. Discover how Amazon Ads generates millions of images, videos,
  and ads across multiple channels, drastically simplifying the experience of building
  advertising campaigns. Learn about cutting-edge AWS services, including Amazon Bedrock,
  Amazon SageMaker, and serverless compute, that enable advertisers to create ads
  cost
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- generative-ai
- advertising
- aws
- cloud
- creative
- video
- re-invent
thematic: media
title: 'AWS re:Invent 2024 - Unlock the power of generative AI: Simplify ad creation
  with AWS (AMZ303)'
url: https://www.youtube.com/watch?v=1t8tlKDZeA0
video_id: 1t8tlKDZeA0
year: 2024
---

# AWS re:Invent 2024 - Unlock the power of generative AI: Simplify ad creation with AWS (AMZ303)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=1t8tlKDZeA0)
> 📅 2024-12-05 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[AWS]] [[Amazon Ads]] [[Amazon Bedrock]] [[Amazon SageMaker]]

# Unlocking the Power of Generative AI: Simplifying Ad Creation with AWS

## Session Overview

At AWS re:Invent 2024, Amazon Ads experts presented how they harness generative AI on AWS to transform the advertising creative process. The session explored how Amazon Ads produces millions of images, videos, and complete ad units across multiple channels, dramatically simplifying campaign creation for advertisers of every size. By combining advanced foundation models with scalable AWS infrastructure, Amazon Ads has reduced the time, cost, and creative expertise required to launch high-performing campaigns, enabling advertisers to generate compelling assets in seconds rather than days or weeks.

## Reimagining the Creative Process with Generative AI

### From Manual Production to AI-Assisted Creativity

Traditional ad creation has long demanded specialized design skills, expensive production resources, and extended turnaround times—barriers that disproportionately affect small and mid-sized advertisers. Amazon Ads addresses these challenges by embedding generative AI directly into the campaign-building experience. Advertisers can now produce lifestyle imagery, video content, and channel-specific creative variants from simple product inputs and text prompts. This shift moves the creative workflow from a resource-intensive production model to an iterative, prompt-driven one in which advertisers explore many creative directions quickly and select the variants most likely to resonate with their target audiences.

### Scaling Across Channels and Formats

Because Amazon Ads serves campaigns across diverse surfaces—including streaming TV, display, sponsored placements, and partner publishers—the generative AI system is designed to produce assets tailored to each channel's specifications and creative conventions. The platform automatically adapts dimensions, focal points, and messaging style, allowing a single creative concept to be deployed coherently across the customer journey without requiring advertisers to manage each variation manually.

## The AWS Architecture Powering Ad Generation

### Foundation Models with Amazon Bedrock and Amazon SageMaker

The technical backbone of the solution combines Amazon Bedrock for access to leading foundation models with Amazon SageMaker for custom model training, fine-tuning, and specialized inference workloads. This pairing gives Amazon Ads flexibility to use general-purpose models where appropriate while customizing models for advertising-specific tasks such as product preservation, brand-safe imagery, and high-fidelity composition. The team highlighted the importance of evaluating multiple models, selecting the right model for each step in the generation pipeline, and continuously benchmarking quality, latency, and cost.

### Serverless Compute and Cost-Efficient Inference

To serve thousands of advertisers cost-effectively at scale, Amazon Ads relies heavily on serverless compute and optimized inference patterns. The architecture decouples request orchestration from heavy GPU inference, batches workloads where possible, and uses asynchronous pipelines for long-running generation tasks such as video synthesis. Best practices shared in the session emphasized caching intermediate artifacts, reusing embeddings, applying model distillation and quantization to reduce inference cost, and right-sizing accelerators based on traffic patterns. These optimizations allow the system to deliver creative outputs in seconds while maintaining a sustainable unit economics profile.

### Quality, Safety, and Continuous Improvement

The presenters underscored that generation quality alone is not sufficient—outputs must also meet brand-safety, policy, and trust requirements. The pipeline therefore integrates automated evaluation, content moderation, and human-in-the-loop review for higher-risk scenarios. Telemetry from advertiser interactions, such as which generated variants are selected or edited, feeds back into model improvement cycles, creating a continuous learning loop that progressively raises the relevance and performance of generated assets.

## Lessons Learned and Outcomes

### Practical Guidance for Builders

Drawing on lessons from research and production deployment, the speakers offered practical guidance for teams building similar generative AI systems. Successful programs start from clearly defined customer problems rather than model capabilities, invest early in robust evaluation frameworks, and treat prompt engineering and data curation as first-class engineering disciplines. They also recommended designing for model swapability from day one, since the foundation model landscape evolves rapidly and the ability to adopt better models without re-architecting the platform is a major competitive advantage.

### Impact on Advertisers and the Road Ahead

The combined effect of these capabilities is a meaningful reduction in the barrier to entry for advertising creative, enabling more sellers and brands to participate in sophisticated campaigns across Amazon's surfaces. Looking forward, Amazon Ads plans to deepen multimodal generation—particularly in video—expand personalization at the creative level, and continue refining the balance of automation and advertiser control, ensuring that generative AI augments rather than replaces the strategic and brand judgment that advertisers bring to their campaigns.