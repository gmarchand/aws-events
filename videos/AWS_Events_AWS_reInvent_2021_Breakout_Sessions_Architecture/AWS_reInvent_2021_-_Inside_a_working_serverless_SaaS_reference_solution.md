# AWS re:Invent 2021 - Inside a working serverless SaaS reference solution

[Video Link](https://www.youtube.com/watch?v=8Z5zBsKgTxY)

## Description

The serverless SaaS model presents architects and developers with a range of new multi-tenant design considerations. How do you implement tenant isolation in an AWS Lambda environment? How do you support tiering and noisy-neighbor conditions? How do you build multi-tenant-aware microservices in a serverless model? These are among the topics explored in this session, which covers a reference solution. Consider the code, design, and architecture strategies used to construct a serverless SaaS environment (highlighting key considerations and tradeoffs).

Learn more about re:Invent 2021 at https://bit.ly/3IvOLtK
 
Subscribe: 
More AWS videos http://bit.ly/2O3zS75 
More AWS events videos http://bit.ly/316g9t4

ABOUT AWS
Amazon Web Services (AWS) hosts events, both online and in-person, bringing the cloud computing community together to connect, collaborate, and learn from AWS experts.

AWS is the world’s most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally. Millions of customers—including the fastest-growing startups, largest enterprises, and leading government agencies—are using AWS to lower costs, become more agile, and innovate faster.

#AWS #AmazonWebServices #CloudComputing

## Transcript

(upbeat music) Hey, everybody, thanks so much for joining my session today. As the slide says, my name's Tod Golding, and I'm a partner solutions architect here at AWS and I'm part of a team that's called the SaaS Factory, and that team builds, delivers, optimizes SaaS solutions on top of AWS, and over the last few years, we've been building a lot of content around SaaS best practices of whitepapers, blog posts, targeted solutions. So we've shown people how to do data partitioning and isolation in these pocketed solutions, but we've also said we'd really like to build prescriptive solutions that show people an end-to-end working environment. So instead of just focusing on pockets of specific SaaS patterns or best practices, how could we show you an entire application and what the moving parts of that application would look like, and what would it mean for you as a developer to orchestrate everything that's needed to make that work? And so, to accommodate that, we created, actually, two reference architectures. One that I'm speaking on here at AWS about, EKS, and the one we're talking about today, which is serverless SaaS, and the goal of this session really is to dig into that serverless SaaS architecture and really show you all the moving parts inside of it here, so we're gonna look at how isolation, and onboarding, and all of these things we talk about around SaaS come to life in a real working SaaS application. And our goal here is to expose you to all the moving parts of that reference solution and let you see all the sort of nuances that are involved in making it all work. Now, I really wanna highlight the fact that this is a reference solution, right? We've chosen some specific strategies and we've picked some specific sort of approaches to implement this specific serverless SaaS environment, but you should know that there's more than one way to implement serverless SaaS on top of AWS, and you could see us morphing this reference solution or creating new reference solutions as we go along, but the overall hope here is that you can take this reference solution, I'll give you a link at the end, download it, and either use it as the starting point of a solution you might be building or just use it as a way to get yourself much more familiar with what's involved in actually building a full SaaS, serverless SaaS, solution. Now I will highlight the fact that this is a 400-level session, so we're not gonna be just covering fundamentals of serverless SaaS, and we're not gonna teach like the basics of the architecture. Our goal, really, here is to sort of get into the weeds. We wanna look under the hood of this solution and, in fact, go all the way down to the code at some point. Now, we're not gonna crack open the IDE or anything like that, but we'll pull up some snippets of code and give you a sense of what's going on under the hood, what's really making this work, and the idea is that hopefully you'll take all that knowledge away, and if you take that and you look at the reference solution, it'll give you overall a better sense of what the overall landscape looks like. Now, before we dig into the actual architecture, it's good to stop and ask ourselves, why serverless for SaaS? Why is it such a good fit? And if you look generally at what we're doing in SaaS environments, a lot of what our effort and energy goes into is trying to somehow anticipate tenant activity and then map our consumption of infrastructure resources to that, to that, those consumption patterns, and so what I did here is I've created a simple graph. We've shown this before, but essentially the blue line of this graph represents the trends of consumption inside your SaaS application, and this is the realistic universe of SaaS, right? Sometimes we've got these peaks and valleys of activity. Sometimes we're adding new tenants and the load is changing all the time, and it gets really hard to anticipate where the peaks and valleys of that activity will be or how to build an infrastructure that responds correctly to that, but in the dream world, we'd get this red line that you see here where the infrastructure consumption of our environment would align perfectly to the actual tenant activity, 'cause that's our real goal as SaaS architects. We wanna have just enough infrastructure to support the environment that we're spinning up here, and to me, this is the sweet spot of serverless SaaS. Yes, EKS, ECS, lots of others do a good job here, but here in serverless, we are truly without servers, so we don't have to think about scaling policies or what our provisioning sort of experience is. We essentially consume what we need, and we only pay for what we need. The other dimension of this is that just generally the deployment and the life cycle of managing and operating these serverless SaaS environments tends to be lower in this function-based model where everything is serverless as well, so rolling out new features, doing canary releases, all those things get a lot easier to me in the serverless SaaS environment, and here's where we get the better agility, the better efficiency that we're after operationally, a lot of those good things we really wanna focus on. We also tend to be able to now focus more of our time and energy on the actual IP of our solution. Now, I'm not saying that serverless means that you should only use serverless for SaaS environments, but it is a good fit, and EKS is still a good fit for others. ECS is still a good fit. EC2 can be a fit. There's just some natural alignment here that's worth highlighting. The other piece of the puzzle here is we really wanted to just quickly talk to you a little bit about what sort of thought process went into the serverless SaaS reference architecture. What were the key architectural decisions we made, and specifically which serverless architecture decisions did we make? And one of the really big ones here was the deployment model we chose, right? 'Cause we really wanted to highlight the fact that in a serverless SaaS environment, you really are picking, often, between multiple deployment modes. Can I deploy everything in a pool model where tenants are sharing resources? Can I deploy in a silo model where tenants maybe have dedicated resources? And what we really wanted to do here was offer you a hybrid of those and show what it'd mean to support both of those deployment models in an environment, and that had a huge ripple effect through the overall architecture of our solution, and you're gonna see that. The other thing here is how did we automate those deployments based on tiers? What's all the infrastructure and code that we had to put in place to automate this complex deployment model, right? We're now supporting multiple deployments, and that really had a real influence on the overall automation strategy of our onboarding experience. Now, the other piece we're gonna look at is this noisy neighbor scenario. Even in serverless environments, there's still a potential for you to have noisy neighbor conditions, and so we had to think about, well, what strategies would we use? How would we build our serverless SaaS reference architecture in a way that would limit your potential to have noisy neighbor and manage that noisy neighbor experience on your own? Now, tenant isolation is something we look at in every environment, and certainly there are things in this reference architecture that are similar to the other reference environments we have. However, there are a handful of considerations here and a handful of strategies we've used for isolation that are unique to the serverless bit, so we'll dig into what's particularly unique about the serverless model and how it influences your approach to isolation. And then lastly, we'll look at tiers and just generally how to use tiering strategies to control and influence the experience of your environment. Okay, enough background and history of how we got here. Let's dig into the high-level architecture of your solution, right? Let's just see what the overall landscape of this EKS reference architecture looks like, and you're gonna see that we've, actually, the solution breaks into two very distinct pieces. The first piece of the puzzle is what we call the control plane, and here in the control plane is where all the horizontal services live for your server, for your serverless SaaS environment, right? This is where we see registration, and onboarding, and tenant provisioning, all of these things that are needed to just manage and operate your business, and here we'll have an administrative application, and that administrative application will actually be used to control and interact with the control plane services, so manage tenants, manage users, and so on. And I should highlight the fact that this control plane is fundamental to building a really good SaaS environment. You'll see it across all the SaaS solutions we build, and we very much encourage organizations. Hey, if you're really trying to get innovation and agility out of your SaaS environment, pour a lot of energy into building a really good control plane because it's the single pane of glass that manages and operates everything about your SaaS environment. Now, it's interesting to note that the control plane actually doesn't have multi-tenant code in it, right? There's no multi-tenancy over there. These are just services that are managing your multi-tenant environment. Where the multi-tenancy really shows up is over in what we'd call the application plane of your environment, and this is where the application lives. This is where you'll see that we have basically a classic sort of serverless web application here. We have an S3 bucket, an API Gateway, and a set of microservices, and those are all being accessed by some sample SaaS application that we have, and on the surface this looks just like any other application, but what we're gonna find is when we dig into the weeds of this application, you're gonna see where data partitioning and isolation and routing show up at the API Gateway. They show up inside of our microservices, so there's lots more moving parts to SaaS inside this application plane that just aren't here at this level. But overall, this is the landscape of what we're going to run and build as part of this environment and ultimately the high-level view of what you get in the box with the serverless SaaS solution. So now let's dig into the control plane part itself first. Let's start there and look at what happens when you actually provision the control plane, because I showed you this high-level view of the control plane, but the reality is there are a lot more moving parts to that control plane and a lot of automation that happens behind the scenes to bring to life all the moving parts of that control plane. So when you look inside the serverless SaaS solution, you're gonna see that we have this bootstrap template in the repo. You'll see it there, and this bootstrap template is responsible for spinning up the whole environment that is the baseline environment of this solution before any tenants are introduced. So I wanna walk you through a little bit of the moving parts here of the template that's a part of this bootstrap template and the components of it, and if you look at these, you'll see these correlate straight to the template code that's inside the repo. So there's this create tables step where we'll create all of these different tables that are needed to manage state and information about our environment. You'll see we have a tenant user mapping table, and we'll get into the details of what that involves, but essentially how we're gonna map user pools, and so on, the tenant details table, where we actually store all the details and configuration of the tenant, and this tenant stack mapping table, which plays a key role in supporting this silo and pool model. So we'll poke at all those tables. You also see that we create user pools here as part of this template. So you'll see that we create a pooled user pool from the beginning, and that pooled user pool is really meant to represent all those users that are gonna be our pooled model. They're gonna share one user pool for all of them. And then we also create a user pool for our admin users, and here the admin users are the SaaS providers themselves, right? This is where your admin application authenticates, so we know we're gonna need those two as a baseline so we provision them at the start and then we have to provision the actual microservices, right? Before, I showed you in that control plane we had user management, tenant management. This is where we provision and configure all of those microservices. Now, these are Lambda functions, but they're Lambda functions in what I would call a logical or a composite sort of microservice where multiple functions are part of one microservice. So tenant management is composed from multiple Lambda functions. You'll also see that we set up the API Gateway here, so it's not just a matter of provisioning the Gateway. It's a matter of provisioning and configuring the Gateway for all the routes and the permissions and everything else that have to get set up for this to work. And then we'll set up the actual web applications, and there's three applications that are part of this overall experience. There is an admin application that we talked about that is the SaaS provider experience. There's a SaaS e-commerce-y kind of app, a really lightweight e-commerce app just to show what your SaaS application would look like, and then there's a landing page. There's landing pages for self-service sign-up into your solution. And so for each of these, we have to provision the usual constructs that are needed for an application, a web application in a serverless model. So we'll set up the S3 buckets, we'll set up the CloudFront bits to host those applications, and then the last piece are these custom resources, and these custom resources are really just, if you're familiar with CloudFormation, these are custom resources in CloudFormation that include the custom code we need to trigger certain onboarding events. So, for example, there's a settings table and there's a tenant stack map that are part of our provisioning experience, and those tables are run from CloudFormation templates, and therefore they need these custom resources to make all that work. But anyway, this is all the high-level view of all the pieces that get created when you run this bootstrap template, and obviously now, if you poke into the code, you should see a pretty good correlation between what's here and what's actually in that template file. Okay, now, before we go deeper into the architecture, I wanna make it really clear, and I kind of talked about the need for different deployment models, but I really wanna make it clear that there are two very distinct deployment models for this reference architecture, and we intentionally are trying to show this off. We've talked an awful lot about the fact that some SaaS environments aren't just pool, where resources are shared for tenants, or silo. Those two don't have to be mutually exclusive, and so in this environment, we wanted to do what we often tell our customers to do, which is sometimes you have to support both, which is some tenants are in the silo model and they have dedicated infrastructure and some of your tenants will be in the pooled model, and you'll use tiering to separate those experiences. So at a conceptual level, we'll have onboarding, and now as each tenant onboards, in this case, a platinum tier tenant onboards, because it's platinum tier, we'll actually provision a silo for that tenant because they get dedicated resources here and we'll provision a silo for the next tenant that onboards. However, the other tiers in our environment, when they're signing up and onboarding into our experience, so premium, standard, basic, and so on, when they come in, they are going to go into our pooled infrastructure. So here we won't provision new infrastructure for them. We'll just configure for them the bits that help them consume the pooled resources that are part of the environment, and to me, this whole experience of supporting silo and pool side by side is one of the more exciting bits of the serverless SaaS environment. I wanna see this, in fact, show up in more of our reference architectures, because I think seeing all the moving parts of this and seeing how this influences the whole architecture is pretty eye-opening and, I think, pretty useful to a lot of organizations that need to support this model. Okay, so now we've seen that environment and we've seen we have these different deployment models. Let's look at what it means to register a new tenant through the control plane. So when we come into the control plane, we can come in one of two ways to register a new tenant. We can come in through the landing page and say, "Hey, this is a self-service sign up. I'll sign up, I'll provide you my information, my plan, et cetera, and I will sign up," or you can come through the admin console and you can actually trigger an onboarding by filling that out, information out through that, and we provided that experience through two different paths because we wanna acknowledge the reality that some organizations will have self-service, some will not. Some will trigger that only through internally-driven processes, but the reality is whether it's self-service or not, it's all gonna come through one registration experience. So the code behind it, all the microservices that orchestrate it all, are all the same, and in fact, this registration or onboarding flow is common to almost all of our architectures. It just varies a little bit depending upon some of the choices that you make. So here registration will essentially orchestrate all of the onboarding experience. So here, when I say I wanna register a new tenant, we'll go out and create a new user in the user pool, in this case, Cognito. Now, interestingly, because we're showing, supporting both silo and pool models, we actually have some conditional bits here, right? If you're coming in as a silo user, we're actually gonna give you your own user pool. However, if you're coming in as a pooled user in one of those tiers, we're gonna share the user pool amongst the tenants, and there's some orchestration that has to happen there and some configuration that has to happen there to support that. And then, of course, we're actually gonna create that first user that signed up, that tenant admin user, as part of this experience. Now, as part of this also, you're gonna see that we also configure custom claims in Cognito to identify the binding between the user and the tenant, and so later, when we look at authentication, you'll see how the tokens that come out of that experience return us a token that is enriched with both tenant information and user information. And we also have to create a tenant here, so we'll essentially call that service, and this is where, yes, we'll create the tenant with their identifier and their plan, but we're also gonna store lots of configuration information in here about this tenant, and you'll see how that configuration information actually is used during authentication and other parts of this experience. And then the last piece is this provisionings piece, and this is the piece that lots of people will overlook, right? They'll think, "Well, we're only pooled, so we don't need it," but now in this model where we're supporting both pool and silo models, a lot of effort and energy goes into this tenant provisioning experience, because if you're silo, I actually have to provision separate infrastructure for you as a tenant. But ultimately, when this is done, right, when I've created the user, created the tenant, and the registration is done, everything is done, a tenant is now in the system and ready to be activated and used, and that tenant can essentially come and log in and begin to use the service, and getting all of this orchestrated and frictionless is essential to building a SaaS environment that can scale. Now, if we look at tier-driven onboarding and what that actually looks like, so imagine we have this environment. We've provisioned this baseline environment. We've created this pool environment 'cause we know we need to pool from the beginning, so it's there, and we've onboarded a couple of tenants to that, into that pooled environment. Now, when we add a new tenant here, that provisioning experience will simply configure a new tenant and add them to the pool experience. Now, I could also have a siloed tenant here. This tenant's running. It's got dedicated resources and has been provisioned in a dedicated environment, and one nuance here that sometimes gets lost on people is that sometimes people will say, "Why do you need to have siloed environments in a Lambda environment? Because every time I execute a function, I'm only executing it on behalf of a single tenant at a moment in time." However, when you get into the details here, and you'll see this as we go further on, it actually affects the isolation story 'cause I can implement a different isolation story if I know those functions are dedicated, and it starts affecting noisy neighbor and other conditions in terms of concurrency and other factors. So even though Lambda's only executed at a moment in time for a tenant, there's still value in siloing it off and offering it separately, and customers may just demand that anyway, even if they were 100% equivalent. So now when we onboard another tenant, now you'll see we fire off, this is a siloed tenant, we fire off the CodePipeline. It provisions all the bits and adds it to our environment. So this is very high level. Obviously I'm showing microservices as the core of the provisioning. There's more pieces getting provisioned as part of this experience, but that's conceptually what's going on. So let's look inside that provisioning experience a little bit and see what's going on. If you go look at that bootstrap template that we talked about at the beginning, one of the things it does is it calls this custom resource, the update tenant stack table resource, and it's essentially saying, "Hey, when I first build this environment and I first spin it up, I need a pooled environment, and so what I'm gonna do is I'm gonna call this custom resource." This custom resource will essentially go put an entry into a DynamoDB table, and that DynamoDB table will say, "Hey, I need to create a new stack. It's a pooled stack, and I need to go get it created and provisioned for this baseline environment." Then a pipeline will essentially pick that up. Pipeline will say, "Hey, there's a new environment needs to be created," and then it'll go to this tenant template and that tenant template will then provision everything, and we'll look at that tenant template there in a little more detail, but it will essentially provision everything that's needed for the pool, and now we're ready to start accepting pooled customers. But what I thought was really cool about the solution here that the team built is that now we use this exact same process when we onboard a siloed tenant. So now if a siloed tenant comes along and they wanna add the infrastructure for the tenant, we don't create an entirely separate process. Instead, we essentially put a row into this table and that table says, "Hey, a new siloed tenant needs to be onboarded," and the CodePipeline picks that up, and then it goes over to the tenant table and it creates the siloed stack. And so if I add more tenants through this process that are siloed, it would just continue to put entries in the table and continue to add siloed tenants, and to me, the reuse of this and the fact that this is a common mechanism means that I can essentially change what gets provisioned and the plumbing of that whole end-to-end experience still works fine. So let's look now inside of what actually happens when we're creating that tenant stack. So we talked about that last template in that process. Well, what does it actually do to provision our tenant environments? Well, first of all, it creates the product and order tables, right? We need to have these two product and order microservices and it needs to create a table for each of those, and then it also needs to actually deploy our microservices. So here we've got a product and an order microservice. It configures and sets up the functions for all of those bits and then it sets up the API Gateway as the entry point to these microservices, and then the last bit is it configures the permissions and so on. So if you go to poke into that stack and look inside of it, you'll see that these are the basic parts it's orchestrating, and you can see that they're shared between pooled and silo, and to me, this is also awesome that it's all shared because even though we're gonna allow pool and silo to have different stacks, we're not gonna allow them to run different versions of the code. We don't want one-off infrastructure for them, so having this be all one process is particularly powerful. Now, the other piece of this that gets lost in the shuffle is, yes, we can onboard a tenant. We can get them into the system and we provision all their infrastructure, but what happens when we need to roll out an update? Like we wanna update a new version of the order service so we wanna roll out some new features or functionality, and now we have these different stacks that are running. Well, this is where we introduced a table, and I don't know, there's lots of ways to implement this mechanism, but we used a table to capture and describe which stacks were out there. So you see here we have this TenantStackMapping. I talked at the beginning how this table gets provisioned, and this is the table that keeps track of all the different stacks that have been created, and you'll see the first two rows are actually two siloed tenants. So they have their tenant ID there, and then we have a third one we called pooled. We named it pooled 'cause it made it easier. This is that pooled one that got created at the beginning in the baseline. And then you'll see we have an applyLatest column here, and this is actually used to figure out who's actually gonna get the latest code deployed to them, and this is where we can actually do canary releases. This isn't about keeping somebody off the latest version. It's about saying, "Hey, we're deploying, and let's just deploy to these particular tenants first and then we'll deploy to the rest." So it's kind of a clever way we've introduced here just to manage that. And then the rest is just the CodeCommit and the stack names and so on. So this table, essentially, now, when we deploy a new feature and we hit the source and the build and the deploy process, that deploy process can look at that table and say, "Who do I have to deploy to? Oh, well, I've gotta deploy to pooled, 'cause I know I have a stack for that, and then I have two silos that I have to deploy to." So to me, this is the overlooked piece of the puzzle, right? Everybody focuses on the provisioning and the initial provisioning, but you also have to focus on the deployment. Once these environments are out there and they're separate, how can we automate and track that deployment as well? Now, if you look at how we actually do this in the code and how we apply this and where tiering shows up inside the code, I did wanna grab a couple of snippets of code just to show you bits here. So this is the register_tenant bit, and you'll see here when we're registering a tenant, we look at the different tiers, and in this case, we're assigning a different API key, right? So it could have been any sort of attribute. I just wanna show you that, hey, as we're in the code, we're actually doing these tier-based activities during the creation of a tenant, and you'll see how we use these API keys later. And then later on, you'll see that we essentially go fill in all those attributes that we get back from setting up the user pool and all those other bits that are configured, and we essentially persist that information about the tenant by calling the tenant management service with all those different attributes. So you can see tier laced into this, and then you can see how we're capturing all this configuration data and storing it in the tenant, and then later on we'll come back and reference it. Okay, now one of the key parts of this is during the provisioning process, how do I actually trigger that pipeline to onboard a new tenant? So if I'm inside my code and I'm looking at where in the code in this process, well, if you go look at the provision_tenant function here and you look at inside the details here, you'll see where we're actually inserting an item into that table. So when we put an entry into that stack mapping table, then we can actually go and then trigger the pipeline from our code, and that will make that overall process work. So if you're hunting for that, this lands in this particular function here, and you can see how essentially all we're doing is just inserting a row and kicking off the pipeline. Now, another part of the control plane that's a more simple version of this if we move away from provisioning is this management of tenants and users, right? We still have to have some way to manage the life cycle of individual tenants. Are they enabled, disabled? How do we edit their state? How do we edit information about their policies, and so on? And we also have the need to manage users. We have both to manage tenant users and admin users, and these are just additional services that are inside the control plane. So here you'll see you have an admin console. That admin console will hit the tenant management service, and this is where we'll update the state of the tenant through that experience, but also through the admin console, I can hit the user management service and I can update and add users to the admin console, traditional sort of user management here. And, of course, our SaaS application also has to manage tenant users and be able to add new users as part of their experience, and that happens through the SaaS application. Now here, you'll see we've shared user management. You could easily have pulled these apart and have a separate admin user management, but the code mostly was similar for these two, so we shared that as one service, and then they're just managing that state inside of Cognito. Now, if we look at the code behind creating a user and creating a tenant, really straightforward code. The really interesting thing is when you look at this create_user piece, you'll see a line of code near the bottom where we're actually setting the tenant ID into the attributes of the tenant. So here we're basically, yes, we're populating the attributes of the user when we're creating the user, but we're also filling in tenant context as part of that so when the tenant gets persisted into Cognito, we'll have that extra bit of data, and then when we go to create the tenant, we're really just filling out all these different attributes that we need, all this different configuration bits and persisting that data, and we'll look at what some of that data is that lands there, but really, really basic operations code, so not very complex here. Okay, so now we have the ability to introduce a tenant into our environment. We have all that onboarding bits, all that provisioning goodness that we talked about. Now how do we actually authenticate a user and authorize their access to the resources that are part of our application? So here, when we come into this experience, we'll have a tenant come in. They'll hit our SaaS application and that SaaS application will actually redirect them to a hosted UI that Cognito provides. So Cognito provides this ability to basically offer you a login experience. We've used that in this solution. We redirect that hosted UI. You now log in through that experience. You authenticate as that user that we created before, and back from that comes that JWT token that we talked about, and that JWT token has this user and tenant context in it, and now we pass that JWT token along to the API Gateway and downstream to the services that are part of our application. So here we come into the API Gateway, and the first thing we do inside the API Gateway is the authorizer actually wants to look at who's making the request and apply some authorization sort of policies here. So here it'll look at the incoming JWT token, it'll crack it open, it'll say, "Oh, what kind of user are you? Which tenant are you associated with?" It'll actually look at creating the isolation policies and giving you credentials back, and we'll dig into what that looks like in more detail, but then it will essentially create an authorization policy, an authorizer policy here, that will determine which flows are allowed for you, and this is part of our overall authorization mechanism here. And through that policy, we can control a couple things here. We can say, "Hey, based on your API key and your usage plan, how much of this, how many requests can you be making? How much activity can you be generating based on your tier?" We'll dig into that, and then I can say, "Hey, based on your role, like if you're an admin, I might open more paths for you than if you were some other role in the system." So here it can actually block routes and disable routes in real time as part of your request, but soon as you get through that authorization experience and you go over to the Lambda function, which is where your microservice goes, now those credentials go over with you that were resolved as part of the authorizer, and now your app, your microservice, can use those credentials as part of your overall isolation scheme. Okay, the other piece of this is the tenant routing piece, right? Now, as part of authentication and getting in, ultimately we have to figure out which user pool to authenticate you against and which stack to send you to, because we have silo stacks and we have pool stacks. So now when we come into the app and we say, "Hey, you've come into the app and you've authenticated into the app, and I now need to go, or you're trying to authenticate into the app, I need more data to be able to figure out what to do here," and this is where that information we stored inside of tenant management. I said we would store additional configuration information in here. Well here, you'll see we've got a mapping of the tenant to the tenant name. We've got a user pool mapping to let you know which user pool to use for this environment and we've got this URL that tells us how to route your specific traffic based on the stack. So now when we have that information and that comes back, now when we wanna go authenticate you, we know which user pool to authenticate you against. So here we'll actually essentially say, "Which user pool?" Well, which user pool will depend on what kind of tenant you are. If you're a pooled tenant, I'll authenticate you against that shared user pool tenant. If you're a siloed tenant, a platinum tier tenant, you'll have a separate user pool, and I'll authenticate you against that. But ultimately, I authenticate, and back from that comes a JWT token, and now with that JWT token and that URL, I know what stack to route you to. So here I've got platinum stacks and the pooled stack. I need to know where to send that workload, and here, based on that configuration information, I can figure out how to send that. So you can see here the routing has a lot of dimensions to it, right, and it's all driven by this configuration information that's in tenant management. Okay, now we can move into the isolation piece of this, right? We're authenticated, we're onboarded. We did all those bits, but now let's move into the actual multi-tenant microservices of our environment and say, "What do we do inside those to actually ensure that these environments are isolated?" Yes, we're authorizing and authenticating, but we still need isolation to be sure a tenant, one tenant, can impact or access the resources of another tenant, and it turns out because we support these two modes, the silo and the pool mode of deployment, we actually have two distinct isolation schemes. So for the siloed environments, we will actually deploy, at deployment time, attach an IAM policy. So here you'll see I've got a Tenant 1 execution role attached to these Tenant 1 Lambda functions, and I have a Tenant 2 execution role attached to these Tenant 2 Lambda functions, and this all happens at deployment time. So here now, when I attach the policy at deployment time, that policy will say, "For the life of this function, this function can only access the resources allowed by that execution role." It's a super powerful isolation scheme because now it can only access resources that are valid for that particular tenant, and the code inside of these functions doesn't even matter. If it tries to cross those boundaries, it's not gonna be able to across the boundary, so the developers don't have to do anything to comply with it, and that's great and an awesome story for siloed environments, but we also have these pooled environments, and in a pooled environment, if you look at the Lambda function, when this Lambda function is deployed, it has to be deployed in a much wider context. It can't have a really wide, sorry, narrow execution role. It has to have an execution role that's valid for all the pooled tenants. So now in this mode, instead, we have to resolve all of your scoping and your access and your policies for isolation at runtime here, right? So here now, when the code makes a call into here on behalf of Tenant 3, we have to resolve what the policies are for Tenant 3, get those credentials, and then apply them in the code of our application. So this requires the cooperation and the use of these individual functions to be aware of the fact that they have to resolve that. Now, with libraries and other mechanisms, we'll go out and make it easier to resolve that and get that policy data, and we'll supply different mechanisms to help with that, but still, the code could go around it here in a way that it couldn't in the siloed model. Okay, so let's look at now at this deployment-based experience. What does that really look like for isolation? Well, here, the tenant comes in, tenant hits our Gateway, it hits the authorizer, and now we hit our deployed siloed function, and here you'll see we have an execution role attached, and that execution role has a very specific policy for Tenant 1 to say Tenant 1 can access this particular order table, and so now it constrains your access to just that order table. So the execution role here is at deployment time and gives us our awesome isolation story. Now let's look at what that would look like, though, in a pooled model. Now, in a pooled model, we're gonna get a request into the API Gateway. That's gonna go out to the authorizer, and now the authorizer is going to be responsible for figuring out contextually which tenant is currently calling and what are the credentials that are allowed for that particular tenant. So this authorizer will go out, will essentially use that context of that particular tenant, and now you'll see our policy is more of a template. There's a placeholder there where we will insert the tenant context, and then we will assume a role with IAM here for that new policy, and we will return the credentials that come back from that, and then those credentials will then go into our microservices down below. So here now, inside these microservices on the left-hand side, you'll see a code that actually will use these specific credentials as they go to try to access data. So all this is runtime-applied. Now say within our team, there was a lot of debate about this approach because some of the approaches we describe will say resolve these scopes within the microservices instead of at the authorizer level, but if your policies are small enough and manageable enough and you're really focused on the caching and you can put them all at the authorizer side, that's a perfectly valid approach too. I would just say if you're gonna go away and look at what isolation scheme you're gonna implement for your pooled model, really weigh those options. Is it better for me to get those creds and inject them at the authorizer side, or is it better to deploy that responsibility more to each individual microservice and let the microservice decide how it's going to resolve down to those credentials and then manage all of that at the microservice level? We've absolutely seen this done multiple ways, just this is the way we happened to implement it inside of the reference architecture, and we were able to cache policies and do some other things here and centralize this a bit more here, but then there are the downsides that all of that processing is done at the authorizer side. Okay, now, if you wanna look at what that actually looks like inside of the data access layer of our code, right? If we were to crack open the data access layer of our code and say, "What's going on here?" well, now we have code that's accessing databases or tables, and it's gotta support both silo and pooled models. So in the code, you'll see, hey, we look if this is a pooled model, well, now we know we're using dynamic isolation, so we're actually gonna go out and when we create our DynamoDB instance, right, when we create that, that instance that is going to be used to access DynamoDB, here we'll actually use the credentials that are the credentials that were acquired by the authorizer. However, if we're not using that and we're in a silo model, well, now we can rely on the execution role, and so we don't need to insert these credentials or anything else. The execution role takes care of all that for us. So here in supporting silo and pool models is another example where the code is somewhat influenced by this experience. Now, the other thing here is that you'll see that we have partitioned examples of products in here where we use instead of a silo model for the data, we use a pooled model for the data, and this is in our product table, and in this case, the shard ID of each table is actually a tenant identifier and now we're partitioning by that tenant identifier. And so here, when you look at the isolation policies, you'll actually see that the policy has this notion of a leading key that references the shard ID, and that says, "Hey, scope down to Tenant 1 or down to Tenant 2 or Tenant 3 in the policy," and we've shown this in a lot of examples we had before, so I didn't show this one. Instead, I focused on the other, but this applies both to the silo and pooled models of storage also, just different policy schemes. Now, if we actually go beyond this and we look inside the microservices, right, of our application, so now we've talked about isolation, let's go inside the actual microservices and see what multi-tenant bits are actually in there. Well, here, when I hit the Gateway, and I take a request, and that request is coming into my authorizer, yes, it's gonna extract the tenant ID and it's gonna send that tenant ID into my microservices, but now my microservices have to do things that require tenant context. Log a message with tenant context, record a metric with tenant context, access data with tenant context. Well, here, we don't want all that code in the microservices if we can help it. We want life to be as simple as it can be for our developers, so here what we did in our reference architecture is essentially move all of that logic, all that common logic, out to a set of shared code that runs in a Lambda layer, and in a Lambda layer, we can essentially say we're gonna share all this code, we're gonna deploy it and version it separately, and it will be accessible to all of our Lambda functions. So here we put logging here, so it'll do tenant-aware logging and send data out to the logs and out to CloudWatch Logs with tenant context, and we've got a metrics manager here that will send metrics data out with tenant context, and the idea is if you look at the actual code behind this, the application developer knows almost nothing about the fact that we're using tenant context here, and the nice part of layers here is that you can just keep deploying and managing these shared concepts and they'll just automatically be accessible to all of your microservices. Now, if we see it in actual action, what does that look like inside the code? So here's a get_order function, and how are these helpers looking out? Well, you'll see here's an example of me logging with tenant context. All I'm doing is calling a log message. I'm not extracting the token. I'm not pulling the tenant ID out of the JWT. I'm not doing anything else other than passing the event and passing the message, and the log message logging takes care of everything else. When I go get a record from the data access layer, there's no special tenant handling or anything else here. It just goes and gets it, and the same when I record a metric. It's just record a metric, and the whole idea here is when you look at this code, there's not all kinds of crazy multi-tenant sort of activity or policies in here that are managing this. Now, obviously, but we did a little bit of work to record these and land them inside of different mechanisms inside of AWS, and so for now, at least, in the simpler version of this, you can go over to X-Ray and actually filter by an annotation that's here, and this is where you can go see the activity that's going on in the application. This is a really lightweight example of what you could do here. We really wanna encourage people to build these really rich dashboards that surface this log and this metric data. Now, the last thing we're gonna look at here is tier-based throttling, right? We said we wanted to offer different experiences to different tiers, and yes, we're isolating differently and we're deploying differently, but we also wanna be able to say how can we just use tiers as a way of preventing one tenant from adversely affecting another? So if you see this environment, I've got a basic, a standard, a platinum, a couple of platinum tier tenants, and they're hitting the API Gateway, what I wanna be able to do is say, "Hey, basic tier tenant, you can't impact the experience of the platinum tier tenant. I'm gonna introduce throttling that will prevent that," and the way we do that is we go out to the custom authorizer. The custom authorizer then says, "Oh, I get the tenant context. I'll then map that to a tenant tier to find out what tier they are and then I'll map that to an API key, and once I have that API key," 'cause we have a separate API key for each tier, "I can then have an authorizer policy that essentially will map our API key to the usage plan, and then that usage plan will be used to process a given request." So the really cool part of this is you just make your normal request. This authorizer code goes out and figures out your tenant context and figures out your API key and then makes a request with that API key and the attached usage plan, and now you get throttling applied on a tenant-by-tenant basis. So instead of having to do that somewhere outside of this, or do something more exotic here, this is all automated for you, and now you get tier-based throttling strategies, a really powerful construct. Finally, a few takeaways here. Hopefully there's a few things that I think that are really important to remind you of as we wrap up here. Certainly, I hope it's clear that serverless and SaaS are just a natural fit for one another. I mean, EKS, ECS, they're all good fits for SaaS, they're awesome, but this nature of having no server is really powerful, and it really lets us match actual tenant activity with meant tenant consumption and it makes for a really great operational experience. You should really dig in and think about what are the actual isolation needs of your customers. What are the tiering needs as you start to look at this reference architecture? 'Cause you can see here we've got these special deployment models, we've got these tiering strategies, a whole lot of things being driven by tier here, but you have to go and figure out what are the right tiers for my environment and for my solution. Also, it should be really clear that this onboarding experience where we have this unique sort of deployment consideration, as in we're deploying separate stacks whether you're silo or pool, well, you need to really invest in making sure that's a fully automated experience, right? Here's where blurring the lines, where we're really gonna have, we have DevOps-y code that is running all the time every time our tenants are onboarding the system, and that gives us the power to scale our system and take on new tenants at a rapid pace. You saw here where we used usage plans and API keys in a really creative way with the authorizer, and I think that's a really great way to do tier-based throttling in serverless SaaS environments, and also we talked about the need for having these shared multi-tenant concepts be put into libraries and deployed into Lambda layers to simplify the experience for your developers. Do everything you can to make, sort of take the details of multi-tenancy away from your developers and move those into libraries where you can manage and configure them separately. Also, serverless SaaS is a great opportunity for you to really get great operational efficiency and agility out of your environment. You should absolutely look at creative ways for doing deployments here, like canary releases and other mechanisms now because they're a little simpler in this model, and also now you're freed up 'cause you don't have as many complexities around scaling policy and things of that nature. And obviously, overall, I'd love for you to just take the serverless SaaS reference architecture and use it as a starting point, a starting point to learn more about serverless SaaS or a starting point to start to build your own solution, and you'll see that you can actually begin to shift this to your own code quite easily. Either way, we're hoping this gives you a better sense of what it means to build serverless SaaS on top of AWS. I'd also say there's a workshop that's associated with this at re:Invent as well that can guide you through this in even more detail than we were able to cover here today. Okay, so I promised links to code at the end here. There's a link to the actual serverless SaaS reference architecture that we have and a link to the workshop that I called out here, so you can go out there, clone the code, and get going. I also wanna highlight the fact that we have more sessions going here. We have more workshops around SaaS, more chalk talks around SaaS. We actually have a business session around SaaS, if that interests you, lots of content around SaaS that can help you round out your view of the SaaS landscape, and that's it. I really appreciate you being a part of this session. I hope that you find the serverless SaaS information useful and that you can go out and start taking a peek, and I'm hoping it'll give you a head start if you're thinking about building serverless SaaS solutions on top of AWS, thanks so much. (upbeat music)

## Subtitles with Timestamps

[00:00](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=0s) (upbeat music)

[00:10](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=10s) Hey, everybody, thanks so much

[00:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=11s) for joining my session today.

[00:13](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=13s) As the slide says, my name's Tod Golding,

[00:15](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=15s) and I'm a partner solutions architect here at AWS

[00:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=19s) and I'm part of a team that's called the SaaS Factory,

[00:21](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=21s) and that team builds, delivers,

[00:23](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=23s) optimizes SaaS solutions on top of AWS,

[00:27](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=27s) and over the last few years,

[00:28](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=28s) we've been building a lot of content

[00:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=29s) around SaaS best practices of whitepapers,

[00:32](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=32s) blog posts, targeted solutions.

[00:35](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=35s) So we've shown people how to do data partitioning

[00:37](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=37s) and isolation in these pocketed solutions,

[00:41](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=41s) but we've also said we'd really like to build

[00:43](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=43s) prescriptive solutions that show people

[00:45](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=45s) an end-to-end working environment.

[00:47](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=47s) So instead of just focusing on pockets

[00:50](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=50s) of specific SaaS patterns or best practices,

[00:52](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=52s) how could we show you an entire application

[00:55](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=55s) and what the moving parts

[00:57](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=57s) of that application would look like,

[00:58](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=58s) and what would it mean for you as a developer

[01:00](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=60s) to orchestrate everything that's needed to make that work?

[01:04](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=64s) And so, to accommodate that,

[01:06](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=66s) we created, actually, two reference architectures.

[01:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=68s) One that I'm speaking on here at AWS about, EKS,

[01:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=71s) and the one we're talking about today,

[01:12](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=72s) which is serverless SaaS,

[01:15](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=75s) and the goal of this session really is

[01:16](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=76s) to dig into that serverless SaaS architecture

[01:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=79s) and really show you all the moving parts inside of it here,

[01:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=82s) so we're gonna look at how isolation, and onboarding,

[01:26](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=86s) and all of these things we talk about around SaaS

[01:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=89s) come to life in a real working SaaS application.

[01:33](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=93s) And our goal here is to expose you

[01:35](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=95s) to all the moving parts of that reference solution

[01:38](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=98s) and let you see all the sort of nuances

[01:42](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=102s) that are involved in making it all work.

[01:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=104s) Now, I really wanna highlight

[01:46](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=106s) the fact that this is a reference solution, right?

[01:49](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=109s) We've chosen some specific strategies

[01:51](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=111s) and we've picked some specific sort of approaches

[01:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=114s) to implement this specific serverless SaaS environment,

[01:58](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=118s) but you should know that there's more than one way

[02:00](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=120s) to implement serverless SaaS on top of AWS,

[02:02](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=122s) and you could see us morphing this reference solution

[02:05](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=125s) or creating new reference solutions as we go along,

[02:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=128s) but the overall hope here is

[02:09](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=129s) that you can take this reference solution,

[02:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=131s) I'll give you a link at the end, download it,

[02:14](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=134s) and either use it as the starting point

[02:16](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=136s) of a solution you might be building

[02:17](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=137s) or just use it as a way to get yourself

[02:20](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=140s) much more familiar with what's involved

[02:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=142s) in actually building a full SaaS, serverless SaaS, solution.

[02:27](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=147s) Now I will highlight the fact

[02:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=149s) that this is a 400-level session,

[02:31](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=151s) so we're not gonna be just covering

[02:33](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=153s) fundamentals of serverless SaaS,

[02:34](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=154s) and we're not gonna teach

[02:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=156s) like the basics of the architecture.

[02:39](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=159s) Our goal, really, here is to sort of get into the weeds.

[02:42](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=162s) We wanna look under the hood of this solution

[02:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=164s) and, in fact, go all the way down to the code at some point.

[02:46](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=166s) Now, we're not gonna crack open the IDE

[02:48](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=168s) or anything like that,

[02:50](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=170s) but we'll pull up some snippets of code

[02:52](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=172s) and give you a sense of what's going on under the hood,

[02:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=174s) what's really making this work,

[02:56](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=176s) and the idea is that hopefully

[02:57](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=177s) you'll take all that knowledge away,

[02:58](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=178s) and if you take that and you look at the reference solution,

[03:02](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=182s) it'll give you overall a better sense

[03:03](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=183s) of what the overall landscape looks like.

[03:07](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=187s) Now, before we dig into the actual architecture,

[03:10](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=190s) it's good to stop and ask ourselves,

[03:12](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=192s) why serverless for SaaS?

[03:14](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=194s) Why is it such a good fit?

[03:16](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=196s) And if you look generally

[03:17](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=197s) at what we're doing in SaaS environments,

[03:20](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=200s) a lot of what our effort and energy goes into

[03:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=202s) is trying to somehow anticipate tenant activity

[03:27](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=207s) and then map our consumption

[03:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=209s) of infrastructure resources to that,

[03:32](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=212s) to that, those consumption patterns,

[03:34](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=214s) and so what I did here is I've created a simple graph.

[03:37](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=217s) We've shown this before,

[03:38](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=218s) but essentially the blue line of this graph

[03:41](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=221s) represents the trends of consumption

[03:43](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=223s) inside your SaaS application,

[03:45](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=225s) and this is the realistic universe of SaaS, right?

[03:48](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=228s) Sometimes we've got these peaks and valleys of activity.

[03:51](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=231s) Sometimes we're adding new tenants

[03:52](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=232s) and the load is changing all the time,

[03:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=234s) and it gets really hard to anticipate

[03:57](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=237s) where the peaks and valleys of that activity will be

[04:00](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=240s) or how to build an infrastructure

[04:02](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=242s) that responds correctly to that,

[04:04](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=244s) but in the dream world,

[04:06](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=246s) we'd get this red line that you see here

[04:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=248s) where the infrastructure consumption of our environment

[04:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=251s) would align perfectly to the actual tenant activity,

[04:15](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=255s) 'cause that's our real goal as SaaS architects.

[04:17](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=257s) We wanna have just enough infrastructure

[04:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=259s) to support the environment that we're spinning up here,

[04:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=262s) and to me, this is the sweet spot of serverless SaaS.

[04:25](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=265s) Yes, EKS, ECS, lots of others do a good job here,

[04:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=269s) but here in serverless, we are truly without servers,

[04:31](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=271s) so we don't have to think about scaling policies

[04:34](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=274s) or what our provisioning sort of experience is.

[04:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=276s) We essentially consume what we need,

[04:39](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=279s) and we only pay for what we need.

[04:41](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=281s) The other dimension of this is that just generally

[04:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=284s) the deployment and the life cycle

[04:47](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=287s) of managing and operating these serverless SaaS environments

[04:50](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=290s) tends to be lower in this function-based model

[04:53](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=293s) where everything is serverless as well,

[04:55](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=295s) so rolling out new features, doing canary releases,

[04:59](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=299s) all those things get a lot easier to me

[05:01](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=301s) in the serverless SaaS environment,

[05:04](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=304s) and here's where we get the better agility,

[05:07](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=307s) the better efficiency that we're after operationally,

[05:10](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=310s) a lot of those good things we really wanna focus on.

[05:13](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=313s) We also tend to be able to now focus more of our time

[05:16](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=316s) and energy on the actual IP of our solution.

[05:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=319s) Now, I'm not saying that serverless means

[05:21](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=321s) that you should only use serverless for SaaS environments,

[05:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=324s) but it is a good fit,

[05:25](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=325s) and EKS is still a good fit for others.

[05:27](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=327s) ECS is still a good fit. EC2 can be a fit.

[05:30](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=330s) There's just some natural alignment here

[05:32](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=332s) that's worth highlighting.

[05:35](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=335s) The other piece of the puzzle here is

[05:37](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=337s) we really wanted to just quickly talk to you a little bit

[05:40](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=340s) about what sort of thought process

[05:42](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=342s) went into the serverless SaaS reference architecture.

[05:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=344s) What were the key architectural decisions we made,

[05:48](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=348s) and specifically which serverless architecture

[05:52](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=352s) decisions did we make?

[05:53](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=353s) And one of the really big ones here

[05:56](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=356s) was the deployment model we chose, right?

[05:58](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=358s) 'Cause we really wanted to highlight the fact

[05:59](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=359s) that in a serverless SaaS environment,

[06:02](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=362s) you really are picking, often,

[06:03](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=363s) between multiple deployment modes.

[06:05](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=365s) Can I deploy everything in a pool model

[06:07](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=367s) where tenants are sharing resources?

[06:09](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=369s) Can I deploy in a silo model

[06:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=371s) where tenants maybe have dedicated resources?

[06:13](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=373s) And what we really wanted to do here

[06:15](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=375s) was offer you a hybrid of those

[06:17](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=377s) and show what it'd mean to support

[06:18](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=378s) both of those deployment models in an environment,

[06:20](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=380s) and that had a huge ripple effect

[06:23](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=383s) through the overall architecture of our solution,

[06:25](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=385s) and you're gonna see that.

[06:27](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=387s) The other thing here is how did we automate

[06:30](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=390s) those deployments based on tiers?

[06:31](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=391s) What's all the infrastructure and code

[06:34](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=394s) that we had to put in place

[06:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=396s) to automate this complex deployment model, right?

[06:39](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=399s) We're now supporting multiple deployments,

[06:41](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=401s) and that really had a real influence

[06:43](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=403s) on the overall automation strategy

[06:46](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=406s) of our onboarding experience.

[06:48](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=408s) Now, the other piece we're gonna look at

[06:50](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=410s) is this noisy neighbor scenario.

[06:53](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=413s) Even in serverless environments,

[06:55](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=415s) there's still a potential for you

[06:57](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=417s) to have noisy neighbor conditions,

[06:59](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=419s) and so we had to think about, well,

[07:00](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=420s) what strategies would we use?

[07:02](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=422s) How would we build

[07:03](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=423s) our serverless SaaS reference architecture

[07:05](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=425s) in a way that would limit your potential

[07:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=428s) to have noisy neighbor

[07:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=428s) and manage that noisy neighbor experience on your own?

[07:13](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=433s) Now, tenant isolation is something

[07:14](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=434s) we look at in every environment,

[07:17](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=437s) and certainly there are things

[07:18](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=438s) in this reference architecture that are similar

[07:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=442s) to the other reference environments we have.

[07:23](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=443s) However, there are a handful of considerations here

[07:26](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=446s) and a handful of strategies we've used for isolation

[07:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=449s) that are unique to the serverless bit,

[07:30](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=450s) so we'll dig into what's particularly unique

[07:33](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=453s) about the serverless model

[07:34](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=454s) and how it influences your approach to isolation.

[07:38](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=458s) And then lastly, we'll look at tiers

[07:40](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=460s) and just generally how to use tiering strategies

[07:43](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=463s) to control and influence the experience of your environment.

[07:49](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=469s) Okay, enough background and history of how we got here.

[07:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=474s) Let's dig into the high-level architecture

[07:56](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=476s) of your solution, right?

[07:57](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=477s) Let's just see what the overall landscape

[08:00](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=480s) of this EKS reference architecture looks like,

[08:02](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=482s) and you're gonna see that we've, actually,

[08:04](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=484s) the solution breaks into two very distinct pieces.

[08:07](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=487s) The first piece of the puzzle

[08:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=488s) is what we call the control plane,

[08:10](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=490s) and here in the control plane

[08:12](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=492s) is where all the horizontal services live for your server,

[08:17](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=497s) for your serverless SaaS environment, right?

[08:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=499s) This is where we see registration,

[08:21](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=501s) and onboarding, and tenant provisioning,

[08:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=504s) all of these things that are needed

[08:26](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=506s) to just manage and operate your business,

[08:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=509s) and here we'll have an administrative application,

[08:31](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=511s) and that administrative application will actually be used

[08:35](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=515s) to control and interact with the control plane services,

[08:39](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=519s) so manage tenants, manage users, and so on.

[08:43](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=523s) And I should highlight the fact

[08:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=524s) that this control plane is fundamental

[08:46](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=526s) to building a really good SaaS environment.

[08:48](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=528s) You'll see it across all the SaaS solutions we build,

[08:51](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=531s) and we very much encourage organizations.

[08:53](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=533s) Hey, if you're really trying to get innovation

[08:55](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=535s) and agility out of your SaaS environment,

[08:57](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=537s) pour a lot of energy

[08:58](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=538s) into building a really good control plane

[09:00](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=540s) because it's the single pane of glass that manages

[09:04](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=544s) and operates everything about your SaaS environment.

[09:07](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=547s) Now, it's interesting to note that the control plane

[09:09](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=549s) actually doesn't have multi-tenant code in it, right?

[09:12](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=552s) There's no multi-tenancy over there.

[09:14](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=554s) These are just services

[09:15](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=555s) that are managing your multi-tenant environment.

[09:18](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=558s) Where the multi-tenancy really shows up

[09:20](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=560s) is over in what we'd call

[09:21](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=561s) the application plane of your environment,

[09:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=564s) and this is where the application lives.

[09:26](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=566s) This is where you'll see that we have

[09:27](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=567s) basically a classic sort of serverless web application here.

[09:32](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=572s) We have an S3 bucket, an API Gateway,

[09:35](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=575s) and a set of microservices,

[09:37](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=577s) and those are all being accessed

[09:39](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=579s) by some sample SaaS application that we have,

[09:42](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=582s) and on the surface this looks

[09:43](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=583s) just like any other application,

[09:45](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=585s) but what we're gonna find is when we dig

[09:47](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=587s) into the weeds of this application,

[09:49](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=589s) you're gonna see where data partitioning

[09:51](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=591s) and isolation and routing show up at the API Gateway.

[09:55](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=595s) They show up inside of our microservices,

[09:57](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=597s) so there's lots more moving parts to SaaS

[09:59](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=599s) inside this application plane

[10:00](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=600s) that just aren't here at this level.

[10:03](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=603s) But overall, this is the landscape

[10:05](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=605s) of what we're going to run and build

[10:07](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=607s) as part of this environment

[10:09](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=609s) and ultimately the high-level view

[10:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=611s) of what you get in the box

[10:13](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=613s) with the serverless SaaS solution.

[10:16](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=616s) So now let's dig into the control plane part itself first.

[10:20](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=620s) Let's start there and look at what happens

[10:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=622s) when you actually provision the control plane,

[10:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=624s) because I showed you

[10:25](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=625s) this high-level view of the control plane,

[10:27](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=627s) but the reality is there are a lot more moving parts

[10:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=629s) to that control plane and a lot of automation

[10:31](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=631s) that happens behind the scenes to bring to life

[10:34](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=634s) all the moving parts of that control plane.

[10:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=636s) So when you look inside the serverless SaaS solution,

[10:39](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=639s) you're gonna see that we have

[10:40](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=640s) this bootstrap template in the repo.

[10:43](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=643s) You'll see it there,

[10:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=644s) and this bootstrap template is responsible

[10:47](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=647s) for spinning up the whole environment

[10:48](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=648s) that is the baseline environment of this solution

[10:51](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=651s) before any tenants are introduced.

[10:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=654s) So I wanna walk you through a little bit

[10:55](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=655s) of the moving parts here of the template

[10:58](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=658s) that's a part of this bootstrap template

[11:00](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=660s) and the components of it, and if you look at these,

[11:02](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=662s) you'll see these correlate

[11:03](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=663s) straight to the template code that's inside the repo.

[11:07](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=667s) So there's this create tables step

[11:09](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=669s) where we'll create all of these different tables

[11:12](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=672s) that are needed to manage state

[11:13](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=673s) and information about our environment.

[11:16](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=676s) You'll see we have a tenant user mapping table,

[11:18](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=678s) and we'll get into the details of what that involves,

[11:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=679s) but essentially how we're gonna map user pools, and so on,

[11:23](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=683s) the tenant details table,

[11:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=684s) where we actually store all the details

[11:26](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=686s) and configuration of the tenant,

[11:27](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=687s) and this tenant stack mapping table,

[11:30](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=690s) which plays a key role

[11:32](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=692s) in supporting this silo and pool model.

[11:34](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=694s) So we'll poke at all those tables.

[11:37](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=697s) You also see that we create user pools here

[11:39](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=699s) as part of this template.

[11:41](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=701s) So you'll see that we create

[11:43](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=703s) a pooled user pool from the beginning,

[11:46](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=706s) and that pooled user pool is really meant to represent

[11:50](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=710s) all those users that are gonna be our pooled model.

[11:52](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=712s) They're gonna share one user pool for all of them.

[11:56](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=716s) And then we also create a user pool for our admin users,

[11:59](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=719s) and here the admin users

[12:01](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=721s) are the SaaS providers themselves, right?

[12:03](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=723s) This is where your admin application authenticates,

[12:05](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=725s) so we know we're gonna need those two as a baseline

[12:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=728s) so we provision them at the start

[12:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=731s) and then we have to provision

[12:12](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=732s) the actual microservices, right?

[12:14](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=734s) Before, I showed you in that control plane

[12:16](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=736s) we had user management, tenant management.

[12:18](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=738s) This is where we provision and configure

[12:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=739s) all of those microservices.

[12:21](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=741s) Now, these are Lambda functions,

[12:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=742s) but they're Lambda functions in what I would call

[12:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=744s) a logical or a composite sort of microservice

[12:28](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=748s) where multiple functions are part of one microservice.

[12:30](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=750s) So tenant management is composed

[12:33](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=753s) from multiple Lambda functions.

[12:37](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=757s) You'll also see that we set up the API Gateway here,

[12:39](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=759s) so it's not just a matter of provisioning the Gateway.

[12:40](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=760s) It's a matter of provisioning and configuring the Gateway

[12:43](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=763s) for all the routes and the permissions and everything else

[12:45](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=765s) that have to get set up for this to work.

[12:47](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=767s) And then we'll set up the actual web applications,

[12:50](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=770s) and there's three applications

[12:52](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=772s) that are part of this overall experience.

[12:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=774s) There is an admin application that we talked about

[12:56](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=776s) that is the SaaS provider experience.

[12:59](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=779s) There's a SaaS e-commerce-y kind of app,

[13:01](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=781s) a really lightweight e-commerce app

[13:03](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=783s) just to show what your SaaS application would look like,

[13:06](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=786s) and then there's a landing page.

[13:07](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=787s) There's landing pages

[13:09](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=789s) for self-service sign-up into your solution.

[13:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=791s) And so for each of these,

[13:12](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=792s) we have to provision the usual constructs

[13:15](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=795s) that are needed for an application,

[13:17](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=797s) a web application in a serverless model.

[13:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=799s) So we'll set up the S3 buckets,

[13:20](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=800s) we'll set up the CloudFront bits to host those applications,

[13:25](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=805s) and then the last piece are these custom resources,

[13:27](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=807s) and these custom resources are really just,

[13:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=809s) if you're familiar with CloudFormation,

[13:31](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=811s) these are custom resources in CloudFormation

[13:33](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=813s) that include the custom code we need

[13:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=816s) to trigger certain onboarding events.

[13:39](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=819s) So, for example, there's a settings table

[13:41](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=821s) and there's a tenant stack map

[13:43](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=823s) that are part of our provisioning experience,

[13:46](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=826s) and those tables are run from CloudFormation templates,

[13:49](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=829s) and therefore they need these custom resources

[13:53](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=833s) to make all that work.

[13:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=834s) But anyway, this is all the high-level view

[13:58](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=838s) of all the pieces that get created

[13:59](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=839s) when you run this bootstrap template,

[14:02](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=842s) and obviously now, if you poke into the code,

[14:04](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=844s) you should see a pretty good correlation between what's here

[14:07](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=847s) and what's actually in that template file.

[14:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=851s) Okay, now, before we go deeper into the architecture,

[14:14](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=854s) I wanna make it really clear,

[14:15](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=855s) and I kind of talked about the need

[14:17](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=857s) for different deployment models,

[14:18](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=858s) but I really wanna make it clear

[14:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=859s) that there are two very distinct deployment models

[14:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=862s) for this reference architecture,

[14:25](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=865s) and we intentionally are trying to show this off.

[14:28](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=868s) We've talked an awful lot about the fact

[14:30](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=870s) that some SaaS environments aren't just pool,

[14:33](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=873s) where resources are shared for tenants, or silo.

[14:35](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=875s) Those two don't have to be mutually exclusive,

[14:39](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=879s) and so in this environment,

[14:40](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=880s) we wanted to do what we often tell our customers to do,

[14:42](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=882s) which is sometimes you have to support both,

[14:45](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=885s) which is some tenants are in the silo model

[14:47](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=887s) and they have dedicated infrastructure

[14:49](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=889s) and some of your tenants will be in the pooled model,

[14:51](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=891s) and you'll use tiering to separate those experiences.

[14:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=894s) So at a conceptual level, we'll have onboarding,

[14:57](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=897s) and now as each tenant onboards, in this case,

[15:00](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=900s) a platinum tier tenant onboards, because it's platinum tier,

[15:04](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=904s) we'll actually provision a silo for that tenant

[15:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=908s) because they get dedicated resources here

[15:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=911s) and we'll provision a silo

[15:13](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=913s) for the next tenant that onboards.

[15:16](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=916s) However, the other tiers in our environment,

[15:18](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=918s) when they're signing up and onboarding into our experience,

[15:20](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=920s) so premium, standard, basic, and so on, when they come in,

[15:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=924s) they are going to go into our pooled infrastructure.

[15:27](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=927s) So here we won't provision new infrastructure for them.

[15:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=929s) We'll just configure for them

[15:32](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=932s) the bits that help them consume the pooled resources

[15:35](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=935s) that are part of the environment,

[15:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=936s) and to me, this whole experience

[15:38](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=938s) of supporting silo and pool side by side

[15:41](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=941s) is one of the more exciting bits

[15:42](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=942s) of the serverless SaaS environment.

[15:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=944s) I wanna see this, in fact,

[15:45](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=945s) show up in more of our reference architectures,

[15:47](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=947s) because I think seeing all the moving parts of this

[15:50](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=950s) and seeing how this influences the whole architecture

[15:53](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=953s) is pretty eye-opening and, I think,

[15:55](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=955s) pretty useful to a lot of organizations

[15:57](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=957s) that need to support this model.

[16:01](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=961s) Okay, so now we've seen that environment

[16:03](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=963s) and we've seen we have these different deployment models.

[16:06](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=966s) Let's look at what it means

[16:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=968s) to register a new tenant through the control plane.

[16:10](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=970s) So when we come into the control plane,

[16:13](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=973s) we can come in one of two ways to register a new tenant.

[16:16](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=976s) We can come in through the landing page and say,

[16:18](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=978s) "Hey, this is a self-service sign up.

[16:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=979s) I'll sign up, I'll provide you my information,

[16:21](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=981s) my plan, et cetera, and I will sign up,"

[16:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=984s) or you can come through the admin console

[16:27](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=987s) and you can actually trigger an onboarding

[16:28](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=988s) by filling that out, information out through that,

[16:30](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=990s) and we provided that experience through two different paths

[16:34](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=994s) because we wanna acknowledge

[16:35](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=995s) the reality that some organizations

[16:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=996s) will have self-service, some will not.

[16:38](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=998s) Some will trigger that

[16:39](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=999s) only through internally-driven processes,

[16:42](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1002s) but the reality is whether it's self-service or not,

[16:46](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1006s) it's all gonna come through one registration experience.

[16:48](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1008s) So the code behind it,

[16:49](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1009s) all the microservices that orchestrate it all,

[16:52](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1012s) are all the same, and in fact,

[16:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1014s) this registration or onboarding flow

[16:56](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1016s) is common to almost all of our architectures.

[16:58](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1018s) It just varies a little bit

[16:59](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1019s) depending upon some of the choices that you make.

[17:02](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1022s) So here registration will essentially orchestrate

[17:05](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1025s) all of the onboarding experience.

[17:07](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1027s) So here, when I say I wanna register a new tenant,

[17:10](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1030s) we'll go out and create a new user in the user pool,

[17:13](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1033s) in this case, Cognito.

[17:15](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1035s) Now, interestingly, because we're showing,

[17:18](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1038s) supporting both silo and pool models,

[17:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1042s) we actually have some conditional bits here, right?

[17:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1044s) If you're coming in as a silo user,

[17:26](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1046s) we're actually gonna give you your own user pool.

[17:28](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1048s) However, if you're coming in as a pooled user

[17:30](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1050s) in one of those tiers,

[17:31](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1051s) we're gonna share the user pool amongst the tenants,

[17:34](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1054s) and there's some orchestration

[17:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1056s) that has to happen there and some configuration

[17:38](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1058s) that has to happen there to support that.

[17:40](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1060s) And then, of course, we're actually gonna create

[17:41](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1061s) that first user that signed up, that tenant admin user,

[17:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1064s) as part of this experience.

[17:45](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1065s) Now, as part of this also, you're gonna see

[17:47](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1067s) that we also configure custom claims in Cognito

[17:51](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1071s) to identify the binding

[17:52](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1072s) between the user and the tenant,

[17:53](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1073s) and so later, when we look at authentication,

[17:56](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1076s) you'll see how the tokens that come out of that experience

[17:59](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1079s) return us a token that is enriched

[18:00](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1080s) with both tenant information and user information.

[18:04](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1084s) And we also have to create a tenant here,

[18:06](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1086s) so we'll essentially call that service,

[18:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1088s) and this is where, yes, we'll create the tenant

[18:10](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1090s) with their identifier and their plan,

[18:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1091s) but we're also gonna store lots of configuration information

[18:14](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1094s) in here about this tenant,

[18:15](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1095s) and you'll see how that configuration information

[18:17](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1097s) actually is used during authentication

[18:20](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1100s) and other parts of this experience.

[18:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1104s) And then the last piece is this provisionings piece,

[18:26](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1106s) and this is the piece

[18:27](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1107s) that lots of people will overlook, right?

[18:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1109s) They'll think, "Well, we're only pooled,

[18:31](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1111s) so we don't need it," but now in this model

[18:33](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1113s) where we're supporting both pool and silo models,

[18:38](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1118s) a lot of effort and energy

[18:39](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1119s) goes into this tenant provisioning experience,

[18:41](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1121s) because if you're silo, I actually have to provision

[18:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1124s) separate infrastructure for you as a tenant.

[18:47](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1127s) But ultimately, when this is done, right,

[18:48](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1128s) when I've created the user, created the tenant,

[18:50](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1130s) and the registration is done, everything is done,

[18:52](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1132s) a tenant is now in the system

[18:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1134s) and ready to be activated and used,

[18:57](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1137s) and that tenant can essentially come and log in

[18:59](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1139s) and begin to use the service,

[19:01](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1141s) and getting all of this orchestrated and frictionless

[19:04](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1144s) is essential to building a SaaS environment that can scale.

[19:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1148s) Now, if we look at tier-driven onboarding

[19:10](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1150s) and what that actually looks like,

[19:12](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1152s) so imagine we have this environment.

[19:14](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1154s) We've provisioned this baseline environment.

[19:16](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1156s) We've created this pool environment

[19:18](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1158s) 'cause we know we need to pool

[19:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1159s) from the beginning, so it's there,

[19:21](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1161s) and we've onboarded a couple of tenants to that,

[19:23](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1163s) into that pooled environment.

[19:25](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1165s) Now, when we add a new tenant here,

[19:28](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1168s) that provisioning experience

[19:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1169s) will simply configure a new tenant

[19:32](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1172s) and add them to the pool experience.

[19:34](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1174s) Now, I could also have a siloed tenant here.

[19:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1176s) This tenant's running.

[19:38](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1178s) It's got dedicated resources

[19:40](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1180s) and has been provisioned in a dedicated environment,

[19:43](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1183s) and one nuance here that sometimes gets lost on people

[19:46](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1186s) is that sometimes people will say,

[19:47](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1187s) "Why do you need to have siloed environments

[19:50](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1190s) in a Lambda environment?

[19:52](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1192s) Because every time I execute a function,

[19:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1194s) I'm only executing it on behalf of a single tenant

[19:57](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1197s) at a moment in time."

[19:58](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1198s) However, when you get into the details here,

[20:00](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1200s) and you'll see this as we go further on,

[20:02](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1202s) it actually affects the isolation story

[20:04](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1204s) 'cause I can implement a different isolation story

[20:06](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1206s) if I know those functions are dedicated,

[20:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1208s) and it starts affecting noisy neighbor and other conditions

[20:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1211s) in terms of concurrency and other factors.

[20:13](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1213s) So even though Lambda's only executed

[20:16](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1216s) at a moment in time for a tenant,

[20:18](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1218s) there's still value in siloing it off

[20:20](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1220s) and offering it separately,

[20:21](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1221s) and customers may just demand that anyway,

[20:23](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1223s) even if they were 100% equivalent.

[20:27](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1227s) So now when we onboard another tenant,

[20:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1229s) now you'll see we fire off, this is a siloed tenant,

[20:32](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1232s) we fire off the CodePipeline.

[20:33](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1233s) It provisions all the bits

[20:35](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1235s) and adds it to our environment.

[20:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1236s) So this is very high level.

[20:38](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1238s) Obviously I'm showing microservices

[20:40](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1240s) as the core of the provisioning.

[20:41](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1241s) There's more pieces getting provisioned

[20:43](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1243s) as part of this experience,

[20:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1244s) but that's conceptually what's going on.

[20:47](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1247s) So let's look inside that provisioning experience

[20:50](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1250s) a little bit and see what's going on.

[20:52](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1252s) If you go look at that bootstrap template

[20:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1254s) that we talked about at the beginning,

[20:55](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1255s) one of the things it does is it calls this custom resource,

[20:58](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1258s) the update tenant stack table resource,

[21:02](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1262s) and it's essentially saying, "Hey, when I first build

[21:05](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1265s) this environment and I first spin it up,

[21:06](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1266s) I need a pooled environment,

[21:09](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1269s) and so what I'm gonna do

[21:10](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1270s) is I'm gonna call this custom resource."

[21:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1271s) This custom resource will essentially go put an entry

[21:14](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1274s) into a DynamoDB table,

[21:16](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1276s) and that DynamoDB table will say,

[21:18](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1278s) "Hey, I need to create a new stack.

[21:20](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1280s) It's a pooled stack, and I need to go get it created

[21:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1282s) and provisioned for this baseline environment."

[21:25](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1285s) Then a pipeline will essentially pick that up.

[21:28](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1288s) Pipeline will say, "Hey,

[21:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1289s) there's a new environment needs to be created,"

[21:31](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1291s) and then it'll go to this tenant template

[21:33](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1293s) and that tenant template will then provision everything,

[21:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1296s) and we'll look at that tenant template there

[21:38](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1298s) in a little more detail,

[21:39](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1299s) but it will essentially provision everything

[21:41](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1301s) that's needed for the pool,

[21:42](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1302s) and now we're ready to start accepting pooled customers.

[21:46](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1306s) But what I thought was really cool

[21:48](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1308s) about the solution here that the team built

[21:50](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1310s) is that now we use this exact same process

[21:53](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1313s) when we onboard a siloed tenant.

[21:55](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1315s) So now if a siloed tenant comes along

[21:57](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1317s) and they wanna add the infrastructure for the tenant,

[21:59](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1319s) we don't create an entirely separate process.

[22:02](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1322s) Instead, we essentially put a row into this table

[22:05](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1325s) and that table says, "Hey, a new siloed tenant

[22:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1328s) needs to be onboarded,"

[22:10](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1330s) and the CodePipeline picks that up,

[22:13](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1333s) and then it goes over to the tenant table

[22:15](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1335s) and it creates the siloed stack.

[22:17](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1337s) And so if I add more tenants

[22:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1339s) through this process that are siloed,

[22:20](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1340s) it would just continue to put entries in the table

[22:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1342s) and continue to add siloed tenants, and to me,

[22:25](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1345s) the reuse of this and the fact

[22:27](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1347s) that this is a common mechanism

[22:28](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1348s) means that I can essentially change

[22:30](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1350s) what gets provisioned and the plumbing

[22:32](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1352s) of that whole end-to-end experience still works fine.

[22:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1356s) So let's look now inside of what actually happens

[22:38](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1358s) when we're creating that tenant stack.

[22:41](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1361s) So we talked about that last template in that process.

[22:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1364s) Well, what does it actually do

[22:45](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1365s) to provision our tenant environments?

[22:47](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1367s) Well, first of all,

[22:48](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1368s) it creates the product and order tables, right?

[22:50](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1370s) We need to have these two product and order microservices

[22:53](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1373s) and it needs to create a table for each of those,

[22:55](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1375s) and then it also needs to actually deploy our microservices.

[22:59](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1379s) So here we've got a product and an order microservice.

[23:02](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1382s) It configures and sets up the functions

[23:05](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1385s) for all of those bits

[23:06](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1386s) and then it sets up the API Gateway

[23:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1388s) as the entry point to these microservices,

[23:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1391s) and then the last bit is

[23:12](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1392s) it configures the permissions and so on.

[23:14](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1394s) So if you go to poke into that stack and look inside of it,

[23:18](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1398s) you'll see that these are

[23:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1399s) the basic parts it's orchestrating,

[23:20](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1400s) and you can see that they're shared

[23:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1402s) between pooled and silo,

[23:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1404s) and to me, this is also awesome that it's all shared

[23:26](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1406s) because even though we're gonna allow

[23:28](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1408s) pool and silo to have different stacks,

[23:31](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1411s) we're not gonna allow them

[23:32](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1412s) to run different versions of the code.

[23:33](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1413s) We don't want one-off infrastructure for them,

[23:35](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1415s) so having this be all one process is particularly powerful.

[23:41](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1421s) Now, the other piece of this

[23:42](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1422s) that gets lost in the shuffle is, yes,

[23:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1424s) we can onboard a tenant.

[23:45](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1425s) We can get them into the system

[23:47](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1427s) and we provision all their infrastructure,

[23:49](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1429s) but what happens when we need to roll out an update?

[23:52](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1432s) Like we wanna update a new version of the order service

[23:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1434s) so we wanna roll out some new features or functionality,

[23:56](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1436s) and now we have these different stacks that are running.

[23:59](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1439s) Well, this is where we introduced a table, and I don't know,

[24:01](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1441s) there's lots of ways to implement this mechanism,

[24:03](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1443s) but we used a table to capture and describe

[24:06](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1446s) which stacks were out there.

[24:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1448s) So you see here we have this TenantStackMapping.

[24:10](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1450s) I talked at the beginning how this table gets provisioned,

[24:12](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1452s) and this is the table that keeps track

[24:14](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1454s) of all the different stacks that have been created,

[24:16](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1456s) and you'll see the first two rows

[24:18](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1458s) are actually two siloed tenants.

[24:20](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1460s) So they have their tenant ID there,

[24:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1462s) and then we have a third one we called pooled.

[24:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1464s) We named it pooled 'cause it made it easier.

[24:26](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1466s) This is that pooled one

[24:27](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1467s) that got created at the beginning in the baseline.

[24:30](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1470s) And then you'll see we have an applyLatest column here,

[24:33](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1473s) and this is actually used to figure out

[24:34](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1474s) who's actually gonna get the latest code deployed to them,

[24:37](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1477s) and this is where we can actually do canary releases.

[24:40](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1480s) This isn't about keeping somebody off the latest version.

[24:43](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1483s) It's about saying, "Hey, we're deploying,

[24:45](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1485s) and let's just deploy to these particular tenants first

[24:48](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1488s) and then we'll deploy to the rest."

[24:50](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1490s) So it's kind of a clever way

[24:52](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1492s) we've introduced here just to manage that.

[24:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1494s) And then the rest is just the CodeCommit

[24:56](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1496s) and the stack names and so on.

[24:58](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1498s) So this table, essentially, now,

[25:00](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1500s) when we deploy a new feature and we hit the source

[25:03](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1503s) and the build and the deploy process,

[25:05](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1505s) that deploy process can look at that table and say,

[25:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1508s) "Who do I have to deploy to?

[25:10](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1510s) Oh, well, I've gotta deploy to pooled,

[25:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1511s) 'cause I know I have a stack for that,

[25:12](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1512s) and then I have two silos that I have to deploy to."

[25:16](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1516s) So to me, this is the overlooked piece of the puzzle, right?

[25:18](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1518s) Everybody focuses on the provisioning

[25:20](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1520s) and the initial provisioning,

[25:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1522s) but you also have to focus on the deployment.

[25:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1524s) Once these environments are out there and they're separate,

[25:26](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1526s) how can we automate and track that deployment as well?

[25:31](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1531s) Now, if you look at how we actually do this in the code

[25:35](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1535s) and how we apply this

[25:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1536s) and where tiering shows up inside the code,

[25:39](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1539s) I did wanna grab a couple of snippets of code

[25:40](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1540s) just to show you bits here.

[25:42](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1542s) So this is the register_tenant bit,

[25:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1544s) and you'll see here when we're registering a tenant,

[25:47](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1547s) we look at the different tiers, and in this case,

[25:49](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1549s) we're assigning a different API key, right?

[25:52](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1552s) So it could have been any sort of attribute.

[25:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1554s) I just wanna show you that, hey, as we're in the code,

[25:56](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1556s) we're actually doing these tier-based activities

[25:58](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1558s) during the creation of a tenant,

[26:00](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1560s) and you'll see how we use these API keys later.

[26:05](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1565s) And then later on,

[26:06](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1566s) you'll see that we essentially go

[26:07](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1567s) fill in all those attributes

[26:09](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1569s) that we get back from setting up the user pool

[26:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1571s) and all those other bits that are configured,

[26:13](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1573s) and we essentially persist that information about the tenant

[26:18](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1578s) by calling the tenant management service

[26:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1579s) with all those different attributes.

[26:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1582s) So you can see tier laced into this,

[26:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1584s) and then you can see how we're capturing

[26:26](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1586s) all this configuration data and storing it in the tenant,

[26:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1589s) and then later on we'll come back and reference it.

[26:32](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1592s) Okay, now one of the key parts of this is

[26:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1596s) during the provisioning process,

[26:38](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1598s) how do I actually trigger that pipeline

[26:40](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1600s) to onboard a new tenant?

[26:42](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1602s) So if I'm inside my code

[26:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1604s) and I'm looking at where in the code in this process,

[26:47](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1607s) well, if you go look at the provision_tenant function here

[26:50](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1610s) and you look at inside the details here,

[26:52](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1612s) you'll see where we're actually inserting

[26:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1614s) an item into that table.

[26:55](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1615s) So when we put an entry into that stack mapping table,

[26:59](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1619s) then we can actually go

[27:00](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1620s) and then trigger the pipeline from our code,

[27:03](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1623s) and that will make that overall process work.

[27:06](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1626s) So if you're hunting for that,

[27:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1628s) this lands in this particular function here,

[27:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1631s) and you can see how essentially all we're doing

[27:13](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1633s) is just inserting a row and kicking off the pipeline.

[27:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1639s) Now, another part of the control plane

[27:21](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1641s) that's a more simple version of this

[27:23](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1643s) if we move away from provisioning

[27:25](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1645s) is this management of tenants and users, right?

[27:28](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1648s) We still have to have some way

[27:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1649s) to manage the life cycle of individual tenants.

[27:32](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1652s) Are they enabled, disabled?

[27:35](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1655s) How do we edit their state?

[27:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1656s) How do we edit information about their policies, and so on?

[27:39](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1659s) And we also have the need to manage users.

[27:41](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1661s) We have both to manage tenant users and admin users,

[27:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1664s) and these are just additional services

[27:47](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1667s) that are inside the control plane.

[27:49](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1669s) So here you'll see you have an admin console.

[27:51](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1671s) That admin console will hit the tenant management service,

[27:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1674s) and this is where we'll update the state

[27:55](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1675s) of the tenant through that experience,

[27:59](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1679s) but also through the admin console,

[28:01](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1681s) I can hit the user management service

[28:02](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1682s) and I can update and add users to the admin console,

[28:06](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1686s) traditional sort of user management here.

[28:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1688s) And, of course, our SaaS application

[28:10](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1690s) also has to manage tenant users

[28:12](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1692s) and be able to add new users as part of their experience,

[28:15](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1695s) and that happens through the SaaS application.

[28:17](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1697s) Now here, you'll see we've shared user management.

[28:20](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1700s) You could easily have pulled these apart

[28:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1702s) and have a separate admin user management,

[28:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1704s) but the code mostly was similar for these two,

[28:26](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1706s) so we shared that as one service,

[28:28](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1708s) and then they're just managing that state inside of Cognito.

[28:33](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1713s) Now, if we look at the code

[28:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1716s) behind creating a user and creating a tenant,

[28:37](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1717s) really straightforward code.

[28:39](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1719s) The really interesting thing is

[28:41](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1721s) when you look at this create_user piece,

[28:43](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1723s) you'll see a line of code near the bottom

[28:45](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1725s) where we're actually setting the tenant ID

[28:48](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1728s) into the attributes of the tenant.

[28:50](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1730s) So here we're basically, yes,

[28:53](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1733s) we're populating the attributes of the user

[28:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1734s) when we're creating the user,

[28:56](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1736s) but we're also filling in tenant context as part of that

[28:59](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1739s) so when the tenant gets persisted into Cognito,

[29:02](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1742s) we'll have that extra bit of data,

[29:04](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1744s) and then when we go to create the tenant,

[29:06](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1746s) we're really just filling out

[29:07](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1747s) all these different attributes that we need,

[29:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1748s) all this different configuration bits

[29:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1751s) and persisting that data,

[29:12](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1752s) and we'll look at what some of that data

[29:14](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1754s) is that lands there,

[29:15](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1755s) but really, really basic operations code,

[29:17](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1757s) so not very complex here.

[29:20](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1760s) Okay, so now we have the ability

[29:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1762s) to introduce a tenant into our environment.

[29:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1764s) We have all that onboarding bits,

[29:26](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1766s) all that provisioning goodness that we talked about.

[29:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1769s) Now how do we actually authenticate a user

[29:31](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1771s) and authorize their access to the resources

[29:34](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1774s) that are part of our application?

[29:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1776s) So here, when we come into this experience,

[29:37](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1777s) we'll have a tenant come in.

[29:39](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1779s) They'll hit our SaaS application

[29:40](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1780s) and that SaaS application will actually redirect them

[29:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1784s) to a hosted UI that Cognito provides.

[29:46](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1786s) So Cognito provides this ability

[29:48](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1788s) to basically offer you a login experience.

[29:50](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1790s) We've used that in this solution.

[29:52](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1792s) We redirect that hosted UI.

[29:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1794s) You now log in through that experience.

[29:56](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1796s) You authenticate as that user that we created before,

[30:00](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1800s) and back from that comes

[30:01](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1801s) that JWT token that we talked about,

[30:03](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1803s) and that JWT token has this user and tenant context in it,

[30:07](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1807s) and now we pass that JWT token along to the API Gateway

[30:12](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1812s) and downstream to the services

[30:15](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1815s) that are part of our application.

[30:16](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1816s) So here we come into the API Gateway,

[30:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1819s) and the first thing we do inside the API Gateway

[30:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1822s) is the authorizer actually wants to look

[30:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1824s) at who's making the request

[30:27](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1827s) and apply some authorization sort of policies here.

[30:30](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1830s) So here it'll look at the incoming JWT token,

[30:33](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1833s) it'll crack it open, it'll say,

[30:34](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1834s) "Oh, what kind of user are you?

[30:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1836s) Which tenant are you associated with?"

[30:38](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1838s) It'll actually look at creating the isolation policies

[30:41](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1841s) and giving you credentials back,

[30:43](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1843s) and we'll dig into what that looks like in more detail,

[30:46](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1846s) but then it will essentially create an authorization policy,

[30:50](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1850s) an authorizer policy here,

[30:52](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1852s) that will determine which flows are allowed for you,

[30:55](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1855s) and this is part of our

[30:57](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1857s) overall authorization mechanism here.

[30:59](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1859s) And through that policy,

[31:01](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1861s) we can control a couple things here.

[31:03](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1863s) We can say, "Hey, based on your API key and your usage plan,

[31:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1868s) how much of this, how many requests can you be making?

[31:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1871s) How much activity can you be generating

[31:13](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1873s) based on your tier?"

[31:14](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1874s) We'll dig into that, and then I can say,

[31:16](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1876s) "Hey, based on your role, like if you're an admin,

[31:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1879s) I might open more paths for you

[31:20](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1880s) than if you were some other role in the system."

[31:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1882s) So here it can actually block routes

[31:25](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1885s) and disable routes in real time as part of your request,

[31:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1889s) but soon as you get through that authorization experience

[31:32](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1892s) and you go over to the Lambda function,

[31:34](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1894s) which is where your microservice goes,

[31:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1896s) now those credentials go over with you

[31:39](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1899s) that were resolved as part of the authorizer,

[31:41](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1901s) and now your app, your microservice,

[31:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1904s) can use those credentials

[31:45](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1905s) as part of your overall isolation scheme.

[31:50](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1910s) Okay, the other piece of this

[31:52](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1912s) is the tenant routing piece, right?

[31:53](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1913s) Now, as part of authentication and getting in,

[31:56](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1916s) ultimately we have to figure out

[31:58](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1918s) which user pool to authenticate you against

[32:01](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1921s) and which stack to send you to,

[32:03](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1923s) because we have silo stacks and we have pool stacks.

[32:06](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1926s) So now when we come into the app and we say,

[32:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1928s) "Hey, you've come into the app

[32:09](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1929s) and you've authenticated into the app,

[32:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1931s) and I now need to go,

[32:12](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1932s) or you're trying to authenticate into the app,

[32:15](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1935s) I need more data to be able to figure out what to do here,"

[32:17](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1937s) and this is where that information we stored

[32:20](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1940s) inside of tenant management.

[32:21](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1941s) I said we would store

[32:23](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1943s) additional configuration information in here.

[32:26](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1946s) Well here, you'll see we've got a mapping

[32:27](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1947s) of the tenant to the tenant name.

[32:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1949s) We've got a user pool mapping to let you know

[32:31](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1951s) which user pool to use for this environment

[32:33](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1953s) and we've got this URL that tells us

[32:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1956s) how to route your specific traffic based on the stack.

[32:39](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1959s) So now when we have that information and that comes back,

[32:42](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1962s) now when we wanna go authenticate you,

[32:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1964s) we know which user pool to authenticate you against.

[32:47](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1967s) So here we'll actually essentially say, "Which user pool?"

[32:51](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1971s) Well, which user pool will depend

[32:52](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1972s) on what kind of tenant you are.

[32:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1974s) If you're a pooled tenant,

[32:55](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1975s) I'll authenticate you against that shared user pool tenant.

[32:58](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1978s) If you're a siloed tenant, a platinum tier tenant,

[33:01](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1981s) you'll have a separate user pool,

[33:02](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1982s) and I'll authenticate you against that.

[33:05](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1985s) But ultimately, I authenticate,

[33:07](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1987s) and back from that comes a JWT token,

[33:09](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1989s) and now with that JWT token and that URL,

[33:14](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1994s) I know what stack to route you to.

[33:17](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=1997s) So here I've got platinum stacks and the pooled stack.

[33:20](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2000s) I need to know where to send that workload,

[33:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2002s) and here, based on that configuration information,

[33:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2004s) I can figure out how to send that.

[33:26](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2006s) So you can see here

[33:27](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2007s) the routing has a lot of dimensions to it, right,

[33:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2009s) and it's all driven by this configuration information

[33:32](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2012s) that's in tenant management.

[33:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2016s) Okay, now we can move

[33:37](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2017s) into the isolation piece of this, right?

[33:39](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2019s) We're authenticated, we're onboarded.

[33:42](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2022s) We did all those bits, but now let's move

[33:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2024s) into the actual multi-tenant microservices

[33:46](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2026s) of our environment and say,

[33:47](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2027s) "What do we do inside those to actually ensure

[33:50](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2030s) that these environments are isolated?"

[33:52](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2032s) Yes, we're authorizing and authenticating,

[33:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2034s) but we still need isolation to be sure a tenant, one tenant,

[33:57](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2037s) can impact or access the resources of another tenant,

[34:02](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2042s) and it turns out because we support these two modes,

[34:04](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2044s) the silo and the pool mode of deployment,

[34:06](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2046s) we actually have two distinct isolation schemes.

[34:10](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2050s) So for the siloed environments,

[34:12](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2052s) we will actually deploy, at deployment time,

[34:15](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2055s) attach an IAM policy.

[34:18](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2058s) So here you'll see I've got a Tenant 1 execution role

[34:21](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2061s) attached to these Tenant 1 Lambda functions,

[34:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2064s) and I have a Tenant 2 execution role

[34:26](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2066s) attached to these Tenant 2 Lambda functions,

[34:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2069s) and this all happens at deployment time.

[34:32](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2072s) So here now, when I attach the policy at deployment time,

[34:35](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2075s) that policy will say, "For the life of this function,

[34:38](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2078s) this function can only access the resources

[34:40](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2080s) allowed by that execution role."

[34:43](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2083s) It's a super powerful isolation scheme

[34:45](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2085s) because now it can only access resources

[34:48](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2088s) that are valid for that particular tenant,

[34:50](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2090s) and the code inside of these functions doesn't even matter.

[34:53](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2093s) If it tries to cross those boundaries,

[34:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2094s) it's not gonna be able to across the boundary,

[34:56](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2096s) so the developers don't have to do

[34:58](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2098s) anything to comply with it, and that's great

[35:00](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2100s) and an awesome story for siloed environments,

[35:03](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2103s) but we also have these pooled environments,

[35:05](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2105s) and in a pooled environment,

[35:07](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2107s) if you look at the Lambda function,

[35:09](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2109s) when this Lambda function is deployed,

[35:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2111s) it has to be deployed in a much wider context.

[35:15](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2115s) It can't have a really wide, sorry, narrow execution role.

[35:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2119s) It has to have an execution role

[35:20](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2120s) that's valid for all the pooled tenants.

[35:23](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2123s) So now in this mode, instead,

[35:25](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2125s) we have to resolve all of your scoping

[35:28](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2128s) and your access and your policies

[35:30](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2130s) for isolation at runtime here, right?

[35:33](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2133s) So here now, when the code makes a call

[35:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2136s) into here on behalf of Tenant 3,

[35:38](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2138s) we have to resolve what the policies are for Tenant 3,

[35:41](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2141s) get those credentials,

[35:43](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2143s) and then apply them in the code of our application.

[35:45](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2145s) So this requires the cooperation

[35:49](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2149s) and the use of these individual functions

[35:53](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2153s) to be aware of the fact that they have to resolve that.

[35:56](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2156s) Now, with libraries and other mechanisms,

[35:58](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2158s) we'll go out and make it easier to resolve that

[36:01](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2161s) and get that policy data,

[36:03](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2163s) and we'll supply different mechanisms to help with that,

[36:06](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2166s) but still, the code could go around it here

[36:09](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2169s) in a way that it couldn't in the siloed model.

[36:13](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2173s) Okay, so let's look at now

[36:14](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2174s) at this deployment-based experience.

[36:17](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2177s) What does that really look like for isolation?

[36:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2179s) Well, here, the tenant comes in, tenant hits our Gateway,

[36:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2182s) it hits the authorizer,

[36:23](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2183s) and now we hit our deployed siloed function,

[36:26](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2186s) and here you'll see we have an execution role attached,

[36:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2189s) and that execution role

[36:30](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2190s) has a very specific policy for Tenant 1 to say

[36:33](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2193s) Tenant 1 can access this particular order table,

[36:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2196s) and so now it constrains your access

[36:40](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2200s) to just that order table.

[36:42](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2202s) So the execution role here is at deployment time

[36:46](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2206s) and gives us our awesome isolation story.

[36:48](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2208s) Now let's look at what that would look like,

[36:50](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2210s) though, in a pooled model.

[36:51](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2211s) Now, in a pooled model,

[36:53](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2213s) we're gonna get a request into the API Gateway.

[36:56](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2216s) That's gonna go out to the authorizer,

[36:58](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2218s) and now the authorizer is going to be responsible

[37:00](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2220s) for figuring out contextually

[37:03](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2223s) which tenant is currently calling

[37:05](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2225s) and what are the credentials that are allowed

[37:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2228s) for that particular tenant.

[37:09](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2229s) So this authorizer will go out,

[37:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2231s) will essentially use that context

[37:13](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2233s) of that particular tenant,

[37:15](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2235s) and now you'll see our policy is more of a template.

[37:17](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2237s) There's a placeholder there

[37:18](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2238s) where we will insert the tenant context,

[37:21](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2241s) and then we will assume a role

[37:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2242s) with IAM here for that new policy,

[37:25](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2245s) and we will return the credentials

[37:27](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2247s) that come back from that,

[37:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2249s) and then those credentials will then go

[37:31](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2251s) into our microservices down below.

[37:33](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2253s) So here now, inside these microservices

[37:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2256s) on the left-hand side,

[37:37](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2257s) you'll see a code that actually will use

[37:39](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2259s) these specific credentials as they go to try to access data.

[37:43](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2263s) So all this is runtime-applied.

[37:46](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2266s) Now say within our team,

[37:47](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2267s) there was a lot of debate about this approach

[37:49](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2269s) because some of the approaches we describe

[37:51](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2271s) will say resolve these scopes

[37:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2274s) within the microservices

[37:57](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2277s) instead of at the authorizer level,

[37:59](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2279s) but if your policies

[38:01](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2281s) are small enough and manageable enough

[38:03](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2283s) and you're really focused on the caching

[38:05](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2285s) and you can put them all at the authorizer side,

[38:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2288s) that's a perfectly valid approach too.

[38:10](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2290s) I would just say if you're gonna go away

[38:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2291s) and look at what isolation scheme

[38:13](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2293s) you're gonna implement for your pooled model,

[38:15](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2295s) really weigh those options.

[38:17](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2297s) Is it better for me to get those creds

[38:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2299s) and inject them at the authorizer side,

[38:21](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2301s) or is it better to deploy that responsibility more

[38:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2304s) to each individual microservice

[38:26](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2306s) and let the microservice decide

[38:28](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2308s) how it's going to resolve down to those credentials

[38:30](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2310s) and then manage all of that at the microservice level?

[38:34](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2314s) We've absolutely seen this done multiple ways,

[38:37](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2317s) just this is the way we happened to implement it

[38:38](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2318s) inside of the reference architecture,

[38:41](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2321s) and we were able to cache policies

[38:42](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2322s) and do some other things here

[38:43](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2323s) and centralize this a bit more here,

[38:46](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2326s) but then there are the downsides

[38:47](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2327s) that all of that processing is done at the authorizer side.

[38:51](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2331s) Okay, now, if you wanna look

[38:53](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2333s) at what that actually looks like

[38:55](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2335s) inside of the data access layer of our code, right?

[38:58](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2338s) If we were to crack open the data access layer of our code

[39:00](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2340s) and say, "What's going on here?"

[39:01](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2341s) well, now we have code that's accessing databases or tables,

[39:05](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2345s) and it's gotta support both silo and pooled models.

[39:09](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2349s) So in the code, you'll see, hey,

[39:10](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2350s) we look if this is a pooled model,

[39:12](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2352s) well, now we know we're using dynamic isolation,

[39:15](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2355s) so we're actually gonna go out

[39:17](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2357s) and when we create our DynamoDB instance,

[39:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2359s) right, when we create that,

[39:21](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2361s) that instance that is going to be used to access DynamoDB,

[39:25](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2365s) here we'll actually use the credentials

[39:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2369s) that are the credentials

[39:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2369s) that were acquired by the authorizer.

[39:32](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2372s) However, if we're not using that and we're in a silo model,

[39:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2376s) well, now we can rely on the execution role,

[39:38](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2378s) and so we don't need to insert

[39:40](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2380s) these credentials or anything else.

[39:41](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2381s) The execution role takes care of all that for us.

[39:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2384s) So here in supporting silo and pool models

[39:46](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2386s) is another example where the code

[39:48](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2388s) is somewhat influenced by this experience.

[39:51](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2391s) Now, the other thing here is that you'll see

[39:53](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2393s) that we have partitioned examples

[39:56](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2396s) of products in here

[39:58](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2398s) where we use instead of a silo model for the data,

[40:00](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2400s) we use a pooled model for the data,

[40:03](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2403s) and this is in our product table, and in this case,

[40:06](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2406s) the shard ID of each table is actually a tenant identifier

[40:10](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2410s) and now we're partitioning by that tenant identifier.

[40:14](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2414s) And so here, when you look at the isolation policies,

[40:16](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2416s) you'll actually see that the policy has this notion

[40:18](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2418s) of a leading key that references the shard ID,

[40:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2422s) and that says, "Hey, scope down to Tenant 1

[40:25](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2425s) or down to Tenant 2 or Tenant 3 in the policy,"

[40:27](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2427s) and we've shown this in a lot of examples we had before,

[40:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2429s) so I didn't show this one.

[40:31](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2431s) Instead, I focused on the other,

[40:33](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2433s) but this applies both to the silo

[40:35](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2435s) and pooled models of storage also,

[40:37](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2437s) just different policy schemes.

[40:40](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2440s) Now, if we actually go beyond this

[40:41](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2441s) and we look inside the microservices,

[40:43](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2443s) right, of our application,

[40:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2444s) so now we've talked about isolation,

[40:46](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2446s) let's go inside the actual microservices

[40:48](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2448s) and see what multi-tenant bits are actually in there.

[40:52](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2452s) Well, here, when I hit the Gateway, and I take a request,

[40:55](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2455s) and that request is coming into my authorizer, yes,

[40:58](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2458s) it's gonna extract the tenant ID

[40:59](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2459s) and it's gonna send that tenant ID into my microservices,

[41:02](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2462s) but now my microservices have to do things

[41:04](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2464s) that require tenant context.

[41:06](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2466s) Log a message with tenant context,

[41:07](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2467s) record a metric with tenant context,

[41:10](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2470s) access data with tenant context.

[41:12](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2472s) Well, here, we don't want all that code

[41:14](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2474s) in the microservices if we can help it.

[41:16](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2476s) We want life to be as simple

[41:17](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2477s) as it can be for our developers,

[41:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2479s) so here what we did in our reference architecture

[41:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2482s) is essentially move all of that logic,

[41:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2484s) all that common logic, out to a set of shared code

[41:28](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2488s) that runs in a Lambda layer, and in a Lambda layer,

[41:31](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2491s) we can essentially say we're gonna share all this code,

[41:33](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2493s) we're gonna deploy it and version it separately,

[41:35](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2495s) and it will be accessible to all of our Lambda functions.

[41:39](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2499s) So here we put logging here,

[41:41](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2501s) so it'll do tenant-aware logging

[41:43](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2503s) and send data out to the logs

[41:45](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2505s) and out to CloudWatch Logs with tenant context,

[41:48](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2508s) and we've got a metrics manager here

[41:49](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2509s) that will send metrics data out with tenant context,

[41:52](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2512s) and the idea is if you look at the actual code behind this,

[41:55](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2515s) the application developer knows almost nothing

[41:58](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2518s) about the fact that we're using tenant context here,

[42:00](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2520s) and the nice part of layers here

[42:01](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2521s) is that you can just keep deploying

[42:03](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2523s) and managing these shared concepts

[42:05](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2525s) and they'll just automatically be accessible

[42:07](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2527s) to all of your microservices.

[42:10](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2530s) Now, if we see it in actual action,

[42:12](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2532s) what does that look like inside the code?

[42:14](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2534s) So here's a get_order function,

[42:16](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2536s) and how are these helpers looking out?

[42:18](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2538s) Well, you'll see here's an example

[42:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2539s) of me logging with tenant context.

[42:21](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2541s) All I'm doing is calling a log message.

[42:23](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2543s) I'm not extracting the token.

[42:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2544s) I'm not pulling the tenant ID out of the JWT.

[42:26](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2546s) I'm not doing anything else

[42:28](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2548s) other than passing the event and passing the message,

[42:30](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2550s) and the log message logging takes care of everything else.

[42:33](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2553s) When I go get a record from the data access layer,

[42:35](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2555s) there's no special tenant handling or anything else here.

[42:38](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2558s) It just goes and gets it,

[42:39](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2559s) and the same when I record a metric.

[42:41](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2561s) It's just record a metric,

[42:42](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2562s) and the whole idea here is when you look at this code,

[42:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2564s) there's not all kinds of crazy multi-tenant sort of activity

[42:47](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2567s) or policies in here that are managing this.

[42:51](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2571s) Now, obviously, but we did a little bit of work

[42:53](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2573s) to record these and land them

[42:56](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2576s) inside of different mechanisms inside of AWS,

[42:59](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2579s) and so for now, at least, in the simpler version of this,

[43:01](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2581s) you can go over to X-Ray

[43:02](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2582s) and actually filter by an annotation that's here,

[43:06](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2586s) and this is where you can go see the activity

[43:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2588s) that's going on in the application.

[43:09](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2589s) This is a really lightweight example

[43:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2591s) of what you could do here.

[43:12](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2592s) We really wanna encourage people

[43:13](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2593s) to build these really rich dashboards

[43:15](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2595s) that surface this log and this metric data.

[43:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2599s) Now, the last thing we're gonna look at here

[43:21](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2601s) is tier-based throttling, right?

[43:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2602s) We said we wanted to offer different experiences

[43:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2604s) to different tiers, and yes,

[43:26](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2606s) we're isolating differently and we're deploying differently,

[43:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2609s) but we also wanna be able to say

[43:31](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2611s) how can we just use tiers as a way

[43:33](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2613s) of preventing one tenant from adversely affecting another?

[43:37](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2617s) So if you see this environment,

[43:38](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2618s) I've got a basic, a standard, a platinum,

[43:40](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2620s) a couple of platinum tier tenants,

[43:42](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2622s) and they're hitting the API Gateway,

[43:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2624s) what I wanna be able to do is say, "Hey, basic tier tenant,

[43:46](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2626s) you can't impact the experience of the platinum tier tenant.

[43:50](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2630s) I'm gonna introduce throttling that will prevent that,"

[43:53](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2633s) and the way we do that is

[43:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2634s) we go out to the custom authorizer.

[43:56](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2636s) The custom authorizer then says,

[43:57](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2637s) "Oh, I get the tenant context.

[43:59](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2639s) I'll then map that to a tenant tier

[44:01](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2641s) to find out what tier they are

[44:02](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2642s) and then I'll map that to an API key,

[44:05](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2645s) and once I have that API key,"

[44:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2648s) 'cause we have a separate API key for each tier,

[44:11](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2651s) "I can then have an authorizer policy

[44:13](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2653s) that essentially will map our API key to the usage plan,

[44:17](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2657s) and then that usage plan will be used

[44:21](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2661s) to process a given request."

[44:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2662s) So the really cool part of this is

[44:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2664s) you just make your normal request.

[44:26](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2666s) This authorizer code goes out

[44:28](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2668s) and figures out your tenant context

[44:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2669s) and figures out your API key

[44:31](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2671s) and then makes a request with that API key

[44:34](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2674s) and the attached usage plan,

[44:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2676s) and now you get throttling applied

[44:38](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2678s) on a tenant-by-tenant basis.

[44:39](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2679s) So instead of having to do that somewhere outside of this,

[44:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2684s) or do something more exotic here,

[44:46](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2686s) this is all automated for you,

[44:48](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2688s) and now you get tier-based throttling strategies,

[44:51](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2691s) a really powerful construct.

[44:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2694s) Finally, a few takeaways here.

[44:56](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2696s) Hopefully there's a few things

[44:58](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2698s) that I think that are really important

[44:59](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2699s) to remind you of as we wrap up here.

[45:03](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2703s) Certainly, I hope it's clear that serverless and SaaS

[45:06](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2706s) are just a natural fit for one another.

[45:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2708s) I mean, EKS, ECS,

[45:09](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2709s) they're all good fits for SaaS, they're awesome,

[45:12](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2712s) but this nature of having no server is really powerful,

[45:16](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2716s) and it really lets us match

[45:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2719s) actual tenant activity with meant tenant consumption

[45:22](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2722s) and it makes for a really great operational experience.

[45:26](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2726s) You should really dig in and think about

[45:28](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2728s) what are the actual isolation needs of your customers.

[45:31](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2731s) What are the tiering needs

[45:33](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2733s) as you start to look at this reference architecture?

[45:35](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2735s) 'Cause you can see here

[45:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2736s) we've got these special deployment models,

[45:38](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2738s) we've got these tiering strategies,

[45:40](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2740s) a whole lot of things being driven by tier here,

[45:43](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2743s) but you have to go and figure out

[45:44](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2744s) what are the right tiers for my environment

[45:47](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2747s) and for my solution.

[45:49](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2749s) Also, it should be really clear

[45:51](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2751s) that this onboarding experience

[45:53](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2753s) where we have this unique sort of deployment consideration,

[45:56](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2756s) as in we're deploying separate stacks

[45:57](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2757s) whether you're silo or pool, well,

[46:00](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2760s) you need to really invest in making sure

[46:02](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2762s) that's a fully automated experience, right?

[46:04](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2764s) Here's where blurring the lines,

[46:05](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2765s) where we're really gonna have,

[46:06](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2766s) we have DevOps-y code that is running all the time

[46:09](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2769s) every time our tenants are onboarding the system,

[46:12](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2772s) and that gives us the power to scale our system

[46:14](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2774s) and take on new tenants at a rapid pace.

[46:18](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2778s) You saw here where we used usage plans

[46:19](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2779s) and API keys in a really creative way with the authorizer,

[46:23](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2783s) and I think that's a really great way

[46:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2784s) to do tier-based throttling in serverless SaaS environments,

[46:28](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2788s) and also we talked about the need

[46:30](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2790s) for having these shared multi-tenant concepts

[46:33](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2793s) be put into libraries and deployed into Lambda layers

[46:36](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2796s) to simplify the experience for your developers.

[46:38](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2798s) Do everything you can to make,

[46:41](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2801s) sort of take the details of multi-tenancy

[46:43](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2803s) away from your developers

[46:45](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2805s) and move those into libraries

[46:47](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2807s) where you can manage and configure them separately.

[46:51](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2811s) Also, serverless SaaS is a great opportunity

[46:54](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2814s) for you to really get great operational efficiency

[46:56](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2816s) and agility out of your environment.

[46:58](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2818s) You should absolutely look at creative ways

[47:01](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2821s) for doing deployments here,

[47:02](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2822s) like canary releases and other mechanisms now

[47:05](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2825s) because they're a little simpler in this model,

[47:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2828s) and also now you're freed up

[47:09](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2829s) 'cause you don't have as many complexities

[47:12](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2832s) around scaling policy and things of that nature.

[47:15](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2835s) And obviously, overall, I'd love for you

[47:17](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2837s) to just take the serverless SaaS reference architecture

[47:20](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2840s) and use it as a starting point,

[47:21](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2841s) a starting point to learn more about serverless SaaS

[47:24](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2844s) or a starting point to start to build your own solution,

[47:27](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2847s) and you'll see that you can actually begin

[47:29](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2849s) to shift this to your own code quite easily.

[47:32](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2852s) Either way, we're hoping this gives you

[47:33](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2853s) a better sense of what it means

[47:35](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2855s) to build serverless SaaS on top of AWS.

[47:38](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2858s) I'd also say there's a workshop

[47:40](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2860s) that's associated with this at re:Invent as well

[47:43](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2863s) that can guide you through this in even more detail

[47:45](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2865s) than we were able to cover here today.

[47:48](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2868s) Okay, so I promised links to code at the end here.

[47:51](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2871s) There's a link to the actual

[47:52](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2872s) serverless SaaS reference architecture that we have

[47:55](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2875s) and a link to the workshop that I called out here,

[47:57](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2877s) so you can go out there, clone the code, and get going.

[48:01](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2881s) I also wanna highlight the fact

[48:02](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2882s) that we have more sessions going here.

[48:04](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2884s) We have more workshops around SaaS,

[48:05](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2885s) more chalk talks around SaaS.

[48:07](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2887s) We actually have a business session around SaaS,

[48:08](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2888s) if that interests you,

[48:10](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2890s) lots of content around SaaS that can help you

[48:12](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2892s) round out your view of the SaaS landscape, and that's it.

[48:17](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2897s) I really appreciate you being a part of this session.

[48:20](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2900s) I hope that you find the serverless SaaS information useful

[48:23](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2903s) and that you can go out and start taking a peek,

[48:25](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2905s) and I'm hoping it'll give you a head start

[48:27](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2907s) if you're thinking about building

[48:28](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2908s) serverless SaaS solutions on top of AWS, thanks so much.

[48:32](https://www.youtube.com/watch?v=8Z5zBsKgTxY&t=2912s) (upbeat music)

