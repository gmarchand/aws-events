---
clients:
- AWS
date: 2024-12-05
description: "At AWS, we’ve learned that building resilient services requires more
  than just designing for high availability. In this session AWS operational leaders
  are back for more insights on how to mitigate impact when, not if, the unexpected
  happens. Hear a few short stories collected from 18 years of operational excellence,
  with practical advice on preparing for and mitigating failure.\n\nLearn more:\nAWS
  re:Invent: https://go.aws/reinvent.\nMore AWS events: https://go.aws/3kss9CP \n\nSubscribe:\nMore
  AWS vid"
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- aws
- resilience
- cloud
- reinvent
- operations
- high-availability
thematic: media
title: 'AWS re:Invent 2024 - Failing without flailing: Lessons we learned at AWS the
  hard way (ARC333)'
url: https://www.youtube.com/watch?v=c2ekr1Us51s
video_id: c2ekr1Us51s
year: 2024
---

# AWS re:Invent 2024 - Failing without flailing: Lessons we learned at AWS the hard way (ARC333)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=c2ekr1Us51s)
> 📅 2024-12-05 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[AWS]]

# Failing Without Flailing: Lessons Learned at AWS the Hard Way

## Overview of the Session

At AWS re:Invent 2024, operational leaders from AWS returned to share hard-earned lessons drawn from eighteen years of running large-scale cloud services. The session, identified as ARC333, built on the premise that designing for high availability alone is insufficient for building truly resilient systems. Instead, the speakers emphasized that resilience requires anticipating, preparing for, and gracefully mitigating the inevitable moments when systems behave in unexpected ways. Through a series of short operational stories, the presenters offered practical guidance on how engineering teams can fail without flailing, treating disruption as a predictable part of operating distributed systems at scale.

## Core Themes and Lessons

### Designing for the Inevitability of Failure

A central message of the session was that failure in complex systems is not a question of *if* but *when*. The speakers framed resilience as an operational discipline rather than a static architectural property, arguing that even well-designed services encounter conditions their builders never anticipated. They stressed the importance of assuming that dependencies will degrade, traffic patterns will shift suddenly, and rare edge cases will eventually surface in production. By internalizing this mindset, teams shift their focus from preventing all failures to limiting blast radius, accelerating recovery, and maintaining customer trust when something does go wrong.

### Mitigating Impact Through Operational Excellence

Drawing on AWS's long operational history, the presenters shared lessons on how to reduce the severity and duration of incidents when they occur. They highlighted the value of building mechanisms that detect anomalies early, contain problems within isolated boundaries such as cells or Availability Zones, and provide operators with safe, well-rehearsed levers to pull during a live event. Practices such as gradual deployments, automated rollback, throttling, load shedding, and static stability were discussed as ways to ensure that a service can continue serving customers even when parts of the system or its dependencies are impaired. The speakers also emphasized that runbooks, game days, and continuous practice of recovery procedures are what allow teams to act calmly and decisively under pressure rather than improvising during an incident.

### Learning From Real-World Operational Stories

The session relied heavily on storytelling, with the presenters recounting specific situations in which AWS services encountered unexpected behavior and the lessons engineers extracted from each event. These narratives illustrated how seemingly small design decisions—around retries, timeouts, capacity planning, configuration changes, or dependency assumptions—can cascade into significant customer impact when conditions change. The speakers consistently returned to the importance of correction-of-error culture, in which every incident becomes an opportunity to identify root causes, propagate fixes across similar systems, and strengthen the broader operational fabric of the organization.

## Key Takeaways for Practitioners

The overarching outcome of the talk was a set of practical principles that engineering teams can apply to their own services. Teams should assume failure modes will occur and invest deliberately in containment and recovery rather than relying on prevention alone. They should build observability that surfaces problems quickly, automate the safest path back to a healthy state, and routinely practice their response so that operators are prepared when real incidents arrive. Finally, they should treat every failure as a source of durable organizational learning, ensuring that lessons from one team improve the resilience of the entire platform. The session reinforced that operational excellence is a continuous, evolving practice—one shaped by humility, preparation, and a willingness to learn from the difficult moments that all large-scale systems eventually face.