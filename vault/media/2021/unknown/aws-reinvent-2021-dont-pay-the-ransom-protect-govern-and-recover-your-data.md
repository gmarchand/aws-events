---
clients:
- AWS
date: 2021-12-17
description: 'Enterprise data protection is more important than ever because of not
  only a rise in cyberattacks but also increasing sophistication, including exfiltration
  techniques. How can you ensure your business knows what sensitive data is vulnerable
  and ensure that it is ready to respond if attacks occur? A proactive approach is
  needed to govern data access and detect unauthorized use. And inevitably, when production
  data is compromised, you need to be able to quickly recover at scale. In this session, '
event: unknown
has_transcript: true
language: en
playlist: ''
tags:
- security
- ransomware
- data-protection
- aws
- cloud
- backup
- governance
thematic: media
title: 'AWS re:Invent 2021 - Don’t pay the ransom: Protect, govern, and recover your
  data'
url: https://www.youtube.com/watch?v=cINWoXYWNXY
video_id: cINWoXYWNXY
year: 2021
---

# AWS re:Invent 2021 - Don’t pay the ransom: Protect, govern, and recover your data

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=cINWoXYWNXY)
> 📅 2021-12-17 | 🎤 unknown | 🌐 en
> 🏢 Clients: [[AWS]]

# Don't Pay the Ransom: Protect, Govern, and Recover Your Data

## Overview of the Modern Data Protection Challenge

Enterprise data protection has become a critical business imperative as organizations face an unprecedented rise in cyberattacks, particularly ransomware incidents that have grown both in frequency and sophistication. In this AWS re:Invent 2021 session, Theresa Miller of Cohesity examines why traditional defensive postures are no longer sufficient and how a proactive, integrated approach to data management can help businesses avoid the agonizing choice of paying a ransom to recover their operations. The central message is that paying attackers should never be the answer; instead, enterprises must combine prevention, governance, and rapid recovery into a unified strategy that addresses today's threat landscape.

The session emphasizes that modern attackers no longer simply encrypt data and demand payment. Increasingly, they use exfiltration techniques to steal sensitive information before locking systems, then threaten public exposure if victims refuse to pay. This evolution means organizations must understand exactly what sensitive data they hold, where it lives, and who has access to it long before an incident occurs.

## A Three-Pillar Approach to Cyber Resilience

### Protecting Data Through Immutable Backup and Hardened Infrastructure

The first pillar focuses on ensuring that backup data itself cannot become a casualty of an attack. Miller explains that ransomware actors increasingly target backup repositories first, knowing that organizations with compromised backups have little choice but to negotiate. To counter this, enterprises need immutable backup snapshots that cannot be altered or deleted by attackers, even those who obtain administrative credentials. Additional safeguards such as multi-factor authentication, encryption in flight and at rest, role-based access controls, and the elimination of legacy protocols all contribute to hardening the environment. By delivering data management as a service on AWS, Cohesity allows customers to consume these protections without managing the underlying infrastructure themselves.

### Governing Sensitive Data and Detecting Unauthorized Use

The second pillar addresses the reality that you cannot protect what you do not understand. Miller walks through how data classification, discovery, and governance capabilities allow organizations to identify sensitive information such as personally identifiable information, financial records, and regulated data across sprawling environments. Continuous monitoring and anomaly detection then help surface unauthorized access patterns or unusual behavior that may signal an attack in progress. This proactive visibility shortens the time between compromise and detection, which is often the difference between a contained incident and a catastrophic breach. Governance also supports regulatory compliance, giving teams a clearer picture of risk exposure across their entire data estate.

### Recovering Quickly and at Scale When Incidents Occur

The third pillar acknowledges that even with strong protection and governance, breaches will sometimes succeed. When production data is compromised, the speed and reliability of recovery determine the business impact. Miller highlights the importance of being able to restore at scale, whether that means recovering individual files, entire virtual machines, databases, or full application environments. Leveraging AWS as a recovery target gives organizations elasticity to spin up clean environments quickly, and instant mass restore capabilities help bring operations back online in minutes or hours rather than days or weeks. Testing recovery procedures regularly is essential so that when an actual event occurs, the runbook is proven rather than theoretical.

## Key Takeaways and Recommended Actions

The session closes by reinforcing that cyber resilience is a continuous discipline rather than a one-time project. Organizations should evaluate their current backup architecture for immutability and access controls, invest in classifying and governing sensitive data so they understand their exposure, and rehearse recovery scenarios so that operational muscle memory exists before a crisis. By combining these capabilities through a managed service delivered on AWS, businesses can reduce operational complexity while strengthening their defensive posture. Ultimately, the message is that organizations who plan for resilience never have to face the question of whether to pay a ransom, because they retain control over their own recovery.