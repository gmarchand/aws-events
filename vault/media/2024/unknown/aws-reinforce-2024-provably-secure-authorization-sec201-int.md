---
clients:
- AWS
date: 2024-06-13
description: "Automated reasoning has revolutionized how AWS demonstrates the security
  of controls. This new model is called provable security, where automated reasoning
  tools apply mathematical logic to help answer critical questions about your infrastructure.
  \n\nIn this talk, learn how AWS has used automated reasoning to prove the security
  properties of AWS access controls, namely IAM authorization. In addition, the talk
  covers the capabilities and services AWS has built for users to verify their own
  securit"
event: unknown
has_transcript: true
language: en
playlist: ''
tags:
- security
- aws
- authorization
- automated-reasoning
- cloud
- infrastructure
thematic: media
title: AWS re:Inforce 2024 - Provably secure authorization (SEC201-INT)
url: https://www.youtube.com/watch?v=xPe_ddEnj4Q
video_id: xPe_ddEnj4Q
year: 2024
---

# AWS re:Inforce 2024 - Provably secure authorization (SEC201-INT)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=xPe_ddEnj4Q)
> 📅 2024-06-13 | 🎤 unknown | 🌐 en
> 🏢 Clients: [[AWS]]

# Provably Secure Authorization at AWS

## Overview of Provable Security

AWS has fundamentally transformed how it demonstrates the security of its controls through the application of automated reasoning, a discipline that uses mathematical logic to provide rigorous answers to critical questions about cloud infrastructure. This approach, known as provable security, moves beyond traditional testing and empirical validation by mathematically proving that systems behave according to their specifications under all possible conditions. By formalizing security properties and applying theorem-proving techniques, AWS can offer customers a level of assurance that goes well beyond what conventional verification methods can achieve.

The session emphasizes that provable security is not a theoretical exercise confined to academic research. AWS has operationalized these techniques across its core services, embedding mathematical proofs into the development lifecycle of foundational components. This shift represents a significant evolution in how cloud providers communicate trust to their customers, replacing assertions and audits with verifiable mathematical guarantees.

## Applying Automated Reasoning to IAM Authorization

### Proving the Correctness of Access Controls

A central focus of the talk is how AWS has applied automated reasoning to the security properties of IAM authorization, the system that governs every access decision across the AWS platform. By modeling the authorization logic in formal terms, AWS engineers can prove that access controls behave as intended, ensuring that policies grant or deny permissions exactly as specified. This work helps eliminate entire classes of subtle bugs and misconfigurations that could otherwise lead to unintended access, and it provides confidence that the authorization layer underlying millions of customer workloads is mathematically sound.

### Cedar and Amazon Verified Permissions

Building on this foundation, AWS has extended provable security techniques to customer-facing tools, most notably through Cedar, an open source policy language designed from the ground up with formal verification in mind. Cedar enables developers to express fine-grained authorization rules with clear semantics, and its design has been validated using the same automated reasoning methods AWS applies internally. Through Amazon Verified Permissions, customers can adopt Cedar within their own custom applications, gaining access to a policy engine whose correctness has been mathematically established. This empowers organizations to build authorization systems that are not only expressive and flexible but also verifiably secure.

### Customer Tools for Verifying Security Posture

Beyond Cedar, AWS has developed a broader set of capabilities and services that allow customers to verify their own security postures using provable techniques. These tools enable organizations to reason about their configurations, validate that policies meet intended security goals, and detect deviations before they manifest as vulnerabilities. By making provable security accessible through managed services, AWS extends the benefits of formal methods to customers who do not have specialized expertise in automated reasoning.

## Outcomes and Strategic Direction

The talk illustrates a clear strategic direction in which AWS continues to invest in mathematical rigor as a differentiator for cloud security. The combination of internally proven authorization systems, open source contributions like Cedar, and customer-facing services such as Amazon Verified Permissions reflects a commitment to raising the baseline of security assurance across the industry. Customers are encouraged to explore these capabilities to strengthen their own applications, leveraging tools whose foundations have been verified with the same techniques AWS uses to secure its own platform.