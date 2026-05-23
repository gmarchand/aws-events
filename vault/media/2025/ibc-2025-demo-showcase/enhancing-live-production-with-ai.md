---
clients:
- AWS
- Vizrt
- Amazon Prime Video
- University of Bristol
date: 2025-09-29
description: Customers face increasing challenges in creating customized variants
  of live content to support different markets and use-cases such as localization.
  Additionally, as customers migrate their broadcast workloads to the cloud, they
  require tools to ensure the quality of their live outputs. The enhancing live production
  with AI demonstration showcases how to address these challenges through two AI-powered
  systems powered by AWS and AWS Partner offerings. The demo features an innovative
  system for b
event: ibc-2025-demo-showcase
has_transcript: true
language: en
playlist: IBC 2025 Demo Showcase
tags:
- ai
- live-production
- cloud
- broadcast
- localization
- quality-control
- aws
thematic: media
title: Enhancing live production with AI
url: https://www.youtube.com/watch?v=dpuA2Rzm5C8
video_id: dpuA2Rzm5C8
year: 2025
---

# Enhancing live production with AI

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=dpuA2Rzm5C8)
> 📅 2025-09-29 | 🎤 ibc-2025-demo-showcase | 🌐 en
> 🏢 Clients: [[AWS]] [[Vizrt]] [[Amazon Prime Video]] [[University of Bristol]]

# Enhancing Live Production with AI

In this demonstration, Robin Williams, Senior Solutions Architect at AWS, presents two AI-driven solutions designed to enhance live cloud production. The first addresses real-time multilingual broadcasting through automated graphics translation, while the second focuses on video quality control using a purpose-built artifact detector. Both systems illustrate how AWS services can be combined with specialized broadcast technologies to streamline operations while preserving human oversight.

## Automated Graphics Translation for Multilingual Broadcasting

The first solution combines AWS services with Vizrt's graphics technology to deliver real-time multilingual broadcasting. Operators interact with a web application hosted on Amazon S3 and distributed via CloudFront to manage broadcast graphics. When text elements are created, AWS Lambda processes the request through API Gateway and stores the associated metadata in DynamoDB. Translations are generated using Amazon Bedrock, then published to Amazon MSK, where Viz Data Center consumes the messages and acts as a gateway, distributing the translated content to the Viz Engine to ensure real-time updates across multiple language variants.

### Workflow in Practice

In the live demonstration, submitting a text element triggers two simultaneous outcomes: the system automatically generates translations, and the Viz Engine output reflects them in real time on the broadcast graphic. Operators retain full control and can manually edit any translation, with changes appearing instantly in the output. This balance of automation and operator intervention ensures both efficiency and the cultural and linguistic accuracy required for professional broadcasting.

## Video Quality Control with MVAD

The second solution is the Multi-Visual Artifact Detector (MVAD), co-developed by Amazon Prime Video and the University of Bristol. MVAD analyzes video quality by detecting issues such as frame distortion and blurring, and it delivers plain-language insights through integration with Amazon Bedrock. Operators access a static website hosted on Amazon S3, secured by Amazon Cognito authentication. When analysis is requested, an AWS Lambda function equipped with FFmpeg generates 10 to 30 second clips from active AWS Elemental MediaConnect flows and stores both the clips and metadata in Amazon S3. Amazon SNS notifications then trigger two parallel workflows: one uses Amazon Bedrock with TwelveLabs Pegasus 1.2 for content analysis, while the other connects to a self-hosted MVAD deployment on Amazon EC2 for temporal analysis and artifact detection. Results from both workflows are stored in S3 for immediate browser access.

### Operator Experience

A custom MediaConnect dashboard presents all active flows with thumbnails, status indicators, and connection details optimized for broadcast operations. After selecting a flow and choosing a recording duration, MVAD performs temporal analysis at multiple points across the clip while Amazon Bedrock provides detailed content analysis. The interface displays the analyzed clip alongside a timeline view, allowing operators to jump directly to points of interest. By combining technical metrics with AI-powered content recognition expressed in plain language, the system enables rapid identification and resolution of broadcast issues.

## Conclusion

Together, these two solutions show how AI applications can be built on AWS to meaningfully enhance live broadcast operations. By automating translation workflows and surfacing quality issues through intelligent analysis, they reduce operational burden while keeping human operators in control. The result is a flexible approach suitable for broadcasters of all sizes seeking to modernize their live production capabilities.