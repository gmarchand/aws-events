# AWS re:Invent 2025 - AI-powered SaaS Observability using OpenSearch  (ISV313)

[Video Link](https://www.youtube.com/watch?v=KhbLaC9vw-U)

## Description

SaaS providers struggle with observability at scale, balancing costs, combining cross-tenant and single-tenant data, and surfacing actionable insights. In this code talk, learn how to build next-generation observability for your SaaS platform using semantic search, agent-led search, and other AI-powered techniques. We’ll dive deep on index mappings, ingestion flows, and query patterns, live coding a solution using Amazon OpenSearch Service.

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

So in the talk today, what we're going to do is look at how AI can help us become more effective at this troubleshooting, right? How we can restore service to our customers quicker, how we can uh find the root cause of a of a problem and then mitigate the problem easier and faster. Now this is a level 300 code talk you're attending today, so which means we're going to show you a lot of hands-on things using Amazon Open Search Service. We're going to show you code, but we're not necessarily going into the level 400 of, um, you know, explaining every single line of what we're doing. It's more meant to be an inspirational session of what you can do in this area and how you can achieve it using open search. Um, we, um, we have prepared, uh, a, um, a thorough guide for you that will, uh, link to in the end. It's a GitHub gist which will contain all of the references, all of the code snippets, and all of the material that you will need to dive deeper on this yourself afterwards. So there's no need for you to, uh, take photographs or, uh, note stuff down and, and research on the fly and so on. We'll all reference that afterwards, OK? So, uh, my name is Ulli. I'm a solutions architect, uh, based in Berlin, Germany, and my, uh, primary job is to work with software companies running SAS on AWS, um, but I'm also part of the open search community here at AWS, and today I'm very happy to be, um, accompanied by Ruben. Hi everyone, Ruben Jimenez, um, also a senior solutions architect, um, and dedicated to the, um, community of cloud ops, more of the observability, more of the optimization perspective, and very similar to Yuli, um, dealing with SAS customers and SAS customers at scale, so. So before we go into the hands on part, let me give you a brief tour of the demo application that we've developed for this talk. So when we talk about uh observability and we do a uh a hands on demo for that, we need some application that generates our observability data. And what we've done here for you to have as a background is, uh, we've basically taken the open telemetry demo application, um, and modified that. So the open telemetry demo application, uh, if you don't know it, it's an open source project you can go and check it out on GitHub, uh, and it's basically a web shop where you can buy telescopes, binoculars, and such things, and this webshop is backed by a series of different microservices that are all performing different tasks such as uh shipping, such as billing, check out, um, and so on and so forth, accounting and different microservices you'll you'll see later on. Now the main modification we did to that application is to make it into a multi-tenant SAS application. So what we're pretending here is that we're a SAS provider that offers these webshops to to different uh webshop providers um in a multi-tenant fashion. And what we did for that is we duplicated this demo application across our different tenants and when you see these animal names, uh, this is our tenant identifiers, right? So we have 10 of those and then we also extracted some shared services from these tenants, uh, which is a pattern that we often see in multi-tenant applications, right? So, uh, some things are run locally for each tenant, but then we also have shared services that are running things that all of our tenants have access to. Now this demo application is deployed into Kubernetes and Amazon EKS, and there is another component to be aware of which is this open telemetry collector component and the application, the um single uh so the different tenant applications and also the shared services export their observability data, so logs, metrics, and traces into this open telemetry collector. And this open telemetry collector then forwards this data into Amazon Open Search Service. Um, and if you're not super familiar with, um, OpenSearch and Amazon Open Search Service, the kind of the main database or the, the thing that is storing the data in OpenSearch is called an index, and then in open search service we also have this component called Open search ingestion, which is kind of an ETL tool, um, aimed at open search, right? So open search ingestion takes the data from Open telemetry Collector, transforms it, and puts it into Open search. And then last but not least, we have open search dashboards, which is an exploration and visualization component in the open search ecosystem that we're going to use to look at our data. Now what you see here is a very classic architecture for observability, right, so many AWS customers running their applications in Amazon EKS and running their observability using OpenSearch have such an architecture. So this is nothing new. What we want to talk about today is the addition of AI to this whole setup, and we're going to cover three different AI use cases again with the goal of helping us to speed up the search for the root cause of an issue. The first thing that we'll talk about is natural language query query generation in open search dashboards, which will help us um uh query our log data quicker so that we can get to the root of the problem quicker. Secondly, we'll talk about semantic log search which will enable us to find um pieces of log data that we don't know how they look so maybe you remember that if you look for a specific log line you have to kind of know how that log line looks. You have to know the specific words that are mentioned in the log line to actually be able to surface that, but sometimes you just don't know really what you're looking for, and this is what the second section will be about. And last but not least we're going to tie everything together using MCP or model context protocol where we have an AI agent in our case Kiro CLI to um do a semantic search on our log data and uh do natural language interaction for us to not only troubleshoot or find the root cause but also mitigate the issue that is uh underlying. So let me switch over to our uh demo environment here. And I brought up this uh same architecture that I just showed you here on the left, so this should be familiar. This is our hotel demo demo application running in a multi-tenant fashion. And I just want to quickly show you how this looks on a technical level. So, um, if you don't know Kubernetes very much, uh, CBCTL is the standard tooling to interact with, uh, with Kubernetes and Amazon EKS. So what we can do here is we can say, uh, CUCTL get name spaces. And then we'll see exactly what you see here on the right, uh, on the left, sorry. Uh, we have, uh, our different animals which are our tenants. We have this uh shared name space down here. And we also have our open telemetry collector name space up here. So this is all currently deployed in Amazon EKS and running. And we can also have a deeper look into these name spaces so we can say uh CubeCa get pods and then take one of our tenants, let's take the Falcon tenant and just have a look at what's running in there and you can see there are these different microservices that are powering this webshop that I talked about. So you see here things like uh the card and the the the product catalog and so on and so forth. Uh, same thing with our shared services. We can have a look at those as well. And you see here the shared services that all of our tenants are centrally accessing. Now you see here that I mean here we see an error but this has already been there for 44 days so it's nothing going on right now. Everything else seems to be running smoothly, right? Um, no, no big issues to see so far. But unfortunately not everything is good. In fact, just before our session we got a call from our CEO and he's really upset because our customers are really upset because actually the web shops are not working like any of our customers' webshops are not working at the moment. And he said that people are able to shop on the web shops like they're able to put things into their cars and so on, but they're not actually able to purchase anything which of course is is bad for for any web shop, right? So we should uh go and fix that uh ASAP. So as a first step in troubleshooting this, uh, I'll do what, uh, probably an ops person would do as well and try to reproduce or, um, uh, yeah, try to reproduce the problem on my own system, right? And the way I do this is, uh, using QubCTL port forward, um, so this is basically a tool to, uh, bring an application that is running in Kubernetes to my local host to be able to access it in a browser. So I'll do that again using the Falcon tenant and now I can access this demo application from the Falcon tenant at my port 8080 of my local host. So let's go ahead and do that. Local host 8080. And this is the webshop I was talking about so this is a kind of the classic hotel demo application and down here you have different products at your disposal that you can purchase. Let's take this telescope here. This looks good and then uh let's scroll down here to place the order. And Nothing happens, right? I click this. Nothing actually happens. Let's open the deaf console of the browser to see what's going on in terms of network activity here. We see that there's a call to check out. And this is still pending, so this is taking a long time so let's see if that comes back. Uh, it's actually timed out now with a 504, right? So there seems to be something wrong 504 if you remember, it's a, it's a gateway timeout HTP error, right? So something is timing out somewhere, but in a distributed system like this, it's quite hard to find the root cause of this now. So maybe Ruben, we can have a look at open search dashboards to figure out what the problem is. Awesome, thank you Gilli. So as Julie mentioned, um, what we can do is we can go into the console or go into the open search service, um, open dashboards, um, as you can see it's an open search UI or dashboards that specifically have connectivity into our clusters or a multi-tenant cluster. What we have here is an application or endpoint that we've configured. And what we'll do is we're going ahead and launch um this dashboard here we have our particular cluster we can go ahead and click on that. Can you zoom in a bit? Um, I think it's, uh, a bit, yeah. How are we doing there? Good. Maybe a little too much so what we have is we have the logs in terms of the the multi cluster showing up here. So what we have is we have kind of the look and feel for most of you that actually have been working with OpenSearch or open search dashboards. This should look very familiar to you really kinda have the histogram here really kinda showing the activity of those logs that are actually put into that particular um. Um, index. I'll shrink it just a little bit so we can get down here. And then from there what we're really kind of looking at is um how do we then take it and um really kind of look at it from signal to noise right? so we have a lot of logs that come through or that are there um and how do we how do we how do we make it. More palatable or or how do we really kind of start to search for what is that root cause or what it, how can we start, you know, looking for that needle in the haystack so if we were to just kind of peruse it here which we all kind of know and, and, and work with on a daily basis, especially from an ops perspective, kind of looking down and it's really kind of a lot of, a lot of information, right? Nothing that we can really index on or really anything that we can kind of put our finger on right in terms of that. So what we wanna do here and you kind of ask yourself, well I could just go ahead and I could do a query. I could put it together and I could kind of figure it out that might take a lot of time, right? And especially if you haven't done it in a while, it's like oh my goodness, where do I start? So what we wanna do is then kind of ask ourselves could we use AI to actually help us do that, right? Could we use AI to give us a little helping hand in order to kind of figure that out or what that looks like? So what we're gonna do now is we're gonna go ahead and put in a prompt. And then what we'll try to do is we'll try to narrow it down, right? Kind of narrow the logs down, kind of narrow overall what's happening or what's going on. So what I have here is I, I kinda have a cheat sheet from here, right, in terms of that. So what I'll do is I'll pop into here, I'll copy this, and this is really the prompt that I'm putting in for AI. So what I'll do is I'll pop it into here. And what I'm actually mentioning or what I'm actually bringing attention to is how can we, you know, how can we, we narrow it or, you know, get to the get to the cause. In the past I've, I've worked with this before and you know since I've been familiar with the infrastructure and things like that and working with teams I'm able to say you know this is really kind of um barks like a dog and and kinda acts like in terms of an exceeded rate limit, right? And so you know we've kind of had this in the past and I've kind of seen it right? so I'm, I'm heading towards that direction and see if I can get confirmation or not overall for that, right? So I'll go ahead and hit this prompt here. And so what's nice about AI as well, so not only did it actually narrow it down a little bit for me, right, in terms of the logs and things like that that are happening, what I'll do is I'll open it up a bit. Can kinda see a little bit of the instrumentation that went on here, right, looking for different things, um, ah, and it actually picked it up, right? rate limit exceeded and it looks like it's actually doing kind of the ship order right or the ship order maybe maybe being affected or maybe something going on with that in terms of um could cause some some problems with the other tenants right overall or it could be a tenant that's over oversubscribed and actually causing that shared service to have issues. What it also did for us, it actually went ahead normally, as I mentioned before, is we could do a PPL, right? And it actually did that for us. So not only did it actually do an AI or give us kind of some recommendations, but it also gave us a PPO that if we weren't familiar with really kind of how to craft that or do that, it gives it to us right there and then, right? So we can have a reference that we could actually do it and run it so it's very similar to the different PPOs that you would run normally in your operations. So if we go to the ice summary too, which gives us a little bit of help here. Uh, taking a bit to Generate so again it's saying hey we did a sample of this and it looks like it's the uh the shipping rate limiter right or shared name space that could be the smoking gun, right? So it gives us a little bit more and it says hey look it could actually affect or or affect these downstream processes right or these other shared services because of high traffic and not be able to process it overall. So we're now kind of formulating a picture of what does that look like now we're starting to really kind of hone in on what is that needle in the haystack, um, overall. So really we, we could do this and, and have some confirmation here, but what we wanna do is really kind of just look at, look at this, and you know, let's go through even kind of some visualization, right? I find it pretty kind of kick that through, but what I wanna do is I wanna kind of show you how this works. So what we can do is we can actually do an NOP also for a visualization. And so again this is kind of yeah it's kind of not really nice in terms of where it actually shows it and things like that I think it might be an upgrade or or not that's needed but what we're gonna do is we're gonna put in a natural response here and we're gonna see where that where that ends up or what kind of visualization that will confirm you know is our shared services having a problem with other tenants, right? So what I'll do is I'll come back here. And what I'm gonna do for this visualization here is I'm gonna log the activity, right? Give me the activity of these particular tenants and show me if there's a problem or there could potentially be a problem. And again, I like to think of it as a picture is worth 1000 words, and you can really kind of then see what's happening or what's going on. So as we can see here it actually generated a particular visualization that we can kind of see it so you can see the eagle tenant is really, you know, really, really busy, really trying to process, and you can see that the other services are really competing, right? So what we can really kind of index on that or really kind of just make that leap a bit is a noisy neighbor problem and a lot of us in terms of EKS clusters and the operational piece. You know how many times do we actually run in the noisy neighbor problem right in terms of that, especially in the multi-tenancy environment so now we're starting to say we really have this, this, this noise that's out there in terms of logs, but now we're able to really kind of make that funnel a little more finite, and then we have some answers or we have some, some areas that we can actually, uh, start to dive deep in. And Yuli mentioned these are kind of just a couple ways to go about, you know, how do we, how do we make a semblance out of chaos in terms of where we can start moving and how we can start troubleshooting, and it gives us a little bit of foray into the AI perspective. So I'll hand it over to Yuli at this point and then we'll go a little deeper in terms of the next kind of mechanism or kind of tool in our toolbox to do the semantic search and then really, really hone in on what could be the issue or what's going on with the actual multi-tenant clusters. Y, pass it over to you. So just to summarize this piece we've now figured out both the uh issue that is going on right there's a rate limiting problem in our shipping service in our shared name space and this is caused by a noisy neighbor problem caused by our eagle tenant, right? So it's apparently they're doing a big sale or something overloading our system and affecting everyone else. So, um, in, uh in this next section on semantic search I wanna take a step back so you, um, saw that Ruben in the very beginning. Uh, put in this prompt like is there a lock that is mentioning rate limit exceeded, right, which basically tells you that he kind of already knew what he was looking for, right? He said like he had this problem in the past and he knew a bit what to, what to dig after. But in lots of cases you don't really know, right? There's something weird going on in your system and you don't really know like there's this 5:04 gateway timeout and maybe you've never seen that before, right? So you may be uh completely blank and in this case semantic lock search could be of, uh, of good use. Now for a semantic log search I will pull up this uh architecture here um give me a brief show of hands who of you knows in general what semantic search is? OK, so that's like, uh, a third of the room. So let me briefly explain in general semantic search. So semantic search is kind of, um, uh, an evolution of search of a classic lexical search, right? So lexical search, what we basically do there, we compare words with with each other. We have a user query and we compare this user query word by word with what we have in our database and in this case it's log data, but it could be other types of data as well. For semantic search we're evolving this a bit and we're making search available also by meaning, which means that we're not only looking at the words that the user put in, but we're looking at the meaning of what the user put in and comparing that to the meaning of things that we have in our database. And semantic Search is powered heavily by these vector embedding models, and we have a couple of them running on Amazon Bedrock and for this particular purpose we chose the most cost effective one that we have there, which is Amazon Titan text embeddings V2. Uh, and I'll show you a bit how, how the output of those models looks, uh, later on. But for uh for log semantic log search we have to consider uh two let's say specifics about log data versus other types of search, and the first specific is that we have log data is typically very large in volume, right? So it's not just a product catalog where we have a couple of 1000 of entries maybe. But even in our little demo application we're ingesting thousands of log lines per minute already and of course in production systems it will be orders of magnitude more than that so we cannot just go and run every single log line against this embedding model because it's an AI model and this will like uh stack up quite a bill right if we do that for every single log line. So what we have to do instead is we need to work with a subset of our logs and just do embeddings for those uh the subset, and we're doing that using a technique called sampling and and I'll dive a bit into that. Now, uh, what's good on the other hand with the log lines is that log lines are typically semantically not very different from each other, right? So when you have, when you look at a uh at one specific microservices, uh, microservice and the log lines that this microservice is producing, it's typically repeating itself over and over again, right? It's the same log lines maybe with different IDs, maybe with different numbers. Numbers like the time something took or something, but this all doesn't change anything semantically like it doesn't change the meaning of the log line, right? It's it's it's only like a different, a different identifier or so which doesn't change anything in terms of semantics so we're good to do this sampling we we shouldn't miss out on too much information because it's the same things repeating themselves all the time anyway, right? So we we're good to do this sort of technique here. So let me first show you how we actually achieve this uh sampling uh and for that let's dive into uh open search ingestion which I mentioned mentioned in the beginning which is this ETL tool that we have available in the open search context. Now let's dive into the logs ingestion pipeline, which takes logs from our open telemetry collector, transforms them and puts them into open search. Now, um, the. The uh log data that we've been working with so far was our raw log data and you see that we have a little sub pipeline here that is basically just putting every single log line into open search and what Ruben has showed you before was working with with this raw data. But we have a different another subpipeline here which we call the sampled subpipeline and we, when we look at this definition down here, uh, we see that we've introduced this rate limiter in here and this rate limiter now does the sampling for us so it takes only 10 events per 2nd, 10 log lines per second per service. And we'll drop the rest, which basically means we have now a good kind of little selection of log lines from each and every single service that we have in our system. And then what we're doing with those sampled logs is we're ingesting them into a new index in open search called sampled logs. So we now have two indexes, we have the main one that stores all of our logs, and then we have the sampled logs that don't just contains a subset. But with the the the subset of of logs we're not able to do semantic search yet, right? We need to do some configuration on the open search site to be actually able to do this kind of semantic search. So let's do that together. The way I'll do that is using the open search dev tools and if you're not familiar with open search so much it's basically um a very uh lightweight developer environment where you have HTTP requests on the left hand side and the result of those requests on the right hand side and we can just kind of fire off HTP requests right and see what they come back with. Now with setting up semantic Search there are 3 steps involved and we're gonna walk through them one by one. The first one is we need to connect Amazon OpenSearch Service to Amazon Bedrock because Amazon Bedrock hosts the actual embedding model that we need, uh, as I said before, and OpenSearch will be the database and it will also do the communication to Bedrock on our behalf. Now the requests I'll fire off here are a pretty boilerplate. I'm not going to dive too much into details here. What we first need to create in OpenSearch is a is a connector to Amazon Bedrock, and we will specify the model here that we want to use in Bedrock. And then we're gonna take this connector ID that OpenSearch generated and put it into our register call here, but we also need to create this uh so-called model group and we'll also take that ID and put it into our register call. I said, as I said, I'm going, going through that a bit quicker. It's all in the GitHub just if you want to follow up a bit more in detail. Now when registering the model we get this model ID which we'll be using for the remainder of this section. We need to deploy this model first so it's known throughout our open search domain and then we can actually go and predict, which means we're testing this model now. And the cool thing is we're now talking still to the open search API, right, so through the open search API. This will call Amazon Bedrock under the hood and give us a response again through the Open search API, so the two systems are now connected with each other. And this embedding model, if you've never seen this before, comes back with this long list of floating point numbers, and this is the output that an embedding model produces, and this in a mathematical way encodes the meaning of what I put in. So I put in here what is the meaning of life, and this question is now encoded into this long list of floating point numbers which is our vector embedding. Cool, so we have established the connection now, but our sampled logs index is still not able to do semantic search, so we need to configure the sampled logs index to perform this embedding automatically on our behalf to be able to do the semantic search. So let's go ahead and configure this index. When I look at the index so far and I'm just kind of spitting out the definition of this index here, um, we don't find anything in terms of embedding in here, right? It's not in there, it's just containing all of our like plain lock lines. What I would do first is create a so-called ingest pipeline, which is a configuration object that will enable OpenSearch to automatically embed uh log lines that are flowing into the index. So I'm creating this embedding, uh, this ingest pipeline. And what this does is, it's just processing all of the uh the log lines that are flowing in, taking the log body. And producing a new field called body embedding that will store this floating point-like array of floating point numbers that we saw before, which is the vector embedding. And then we are going to create an index template for our sampled logs which contains this pipeline, so basically now saying please prepare this index for automatically embedding all of the log lines that are flowing in and you see here that I also specified this new body embedding field which is a vector field in OpenSearch. And what I'll then do is I'll just delete the sample logs index, and what's happening now under the hood is that open search ingestion will continue to ingest data into this index and open search, since the index does not exist, it will recreate it automatically applying the configuration that we've set up here. So now the index will be recreated using all this embedding pipeline and the new embedding field. So let's have a look at this sample logs index now, it's not yet found, so apparently open search ingestion has not ingested new log lines yet. Let me repeat that a few times. Should usually take just a few seconds, but sometimes it can take a bit more. And there it is back up and when I now search for embedding, we have this body embedding field here that uh is now part of my index definition. And when I go down here, I also have this pipeline as part of my index setting. So what's now happening exactly what I wanted, all of the new log lines that are flowing in are automatically embedded by OpenSearch using Amazon Bedrock. And this is the last piece of set up I needed to do. I can now perform semantic search on this index. Now we've been talking or I've been talking so much about setting this up that it's worth kind of recapping what the value of this is actually. So let's take a step back. Remember we have this 504 gateway timeout. I know that when there's a 504 gateway timeout. It indicates that something just takes very long to process, right, kind of that's what I know, right? I don't know anything of rate limiting. I don't know any exceeded or acute or anything. I don't know how the specific log line would look, but I have, um, an idea that something is just taking very long to process. So let's do that. Let's search so I can put in something very vague here. I can ask for something like uh something is taking too long, and I can do a semantic search for that to find log lines that are semantically relevant for this query. So let's have a look what it came back with. And it's exactly again the shared shipping service that we saw before, right? And it's found the log line rate limit exceeded request queued, so you see that lexically those things are not related, right? Some is taking too long is not contained anywhere in this log line, but in meaning in semantics they're very similar to each other. So I've now gone from a kind of a blank page problem. I have no idea what to even look for. I've gone to the log entry that is uh that is going into the right direction, right? So now I can have a deeper look at my shipping service to figure out what exactly that problem could be. OK, so having finished our semantic search, let's, um, let's do the 3rd part of the session and do everything together, natural language processing and semantic search, bring it all together using moderate context protocol or MCP. Cool, thank you, Yuling. So as Julie had mentioned, so it's really kind of the latest and greatest, right? So how can we have an agent, um, process these particular searches for us really kind of. Um, with a prompt, right, how can we use that same NOP or that prompt to get information back, right? How can we use it as a tool in order to, uh, interrogate, um, that particular open search service, right? And as we are moving into kind of that agentic framework, and I'm sure you're hearing throughout the, the, the conference, what is that agentic enterprise or what is that agentic framework look like, right? So we have standalone, um, agents, we have, um, autonomous agents and things like that, right? So what we're doing is we're gonna use Qiro CLI as our as our client. What we're gonna do is we're going to talk to you or interact with an MCP server that we've actually went ahead and and built out, um, in terms of Python. And then from there it actually has all of the scaffolding that Yuli had talked about in terms of being able to use the model, use the embeddings, and then go ahead and, and use that reasoning, and then bring back a particular response, um, and this was all kind of connective tissue, um, kind of leading up to this or, or delivering this piece overall. What I'm gonna do now is I'm gonna go into the configuration file in terms of the actual MCP server itself. But again, in the gist itself it has really kind of that that scaffolding of how you would set it up, how you would configure it in Kiro CLI, so you know if you're kind of wanting to dive a little bit deeper in those settings of that configuration, it's in the gist. So we'll share it up there, um, and you can go ahead and look at it and try it out or kick the tires on it. I'm a huge fan of Clear if nobody's noticed. Ah. So I'm gonna just go into the file itself in terms of the um where the actual downloads is or where. Where we have that MCP server. It's kind of painful for you guys to watch me type here. Goodness gracious. Let's see here. Uh, it doesn't say it's there. Sorry guys on that one. We'll pop in here. Just add a main main dot pi in the end. I'm a cat, not a CD. Oh, that's right. There we go, perfect. So what we have here is just kind of the set up, uh, in terms of where we're setting this up or actually the main dot pie itself. So what we have is we have our, our really kind of our import vote to 3 client right from there we're actually referencing the fast MCP for that particular component. Then we're walking down and kind of the open search connection. There's documentation that that's out there that really kind of brings this to bear or you can actually look at and reference. So what we have here is we have the host, which is the actual uh search or it's actually the open search endpoint that we're gonna interrogate or hit. We have the region that's there as well. Um, services, yes, of course, credentials we use the session and things like that which is in the AWBS account so you can access it, um, use that SIGV4 access and, and, and go ahead and being able to, um, uh, get that information or query that information. Then what we have is we use the open search client here based on the Python piece overall in terms of that client, right? So it's actually calling it, it's using the host and using the variables above in order to make that connection or hit that end point. Then what we have here is we're actually describing the MCP server itself. Uh, fast MCP seems to be, um, within Python the best way to go ahead and do that, uh, that query, right? Or do that interrogation of that endpoint, um, and then from here if we really look at it, it really just kind of boil it down. Is we can just put in a few lines of code um for that MCP server to actually do a really dynamic fetch of that particular model or that embedding model that Yuli actually set up right initially so there really isn't a whole lot of work we already have the plumbing that can actually make that connectivity or talk to that end point and what we have here is we actually have just a stanza here in terms of MCP tooling. That we can say hey look we want you to do that semantic search and we want you to go ahead and give this that body information coming back and as Julie displayed before we actually have that embedding that will actually return a response based on that very uh finite query on those 10 logs, right? Um, and then we also have the model ID so dynamically we're actually pulling in that that model ID so that we can use it and leverage it within the semantic search. And again, as you referenced before, we have the sample logs here that we could actually leverage and utilize. So what I'm gonna now do is I'm gonna go ahead and kick off our client right? um here the MCP client from there so we'll clear that out. So what this is doing is it's actually going into the MCP. JSON file or settings file, and what it's doing is it's setting it up, right? So it's reading all of the MCP servers that I have configured already and so one of them is the OS logs or it's the main pie, right, that's actually coming through. And as you can see it went ahead and welcomed and it actually loaded it successfully. You can actually go in and type MCP itself and you can validate that I actually did load or it did actually come into your environment or within your MCP client through Quiro. So what I'm gonna now do is I'm gonna just type in a a a particular uh input or an NOP input and see what I actually get right um from there so I'm gonna come down, um, my cheat sheet one more time here. What I'm gonna do at that point is ask it. Oh goodness gracious, no no no no no no. And I'm going back to a little bit to what I know in terms of the exceeded rate limits. Yuli said just sight unseen we can actually get it, but again, I wanna see what we're gonna get back with a very um targeted um NOP or or prompt. So again on everything here we'll go ask, do we really trust it or do we want it to do what we say it wants to do so we'll push it through here again. And here we go. So it's actually showing us here it found a 500 rate limit logs from the shared shipping service. So through the whole talk, you know, we've kind of been, you know, dancing around. OK, how do we really kind of, um, close the funnel or actually start to hone in on the particular root cause, and then we see it again, right? So it's more or less, it's, it's a problem with the shared shipping, um, and it's actually a noisy neighbor issue, uh, and causing that component altogether. So we kind of have confirmation at this point. So what we also wanna do is how do we remediate this right? so we can just ask it directly, um, remediate issue for me. And so Kiiro and and really kind of the whole AI component here will go ahead and just kinda give me suggestions on what they can do in order to remediate this right again you know if I didn't really know or understand what was actually going on um. With that piece, um, it would actually show me exactly what could be, what could be going on in, in that so what it's seemed really at this point, let's see. So it's actually scaling itself right? so it's actually go ahead and it's actually scaling this, uh, shipping, right? So it's actually going through and it's scaling it for me, um, overall so you know it actually went ahead and looked and says hey the recommendation is scaling that that that shipping shared service then if we go ahead and scale it. Will it go ahead and remediate the problem? So it went ahead and gave us that, or it kicked off for us, right? And we went ahead and said, OK, trust it, go ahead and do it, right? Very similar. Like, are you sure you wanna delete? Kind of the same thing, right? You wanna make sure that that you're adhering to it and, and kind of responding to it. So basically it actually scaled, so it actually gives you actions here, scaled shipping deployment from 1 to 5 replicas, right? And it did a few other things there. Um, so this is kind of what it fixed here distributions, and it gives you kind of uh an overview of what it did and what it didn't do at that point. So what we're gonna do at this point is we're gonna go back into the application to see if it actually did did prove to be successful or not, right? So, um, what we'll do is we'll go back out, um, on our command line and we'll see, um, what actually happened, if anything, so we'll quit, uh, that piece. You know, forward again, so we'll just take a look at the shared, uh, services real quick and see if it actually did. It did actually scale it so we can say yes, that actually happened and Kiiro did what we really kind of recommended it could do to solve that problem. That we wanna do is come over here we wanna port forward so as Julie had uh kicked off before we just port forward here. On one of these front ends and then we'll go and test the application to see if that application is functioning the way we wanted it to. So we'll go back here to the hotel, we'll go ahead and exit out of that, and we'll continue shopping. We'll come back in and we'll actually choose this particular product, right? We'll just kind of stay with what we wanted to before, um, of course our, our, you know, nephew wanted this particular thing, so let's see if we can actually complete it or get it done. So we'll add it to the cart as we did before. We'll walk it down here. Everything else is pretty much the same, and we'll see if we can actually place that order boom, successful. So now we've really kind of have full circle, right? So we actually went through and we looked at it from NLP, really kind of narrowed it. We went from the semantic search, not really understanding, um, what could be the issue, but then we're actually homing in more and more in terms of what the needle in the haystack would be. And then we used MCP. It's kind of an external or an agent tool to actually give us that same confirmation to actually fix it and, and move forward. So, um, with that, I'll go ahead and hand it back over to Yuli to take us home. So this uh already brings us to the end of the session. This is the GitHub gist we uh promised a few times during the session so do uh check this out uh it contains all of the code snippets, documentation references, and other references, explanations, and so on that we talked about during this session. Um, let's have a look at the time. So I think we have time for one or two spontaneous questions. So if any one of you has like, uh, wants to have a question for the room that we can answer, uh, you can do that now if you wanna raise your hand. Anyone here? OK, yeah. Uh-huh, um, is it the This is. OK, so just repeating the question for everyone. The, the question was for the connection between open search and Bedrock, whether we can have a cross region connection for that. And yes, in fact you can, yeah, you can, you can do that, uh, in our case we did it same region but you can have it cross region as well. Basically how it works is that, um, open search is assuming a role on your behalf and just, um, calling the Bedrock service, uh, end point on your behalf, yeah. Any other questions from the op side of the house? Go ahead. Just a question when you're demoing all those tools and I was showing you what part was that tools? Is that part of open? Yes, it's part is a standard part of open search dashboards. Um, so, uh, open search, uh, is fully HTTP API based, right? Uh, so, uh, in contrast to other search tools that are out there, it's fully HDP API, and this is, uh, kind of the. Main kind of playground that that people use in open search right to to play with different uh play with different end points yeah so this is not nothing new this has been around for pretty much ever yeah. Cool. OK, so, uh, with that, let's, uh, close off the session. Uh, thanks a lot for spending your valuable time with us. Uh, we can take further questions in the hallway, by the way, we just need to move out in a bit for the next speakers. Uh, happy to, to take any questions, um, offline. Um, please do fill out the session survey. I know everyone reminds you of that. Uh, please do for this session as well, especially if you liked it. We read every single piece of feedback that you put in there, so please, uh, do fill that out. Um, have a great rest of reinvent, um, enjoy the conference and hopefully see you all soon. Thanks folks.

## Subtitles with Timestamps

[00:00](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=0s) So in the talk today,

[00:01](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1s) what we're going to do is look at how AI

[00:04](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=4s) can help us

[00:05](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=5s) become more effective at this troubleshooting,

[00:08](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=8s) right? How we can

[00:10](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=10s) restore

[00:11](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=11s) service to our customers quicker,

[00:13](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=13s) how we can uh find the root cause of

[00:15](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=15s) a of a problem and then mitigate the problem

[00:18](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=18s) easier and faster.

[00:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=20s) Now this is a level 300 code

[00:22](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=22s) talk you're attending today, so which means

[00:24](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=24s) we're going to show you a lot of hands-on things

[00:27](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=27s) using Amazon Open Search Service.

[00:29](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=29s) We're going to show you code,

[00:31](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=31s) but we're not necessarily going into the

[00:33](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=33s) level 400 of, um, you know,

[00:35](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=35s) explaining every single line of what we're doing.

[00:38](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=38s) It's more meant to be an inspirational

[00:40](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=40s) session of what you can do

[00:42](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=42s) in this area

[00:43](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=43s) and how you can achieve it using

[00:45](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=45s) open search.

[00:48](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=48s) Um, we, um, we have

[00:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=50s) prepared, uh, a, um, a

[00:52](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=52s) thorough guide for you that will, uh,

[00:54](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=54s) link to in the end. It's a GitHub gist

[00:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=57s) which will contain all of the references, all

[00:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=59s) of the code snippets, and all of the material

[01:01](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=61s) that you will need to dive deeper on this

[01:03](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=63s) yourself afterwards.

[01:04](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=64s) So there's no need for you to,

[01:06](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=66s) uh, take photographs or, uh,

[01:09](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=69s) note stuff down and, and research on the

[01:11](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=71s) fly and so on. We'll all reference that

[01:13](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=73s) afterwards, OK?

[01:15](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=75s) So, uh, my name is Ulli. I'm a solutions

[01:17](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=77s) architect,

[01:18](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=78s) uh, based in Berlin, Germany,

[01:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=80s) and my, uh, primary job

[01:22](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=82s) is to work with software companies

[01:24](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=84s) running SAS on AWS,

[01:26](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=86s) um, but I'm also part of the open search

[01:28](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=88s) community here at AWS,

[01:30](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=90s) and today I'm very happy to be, um,

[01:33](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=93s) accompanied by Ruben.

[01:35](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=95s) Hi everyone, Ruben Jimenez, um, also a

[01:37](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=97s) senior solutions architect,

[01:39](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=99s) um, and dedicated to the,

[01:41](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=101s) um, community of cloud ops,

[01:43](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=103s) more of the observability, more of the optimization

[01:46](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=106s) perspective, and very similar to Yuli,

[01:48](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=108s) um, dealing with SAS customers and SAS

[01:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=110s) customers at scale,

[01:52](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=112s) so. So before we

[01:54](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=114s) go into the hands on part, let me

[01:56](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=116s) give you a brief tour of the demo application

[01:58](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=118s) that we've developed for this talk.

[02:01](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=121s) So when we talk about uh observability

[02:03](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=123s) and we do a uh a hands on demo

[02:05](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=125s) for that, we need some application that generates

[02:07](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=127s) our observability data.

[02:09](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=129s) And what we've done here for you to

[02:11](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=131s) have as a background is, uh,

[02:14](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=134s) we've basically taken the open telemetry

[02:16](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=136s) demo application, um, and modified

[02:19](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=139s) that. So the open telemetry

[02:21](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=141s) demo application,

[02:22](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=142s) uh, if you don't know it, it's an open source

[02:24](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=144s) project you can go and check it out on GitHub,

[02:27](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=147s) uh, and it's basically a web shop

[02:29](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=149s) where you can buy telescopes, binoculars,

[02:32](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=152s) and such things,

[02:34](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=154s) and this webshop is backed by

[02:36](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=156s) a series of different microservices

[02:38](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=158s) that are all performing different tasks such

[02:40](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=160s) as uh shipping, such as billing,

[02:43](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=163s) check out, um, and so on and so

[02:45](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=165s) forth, accounting and different microservices

[02:47](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=167s) you'll you'll see later on.

[02:49](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=169s) Now the main modification we did to that

[02:52](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=172s) application is to make it into a multi-tenant

[02:55](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=175s) SAS application. So what we're pretending

[02:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=177s) here is that we're a SAS provider that

[02:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=179s) offers these

[03:00](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=180s) webshops to to different uh webshop

[03:02](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=182s) providers um in a multi-tenant

[03:04](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=184s) fashion.

[03:06](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=186s) And what we did for that is we duplicated

[03:09](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=189s) this demo application across our different

[03:11](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=191s) tenants and when you see these animal

[03:13](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=193s) names, uh, this is our tenant identifiers,

[03:16](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=196s) right? So we have 10 of those and

[03:18](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=198s) then we also extracted some

[03:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=200s) shared services from these tenants,

[03:22](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=202s) uh, which is a pattern that we often see in multi-tenant

[03:25](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=205s) applications, right? So, uh, some things are

[03:27](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=207s) run locally for each tenant, but then we also

[03:29](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=209s) have shared services that are running

[03:31](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=211s) things that all of our tenants have

[03:34](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=214s) access to.

[03:35](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=215s) Now this demo application is deployed into

[03:37](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=217s) Kubernetes and Amazon EKS,

[03:40](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=220s) and there is another component

[03:42](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=222s) to be aware of which is this open telemetry

[03:45](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=225s) collector component and the

[03:48](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=228s) application, the um

[03:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=230s) single uh so the different tenant

[03:52](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=232s) applications and also the shared services

[03:54](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=234s) export their observability data,

[03:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=237s) so logs, metrics, and traces

[03:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=239s) into this open telemetry collector.

[04:01](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=241s) And this open telemetry collector then forwards

[04:04](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=244s) this data into Amazon Open Search

[04:06](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=246s) Service.

[04:07](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=247s) Um, and if you're not super familiar

[04:09](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=249s) with, um, OpenSearch and Amazon Open Search

[04:12](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=252s) Service,

[04:13](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=253s) the kind of the main

[04:15](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=255s) database or the, the thing that is storing

[04:18](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=258s) the data in OpenSearch is called an index,

[04:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=260s) and then in open search service we also

[04:22](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=262s) have this component called Open search

[04:24](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=264s) ingestion, which is kind of an ETL

[04:27](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=267s) tool, um, aimed at open

[04:29](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=269s) search, right? So open search ingestion takes

[04:31](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=271s) the data from Open telemetry Collector,

[04:34](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=274s) transforms it, and puts it into

[04:36](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=276s) Open search.

[04:38](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=278s) And then last but not least, we have open search

[04:40](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=280s) dashboards, which is an exploration

[04:43](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=283s) and visualization component in the

[04:45](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=285s) open search ecosystem that we're going

[04:47](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=287s) to use to look at our data.

[04:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=290s) Now what you see here is a very

[04:52](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=292s) classic architecture for observability,

[04:54](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=294s) right, so many AWS customers running

[04:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=297s) their applications in Amazon EKS

[05:00](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=300s) and running their observability using OpenSearch

[05:02](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=302s) have such an architecture. So this is

[05:04](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=304s) nothing new.

[05:06](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=306s) What we want to talk about today is

[05:08](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=308s) the addition of AI to this

[05:10](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=310s) whole setup,

[05:11](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=311s) and we're going to cover three different

[05:14](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=314s) AI use cases again

[05:16](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=316s) with the goal of helping us to

[05:18](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=318s) speed up the search for the root

[05:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=320s) cause of an issue.

[05:22](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=322s) The first thing

[05:23](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=323s) that we'll talk about is natural

[05:26](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=326s) language query query generation

[05:28](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=328s) in open search dashboards,

[05:30](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=330s) which will help us um

[05:32](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=332s) uh query our log data

[05:34](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=334s) quicker so that we can get to the root

[05:36](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=336s) of the problem quicker.

[05:39](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=339s) Secondly, we'll talk about semantic log

[05:41](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=341s) search which will enable us to find

[05:44](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=344s) um pieces of log data that

[05:47](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=347s) we don't know how they look so

[05:49](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=349s) maybe you remember that if you

[05:51](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=351s) look for a specific log line you have

[05:53](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=353s) to kind of know how that log line

[05:55](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=355s) looks. You have to know

[05:56](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=356s) the specific words that are mentioned in the log

[05:58](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=358s) line to actually be able to surface that,

[06:01](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=361s) but sometimes you just don't know really what you're

[06:03](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=363s) looking for, and this is what the second section

[06:05](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=365s) will be about.

[06:07](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=367s) And last but not least we're going to tie everything

[06:09](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=369s) together

[06:11](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=371s) using MCP or model context protocol

[06:13](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=373s) where we have an AI agent in our case

[06:15](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=375s) Kiro CLI

[06:17](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=377s) to um do a semantic search on

[06:19](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=379s) our log data and uh do

[06:21](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=381s) natural language interaction for us to not

[06:23](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=383s) only troubleshoot or find the root cause

[06:25](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=385s) but also mitigate the issue

[06:27](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=387s) that is uh underlying.

[06:31](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=391s) So let me switch over to our

[06:33](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=393s) uh demo

[06:34](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=394s) environment here.

[06:37](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=397s) And I brought up this uh same architecture

[06:40](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=400s) that I just showed you here on the left, so

[06:42](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=402s) this should be familiar. This is our

[06:44](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=404s) hotel demo demo application running in

[06:46](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=406s) a multi-tenant fashion.

[06:48](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=408s) And I just want to quickly show you how this

[06:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=410s) looks on a technical level. So, um,

[06:52](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=412s) if you don't know Kubernetes very much,

[06:55](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=415s) uh, CBCTL is the standard

[06:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=417s) tooling to interact with, uh, with Kubernetes

[07:00](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=420s) and Amazon EKS.

[07:01](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=421s) So what we can do here is we can say,

[07:03](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=423s) uh, CUCTL get name spaces.

[07:06](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=426s) And then we'll see exactly what you see here

[07:08](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=428s) on the right, uh, on the left, sorry.

[07:11](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=431s) Uh, we have, uh, our different

[07:13](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=433s) animals which are our tenants.

[07:16](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=436s) We have this uh shared name

[07:18](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=438s) space down here.

[07:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=440s) And we also have our open telemetry

[07:23](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=443s) collector name space up here.

[07:25](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=445s) So this is all currently deployed in

[07:28](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=448s) Amazon EKS and running.

[07:31](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=451s) And we can also have a deeper look into

[07:33](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=453s) these name spaces so we can say

[07:35](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=455s) uh CubeCa get pods and

[07:37](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=457s) then take one of our tenants, let's take the Falcon

[07:39](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=459s) tenant

[07:41](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=461s) and just have a look at what's running in

[07:43](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=463s) there and you can see

[07:45](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=465s) there are these different microservices that are

[07:47](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=467s) powering this webshop that I talked

[07:49](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=469s) about. So you see here things

[07:51](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=471s) like uh the card and the the the

[07:54](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=474s) product catalog and so on and so forth.

[07:56](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=476s) Uh, same thing with our

[07:58](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=478s) shared services. We can have a look at

[08:01](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=481s) those as well.

[08:04](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=484s) And you see here the shared services

[08:06](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=486s) that all of our tenants are centrally

[08:08](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=488s) accessing. Now you

[08:10](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=490s) see here that I mean here we

[08:12](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=492s) see an error but this has already been

[08:15](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=495s) there for 44 days so it's

[08:17](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=497s) nothing going on right now.

[08:19](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=499s) Everything else seems to be running smoothly, right?

[08:22](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=502s) Um, no, no big issues to

[08:24](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=504s) see so far.

[08:26](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=506s) But unfortunately not everything is good. In fact,

[08:29](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=509s) just before our session we got a call from our

[08:31](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=511s) CEO

[08:32](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=512s) and he's really upset

[08:34](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=514s) because our customers are really upset

[08:36](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=516s) because actually the web shops are not

[08:38](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=518s) working like any of our customers' webshops

[08:41](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=521s) are not working at the moment.

[08:44](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=524s) And he said that

[08:45](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=525s) people are able to shop on

[08:47](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=527s) the web shops like they're able to put things

[08:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=530s) into their cars and so on,

[08:52](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=532s) but they're not actually able to purchase

[08:54](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=534s) anything which of course is is bad for for

[08:56](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=536s) any web shop, right? So we should uh

[08:58](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=538s) go and fix that uh ASAP.

[09:02](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=542s) So as a first step in troubleshooting

[09:04](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=544s) this, uh, I'll do what, uh, probably

[09:06](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=546s) an ops person would do as well and

[09:08](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=548s) try to reproduce or, um,

[09:11](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=551s) uh, yeah,

[09:12](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=552s) try to reproduce the problem on my own system,

[09:14](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=554s) right? And the way I do this is,

[09:16](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=556s) uh, using QubCTL port forward,

[09:19](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=559s) um, so this is basically a tool to,

[09:21](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=561s) uh, bring an application that is running

[09:23](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=563s) in Kubernetes to my local

[09:25](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=565s) host to be able to access it in a browser.

[09:28](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=568s) So I'll do that again using the Falcon

[09:30](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=570s) tenant and now I can access

[09:32](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=572s) this demo application from the Falcon tenant

[09:35](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=575s) at my port 8080

[09:37](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=577s) of my local host.

[09:40](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=580s) So let's go ahead and do that.

[09:44](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=584s) Local host 8080.

[09:47](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=587s) And this is the webshop I was talking about so

[09:49](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=589s) this is a kind of the classic

[09:51](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=591s) hotel demo application

[09:53](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=593s) and down here you have different products

[09:55](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=595s) at your disposal that you can purchase.

[09:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=597s) Let's take this telescope here. This looks

[10:00](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=600s) good and

[10:02](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=602s) then uh let's scroll down here

[10:04](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=604s) to place the order.

[10:07](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=607s) And

[10:10](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=610s) Nothing happens,

[10:11](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=611s) right? I click this.

[10:15](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=615s) Nothing actually happens. Let's open the deaf

[10:17](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=617s) console of the browser to see what's

[10:19](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=619s) going on in terms of network activity here.

[10:22](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=622s) We see that there's a call to check out.

[10:25](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=625s) And this is still pending, so this

[10:27](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=627s) is taking a long time so let's see

[10:30](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=630s) if that comes back.

[10:37](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=637s) Uh, it's actually timed out now with a

[10:39](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=639s) 504, right?

[10:40](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=640s) So there seems to be something wrong 504

[10:43](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=643s) if you remember, it's a, it's a gateway timeout

[10:46](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=646s) HTP error, right? So something is timing

[10:48](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=648s) out somewhere,

[10:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=650s) but in a distributed system like this,

[10:52](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=652s) it's quite hard to find the root cause of

[10:54](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=654s) this now.

[10:55](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=655s) So maybe Ruben, we can have a look

[10:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=657s) at open search dashboards to figure out

[10:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=659s) what the problem is. Awesome, thank you Gilli.

[11:03](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=663s) So as Julie mentioned, um, what we can

[11:05](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=665s) do is we can go into the console or

[11:07](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=667s) go into the open search service, um, open

[11:09](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=669s) dashboards, um, as you can see

[11:11](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=671s) it's an open search UI or dashboards

[11:14](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=674s) that specifically have connectivity into

[11:16](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=676s) our clusters or a multi-tenant cluster.

[11:19](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=679s) What we have here is an application or

[11:21](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=681s) endpoint that we've configured.

[11:24](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=684s) And what we'll do is we're going ahead and launch

[11:26](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=686s) um this dashboard

[11:28](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=688s) here we have our particular cluster we can

[11:30](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=690s) go ahead and click on that.

[11:32](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=692s) Can you zoom in a bit? Um,

[11:33](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=693s) I think it's, uh, a bit,

[11:36](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=696s) yeah. How

[11:39](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=699s) are we doing there? Good.

[11:43](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=703s) Maybe a little too much

[11:46](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=706s) so what we have is we have the logs in

[11:48](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=708s) terms of the the multi cluster showing up

[11:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=710s) here. So what we have is we have kind

[11:52](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=712s) of the look and feel for most of you that actually

[11:54](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=714s) have been working with OpenSearch or open search dashboards.

[11:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=717s) This should look very familiar to you

[12:00](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=720s) really kinda have the histogram here really

[12:02](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=722s) kinda showing the activity of those logs that are

[12:04](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=724s) actually put into that particular

[12:06](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=726s) um.

[12:08](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=728s) Um,

[12:09](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=729s) index.

[12:12](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=732s) I'll shrink it just a little bit so we can get down

[12:14](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=734s) here. And

[12:18](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=738s) then from there what we're really kind of looking at is

[12:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=740s) um how do we then take it

[12:23](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=743s) and

[12:24](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=744s) um

[12:25](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=745s) really kind of look at it from signal to noise

[12:27](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=747s) right? so we have a lot of logs that come

[12:29](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=749s) through or that are there

[12:31](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=751s) um and how do we

[12:32](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=752s) how do we how do we make it.

[12:34](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=754s) More palatable or or how do we really kind of

[12:36](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=756s) start to search for

[12:38](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=758s) what is that root cause or what

[12:40](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=760s) it, how can we start, you know, looking

[12:42](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=762s) for that needle in the haystack

[12:44](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=764s) so if we were to just kind of peruse it here

[12:46](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=766s) which we all kind of know and, and, and work

[12:49](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=769s) with on a daily basis, especially from an ops

[12:51](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=771s) perspective,

[12:52](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=772s) kind of looking down and

[12:53](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=773s) it's really kind of a lot of,

[12:55](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=775s) a lot of information, right? Nothing that we

[12:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=777s) can really index on or really anything that we

[12:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=779s) can kind of put our finger on right

[13:01](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=781s) in terms of that.

[13:03](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=783s) So what we wanna do here and you kind

[13:05](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=785s) of ask yourself, well I could just go ahead and

[13:07](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=787s) I could do a query. I could put it together

[13:09](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=789s) and I could kind of figure it out

[13:11](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=791s) that might take a lot of time, right? And

[13:13](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=793s) especially if you haven't done it in a while, it's like

[13:15](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=795s) oh my goodness, where do I start?

[13:18](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=798s) So what we wanna do is then kind of ask

[13:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=800s) ourselves could we use AI to actually help us

[13:22](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=802s) do that, right?

[13:23](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=803s) Could we use AI to give us a little helping

[13:25](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=805s) hand in order to kind of figure that out or what that

[13:27](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=807s) looks like?

[13:29](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=809s) So what we're gonna do now is we're gonna go ahead and put

[13:31](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=811s) in a prompt.

[13:32](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=812s) And then what we'll try to do is we'll try to narrow it

[13:34](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=814s) down, right? Kind of narrow the logs down,

[13:36](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=816s) kind of narrow overall what's happening or what's

[13:39](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=819s) going on.

[13:41](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=821s) So what I have here is I, I kinda have a cheat

[13:43](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=823s) sheet from here, right, in terms of that. So

[13:45](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=825s) what I'll do is I'll pop into here,

[13:47](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=827s) I'll copy this, and this is really the prompt that

[13:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=830s) I'm putting in for AI.

[13:52](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=832s) So what I'll do is I'll pop it into here.

[13:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=837s) And what I'm actually mentioning or what I'm actually

[13:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=839s) bringing attention to is

[14:01](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=841s) how can we, you know, how can we, we narrow

[14:03](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=843s) it or, you know, get to the get to the cause.

[14:06](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=846s) In the past I've, I've worked with this

[14:09](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=849s) before and you know since I've been familiar with

[14:11](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=851s) the infrastructure and things like that and working with teams

[14:13](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=853s) I'm able to say

[14:14](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=854s) you know this is really kind of

[14:16](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=856s) um barks like a dog and and kinda acts

[14:18](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=858s) like in terms of an exceeded rate limit,

[14:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=860s) right? And so you know we've kind

[14:22](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=862s) of had this in the past and I've kind of

[14:25](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=865s) seen it right?

[14:26](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=866s) so I'm, I'm heading towards that direction and

[14:28](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=868s) see if I can get confirmation or not

[14:30](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=870s) overall for that, right?

[14:32](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=872s) So I'll go ahead and hit this prompt here.

[14:37](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=877s) And so what's nice about AI as well, so

[14:39](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=879s) not only did it actually narrow it down a little bit

[14:41](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=881s) for me, right, in terms of the logs and things

[14:43](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=883s) like that that are happening,

[14:45](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=885s) what I'll do is I'll open it up a bit.

[14:48](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=888s) Can kinda see a little bit of the instrumentation that went

[14:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=890s) on here, right, looking for different things,

[14:53](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=893s) um, ah,

[14:54](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=894s) and it actually picked it up, right? rate limit exceeded

[14:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=897s) and it looks like it's actually doing kind of the ship

[14:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=899s) order right or the ship order

[15:01](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=901s) maybe maybe being affected or

[15:03](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=903s) maybe

[15:04](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=904s) something going on with that in terms of um

[15:06](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=906s) could cause some some problems with the other tenants

[15:09](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=909s) right overall or it could be a tenant

[15:11](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=911s) that's over oversubscribed and

[15:13](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=913s) actually causing that shared service to have issues.

[15:16](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=916s) What it also did for us, it actually went ahead

[15:19](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=919s) normally, as I mentioned before, is we could do

[15:21](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=921s) a PPL, right? And it actually did that

[15:23](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=923s) for us. So not only did it actually

[15:25](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=925s) do an AI or give us kind of some recommendations,

[15:28](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=928s) but it also gave us a PPO

[15:30](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=930s) that if we weren't familiar with really kind of

[15:32](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=932s) how to craft that or do that, it

[15:34](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=934s) gives it to us right there and then, right?

[15:36](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=936s) So we can have a reference that we could actually do it

[15:38](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=938s) and run it so it's very similar

[15:41](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=941s) to the different PPOs that you would run normally

[15:43](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=943s) in your operations.

[15:45](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=945s) So if we go to the ice summary too, which gives

[15:47](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=947s) us a little bit of help here.

[15:53](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=953s) Uh, taking a bit to

[15:56](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=956s) Generate

[15:56](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=956s) so again it's saying hey we did a sample of

[15:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=959s) this and it looks like it's the uh the shipping

[16:01](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=961s) rate limiter right or shared name space

[16:03](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=963s) that could be the smoking gun, right?

[16:05](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=965s) So it gives us a little bit more and it says hey look

[16:08](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=968s) it could actually affect or or

[16:10](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=970s) affect these downstream processes right or these

[16:12](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=972s) other shared services because of high traffic

[16:14](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=974s) and not be able to process it overall.

[16:17](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=977s) So we're now kind of formulating a picture

[16:19](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=979s) of what does that look like

[16:21](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=981s) now we're starting to really kind of hone in on what is that

[16:23](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=983s) needle in the haystack, um, overall.

[16:25](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=985s) So really we, we could do this and, and have

[16:28](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=988s) some confirmation here,

[16:29](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=989s) but what we wanna do is really kind of just look at, look

[16:31](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=991s) at this, and

[16:32](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=992s) you know, let's go through even kind of some visualization,

[16:35](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=995s) right? I find it

[16:36](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=996s) pretty kind of kick that through, but what I wanna

[16:38](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=998s) do is I wanna kind of show you how this works.

[16:41](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1001s) So what we can do is we can actually do an NOP

[16:43](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1003s) also for a visualization.

[16:46](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1006s) And so

[16:47](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1007s) again this is kind of yeah it's kind of

[16:49](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1009s) not really nice in terms of where it actually

[16:51](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1011s) shows it and things like that I think it might be an upgrade

[16:53](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1013s) or or not that's needed

[16:55](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1015s) but what we're gonna do is we're gonna put in a natural response

[16:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1017s) here and we're gonna see

[16:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1019s) where that where that ends up or what kind of visualization

[17:02](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1022s) that will confirm

[17:04](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1024s) you know is our shared services having a problem

[17:06](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1026s) with other tenants, right?

[17:08](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1028s) So what I'll do is I'll come back here.

[17:12](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1032s) And what I'm gonna do for this visualization here

[17:14](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1034s) is I'm gonna log the activity, right?

[17:17](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1037s) Give me the activity of these

[17:19](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1039s) particular tenants

[17:21](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1041s) and show me if there's a

[17:23](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1043s) problem or there could potentially be a problem.

[17:25](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1045s) And again, I like to think of it as a picture is worth

[17:28](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1048s) 1000 words,

[17:29](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1049s) and you can really kind of then see what's happening or

[17:31](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1051s) what's going on.

[17:32](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1052s) So as we can see here it actually generated

[17:35](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1055s) a particular visualization that we can kind of see

[17:37](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1057s) it so you can see the eagle tenant

[17:39](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1059s) is really,

[17:40](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1060s) you know, really, really busy, really trying to

[17:42](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1062s) process, and you can see that the other

[17:44](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1064s) services are really competing, right?

[17:46](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1066s) So what we can really kind of index on that or

[17:48](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1068s) really kind of just make that leap a bit

[17:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1070s) is a noisy neighbor problem and a

[17:53](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1073s) lot of us in terms of EKS clusters

[17:55](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1075s) and the operational piece.

[17:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1077s) You know how many times do we actually run in the noisy

[17:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1079s) neighbor problem right in terms of that, especially

[18:01](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1081s) in the multi-tenancy environment

[18:03](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1083s) so now we're starting to say

[18:05](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1085s) we really have this, this, this noise

[18:07](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1087s) that's out there in terms of logs, but now we're able

[18:09](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1089s) to really kind of

[18:11](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1091s) make that funnel a little more finite,

[18:14](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1094s) and then we have some answers or we have some, some

[18:16](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1096s) areas that we can actually,

[18:17](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1097s) uh, start to dive deep in.

[18:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1100s) And Yuli mentioned these are kind of just

[18:22](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1102s) a couple ways to go about, you know,

[18:24](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1104s) how do we,

[18:25](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1105s) how do we make a semblance out of chaos

[18:28](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1108s) in terms of where we can start moving and how we

[18:30](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1110s) can start troubleshooting,

[18:31](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1111s) and it gives us a little bit of foray into the AI

[18:34](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1114s) perspective.

[18:35](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1115s) So I'll hand it over to Yuli at this point

[18:38](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1118s) and then we'll go a little deeper in terms of the

[18:40](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1120s) next kind of mechanism or kind of tool

[18:42](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1122s) in our toolbox to do the semantic

[18:44](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1124s) search and then really, really hone

[18:46](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1126s) in on what could be the issue or what's going on

[18:48](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1128s) with the actual multi-tenant clusters. Y,

[18:51](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1131s) pass it over to you.

[18:53](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1133s) So just to summarize this piece we've now figured

[18:56](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1136s) out both the

[18:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1137s) uh issue that is going on right there's a

[18:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1139s) rate limiting problem in our shipping

[19:01](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1141s) service in our shared name space and this

[19:04](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1144s) is caused by a noisy neighbor problem

[19:06](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1146s) caused by our eagle tenant, right? So it's

[19:08](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1148s) apparently they're doing a big sale or something

[19:11](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1151s) overloading our system and affecting

[19:13](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1153s) everyone else.

[19:14](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1154s) So, um,

[19:15](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1155s) in, uh in this next section on semantic

[19:18](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1158s) search I wanna take a step back so you,

[19:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1160s) um, saw that Ruben in the very

[19:22](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1162s) beginning. Uh, put in this

[19:24](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1164s) prompt like is there a lock that

[19:27](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1167s) is mentioning rate limit exceeded,

[19:29](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1169s) right, which basically tells you

[19:31](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1171s) that he kind of already knew what

[19:33](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1173s) he was looking for, right? He said like he

[19:35](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1175s) had this problem in the past and he

[19:37](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1177s) knew a bit what to, what to dig after.

[19:40](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1180s) But in lots of cases you don't

[19:42](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1182s) really know, right?

[19:44](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1184s) There's something weird going on in your system and

[19:46](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1186s) you don't really know like there's this 5:04 gateway

[19:48](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1188s) timeout and maybe you've never seen that

[19:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1190s) before, right? So you may be uh

[19:53](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1193s) completely blank and in this case

[19:55](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1195s) semantic lock search could be

[19:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1197s) of, uh, of good use.

[20:00](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1200s) Now for a semantic log search I will

[20:02](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1202s) pull up this uh architecture here

[20:05](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1205s) um give me a brief show of hands who of you

[20:07](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1207s) knows in general what semantic search is?

[20:12](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1212s) OK, so that's like, uh, a third of the room. So

[20:14](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1214s) let me briefly explain in general

[20:16](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1216s) semantic search.

[20:18](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1218s) So semantic search is kind of, um,

[20:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1220s) uh, an evolution of search

[20:22](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1222s) of a classic lexical search, right? So

[20:25](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1225s) lexical search, what we basically do there,

[20:27](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1227s) we compare words with with each other. We

[20:29](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1229s) have a user query and we compare

[20:31](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1231s) this user query word by word with

[20:34](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1234s) what we have in our database and in this case

[20:36](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1236s) it's log data, but it could be other types of

[20:38](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1238s) data as well.

[20:39](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1239s) For semantic search we're evolving this a

[20:41](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1241s) bit and we're making

[20:43](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1243s) search available also by meaning,

[20:45](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1245s) which means that we're not only looking at

[20:47](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1247s) the words that the user put in, but we're

[20:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1250s) looking at the meaning of what the user put

[20:52](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1252s) in and comparing that to the meaning

[20:54](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1254s) of things that we have in our database.

[20:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1257s) And semantic Search is powered heavily

[20:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1259s) by these vector embedding models, and

[21:01](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1261s) we have a couple of them

[21:03](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1263s) running on Amazon Bedrock

[21:05](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1265s) and for this particular purpose we chose

[21:07](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1267s) the most cost effective one that we have

[21:09](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1269s) there, which is Amazon Titan text

[21:11](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1271s) embeddings V2.

[21:13](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1273s) Uh, and I'll show you a bit how, how the

[21:15](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1275s) output of those models looks, uh, later

[21:17](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1277s) on. But for

[21:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1280s) uh for log semantic log

[21:22](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1282s) search we have to consider uh

[21:24](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1284s) two let's say specifics

[21:26](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1286s) about log data versus other types

[21:28](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1288s) of search,

[21:29](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1289s) and the first specific is that

[21:32](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1292s) we have log data is typically

[21:34](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1294s) very large in volume, right? So

[21:36](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1296s) it's not just a product catalog where we have a

[21:38](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1298s) couple of 1000 of entries maybe.

[21:41](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1301s) But even in our little demo application

[21:43](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1303s) we're ingesting thousands of log

[21:45](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1305s) lines per minute already and of

[21:47](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1307s) course in production systems it will be

[21:49](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1309s) orders of magnitude more than that

[21:52](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1312s) so we cannot just go and run

[21:54](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1314s) every single log line against this embedding

[21:56](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1316s) model because it's an AI model and this will

[21:58](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1318s) like uh stack up quite a bill

[22:00](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1320s) right if we do that for every single log line.

[22:03](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1323s) So what we have to do instead is we need to

[22:05](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1325s) work with a subset of our logs

[22:08](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1328s) and just do embeddings for

[22:10](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1330s) those uh the subset, and we're doing

[22:12](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1332s) that using a technique called sampling

[22:14](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1334s) and and I'll dive a bit into that.

[22:17](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1337s) Now, uh, what's good on the other hand

[22:19](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1339s) with the log lines is that log

[22:22](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1342s) lines are typically semantically not

[22:24](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1344s) very different from each other, right? So

[22:26](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1346s) when you have, when you look at a uh at

[22:28](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1348s) one specific microservices,

[22:31](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1351s) uh, microservice and the log lines

[22:33](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1353s) that this microservice is producing,

[22:35](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1355s) it's typically repeating itself over and over

[22:37](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1357s) again, right? It's the same log lines maybe

[22:40](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1360s) with different IDs, maybe with different

[22:42](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1362s) numbers. Numbers like the time something took or

[22:44](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1364s) something, but this all doesn't change

[22:46](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1366s) anything semantically like it doesn't change the meaning

[22:48](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1368s) of the log line, right? It's it's it's only

[22:51](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1371s) like a different, a different identifier

[22:53](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1373s) or so which doesn't change anything in terms of

[22:55](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1375s) semantics so we're good to do this

[22:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1377s) sampling we

[22:58](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1378s) we shouldn't miss out on too much

[23:00](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1380s) information because it's the same things repeating

[23:02](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1382s) themselves all the time anyway, right? So we we're

[23:04](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1384s) good to do this sort of technique here.

[23:08](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1388s) So let me first show you how we actually

[23:11](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1391s) achieve this uh sampling uh

[23:13](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1393s) and for that let's dive into

[23:16](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1396s) uh open search ingestion which I mentioned

[23:18](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1398s) mentioned in the beginning which is this ETL

[23:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1400s) tool that we have available in

[23:22](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1402s) the open search context.

[23:25](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1405s) Now let's dive into the logs

[23:28](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1408s) ingestion pipeline, which

[23:30](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1410s) takes logs from our open telemetry collector,

[23:32](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1412s) transforms them and puts them into open

[23:34](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1414s) search. Now,

[23:36](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1416s) um,

[23:37](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1417s) the.

[23:40](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1420s) The uh log

[23:42](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1422s) data that we've been working with so far

[23:44](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1424s) was our raw log data

[23:46](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1426s) and you see that we have a little sub pipeline

[23:48](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1428s) here that is basically just putting every single

[23:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1430s) log line into open search and what Ruben

[23:52](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1432s) has showed you before was working with with

[23:55](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1435s) this raw data.

[23:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1437s) But we have a different another subpipeline

[23:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1439s) here which we call the sampled subpipeline

[24:02](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1442s) and we, when we look at this definition

[24:04](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1444s) down here,

[24:06](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1446s) uh, we see that we've introduced this

[24:08](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1448s) rate limiter in here and this rate

[24:10](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1450s) limiter now does the sampling for us

[24:12](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1452s) so it takes

[24:14](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1454s) only 10 events per 2nd, 10

[24:16](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1456s) log lines per second per service.

[24:19](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1459s) And we'll drop the rest,

[24:21](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1461s) which basically means we have now a good

[24:23](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1463s) kind of little selection of log

[24:25](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1465s) lines from each and every single service that

[24:27](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1467s) we have

[24:28](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1468s) in our system.

[24:30](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1470s) And then what we're doing with those sampled

[24:32](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1472s) logs is we're ingesting them

[24:35](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1475s) into a new index in open

[24:37](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1477s) search called sampled logs. So we now have

[24:39](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1479s) two indexes, we have the main one

[24:42](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1482s) that stores all of our logs, and then we have

[24:44](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1484s) the sampled logs that don't just contains

[24:46](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1486s) a subset.

[24:47](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1487s) But

[24:48](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1488s) with the the the subset of of

[24:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1490s) logs

[24:51](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1491s) we're not able to do semantic search yet, right?

[24:54](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1494s) We need to do some configuration

[24:55](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1495s) on the open search site to be actually

[24:58](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1498s) able to do this kind of semantic

[25:00](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1500s) search. So let's do that

[25:02](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1502s) together. The

[25:06](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1506s) way I'll do that is using

[25:08](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1508s) the open search dev tools and if you're not

[25:10](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1510s) familiar with open search so much it's

[25:12](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1512s) basically um a very

[25:14](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1514s) uh lightweight developer environment

[25:16](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1516s) where you have

[25:18](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1518s) HTTP requests on the left hand side

[25:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1520s) and the result of those requests on

[25:23](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1523s) the right hand side and we can just kind of fire

[25:25](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1525s) off HTP requests right and see what

[25:27](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1527s) they come back with.

[25:29](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1529s) Now with setting up semantic Search there are

[25:31](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1531s) 3 steps involved and we're gonna walk

[25:34](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1534s) through them one by one.

[25:35](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1535s) The first one is we need to

[25:38](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1538s) connect Amazon OpenSearch Service

[25:41](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1541s) to Amazon Bedrock because Amazon Bedrock

[25:43](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1543s) hosts the actual embedding model that we need,

[25:45](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1545s) uh, as I said before,

[25:47](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1547s) and OpenSearch will be the database

[25:49](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1549s) and it will also do the communication

[25:51](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1551s) to Bedrock on our behalf.

[25:55](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1555s) Now the requests I'll fire off

[25:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1557s) here are a pretty boilerplate.

[25:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1559s) I'm not going to dive too much into

[26:01](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1561s) details here.

[26:03](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1563s) What we first need to create in

[26:05](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1565s) OpenSearch is a is a connector to Amazon

[26:07](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1567s) Bedrock, and we will specify the

[26:09](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1569s) model here that we want to use in Bedrock.

[26:13](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1573s) And

[26:14](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1574s) then we're gonna take this connector ID

[26:17](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1577s) that OpenSearch generated and

[26:19](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1579s) put it into our

[26:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1580s) register

[26:22](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1582s) call here, but we also need to create

[26:24](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1584s) this uh so-called model group and

[26:26](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1586s) we'll also take that ID and put it into

[26:28](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1588s) our register call. I said, as

[26:30](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1590s) I said, I'm going, going through that a bit

[26:32](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1592s) quicker. It's all in the GitHub just

[26:34](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1594s) if you want to follow up a bit more in detail.

[26:38](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1598s) Now when registering the model we get this

[26:40](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1600s) model ID which we'll be

[26:42](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1602s) using for the remainder of

[26:44](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1604s) this section.

[26:46](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1606s) We need to deploy this model first

[26:48](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1608s) so it's known throughout our open search

[26:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1610s) domain

[26:51](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1611s) and then we can actually go and

[26:53](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1613s) predict, which means we're testing

[26:55](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1615s) this model now.

[26:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1617s) And the cool thing is we're now

[26:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1619s) talking still to the open search API,

[27:01](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1621s) right, so through the open search API.

[27:05](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1625s) This will call Amazon

[27:07](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1627s) Bedrock under the hood and

[27:09](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1629s) give us a response again through the Open

[27:11](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1631s) search API, so the two systems are

[27:13](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1633s) now connected with each other.

[27:17](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1637s) And this embedding model, if you've

[27:19](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1639s) never seen this before, comes back with this

[27:21](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1641s) long list of floating point numbers,

[27:24](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1644s) and this is the output that an

[27:26](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1646s) embedding model produces,

[27:27](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1647s) and this

[27:28](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1648s) in a mathematical way encodes

[27:30](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1650s) the meaning of what I put in. So I

[27:33](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1653s) put in here what is the meaning of life,

[27:35](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1655s) and this question is now encoded

[27:37](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1657s) into this long list of floating point

[27:40](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1660s) numbers which is our vector embedding.

[27:44](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1664s) Cool, so we have established the connection

[27:46](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1666s) now, but our sampled logs index

[27:49](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1669s) is still not able to do semantic

[27:51](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1671s) search, so we need to configure the sampled logs

[27:53](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1673s) index to perform this embedding automatically

[27:56](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1676s) on our behalf to be able to do the

[27:58](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1678s) semantic search.

[27:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1679s) So let's go ahead and configure this index.

[28:04](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1684s) When I look at the index so far

[28:06](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1686s) and I'm just kind of spitting

[28:08](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1688s) out the definition of this index here,

[28:10](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1690s) um, we don't find anything in

[28:12](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1692s) terms of embedding in here, right? It's not

[28:14](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1694s) in there, it's just containing all of

[28:16](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1696s) our like plain lock lines.

[28:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1700s) What I would do first is create a so-called

[28:22](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1702s) ingest pipeline, which is a configuration

[28:25](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1705s) object that will enable OpenSearch to

[28:27](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1707s) automatically embed uh

[28:29](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1709s) log lines that are flowing into the index.

[28:32](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1712s) So I'm creating this embedding, uh,

[28:35](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1715s) this ingest pipeline.

[28:37](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1717s) And what this does

[28:38](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1718s) is, it's just processing all

[28:40](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1720s) of the uh the log lines that are

[28:43](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1723s) flowing in,

[28:44](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1724s) taking the log body.

[28:46](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1726s) And producing a new field called body embedding

[28:48](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1728s) that will store this floating point-like

[28:51](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1731s) array of floating point numbers that we saw

[28:53](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1733s) before, which is the vector embedding.

[28:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1737s) And then we are going to create

[28:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1739s) an index template for our

[29:01](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1741s) sampled logs which contains this pipeline,

[29:04](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1744s) so basically now saying please prepare

[29:06](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1746s) this index for automatically

[29:08](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1748s) embedding all of the log lines that are flowing

[29:11](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1751s) in and you see here that I also

[29:13](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1753s) specified this new body embedding

[29:15](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1755s) field which is a vector field in OpenSearch.

[29:19](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1759s) And what I'll then do is I'll just delete

[29:21](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1761s) the sample logs index,

[29:23](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1763s) and what's happening now under the hood is

[29:25](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1765s) that open search ingestion will

[29:27](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1767s) continue to ingest data into this index

[29:31](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1771s) and open search, since the index does not

[29:33](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1773s) exist, it will recreate it automatically

[29:36](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1776s) applying the configuration that we've set up

[29:38](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1778s) here. So now the index will be recreated

[29:41](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1781s) using all this embedding pipeline and the new embedding

[29:44](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1784s) field. So

[29:46](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1786s) let's have a look at this sample

[29:48](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1788s) logs index now, it's not yet found, so

[29:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1790s) apparently open search ingestion has

[29:52](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1792s) not ingested new log lines

[29:54](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1794s) yet. Let me

[29:56](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1796s) repeat that a few times.

[29:58](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1798s) Should usually take just a few seconds, but

[30:00](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1800s) sometimes it can take a bit more.

[30:10](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1810s) And there it is back up and when I now

[30:12](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1812s) search for embedding,

[30:14](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1814s) we have this body embedding field here

[30:17](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1817s) that uh is now part of my index

[30:19](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1819s) definition.

[30:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1820s) And when I go down here,

[30:22](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1822s) I also have this pipeline as

[30:24](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1824s) part of my index setting.

[30:26](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1826s) So what's now happening exactly what I wanted,

[30:28](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1828s) all of the new log lines that are flowing in

[30:31](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1831s) are automatically embedded by

[30:33](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1833s) OpenSearch using Amazon Bedrock.

[30:37](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1837s) And this is the last piece of set up I needed

[30:39](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1839s) to do. I can now perform semantic

[30:41](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1841s) search on this index.

[30:43](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1843s) Now we've been talking or I've been talking so

[30:45](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1845s) much about setting this up that it's worth

[30:47](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1847s) kind of recapping what the value of

[30:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1850s) this is actually. So let's take a

[30:52](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1852s) step back.

[30:53](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1853s) Remember we have this 504 gateway

[30:55](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1855s) timeout.

[30:56](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1856s) I know

[30:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1857s) that when there's a 504 gateway

[30:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1859s) timeout. It indicates that

[31:01](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1861s) something just takes very long to process,

[31:04](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1864s) right, kind of that's what I know, right? I

[31:06](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1866s) don't know anything of rate limiting.

[31:08](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1868s) I don't know any

[31:09](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1869s) exceeded or acute or anything. I

[31:11](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1871s) don't know how the specific log line

[31:13](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1873s) would look,

[31:15](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1875s) but I have, um, an idea that

[31:18](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1878s) something is just taking very long to process.

[31:22](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1882s) So let's do that. Let's search

[31:24](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1884s) so I can put in something very vague here. I

[31:27](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1887s) can ask for something like

[31:29](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1889s) uh something is taking too long, and I can

[31:31](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1891s) do a semantic search for that to

[31:33](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1893s) find log lines that are

[31:35](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1895s) semantically relevant for this query.

[31:38](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1898s) So let's have a look what it came back with.

[31:41](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1901s) And it's exactly again the shared

[31:43](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1903s) shipping service that we saw before,

[31:45](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1905s) right? And it's found the log

[31:47](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1907s) line rate limit exceeded request queued,

[31:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1910s) so you see

[31:51](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1911s) that lexically

[31:53](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1913s) those things are not related, right?

[31:55](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1915s) Some is taking too long is not

[31:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1917s) contained anywhere in this log line, but

[31:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1919s) in meaning in semantics they're very

[32:01](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1921s) similar to each other.

[32:03](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1923s) So I've now gone from a kind of a blank

[32:05](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1925s) page problem. I have no idea what to even

[32:07](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1927s) look for.

[32:08](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1928s) I've gone to the log entry that

[32:10](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1930s) is uh that is

[32:13](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1933s) going into the right direction, right? So now I can

[32:15](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1935s) have a deeper look at my shipping service

[32:18](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1938s) to figure out what exactly that problem

[32:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1940s) could be. OK,

[32:25](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1945s) so having finished our semantic

[32:27](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1947s) search, let's, um, let's do the

[32:29](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1949s) 3rd part of the session

[32:31](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1951s) and do everything together, natural language

[32:33](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1953s) processing and semantic search, bring it

[32:35](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1955s) all together using moderate context

[32:37](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1957s) protocol or MCP.

[32:41](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1961s) Cool, thank you, Yuling.

[32:44](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1964s) So as Julie had mentioned, so it's

[32:46](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1966s) really kind of the latest and greatest, right? So

[32:48](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1968s) how can we have an agent,

[32:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1970s) um, process these particular

[32:53](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1973s) searches for us really kind of.

[32:54](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1974s) Um, with a prompt, right, how can we use

[32:56](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1976s) that same NOP or that

[32:58](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1978s) prompt to get information back, right?

[33:01](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1981s) How can we use it as a tool in order to,

[33:03](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1983s) uh, interrogate,

[33:05](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1985s) um, that particular open search service, right?

[33:07](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1987s) And as we are moving into kind of that agentic

[33:09](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1989s) framework, and I'm sure you're hearing throughout the, the,

[33:12](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1992s) the conference, what is that agentic enterprise

[33:15](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1995s) or what is that agentic framework look like, right?

[33:17](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=1997s) So we have standalone, um, agents,

[33:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2000s) we have, um, autonomous agents and things

[33:22](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2002s) like that, right?

[33:23](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2003s) So what we're doing is we're gonna use Qiro CLI

[33:26](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2006s) as our as our client.

[33:28](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2008s) What we're gonna do is we're going to talk to

[33:30](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2010s) you or interact with an MCP server

[33:32](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2012s) that we've actually went ahead and and built out,

[33:35](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2015s) um, in terms of Python.

[33:37](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2017s) And then from there it actually has all

[33:39](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2019s) of the scaffolding that Yuli had talked

[33:41](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2021s) about in terms of being able to use the

[33:43](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2023s) model, use the embeddings,

[33:45](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2025s) and then go ahead and, and use that reasoning,

[33:47](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2027s) and then bring back a particular response,

[33:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2030s) um, and this was all kind of connective tissue,

[33:53](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2033s) um, kind of leading up to this or, or

[33:55](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2035s) delivering this piece overall.

[33:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2037s) What I'm gonna do now is I'm gonna go into

[33:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2039s) the configuration file in terms of

[34:02](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2042s) the actual MCP server itself.

[34:04](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2044s) But again, in the gist itself it has

[34:06](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2046s) really kind of that that scaffolding of how you would

[34:08](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2048s) set it up,

[34:09](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2049s) how you would configure it in Kiro CLI,

[34:12](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2052s) so you know if you're kind of wanting to dive a

[34:14](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2054s) little bit deeper in those settings of that configuration,

[34:17](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2057s) it's in the gist. So we'll share it

[34:19](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2059s) up there, um, and you can go ahead and look at

[34:21](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2061s) it and try it out or kick the tires on it.

[34:31](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2071s) I'm a huge fan of Clear if nobody's noticed.

[34:38](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2078s) Ah. So I'm gonna just go into

[34:41](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2081s) the file itself in terms of the

[34:43](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2083s) um where the actual downloads is

[34:45](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2085s) or where.

[34:49](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2089s) Where we have that MCP server.

[34:55](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2095s) It's kind of painful for you guys to watch me type here.

[35:08](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2108s) Goodness gracious.

[35:11](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2111s) Let's see here.

[35:18](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2118s) Uh, it doesn't say it's there. Sorry guys on that

[35:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2120s) one. We'll

[35:24](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2124s) pop in here. Just add a main main

[35:26](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2126s) dot pi in the end.

[35:28](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2128s) I'm a cat, not a CD. Oh, that's

[35:30](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2130s) right. There

[35:35](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2135s) we go, perfect.

[35:39](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2139s) So what we have here is just kind of the set

[35:41](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2141s) up, uh, in terms of where we're setting

[35:43](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2143s) this up or actually the main dot pie itself.

[35:45](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2145s) So what we have is we have our, our really kind of our import

[35:48](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2148s) vote to 3 client right from there we're

[35:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2150s) actually referencing the fast MCP

[35:52](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2152s) for that particular component.

[35:53](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2153s) Then we're walking down and kind of the open search

[35:56](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2156s) connection. There's documentation that that's

[35:58](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2158s) out there that really kind of brings this to

[36:00](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2160s) bear or you can actually look at and reference.

[36:02](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2162s) So what we have here is we have the host, which is

[36:04](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2164s) the actual uh search

[36:06](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2166s) or it's actually the open search endpoint that

[36:09](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2169s) we're gonna interrogate or hit.

[36:10](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2170s) We have the region that's there as well. Um,

[36:13](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2173s) services, yes, of course, credentials

[36:15](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2175s) we use the session and things like that which

[36:18](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2178s) is in the AWBS account so you can

[36:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2180s) access it, um, use that SIGV4

[36:23](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2183s) access and, and, and go ahead and

[36:25](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2185s) being able to, um, uh,

[36:27](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2187s) get that information or query that information.

[36:30](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2190s) Then what we have is we use the open search

[36:32](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2192s) client here

[36:33](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2193s) based on the Python piece overall

[36:35](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2195s) in terms of that client, right?

[36:37](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2197s) So it's actually calling it, it's using the host

[36:39](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2199s) and using the variables above in

[36:41](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2201s) order to make that connection or hit that

[36:44](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2204s) end point.

[36:45](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2205s) Then what we have here is we're actually describing

[36:47](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2207s) the MCP server itself.

[36:49](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2209s) Uh, fast MCP seems to be,

[36:51](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2211s) um, within Python

[36:53](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2213s) the best way to go ahead and do that, uh,

[36:55](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2215s) that query, right? Or do that interrogation

[36:58](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2218s) of that endpoint,

[36:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2219s) um, and then from here

[37:01](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2221s) if we really look at it, it really just kind of boil

[37:03](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2223s) it down. Is we can just

[37:05](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2225s) put in a few lines of code

[37:08](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2228s) um for that MCP server to

[37:10](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2230s) actually do a really dynamic

[37:12](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2232s) fetch of that particular model or that embedding

[37:15](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2235s) model that Yuli actually set up right initially

[37:18](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2238s) so there really isn't a whole lot of work we

[37:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2240s) already have the plumbing that can actually make that connectivity

[37:23](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2243s) or talk to that end point

[37:25](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2245s) and what we have here is we actually have

[37:27](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2247s) just a stanza here

[37:29](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2249s) in terms of MCP tooling.

[37:30](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2250s) That we can say hey look we want you to do that

[37:32](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2252s) semantic search

[37:34](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2254s) and we want you to go ahead and give this that

[37:36](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2256s) body information coming back and

[37:38](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2258s) as Julie displayed before we

[37:40](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2260s) actually have that embedding that will actually

[37:42](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2262s) return a response

[37:44](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2264s) based on that very uh finite

[37:46](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2266s) query on those 10 logs, right?

[37:49](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2269s) Um, and then we also have the model ID

[37:51](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2271s) so dynamically we're actually pulling in that

[37:53](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2273s) that model ID so that we can use it and leverage

[37:56](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2276s) it within the semantic search.

[37:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2279s) And again, as you referenced before, we have the sample

[38:01](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2281s) logs here that we could actually leverage and utilize.

[38:08](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2288s) So what I'm gonna now do is I'm gonna go ahead and kick

[38:10](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2290s) off our client right? um

[38:12](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2292s) here the MCP client from there

[38:14](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2294s) so we'll clear that out.

[38:25](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2305s) So what this is doing is it's actually going into

[38:27](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2307s) the MCP. JSON file or

[38:29](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2309s) settings file, and what it's doing is it's setting

[38:31](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2311s) it up, right?

[38:32](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2312s) So it's reading all of the MCP servers

[38:34](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2314s) that I have configured already

[38:36](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2316s) and so one of them is the OS logs or it's

[38:38](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2318s) the main pie, right, that's actually coming through.

[38:41](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2321s) And as you can see it went ahead and welcomed

[38:43](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2323s) and it actually loaded it successfully. You

[38:45](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2325s) can actually go in and type MCP

[38:47](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2327s) itself and you can validate that I

[38:49](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2329s) actually did load or it did actually come into your

[38:51](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2331s) environment or within your MCP

[38:54](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2334s) client through Quiro.

[38:55](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2335s) So what I'm gonna now do is I'm gonna just type in

[38:58](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2338s) a a a particular

[38:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2339s) uh input or an NOP input

[39:02](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2342s) and see what I actually get right

[39:04](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2344s) um from there

[39:05](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2345s) so I'm gonna come down, um, my cheat sheet one

[39:07](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2347s) more time here.

[39:09](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2349s) What I'm gonna do at that point is

[39:11](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2351s) ask it.

[39:14](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2354s) Oh goodness gracious, no

[39:15](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2355s) no no no no no.

[39:22](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2362s) And I'm going back to a little bit to what I

[39:24](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2364s) know in terms of the exceeded rate limits.

[39:26](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2366s) Yuli said just sight unseen we can actually get it,

[39:29](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2369s) but again, I wanna see what we're gonna get back

[39:31](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2371s) with a very um targeted

[39:33](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2373s) um

[39:34](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2374s) NOP or or prompt.

[39:41](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2381s) So again on everything here we'll go ask, do

[39:43](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2383s) we really trust it or do we want it to do what we say

[39:46](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2386s) it wants to do

[39:47](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2387s) so we'll push it through here again.

[39:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2390s) And here we go. So it's actually showing us

[39:52](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2392s) here it found a 500 rate limit logs

[39:54](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2394s) from the shared shipping service.

[39:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2397s) So through the whole talk, you know, we've kind of been,

[39:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2399s) you know, dancing around. OK, how do we really kind of, um,

[40:02](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2402s) close the funnel or actually start to hone in

[40:04](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2404s) on the particular root cause,

[40:06](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2406s) and then we see it again, right? So

[40:08](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2408s) it's more or less, it's, it's a problem with the shared

[40:10](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2410s) shipping, um, and it's actually a noisy

[40:12](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2412s) neighbor issue, uh, and causing that component

[40:15](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2415s) altogether.

[40:16](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2416s) So we kind of have confirmation at this point.

[40:18](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2418s) So what we also wanna do is how do we remediate

[40:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2420s) this right?

[40:21](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2421s) so we can just ask it directly,

[40:24](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2424s) um, remediate issue

[40:26](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2426s) for me.

[40:28](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2428s) And so Kiiro and and really

[40:30](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2430s) kind of the whole AI component here

[40:32](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2432s) will go ahead and just kinda give me suggestions on

[40:35](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2435s) what they can do in order to remediate

[40:37](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2437s) this right

[40:38](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2438s) again you know if I didn't really know or

[40:40](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2440s) understand what was actually going on

[40:42](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2442s) um.

[40:44](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2444s) With that piece,

[40:45](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2445s) um, it would actually show me exactly what

[40:47](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2447s) could be, what could be going on in, in that

[40:49](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2449s) so what it's seemed really at this point, let's

[40:52](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2452s) see. So

[40:55](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2455s) it's actually scaling itself right? so it's

[40:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2457s) actually go ahead and it's actually scaling

[40:59](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2459s) this, uh, shipping, right?

[41:02](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2462s) So it's actually going through and it's scaling

[41:04](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2464s) it for me,

[41:05](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2465s) um, overall

[41:06](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2466s) so you know it actually went ahead and looked

[41:08](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2468s) and says hey the recommendation is scaling

[41:11](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2471s) that that that shipping shared service

[41:13](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2473s) then if we go ahead and scale it.

[41:15](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2475s) Will it go ahead and remediate the problem?

[41:17](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2477s) So it went ahead and gave us that, or it kicked off

[41:19](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2479s) for us, right? And we went ahead and said, OK, trust

[41:21](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2481s) it, go ahead and do it, right?

[41:23](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2483s) Very similar. Like, are you sure you wanna delete?

[41:26](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2486s) Kind of the same thing, right? You wanna make sure that

[41:28](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2488s) that you're adhering to it and, and kind of responding

[41:30](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2490s) to it. So basically it actually

[41:32](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2492s) scaled, so it actually gives you actions here,

[41:35](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2495s) scaled shipping deployment from 1 to 5 replicas,

[41:37](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2497s) right? And it did a few other things there.

[41:39](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2499s) Um, so this is kind of what it fixed here

[41:41](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2501s) distributions, and it gives you kind of uh an overview

[41:44](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2504s) of what it did and what it didn't do at that point.

[41:47](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2507s) So what we're gonna do at this point is we're gonna go

[41:49](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2509s) back into the application to see if it

[41:51](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2511s) actually did did prove to be successful

[41:53](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2513s) or not, right?

[41:55](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2515s) So, um, what we'll do is we'll go

[41:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2517s) back out,

[41:58](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2518s) um, on our command line

[42:00](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2520s) and we'll see, um, what

[42:02](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2522s) actually happened, if anything, so we'll quit,

[42:05](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2525s) uh, that piece.

[42:07](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2527s) You know, forward again,

[42:10](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2530s) so we'll just take a look at the

[42:12](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2532s) shared, uh, services real quick and

[42:14](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2534s) see if it actually did. It did actually scale

[42:16](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2536s) it so we can say yes, that actually happened

[42:19](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2539s) and Kiiro did what we really kind of

[42:21](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2541s) recommended it could do to solve that problem.

[42:24](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2544s) That we wanna do is come over here we wanna port

[42:26](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2546s) forward so as Julie had uh kicked off

[42:28](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2548s) before we just port forward here.

[42:31](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2551s) On one of these front ends and then we'll go and

[42:33](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2553s) test the application to see if that application

[42:35](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2555s) is functioning the way we wanted it to.

[42:38](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2558s) So we'll go back here to the hotel,

[42:41](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2561s) we'll go ahead and exit out of that,

[42:43](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2563s) and we'll continue shopping.

[42:45](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2565s) We'll come back in and we'll actually choose

[42:47](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2567s) this particular product, right?

[42:49](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2569s) We'll just kind of stay with what we wanted to

[42:51](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2571s) before, um, of course our, our, you

[42:53](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2573s) know, nephew wanted this particular thing, so

[42:56](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2576s) let's see if we can actually complete it or get it done.

[42:58](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2578s) So we'll add it to the cart as we did before.

[43:01](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2581s) We'll walk it down here. Everything else is pretty much

[43:03](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2583s) the same, and we'll see if we can actually place that

[43:05](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2585s) order boom,

[43:06](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2586s) successful.

[43:07](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2587s) So now we've really kind of have full circle,

[43:10](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2590s) right? So we actually went through and we looked

[43:12](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2592s) at it from NLP,

[43:13](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2593s) really kind of narrowed it.

[43:15](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2595s) We went from the semantic search, not really

[43:17](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2597s) understanding, um, what could be the issue, but

[43:19](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2599s) then we're actually homing in more and more in

[43:21](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2601s) terms of what the needle in the haystack would be.

[43:23](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2603s) And then we used MCP.

[43:25](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2605s) It's kind of an external or an agent tool

[43:27](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2607s) to actually give us that same confirmation to actually

[43:29](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2609s) fix it and, and move forward.

[43:31](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2611s) So, um,

[43:33](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2613s) with that, I'll go ahead and hand it back over

[43:35](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2615s) to Yuli to take us home.

[43:46](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2626s) So this uh already brings us to the

[43:48](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2628s) end of the session.

[43:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2630s) This is the GitHub gist we

[43:52](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2632s) uh promised a few times during the session

[43:54](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2634s) so do uh check this out uh

[43:56](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2636s) it contains all of the

[43:58](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2638s) code snippets,

[44:00](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2640s) documentation references, and other

[44:02](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2642s) references, explanations, and so on

[44:04](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2644s) that we talked about during this session.

[44:07](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2647s) Um, let's have a look at the time. So

[44:09](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2649s) I think we have time for one or two spontaneous

[44:12](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2652s) questions. So if any one of you has like, uh,

[44:14](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2654s) wants to have a

[44:16](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2656s) question for the room

[44:17](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2657s) that we can answer, uh, you can do that now

[44:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2660s) if you wanna raise your hand.

[44:21](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2661s) Anyone here?

[44:23](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2663s) OK, yeah.

[44:28](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2668s) Uh-huh, um, is

[44:30](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2670s) it the This is.

[44:36](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2676s) OK, so just repeating the question for everyone. The, the

[44:39](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2679s) question was for the connection between open

[44:41](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2681s) search and Bedrock,

[44:42](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2682s) whether we can have a cross region

[44:44](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2684s) connection for that. And yes, in fact you can,

[44:46](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2686s) yeah, you can, you can do that, uh, in

[44:49](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2689s) our case we did it same region but you can

[44:51](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2691s) have it cross region as well. Basically how

[44:53](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2693s) it works is

[44:54](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2694s) that, um, open search is assuming a role

[44:56](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2696s) on your behalf and just, um,

[44:58](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2698s) calling the Bedrock service, uh, end point

[45:00](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2700s) on your behalf, yeah.

[45:03](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2703s) Any other questions from the op side of the house?

[45:06](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2706s) Go ahead. Just

[45:12](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2712s) a question when you're demoing all those tools and I was showing you what part was that tools? Is that part of open?

[45:16](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2716s) Yes, it's part is a standard part of

[45:18](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2718s) open search dashboards. Um, so,

[45:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2720s) uh, open search, uh, is fully

[45:22](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2722s) HTTP API based, right? Uh,

[45:25](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2725s) so, uh, in contrast to other

[45:27](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2727s) search tools that are out there, it's fully HDP

[45:29](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2729s) API,

[45:30](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2730s) and this is, uh, kind of the.

[45:33](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2733s) Main kind of playground that

[45:35](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2735s) that people use in open search right to to

[45:37](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2737s) play with different uh play with different

[45:39](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2739s) end points yeah so this is not nothing new this

[45:42](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2742s) has been around for pretty much ever yeah.

[45:46](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2746s) Cool. OK, so, uh, with that, let's,

[45:48](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2748s) uh, close off the session. Uh, thanks a lot for

[45:50](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2750s) spending your valuable time with us. Uh, we can

[45:52](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2752s) take further questions in the hallway, by the

[45:54](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2754s) way, we just need to move out in a bit for

[45:57](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2757s) the next speakers.

[45:58](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2758s) Uh, happy to, to take any questions,

[46:00](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2760s) um, offline.

[46:02](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2762s) Um,

[46:03](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2763s) please do fill out the session survey.

[46:05](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2765s) I know everyone reminds you of that. Uh, please

[46:07](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2767s) do for this session as well, especially if you

[46:09](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2769s) liked it. We read every single piece of feedback

[46:12](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2772s) that you put in there, so please, uh, do fill

[46:14](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2774s) that out.

[46:15](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2775s) Um, have a great rest of reinvent,

[46:18](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2778s) um, enjoy the conference and

[46:20](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2780s) hopefully see you all soon.

[46:21](https://www.youtube.com/watch?v=KhbLaC9vw-U&t=2781s) Thanks folks.

