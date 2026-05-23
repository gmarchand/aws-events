---
clients:
- AWS
- Capital One
date: 2024-06-14
description: Join this session to learn about Capital One’s strategic AWS Secrets
  Manager implementation that has helped ensure unified security across environments.
  Discover the key principles that can guide consistent use, with real-world examples
  to showcase the benefits and challenges faced. Gain insights into achieving reliability
  and resilience in financial services applications on AWS, including methods for
  maintaining system functionality amidst failures and scaling operations safely.
  Find out how yo
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- security
- secrets-management
- cloud
- resilience
- fintech
- devops
thematic: media
title: AWS re:Inforce 2024 - Capital One’s approach for secure and resilient applications
  (DAP302)
url: https://www.youtube.com/watch?v=W7OTRZphSi8
video_id: W7OTRZphSi8
year: 2024
---

# AWS re:Inforce 2024 - Capital One’s approach for secure and resilient applications (DAP302)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=W7OTRZphSi8)
> 📅 2024-06-14 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[AWS]] [[Capital One]]

# Capital One's Approach for Secure and Resilient Applications on AWS

## Overview of the Session

At AWS re:Inforce 2024, Capital One presented its strategic approach to building secure and resilient applications on AWS, focusing on how a major financial services institution unifies security practices across environments while maintaining the reliability customers expect from a regulated industry. The session combined practical implementation guidance with architectural principles, drawing on Capital One's real-world experience operating mission-critical workloads at scale. The discussion emphasized that security and resilience are not separate disciplines but complementary pillars that must be designed together from the start.

## Establishing Unified Security Through Secrets Management

### Strategic Implementation of AWS Secrets Manager

Capital One's security strategy centers on the consistent and disciplined use of AWS Secrets Manager to protect credentials, API keys, and other sensitive material across the organization. By standardizing on a single secrets management service, the company eliminates the fragmentation that typically arises when teams adopt different tools for handling sensitive data, and it ensures that policies for rotation, access control, and auditing apply uniformly to every workload. This unified approach reduces the attack surface, simplifies compliance reporting, and gives security teams a clear vantage point for monitoring how secrets are accessed and consumed throughout the enterprise.

### Guiding Principles and Lessons Learned

The presenters articulated a set of guiding principles that drive consistent secret usage, including treating secrets as first-class infrastructure, automating rotation wherever feasible, enforcing least-privilege access through fine-grained IAM policies, and integrating secret retrieval directly into application runtimes rather than embedding credentials in code or configuration files. They shared real-world examples illustrating both the benefits realized—such as faster incident response and reduced credential sprawl—and the challenges encountered, including the operational complexity of coordinating rotation across distributed services and the cultural shift required to move teams away from legacy practices.

## Building Reliability and Resilience for Financial Services

### Multi-Region Architecture and Core AWS Services

Resilience for financial workloads demands that systems continue functioning despite component failures, regional disruptions, or unexpected load surges. Capital One described how it leverages multi-Region AWS services to achieve this goal, using Amazon Route 53 to direct traffic intelligently across healthy endpoints, AWS Auto Scaling to adjust capacity safely in response to demand, and Amazon DynamoDB global tables to maintain consistent, low-latency data access across geographies. Together these services form the foundation of an architecture that can absorb failures without interrupting customer experiences.

### Chaos Engineering and Site Reliability Practices

To validate that their resilience mechanisms actually work under stress, Capital One applies chaos engineering and site reliability engineering disciplines, deliberately injecting failures into production-like environments to surface weaknesses before they affect customers. The team treats every observed failure mode as a learning opportunity, feeding insights back into architectural improvements and operational runbooks. They also emphasized the importance of scaling operations safely, ensuring that automated responses to load or failure events do not themselves become sources of instability—a particular concern in financial services, where cascading failures carry significant regulatory and reputational consequences.

## Key Takeaways

The session concluded by reinforcing that secure and resilient applications result from deliberate engineering choices, organizational discipline, and continuous validation. Capital One's experience demonstrates that combining a unified secrets management strategy with multi-Region resilience patterns and proactive chaos testing enables a financial institution to meet stringent security and availability requirements on AWS. The presenters encouraged attendees to adopt similar principles, adapting them to their own contexts, and to view security and reliability as ongoing practices rather than one-time implementations.