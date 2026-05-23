---
clients:
- Rovio
- AWS
- Anthropic
date: 2025-12-07
description: Explore how Rovio, the creator of Angry Birds, is reimagining game asset
  creation using AWS’s generative AI services. Learn how they built a custom image
  generation pipeline using SageMaker Training Jobs, EC2 g6e instances, and SageMaker
  Endpoints to accelerate content creation while preserving brand identity. The session
  will also highlight how Rovio uses Amazon Bedrock and Claude in adjacent creative
  workflows. With real examples from Angry Birds Dream Blast, discover how Rovio balances
  creati
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- genai
- gaming
- aws
- sagemaker
- ec2
- image-generation
- cloud
thematic: media
title: 'AWS re:Invent 2025 - Angry Birds Meets GenAI: Transforming Rovio''s Asset
  Creation with AWS (IND398)'
url: https://www.youtube.com/watch?v=ZDrqhVSY9Mc
video_id: ZDrqhVSY9Mc
year: 2025
---

# AWS re:Invent 2025 - Angry Birds Meets GenAI: Transforming Rovio's Asset Creation with AWS (IND398)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=ZDrqhVSY9Mc)
> 📅 2025-12-07 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[Rovio]] [[AWS]] [[Anthropic]]

# Angry Birds Meets GenAI: Transforming Rovio's Asset Creation with AWS

## Reimagining Game Content Production Through Generative AI

Rovio, the studio behind the globally recognized Angry Birds franchise, is fundamentally rethinking how game assets are created by leveraging the generative AI capabilities offered through Amazon Web Services. As live-service mobile games demand a continuous stream of fresh, high-quality visual content, traditional manual asset production pipelines struggle to keep pace with player expectations and release cadences. To address this challenge, Rovio partnered with AWS to design a generative AI strategy that accelerates content creation while safeguarding the distinctive visual identity that has defined the Angry Birds brand for more than a decade.

The session showcases how Rovio combines multiple AWS services into a cohesive pipeline that supports both fully automated and human-in-the-loop creative workflows. Rather than relying on a single off-the-shelf model, the studio adopts a multi-service approach that lets each component of the pipeline contribute its specialized strengths, ranging from custom-trained image models to large language models for ideation, prompt engineering, and metadata enrichment.

## Building a Custom Image Generation Pipeline on AWS

### Training, Hosting, and Scaling Brand-Aligned Models

At the heart of Rovio's solution is a custom image generation pipeline built on Amazon SageMaker. The team uses SageMaker Training Jobs to fine-tune image models on curated datasets of Angry Birds artwork, ensuring that generated outputs faithfully reflect the franchise's signature characters, color palettes, and stylistic conventions. Training workloads run on Amazon EC2 g6e instances, which provide the GPU performance needed to iterate quickly on model variants without incurring the overhead of managing dedicated infrastructure.

Once models reach production quality, Rovio deploys them behind SageMaker Endpoints, giving artists and automated systems on-demand access to inference. This architecture allows the studio to scale generation capacity elastically in response to production peaks, while keeping costs aligned with actual usage. The endpoint-based design also makes it straightforward to roll out updated model versions, run A/B comparisons, and integrate the generation service into existing creative tools used by Rovio's art teams.

### Extending Creativity with Amazon Bedrock and Claude

Beyond image generation, Rovio incorporates Amazon Bedrock and Anthropic's Claude into adjacent creative workflows. These foundation models support tasks such as concept brainstorming, prompt refinement, narrative generation, and quality review of generated assets. By coupling a purpose-built image model with general-purpose language models accessed through Bedrock, Rovio creates an end-to-end creative loop where ideas can be expressed in natural language, translated into precise generation prompts, rendered visually, and then evaluated or iterated upon.

## Lessons from Angry Birds Dream Blast and the Path Forward

### Balancing Creative Control, Scale, and Brand Integrity

Real-world examples from Angry Birds Dream Blast illustrate how the pipeline delivers tangible production benefits. Rovio demonstrates how generative AI shortens the time required to produce thematic event art, seasonal variations, and supporting marketing visuals, freeing artists to focus on higher-value creative direction rather than repetitive execution. Throughout this process, the studio emphasizes that human oversight remains central: artists curate training data, validate outputs, and make the final calls on which assets ship to players, ensuring that automation amplifies rather than replaces creative craft.

The key takeaway is that combining custom-trained models on SageMaker with managed foundation models on Bedrock enables Rovio to achieve a careful balance between creative control, operational scalability, and production efficiency. This multi-service generative AI strategy positions Rovio to sustain a faster content cadence, preserve the unmistakable Angry Birds aesthetic, and continue exploring new creative possibilities as AWS's generative AI portfolio evolves.