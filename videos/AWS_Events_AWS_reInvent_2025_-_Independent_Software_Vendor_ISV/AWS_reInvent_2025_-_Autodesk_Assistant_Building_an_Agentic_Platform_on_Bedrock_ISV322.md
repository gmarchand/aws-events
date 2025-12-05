# AWS re:Invent 2025 - Autodesk Assistant: Building an Agentic Platform on Bedrock (ISV322)

[Video Link](https://www.youtube.com/watch?v=4i4ybcj8eeY)

## Description

Autodesk tackled fragmented workflows and inconsistent experiences across its product portfolio by building the Autodesk Assistant Platform— a next-generation, agentic AI partner that unifies capabilities, anticipates needs, and performs complex tasks in collaboration with its human counterpart. Powered by Amazon Bedrock AgentCore and Strands, the platform seamlessly bridges cloud and desktop environments while coordinating domain-specific agents and MCP servers to deliver contextual insights and automate complex workflows. This session explores Autodesk's architecture, implementation approach, and key lessons learned in designing and scaling an agentic platform that breaks down product silos at enterprise scale.

Learn more:
AWS re:Invent: https://go.aws/reinforce.
More AWS events: https://go.aws/3kss9CP 

Subscribe:
More AWS videos: http://bit.ly/2O3zS75
More AWS events videos: http://bit.ly/316g9t4

ABOUT AWS:
Amazon Web Services (AWS) hosts events, both online and in-person, bringing the cloud computing community together to connect, collaborate, and learn from AWS experts.
 AWS is the world's most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally. Millions of customers—including the fastest-growing startups, largest enterprises, and leading government agencies—are using AWS to lower costs, become more agile, and innovate faster.

#AWSreInvent #AWSreInvent2025 #AWS

## Transcript

Hello everyone, uh, thank you for coming to our session. Really excited to be here today to talk to you about Autodesk Assistant and how we are building an agentic platform on top of AWS Bedrock. My name's Matthew Liam. I'm a software architect at Autodesk, and I'm joined here by Sahil Sahini, who's a solution architect at AWS and someone who's been an incredible partner throughout this journey. Um, I know we only have 20 minutes and a lot to go through, so let's dive right in. For those of you not familiar with Autodesk, Autodesk is a global leader in 3D design, engineering, and entertainment software. We build the software that architects, engineers, uh, designers, and creators use to build everything from cars. Games, machines, machines, games, um, essentially anything that needs to be imagined, designed and built. Autodesks have been the pioneers in the design and make space for over 40 years now, and as our customers have grown, so have we, from a handful of innovators to over 15,000 people globally. Our industry solutions and platform services allows our customers to take an idea and turn it into reality from design all the way through to manufacturing, production, construction, and beyond. Today our customers like many of yours are facing unprecedented amount of disruption and demand. Manufacturers are feeling challenged to constantly push new products out to the market while dealing with supply chain delays and labor shortages. In our AECO industry, designers are constantly feeling pressured to deliver new products, more complex projects faster while dealing with the demand of more, uh, more infrastructure, more housing, more experiences, all while being more sustainable, and our production studio of all sizes are struggling to keep up with consumer demand, tight timelines, as well as the constant demand for fresh new content. Agentic AI represents a fundamental shift in how AI systems function. In the design and make space, it is allowing us to move beyond the old model of point and click to this new era of describe and do where your intent becomes your actions. It is also unlocking entirely new levels of creative velocity for our customers. The amount of time it's going to take to go from an idea to impact is being shortened to moments, no longer weeks, allowing our customers to really focus on innovation and spend less time on the day to day busy work. Agente AI is also redefining what's even possible for our customers. Signaling the shift from manual tasks to highly connected, automated and accessible workflows. All of this is allowing our customers to unlock faster, smarter outcomes from optimizing their site plans to, um, streamlining design iterations to automating post-production sites. And so that's why we built Autodesk Assistant. Autodesk Assistant is your agentic AI partner that speaks, design, and make. From day one it's able to do three things automate the manual, connect the disconnected, and deliver real-time insights all in collaboration with, uh, their human counterpart. Let's jump into a quick demo to see it in action. Oops. OK, um, so right here is Revit. Revit is our building information and modeling software, and on the right hand side here I have Autodesk assistant. The first thing I'm gonna ask assistant to do is tell me more about the building model that I have opened up here. Um, this is a very common like tell me, ask me type use case, um, very similar to software engineer where maybe you're entering a new code repo and so then uh and you wanna be able to quickly get up to speed, so the first thing you wanna ask is be able to ask questions about it. So in this case I'm gonna ask it to tell me the window to wall ratio of the building in my north facade. Um, Autodesk assistant is gonna go in, do its calculation, and return back around 19%. The next thing I'm gonna ask the assistant to do is more of a do it for me use case or like design with me use case. Um, in this case I'm gonna ask the assistant to take all these windows we didn't like the 19% and modify it to double hung windows with slightly larger dimensions so that um we're able to get a little bit more sunlight. Oh, behind the scenes, Autodesk assistant is taking this prompt, routing it to one of our AI agents, which has a number of MCP servers behind it. It's calling an LLM which helps decide which, uh, MCP server and tool to use, which in turns calls one of the product APIs. So assistant's going to try different things and Just like that, all my windows were modified, um, so this is really powerful, especially for users like me who not an expert at Reddit, but I'm able to go in, use natural language, and make all these modifications. Um, the next thing I'm gonna ask the assistant to do is help me with some of my workflow documentation, um, type work. So once a model is complete, there's a lot of work, a lot of manual work that goes into making it ready to be distributed to other contractors or architects to kind of take the design forward, um, so the first thing I'm gonna ask the assistant to do is create a floor plan view of my building. So it's gonna go in, create a new sheet of my floor plan. It's a little bit messy, so we need to clean it up. Next I'm gonna ask the assistant to apply a view template on top of this, um, and also help me annotate some of the doors, windows and walls, um. So gonna ask the assistant to do that, let it run and assistant's gonna go in, look at my current sheet, identify all those objects, and create a new view that has all those different annotations. So we're almost done. The last thing I'm gonna ask the assistant to help me with is create a cover sheet with this view, um, so cover sheet has a lot of our company standards, the numbering, naming, etc. um, so that's the last step before we're able to share it with others. So just like that I was able to go from taking an existing model, being able to ask questions about it, uh, be able to modify it through natural language and then get it into a state that is ready to be shared with others. Next, let's look at the architecture that powers all of this. So starting with number one is our MCP servers. Our MCPs are a core component of our Autodesk assistant architecture. At at Autodesk we've been investing in data and APIs for the last decade, so MCPs is a natural extension of that journey. That allows us to bridge LLM models and our APIs to real world actions. We have both, uh, local MCP servers as well as cloud MCP servers. The majority of our customers use Autodesk products through our desktop, um, but there's still a lot of integration with our cloud services, so that's why we support both. Um, number 2 is our agents. We have a wide variety of agents at Autodesk. We have products specific agents like an AutoCT agent or a Revet agent. We also have, uh, more general agents that span across multiple products, so like a customer support agent or an agent that helps with administration and licensing. These agents essentially provide the core capabilities of Autodesk assistant, everything from question and answers to, um, helping automate some tasks and workflows and then within these agents another thing important to call out is that there's a wide variety of complexity. Some agents are very simple and are simply just calling an LLM to help with uh MCP tool execution, while other agents are a bit more complex and have like a multi-stage workflow within it. Another core component of our architecture is our assistant back end. How we've built Autodesk Assistant is as a shared platform service across our whole organization, so any team across our, you know, any team or product can bring their agent or MCP server and build on top of our platform. Um, and so as a platform team we've been focusing a lot of effort in the shared capabilities like guard rails, context management, um, how we're handling like observability of token usage and LLM tracing. Another, uh, key point is the conversation proxy router. This is essentially like the brains of Autodesk Assistant because it is responsible for all the routing of requests across all our products to the correct domain agent. It also handles some of the agent to agent communication that we have here. Um, we use a number of different strategies within this conversation proxy router. In some cases we're using an LLM to help with the decision. In other cases we have more deterministic flows where it's more like rule based. So for a given product it'll route to, it'll always route to a specific agent. Um, so now when a user submits a query they're interacting with our assistant UI. We have many different flavors of our assistant UI. We have the embedded version that you saw in the demo, but we also have this in a web version. But regardless of where you're accessing assistant, you're always gonna get the same look and feel and overall general experience is gonna be the same. The assistant UI plays a very important role in the sense that it passes the user prompt to our back end, but in addition to passing the user prompt, it also passes applicable context. Um, this context can be like who the user is, where the user is coming from, what product they're from. Um, what license do they have, all the applicable MCP tools, and this is really important because we use this context to help with the decision making for agent selection as well as MCP tool selection. So once the um request gets routed to one of the agents, the agents process that request and sends it back to the assistant to UI to be uh exposed to the user. Um, and that is essentially our end to end flow of how we process a requests through our assistant architecture. Uh, I'm now gonna pass it off to Cejil who's gonna go over Agent core and some of the underlying services. Oh Folks, um, Sahil, I'm solution architect, um, with AWS specializing in generative AI and agentic AI, and I work with, uh, strategic partners like Autodesk in building next generation of generating AI applications, so. Autodesk was building this whole agentic workflow. They realized at a very early stage that building these agents are great. It's good for business, but taking it to production. Are, uh, that, that, that caught their attention is around the performance, scalability, security, and the governance of agents and the workflows that they, they were building. A platform team was building agents. They, they, they took a step back. They tried to make it more like a platform strategy rather than building it as a bespoke or a snowflake agents. And during, during the exploration phase, there are a couple of challenges that organizations like Auditors figured out at an early stage, specifically around how to get. A secure compute runtime environment for agents as well as for their MCP servers. How to get this centralized contextual management so that all the industries across Autodesk can have the same contextual information when the workflow goes between the agents? What is the centralized identity and the excess governance that they needed on the top of Autodesk assistant? And moreover, how to discover or connect with the custom MCP servers or a cross domain agent for any purpose-built workflows and for without saying it, auditability and observability is one of the callouts and. Auditors figured out at an early stage, these are the things we cannot let all the industry teams build by themselves. Why don't we have it as a platform strategy so that everybody can plug it in, use the best practices, and build their workflows on top of it. Saying that that was the Autodesk platform approach. AutoDisk built a centralized Autodesk assistant which is uh frontend UI so that all the end users across different industries and personas will have same consistent experience. They will not see a different UI behind the scene. They will be talking to platform components that I'll be going in the next slide, and all the domain agents or MCP server will integrate to this platform to make sure that they get the best out of what has already been vetted on. Going next, this is a high level overview of how Autodesk laid it across. Like Matt talked about how Autodesk built this centralized agent, and that's where Autodesk use agent core runtime and use strands as a framework to power all the interactions or the workflow to the domain agents and MCP server. So every time a user query comes in. This is a centralized orchestration agent power on strands that take that call, whether that query needs to be solved by a default agent, a domain agent, or a support agent. And all these agents have their own native integration to a hybrid MCP servers. Moreover, Autodesk being doubled down onto Agent Core Gateway because Autodesk have invested a lot on API, on data, and how to quickly convert those APIs into MCP servers. That's where Autodesk use. Code gateway where all the AutoDisk APIs that are open API enable are being directly exposed through agent code gateway and being exposed as an MCP server. Moreover, all the existing MCP servers that have been created or been built have been interfaced behind agent code gateway. And if you look at the top. Audit deck with a platform mindset, they made a couple of uh uh capabilities as a centralized platform capabilities coming from guard rails. Every conversation that is coming in or going out of Autodesk assistant has been vetted thoroughly. It has all the guard rail policy. been inferred at the time of inference. Similarly, Autodesk use leverage agent core memory and AWS surveillance services to store all the short term and the long-term conversation so that all the agent workflows that is going across the domain have the same contextual information. Agent core identity has been leveraged to power all the MCP workflows and to make sure agents have the centralized uh identity while interacting with the underlying or downstream applications and Autodesk also build a hybrid cloud. MCP server powered on AWS Serves for all the cloud MCP as well as the desktop MCP. I know I talked a lot about Agent Core. Let me give you a quick overview what Agent Core is for people who don't know about Agent Core. These are a set of fundamental services that Amazon released 6 months back, I would say, and it got GA very recently. Uh, which, which helps our customers to build, scale, or roll out agents to production quickly. In agent core, the fundamental concept. Primitives and you don't have to use all of them. You can use what is required for your agent protocol. Agent Core also offer you open from uh model support. You can have interaction with model from Bedrock, from OpenAI, whatever your model inference platform is, and you can use any framework of your choice. I'll quickly touch on a couple of things that AutoDisk use and that that has been used as a centralized platform, specifically around runtime. Autitork figured out like many of the industry teams have their own preference. On the framework, a couple of teams use Landgraf. Few teams are comfortable with crew AI Strands is predominantly, like many teams use, so Autodisk use Asian core runtime for a secure, isolated compute infrastructure so that all the industry teams can just plug into it and have a production ready computer compute environment for them. Running their MCP servers or their domain agents. Agent Code Gateway is a surveillance offering that lets you expose your open API spec, your existing MCP server, or any lambda functions that you have built for your business workflow. It helps you to integrate and give you a quick turnaround for MCP interfaces along with agent core identity. And finally on the agent core memory to have this centralized contextual management and to make sure that the workflow have the short term information and all the previous conversation that happened with Autodesk assistant AutoTk vetted on agent core memory and use all the short term and the long term memory to power the workflow. Going next, uh, I wanna quickly touch on Strands agent because, uh, when many teams within Autodesk were using different framework, there is also, uh, a lack of opinion. What should we go ahead with, and that's where Autodesk made Strands as a framework of choice so that, uh, all the industry teams while building their agentic framework can quickly get on boarded, have a native integration with Agent Core. Sorry. Couple of features about Strand, it has support for all the open source protocol. It has support for MCP, A2A, easy to build, and Autodisk have seen greater adoption, a seamless adoption of strands, and it accelerates the development cycle for all the industry teams to quickly build the agents. Going, I know we have a couple of seconds left. I'll quickly go over the key takeaways. Um, artists realized that while they were building a system like concurrent sessions, they need a scalable runtime environment and that's where they leverage Agent core runtime with other AWS surveillance options that they were using Platform component, uh, they unified the framework and make sure. Agents and MCP servers are common so that industry teams don't have to swing between different kinds of services and, uh, get to the work. I know we, but at high level, these are the key takeaways. I will go to call to action. Deep dive onto Agent Core. We have a lot of samples there. We have also built what we build for Autodesk Assistant as an agent Omnimesh, which is an open source framework of multi-agent collaboration. We encourage you to test it in your AWS account and finally, we encourage you to check Autodisk Assistant in action to see all those cool features. With that, thank you very much. We will be around here, so if you have any question, happy to answer.

## Subtitles with Timestamps

[00:00](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=0s) Hello everyone, uh, thank you for

[00:02](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=2s) coming to our session.

[00:04](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=4s) Really excited to be here today to talk to you

[00:06](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=6s) about Autodesk Assistant and how we are

[00:08](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=8s) building an agentic platform on top of

[00:10](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=10s) AWS Bedrock.

[00:12](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=12s) My name's Matthew Liam. I'm a software architect

[00:14](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=14s) at Autodesk, and I'm joined here

[00:16](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=16s) by Sahil Sahini,

[00:18](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=18s) who's a solution architect at AWS

[00:21](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=21s) and someone who's been an incredible partner throughout

[00:23](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=23s) this journey.

[00:24](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=24s) Um, I know we only have 20 minutes and a lot to go

[00:27](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=27s) through, so let's dive right in.

[00:29](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=29s) For those of you not familiar with Autodesk,

[00:31](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=31s) Autodesk is a global leader in 3D

[00:34](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=34s) design, engineering, and entertainment

[00:36](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=36s) software.

[00:37](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=37s) We build the software that architects,

[00:40](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=40s) engineers,

[00:41](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=41s) uh, designers, and creators use to

[00:43](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=43s) build everything from cars.

[00:47](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=47s) Games, machines,

[00:49](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=49s) machines,

[00:50](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=50s) games,

[00:51](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=51s) um,

[00:53](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=53s) essentially anything that needs to be

[00:55](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=55s) imagined, designed and built.

[00:57](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=57s) Autodesks have been the pioneers in the design and

[00:59](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=59s) make space for over 40 years now,

[01:02](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=62s) and as our customers have grown,

[01:04](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=64s) so have we, from a handful of innovators

[01:06](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=66s) to over 15,000 people globally.

[01:10](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=70s) Our industry solutions and

[01:12](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=72s) platform services allows our customers

[01:15](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=75s) to take an idea and turn it into

[01:17](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=77s) reality from design all the

[01:19](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=79s) way through to manufacturing,

[01:21](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=81s) production, construction, and beyond.

[01:25](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=85s) Today our customers like many of yours

[01:27](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=87s) are facing unprecedented

[01:29](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=89s) amount of disruption and demand.

[01:32](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=92s) Manufacturers are feeling challenged

[01:34](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=94s) to constantly push new products out

[01:36](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=96s) to the market

[01:37](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=97s) while dealing with supply chain delays and

[01:39](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=99s) labor shortages.

[01:41](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=101s) In our AECO industry,

[01:44](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=104s) designers are constantly feeling pressured

[01:46](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=106s) to deliver new products,

[01:48](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=108s) more complex projects faster

[01:50](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=110s) while dealing with the demand of more,

[01:52](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=112s) uh, more infrastructure, more housing,

[01:55](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=115s) more experiences,

[01:56](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=116s) all while being more sustainable,

[01:59](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=119s) and our production studio of all sizes

[02:01](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=121s) are struggling to keep up with consumer

[02:03](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=123s) demand, tight timelines,

[02:06](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=126s) as well as

[02:07](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=127s) the constant demand for fresh new content.

[02:11](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=131s) Agentic AI represents a

[02:13](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=133s) fundamental shift in how

[02:15](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=135s) AI systems function.

[02:17](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=137s) In the design and make space,

[02:19](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=139s) it is allowing us to move beyond

[02:22](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=142s) the old model of point and click

[02:24](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=144s) to this new era of describe and do

[02:27](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=147s) where your intent

[02:28](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=148s) becomes your actions.

[02:30](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=150s) It is also unlocking entirely new

[02:32](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=152s) levels of creative velocity for our customers.

[02:36](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=156s) The amount of time it's going to take to

[02:38](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=158s) go from an idea to impact

[02:40](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=160s) is being shortened to moments, no longer

[02:42](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=162s) weeks, allowing our customers

[02:44](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=164s) to really focus on innovation and

[02:47](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=167s) spend less time on the day to day busy work.

[02:50](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=170s) Agente AI is also redefining

[02:52](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=172s) what's even possible for our customers.

[02:56](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=176s) Signaling the shift from manual tasks

[02:58](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=178s) to highly connected, automated

[03:01](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=181s) and accessible workflows.

[03:04](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=184s) All of this is allowing our customers to unlock

[03:06](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=186s) faster,

[03:07](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=187s) smarter outcomes

[03:09](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=189s) from optimizing their site plans

[03:12](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=192s) to, um,

[03:13](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=193s) streamlining design iterations to

[03:15](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=195s) automating post-production sites.

[03:20](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=200s) And so that's why we built Autodesk Assistant.

[03:23](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=203s) Autodesk Assistant is your agentic AI

[03:25](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=205s) partner that speaks, design, and make.

[03:28](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=208s) From day one it's able to do three things

[03:30](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=210s) automate the manual,

[03:32](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=212s) connect the disconnected,

[03:34](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=214s) and deliver real-time insights all

[03:36](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=216s) in collaboration with, uh,

[03:38](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=218s) their human counterpart.

[03:40](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=220s) Let's jump into a quick demo to see it in

[03:42](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=222s) action. Oops.

[03:55](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=235s) OK, um, so right here

[03:57](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=237s) is Revit. Revit is our

[03:59](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=239s) building information and modeling software,

[04:02](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=242s) and on the right hand side here I have

[04:04](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=244s) Autodesk assistant.

[04:06](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=246s) The first thing I'm gonna ask assistant to

[04:08](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=248s) do is tell me more about the

[04:10](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=250s) building model that I have opened up

[04:13](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=253s) here. Um, this is a very common

[04:15](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=255s) like tell me, ask me type use

[04:17](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=257s) case,

[04:18](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=258s) um, very similar to software engineer

[04:20](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=260s) where maybe you're entering

[04:22](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=262s) a new code repo and so then uh

[04:24](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=264s) and you wanna be able to quickly get up to speed,

[04:27](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=267s) so the first thing you wanna ask is be able

[04:29](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=269s) to ask questions about it.

[04:31](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=271s) So in this case I'm gonna ask it to tell

[04:33](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=273s) me the window to wall ratio

[04:35](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=275s) of the building in my north facade.

[04:38](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=278s) Um, Autodesk assistant is gonna go in,

[04:40](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=280s) do its calculation, and return back

[04:42](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=282s) around 19%.

[04:45](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=285s) The next thing I'm gonna ask the assistant to do

[04:47](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=287s) is more of a do it for me use case

[04:49](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=289s) or like design with me use case.

[04:51](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=291s) Um, in this case I'm gonna ask the assistant

[04:53](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=293s) to take all these windows

[04:56](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=296s) we didn't like the 19% and modify

[04:58](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=298s) it to double hung windows with

[05:00](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=300s) slightly larger dimensions

[05:03](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=303s) so that um we're able to get a little

[05:05](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=305s) bit more sunlight.

[05:09](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=309s) Oh, behind the scenes, Autodesk

[05:11](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=311s) assistant is taking this prompt, routing

[05:13](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=313s) it to one of our AI agents, which

[05:16](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=316s) has a number of MCP servers behind

[05:18](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=318s) it. It's calling an LLM

[05:20](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=320s) which helps decide which, uh, MCP

[05:23](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=323s) server and tool to use,

[05:24](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=324s) which in turns calls one of the product APIs.

[05:30](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=330s) So assistant's going to try different things

[05:32](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=332s) and

[05:34](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=334s) Just like that, all my windows were modified,

[05:36](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=336s) um, so this is really powerful, especially

[05:39](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=339s) for users like me

[05:41](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=341s) who not an expert at Reddit, but I'm able to

[05:43](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=343s) go in, use natural language,

[05:45](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=345s) and make all these modifications.

[05:49](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=349s) Um, the next thing I'm gonna ask the assistant

[05:51](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=351s) to do is help me with some of my workflow

[05:54](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=354s) documentation,

[05:55](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=355s) um, type work.

[05:57](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=357s) So

[05:58](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=358s) once a model is complete, there's

[06:00](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=360s) a lot of work, a lot of manual work that

[06:02](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=362s) goes into

[06:04](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=364s) making it ready to be distributed to

[06:06](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=366s) other contractors or architects

[06:08](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=368s) to kind of take the design forward,

[06:11](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=371s) um, so the first thing I'm gonna ask the assistant

[06:13](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=373s) to do is create a floor plan view

[06:15](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=375s) of my building.

[06:17](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=377s) So it's gonna go in, create a new sheet of

[06:19](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=379s) my floor plan.

[06:21](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=381s) It's a little bit messy, so we need to clean

[06:23](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=383s) it up. Next I'm gonna ask the assistant

[06:25](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=385s) to apply a view template

[06:27](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=387s) on top of this,

[06:29](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=389s) um, and also help me annotate

[06:31](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=391s) some of the doors, windows and walls,

[06:34](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=394s) um.

[06:35](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=395s) So gonna ask the assistant to do that,

[06:38](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=398s) let it run

[06:39](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=399s) and assistant's gonna go in,

[06:41](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=401s) look at my current sheet, identify all those

[06:44](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=404s) objects,

[06:45](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=405s) and create a new view that has all those

[06:47](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=407s) different annotations.

[06:49](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=409s) So we're almost done. The last thing I'm gonna

[06:51](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=411s) ask the assistant to help me with is create

[06:53](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=413s) a cover sheet with this view,

[06:55](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=415s) um, so cover sheet has a

[06:57](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=417s) lot of our company standards, the numbering,

[07:00](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=420s) naming, etc.

[07:02](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=422s) um, so that's the last step

[07:04](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=424s) before we're able to share it with others.

[07:09](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=429s) So just like that I was able

[07:11](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=431s) to go from taking an existing

[07:13](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=433s) model, being able to ask questions about

[07:15](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=435s) it, uh, be able to

[07:17](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=437s) modify it through natural language and

[07:19](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=439s) then get it into a state

[07:21](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=441s) that is ready to be shared with others.

[07:26](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=446s) Next, let's look at the architecture that

[07:28](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=448s) powers all of this.

[07:30](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=450s) So starting with number one is our

[07:32](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=452s) MCP servers.

[07:34](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=454s) Our MCPs are a core component

[07:36](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=456s) of our Autodesk assistant architecture.

[07:39](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=459s) At at Autodesk we've been investing

[07:41](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=461s) in data and APIs for the last decade,

[07:44](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=464s) so MCPs is a natural extension

[07:46](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=466s) of that journey.

[07:48](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=468s) That allows us to bridge LLM

[07:50](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=470s) models

[07:51](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=471s) and our APIs to real world

[07:53](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=473s) actions.

[07:54](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=474s) We have both, uh, local MCP

[07:56](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=476s) servers as well as cloud MCP servers.

[07:59](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=479s) The majority of our customers

[08:01](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=481s) use Autodesk products through our

[08:03](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=483s) desktop,

[08:04](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=484s) um, but there's still a lot of integration with

[08:06](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=486s) our cloud services,

[08:08](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=488s) so that's why we support both.

[08:11](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=491s) Um, number 2 is our agents. We

[08:13](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=493s) have a wide variety of agents at Autodesk.

[08:15](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=495s) We have products specific agents like an

[08:17](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=497s) AutoCT agent or a Revet agent.

[08:20](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=500s) We also have, uh, more

[08:22](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=502s) general agents that span across multiple

[08:24](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=504s) products, so like a customer support agent

[08:27](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=507s) or an agent that helps with administration and

[08:29](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=509s) licensing.

[08:30](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=510s) These agents essentially provide the core

[08:33](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=513s) capabilities of Autodesk assistant,

[08:35](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=515s) everything from question and answers

[08:38](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=518s) to, um, helping automate

[08:40](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=520s) some tasks and workflows

[08:42](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=522s) and then within these agents another

[08:44](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=524s) thing important to call out is that there's a wide

[08:46](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=526s) variety of complexity.

[08:48](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=528s) Some agents are very simple and are simply

[08:50](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=530s) just calling an LLM to help with uh

[08:53](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=533s) MCP tool execution,

[08:55](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=535s) while other agents are a bit more complex and

[08:57](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=537s) have like a multi-stage workflow within it.

[09:01](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=541s) Another core component of our architecture

[09:03](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=543s) is our assistant back end.

[09:05](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=545s) How we've built Autodesk Assistant is

[09:07](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=547s) as a shared platform service

[09:09](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=549s) across our whole organization,

[09:11](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=551s) so any team across our,

[09:13](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=553s) you know, any team or product can bring

[09:15](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=555s) their agent or MCP server and

[09:18](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=558s) build on top of our platform.

[09:20](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=560s) Um, and so as a platform team we've

[09:22](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=562s) been focusing a lot of effort

[09:24](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=564s) in the shared capabilities like guard

[09:26](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=566s) rails,

[09:27](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=567s) context management,

[09:29](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=569s) um, how we're handling like observability

[09:31](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=571s) of token usage and LLM

[09:34](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=574s) tracing.

[09:36](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=576s) Another,

[09:37](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=577s) uh, key point is the

[09:39](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=579s) conversation proxy router. This is essentially

[09:41](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=581s) like the brains of Autodesk Assistant

[09:44](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=584s) because it is responsible for all the

[09:46](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=586s) routing of requests

[09:48](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=588s) across all our products

[09:50](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=590s) to the correct domain agent.

[09:52](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=592s) It also handles some of the agent to

[09:54](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=594s) agent communication that we have here.

[09:56](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=596s) Um, we use a number of different strategies

[09:58](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=598s) within this conversation proxy router.

[10:01](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=601s) In some cases we're using an LLM to

[10:03](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=603s) help with the decision. In other cases

[10:05](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=605s) we have more deterministic flows

[10:07](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=607s) where it's more like rule based.

[10:09](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=609s) So for a given product it'll route

[10:11](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=611s) to, it'll always route to a specific agent.

[10:15](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=615s) Um, so now when a user submits a

[10:17](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=617s) query they're interacting with our

[10:20](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=620s) assistant UI.

[10:21](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=621s) We have many different flavors of our assistant

[10:23](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=623s) UI. We have the embedded version that you

[10:25](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=625s) saw in the demo,

[10:26](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=626s) but we also have this in a web version.

[10:29](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=629s) But regardless of where you're accessing assistant,

[10:31](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=631s) you're always gonna get the same look and feel

[10:34](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=634s) and overall general experience is

[10:36](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=636s) gonna be the same.

[10:38](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=638s) The assistant UI plays a very important

[10:40](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=640s) role in the sense that it passes

[10:42](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=642s) the user prompt to our back end,

[10:45](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=645s) but in addition to passing the user prompt,

[10:47](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=647s) it also passes

[10:48](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=648s) applicable context.

[10:50](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=650s) Um, this context can be like who the user

[10:52](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=652s) is, where the user is coming from,

[10:54](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=654s) what product they're from.

[10:56](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=656s) Um, what license do they have, all

[10:58](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=658s) the applicable MCP tools,

[11:00](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=660s) and this is really important because we use

[11:02](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=662s) this context to help with the

[11:05](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=665s) decision making

[11:06](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=666s) for agent selection

[11:08](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=668s) as well as MCP tool selection.

[11:11](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=671s) So once the um

[11:14](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=674s) request gets routed to one of the agents,

[11:16](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=676s) the agents process that request and

[11:18](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=678s) sends it back

[11:19](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=679s) to the assistant to UI to

[11:22](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=682s) be uh exposed to the user.

[11:24](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=684s) Um, and that is essentially our end

[11:26](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=686s) to end flow of how we process a

[11:28](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=688s) requests through our assistant architecture.

[11:30](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=690s) Uh, I'm now gonna pass it off to Cejil who's

[11:33](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=693s) gonna go over Agent core and some of

[11:35](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=695s) the underlying services.

[11:37](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=697s) Oh Folks,

[11:40](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=700s) um, Sahil, I'm solution

[11:42](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=702s) architect, um, with AWS

[11:45](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=705s) specializing in generative AI and agentic

[11:47](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=707s) AI, and I work with, uh,

[11:49](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=709s) strategic partners like Autodesk in

[11:51](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=711s) building next generation of generating AI

[11:54](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=714s) applications,

[11:55](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=715s) so. Autodesk was

[11:58](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=718s) building this whole agentic workflow. They

[12:00](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=720s) realized at a very early stage

[12:03](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=723s) that building these agents are

[12:05](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=725s) great. It's good for business,

[12:07](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=727s) but taking it to production.

[12:12](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=732s) Are, uh,

[12:13](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=733s) that, that, that caught their attention is

[12:16](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=736s) around the performance, scalability,

[12:19](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=739s) security, and the governance of agents and the workflows

[12:21](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=741s) that they, they were building.

[12:25](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=745s) A platform team was building agents.

[12:28](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=748s) They, they, they took a step back. They

[12:30](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=750s) tried to make it more like a platform strategy

[12:33](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=753s) rather than building it as a bespoke

[12:35](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=755s) or a snowflake agents.

[12:37](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=757s) And during, during the exploration

[12:39](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=759s) phase,

[12:40](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=760s) there are a couple of challenges

[12:42](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=762s) that organizations like Auditors

[12:44](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=764s) figured out at an early stage, specifically

[12:47](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=767s) around how to get. A secure compute

[12:49](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=769s) runtime environment for agents

[12:52](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=772s) as well as for their MCP servers.

[12:54](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=774s) How to get this centralized contextual

[12:56](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=776s) management so that all the industries

[12:59](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=779s) across Autodesk

[13:01](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=781s) can have the same contextual information

[13:03](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=783s) when the workflow goes between the agents?

[13:06](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=786s) What is the centralized identity and the

[13:08](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=788s) excess governance that they needed

[13:10](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=790s) on the top of Autodesk assistant?

[13:13](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=793s) And moreover,

[13:14](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=794s) how to discover or connect with the custom

[13:16](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=796s) MCP servers or a cross domain

[13:19](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=799s) agent for any purpose-built

[13:21](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=801s) workflows and for

[13:23](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=803s) without saying it, auditability and observability

[13:25](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=805s) is one of the callouts and. Auditors

[13:28](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=808s) figured out at an early stage,

[13:30](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=810s) these are the things we cannot let all the

[13:32](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=812s) industry teams build by themselves.

[13:34](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=814s) Why don't we have it as a platform strategy

[13:36](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=816s) so that everybody can plug it in,

[13:39](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=819s) use the best practices, and build their workflows

[13:41](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=821s) on top of it.

[13:44](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=824s) Saying that that was the Autodesk platform

[13:46](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=826s) approach.

[13:47](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=827s) AutoDisk built a centralized

[13:49](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=829s) Autodesk assistant which is uh

[13:51](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=831s) frontend UI so that all the end

[13:53](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=833s) users across different

[13:55](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=835s) industries and personas will have

[13:58](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=838s) same consistent experience. They

[14:00](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=840s) will not see a different UI

[14:02](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=842s) behind the scene.

[14:03](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=843s) They will be talking to platform components

[14:06](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=846s) that I'll be going in the next slide,

[14:08](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=848s) and all the domain agents or MCP

[14:10](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=850s) server will integrate to this platform

[14:13](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=853s) to make sure that they get the best out of

[14:15](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=855s) what has already been vetted on.

[14:18](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=858s) Going next, this is a high level overview of

[14:20](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=860s) how Autodesk laid it across.

[14:22](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=862s) Like Matt talked about how Autodesk

[14:25](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=865s) built this centralized agent, and that's

[14:27](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=867s) where Autodesk use agent core runtime

[14:29](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=869s) and use strands as a framework

[14:32](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=872s) to power all the interactions

[14:34](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=874s) or the workflow to the domain agents and MCP

[14:36](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=876s) server. So every time a user query

[14:39](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=879s) comes in.

[14:40](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=880s) This is a centralized orchestration agent

[14:42](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=882s) power on strands that take that

[14:44](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=884s) call, whether that query needs to be solved

[14:46](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=886s) by a

[14:47](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=887s) default agent, a domain agent, or

[14:49](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=889s) a support agent. And all these agents

[14:52](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=892s) have their own native integration to a hybrid

[14:54](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=894s) MCP servers.

[14:56](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=896s) Moreover, Autodesk being doubled

[14:58](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=898s) down onto Agent Core Gateway because

[15:00](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=900s) Autodesk have invested a lot

[15:02](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=902s) on API, on data,

[15:04](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=904s) and how to quickly

[15:06](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=906s) convert those APIs into

[15:09](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=909s) MCP servers. That's where

[15:10](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=910s) Autodesk use.

[15:12](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=912s) Code gateway

[15:13](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=913s) where all the AutoDisk APIs that are open

[15:15](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=915s) API enable

[15:18](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=918s) are being directly exposed through agent

[15:20](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=920s) code gateway and being exposed

[15:22](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=922s) as an MCP server.

[15:24](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=924s) Moreover,

[15:26](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=926s) all the existing MCP servers

[15:28](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=928s) that have been created or been built

[15:30](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=930s) have been interfaced behind agent code gateway.

[15:33](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=933s) And if you look at the top.

[15:35](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=935s) Audit deck with a platform mindset,

[15:38](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=938s) they made a couple of uh uh

[15:40](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=940s) capabilities as a centralized platform

[15:42](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=942s) capabilities

[15:43](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=943s) coming from guard rails. Every conversation

[15:46](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=946s) that is coming in or going out of

[15:48](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=948s) Autodesk assistant

[15:49](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=949s) has been vetted thoroughly.

[15:51](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=951s) It has all the guard rail policy.

[15:53](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=953s) been inferred at the time of

[15:55](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=955s) inference.

[15:56](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=956s) Similarly, Autodesk use leverage

[15:58](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=958s) agent core memory and AWS surveillance

[16:01](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=961s) services to store all the

[16:03](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=963s) short term and the long-term conversation

[16:05](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=965s) so that all the agent workflows that is

[16:07](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=967s) going across the domain have the same

[16:09](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=969s) contextual information.

[16:11](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=971s) Agent core identity has been leveraged

[16:14](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=974s) to power all the MCP workflows

[16:16](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=976s) and to make sure

[16:17](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=977s) agents have the centralized uh

[16:19](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=979s) identity while interacting with the underlying

[16:22](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=982s) or downstream applications

[16:24](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=984s) and Autodesk also build a hybrid

[16:26](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=986s) cloud. MCP server

[16:28](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=988s) powered on AWS Serves

[16:30](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=990s) for all the cloud MCP as well as the

[16:32](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=992s) desktop MCP.

[16:34](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=994s) I know I talked a lot about Agent Core.

[16:36](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=996s) Let me give you a

[16:38](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=998s) quick overview what Agent Core is

[16:40](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1000s) for people who don't know about Agent Core.

[16:42](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1002s) These are a set of fundamental services

[16:45](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1005s) that Amazon released

[16:47](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1007s) 6 months back, I would say, and it got

[16:49](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1009s) GA very recently.

[16:51](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1011s) Uh, which, which

[16:52](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1012s) helps our customers to build,

[16:55](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1015s) scale, or roll out agents to

[16:57](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1017s) production quickly.

[16:58](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1018s) In agent core, the fundamental

[17:00](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1020s) concept.

[17:07](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1027s) Primitives and

[17:09](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1029s) you don't have to use all of them. You can use

[17:11](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1031s) what is required for your agent protocol.

[17:14](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1034s) Agent Core also offer you open

[17:17](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1037s) from uh model support. You can have

[17:19](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1039s) interaction with model from Bedrock,

[17:21](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1041s) from OpenAI, whatever your model inference

[17:24](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1044s) platform is, and you can use any framework

[17:26](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1046s) of your choice.

[17:27](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1047s) I'll quickly touch on a couple of things that AutoDisk

[17:30](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1050s) use and that that has been used as a centralized

[17:32](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1052s) platform, specifically around runtime.

[17:35](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1055s) Autitork figured out like many of the industry

[17:37](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1057s) teams have their own preference. On the framework,

[17:39](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1059s) a couple of teams use

[17:41](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1061s) Landgraf. Few teams are

[17:43](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1063s) comfortable with crew AI Strands

[17:45](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1065s) is predominantly,

[17:46](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1066s) like many teams use,

[17:48](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1068s) so Autodisk use Asian core runtime for

[17:50](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1070s) a secure, isolated

[17:53](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1073s) compute infrastructure so that all

[17:55](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1075s) the industry teams can just plug into it

[17:57](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1077s) and have

[17:58](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1078s) a production ready computer compute

[18:00](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1080s) environment for them.

[18:02](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1082s) Running their MCP servers or their

[18:04](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1084s) domain agents.

[18:05](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1085s) Agent Code Gateway is

[18:07](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1087s) a surveillance offering that lets you expose

[18:10](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1090s) your

[18:11](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1091s) open API spec, your existing

[18:13](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1093s) MCP server, or any lambda

[18:15](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1095s) functions that you have built for your

[18:17](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1097s) business workflow. It helps you to integrate

[18:20](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1100s) and give you a quick turnaround for

[18:22](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1102s) MCP interfaces along with agent

[18:25](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1105s) core identity.

[18:26](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1106s) And finally on the agent core memory

[18:28](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1108s) to have this centralized contextual management

[18:31](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1111s) and to make sure

[18:32](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1112s) that the workflow have the

[18:35](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1115s) short term

[18:36](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1116s) information and all the

[18:37](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1117s) previous conversation that happened with Autodesk

[18:40](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1120s) assistant AutoTk vetted on

[18:42](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1122s) agent core memory and use all the short

[18:44](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1124s) term and the

[18:45](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1125s) long term memory to power the workflow.

[18:49](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1129s) Going next, uh, I wanna quickly touch on

[18:51](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1131s) Strands agent because, uh, when

[18:53](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1133s) many teams within Autodesk were

[18:55](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1135s) using different framework,

[18:57](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1137s) there is also, uh,

[18:59](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1139s) a lack of opinion. What should we go

[19:01](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1141s) ahead with, and that's where Autodesk made Strands

[19:03](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1143s) as a framework of choice

[19:06](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1146s) so that, uh, all the industry teams while

[19:09](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1149s) building their agentic framework can

[19:11](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1151s) quickly get on boarded, have a native integration

[19:14](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1154s) with Agent Core.

[19:16](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1156s) Sorry. Couple of features

[19:18](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1158s) about Strand, it has support for

[19:20](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1160s) all the open source protocol.

[19:22](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1162s) It has support for MCP, A2A,

[19:24](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1164s) easy to build,

[19:25](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1165s) and Autodisk have seen

[19:27](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1167s) greater adoption, a seamless adoption

[19:29](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1169s) of strands, and it accelerates

[19:31](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1171s) the development cycle for all the industry

[19:33](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1173s) teams to quickly build the agents.

[19:36](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1176s) Going, I know we have a couple of seconds

[19:38](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1178s) left. I'll quickly go over the key takeaways.

[19:41](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1181s) Um, artists realized that while

[19:43](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1183s) they were building a system

[19:45](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1185s) like concurrent sessions, they need a

[19:47](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1187s) scalable runtime environment and that's

[19:49](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1189s) where they leverage Agent core runtime

[19:52](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1192s) with other AWS surveillance options

[19:54](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1194s) that they were using

[19:55](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1195s) Platform component, uh,

[19:57](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1197s) they unified the framework and make

[19:59](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1199s) sure. Agents

[20:01](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1201s) and MCP servers are common

[20:03](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1203s) so that industry teams don't have to swing

[20:06](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1206s) between different kinds of services and,

[20:08](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1208s) uh, get to the work. I know we,

[20:11](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1211s) but at high level, these are the key takeaways.

[20:13](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1213s) I will go to call to action.

[20:16](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1216s) Deep dive onto Agent Core. We have a

[20:18](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1218s) lot of samples there.

[20:20](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1220s) We have also built what we build for Autodesk

[20:22](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1222s) Assistant as an agent Omnimesh, which is

[20:24](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1224s) an open source framework of

[20:26](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1226s) multi-agent collaboration. We encourage you

[20:28](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1228s) to test it in your AWS account and

[20:31](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1231s) finally, we encourage you to check

[20:33](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1233s) Autodisk Assistant in action to see all

[20:35](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1235s) those cool features.

[20:36](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1236s) With that, thank you very much. We will be

[20:38](https://www.youtube.com/watch?v=4i4ybcj8eeY&t=1238s) around here, so if you have any question, happy to answer.

