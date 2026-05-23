---
clients:
- AWS
- Washington Post
- Amazon Bedrock
- Arc XP
date: 2024-12-08
description: AI-based chatbots are transforming how we use and build applications.
  As a tech innovator, the Washington Post built an LLM-powered chatbot trained on
  custom data including documentation, internal processes, and runbooks using Amazon
  Bedrock. But LLMs can also come with challenges, such as identifying hallucinations
  at scale, protecting against abuse from prompt injection, and ensuring against inadvertent
  disclosure of data. In this session, Joe Croney, CTO of the Washington Post’s Arc
  XP Busine
event: unknown
has_transcript: true
language: en-US
playlist: ''
tags:
- ai
- chatbot
- aws
- bedrock
- llm
- observability
- ethics
thematic: media
title: AWS re:Invent 2024 - Ensuring ethical use of AI models through consistent observability
  (AIM268)
url: https://www.youtube.com/watch?v=Z7GhKUaalZg
video_id: Z7GhKUaalZg
year: 2024
---

# AWS re:Invent 2024 - Ensuring ethical use of AI models through consistent observability (AIM268)

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=Z7GhKUaalZg)
> 📅 2024-12-08 | 🎤 unknown | 🌐 en-US
> 🏢 Clients: [[AWS]] [[Washington Post]] [[Amazon Bedrock]] [[Arc XP]]

# Ensuring Ethical Use of AI Models Through Consistent Observability

## Session Overview

This AWS re:Invent 2024 session, presented by Joe Croney, CTO of The Washington Post's Arc XP Business, in partnership with Datadog, examines how organizations can build LLM-powered chatbots responsibly while maintaining visibility into their behavior at scale. The discussion centers on The Washington Post's experience developing a custom chatbot trained on internal documentation, processes, and runbooks using Amazon Bedrock, and how observability practices became essential to ensuring the system operates ethically and effectively. As AI-based chatbots increasingly transform application development and user interaction, the session addresses the practical challenges teams face when moving these systems from experimentation into production environments.

## Building the Chatbot on Amazon Bedrock

The Washington Post's Arc XP team approached chatbot development as a way to enhance customer experience by surfacing institutional knowledge contained in technical documentation and operational runbooks. By leveraging Amazon Bedrock, the team gained access to foundation models without the overhead of managing infrastructure, allowing them to focus on tailoring the assistant to their specific business context. Training the model on proprietary data enabled the chatbot to answer domain-specific questions that generic LLMs could not address accurately, transforming static documentation into an interactive resource for customers and internal users alike.

## Addressing the Core Challenges of LLMs in Production

### Hallucinations, Prompt Injection, and Data Disclosure

Despite the productivity gains LLMs offer, the session emphasizes that deploying them responsibly requires confronting several persistent risks. Hallucinations, where the model generates plausible but incorrect information, become difficult to identify when interactions occur at scale across thousands of conversations. Prompt injection attacks present another threat, as malicious users may craft inputs designed to manipulate model behavior or bypass guardrails. Equally concerning is the risk of inadvertent data disclosure, where sensitive internal information embedded in training data or context windows could be surfaced to unauthorized users. Each of these issues compounds the difficulty of trusting AI outputs in customer-facing scenarios.

### Observability as the Foundation for Ethical AI

To mitigate these risks, The Washington Post implemented comprehensive LLM observability practices, partnering with Datadog to gain consistent visibility into model behavior, prompt patterns, response quality, and anomalous interactions. Observability allows the team to detect hallucinations through monitoring and evaluation pipelines, identify prompt injection attempts by analyzing input patterns, and ensure that responses align with both customer needs and ethical guidelines. By treating LLM monitoring with the same rigor applied to traditional application performance management, the team established feedback loops that support continuous improvement and accountability.

## Key Takeaways and Outcomes

The session concludes that responsible AI deployment is less about choosing the right model and more about establishing the operational discipline needed to observe, measure, and govern its behavior over time. The Washington Post's experience demonstrates that combining Amazon Bedrock's flexibility with robust observability tooling enables organizations to deliver AI-powered features that are both useful and trustworthy. For teams considering similar initiatives, the central lesson is that observability must be built in from the start rather than added retroactively, ensuring that ethical use of AI is enforced through measurable signals rather than aspirational policy.