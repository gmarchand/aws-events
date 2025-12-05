# AWS re:Invent 2021 - SaaS architecture patterns: From concept to implementation

[Video Link](https://www.youtube.com/watch?v=j7Sqt8GpYl0)

## Description

SaaS architecture varies across domains, stacks, and customer requirements. However, there are well-defined patterns that must be addressed by SaaS solutions. Identity, onboarding, tenant isolation, data partitioning, tiering—these are among the patterns that, while implemented differently on AWS stacks and services, are core to most SaaS solutions. In this session, take a detailed dive into the landscape of these SaaS patterns. For each one, we’ll move from concept to implementation, looking at the permutations of architecture and code that are used to bring these patterns to life with different compute, storage, identity, networking, and management constructs.

Learn more about re:Invent 2021 at https://bit.ly/3IvOLtK
 
Subscribe: 
More AWS videos http://bit.ly/2O3zS75 
More AWS events videos http://bit.ly/316g9t4

ABOUT AWS
Amazon Web Services (AWS) hosts events, both online and in-person, bringing the cloud computing community together to connect, collaborate, and learn from AWS experts.

AWS is the world’s most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally. Millions of customers—including the fastest-growing startups, largest enterprises, and leading government agencies—are using AWS to lower costs, become more agile, and innovate faster.

#AWS #AmazonWebServices #CloudComputing

## Transcript

(upbeat music) Hi, everybody. Thanks so much for joining my session today, As the slide says, my name is Tod Golding, and I'm a partner solutions architect at AWS, and I'm part of a team that's called the SaaS Factory. That team works with organizations that are involved in building and delivering and operating SaaS solutions on top of AWS. And obviously, in the last few years, our team has been responsible for creating a lot of content and a lot of best practices guidance, the SaaS Competency, reference architectures and so on with the goal of really helping SaaS developers better understand what it means to build and deliver a best-practices SaaS solution on top of AWS, and certainly we've got these reference solutions. We've got these sort of end-to-end examples of what it means to build a SaaS solution, but we also know that people need sort of guidance on just, what are the general sort of patterns? How do people address identity? How do people address billing? How do we go after isolation? So today we're really gonna take a slightly different approach to this. Instead of sort of going deep in any one specific architecture, so EKS or serverless, instead, we're gonna look at sort of the landscape of SaaS patterns, if you will. We're gonna look at all the different sort of nuanced different ways and pieces of the SaaS puzzle that you need to be thinking about as a designer and an architect and somebody who's trying to build a multi-tenant system with the idea that if we can sort of expose you to this entire landscape of options, you can then sort of think about how these apply to your environment, how they might influence your solution, and how you might use them to compose the architecture that best meets your needs. Now, again, this is a 300-level session, so we're intentionally kinda not digging into code here or opening up the IDE or sort of wandering into the depth of how to build any one specific one of these solutions. Instead, we're gonna go across the breadth here, right? We're gonna just try to look end to end at all the common patterns, and these patterns don't necessarily break out like Gang of Four patterns. They don't fall into this hierarchy so naturally, but we generally should be able to give some labels and some homes to these things that should give you a terminology and a vocabulary for talking about SaaS as you try to build your own solutions. Now, obviously as we talk about patterns and we talk about how to build SaaS solutions, the word that often comes up here is a blueprint, right? Lots of people will come to me and say, "Hey, Tod, we're ready to build this solution. "I'm talking to somebody about "what it looks like to build multitenancy. "Can you give me the blueprint "for building SaaS on my solution?" And the reality is there really is no blueprint for SaaS, right? There is no one sort of, grab this architecture, use it, and this is the best-practice architecture. Yes, we have examples of ways to do that, but in reality, SaaS is more the hybrid of all of these different architecture sort of mechanisms and components coming together to address your needs. So you're not gonna just take your code, run it through some machine, and then have it somehow spit out a SaaS solution on the other side. Instead, you're going to look across the landscape of possibilities and figure out which of those options best meet the needs of your existing environment. And if we sort of look at the patterns that are out there, I've tried to give a bit of a home to these patterns, a bit of categories to these patterns, and these are just a better way to sort of think about what it means to build SaaS on top of AWS. So one grouping here is what I would call the management group. This is where all the management of operational sort of patterns show up. This is where we think about what it means to provide a unified pane of glass that is used to manage an operator bit. So here we'll look at things like metrics and analytics and what it means to analyze the trends and activity of our tenants. We'll look at billing, 'cause billing's obviously fundamental. How do we implement subscription and other kinds of billing constructs? We'll look at what it means to provision tenant environments, right? How do I set up, configure, and create these environments? The other category we'll look at, and it's the one a lot of people sort of like to hover around the most, is this application category, and here, the patterns are more about multitenancy. How do I actually implement multitenancy inside my application? How do I implement isolation? How do I partition data? How do I think about how my app is going to be deployed? Am I gonna have silos for tenants? Am I going to share tenant infrastructure? And routing even shows up in this group, right? How am I gonna get the load to the different deployment footprints in my environment? The other category here is what I call tenancy, and this is more about, how do I establish sort of tenancy inside a SaaS environment? So here, we're looking more at like, how do I create a SaaS identity? How do I create and bind users to a tenant identity? How does that authentication and authorization experience work? I'll look at onboarding like, how does a tenant get into the new system, and then how do I even just create tenants in the system? How do I give them an ID and a plan and configure the policies of that tenant? And then tiering often shows up here as well like, how do I present different experiences to different tenants? So a basic tier tenant might have a slightly different experience than an advanced tier tenant, for example. So here, if you look across this top, this is not meant to be the ultimate list of patterns, but these are the sort of silos. These are the different sort of families of patterns that we're going to explore. But the real takeaway here is, across all these different families, what our job really is as SaaS architects and SaaS builders is to figure out, how do these specific patterns apply to my solution, right? What kind of identity pattern is best for me? What kind of isolation pattern best meets the needs of my environment, right? And here's where, when I talk to SaaS organizations, where we often have to start that conversation, right? So instead of just saying, "How am I going to do data partitioning?" we have to start with like, what are you trying to achieve as a business? What are the personas of the different tiers of tenants you're gonna have in your environment? How are they gonna consume your system? Are we starting at a legacy environment, 'cause certainly our path and the patterns we use might be heavily influenced by the legacy environment. So really it's the mix of the realities of your current environment plus these patterns that lets you sort of compose this overall SaaS architecture. Now, whenever we talk about SaaS, if we sorta step up a level from the details of individual patterns, there are two sort of high-level domains that we talk about when we talk about SaaS architectures. We'll certainly talk about this control plane, and this control plane is really where all the horizontal services of your SaaS application live. So here you'll see that we have things like onboarding and identity and all of these sort of constructs that are here to support and operate and manage our SaaS environment. And so we'll dig into that control plane and look at all the different pieces that are part of that control plane, but it's really important to note that the control plane isn't a multi-tenant environment itself. It is the management and operation experience of your multi-tenant environment. Where all the multitenancy really shows up is in your application plane, and the application plane is where your multi-tenant business services and application components, and this is where we're gonna implement tenant isolation. This is where we're gonna implement data partitioning. This is where lots of our energy goes into figuring out, what's the right microservices for our multi-tenant environment? How are people going to authenticate into our environment and so on? And so whenever we talk about SaaS applications, you'll always hear us talking about this particular concept lives in the control plane, or it lives in the application plane, and we'll sort of take our path through this with that control plane and application plane in mind. Now the other thing I wanna note here is this sort of notion of what it means to be a SaaS application or a SaaS service, right? I will have people who will come to me and they will have built an application, and they'll build basically the application plane side of this experience. They'll have multi-tenant services. They will have built isolation, and they'll think, "Hey, we're ready for multitenancy," and then I will ask questions about, well, what have you done on the control plane side, right? Do you have automated onboarding? How are you tracking metrics and analytics about your tenants? Do you have a fully automated provisioning experience for each one of your tenants? Do you have this rich operational view of what's going on inside your tenant environments? And to me, if you don't have the control plane piece of this puzzle, you don't really have a SaaS service, right? If I have a great SaaS application and a great multi-tenant implementation in my application plane, but I can't sort of get all the innovation and the agility and all the goodness that comes from this control plane, I really can't operate as successfully as I could as a SaaS business. Now, when we talk about SaaS environments across this entire discussion of patterns, you're gonna hear some terms that are really common terms here. The term silo you're gonna hear come up from us a lot, and silo is really meant to describe a SaaS environment and a SaaS architecture where the resources of a tenant are dedicated to an individual tenant. This doesn't mean the entire stack is dedicated to the tenant. It could be that just some resource is delivered and offered in a per-tenant basis and that resource is siloed. And it's important to note that even if I run a full stack silo, all tenants running their own infrastructure, if I have that control plane that manages and operates this, I'd still consider that a multi-tenant SaaS environment. Yes, some resources are shared and some resources are dedicated, but to me that's still a multi-tenant SaaS business. Now on the opposite side of silo, you'll also hear us use the term pool, and pool is really used to refer to the sharing of infrastructure, and this is the more classic definition of multitenancy. Here, tenants are sharing some resource. And again, this is super granular. I could be in an environment where some resources are shared and some are actually siloed, but in general, when a resource is shared by tenants, we refer to that as a pooled model. Now, historically, we've also talked about this bridge model and use this term to refer to tenants that are using a mix of both. I think longer term, we'll sort of phase out this notion of a bridge, but we do wanna acknowledge that everything isn't just silo, everything isn't just pool. There's obviously this mode in between where some things are siloed and some things are pooled. Anyway, this terminology is gonna be used across the rest of the presentation, and hopefully it's very clear what we're talking about when we talk about silo and pool. Okay, so enough background. Let's start looking at the actual moving parts of the control plane. What services are in the control plane, what functionality is there, and what do we need to do in them? And we're gonna start with one of the most important pieces of the control plane, which is this onboarding experience. How do we onboard and get new tenants into our system? How are they created? How are they provisioned and configured? And this is a really common pattern across all of the solutions that we describe, and here you'll see I'm gonna describe this as Lambda services, but this could be ECS, it could be EKS, it could be EC2. The idea is that I have these microservices and they're being orchestrated in this onboarding flow. So when a tenant comes in and the tenant is going to be registered and onboarded into my system, they'll come into this registration service. Now it's important to note that that registration could have been triggered by a self-service experience that was a classic, say, B-to-C experience, or it could be something internally triggered by an internal mechanism. Either way, from the registration experience down, all the automation of that would be exactly the same in both those scenarios. So here we hit the registration service. It's now gonna hit the tenant service, and that tenant service is now gonna configure all the information about a tenant. What's their ID? What's their policies? What identity settings might they have that we need to keep track of, and so on? And then we're also going to provision a user here. So when we provision a user, we're setting up that first user in our system that is gonna be the first sort of tenant admin, if you will, of this user, and then that experience actually is gonna have to go out to our identity provider, and here I've shown Cognito. I could be showing Okta or Auth0 or Ping or any identity provider, but the key here is I have to create a user in that experience. In this case, I create a user pool in this example for each tenant, 'cause that's a Cognito construct, and then you'll see here I create and populate custom claims, and these custom claims are what connect our user identity to our tenant identity. So when we're all done with this, in the custom claims, you'll see tenant identifier, you'll see user information, and when I authenticate this user and bring them into the system, I'll actually get a token that comes back that includes all of that tenant context, and we'll talk about how that gets used later on. You might also find that I provision policies here for the user. These could get provisioned here. They also could get provisioned in other phases of the process. Where this happens kinda depends on the nature and the deployment model of your solution, but I at least wanted include the fact that these get created somewhere in this process. So now I've got my tenant created. I've got my user created. I also typically in this pattern have some onboarding experience that I have to go through for the billing system. So somewhere out there, I've set up my billing system. I know I'm gonna bill tenants. Well, now a new tenant's showing up. I have to provision that new tenant into that experience. So here, this is where we'll see different billing providers showing up, Chargebee, and we'll talk a little bit more about the role of those providers in this experience. And then the last step is the one that often has a lot of complexity to it, which is this provisioning step. If I'm running a pooled environment where all my tenants are sharing infrastructure, the onboarding of a new tenant might not mean we have to create very much infrastructure at all, or it turns out if I've got a siloed model where tenants need their own infrastructure, the onboarding will actually have to provision infrastructure for each tenant, and you'll see this show up in the different reference architectures that we offer. So this is often an overlooked piece of this 'cause people won't think of provisioning and setup of new infrastructure as part of their onboarding process, but it's absolutely an essential part of it for some deployment models. Now, one way this shows up and one way that provisioning sort of gets impacted by this is by what we would call tier-driven onboarding. So in this model, essentially a tenant comes in, they register, they tell us what tier they are. Are they basic, advanced, platinum, or whatever? Certainly we're gonna set up the tenant, the user, do all those other bits we're going to, but we're also gonna go off to this provisioning experience, and the provisioning experience will actually now provision dedicated resources for that tenant, siloed resources that are needed for them individually. This flow is all driven by what tier you provided to me, and all has to be part of my onboarding experience. It can't be some experience somehow outside of the onboarding world. Now if you look at what this actually looks like in practice, in action, and you go look under the hood here of one of these solutions, well, let's say for example, and this is exactly, by the way, what our serverless SaaS reference architecture does. I come in, I've got these pooled tenants. These pooled tenants have some microservices. They've already been provisioned and configured. They're all just shared by all the tenants, and so adding a new tenant here simply adds a new tenant that consumes those resources. There's probably other bits that are getting configured, but in general, it's gonna just consume the existing microservices that are running for us. And then in this system, let's say I have a siloed customer. That siloed customer's in this platinum tier plan, and so they have their own dedicated resources running in this silo. And now if I onboard another tenant and they indicate to me that they're a platinum user, I have to kick off some provisioning process that's gonna provision that user's resources into my environment. Okay, so that's kind of the onboarding piece of that. Now, another huge part of the control plane is this notion of identity, and when we talk about multi-tenant systems, it's really important to have what we'd say, to have tenant-aware identity. It's not enough just to be able to authenticate against any identity provider. We have to authenticate in a way that introduces tenancy into our environment. So here, if I have an identity flow or a tenant is coming in and they're authenticating into my system and they hit my web app, when they hit my web app, they're gonna be redirected to an identity provider, again, Cognito, Auth0, whatever it is, and now when we authenticate in that environment, we now know the binding of the user to that tenant, and this is where those custom claims come into place. Those all come back here. We'll get an identity token and an access token back. We're describing like an OIDC kind of authentication here, and those tokens will be enriched with tenant context. They'll tell me not just what user I am, but what tenant I'm related to, what tier I am and so on, and now that piece of information will flow back into the services of my application. So now when I'm in some application service and I need tenant context, I don't have to go somewhere else to get it. I can open that JWT token, peek inside of it, get the tenant ID, get what other tenant context I need, and I get really good efficiency out of that. And if I call another service, I can simply pass that same token along to the next service, and that service can now rely on it as well. And so this is this whole notion of tenant-aware identity, which is to say we're really passing tenant context through all of our experience in a way that everybody sort of has it at their fingertips and can use it to access data, record metrics, or whatever they need to do. Now if we look at a flow for that and what sort of an authentication flow might look like, well, here's one where I've got a tenant coming in. They're coming into the application. They're using a subdomain to come in in this case, so there's multiple ways to come in here. We won't get to dig into all those, but when I come in, I say, "Hey, I've got a tenant. "They wanna authenticate," and in this case, because I don't know what to authenticate you against, I have to actually go out to tenant management, which is where I stored your identity settings and all the other information, which user pool you're running against and so on, and I have to pass that information back to the app. And in this example, I show the app saving that off in this authorization library, and then that authorization library will now use that tenant context to go out to Cognito and authenticate a user. So here, you'll see it's authenticating against this specific user pool. That's the user pool I got from down below in tenant management. Then that will return a code, and then that code will be exchanged for a JWT, and all of this is just following standard OAuth kind of flow, but now that I have that JWT token back, that JWT token has all that SaaS goodness that we talked about baked into it, and so now that JWT token can get passed down to the microservices of my application. So here it goes to my product service, and the product service has all that goodness. So really the pattern here is, when I authenticate, I wanna authenticate in a SaaS context and I wanna get a token out of that experience that has all that goodness baked into it so that doesn't have to be resolved somewhere else downstream. Now, I talked a little bit about the fact that we were using a user pool per tenant, and I'm gonna get a little AWS specific here, which is, if you're in Cognito, 'cause a lot of our SaaS providers are using Cognito, one of the questions they really face is, should I do a tenant per user pool kinda mapping, or should I have one user pool for all tenants? And the reality is they're both valid. So in the user pool per tenant model, the real advantage here is that I can have separate policies for each tenant, right? I can set up whether you're MFA or what's your security, how soon your password might time out. All of those traditional things I'd set up about your identity, I can have separate settings per user pool here, and then that means per tenant, and that means I can actually offer that as a feature to tenants to be able to say, "Hey, you can manage and configure all of this on your own." However, in a user pool per tenant, now I've gotta resolve you to which user pool you're going to. There are limits on how many user pools I can have. So there's still questions about whether this would be a good fit, and to sort of highlight this, in our EKS reference architecture, we actually do the user pool per tenant model, but then in our serverless SaaS model, we have a model where we're actually using one user pool for all of our pooled tenants, and in this model, we get away from some of the scale challenges and some of the mapping challenges, but now I have to figure out which group you're in, and I have to think about how to still resolve, how to authenticate you. Just have to use a slightly different mechanism, but I don't have to worry about the limits of the number of user pools, so both of them are entirely valid. It really kinda depends more on the profile of your application. Obviously in the single user pool model, I also don't get to configure this. The policies are the same for all tenants, but either way, both of these are good solutions. I just think you have to sorta weigh the pros and the cons. Now also as part of identity, another pattern we see is a model where a customer may wanna bring their own identity to your SaaS solution, right? So I already have an identity solution for all my customers, but now some customer signs up and they don't wanna use my identity. They wanna use their own solution. So here I've shown two sort of on-premises environments with their own identity providers, and my own Cognito user pool that is managing the rest of my tenants. Well, what do I do in this case? Well, in this model, I have to have some kind of hybrid identity model where, as these tenants come in, they will hit some authentication manager. That is my centralized service, and that authentication manager will look at their configuration and say, "Oh, you're a tenant "that's configured my own Cognito identity. "I'll auth you there. "Oh no, you're authenticating "against one of these on-premises environments. "I'll authenticate you there." Now the challenge here is when I authenticate from one of these on-premises environments, I don't necessarily have all that other context that comes back from that authentication, so this is where we'll see people add what I call this sort of JWT enrichment tooling here, which will basically say, "Hey, I'm gonna go out. "I'm gonna take that information "that came back from the authentication, "enrich the JWT token," and now a JWT token just flows out of this experience, downstream to all my services, and whether I came from on premises or I came from Cognito, it all just looks the same to the downstream services. So I see some organizations really have to work through this, and so I wanted to represent this pattern because I think it is important to be able to not always assume that you're gonna own the identity experience. The last piece of identity I wanna talk about here is multi-region identity. Here, the challenge is, how do I sort of authenticate in an environment where I have multiple, I'm running in multiple regions? And certainly one approach to this is to have a common front door for all customers and tenants that are coming in to authenticate in your environment and have a centralized authentication and identity experience for all those different regions, and then just go through and pass that context through to those individual regions. However, this kinda model doesn't usually work out because organizations that are facing compliance or regional sort of considerations aren't able necessarily to host their identity in some shared, centralized place. So in this model, what we'll say is, instead we'll change that front door to something that will map you to the appropriate region, and we'll actually move the identity to the individual region, so now the identity lives in that region, and you're all good there. The other one, and I'll just hit on these two quickly. Obviously, inside the control plane, we also have user management, and that's two flavors of user management. That's the admin console where it's the ISV provider's users being managed in Cognito, and we also have the SaaS provider's users, the tenant users that are managed here, and the user management service is really needed for both of those roles in your system, but a pretty classic thing to have included here. Billing also shows up here in the control plane, and really billing has two specific dimensions to it: configuration and instrumentation. So when we talk about configuration and instrumentation, we're really talking about, what does it mean to get the environment set up to be able to be configured to generate a bill, and then how do I actually instrument my system to send it the data it needs to generate that bill? So if you look here, and I've got an example, some billing providers, Chargebee, Zuora, Stripe, so on. When I go set up an account with them, I have to go in and establish a relationship with them, set up my business with an account there, and I have to configure the billing plans with them, right? What kind of billing structure am I using? Subscription, consumption, number of users, whatever the sort of mechanism I'm using for billing, I have to go set all of that up. Then for my SaaS application, when a new tenant signs up, I actually have to go onboard that tenant to the billing system, right? I have to go create a relationship, create a customer in that system, and the logistics of that and the patterns of that vary based on these different implementations of these different billing providers, but the basic goal is the same: Get the account created here and orchestrate all of that, and it's usually a pretty straightforward process. Once I have all that set up, really now the key thing is generating and capturing the activity that is going to be used for my actual SaaS bill. So if you look here inside my SaaS application, somewhere in here I'm gonna go add the instrumentation to my environment that will capture events and activities, surface them, and publish them to my billing system, and eventually generate a bill. Now, which things should you instrument here? It kinda depends. This really depends on your plans. If you're subscription-based, you might bill one way and generate certain events here, might be feature-based or whatever. If you're consumption-based, you may need to instrument for consumption-based events. It's really sort of driven by what the needs of your environment are, but overall, this is the sort of classic billing component of the control plan. Now if you look at ways this gets implemented, there's lots of ways to implement this ingestion. It's pretty much an event ingestion model, an aggregation and a publication (indistinct) and we actually have a sample Stripe solution out there that illustrates how this works. But essentially here we show EventBridge coming in, taking a billing event, sending it to an aggregator. That aggregator aggregates the billing content, stores it in a database, and then periodically sends that billing information to the billing provider. Now the use of the aggregator here is debatable. You could say, "No, I wanna go straight to the billing provider," but in some cases, people really wanna capture that billing detail, they wanna have their own database of it, and they don't wanna rely on just the reliability of the billing system to successfully process all of their requests. They also don't want it to be necessarily as chatty with the billing provider, but a pretty straightforward integration. Now on the other side of this is the idea of metrics instrumentation and aggregation, right? Metrics is more about, how do I capture which features and functions of my system users are using? How can I capture information about the operational health of the system? This is all the data that's needed just collectively by the business to assess the business, the SaaS business, the SaaS architecture and so on. So here, we really are just setting up classic sort of aggregation and analytics tooling, right? There's no magic here. I showed two examples here, one with Kinesis, all the way through Redshift to QuickSight. You could also use Logstash and elastic search Kibana here to surface that information. Really where this gets more interesting is more on the instrumentation side of this, and here I think there's at least two categories of events. There's probably more here, but two common ones that are here are these system-level metric events, and the system-level metric events are ones where we're essentially finding out CPU and memory and other things that are naturally captured by the tooling like CloudWatch and other bits here, and then we have these application-based events that are more about my domain, right? These are specific things about how features and capabilities are being consumed for my application. And the idea is to aggregate all that up, and then surface it in a way that product managers and operations people and developers can all consume it however they want and make decisions about the architecture and the business and so on. The last piece of the control plane here is this whole notion of application plane integration, and the idea here is that we have this control plane. It's got all these common services in it. It's running in its own construct, but it still needs to interact with the application plane. It has to send billing events to it. It plays a role where it gets data back from the control plane that's used to manage the application plane, and here you'll see that I have two siloed models, and I have two siloed tenants, and a pool tenant environment. And really here, I need some kind of model of interacting with all of these environments that meets my security constraints and really sort of couples these together the way I want them to be coupled then, or I really am super loosely coupled, or is this a really tight integration? It's kind of up to me, but here's where you look at, do I use EventBridge here? Do I use PrivateLink? Do I use VPC peering? It all depends on the deployment model of your application. The key takeaway here is that I have to think about how I'm going to manage that application environment and integrate with that application plane environment from my control plane. Okay, so that's all the control plane bits. Those are all the horizontal bits and shared bits that are common to all of my tenants. Really not a lot of multitenancy in there. Now let's shift over to the application plane, and in the application plane, we'll look more at like, what does it really mean to implement multitenancy on top of AWS, and what are the patterns there? And we're gonna start with the most coarse-grained view of this, right? For some people, the move to SaaS is really all about just getting their system up and running, or some people will just choose a siloed model for their tenants because of the compliance or the domain considerations of their environment. But here really the goal is to say, what does it really mean to offer a full stack siloed implementation of your solution? And here, I'm gonna show different ways that you can implement a full stack silo, but basically silo here really means we're taking the notion of silo and saying every resource in the environment will be dedicated to a tenant, and one way to do this is in an account per tenant model. We'd essentially give each tenant their own account. There are some challenges to that. Setting limits and automation of some of this can be a little bit tough, but some people will use Control Tower here as well to help with some of this, but totally a valid model, and some people like the operational and the cost tracking of this. A really second common model here is the VPC per tenant model, and in a VPC per tenant model, we're essentially putting each tenant in their own VPC, but the good news here is they're all in the same account, and because they're all in the same account, they're a little easier to manage and a little bit easier to get some of the operational efficiency that we'd want out of this, and a little less difficult to automate than maybe the account per tenant model. And then the last one is this notion of a subnet per tenant. So we're now going inside the VPC and giving each tenant their own subnet. I see this one not nearly as often as the others, but I do include it just in case some are interested, but the basic idea here is that we're going to give tenants a full stack in a super valid common model, and this is still considered a multi-tenant SaaS model if we're managing and operating these silos with a control plane that automates onboarding, sort of centralizes identity, and so on. Now what I wanna do here is now walk in like we talked about. There's this silo model that's a full stack silo model, and I wanna get a little more granular, and what we're gonna do from here through the rest of the application plane is more look at, how does silo, pool, et cetera, play out on different AWS stacks, and how does it play out on different technologies? How does it play out on storage? How do we implement isolation? And each one of these are influenced based on the different stack or service that we're using, and so what I'm gonna try to do here is wander a range of stacks and services and talk to you about how the patterns are realized on each one of those. So for example, we're gonna start here with EKS, right? What does it really mean to implement EKS compute silo? So now it's not the whole stack, just compute. What would that look like? So here, if we look at an EKS environment, a slightly simplified version, and we said we were to spin it up, yes, we've got a Multi-AZ, highly available sort of classic, Well-Architected architecture here, and then one way we can implement silo here would be a cluster per tenant model. And in a cluster per tenant model, essentially each tenant will get a fully provisioned EKS cluster for them, and obviously, a lot of moving parts to that, but some people like that cluster-based model either for the isolation profile or the cost accounting model. There's a lot of reasons they see appeal in that. And so here, as each tenant comes in, we essentially create a separate cluster for that tenant. Now within EKS, however, there are multiple ways to implement the silo model of the compute. So here, here's an alternate approach. Same Multi-AZ model, same sort of setup, but now instead of having a separate cluster per tenant, we're actually gonna have a separate namespace for each tenant. So here, we will provision a namespace when a new tenant onboards, and now the overhead of that is not nearly as intense as the cluster per tenant model. Now everything's kind of within the cluster. It's a little simpler to set up and a little easier for us to use the natural EKS components to update, roll out, and provision the resources. And actually our EKS reference architecture, if you're looking on details on how to do namespace per tenant, it's got a really good example of how to set that up. So now each new tenant just gets added as another namespace in here, and we still get good isolation here, a good isolation story. It's just the isolation boundary now is a namespace. Sorta the third variation of this is what we'd call the EKS compute model, pool model, excuse me. And in the EKS pooled model, it's exactly what you think it'd be, right? So all we're really saying is we're gonna have a single cluster, and all the tenants will be running in that cluster. And some people would say, "Well, why not just do that for everything?" Well, there are certain isolation considerations that you have to think about here if you're gonna run in a pooled model. You have to do more work here in terms of how you set up your policies and how you ensure that the tenant's isolation model is going to work the way you want. Still a valid model. In fact, you'll see our EKS reference architecture showing adding a pool model to it alongside a namespace per tenant model to show you that you can have both of those. You just kinda have to accept what comes with this model, but totally good in terms of economies of scale, certainly simplifies deployment, just has a tougher isolation story here, and a tougher maybe story to offer different experiences to different tiers. Okay, now let's sort of pivot there, right? We talked about silo and pool in the context of EKS. Just for contrast now, let's look at what that would look like inside of serverless, and this drives home the point that the model for silo and pool is different depending on which stack you're working with. So here, and this is right out of our serverless SaaS, by the way, reference architecture, we actually have siloed tenants that are our platinum tier tenants. They've somehow got some special sort of designation, they're paying a higher price for their service, and they don't wanna share Lambda functions with other tenants, right? They don't wanna worry about concurrency issues. They're worried about isolation, potentially, considerations, and they want their own dedicated compute, even in a Lambda world where you'd say, "Well, they're only running in the context "of one tenant at a time anyway." Well, still, now these Lambda functions are actually deployed in the context of this individual tenant, and that helps with the isolation, it helps with concurrency, it helps with lots of things. So here, you'll see that we want two siloed tenants. They're both running their own environment, but in that same serverless SaaS solution, you'll see that we have a pooled environment running alongside of it, and the rest of our tenants who are in other tiers, basic, advanced, et cetera, are sharing the compute, and this is the pooled model that we've talked about. So if you look at all three of these, they look, well, they're exactly the same. What's different here is really just how they're onboarded and how they're configured and how they're set up, right? If I onboard a silo tenant, I'm gonna provision a whole new one of these. If I onboard a pool tenant, they're just going to go into the pooled model, but there's lots of moving parts behind orchestrating making all this work, and there are lots of implications that you'll see in terms of how this affects isolation and other considerations. Okay, now, I also wanna highlight the pack across... Hopefully like we saw EKS, we saw serverless, we saw how silo and pool plays out differently, I kinda wanna drive home this point that silo and pool is a resource-driven sort of decision, right? So across everything in AWS you touch, storage, queues, compute, whatever is you're touching, you're really making that silo versus pool decision on a resource-by-resource basis. And to drive that home, you'll see here I've got sort of an example here of a system. It starts out with I've got an order service. That order service has siloed compute because we've decided that, for noisy neighbor or some other reason, we want that compute to be siloed, but it's actually using pooled storage here. We've decided we can share the storage. And now when we go on to, and it interacts with our product service, in our product service, we have both pooled compute and pooled storage. So we've decided in this case that's a good fit for this, and that there's not a noisy neighbor concern, and the data can be commingled. We're all good. Now we go down to our invoice service, and our invoice service says, "I can do pooled compute. "That all works. "It fits for my model, but my tenants for invoice data "want the data to be siloed for that," right? Our experience needs it to be siloed, and there could be any number of factors that might drive that, but the key here is that, in this particular example, we have pooled compute and siloed storage. Now that goes on and interacts with a couple of queues, sends a message about the invoicing down through this queue to another system, and in this case, the queues could have been silo or pool. They could have been shared or they could have been separated, and finally we end up at a shipping system. It's pulling data off of these siloed queues, and it's running pooled storage and pooled compute. So the whole point here is to drive home the idea that the silo versus pool decision is really meant to be made at a much more granular level, and how you make it at each level will also be influenced by what's possible with each AWS stack. How you do this with EKS versus how you do it with Redshift versus how you do this with DynamoDB, they could all look different. Okay, so that's sort of, those are some compute and higher-level sort of silo/pool kinda concepts. We didn't get into ECS or some of those others, but the concepts map very much to those as well. I now wanna look at isolation, and isolation basically is, how do we ensure that one tenant can't touch the resources of another tenant? This is fundamental to SaaS environments, and what are the patterns here? And we're gonna start again at a higher level here when we talk about isolation, and focus first on what I'd call resource-level isolation, and again, here we're talking about silo-based isolation. In this case, our isolation model is one where a tenant is essentially isolated to a single resource, so a single database or a single compute mode, and here, the isolation boundary is actually that entire resource, and in a resource-based model, it's much easier to build an isolation model because we usually have constructs that will describe access at this level, right? We can say an entire database can only be accessed in these scenarios or by these tenants, an entire compute node can only be accessed here, so, much easier to describe this, and let's look at what that really looks like, right? So if we look at some siloed resources, how does isolation actually get attached, and when does it get attached? So here we're gonna look at deployment-driven silo isolation, which means isolation that gets applied to our resources at deployment time. So here I have a simple set of EC2 resources. They're running on behalf of Tenant 1. They're running in a silo, and now because I know these resources are dedicated to Tenant 1, I can essentially attach an instance profile to these EC2 instances that describe everything that these tenants can touch, what resources are available to them and scope it all down to what's valid for Tenant 1. So now when this compute goes to access other resources, it'll all be scoped to what's valid for Tenant 1. So now if I look at Tenant 2 in this same environment, I deploy Tenant 2, and these get deployed with this Tenant 2 scoping policy, now when Tenant 2 resources try to go access data, they can only access Tenant 2 resources. So I can't cross boundaries to Tenant 1's compute, and Tenant 1 can't somehow come over and access Tenant 2's data. And the beauty of this is the code running on these compute instances doesn't know anything about this. This is all done at deployment time. It's all attached as policies to this compute in a way that if I ever try to cross a boundary, I'll be prohibited. And if you look at this same model as it plays out on Lambda, very much the same thing. Now I have an execution role. When I deploy at deployment time a Lambda function, I can deploy it with a role, and now that role will control access to the resources for those Lambda functions, and now when Tenant 2 is deployed, it'll get deployed with its execution roles, and again, I can't cross the boundaries between them. Okay, so that is all sort of resource-driven and this more coarse-grained view of isolation, but we also have in a pool environment what we'd call item-level isolation, and in item-level isolation, now our resources and our tenant information is actually shared within a resource as individual items. So as an example here, I have a database table, and you'll see the individual items here are associated with tenants, but this could be a queue. It could be any resource. The idea is that we're moving inside the resource, and now individual items inside that resource are the things we need to isolate, and now this is where isolation gets much more tricky, because we usually have good constructs at the resource level for describing isolation, but now we're sort of at the mercy of what's available to us when we get to the item level, and actually each approach to isolating at the item level could be different. If we wanna look at an example of this and how item level plays out, now where we had deployment-time isolation earlier when we were talking about the silo, now we have to have what I would call runtime-applied or runtime-enforced isolation. We can't really do this at deployment time. So at runtime, when tenants come in and they try to access some resource, they're all coming into our environment against the same resource. It's a pooled resource, so what we have to do at runtime is our code actually has to go out, it has to say, "Oh, you're calling on behalf of Tenant 3. "Let me go find Tenant 3's policy, "and I'll apply that policy, "and I'll inject that policy "into the compute that's running." And the key thing here is that the compute, when it was deployed, it had to be deployed with a very wide context. It couldn't be scoped down at all. It had to support all tenants. So only now at runtime where we go resolve this tenant call to a policy and inject it, do we now, our code can now use the credentials back from that to go access a piece of data, and that's how we scope our access. So here, we're really looking at the difference of runtime versus deployment-time isolation, and the need for this runtime really comes with this move to item-level isolation often because that's where the intricacies get harder, and this is where we have more shared resources. If you wanna look at what that looks like, item-level isolation within a given resource, here's a sample policy. We show this one a lot. DynamoDB lets you get down to the item level and describe isolation. So you'll see that I have a description of a leading key that just talks about Tenant 1, and will constrain access to items that belong to Tenant 1. So now when I have this DynamoDB table that's got all these different tenants in it, this policy will ensure that it can only access data for item one in that table. So this is where that runtime policy comes to life. Now, if we were talking about a different AWS service, it would be a different policy and a different approach, but the concept is still the same and the pattern is the same, which is I need some policy that will constrain access to that item. Now, we talk about isolation certainly as one way of making sure tenants can't adversely affect one another. We also wanna be sure that, in a multi-tenant environment, one tenant can't somehow impose load that will affect other tenants. So if I have a basic tier tenant that's sending a million API requests, they could be affecting my platinum tier tenant. So we say as part of the patterns, you should have some kind of tier-based throttling in your system. And if we look here, here's an example of a tier-based throttling solution using API Gateway, and here, API Gateway has this notion of usage plans and API keys. So essentially we can set up separate API keys for each tier of our system. So a basic tier user could have one API key, an advanced tier, another API key, and then those API keys would map me to different usage plans that had different policies that would control their throttling separately. So now when a request comes in, a Lambda authorizer can sort of look up the API key, figure out what your usage plan needs to be, and then control the flow to the downstream requests. So if the basic tier is exceeding the limits of their usage plan, the throttling policies of that usage plan will get kicked in, and this will keep a basic tier tenant from affecting a higher-tier tenant potentially. Now obviously, I showed you API Gateway, and this is a perfectly good way to do it, but you can imagine with EKS, for example, I can set up service quotas inside of my namespaces and use that as a way to control throttling. The real takeaway here is that somewhere in the entry point to the services of your application, you oughta have some kind of tier-based policies that are used to decide how you'll apply throttling and ensure that you don't get one tier adversely affecting another. Now the other piece we wanna look at, we said we have all these cool things, like we talked about injecting JWT tokens and applying policies, but what does that really mean to the person who's writing microservices in your system? What's the impact on them? And one of the patterns we talk about here is you should be building microservices that make it as simple as possible for application developers. So if I'm writing a microservice, a product or an order service, I don't really wanna know how to deal with tenant context or tenant IDs. I don't really wanna know how to deal with these isolation policies. Can you take that all out of my view? And so what we're really saying here is build libraries, reusable libraries. If that's Java JAR files, if it's .NET assembly, if you're using middleware, whatever the language construct you're using, take all these multi-tenant constructs and multi-tenant libraries, and take them away from your code and make them reusable across your microservices. Now here I'm showing it with Lambda 'cause Lambda has this really cool thing called layers, and layers let me sort of put shared code one place and deploy it separately, and then share it across my Lambda functions. So here inside my layers, you'll see I have all these helper functions. I've got a log manager, a metrics manager, that are used to just generate tenant contextual logs and metric events where the service doesn't know about it. I have access to this token vending machine, another piece of sample code we have out there, that will let me go get the credentials in this runtime resolution of policies, that example we talked about earlier for isolation, and I've got this token manager that just resolves. It cracks open a JWT and gets me a tenant ID. So the basic idea is I care less about what's in the specific libraries and more that you have these libraries, and that you're moving tenant details away from the microservice developers. Now we're also gonna touch very quickly here on data partitioning, and we're gonna move through this fast because the models and the ideas of data partitioning are pretty straightforward to me. You have silo, we have pool, really. In the silo model, we're basically saying each tenant's gonna get their own storage construct. If that's EKS, I'm sorry, if that's Redshift or if that's DynamoDB, each one of those different storage technologies has a different way to represent silo. Could it be a separate database per tenant? Could it be a separate cluster per tenant? Each one of those is different, and we have guidance on those, but the basic principle is you're picking some unit of that storage technology, and you're not commingling data there, right? That data in there is dedicated to a given tenant. If you look at a pool model, the basic idea is whatever the storage mechanism I'm using, data mechanism is, that the data is commingled for the tenant. It sits side by side, right? And again, what's the commingling look like? Well, it looks different across different AWS services and technologies, but the premise is still the same, and really this comes back to noisy neighbor, tenant isolation. How would you apply those to these concepts? So if you look at RDS, you'll see that RDS, we've got here an RDS instance. This could be a separate table, could be a separate database per tenant, kinda depends on where you wanna go, a separate instance, and on the pooled model, you'll see, oh, all the data's in the same table, but we're using a foreign key that is the tenant ID to get here. Pretty straightforward stuff, and lots of content out there, but a pretty straightforward pattern. I did wanna highlight though that, as you move out into the different AWS services, you can definitely see lots more things to think about, right? In S3, as an example, am I gonna use a bucket per tenant? Could I use a separate prefix per tenant? I can use tags if I want to as a way to separate tenant information, or even use access points, right? So here even, or if I go over to elastic search, am I using a separate index, a separate cluster? There's lots of options here, and we continue to try to produce information here to help you understand what the practices are for each one of those services, but it's still always gonna come back to, what's the silo model, what's the pool model for representing storage? I will highlight here that I would like this to be a domain-driven experience, right? When people are thinking about data partitioning, I want them to get all the way down to the microservice level to say, "What's the right data partitioning story "for this particular microservice?" So here I've shown three different microservices, and they have three different data partitioning schemes. Order service is using silo, product is using pool, and this rating service has a mix of those two going on, right? Well, I want you to have thought about, what's the noisy neighbor, what's the performance, what's the latency, what's the isolation story of that service, and figure out which model is gonna best fit that service. So I definitely don't want you thinking, "Hey, we picked silo for our SaaS. "Now everything is silo." No. Ask yourself on a service-by-service basis what your approach oughta be. Okay, finally, I know we rushed through this. I'm trying to squeeze a lot into this time, so apologies for this being a little bit hurried, but we're trying to fit as much in as we can. I do wanna hit on a few takeaways. Hopefully it's really clear that there's no one universal SaaS blueprint, right? We're really trying to find the mix of things that are the realities in your domain, the realities in your business, and then take these patterns that we talked about today and find out which combination of those things best address the needs of your environment. And I also wanna highlight this idea that classically the notion of multitenancy has been that this is just about shared infrastructure. Hopefully it's pretty clear from this discussion that, to me, multi-tenant doesn't mean you're sharing infrastructure. I can have siloed infrastructure and still run a multi-tenant SaaS business because it all has a common operation and control plane, and the fact that they're all running the same version and they're all managed by the same experience, that's what makes it multi-tenant, and then, yes, some resources will be shared. Some will be dedicated, and that's more of sort of an application, deployment, and design decision. Clearly, to me, I've really tried to drive home the fact that control plane is essential here. This is really what's gonna drive agility and innovation in your business, and if you're starting from scratch, think a lot about that control plane. And then, obviously, we touched on just a few of the AWS services here, right? The approach for these patterns, the approach for deployment, the approach for silo/pool varies across each one of these stacks, but hopefully at the meta level, you can kind of see the common themes of these patterns and then just apply them to each of those services. And then silo and pool, we just sort of talked about this, that silo and pool is a resource-level decision. It isn't a system decision. It's a resource-by-resource decision, and you should be making that choice on a resource-by-resource basis. And then tiering is one of these things that gets lost a lot in this. People won't have tiering, and I think you oughta be thinking about tiering all across the architecture system. How's it gonna affect isolation? How's it going to affect the throttling of experiences? How can you be sure that each tier is getting the experience they're supposed to get? And then finally, find the best mix of these patterns that really fits your environment, right? Look across the landscape. Hopefully you've got enough exposure from this talk to sorta get a sense of what those options are, and find the mix that best meets the needs of your environment. Okay, quickly, I just wanna hit on the fact that there are some other sessions going on. I have more breakouts. We have some awesome workshops going on and Chalk Talks, and even a business session, so a pretty full list of SaaS content out there for you at re:Invent. And that's it. I really appreciate you taking the time to sit through this, and hopefully it was valuable for you, and definitely looking forward to sort of evolving these patterns based on what we learn from the community, so, thanks so much. (upbeat music)

## Subtitles with Timestamps

[00:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=0s) (upbeat music)

[00:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=10s) Hi, everybody.

[00:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=11s) Thanks so much for joining my session today,

[00:13](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=13s) As the slide says, my name is Tod Golding,

[00:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=16s) and I'm a partner solutions architect at AWS,

[00:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=18s) and I'm part of a team that's called the SaaS Factory.

[00:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=20s) That team works with organizations

[00:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=22s) that are involved in building

[00:23](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=23s) and delivering and operating SaaS solutions on top of AWS.

[00:27](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=27s) And obviously, in the last few years,

[00:29](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=29s) our team has been responsible for creating a lot of content

[00:32](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=32s) and a lot of best practices guidance,

[00:34](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=34s) the SaaS Competency, reference architectures and so on

[00:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=38s) with the goal of really helping SaaS developers

[00:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=40s) better understand what it means to build

[00:43](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=43s) and deliver a best-practices SaaS solution on top of AWS,

[00:48](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=48s) and certainly we've got these reference solutions.

[00:51](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=51s) We've got these sort of end-to-end examples

[00:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=54s) of what it means to build a SaaS solution,

[00:56](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=56s) but we also know that people need sort of guidance on just,

[00:59](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=59s) what are the general sort of patterns?

[01:01](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=61s) How do people address identity?

[01:03](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=63s) How do people address billing?

[01:05](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=65s) How do we go after isolation?

[01:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=68s) So today we're really gonna take

[01:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=70s) a slightly different approach to this.

[01:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=71s) Instead of sort of going deep

[01:13](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=73s) in any one specific architecture, so EKS or serverless,

[01:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=78s) instead, we're gonna look at sort of the landscape

[01:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=80s) of SaaS patterns, if you will.

[01:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=82s) We're gonna look at all the different

[01:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=84s) sort of nuanced different ways and pieces of the SaaS puzzle

[01:29](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=89s) that you need to be thinking about

[01:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=91s) as a designer and an architect and somebody

[01:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=93s) who's trying to build a multi-tenant system

[01:35](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=95s) with the idea that if we can sort of expose you

[01:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=98s) to this entire landscape of options,

[01:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=100s) you can then sort of think about

[01:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=102s) how these apply to your environment,

[01:44](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=104s) how they might influence your solution,

[01:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=106s) and how you might use them to compose the architecture

[01:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=109s) that best meets your needs.

[01:51](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=111s) Now, again, this is a 300-level session,

[01:55](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=115s) so we're intentionally kinda not digging into code here

[01:58](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=118s) or opening up the IDE or sort of wandering into the depth

[02:02](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=122s) of how to build any one specific one of these solutions.

[02:05](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=125s) Instead, we're gonna go across the breadth here, right?

[02:07](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=127s) We're gonna just try to look end to end

[02:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=130s) at all the common patterns, and these patterns

[02:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=132s) don't necessarily break out like Gang of Four patterns.

[02:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=136s) They don't fall into this hierarchy so naturally,

[02:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=138s) but we generally should be able to give some labels

[02:21](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=141s) and some homes to these things

[02:23](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=143s) that should give you a terminology

[02:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=144s) and a vocabulary for talking about SaaS

[02:27](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=147s) as you try to build your own solutions.

[02:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=151s) Now, obviously as we talk about patterns

[02:34](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=154s) and we talk about how to build SaaS solutions,

[02:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=156s) the word that often comes up here is a blueprint, right?

[02:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=159s) Lots of people will come to me and say,

[02:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=161s) "Hey, Tod, we're ready to build this solution.

[02:45](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=165s) "I'm talking to somebody about

[02:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=166s) "what it looks like to build multitenancy.

[02:48](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=168s) "Can you give me the blueprint

[02:50](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=170s) "for building SaaS on my solution?"

[02:52](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=172s) And the reality is

[02:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=174s) there really is no blueprint for SaaS, right?

[02:56](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=176s) There is no one sort of, grab this architecture,

[03:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=180s) use it, and this is the best-practice architecture.

[03:04](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=184s) Yes, we have examples of ways to do that,

[03:07](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=187s) but in reality, SaaS is more the hybrid

[03:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=190s) of all of these different architecture sort of mechanisms

[03:14](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=194s) and components coming together to address your needs.

[03:17](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=197s) So you're not gonna just take your code,

[03:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=199s) run it through some machine,

[03:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=200s) and then have it somehow spit out a SaaS solution

[03:23](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=203s) on the other side.

[03:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=204s) Instead, you're going to look

[03:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=206s) across the landscape of possibilities

[03:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=208s) and figure out which of those options best meet the needs

[03:32](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=212s) of your existing environment.

[03:34](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=214s) And if we sort of look at the patterns that are out there,

[03:37](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=217s) I've tried to give a bit of a home to these patterns,

[03:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=220s) a bit of categories to these patterns,

[03:43](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=223s) and these are just a better way to sort of think about

[03:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=226s) what it means to build SaaS on top of AWS.

[03:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=229s) So one grouping here is

[03:51](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=231s) what I would call the management group.

[03:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=233s) This is where all the management

[03:55](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=235s) of operational sort of patterns show up.

[03:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=237s) This is where we think about what it means

[03:59](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=239s) to provide a unified pane of glass

[04:02](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=242s) that is used to manage an operator bit.

[04:04](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=244s) So here we'll look at things like metrics and analytics

[04:07](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=247s) and what it means to analyze the trends

[04:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=251s) and activity of our tenants.

[04:13](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=253s) We'll look at billing,

[04:14](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=254s) 'cause billing's obviously fundamental.

[04:15](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=255s) How do we implement subscription

[04:17](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=257s) and other kinds of billing constructs?

[04:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=259s) We'll look at what it means

[04:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=260s) to provision tenant environments, right?

[04:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=262s) How do I set up, configure, and create these environments?

[04:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=266s) The other category we'll look at,

[04:27](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=267s) and it's the one a lot of people

[04:29](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=269s) sort of like to hover around the most,

[04:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=271s) is this application category,

[04:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=273s) and here, the patterns are more about multitenancy.

[04:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=276s) How do I actually implement multitenancy

[04:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=279s) inside my application?

[04:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=281s) How do I implement isolation?

[04:43](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=283s) How do I partition data?

[04:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=286s) How do I think about how my app is going to be deployed?

[04:48](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=288s) Am I gonna have silos for tenants?

[04:50](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=290s) Am I going to share tenant infrastructure?

[04:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=294s) And routing even shows up in this group, right?

[04:56](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=296s) How am I gonna get the load

[04:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=297s) to the different deployment footprints in my environment?

[05:02](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=302s) The other category here is what I call tenancy,

[05:05](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=305s) and this is more about,

[05:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=306s) how do I establish sort of tenancy

[05:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=308s) inside a SaaS environment?

[05:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=310s) So here, we're looking more at like,

[05:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=312s) how do I create a SaaS identity?

[05:14](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=314s) How do I create and bind users to a tenant identity?

[05:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=318s) How does that authentication

[05:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=320s) and authorization experience work?

[05:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=322s) I'll look at onboarding like,

[05:23](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=323s) how does a tenant get into the new system,

[05:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=326s) and then how do I even just create tenants in the system?

[05:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=328s) How do I give them an ID and a plan

[05:30](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=330s) and configure the policies of that tenant?

[05:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=333s) And then tiering often shows up here as well like,

[05:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=336s) how do I present different experiences

[05:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=338s) to different tenants?

[05:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=339s) So a basic tier tenant

[05:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=341s) might have a slightly different experience

[05:44](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=344s) than an advanced tier tenant, for example.

[05:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=346s) So here, if you look across this top,

[05:48](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=348s) this is not meant to be the ultimate list of patterns,

[05:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=353s) but these are the sort of silos.

[05:56](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=356s) These are the different sort of families of patterns

[06:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=360s) that we're going to explore.

[06:02](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=362s) But the real takeaway here is,

[06:04](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=364s) across all these different families,

[06:07](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=367s) what our job really is as SaaS architects

[06:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=370s) and SaaS builders is to figure out,

[06:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=372s) how do these specific patterns apply to my solution, right?

[06:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=376s) What kind of identity pattern is best for me?

[06:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=379s) What kind of isolation pattern best meets the needs

[06:21](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=381s) of my environment, right?

[06:23](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=383s) And here's where, when I talk to SaaS organizations,

[06:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=386s) where we often have to start that conversation, right?

[06:29](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=389s) So instead of just saying,

[06:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=391s) "How am I going to do data partitioning?"

[06:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=393s) we have to start with like,

[06:34](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=394s) what are you trying to achieve as a business?

[06:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=396s) What are the personas of the different tiers

[06:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=399s) of tenants you're gonna have in your environment?

[06:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=401s) How are they gonna consume your system?

[06:43](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=403s) Are we starting at a legacy environment,

[06:45](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=405s) 'cause certainly our path

[06:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=406s) and the patterns we use might be heavily influenced

[06:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=409s) by the legacy environment.

[06:51](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=411s) So really it's the mix of the realities

[06:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=413s) of your current environment plus these patterns

[06:56](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=416s) that lets you sort of compose

[06:58](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=418s) this overall SaaS architecture.

[07:01](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=421s) Now, whenever we talk about SaaS,

[07:04](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=424s) if we sorta step up a level

[07:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=426s) from the details of individual patterns,

[07:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=428s) there are two sort of high-level domains

[07:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=431s) that we talk about when we talk about SaaS architectures.

[07:15](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=435s) We'll certainly talk about this control plane,

[07:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=438s) and this control plane is really

[07:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=439s) where all the horizontal services

[07:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=442s) of your SaaS application live.

[07:23](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=443s) So here you'll see that we have things like onboarding

[07:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=446s) and identity and all of these sort of constructs

[07:30](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=450s) that are here to support and operate

[07:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=453s) and manage our SaaS environment.

[07:35](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=455s) And so we'll dig into that control plane

[07:37](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=457s) and look at all the different pieces

[07:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=458s) that are part of that control plane,

[07:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=460s) but it's really important to note that the control plane

[07:43](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=463s) isn't a multi-tenant environment itself.

[07:45](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=465s) It is the management and operation experience

[07:47](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=467s) of your multi-tenant environment.

[07:50](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=470s) Where all the multitenancy really shows up is

[07:52](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=472s) in your application plane,

[07:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=474s) and the application plane is

[07:55](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=475s) where your multi-tenant business services

[07:58](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=478s) and application components,

[08:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=480s) and this is where we're gonna implement tenant isolation.

[08:02](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=482s) This is where we're gonna implement data partitioning.

[08:05](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=485s) This is where lots of our energy goes into figuring out,

[08:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=488s) what's the right microservices

[08:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=490s) for our multi-tenant environment?

[08:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=492s) How are people going to authenticate

[08:13](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=493s) into our environment and so on?

[08:15](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=495s) And so whenever we talk about SaaS applications,

[08:17](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=497s) you'll always hear us talking about

[08:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=500s) this particular concept lives in the control plane,

[08:23](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=503s) or it lives in the application plane,

[08:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=504s) and we'll sort of take our path through this

[08:27](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=507s) with that control plane and application plane in mind.

[08:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=511s) Now the other thing I wanna note here is this sort of notion

[08:35](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=515s) of what it means to be a SaaS application

[08:37](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=517s) or a SaaS service, right?

[08:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=520s) I will have people who will come to me

[08:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=521s) and they will have built an application,

[08:44](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=524s) and they'll build basically

[08:45](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=525s) the application plane side of this experience.

[08:48](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=528s) They'll have multi-tenant services.

[08:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=529s) They will have built isolation,

[08:52](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=532s) and they'll think, "Hey, we're ready for multitenancy,"

[08:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=534s) and then I will ask questions about,

[08:56](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=536s) well, what have you done on the control plane side, right?

[08:58](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=538s) Do you have automated onboarding?

[09:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=540s) How are you tracking metrics

[09:01](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=541s) and analytics about your tenants?

[09:03](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=543s) Do you have a fully automated provisioning experience

[09:05](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=545s) for each one of your tenants?

[09:07](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=547s) Do you have this rich operational view

[09:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=550s) of what's going on inside your tenant environments?

[09:13](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=553s) And to me, if you don't have the control plane piece

[09:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=556s) of this puzzle, you don't really have a SaaS service, right?

[09:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=558s) If I have a great SaaS application

[09:21](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=561s) and a great multi-tenant implementation

[09:23](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=563s) in my application plane,

[09:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=564s) but I can't sort of get all the innovation

[09:27](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=567s) and the agility and all the goodness

[09:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=568s) that comes from this control plane,

[09:30](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=570s) I really can't operate as successfully

[09:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=573s) as I could as a SaaS business.

[09:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=576s) Now, when we talk about SaaS environments

[09:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=579s) across this entire discussion of patterns,

[09:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=581s) you're gonna hear some terms

[09:43](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=583s) that are really common terms here.

[09:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=586s) The term silo you're gonna hear come up from us a lot,

[09:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=589s) and silo is really meant to describe a SaaS environment

[09:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=593s) and a SaaS architecture where the resources

[09:56](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=596s) of a tenant are dedicated to an individual tenant.

[09:59](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=599s) This doesn't mean the entire stack

[10:01](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=601s) is dedicated to the tenant.

[10:02](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=602s) It could be that just some resource is delivered

[10:05](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=605s) and offered in a per-tenant basis

[10:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=608s) and that resource is siloed.

[10:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=610s) And it's important to note

[10:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=611s) that even if I run a full stack silo,

[10:13](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=613s) all tenants running their own infrastructure,

[10:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=616s) if I have that control plane that manages and operates this,

[10:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=620s) I'd still consider that a multi-tenant SaaS environment.

[10:23](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=623s) Yes, some resources are shared

[10:25](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=625s) and some resources are dedicated,

[10:27](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=627s) but to me that's still a multi-tenant SaaS business.

[10:30](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=630s) Now on the opposite side of silo,

[10:32](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=632s) you'll also hear us use the term pool,

[10:34](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=634s) and pool is really used to refer

[10:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=638s) to the sharing of infrastructure,

[10:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=640s) and this is the more classic definition of multitenancy.

[10:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=642s) Here, tenants are sharing some resource.

[10:45](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=645s) And again, this is super granular.

[10:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=646s) I could be in an environment where some resources are shared

[10:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=649s) and some are actually siloed,

[10:52](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=652s) but in general, when a resource is shared by tenants,

[10:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=654s) we refer to that as a pooled model.

[10:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=657s) Now, historically, we've also talked about this bridge model

[11:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=660s) and use this term to refer to tenants

[11:01](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=661s) that are using a mix of both.

[11:03](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=663s) I think longer term, we'll sort of phase out this notion

[11:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=666s) of a bridge, but we do wanna acknowledge

[11:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=668s) that everything isn't just silo,

[11:09](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=669s) everything isn't just pool.

[11:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=671s) There's obviously this mode in between

[11:13](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=673s) where some things are siloed and some things are pooled.

[11:15](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=675s) Anyway, this terminology is gonna be used

[11:17](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=677s) across the rest of the presentation,

[11:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=678s) and hopefully it's very clear what we're talking about

[11:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=680s) when we talk about silo and pool.

[11:23](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=683s) Okay, so enough background.

[11:25](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=685s) Let's start looking at the actual moving parts

[11:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=688s) of the control plane.

[11:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=688s) What services are in the control plane,

[11:30](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=690s) what functionality is there,

[11:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=691s) and what do we need to do in them?

[11:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=693s) And we're gonna start

[11:34](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=694s) with one of the most important pieces of the control plane,

[11:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=698s) which is this onboarding experience.

[11:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=700s) How do we onboard and get new tenants into our system?

[11:43](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=703s) How are they created?

[11:44](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=704s) How are they provisioned and configured?

[11:47](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=707s) And this is a really common pattern

[11:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=709s) across all of the solutions that we describe,

[11:52](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=712s) and here you'll see I'm gonna describe this

[11:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=714s) as Lambda services, but this could be ECS,

[11:56](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=716s) it could be EKS, it could be EC2.

[11:59](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=719s) The idea is that I have these microservices

[12:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=720s) and they're being orchestrated in this onboarding flow.

[12:04](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=724s) So when a tenant comes in

[12:05](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=725s) and the tenant is going to be registered

[12:07](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=727s) and onboarded into my system,

[12:09](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=729s) they'll come into this registration service.

[12:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=731s) Now it's important to note

[12:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=731s) that that registration could have been triggered

[12:13](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=733s) by a self-service experience

[12:15](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=735s) that was a classic, say, B-to-C experience,

[12:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=739s) or it could be something internally triggered

[12:21](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=741s) by an internal mechanism.

[12:23](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=743s) Either way, from the registration experience down,

[12:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=746s) all the automation of that would be exactly the same

[12:29](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=749s) in both those scenarios.

[12:30](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=750s) So here we hit the registration service.

[12:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=753s) It's now gonna hit the tenant service,

[12:34](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=754s) and that tenant service is now gonna configure

[12:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=756s) all the information about a tenant.

[12:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=758s) What's their ID?

[12:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=759s) What's their policies?

[12:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=761s) What identity settings might they have

[12:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=762s) that we need to keep track of, and so on?

[12:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=766s) And then we're also going to provision a user here.

[12:48](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=768s) So when we provision a user,

[12:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=769s) we're setting up that first user in our system

[12:52](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=772s) that is gonna be the first sort of tenant admin,

[12:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=774s) if you will, of this user,

[12:56](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=776s) and then that experience actually is gonna have to go

[12:59](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=779s) out to our identity provider,

[13:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=780s) and here I've shown Cognito.

[13:01](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=781s) I could be showing Okta or Auth0 or Ping

[13:04](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=784s) or any identity provider, but the key here is

[13:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=786s) I have to create a user in that experience.

[13:09](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=789s) In this case, I create a user pool

[13:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=790s) in this example for each tenant,

[13:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=792s) 'cause that's a Cognito construct,

[13:14](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=794s) and then you'll see here I create

[13:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=796s) and populate custom claims,

[13:17](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=797s) and these custom claims are what connect our user identity

[13:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=802s) to our tenant identity.

[13:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=804s) So when we're all done with this, in the custom claims,

[13:27](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=807s) you'll see tenant identifier, you'll see user information,

[13:30](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=810s) and when I authenticate this user

[13:32](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=812s) and bring them into the system,

[13:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=813s) I'll actually get a token that comes back

[13:35](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=815s) that includes all of that tenant context,

[13:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=819s) and we'll talk about how that gets used later on.

[13:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=821s) You might also find

[13:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=822s) that I provision policies here for the user.

[13:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=826s) These could get provisioned here.

[13:47](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=827s) They also could get provisioned

[13:48](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=828s) in other phases of the process.

[13:50](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=830s) Where this happens kinda depends on the nature

[13:52](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=832s) and the deployment model of your solution,

[13:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=834s) but I at least wanted include the fact

[13:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=837s) that these get created somewhere in this process.

[13:59](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=839s) So now I've got my tenant created.

[14:01](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=841s) I've got my user created.

[14:02](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=842s) I also typically in this pattern

[14:04](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=844s) have some onboarding experience

[14:05](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=845s) that I have to go through for the billing system.

[14:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=848s) So somewhere out there, I've set up my billing system.

[14:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=851s) I know I'm gonna bill tenants.

[14:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=852s) Well, now a new tenant's showing up.

[14:14](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=854s) I have to provision that new tenant into that experience.

[14:17](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=857s) So here, this is where we'll see

[14:21](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=861s) different billing providers showing up, Chargebee,

[14:23](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=863s) and we'll talk a little bit more

[14:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=864s) about the role of those providers in this experience.

[14:29](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=869s) And then the last step is the one

[14:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=871s) that often has a lot of complexity to it,

[14:34](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=874s) which is this provisioning step.

[14:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=876s) If I'm running a pooled environment

[14:37](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=877s) where all my tenants are sharing infrastructure,

[14:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=880s) the onboarding of a new tenant might not mean

[14:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=882s) we have to create very much infrastructure at all,

[14:44](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=884s) or it turns out if I've got a siloed model

[14:47](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=887s) where tenants need their own infrastructure,

[14:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=889s) the onboarding will actually have to provision

[14:51](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=891s) infrastructure for each tenant,

[14:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=893s) and you'll see this show up

[14:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=894s) in the different reference architectures that we offer.

[14:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=897s) So this is often an overlooked piece of this

[15:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=900s) 'cause people won't think of provisioning

[15:01](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=901s) and setup of new infrastructure

[15:03](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=903s) as part of their onboarding process,

[15:04](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=904s) but it's absolutely an essential part of it

[15:07](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=907s) for some deployment models.

[15:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=910s) Now, one way this shows up

[15:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=912s) and one way that provisioning sort of gets impacted

[15:14](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=914s) by this is by what we would call tier-driven onboarding.

[15:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=918s) So in this model, essentially a tenant comes in,

[15:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=920s) they register, they tell us what tier they are.

[15:23](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=923s) Are they basic, advanced, platinum, or whatever?

[15:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=926s) Certainly we're gonna set up the tenant, the user,

[15:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=928s) do all those other bits we're going to,

[15:29](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=929s) but we're also gonna go off to this provisioning experience,

[15:32](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=932s) and the provisioning experience will actually now provision

[15:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=936s) dedicated resources for that tenant,

[15:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=938s) siloed resources that are needed for them individually.

[15:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=942s) This flow is all driven by what tier you provided to me,

[15:47](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=947s) and all has to be part of my onboarding experience.

[15:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=949s) It can't be some experience

[15:51](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=951s) somehow outside of the onboarding world.

[15:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=954s) Now if you look at what this actually looks like

[15:56](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=956s) in practice, in action, and you go look under the hood here

[15:59](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=959s) of one of these solutions, well, let's say for example,

[16:02](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=962s) and this is exactly, by the way,

[16:04](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=964s) what our serverless SaaS reference architecture does.

[16:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=966s) I come in, I've got these pooled tenants.

[16:09](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=969s) These pooled tenants have some microservices.

[16:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=971s) They've already been provisioned and configured.

[16:13](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=973s) They're all just shared by all the tenants,

[16:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=976s) and so adding a new tenant here simply adds a new tenant

[16:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=979s) that consumes those resources.

[16:21](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=981s) There's probably other bits that are getting configured,

[16:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=984s) but in general,

[16:25](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=985s) it's gonna just consume the existing microservices

[16:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=988s) that are running for us.

[16:29](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=989s) And then in this system, let's say I have a siloed customer.

[16:32](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=992s) That siloed customer's in this platinum tier plan,

[16:35](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=995s) and so they have their own dedicated resources

[16:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=998s) running in this silo.

[16:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=999s) And now if I onboard another tenant

[16:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1002s) and they indicate to me that they're a platinum user,

[16:44](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1004s) I have to kick off some provisioning process

[16:47](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1007s) that's gonna provision that user's resources

[16:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1009s) into my environment.

[16:51](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1011s) Okay, so that's kind of the onboarding piece of that.

[16:55](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1015s) Now, another huge part of the control plane is

[16:58](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1018s) this notion of identity,

[17:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1020s) and when we talk about multi-tenant systems,

[17:02](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1022s) it's really important to have what we'd say,

[17:04](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1024s) to have tenant-aware identity.

[17:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1026s) It's not enough just to be able to authenticate

[17:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1028s) against any identity provider.

[17:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1030s) We have to authenticate in a way

[17:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1031s) that introduces tenancy into our environment.

[17:15](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1035s) So here, if I have an identity flow or a tenant is coming in

[17:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1040s) and they're authenticating into my system

[17:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1042s) and they hit my web app, when they hit my web app,

[17:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1046s) they're gonna be redirected to an identity provider,

[17:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1048s) again, Cognito, Auth0, whatever it is,

[17:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1051s) and now when we authenticate in that environment,

[17:34](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1054s) we now know the binding of the user to that tenant,

[17:37](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1057s) and this is where those custom claims come into place.

[17:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1059s) Those all come back here.

[17:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1061s) We'll get an identity token and an access token back.

[17:44](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1064s) We're describing like an OIDC kind of authentication here,

[17:47](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1067s) and those tokens will be enriched with tenant context.

[17:51](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1071s) They'll tell me not just what user I am,

[17:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1073s) but what tenant I'm related to,

[17:55](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1075s) what tier I am and so on,

[17:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1077s) and now that piece of information will flow

[17:59](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1079s) back into the services of my application.

[18:02](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1082s) So now when I'm in some application service

[18:04](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1084s) and I need tenant context,

[18:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1086s) I don't have to go somewhere else to get it.

[18:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1088s) I can open that JWT token, peek inside of it,

[18:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1091s) get the tenant ID, get what other tenant context I need,

[18:15](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1095s) and I get really good efficiency out of that.

[18:17](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1097s) And if I call another service,

[18:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1099s) I can simply pass that same token along to the next service,

[18:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1102s) and that service can now rely on it as well.

[18:25](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1105s) And so this is this whole notion of tenant-aware identity,

[18:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1108s) which is to say we're really passing tenant context

[18:32](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1112s) through all of our experience

[18:34](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1114s) in a way that everybody sort of has it at their fingertips

[18:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1116s) and can use it to access data, record metrics,

[18:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1120s) or whatever they need to do.

[18:43](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1123s) Now if we look at a flow for that

[18:44](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1124s) and what sort of an authentication flow might look like,

[18:48](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1128s) well, here's one where I've got a tenant coming in.

[18:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1129s) They're coming into the application.

[18:51](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1131s) They're using a subdomain to come in in this case,

[18:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1133s) so there's multiple ways to come in here.

[18:55](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1135s) We won't get to dig into all those,

[18:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1137s) but when I come in, I say, "Hey, I've got a tenant.

[18:59](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1139s) "They wanna authenticate," and in this case,

[19:01](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1141s) because I don't know what to authenticate you against,

[19:04](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1144s) I have to actually go out to tenant management,

[19:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1146s) which is where I stored your identity settings

[19:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1148s) and all the other information,

[19:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1150s) which user pool you're running against and so on,

[19:13](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1153s) and I have to pass that information back to the app.

[19:15](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1155s) And in this example, I show the app saving that off

[19:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1158s) in this authorization library,

[19:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1160s) and then that authorization library

[19:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1162s) will now use that tenant context to go out to Cognito

[19:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1166s) and authenticate a user.

[19:27](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1167s) So here, you'll see it's authenticating

[19:29](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1169s) against this specific user pool.

[19:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1171s) That's the user pool I got

[19:32](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1172s) from down below in tenant management.

[19:35](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1175s) Then that will return a code,

[19:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1176s) and then that code will be exchanged for a JWT,

[19:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1178s) and all of this is just following

[19:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1180s) standard OAuth kind of flow,

[19:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1182s) but now that I have that JWT token back,

[19:44](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1184s) that JWT token has all that SaaS goodness

[19:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1186s) that we talked about baked into it,

[19:47](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1187s) and so now that JWT token can get passed

[19:51](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1191s) down to the microservices of my application.

[19:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1193s) So here it goes to my product service,

[19:55](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1195s) and the product service has all that goodness.

[19:58](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1198s) So really the pattern here is, when I authenticate,

[20:03](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1203s) I wanna authenticate in a SaaS context

[20:05](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1205s) and I wanna get a token out of that experience

[20:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1208s) that has all that goodness baked into it

[20:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1210s) so that doesn't have to be resolved

[20:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1212s) somewhere else downstream.

[20:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1216s) Now, I talked a little bit about the fact

[20:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1218s) that we were using a user pool per tenant,

[20:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1220s) and I'm gonna get a little AWS specific here,

[20:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1222s) which is, if you're in Cognito,

[20:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1224s) 'cause a lot of our SaaS providers are using Cognito,

[20:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1226s) one of the questions they really face is,

[20:29](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1229s) should I do a tenant per user pool kinda mapping,

[20:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1231s) or should I have one user pool for all tenants?

[20:34](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1234s) And the reality is they're both valid.

[20:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1236s) So in the user pool per tenant model,

[20:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1239s) the real advantage here is

[20:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1240s) that I can have separate policies for each tenant, right?

[20:44](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1244s) I can set up whether you're MFA or what's your security,

[20:48](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1248s) how soon your password might time out.

[20:50](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1250s) All of those traditional things

[20:51](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1251s) I'd set up about your identity,

[20:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1253s) I can have separate settings per user pool here,

[20:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1257s) and then that means per tenant,

[20:59](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1259s) and that means I can actually offer that

[21:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1260s) as a feature to tenants to be able to say,

[21:02](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1262s) "Hey, you can manage and configure all of this on your own."

[21:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1266s) However, in a user pool per tenant,

[21:07](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1267s) now I've gotta resolve you

[21:09](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1269s) to which user pool you're going to.

[21:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1271s) There are limits on how many user pools I can have.

[21:13](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1273s) So there's still questions about

[21:15](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1275s) whether this would be a good fit,

[21:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1276s) and to sort of highlight this,

[21:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1278s) in our EKS reference architecture,

[21:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1280s) we actually do the user pool per tenant model,

[21:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1282s) but then in our serverless SaaS model,

[21:25](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1285s) we have a model where we're actually using one user pool

[21:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1288s) for all of our pooled tenants, and in this model,

[21:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1291s) we get away from some of the scale challenges

[21:34](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1294s) and some of the mapping challenges,

[21:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1296s) but now I have to figure out which group you're in,

[21:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1299s) and I have to think about how to still resolve,

[21:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1301s) how to authenticate you.

[21:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1302s) Just have to use a slightly different mechanism,

[21:44](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1304s) but I don't have to worry about the limits

[21:45](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1305s) of the number of user pools,

[21:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1306s) so both of them are entirely valid.

[21:48](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1308s) It really kinda depends more

[21:50](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1310s) on the profile of your application.

[21:52](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1312s) Obviously in the single user pool model,

[21:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1314s) I also don't get to configure this.

[21:56](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1316s) The policies are the same for all tenants,

[22:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1320s) but either way, both of these are good solutions.

[22:02](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1322s) I just think you have to sorta weigh the pros and the cons.

[22:05](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1325s) Now also as part of identity,

[22:07](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1327s) another pattern we see is a model

[22:09](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1329s) where a customer may wanna bring their own identity

[22:13](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1333s) to your SaaS solution, right?

[22:14](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1334s) So I already have an identity solution for all my customers,

[22:17](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1337s) but now some customer signs up

[22:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1339s) and they don't wanna use my identity.

[22:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1340s) They wanna use their own solution.

[22:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1342s) So here I've shown two sort of on-premises environments

[22:25](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1345s) with their own identity providers,

[22:27](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1347s) and my own Cognito user pool

[22:30](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1350s) that is managing the rest of my tenants.

[22:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1351s) Well, what do I do in this case?

[22:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1353s) Well, in this model,

[22:34](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1354s) I have to have some kind of hybrid identity model where,

[22:37](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1357s) as these tenants come in,

[22:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1359s) they will hit some authentication manager.

[22:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1362s) That is my centralized service,

[22:44](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1364s) and that authentication manager will look

[22:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1366s) at their configuration and say, "Oh, you're a tenant

[22:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1369s) "that's configured my own Cognito identity.

[22:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1373s) "I'll auth you there.

[22:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1374s) "Oh no, you're authenticating

[22:55](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1375s) "against one of these on-premises environments.

[22:58](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1378s) "I'll authenticate you there."

[23:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1380s) Now the challenge here is when I authenticate

[23:02](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1382s) from one of these on-premises environments,

[23:04](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1384s) I don't necessarily have all that other context

[23:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1386s) that comes back from that authentication,

[23:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1388s) so this is where we'll see people add

[23:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1390s) what I call this sort of JWT enrichment tooling here,

[23:14](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1394s) which will basically say, "Hey, I'm gonna go out.

[23:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1396s) "I'm gonna take that information

[23:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1398s) "that came back from the authentication,

[23:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1399s) "enrich the JWT token,"

[23:21](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1401s) and now a JWT token just flows out of this experience,

[23:25](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1405s) downstream to all my services,

[23:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1406s) and whether I came from on premises or I came from Cognito,

[23:30](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1410s) it all just looks the same to the downstream services.

[23:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1413s) So I see some organizations

[23:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1416s) really have to work through this,

[23:37](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1417s) and so I wanted to represent this pattern

[23:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1418s) because I think it is important

[23:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1420s) to be able to not always assume

[23:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1422s) that you're gonna own the identity experience.

[23:45](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1425s) The last piece of identity

[23:47](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1427s) I wanna talk about here is multi-region identity.

[23:50](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1430s) Here, the challenge is,

[23:52](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1432s) how do I sort of authenticate in an environment

[23:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1434s) where I have multiple, I'm running in multiple regions?

[23:58](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1438s) And certainly one approach to this is

[23:59](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1439s) to have a common front door for all customers and tenants

[24:03](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1443s) that are coming in to authenticate in your environment

[24:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1446s) and have a centralized authentication

[24:09](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1449s) and identity experience for all those different regions,

[24:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1451s) and then just go through and pass that context

[24:14](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1454s) through to those individual regions.

[24:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1456s) However, this kinda model doesn't usually work out

[24:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1458s) because organizations that are facing compliance

[24:21](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1461s) or regional sort of considerations aren't able necessarily

[24:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1464s) to host their identity in some shared, centralized place.

[24:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1468s) So in this model, what we'll say is,

[24:30](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1470s) instead we'll change that front door to something

[24:32](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1472s) that will map you to the appropriate region,

[24:35](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1475s) and we'll actually move the identity

[24:37](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1477s) to the individual region,

[24:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1479s) so now the identity lives in that region,

[24:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1481s) and you're all good there.

[24:45](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1485s) The other one, and I'll just hit on these two quickly.

[24:47](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1487s) Obviously, inside the control plane,

[24:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1489s) we also have user management,

[24:51](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1491s) and that's two flavors of user management.

[24:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1493s) That's the admin console where it's the ISV provider's users

[24:56](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1496s) being managed in Cognito,

[24:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1497s) and we also have the SaaS provider's users,

[25:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1500s) the tenant users that are managed here,

[25:02](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1502s) and the user management service is really needed

[25:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1506s) for both of those roles in your system,

[25:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1508s) but a pretty classic thing to have included here.

[25:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1511s) Billing also shows up here in the control plane,

[25:15](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1515s) and really billing has two specific dimensions to it:

[25:17](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1517s) configuration and instrumentation.

[25:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1520s) So when we talk about configuration and instrumentation,

[25:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1522s) we're really talking about,

[25:23](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1523s) what does it mean to get the environment set up

[25:25](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1525s) to be able to be configured to generate a bill,

[25:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1528s) and then how do I actually instrument my system

[25:30](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1530s) to send it the data it needs to generate that bill?

[25:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1533s) So if you look here, and I've got an example,

[25:35](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1535s) some billing providers, Chargebee, Zuora, Stripe, so on.

[25:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1540s) When I go set up an account with them,

[25:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1542s) I have to go in and establish a relationship with them,

[25:45](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1545s) set up my business with an account there,

[25:47](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1547s) and I have to configure the billing plans with them, right?

[25:50](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1550s) What kind of billing structure am I using?

[25:52](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1552s) Subscription, consumption, number of users,

[25:56](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1556s) whatever the sort of mechanism I'm using for billing,

[25:58](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1558s) I have to go set all of that up.

[26:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1560s) Then for my SaaS application, when a new tenant signs up,

[26:04](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1564s) I actually have to go onboard that tenant

[26:07](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1567s) to the billing system, right?

[26:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1568s) I have to go create a relationship,

[26:09](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1569s) create a customer in that system, and the logistics of that

[26:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1572s) and the patterns of that vary

[26:14](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1574s) based on these different implementations

[26:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1576s) of these different billing providers,

[26:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1578s) but the basic goal is the same:

[26:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1579s) Get the account created here

[26:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1582s) and orchestrate all of that,

[26:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1584s) and it's usually a pretty straightforward process.

[26:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1586s) Once I have all that set up,

[26:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1588s) really now the key thing is generating

[26:30](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1590s) and capturing the activity

[26:32](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1592s) that is going to be used for my actual SaaS bill.

[26:37](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1597s) So if you look here inside my SaaS application,

[26:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1600s) somewhere in here I'm gonna go add the instrumentation

[26:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1602s) to my environment that will capture events and activities,

[26:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1606s) surface them, and publish them to my billing system,

[26:50](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1610s) and eventually generate a bill.

[26:52](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1612s) Now, which things should you instrument here?

[26:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1614s) It kinda depends.

[26:55](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1615s) This really depends on your plans.

[26:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1617s) If you're subscription-based, you might bill one way

[27:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1620s) and generate certain events here,

[27:02](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1622s) might be feature-based or whatever.

[27:04](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1624s) If you're consumption-based,

[27:05](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1625s) you may need to instrument for consumption-based events.

[27:09](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1629s) It's really sort of driven by

[27:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1630s) what the needs of your environment are,

[27:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1632s) but overall, this is the sort of classic billing component

[27:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1636s) of the control plan.

[27:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1638s) Now if you look at ways this gets implemented,

[27:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1640s) there's lots of ways to implement this ingestion.

[27:23](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1643s) It's pretty much an event ingestion model,

[27:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1646s) an aggregation and a publication (indistinct)

[27:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1648s) and we actually have a sample Stripe solution out there

[27:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1651s) that illustrates how this works.

[27:34](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1654s) But essentially here we show EventBridge coming in,

[27:37](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1657s) taking a billing event, sending it to an aggregator.

[27:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1662s) That aggregator aggregates the billing content,

[27:44](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1664s) stores it in a database,

[27:45](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1665s) and then periodically sends that billing information

[27:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1669s) to the billing provider.

[27:50](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1670s) Now the use of the aggregator here is debatable.

[27:52](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1672s) You could say,

[27:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1673s) "No, I wanna go straight to the billing provider,"

[27:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1674s) but in some cases,

[27:55](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1675s) people really wanna capture that billing detail,

[27:58](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1678s) they wanna have their own database of it,

[27:59](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1679s) and they don't wanna rely on just the reliability

[28:02](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1682s) of the billing system to successfully process

[28:05](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1685s) all of their requests.

[28:07](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1687s) They also don't want it to be necessarily

[28:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1688s) as chatty with the billing provider,

[28:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1690s) but a pretty straightforward integration.

[28:13](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1693s) Now on the other side of this is the idea

[28:15](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1695s) of metrics instrumentation and aggregation, right?

[28:17](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1697s) Metrics is more about, how do I capture which features

[28:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1700s) and functions of my system users are using?

[28:23](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1703s) How can I capture information

[28:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1704s) about the operational health of the system?

[28:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1706s) This is all the data that's needed just collectively

[28:29](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1709s) by the business to assess the business, the SaaS business,

[28:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1713s) the SaaS architecture and so on.

[28:35](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1715s) So here, we really are just setting up

[28:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1718s) classic sort of aggregation and analytics tooling, right?

[28:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1722s) There's no magic here.

[28:43](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1723s) I showed two examples here, one with Kinesis,

[28:45](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1725s) all the way through Redshift to QuickSight.

[28:47](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1727s) You could also use Logstash and elastic search Kibana here

[28:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1733s) to surface that information.

[28:55](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1735s) Really where this gets more interesting

[28:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1737s) is more on the instrumentation side of this,

[29:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1740s) and here I think there's at least two categories of events.

[29:03](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1743s) There's probably more here, but two common ones

[29:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1746s) that are here are these system-level metric events,

[29:09](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1749s) and the system-level metric events are ones

[29:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1751s) where we're essentially finding out CPU

[29:14](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1754s) and memory and other things

[29:15](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1755s) that are naturally captured by the tooling like CloudWatch

[29:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1758s) and other bits here,

[29:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1759s) and then we have these application-based events

[29:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1762s) that are more about my domain, right?

[29:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1764s) These are specific things about how features

[29:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1766s) and capabilities are being consumed for my application.

[29:29](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1769s) And the idea is to aggregate all that up,

[29:32](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1772s) and then surface it in a way

[29:34](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1774s) that product managers and operations people

[29:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1778s) and developers can all consume it however they want

[29:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1781s) and make decisions about the architecture

[29:43](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1783s) and the business and so on.

[29:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1786s) The last piece of the control plane here

[29:48](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1788s) is this whole notion of application plane integration,

[29:52](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1792s) and the idea here is that we have this control plane.

[29:56](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1796s) It's got all these common services in it.

[29:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1797s) It's running in its own construct,

[29:59](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1799s) but it still needs to interact with the application plane.

[30:03](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1803s) It has to send billing events to it.

[30:05](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1805s) It plays a role where it gets data back

[30:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1808s) from the control plane

[30:09](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1809s) that's used to manage the application plane,

[30:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1812s) and here you'll see that I have two siloed models,

[30:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1816s) and I have two siloed tenants,

[30:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1818s) and a pool tenant environment.

[30:21](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1821s) And really here, I need some kind of model

[30:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1824s) of interacting with all of these environments

[30:27](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1827s) that meets my security constraints

[30:30](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1830s) and really sort of couples these together

[30:32](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1832s) the way I want them to be coupled then,

[30:34](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1834s) or I really am super loosely coupled,

[30:35](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1835s) or is this a really tight integration?

[30:37](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1837s) It's kind of up to me, but here's where you look at,

[30:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1839s) do I use EventBridge here?

[30:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1840s) Do I use PrivateLink?

[30:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1842s) Do I use VPC peering?

[30:43](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1843s) It all depends on the deployment model of your application.

[30:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1846s) The key takeaway here is that I have to think about

[30:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1849s) how I'm going to manage that application environment

[30:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1853s) and integrate with that application plane environment

[30:55](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1855s) from my control plane.

[30:58](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1858s) Okay, so that's all the control plane bits.

[31:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1860s) Those are all the horizontal bits

[31:02](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1862s) and shared bits that are common to all of my tenants.

[31:05](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1865s) Really not a lot of multitenancy in there.

[31:07](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1867s) Now let's shift over to the application plane,

[31:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1870s) and in the application plane, we'll look more at like,

[31:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1872s) what does it really mean to implement multitenancy

[31:14](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1874s) on top of AWS, and what are the patterns there?

[31:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1878s) And we're gonna start

[31:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1879s) with the most coarse-grained view of this, right?

[31:21](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1881s) For some people, the move to SaaS is really all about

[31:25](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1885s) just getting their system up and running,

[31:27](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1887s) or some people will just choose a siloed model

[31:29](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1889s) for their tenants because of the compliance

[31:32](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1892s) or the domain considerations of their environment.

[31:35](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1895s) But here really the goal is to say,

[31:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1896s) what does it really mean

[31:37](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1897s) to offer a full stack siloed implementation

[31:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1901s) of your solution?

[31:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1902s) And here, I'm gonna show different ways

[31:45](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1905s) that you can implement a full stack silo,

[31:47](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1907s) but basically silo here really means we're taking the notion

[31:50](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1910s) of silo and saying every resource

[31:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1913s) in the environment will be dedicated to a tenant,

[31:56](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1916s) and one way to do this is in an account per tenant model.

[32:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1920s) We'd essentially give each tenant their own account.

[32:02](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1922s) There are some challenges to that.

[32:03](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1923s) Setting limits and automation

[32:05](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1925s) of some of this can be a little bit tough,

[32:07](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1927s) but some people will use Control Tower here as well

[32:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1931s) to help with some of this, but totally a valid model,

[32:14](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1934s) and some people like the operational

[32:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1936s) and the cost tracking of this.

[32:17](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1937s) A really second common model here

[32:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1940s) is the VPC per tenant model,

[32:23](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1943s) and in a VPC per tenant model,

[32:25](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1945s) we're essentially putting each tenant in their own VPC,

[32:27](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1947s) but the good news here is they're all in the same account,

[32:30](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1950s) and because they're all in the same account,

[32:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1953s) they're a little easier to manage and a little bit easier

[32:35](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1955s) to get some of the operational efficiency

[32:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1958s) that we'd want out of this,

[32:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1958s) and a little less difficult to automate

[32:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1961s) than maybe the account per tenant model.

[32:44](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1964s) And then the last one is this notion of a subnet per tenant.

[32:47](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1967s) So we're now going inside the VPC

[32:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1969s) and giving each tenant their own subnet.

[32:51](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1971s) I see this one not nearly as often as the others,

[32:55](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1975s) but I do include it just in case some are interested,

[32:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1977s) but the basic idea here is

[32:58](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1978s) that we're going to give tenants a full stack

[33:01](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1981s) in a super valid common model,

[33:03](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1983s) and this is still considered a multi-tenant SaaS model

[33:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1986s) if we're managing and operating these silos

[33:09](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1989s) with a control plane that automates onboarding,

[33:14](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1994s) sort of centralizes identity, and so on.

[33:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1998s) Now what I wanna do here

[33:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=1999s) is now walk in like we talked about.

[33:21](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2001s) There's this silo model that's a full stack silo model,

[33:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2004s) and I wanna get a little more granular,

[33:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2006s) and what we're gonna do from here

[33:27](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2007s) through the rest of the application plane is more look at,

[33:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2011s) how does silo, pool, et cetera,

[33:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2013s) play out on different AWS stacks,

[33:35](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2015s) and how does it play out on different technologies?

[33:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2019s) How does it play out on storage?

[33:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2020s) How do we implement isolation?

[33:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2021s) And each one of these are influenced

[33:45](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2025s) based on the different stack or service that we're using,

[33:48](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2028s) and so what I'm gonna try to do here is wander a range

[33:50](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2030s) of stacks and services

[33:51](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2031s) and talk to you about how the patterns are realized

[33:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2034s) on each one of those.

[33:55](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2035s) So for example, we're gonna start here with EKS, right?

[33:58](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2038s) What does it really mean to implement EKS compute silo?

[34:01](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2041s) So now it's not the whole stack, just compute.

[34:04](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2044s) What would that look like?

[34:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2046s) So here, if we look at an EKS environment,

[34:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2048s) a slightly simplified version,

[34:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2050s) and we said we were to spin it up,

[34:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2051s) yes, we've got a Multi-AZ,

[34:14](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2054s) highly available sort of classic,

[34:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2056s) Well-Architected architecture here,

[34:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2059s) and then one way we can implement silo here

[34:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2062s) would be a cluster per tenant model.

[34:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2064s) And in a cluster per tenant model,

[34:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2066s) essentially each tenant will get

[34:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2068s) a fully provisioned EKS cluster for them,

[34:30](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2070s) and obviously, a lot of moving parts to that,

[34:32](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2072s) but some people like that cluster-based model

[34:35](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2075s) either for the isolation profile

[34:37](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2077s) or the cost accounting model.

[34:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2078s) There's a lot of reasons they see appeal in that.

[34:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2080s) And so here, as each tenant comes in,

[34:43](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2083s) we essentially create a separate cluster for that tenant.

[34:47](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2087s) Now within EKS, however, there are multiple ways

[34:50](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2090s) to implement the silo model of the compute.

[34:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2094s) So here, here's an alternate approach.

[34:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2097s) Same Multi-AZ model, same sort of setup,

[35:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2100s) but now instead of having a separate cluster per tenant,

[35:03](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2103s) we're actually gonna have a separate namespace

[35:05](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2105s) for each tenant.

[35:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2106s) So here, we will provision a namespace

[35:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2110s) when a new tenant onboards,

[35:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2111s) and now the overhead of that is not nearly as intense

[35:14](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2114s) as the cluster per tenant model.

[35:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2116s) Now everything's kind of within the cluster.

[35:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2119s) It's a little simpler to set up and a little easier

[35:21](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2121s) for us to use the natural EKS components to update,

[35:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2124s) roll out, and provision the resources.

[35:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2126s) And actually our EKS reference architecture,

[35:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2128s) if you're looking on details

[35:29](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2129s) on how to do namespace per tenant,

[35:32](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2132s) it's got a really good example of how to set that up.

[35:35](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2135s) So now each new tenant just gets added

[35:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2138s) as another namespace in here,

[35:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2139s) and we still get good isolation here,

[35:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2141s) a good isolation story.

[35:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2142s) It's just the isolation boundary now is a namespace.

[35:47](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2147s) Sorta the third variation of this is

[35:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2149s) what we'd call the EKS compute model, pool model, excuse me.

[35:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2153s) And in the EKS pooled model,

[35:55](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2155s) it's exactly what you think it'd be, right?

[35:58](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2158s) So all we're really saying is

[35:59](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2159s) we're gonna have a single cluster,

[36:01](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2161s) and all the tenants will be running in that cluster.

[36:05](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2165s) And some people would say,

[36:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2166s) "Well, why not just do that for everything?"

[36:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2168s) Well, there are certain isolation considerations

[36:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2171s) that you have to think about here

[36:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2172s) if you're gonna run in a pooled model.

[36:15](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2175s) You have to do more work here

[36:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2176s) in terms of how you set up your policies

[36:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2178s) and how you ensure that the tenant's isolation model

[36:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2182s) is going to work the way you want.

[36:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2184s) Still a valid model.

[36:25](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2185s) In fact, you'll see our EKS reference architecture showing

[36:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2188s) adding a pool model to it

[36:30](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2190s) alongside a namespace per tenant model

[36:32](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2192s) to show you that you can have both of those.

[36:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2193s) You just kinda have to accept what comes with this model,

[36:37](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2197s) but totally good in terms of economies of scale,

[36:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2199s) certainly simplifies deployment,

[36:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2201s) just has a tougher isolation story here,

[36:44](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2204s) and a tougher maybe story

[36:45](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2205s) to offer different experiences to different tiers.

[36:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2209s) Okay, now let's sort of pivot there, right?

[36:52](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2212s) We talked about silo and pool in the context of EKS.

[36:55](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2215s) Just for contrast now,

[36:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2217s) let's look at what that would look like

[36:58](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2218s) inside of serverless, and this drives home the point

[37:01](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2221s) that the model for silo and pool is different

[37:05](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2225s) depending on which stack you're working with.

[37:07](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2227s) So here, and this is right out of our serverless SaaS,

[37:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2230s) by the way, reference architecture,

[37:13](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2233s) we actually have siloed tenants

[37:15](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2235s) that are our platinum tier tenants.

[37:17](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2237s) They've somehow got some special sort of designation,

[37:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2239s) they're paying a higher price for their service,

[37:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2242s) and they don't wanna share Lambda functions

[37:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2244s) with other tenants, right?

[37:25](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2245s) They don't wanna worry about concurrency issues.

[37:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2248s) They're worried about isolation,

[37:30](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2250s) potentially, considerations,

[37:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2251s) and they want their own dedicated compute,

[37:35](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2255s) even in a Lambda world where you'd say,

[37:37](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2257s) "Well, they're only running in the context

[37:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2258s) "of one tenant at a time anyway."

[37:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2260s) Well, still, now these Lambda functions

[37:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2262s) are actually deployed in the context

[37:44](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2264s) of this individual tenant,

[37:45](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2265s) and that helps with the isolation,

[37:47](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2267s) it helps with concurrency, it helps with lots of things.

[37:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2269s) So here, you'll see that we want two siloed tenants.

[37:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2274s) They're both running their own environment,

[37:56](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2276s) but in that same serverless SaaS solution,

[37:58](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2278s) you'll see that we have

[37:59](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2279s) a pooled environment running alongside of it,

[38:01](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2281s) and the rest of our tenants who are in other tiers,

[38:04](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2284s) basic, advanced, et cetera, are sharing the compute,

[38:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2288s) and this is the pooled model that we've talked about.

[38:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2290s) So if you look at all three of these, they look,

[38:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2292s) well, they're exactly the same.

[38:14](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2294s) What's different here is really just how they're onboarded

[38:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2296s) and how they're configured and how they're set up, right?

[38:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2299s) If I onboard a silo tenant,

[38:21](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2301s) I'm gonna provision a whole new one of these.

[38:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2302s) If I onboard a pool tenant,

[38:23](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2303s) they're just going to go into the pooled model,

[38:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2306s) but there's lots of moving parts

[38:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2308s) behind orchestrating making all this work,

[38:30](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2310s) and there are lots of implications that you'll see

[38:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2313s) in terms of how this affects isolation

[38:34](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2314s) and other considerations.

[38:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2318s) Okay, now, I also wanna highlight the pack across...

[38:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2321s) Hopefully like we saw EKS, we saw serverless,

[38:43](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2323s) we saw how silo and pool plays out differently,

[38:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2326s) I kinda wanna drive home this point that silo

[38:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2329s) and pool is a resource-driven sort of decision, right?

[38:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2333s) So across everything in AWS you touch,

[38:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2337s) storage, queues, compute, whatever is you're touching,

[39:01](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2341s) you're really making that silo versus pool decision

[39:05](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2345s) on a resource-by-resource basis.

[39:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2348s) And to drive that home, you'll see here

[39:09](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2349s) I've got sort of an example here of a system.

[39:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2352s) It starts out with I've got an order service.

[39:14](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2354s) That order service has siloed compute

[39:17](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2357s) because we've decided that,

[39:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2358s) for noisy neighbor or some other reason,

[39:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2360s) we want that compute to be siloed,

[39:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2362s) but it's actually using pooled storage here.

[39:25](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2365s) We've decided we can share the storage.

[39:27](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2367s) And now when we go on to,

[39:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2368s) and it interacts with our product service,

[39:30](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2370s) in our product service,

[39:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2371s) we have both pooled compute and pooled storage.

[39:35](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2375s) So we've decided in this case that's a good fit for this,

[39:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2378s) and that there's not a noisy neighbor concern,

[39:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2380s) and the data can be commingled.

[39:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2382s) We're all good.

[39:43](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2383s) Now we go down to our invoice service,

[39:45](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2385s) and our invoice service says,

[39:47](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2387s) "I can do pooled compute.

[39:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2389s) "That all works.

[39:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2389s) "It fits for my model, but my tenants for invoice data

[39:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2393s) "want the data to be siloed for that," right?

[39:55](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2395s) Our experience needs it to be siloed,

[39:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2397s) and there could be any number of factors

[39:59](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2399s) that might drive that, but the key here is that,

[40:01](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2401s) in this particular example,

[40:02](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2402s) we have pooled compute and siloed storage.

[40:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2406s) Now that goes on and interacts with a couple of queues,

[40:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2408s) sends a message about the invoicing

[40:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2411s) down through this queue to another system,

[40:13](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2413s) and in this case, the queues could have been silo or pool.

[40:15](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2415s) They could have been shared

[40:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2416s) or they could have been separated,

[40:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2418s) and finally we end up at a shipping system.

[40:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2419s) It's pulling data off of these siloed queues,

[40:23](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2423s) and it's running pooled storage and pooled compute.

[40:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2426s) So the whole point here is to drive home the idea

[40:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2428s) that the silo versus pool decision

[40:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2431s) is really meant to be made at a much more granular level,

[40:35](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2435s) and how you make it at each level will also be influenced

[40:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2438s) by what's possible with each AWS stack.

[40:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2441s) How you do this with EKS

[40:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2442s) versus how you do it with Redshift

[40:44](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2444s) versus how you do this with DynamoDB,

[40:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2446s) they could all look different.

[40:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2449s) Okay, so that's sort of, those are some compute

[40:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2453s) and higher-level sort of silo/pool kinda concepts.

[40:56](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2456s) We didn't get into ECS or some of those others,

[40:58](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2458s) but the concepts map very much to those as well.

[41:01](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2461s) I now wanna look at isolation,

[41:03](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2463s) and isolation basically is, how do we ensure

[41:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2466s) that one tenant can't touch the resources of another tenant?

[41:09](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2469s) This is fundamental to SaaS environments,

[41:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2472s) and what are the patterns here?

[41:13](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2473s) And we're gonna start again at a higher level here

[41:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2476s) when we talk about isolation,

[41:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2479s) and focus first on what I'd call resource-level isolation,

[41:23](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2483s) and again, here we're talking about silo-based isolation.

[41:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2486s) In this case, our isolation model is one

[41:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2488s) where a tenant is essentially isolated to a single resource,

[41:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2493s) so a single database or a single compute mode,

[41:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2496s) and here, the isolation boundary

[41:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2498s) is actually that entire resource,

[41:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2501s) and in a resource-based model,

[41:43](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2503s) it's much easier to build an isolation model

[41:47](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2507s) because we usually have constructs

[41:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2509s) that will describe access at this level, right?

[41:52](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2512s) We can say an entire database can only be accessed

[41:55](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2515s) in these scenarios or by these tenants,

[41:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2517s) an entire compute node can only be accessed here,

[41:59](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2519s) so, much easier to describe this,

[42:02](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2522s) and let's look at what that really looks like, right?

[42:05](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2525s) So if we look at some siloed resources,

[42:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2528s) how does isolation actually get attached,

[42:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2530s) and when does it get attached?

[42:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2532s) So here we're gonna look

[42:13](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2533s) at deployment-driven silo isolation, which means isolation

[42:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2538s) that gets applied to our resources at deployment time.

[42:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2542s) So here I have a simple set of EC2 resources.

[42:25](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2545s) They're running on behalf of Tenant 1.

[42:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2548s) They're running in a silo,

[42:29](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2549s) and now because I know these resources

[42:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2551s) are dedicated to Tenant 1,

[42:34](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2554s) I can essentially attach an instance profile

[42:37](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2557s) to these EC2 instances that describe everything

[42:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2560s) that these tenants can touch,

[42:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2561s) what resources are available to them

[42:43](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2563s) and scope it all down to what's valid for Tenant 1.

[42:47](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2567s) So now when this compute goes to access other resources,

[42:51](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2571s) it'll all be scoped to what's valid for Tenant 1.

[42:55](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2575s) So now if I look at Tenant 2 in this same environment,

[42:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2577s) I deploy Tenant 2, and these get deployed

[43:01](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2581s) with this Tenant 2 scoping policy,

[43:03](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2583s) now when Tenant 2 resources try to go access data,

[43:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2586s) they can only access Tenant 2 resources.

[43:09](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2589s) So I can't cross boundaries to Tenant 1's compute,

[43:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2592s) and Tenant 1 can't somehow come over

[43:15](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2595s) and access Tenant 2's data.

[43:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2596s) And the beauty of this is the code running

[43:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2599s) on these compute instances doesn't know anything about this.

[43:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2602s) This is all done at deployment time.

[43:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2604s) It's all attached as policies to this compute in a way

[43:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2608s) that if I ever try to cross a boundary, I'll be prohibited.

[43:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2611s) And if you look at this same model

[43:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2613s) as it plays out on Lambda, very much the same thing.

[43:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2616s) Now I have an execution role.

[43:37](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2617s) When I deploy at deployment time a Lambda function,

[43:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2621s) I can deploy it with a role,

[43:43](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2623s) and now that role will control access to the resources

[43:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2626s) for those Lambda functions,

[43:47](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2627s) and now when Tenant 2 is deployed,

[43:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2629s) it'll get deployed with its execution roles,

[43:51](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2631s) and again, I can't cross the boundaries between them.

[43:55](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2635s) Okay, so that is all sort of resource-driven

[43:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2637s) and this more coarse-grained view of isolation,

[44:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2640s) but we also have in a pool environment

[44:03](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2643s) what we'd call item-level isolation,

[44:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2646s) and in item-level isolation, now our resources

[44:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2650s) and our tenant information is actually shared

[44:14](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2654s) within a resource as individual items.

[44:17](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2657s) So as an example here, I have a database table,

[44:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2659s) and you'll see the individual items here

[44:21](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2661s) are associated with tenants, but this could be a queue.

[44:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2664s) It could be any resource.

[44:25](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2665s) The idea is that we're moving inside the resource,

[44:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2668s) and now individual items inside that resource

[44:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2671s) are the things we need to isolate,

[44:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2673s) and now this is where isolation gets much more tricky,

[44:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2676s) because we usually have good constructs

[44:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2678s) at the resource level for describing isolation,

[44:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2681s) but now we're sort of at the mercy of what's available to us

[44:44](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2684s) when we get to the item level,

[44:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2686s) and actually each approach to isolating

[44:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2689s) at the item level could be different.

[44:52](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2692s) If we wanna look at an example of this

[44:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2693s) and how item level plays out,

[44:56](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2696s) now where we had deployment-time isolation earlier

[44:59](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2699s) when we were talking about the silo,

[45:01](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2701s) now we have to have what I would call runtime-applied

[45:04](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2704s) or runtime-enforced isolation.

[45:07](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2707s) We can't really do this at deployment time.

[45:09](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2709s) So at runtime, when tenants come in

[45:13](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2713s) and they try to access some resource,

[45:15](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2715s) they're all coming into our environment

[45:17](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2717s) against the same resource.

[45:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2718s) It's a pooled resource,

[45:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2720s) so what we have to do at runtime is our code

[45:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2722s) actually has to go out, it has to say,

[45:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2724s) "Oh, you're calling on behalf of Tenant 3.

[45:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2726s) "Let me go find Tenant 3's policy,

[45:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2728s) "and I'll apply that policy,

[45:30](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2730s) "and I'll inject that policy

[45:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2731s) "into the compute that's running."

[45:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2733s) And the key thing here is that the compute,

[45:35](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2735s) when it was deployed, it had to be deployed

[45:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2738s) with a very wide context.

[45:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2739s) It couldn't be scoped down at all.

[45:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2741s) It had to support all tenants.

[45:43](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2743s) So only now at runtime where we go resolve this tenant call

[45:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2746s) to a policy and inject it, do we now,

[45:48](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2748s) our code can now use the credentials back from that

[45:51](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2751s) to go access a piece of data,

[45:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2753s) and that's how we scope our access.

[45:55](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2755s) So here, we're really looking at the difference of runtime

[45:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2757s) versus deployment-time isolation,

[46:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2760s) and the need for this runtime really comes

[46:04](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2764s) with this move to item-level isolation often

[46:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2766s) because that's where the intricacies get harder,

[46:09](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2769s) and this is where we have more shared resources.

[46:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2772s) If you wanna look at what that looks like,

[46:13](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2773s) item-level isolation within a given resource,

[46:17](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2777s) here's a sample policy.

[46:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2778s) We show this one a lot.

[46:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2779s) DynamoDB lets you get down to the item level

[46:21](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2781s) and describe isolation.

[46:23](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2783s) So you'll see that I have a description

[46:25](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2785s) of a leading key that just talks about Tenant 1,

[46:27](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2787s) and will constrain access to items that belong to Tenant 1.

[46:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2791s) So now when I have this DynamoDB table

[46:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2793s) that's got all these different tenants in it,

[46:35](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2795s) this policy will ensure that it can only access data

[46:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2799s) for item one in that table.

[46:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2800s) So this is where that runtime policy comes to life.

[46:43](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2803s) Now, if we were talking about a different AWS service,

[46:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2806s) it would be a different policy and a different approach,

[46:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2809s) but the concept is still the same

[46:50](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2810s) and the pattern is the same,

[46:51](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2811s) which is I need some policy

[46:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2814s) that will constrain access to that item.

[46:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2817s) Now, we talk about isolation certainly as one way

[47:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2820s) of making sure tenants can't adversely affect one another.

[47:04](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2824s) We also wanna be sure that, in a multi-tenant environment,

[47:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2826s) one tenant can't somehow impose load

[47:09](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2829s) that will affect other tenants.

[47:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2831s) So if I have a basic tier tenant

[47:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2832s) that's sending a million API requests,

[47:14](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2834s) they could be affecting my platinum tier tenant.

[47:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2836s) So we say as part of the patterns,

[47:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2838s) you should have some kind of tier-based throttling

[47:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2840s) in your system.

[47:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2842s) And if we look here,

[47:23](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2843s) here's an example of a tier-based throttling solution

[47:25](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2845s) using API Gateway,

[47:27](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2847s) and here, API Gateway has this notion

[47:30](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2850s) of usage plans and API keys.

[47:32](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2852s) So essentially we can set up separate API keys

[47:35](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2855s) for each tier of our system.

[47:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2856s) So a basic tier user could have one API key,

[47:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2860s) an advanced tier, another API key,

[47:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2862s) and then those API keys would map me

[47:44](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2864s) to different usage plans that had different policies

[47:47](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2867s) that would control their throttling separately.

[47:50](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2870s) So now when a request comes in,

[47:52](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2872s) a Lambda authorizer can sort of look up the API key,

[47:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2874s) figure out what your usage plan needs to be,

[47:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2877s) and then control the flow to the downstream requests.

[48:01](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2881s) So if the basic tier is exceeding the limits

[48:05](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2885s) of their usage plan, the throttling policies

[48:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2888s) of that usage plan will get kicked in,

[48:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2890s) and this will keep a basic tier tenant

[48:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2892s) from affecting a higher-tier tenant potentially.

[48:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2896s) Now obviously, I showed you API Gateway,

[48:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2898s) and this is a perfectly good way to do it,

[48:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2900s) but you can imagine with EKS, for example,

[48:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2902s) I can set up service quotas inside of my namespaces

[48:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2906s) and use that as a way to control throttling.

[48:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2908s) The real takeaway here is that somewhere in the entry point

[48:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2911s) to the services of your application,

[48:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2913s) you oughta have some kind of tier-based policies

[48:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2916s) that are used to decide how you'll apply throttling

[48:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2919s) and ensure that you don't get

[48:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2921s) one tier adversely affecting another.

[48:45](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2925s) Now the other piece we wanna look at,

[48:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2926s) we said we have all these cool things,

[48:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2929s) like we talked about injecting JWT tokens

[48:51](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2931s) and applying policies,

[48:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2933s) but what does that really mean to the person

[48:55](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2935s) who's writing microservices in your system?

[48:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2937s) What's the impact on them?

[48:59](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2939s) And one of the patterns we talk about here is

[49:01](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2941s) you should be building microservices

[49:03](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2943s) that make it as simple as possible

[49:05](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2945s) for application developers.

[49:07](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2947s) So if I'm writing a microservice,

[49:09](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2949s) a product or an order service,

[49:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2951s) I don't really wanna know how to deal

[49:13](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2953s) with tenant context or tenant IDs.

[49:15](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2955s) I don't really wanna know how to deal

[49:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2956s) with these isolation policies.

[49:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2958s) Can you take that all out of my view?

[49:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2960s) And so what we're really saying here is

[49:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2962s) build libraries, reusable libraries.

[49:25](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2965s) If that's Java JAR files, if it's .NET assembly,

[49:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2968s) if you're using middleware,

[49:29](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2969s) whatever the language construct you're using,

[49:32](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2972s) take all these multi-tenant constructs

[49:34](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2974s) and multi-tenant libraries,

[49:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2976s) and take them away from your code

[49:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2979s) and make them reusable across your microservices.

[49:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2982s) Now here I'm showing it with Lambda

[49:44](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2984s) 'cause Lambda has this really cool thing called layers,

[49:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2986s) and layers let me sort of put shared code one place

[49:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2989s) and deploy it separately,

[49:50](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2990s) and then share it across my Lambda functions.

[49:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2993s) So here inside my layers,

[49:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2994s) you'll see I have all these helper functions.

[49:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2997s) I've got a log manager, a metrics manager,

[49:59](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=2999s) that are used to just generate tenant contextual logs

[50:02](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3002s) and metric events where the service doesn't know about it.

[50:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3006s) I have access to this token vending machine,

[50:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3008s) another piece of sample code we have out there,

[50:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3010s) that will let me go get the credentials

[50:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3012s) in this runtime resolution of policies,

[50:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3016s) that example we talked about earlier for isolation,

[50:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3018s) and I've got this token manager that just resolves.

[50:21](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3021s) It cracks open a JWT and gets me a tenant ID.

[50:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3024s) So the basic idea is I care less

[50:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3026s) about what's in the specific libraries

[50:29](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3029s) and more that you have these libraries,

[50:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3031s) and that you're moving tenant details

[50:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3033s) away from the microservice developers.

[50:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3036s) Now we're also gonna touch very quickly here

[50:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3039s) on data partitioning, and we're gonna move through this fast

[50:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3041s) because the models and the ideas of data partitioning

[50:44](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3044s) are pretty straightforward to me.

[50:45](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3045s) You have silo, we have pool, really.

[50:47](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3047s) In the silo model, we're basically saying

[50:50](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3050s) each tenant's gonna get their own storage construct.

[50:52](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3052s) If that's EKS, I'm sorry, if that's Redshift

[50:56](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3056s) or if that's DynamoDB,

[51:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3060s) each one of those different storage technologies

[51:03](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3063s) has a different way to represent silo.

[51:05](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3065s) Could it be a separate database per tenant?

[51:07](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3067s) Could it be a separate cluster per tenant?

[51:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3068s) Each one of those is different,

[51:09](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3069s) and we have guidance on those,

[51:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3071s) but the basic principle is you're picking some unit

[51:15](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3075s) of that storage technology,

[51:17](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3077s) and you're not commingling data there, right?

[51:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3079s) That data in there is dedicated to a given tenant.

[51:23](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3083s) If you look at a pool model,

[51:25](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3085s) the basic idea is whatever the storage mechanism I'm using,

[51:29](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3089s) data mechanism is,

[51:30](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3090s) that the data is commingled for the tenant.

[51:32](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3092s) It sits side by side, right?

[51:34](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3094s) And again, what's the commingling look like?

[51:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3096s) Well, it looks different

[51:37](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3097s) across different AWS services and technologies,

[51:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3100s) but the premise is still the same,

[51:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3102s) and really this comes back

[51:43](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3103s) to noisy neighbor, tenant isolation.

[51:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3106s) How would you apply those to these concepts?

[51:48](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3108s) So if you look at RDS, you'll see that RDS,

[51:50](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3110s) we've got here an RDS instance.

[51:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3113s) This could be a separate table,

[51:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3114s) could be a separate database per tenant,

[51:56](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3116s) kinda depends on where you wanna go, a separate instance,

[51:59](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3119s) and on the pooled model,

[52:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3120s) you'll see, oh, all the data's in the same table,

[52:03](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3123s) but we're using a foreign key

[52:04](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3124s) that is the tenant ID to get here.

[52:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3126s) Pretty straightforward stuff,

[52:07](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3127s) and lots of content out there,

[52:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3130s) but a pretty straightforward pattern.

[52:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3132s) I did wanna highlight though that,

[52:13](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3133s) as you move out into the different AWS services,

[52:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3136s) you can definitely see lots more things

[52:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3139s) to think about, right?

[52:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3140s) In S3, as an example, am I gonna use a bucket per tenant?

[52:23](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3143s) Could I use a separate prefix per tenant?

[52:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3146s) I can use tags if I want to

[52:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3148s) as a way to separate tenant information,

[52:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3151s) or even use access points, right?

[52:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3153s) So here even, or if I go over to elastic search,

[52:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3156s) am I using a separate index, a separate cluster?

[52:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3158s) There's lots of options here,

[52:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3159s) and we continue to try to produce information here

[52:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3162s) to help you understand what the practices are

[52:45](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3165s) for each one of those services,

[52:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3166s) but it's still always gonna come back to,

[52:48](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3168s) what's the silo model,

[52:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3169s) what's the pool model for representing storage?

[52:52](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3172s) I will highlight here that I would like this to be

[52:55](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3175s) a domain-driven experience, right?

[52:58](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3178s) When people are thinking about data partitioning,

[53:00](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3180s) I want them to get all the way down

[53:01](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3181s) to the microservice level to say,

[53:03](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3183s) "What's the right data partitioning story

[53:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3186s) "for this particular microservice?"

[53:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3188s) So here I've shown three different microservices,

[53:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3191s) and they have three different data partitioning schemes.

[53:15](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3195s) Order service is using silo, product is using pool,

[53:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3199s) and this rating service has a mix

[53:21](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3201s) of those two going on, right?

[53:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3202s) Well, I want you to have thought about,

[53:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3204s) what's the noisy neighbor,

[53:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3206s) what's the performance, what's the latency,

[53:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3208s) what's the isolation story of that service,

[53:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3211s) and figure out which model is gonna best fit that service.

[53:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3216s) So I definitely don't want you thinking,

[53:37](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3217s) "Hey, we picked silo for our SaaS.

[53:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3219s) "Now everything is silo."

[53:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3220s) No.

[53:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3221s) Ask yourself on a service-by-service basis

[53:43](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3223s) what your approach oughta be.

[53:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3226s) Okay, finally, I know we rushed through this.

[53:48](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3228s) I'm trying to squeeze a lot into this time,

[53:49](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3229s) so apologies for this being a little bit hurried,

[53:52](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3232s) but we're trying to fit as much in as we can.

[53:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3234s) I do wanna hit on a few takeaways.

[53:56](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3236s) Hopefully it's really clear

[53:57](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3237s) that there's no one universal SaaS blueprint, right?

[54:02](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3242s) We're really trying to find the mix of things

[54:04](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3244s) that are the realities in your domain,

[54:06](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3246s) the realities in your business,

[54:08](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3248s) and then take these patterns that we talked about today

[54:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3250s) and find out which combination

[54:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3252s) of those things best address the needs of your environment.

[54:17](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3257s) And I also wanna highlight this idea

[54:19](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3259s) that classically the notion of multitenancy has been

[54:21](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3261s) that this is just about shared infrastructure.

[54:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3264s) Hopefully it's pretty clear

[54:24](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3264s) from this discussion that, to me,

[54:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3266s) multi-tenant doesn't mean you're sharing infrastructure.

[54:29](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3269s) I can have siloed infrastructure

[54:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3271s) and still run a multi-tenant SaaS business

[54:33](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3273s) because it all has a common operation and control plane,

[54:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3276s) and the fact that they're all running the same version

[54:38](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3278s) and they're all managed by the same experience,

[54:40](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3280s) that's what makes it multi-tenant,

[54:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3282s) and then, yes, some resources will be shared.

[54:45](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3285s) Some will be dedicated,

[54:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3286s) and that's more of sort of an application,

[54:48](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3288s) deployment, and design decision.

[54:51](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3291s) Clearly, to me, I've really tried to drive home the fact

[54:54](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3294s) that control plane is essential here.

[54:56](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3296s) This is really what's gonna drive agility

[54:58](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3298s) and innovation in your business,

[54:59](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3299s) and if you're starting from scratch,

[55:01](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3301s) think a lot about that control plane.

[55:04](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3304s) And then, obviously, we touched on just a few

[55:07](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3307s) of the AWS services here, right?

[55:09](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3309s) The approach for these patterns,

[55:11](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3311s) the approach for deployment,

[55:12](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3312s) the approach for silo/pool varies

[55:15](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3315s) across each one of these stacks,

[55:16](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3316s) but hopefully at the meta level,

[55:18](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3318s) you can kind of see the common themes of these patterns

[55:21](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3321s) and then just apply them to each of those services.

[55:25](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3325s) And then silo and pool,

[55:26](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3326s) we just sort of talked about this,

[55:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3328s) that silo and pool is a resource-level decision.

[55:31](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3331s) It isn't a system decision.

[55:32](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3332s) It's a resource-by-resource decision,

[55:35](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3335s) and you should be making that choice

[55:36](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3336s) on a resource-by-resource basis.

[55:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3339s) And then tiering is one of these things

[55:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3341s) that gets lost a lot in this.

[55:43](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3343s) People won't have tiering,

[55:44](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3344s) and I think you oughta be thinking about tiering

[55:46](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3346s) all across the architecture system.

[55:48](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3348s) How's it gonna affect isolation?

[55:50](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3350s) How's it going to affect the throttling of experiences?

[55:53](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3353s) How can you be sure that each tier is getting

[55:56](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3356s) the experience they're supposed to get?

[55:58](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3358s) And then finally, find the best mix of these patterns

[56:02](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3362s) that really fits your environment, right?

[56:03](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3363s) Look across the landscape.

[56:05](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3365s) Hopefully you've got enough exposure from this talk

[56:07](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3367s) to sorta get a sense of what those options are,

[56:09](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3369s) and find the mix

[56:10](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3370s) that best meets the needs of your environment.

[56:13](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3373s) Okay, quickly, I just wanna hit on the fact

[56:15](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3375s) that there are some other sessions going on.

[56:17](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3377s) I have more breakouts.

[56:17](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3377s) We have some awesome workshops going on and Chalk Talks,

[56:20](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3380s) and even a business session,

[56:22](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3382s) so a pretty full list of SaaS content

[56:25](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3385s) out there for you at re:Invent.

[56:27](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3387s) And that's it.

[56:28](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3388s) I really appreciate you taking the time to sit through this,

[56:32](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3392s) and hopefully it was valuable for you,

[56:34](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3394s) and definitely looking forward

[56:37](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3397s) to sort of evolving these patterns based on

[56:39](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3399s) what we learn from the community,

[56:41](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3401s) so, thanks so much.

[56:42](https://www.youtube.com/watch?v=j7Sqt8GpYl0&t=3402s) (upbeat music)

