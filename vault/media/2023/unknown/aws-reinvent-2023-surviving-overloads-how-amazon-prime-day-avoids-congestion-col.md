---
clients:
- AWS
- Amazon
date: 2023-11-29
description: Congestion collapse is a situation in large distributed systems when
  a collection of servers hits roughly 100% CPU utilization yet provides effectively
  zero productive work. Worse yet, you can’t recover even when systems scale up! In
  this session, join a discussion of the congestion collapse phenomenon and how it
  applies to web applications. This session covers how to recover, with an example
  from Amazon Prime Day. In the second half of the session, the discussion shifts
  to the AWS tools you can
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- cloud
- distributed-systems
- scaling
- prime-day
- congestion
- reinvent
thematic: media
title: 'AWS re:Invent 2023 - Surviving overloads: How Amazon Prime Day avoids congestion
  collapse (NET402)'
url: https://www.youtube.com/watch?v=fOYOvp6X10g
video_id: fOYOvp6X10g
year: 2023
---

# AWS re:Invent 2023 - Surviving overloads: How Amazon Prime Day avoids congestion collapse (NET402)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=fOYOvp6X10g)
> 📅 2023-11-29 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[AWS]] [[Amazon]]

# Surviving Overloads: How Amazon Prime Day Avoids Congestion Collapse

## Understanding Congestion Collapse in Distributed Systems

Congestion collapse represents one of the most insidious failure modes in large-scale distributed systems. The phenomenon occurs when a collection of servers reaches near 100% CPU utilization while simultaneously producing virtually zero productive work. What makes this failure mode particularly dangerous is its self-reinforcing nature: once a system enters this state, simply adding more capacity through horizontal scaling often fails to restore service. The servers remain pinned at maximum utilization, consumed entirely by overhead activities such as connection management, retries, and timeouts, rather than completing useful customer work.

This session explores how congestion collapse manifests specifically in web applications, where the interaction between client retry behavior, queuing dynamics, and resource exhaustion can drive an entire fleet into a non-productive equilibrium. The core insight is that traditional scaling responses—the instinctive reaction of operators facing high utilization—can be ineffective or even counterproductive when a system has already crossed this threshold.

## Lessons from Amazon Prime Day

### Recovery Strategies in Practice

Amazon Prime Day serves as a compelling real-world case study, given the extreme and concentrated traffic loads the event generates. The session walks through how Amazon engineers approach recovery when systems begin showing signs of congestion collapse, emphasizing that the path back to health requires deliberately shedding load rather than simply attempting to absorb it. Techniques such as load shedding, request prioritization, and breaking retry storms become essential tools for restoring productive throughput. The discussion underscores that recovery often requires temporarily serving fewer requests successfully rather than attempting to serve all requests poorly.

### Proactive Testing with AWS Tools

The second half of the session shifts from reactive recovery to proactive prevention. AWS provides tooling that allows teams to deliberately push their systems toward overload conditions in controlled environments, exposing congestion collapse vulnerabilities before they manifest in production. By incorporating overload testing into regular operational practice, teams can characterize their systems' behavior under saturation, validate that protective mechanisms engage correctly, and tune timeout and retry parameters to prevent the conditions that lead to collapse in the first place.

## Key Takeaways for Resilient Architectures

The overarching message is that resilience to congestion collapse cannot be retrofitted during an incident—it must be engineered into systems from the outset and continuously validated. Operators should design with explicit load-shedding mechanisms, sensible timeout hierarchies, and retry policies that include jitter and backoff to avoid synchronized retry storms. Equally important is cultivating the operational discipline to test these protections regularly, ensuring that when traffic spikes such as Prime Day arrive, the system degrades gracefully rather than catastrophically. By combining architectural safeguards with proactive testing using AWS tooling, teams can avoid the trap where adding capacity fails to restore service and instead build systems that maintain productive work even under extreme pressure.