# AWS re:Invent 2021 - Enabling a frictionless and secure payment experience at ETS (sponsored by PwC)

[Video Link](https://www.youtube.com/watch?v=CjbqcbkU0so)

## Description

In this session, learn how PwC and ETS, the world’s largest private educational testing and measurement organization, developed a secure cloud-native payment processing solution that offers a frictionless payment experience for ETS’s global customers. Relying on an event-driven architecture and an extensive list of AWS serverless and managed platform services, ETS is now positioned to use the benefits of operating a scalable, flexible, and cost-optimized enterprise-grade payment processing system. The new solution has helped enable faster turnaround times and speed to market. This presentation is brought to you by PwC, an AWS Partner. Speakers: Gokul Raghuraman (PwC) and Brian Hersh (ETS)

Learn more about re:Invent 2021 at https://bit.ly/3IvOLtK

Subscribe: 
More AWS videos http://bit.ly/2O3zS75 
More AWS events videos http://bit.ly/316g9t4

ABOUT AWS
Amazon Web Services (AWS) hosts events, both online and in-person, bringing the cloud computing community together to connect, collaborate, and learn from AWS experts.

AWS is the world’s most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally. Millions of customers—including the fastest-growing startups, largest enterprises, and leading government agencies—are using AWS to lower costs, become more agile, and innovate faster.

#AWS #AmazonWebServices #CloudComputing

## Transcript

Good morning, everyone. Welcome to day one of re:Invent in 2021. I'm very excited to be here. I'm Gokul Raghuraman from PwC, and I'm joined by my colleagues Mrinal and Brian, who will be speaking to you very shortly. Today, the topic that we are gonna cover is our journey and our experience, and we wanted to share that with you as to how we worked with ETS to build a payment solution, a seamless experience for ETS customers. Now, before we get started, just wanted to call out very quickly that while the three of us are here, behind the scenes, obviously we didn't turn up here by ourselves and built a solution. There was a lot of people who helped us build a solution, both from PwC, as well as ETS, so we want to acknowledge that. The topics that we wanted to cover today would be what are some of the common challenges that you see or that you've seen our customers face, whether it's in the payment space, in any other line of business application, what are the challenges that they face today? How does a cloud-native solution architecture help solve some of those challenges? What kind of challenges we face along the way, our learnings along the way, and how we course corrected over the period of time where we started to where we are today. That's, in a nutshell, what we are gonna cover today. Along the next 60 minutes, my colleagues will talk to you about some of the specific considerations that we had put in place as we built the solution and how we went about operationalizing the solution and where we are today and what the future looks like for us. So, that said, wanted to open by talking a little bit about what are some of the common challenges that we see that our clients face in the marketplace? This is the four that we've shown here are primarily the most common scenarios that we've seen our clients face, right? They either have a scenario where they wanted to focus on building solutions and deploying them and releasing them at the speed at which you could actually experience in the cloud the capabilities provided by service providers like AWS. Perhaps they are interested in focusing most of their energy on actually building applications that are either revenue generating, customer facing applications and not having to worry about managing hardware, managing infrastructure and leave that to people who are dedicated and who are behind the scenes who are helping stand up the solution. The other aspect that comes up a lot is there's a lot of change happening in the marketplace. Every company is innovating and you have a very fixed amount of time to be able to reach the market segment, and that was one of the scenarios that we had at ETS as well. We had, like we had a time limit imposed on us. We had a very short amount of time, we had a very limited set of resources and we had to make the best use of it to be able to stand up a solution within a certain amount of time. So, we'll talk a little bit about what some of those factors were in detail, but at the high level, these are the common challenges that we face whenever we are trying to stand up a cloud-native solution in the cloud. Now, how does cloud-native architecture help? The founding principles at a highest level are these services are managed. When AWS originally started, there was a lot of platform services that used them for compute and storage, but eventually now AWS has a depth and breadth of services that allow you to build solutions very, very quickly and be able to test your hypothesis and then release to the production environment, so that's the beauty of the managed services that are already available there that we were able to take advantage of for our faster release cycles to test them and to be able to scale at the speed and the capacity that you would have normally not been able to. We also, as part of managed services, do one thing that we learned over a period of time and we implemented here was the need to automate right from the get-go, so every sprint, there was not just the application development and testing, but we had the checks and balances in place from a platform as well as from an application perspective to be able to automate most of our pipelines and be able to test them on a sprint by sprint basis. The, what it also allows you to do is to be able to scale at a rate at which you would typically not be able to if you had gone in with managing your own hardware and software, so we were able to put in the right controls and design patterns in place to be able to scale, to be able to roll back, and we heavily leveraged feature toggles to be able to make the solution flexible and customizable. Now, I wanted to pass it on to Brian, who will talk about ETS's journey and where they are. Hello everyone, Brian Hersh, I'm from ETS. Many of you might know ETS. You may have taken one of our very many tests. We have the practice tests, the GRE, TOEFL exams. We're also a heavy research company, largest private-based educational research company in the world, and with that comes many challenges where we're all over the world in many, many, many countries. One of the funny things our partners tell us is they work with retail companies and other types of payment, companies that take payments. ETS has presented a very major challenge for them because culturally, our company is diverse, our product is diverse, our tests are diverse, everything is diverse, and that creates an interesting challenge. So, you can see here, we have 50 million tests that we deliver annually in more than 9,000 locations, and so one of the challenges we have is keeping up with the marketplace, and in years past, we struggled with those challenges, and so one of the things we did was we set out to reinvent our payment process, and we worked together with PwC to come up with what was just a really amazing experience, and every day that goes on, we experience amazing benefits that are, how could I say? Lightspeed. It's just very, a very good journey. So, where were we? ETS had a vendor who was very static in nature, so one of the things that we were limited to was what payment methods did they have? We were basically tied with those. Our lines of business would ask, hey, can we try this payment method, or can we go after this market with these new payments? Because let's say the payments that we're accepting are very US centric, so how do we get to that global rollout and be able to support people throughout the world? And that was a really tough challenge. Other things we struggled with, we had minimal control over our outages and upgrades. The vendor did whatever they want. We had a hosted solution, but at the end of the day, we had very little control over what was going on. That was all happening based on what was going on in their data center, how they were handling the maintenance of our application. So ETS had been thinking, how can we get more flexible? How can we take over more control without having staff of hundreds of people to maintain and support our global presence around the world and be able to take payments in a real-time fashion? So, one of the things we also found was the enhancements, they were costly and they were very slow to occur. Sometimes we would wait six months to a year to get enhancements to the system, and that wasn't something that was, well, wasn't happening nicely for our customers. So customers would ask us for different things, and in IT, our customers are our business units and ETS has different silos of different business units, so each of those business units kind of operates slightly independent of another, so the TOEFL folks may have different requirements than GRE or teacher licensure within praxis, so each of these units have different needs, and so we had to find a way to be able to provide that in a more timely fashion. Also, cross-organizational communication. One of the jokes is we're trying to give this presentation and you have PwC and ETS, two highly technical companies trying to coordinate with the AWS folks to put the presentation together. It's basically like rocket science, and imagine trying to communicate all your requirements and your features and your infrastructure needs to a vendor who also has other challenges, right? Just a silly presentation, not a silly presentation, but a somewhat simplistic presentation that we're trying to give today, just illustrates how difficult that type of thing can be. And the system wasn't scalable, so seasonal challenges prevent or present different opportunities for ETS to reach more test-takers around the world during certain peaks and troughs. The system wasn't very responsive, because it was hosted in a data center and because it was physical infrastructure or hardware or constraints based on a contractual nature. We couldn't just scale up very easily, so those were things we had to pre, premeditate or have discussions with our vendor about those types of things. So, these were the things that we were mainly looking for when we were trying to build a system, problems we were trying to solve, and at the same time with all of this, ETS was going through a technological change. We're basically adapting to the new world, shifting our entire platform on to AWS corporate, just throughout the entire company, also moving to an Agile-based development model, so lot of things happening all at once. Okay, now I'd like to introduce Mrinal. You wanna, oh, you're gonna? All right, no worries. So, I think I'll take a couple of minutes to quickly talk through, before we get into the technical architecture, what were some of the principles or the guiding principles that we use before we designed the solution? AWS has a lot of services. Great, you can leverage them. We decided to go with managed services. That was great, but from an architectural standpoint, we had to put certain principles and building blocks in place so that everybody understands what is the expectation and how we work together as we, like Brian said, this is, there's a global customer base, there's different business units looking for the standardized solution, so we first set about thinking through how are we going to completely re-architect the existing solution? The existing solution was vendor managed. We were building a solution from the ground up, and then we were gonna stand up in AWS. So we looked at the payment process as a whole, and we started at all the sub-processes that our payment flows actually required. So how does the customer come, and what kind of payments is the customer looking to do? What kind of products is the customer looking to purchase and what kind of features and functionalities does a typical payment flow have? And so there's an order processing, there is a payment solution that's happening, there is a reconciliation that happens in the backend, there is the refunds that happen, so there's a number of different flows happen, so we started breaking down everything, that huge monolith into a sequence of sub-processes. The minute we did that, we were able to identify that a lot of these can actually work independently without having to rely on each other, so that was one of the founding principles that we set. We want to make it loosely coupled. We want it to have fault tolerance by isolation in our environment, so we went with the microservice-based approach. We also wanted to make sure, the next question, obviously, once you've decided on microservice is what is the medium of communication, how are you gonna actually communicate, right? Is it gonna be synchronous or asynchronous? What are we gonna do? We, based on the flow and the use cases that we had then charted out, we then identified that an event-based mechanism is the best means to be able to implement the end-to-end payment journey without being able to rely on different parts of the same flow, so we went with an event-based approach that, again, helped us from a fault tolerance perspective. It helped us to be able to manage features independently of each other. We were able to test out different features at different points in time, so that, all that helped the microservice and the human-based architecture set us the foundation for that, right, and when we did this, we actually did a, almost like a pilot tested out our hypothesis, we did one payment method, worked great, and then we started building at a larger scale, right? One of the things that we also did when we started out was we clearly had a deadline to hit. We, there was a need by which we had to have the system up and running, and there was a limited amount of capabilities or resources available in front of us to be able to put that in place. So we, at the get-go, we worked with the ETS team, the architecture team and their product team to think cloud-native first, right? So leverage the power of what is already available, speed up the process of setting up your platform and then very quickly building something on it and then testing on it, right? So we've went with, most of you will see when Mrinal talks about it, most of our capabilities are, were based on native capabilities that AWS provided. One of the motivating factors were also to make sure that we keep an eye on operational overhead, and this solution, after it's built, it needs to be managed, it needs to be cared for and fed for, so we wanted to keep that to a bare minimum as well, so that was one of the motivating factors that we looked at when we went cloud-native. We also want to, obviously, be in a position where we can very quickly swap features in and out, so we put on a lot of feature toggles that allowed us to do that. So, what were some of the key considerations that we looked at when we actually stood up the solution? The feature development, the backlog that came in was great, but we also had to have, like, the foundational set of building blocks in place. This was a payment solution. This was an internet facing solution, right, so you needed to have the right set of these kinds of functional capabilities in place to be able to run this at scale. So, as an example, this had PII data, this had PCII data, so our application needed a good means to be able to handle both kinds of information in the application, and you will see in the architecture how some of these services were designed to handle that security focused needs. We also wanted the ability to have support. This being a payment application, you want to be able to provide a vast number range of payment options that a customer wants to take advantage of. This might be using a credit card, this might be using PayPal, this might be just calling in and making the payment, so you need to take advantage or provide the user with the most number of options, and you need to make it look seamless in the background for the customer, so we had to put that resilience and those capabilities in place for you to be able to do that. So let's say a customer calls, and one of the payment methods is not available. The customer should seamlessly be able to pick another alternate payment method and still be able to go through with this order. This was a global, the customer base was global payments and orders would come in from anywhere in the globe, so, which means automatically, it's not just local currency, you're looking at international currencies as well, so the ability to support those was a big part in how the system was defined by these means of these microservices. We did leverage on, like, there was a number of, like Brian said, there was a, the upstream was maybe about 15 plus applications, which were being in a position to take orders and send all this to the downstream application, which is a payment solution, the standardized payment solution. You need a way to handle every single request, every single transaction, take it all the way to the payment, get back the confirmation number, and you still need a way to be able to trace it end-to-end, right? So observability was a huge factor. The golden signals of observability were put in place. We looked at end-to-end tracing, logging and monitoring, which we will cover shortly. The other motivating factor, as we thought through the solution, was the payment solution needs keep changing. There are new innovations in the market, new innovations that keep coming in, and as a company who's providing that or enabling the payment solution for its customers need to be able to take that in at a very quick pace without a lot of re-architecture that was required in the system. So again, we put in a lot of flexibility, configurability in the environment to make sure that the solution was easily maintainable and it could easily scale in the environment. So to do a deep dive, I'm gonna call Mrinal, who was the architect on the solution to talk us through the key factors and the considerations. Thank you, Gokul and hello, everyone. So, yeah, to explain the architecture, I'll take you through a use case. Let's consider a scenario where the user has filled out all the details, provided all the details, and then it clicks on the pay button. What happens then? The call first reaches our system via our combine, which performs the role of the web application firewall. It hits the API Gateway. The API Gateway uses custom Lambda phrases, because we are to integrate with our homegrown solution from ETS, which manages the tokens, so it essentially, it sent it over from the request, validates against ETS, which is the homegrown solution, and then sees whether it's a valid request or not, and then lets it through. Once it lets it through, it goes to the payment service, which is hosted in ECS Fargate. Now, the premium service has to be sent to a payment gateway, which is an external system, or a third party provided system. To that, it first needs to find out what's the URL and the credentials. Now, URL and all these kinds of things are stored in Parameter Store. Credentials are stored in Secrets Manager where it's rotated, so it gets from these sources, makes a call to the third party gateway, get a response, then it does some additional processing. So, what it does is it creates an event object, it populates all the request and response and all the transaction related details for the event object and puts it in place queues and then sends a response back to the user and user sees what happens to the payment and is redirected to the originating system or whichever system from the request came. Now, what happens to the event now, when you've got that event in our queue? We have a data service, which listens to this queue. It gets the event, it kind of extract the request and response, matches it, puts it into S3, which is one of the, which was one of the requests to early comment to archive all the question responses for future audits and everything. Then it creates a transaction record in the database. Again, database means that you need to know where the database is, where it comes from, Parameter Store, credentials, Secrets Manager where it's located and everything. Then, again, you're storing data in the database, which needs to be encrypted. How the keys are managed, we have new schemas for managing the keys. So after this transaction processing is done, there are a few more steps. So, we need to notify the parent on the upstream system that everything has gone through fine, so we have to send the post back, so data service puts another message in another queue with all the details, like what happened to the transaction, which system needs to be informed and everything, and there is one more system, which is listening to the queue. It gets the response, it reads the queue, gets the message, sees that, okay, this, this has to go to some other system, and then sends it. So, we have kind of given you an idea like, how we had implemented the wind-driven system, a loosely coupled set of microservices handling various aspects of payment. There are other use cases also. Like, for example, there are cases where we had to do batch processing, like for example, settlement records, which comes at an IT level for multiple transactions. What we did is we had a job schedule live in CloudWatch, which will trigger this, triggered the ETS job, which would pick up the file, process it and then update all the records. So this is the, what our architecture kind of, how it solves the payment flow, but there, obviously there are so many use cases, but this is one representative use case, we would say. Now, this is the design. We would go into a little bit detail, like how this particular design actually addresses the key areas, which opened up the work. First was availability. As you saw, most of the solutions that we used are AWS managed solutions, and the wonder of that is they come with high availability out of the box. AWS does it by distributing the underlying infrastructure across multiple availability zones. However, in certain scenarios or in certain services, they are a little bit of considerations. For example, when you're using Lambda or Fargate, like if you are attaching a VPC to your Lambda, you have to ensure that the subnets within the VPC are in multiple availability zone. That only ensures that your functions are distributed in multiple availability zones. But for most of the others, it comes out of the box. You don't have to do a lot of configurations, so that really helps. Another aspect of availability is generally distributing a system across multiple regions. Currently, the system is not designed to do it, but once the enterprise lays out its multi-region strategy, it's very easy to evolve this design to be distributed across multiple regions. Next is security. It's a payment application that is accessed, like, from worldwide customers, which stores PII data, so security is, was very, it was and is a very, very critical aspect of the entire design. So, let's go in layer by layer. So first, API access. How we secured our API access was using API Gateway. Again, there was a little bit of challenge here because we had to integrate with one of our custom solution to validate the token and see whether the incoming requests are valid. For that, we use Lambda operators, which kind of indicates with the homegrown solution, which is called Redis, and so it will take the token, validate the token against Redis and then forward the request only if it's a valid token. Next was encryption across various levels. So first is encryption for data in transit. We kind of enforced HTTPS at the load balancer as well as the API Gateway level, so that way, that kind of ensured that all the data in transit was encrypted. Moreover, we had one more additional layer of security wherein the request body coming from the incoming systems were encrypted using keys, which was mutually agreed upon between this payment gateway solution and the upstream system. Apart from that, since we are storing PII data, we also had additional comments of encrypting any data at rest using customer managed keys. How we were managing these keys, the UI manually uses keys using KMS, and KMS integrates very well with all the solutions that we are using, namely, sorry, namely S3, RDS, SQS, ElastiCache, Secrets Manager, so all these solutions integrates very well with KMS, and that enabled us to encrypt the data at rest using customer managed keys. Another aspect of it is how the, how we secured the AWS services as such, how did we secure AWS S3 bucket or SQS queue? How we did it was, as the design principle states, that this access should be provided at a very fine granular, like at a very low level, so we had individual roles created for each of the tasks that have provisioned, and the access to each of the resources were provided at that particular role level. So the access, the scope of access was limited to very, the funnel was very small. Moving on to the next, resilience. This was, again, one of our key considerations, and we had to take care of it right from the design level. We had, we did it in like two ideas or two angles, I would say. One is loose coupling. How we did that is we ensured that whenever we could use asynchronous communication between the two services, we used that using SQS queues. How we would monitor that is if there is a particular system which is at fault or which is facing issues, it gives that time to that system or service to recover without actually affecting the other systems. The other area was fault isolation, so when we, when we looked at the entire payment solution, we first broke it down into individual processes, like, the processes which can operate within itself and not, does not depend on any other processes, and then we created services for that. So what happens is if one of the processes goes wrong, the other process can still operate. And another thing that we did is we implemented feature roles where we could dynamically turn on and off features if there are any issues. So, I'll give you an example regarding that. So let's say today, we noticed that a particular type of transaction, let's just for namesake, let's use PayPal, payer transaction is facing issues with it. We have the capability in our system to turn off just the PayPal payment option. That will remove the PayPal option, even from the UI, and the user does not get to see the PayPal option at all, but all other types of payment, like the card and everything will work absolutely fine, and that gives us the time for our supporting industry to go back, look at what's exactly happening wrong in our system, fix it and then test it and then again, roll it back, and then we turn or turn it off automatically, sorry, turn it on, and the system is back to normal and there is zero downtime, literally. So yeah, let's, so yeah, these two kind of give us the capability to isolate the area of a problem, isolate the damage and then recover from it and then get the system back to normal as fast as we can. Next was scalability. Again, managed services to the rescue here. We are using Fargate and Lambda for most of our computation requirements, and these, in our experience, scale extremely well, so that kind of takes care of most of our scaling requirement. However, from our experience, we would strongly recommend performance testing your application. Every application's traffic patterns are different, scaling characteristics are different, so you should really do your application based on your scaling characteristics and your traffic pattern. AWS provides you all the tools, but it is our responsibility to you, in our application to make most of it. I mean, we did performance testing on our application. Based on the observations, we did a lot of changes, and that helped us tune our applications better. For example, we changed the CPU and the memory that was provided at the basic task level, ETS task level. We also changed the scaling thresholds based on how the application was, the amount of time it was taking to provision new tasks. We also changed the grace period for the load balancer health check, just so it does not conflict with the server startup times. So, once we did all that, our application was performing way better and it was able to handle the kind of loads that AWS was expecting. Apart from that, there's one more, one bit of performance testing. We validated that during the peak load, we were not violating any kind of thresholds, not the sort of quotas or any rate limitations that are actually imposed, so you need to test that, because you don't want to expose, you don't want to face that in your production, so it's better to face that and then either get those rating mutations increased or tune your application or design your application in a different way. Yeah, again, it's a enterprise application, so support is a big part of it, and to provide effective support, you need to know exactly what's going on in your system, not only at the infrastructure level, but also at a process level, like whatever is, what exactly happened to each and every transaction that went through your system. Now, observability generally consists of three pillars. I'll go one by one through each of them. So, first was logging. So we, our application, our system generated two types of log. One is the application log. Obligation log is noting the record of events that occurred in the system, so it will record something like this event occurred, this was the service that handled it, what's the timestamp, what's the details of it, even what was the outcome, was it a success or a failure, et cetera, and these application logs were pumped into Splunk, which kind of gave us the capability to search the logs, like effectively search the logs. The other type of log that our application do was the request and response log, so whatever requests and response we sent to our gateway, we logged them in our buckets, in our S3 bucket. Now, the interesting part of it is these, since it's a request and response, it did have PII data, and the moment you're talking about PII data, you have additional set of restrictions that you have to handle, additional encryption that you have to handle, so distributing these two types of logs in different sources or different storage patterns helped us, so using S3, how it helped us is it helped us to enable encryption at rest. That was one of our compliance requirement. It also helped us create separate set of access routes around these kind of logs, because you can create a separate access control for the buckets, and another area where it helps is having the lifecycle policies. It helped us automatically transition the logs to archive it based on the business rules that were specified. Second here is metrics. We use Dynatrace as our APM. It's an agent-based solution where we had to install these agents in our containers, and that gives us a lot of visibility, not only in terms of resources, like how your servers are doing, how, the application health and everything, but it also lets you create a request call across multiple services, so, and then obviously it gives you a lot of monitoring capabilities where you can configure alerts based on multiple rules. So, the third part is tracing. Now, a transaction has got multiple stages that across through the day, I would say, so there, there are authorizations, then there are capture, fraud detect, and then the settlement, which happens at a different time in the computation. Now, some of these are valid API calls, some of them are happening in a batch process, but to effectively identify what happened in a transaction, you need to be able to pull out all the details corresponding to a transaction, so what we did is there were two aspects to it again. One thing was you had Dynatrace, which given us, it gave us the ability to trace a request across multiple services. So you see like, oh, what was the, if there was a failure, which service failed, and what was the issue there? Apart from that, we generated the logs in a certain pattern, so we used descent format to export, create the log increase, and one of the attributes of the log descent was a tracing ID, which in our case was transaction ID, but all the services, be them batch processes or being the APIs followed this pattern, and now, and all of the logs being in the same source, when you search with the particular transaction ID, you could get all the events that happened in a transaction in one shot, and that will give you complete visibility regarding what happened in a transaction. So, yeah, so across these three areas, it covered that, the application was very easy to support, and it was very easy to find what happened to a transaction or where the system was failing. Next, another area of key area was maintainability. Like, when we talk about maintainability, these are the things that we are concerned about. How easy it is to identify your fault. Like, was there, where is the problem? Next is how easy it is to introduce the fix into the system or how easy it is to change the system. If it might be a new feature, or it might be fixed, but how easy it is to change the system. And the third is how easy it is to actually do a production release. Like, do you have enough confidence in it? Now, there are a few areas that helped us do that. One was using microservices again. Very, each service having very isolated, already specific purpose, so whenever you see an issue in production, you know exactly which service is responsible for it and what you will have to change. So, your focus is restricted to a very small area, and thereby it's very easy to change. Also, the things that you are doing, you're pretty sure that it's not effecting a lot of areas. You know exactly that, which area of the code is getting affected by it, so that kind of reduces the risk of a change in your system. Next was, okay, I've done the change. Now, how do I ensure that it does not have any collateral damage? Like, did it break anything else? For that, all our testing integration, as well as innate, obviously, but everything was automated, so every time we did a small or a big thing, doesn't matter, we run the entire suit, and having it automated means it was fast and there was hardly any cost of running it. So, you validate your system, you're okay with the change now, but then it's a production. That means you're always scared. So, having a very effective CI/CD pipeline helps. What CI/CD does is not only reduces your window, but it also, it reduces the chances of any error or manual edits in the process, so you're more confident that, about your releases and what will go into the production. So again, with the combination of all these three areas, what it does is it gives the developer a confidence to do a change, as well as the business to introduce this into production. Now, this, all this is, was how the, how it was designed to address all the areas, our concerns of ETS, and the question is whether it did or not. I'll let Brian answer that. This is, I'm a talker, so this is now my chance to talk. It'll kind of be a little funny. So, I have a love/hate relationship with this project. The love was that it exceeded every expectation from the standpoint. Oh, my mic. Yeah, so sorry, a love/hate relationship with this project, because number one, we were under extreme duress. Our vendor came to us, gave us 15 months. We had already been planning to do a long-term investment and get off the platform, but we had a very short period of time. So, what I'll say is extreme exuberation when last, this past June, we went live with our payment system, thanks to our partners PwC and my great team, and everybody at ETS that supported us, but the thing is it would not have been possible with a technology that was not available to us. The AWS platform really made it possible. I currently operate six different environments, which I can freely unencumber. It is a little bit costly from an overhead, like, time perspective, like when we're doing releases, but the thing is I've done 20 releases since June. We do a release every sprint into production. It's very quick. It, everything kind of, we do all of our feature refinements, do our bug fixing, whatever we have, and then every release goes out like clockwork. Pretty much two weeks, you can set your watch to it. So through automation, through everything that's been talked about, like, it's unimaginable as to what we can do. It's also unimaginable in terms of what we've talked about having features being able to be turned on and turned off. When we went live, we thought the big bang was gonna be great. This is where I talk about love/hate, right? The exuberance of going live in June was a huge weight off the shoulders. I manage the application. I have a team. We were all very excited, only to find out not everything is perfect. We're trying to make that transparent to our customers, trying to make that transparent to our accounting department. We're trying to make that transparent to our management, right, in how we handle things. Everything that we talked about from an example standpoint, that's not just talk, that, what they're, what they're presenting in terms of their architecture, all of that actually came true. So, our cycle times were cut down from our ability to bug fix. We can turn off a problematic payment method when our partner has an issue, like the authorizations aren't happening properly or the fraud detection engine isn't quite tweaked properly, we can easily go in and turn off these features. I can turn off these features. I mean, I can't stress enough. ETS has like, 15 maybe internal payment systems or internal order systems to handle each of these test registrations distinctly, so it's like having 15 different partnerships. Then I have external companies who do work on behalf of ETS that connect to us, so I'm effectively a service provider and I'm providing all of this service every two weeks, releasing production, customers don't know we have, we do our deployments, the microservice bleeds out or the container bleeds out, and then the next one comes up and start handling the load. So, we don't necessarily have to stop, integrate, do all this testing, bless you, with all of the different systems that we have. If I had to stop and do testing really rigidly with all these different vendors and different payment systems we have, we'd never get anything out the door. And so from an iterative approach and from our environment approach with having all these environments, it allows us to be extremely flexible. Internally we have, we modeled a, like a mock payment system. So basically we have our own internal, we don't go out to the vendor so we can do performance testing. We can do all kinds of different testing on different environments and have different purposes for those types of things, and so with AWS, it's been extremely easy. I can turn off the environment. So if I need right now, I need them all, but I couldn't imagine doing this back in our previous arrangements. We've already processed 1.5 million transactions since we started, which is really incredible. I've had almost no service issues whatsoever. As a matter of fact, this morning, before this presentation, I won't get too much into the detail, but I had like a little flare up. So Dynatrace sends me a note, I get an instance, I contact my lead developer, we look into the issue, I talk to the product owner, we come to a resolution, we wait 15 minutes, the services are self-resolving, self-healing, we find out there's a issue with our vendor, temporary, but all of that, within a matter of a half an hour, it literally took me longer to log and document the incident for the rest of the company than it did to handle and understand, troubleshoot, get to the bottom of it and make sure that my customers weren't impacted. So, that's a reality that is just the part of the love of where we are with this system. Earlier, they talked about, I'm gonna leave some time for questions, but ETS struggled with currency and providing local currency options to customers. So we have a dynamic currency conversion option, so if you have a credit card that's issued in a particular country, and you want to use that payment method and that is gonna be in a particular method of currency, instead of having to pay in US currency, we can now dynamically offer almost any currency in the world, which is converted into real time, and so that's a flexibility option we never thought we'd have. The other thing is I talked about adding new payment methods. When we first went live, we had all these payment with it. So we went with a big bang, we started them all, and then we realized, oops, this one needs tweaking, we shut it off, we turned it back on, we shut it off, we turned it back on. We had multiple attempts, but we had that flexibility. I didn't need to do releases. One of the things about managing this application, which is really great, is I can have like one service. I can say, oops, break, fix, we need to go and identify the payment UI service. We go particularly get that service up and running or get that container up and running and deal with that. We don't have to deploy the entire application across its mass. We have, I dunno, probably somewhere between 15 and 20 different services that are running. So, I can surgically do whatever I need to do or the team needs to do in order to manage the application. It's a really, a really great thing. And with any system, you want to be able to pay back your investment, so for a lot of different reasons, we're on target to definitely recover our investment within the amortization period that we put together, so that's a positive for ETS. So, anytime you want to invest, you always want to make back your money, and I look at our infrastructure and you think like, hey, we got six of these different environments that should be costing, like in a data center, it would cost us tons and tons of money, and in AWS, our monthly costs are pretty reasonable, so again, that's something we couldn't have really, couldn't have planned it better, so. I think that's about all I want to cover. So, we thank you very much for coming. I appreciate everybody's attention today. Gokul, do you have any final thoughts or want to open it up for questions? So thank you everyone for coming today and listening to our experience and patiently listening to us talk about how we built the system. So, happy to take any questions if you have. We are also available here, we have a booth here in, for PwC, so happy if you want to stop by there and have some questions, have a chat on the solution, happy to do that as well, so. I'm just curious, something I had back of mind when I read your request. Is there a reason why you didn't use load primes or M1 theme templates? Yeah, so I'm happy to answer that. So there are, there are some areas where, like I said, speed to market was very important. There was some existing investments already in play. It was working very well. We didn't want to really boil the option. We wanted to make sure that it works with, because this is not the only solution that is leveraging this. There are other parts of the enterprise, which are leveraging that'll all work together, so we wanted to make sure that continues, and we didn't have to worry about that part of the equation. Yes. Was there anything you could query specifically that you could think of that ADM did not grow or slow down the building process? Yeah, like our, so one of the things we did, just in an agile manner, I've always had an embedded testing group, so they wrote the tests, they wrote the automated tests, we built that into the pipeline, so each battery of tests is set to run on its particular environment, and as I mentioned, some of those environments connect to the vendors, some of them are mock, so basically we've canned responses, so when I have a application system contact me, it's part of the hate relationship. So I'm effectively managing my own gateway because if you sent me a transaction for $50, I've got a canned response for that to give you an accept or decline. I've given you a card, so I maintain that environment, so I'm able to continuously run that with my partners and let them do that consistently, and internally, we just run those tests all, like every day there's regression being run that the tester runs it on every environment because they're slightly different, but from that standpoint, it really has not been a hindrance to us. Any other like, thoughts or more specificity that you wanted? , No, really, we're going into a major release of our accounting software. Okay. It seems that having to monitor everything, real monitoring is when you, everything is set up in terms of a testing environment, and that is a real problem. It takes longer and longer to run. Sure, yeah, yeah. Yeah, I get that. We limited the number of tests that we were able to like, run, so I don't, that's, that was one of the reasons why we had the mock system, so there's only X number of scenarios they could run, but it's probably different for an accounting system versus the payment system, because I have X number of card types, or a decline of 3DS. I mean, I'd say there's probably, maybe 40 scenarios or so, maybe slightly more, but yeah, like the more features you have, the different, but again, if you're in a microservice environment, you're not touching one aspect, you don't necessarily have to worry about the intensive testing there. You can focus. That's correct. Exactly, yeah. So one more area that we, what we did was used to tag the test cases, and so that would let you run specific test cases corresponding to the release. So not always in all releases we would run the entire battery of the test, so we would focus on the areas where we are touching. So for example again, if you are touching the credit card, there's not like, PayPal is not really required to be tested, right? So we had like, correct tags, I will say, to each test cases, and then during the release, we would run only the tags which are relevant to it, not the entire battery. There was another question here, I thought, somewhere. Yeah, I was wondering if we can come back to the log subtypes, so what are these meant to do to log and secure and downsize risk? I don't think that was made very clear. Yeah, so when Mrinal was talking about the different levels of security, so we have tokens that people need to use, so we have external systems and internal systems that are connecting to us, so each of those needs a unique token. Also, we need to have a valid signing, field signing, so when you send me data, I know we have a mutual understanding of what that hash is, so if you send me data that doesn't match, I'm pretty much not gonna accept it because it doesn't meet the hash requirement as well, and then at each entry point, each touch point, we have all security measures related to the tokens and the handshakes that are happening, plus the encryption across the entire system. And also, like, your question is like, it's too broad to answer them like one simple tool, but like, any incoming traffic, you have the gateway, you had the firewalls in place to be able to handle that. Right, and then there's Akamai on the outside, so it's just, there's a whole lot of different points, not one single point of security. That was also key, was to have different varied levels of security. Thanks. Yeah. Okay, so I wanted to know, are there other gateways that we can use in terms of the? Yeah, so first of all, ETS and its gateway provider Fiserv, the reason we chose them was, or one of the implementation methods that we chose with them was to keep our existing PCI level, so ETS does not collect PAN data, credit card data, our payment vendor does that, and so we get an insecure token that comes back, so it's basically just a number that has nothing to do with the person's credit card data, so I don't have to worry about protecting that because the Fiserv's embedded payment JS, they're the ones who directly take that, they provide me a token value in return and they handle the credit card part of it. From our standpoint, from PII, personally identifiable information for customers, it's very important to us. So, as these guys talked about, we have KMS encryption on every piece of data at rest, so it's extremely important for ETS to make sure that all of our data's secure in that manner, and so, even in our logs, so we don't have any credit card data, and in addition to not storing the credit card data, the customer's personal data is also protected by being encrypted. The only people who have access to view any of that data are people who are vetted within our system, and they have access to those logs through the, we built a backend management tool. So for example, if I'm doing an order search and I'm looking for your transaction, I go in, I look up your transaction, and if I need to know what happened to that, so there's a lay person's view, but then you can also click on a button right in the transaction and it'll present the log, which is useful for troubleshooting. So customer service representatives or our internal treasury department can look up that information and get to the bottom of why a customer's payment might've been declined, because we interpret things from our vendors like Fiserv for example, but sometimes you need to look at the raw message to see exactly what happened, so that's the point of why we kept the logs, but it was very important that we have both user level, as well as disk level encryption on being able to access those logs. Not anybody can get to them. Yep. Yes. First wanted to say that I enjoyed the presentation. Thank you. Second part is what service do you use ECS of the literally the thousands of ECS in the market? So I'll answer the first question first. There was no challenges. I mean like, like every system, right, you need to, there's a level of tuning that needs to happen, which is what Mrinal was talking about. As you start scaling up workloads, as you start doing your testing, there's a level of configuration changes that you'll have to do with that comes with any service. It's just easier if it's a managed service. The question around ECS with like an EKS is more directionally where an organization is and what services are allowed, services at that part of time when the decision was made, so that was a big part of why we went with ECS. It was not a technical challenge, it was more an operational perspective. Yeah, at the time, at ETS, we didn't have a lot of operational support and knowledge on the IT side to support a lot of Lambda functions, so we mainly went with the ECS, yep, and I, it's been great, actually, I can't complain at all. How do you manage the process? Cold start. So we used, we did not use Lambda as part of any of our direct synchronous processes. We used Lambda mainly for our backend processes. So cold start was not an issue for us because in the backend processes for, even if it's one or two seconds delayed, it didn't matter to us, with ECS Fargate, and that was one of our considerations also. That's why we picked and choose where we would use Lambda and where we would use ECS Fargate. Yeah, and I was gonna say like, I'm constantly, as the nervous application manager, I'm constantly saying, is this gonna impact, do we have to report a service downtime when we're doing this release? And the bottom line is nine times out of 10, the answer always came back as no. My engineer is saying, nope, this is gonna bleed out the other container is gonna come up, and then you're gonna have that capability in production, just like that, and it's kind of like a seamless fail over. So, that was another benefit, I think, to doing that technology versus having the cold start. And just to finish off, a stat that I didn't report out: we've had, in that six months or so, close to six months, one planned downtime in that entire time in 20 releases, so only one time did I have to tell all the application systems, we're bleeding out, I need everybody to shut down, and it was because we basically had multiple database infrastructure type things that we needed to do at that time, but that's like a dream come true. It's just been great in that sense. All right, thank you. Thank you very much, everyone. We appreciate it. (audience applauds)

## Subtitles with Timestamps

[00:00](https://www.youtube.com/watch?v=CjbqcbkU0so&t=0s) Good morning, everyone.

[00:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1s) Welcome to day one of re:Invent in 2021.

[00:06](https://www.youtube.com/watch?v=CjbqcbkU0so&t=6s) I'm very excited to be here.

[00:08](https://www.youtube.com/watch?v=CjbqcbkU0so&t=8s) I'm Gokul Raghuraman from PwC,

[00:10](https://www.youtube.com/watch?v=CjbqcbkU0so&t=10s) and I'm joined by my colleagues Mrinal and Brian,

[00:14](https://www.youtube.com/watch?v=CjbqcbkU0so&t=14s) who will be speaking to you very shortly.

[00:18](https://www.youtube.com/watch?v=CjbqcbkU0so&t=18s) Today, the topic that we are gonna cover

[00:21](https://www.youtube.com/watch?v=CjbqcbkU0so&t=21s) is our journey and our experience,

[00:25](https://www.youtube.com/watch?v=CjbqcbkU0so&t=25s) and we wanted to share that with you

[00:26](https://www.youtube.com/watch?v=CjbqcbkU0so&t=26s) as to how we worked with ETS to build a payment solution,

[00:31](https://www.youtube.com/watch?v=CjbqcbkU0so&t=31s) a seamless experience for ETS customers.

[00:35](https://www.youtube.com/watch?v=CjbqcbkU0so&t=35s) Now, before we get started,

[00:41](https://www.youtube.com/watch?v=CjbqcbkU0so&t=41s) just wanted to call out very quickly

[00:42](https://www.youtube.com/watch?v=CjbqcbkU0so&t=42s) that while the three of us are here, behind the scenes,

[00:46](https://www.youtube.com/watch?v=CjbqcbkU0so&t=46s) obviously we didn't turn up here by ourselves

[00:49](https://www.youtube.com/watch?v=CjbqcbkU0so&t=49s) and built a solution.

[00:49](https://www.youtube.com/watch?v=CjbqcbkU0so&t=49s) There was a lot of people who helped us build a solution,

[00:52](https://www.youtube.com/watch?v=CjbqcbkU0so&t=52s) both from PwC, as well as ETS,

[00:54](https://www.youtube.com/watch?v=CjbqcbkU0so&t=54s) so we want to acknowledge that.

[00:57](https://www.youtube.com/watch?v=CjbqcbkU0so&t=57s) The topics that we wanted to cover today would be

[01:00](https://www.youtube.com/watch?v=CjbqcbkU0so&t=60s) what are some of the common challenges that you see

[01:04](https://www.youtube.com/watch?v=CjbqcbkU0so&t=64s) or that you've seen our customers face,

[01:07](https://www.youtube.com/watch?v=CjbqcbkU0so&t=67s) whether it's in the payment space,

[01:09](https://www.youtube.com/watch?v=CjbqcbkU0so&t=69s) in any other line of business application,

[01:11](https://www.youtube.com/watch?v=CjbqcbkU0so&t=71s) what are the challenges that they face today?

[01:13](https://www.youtube.com/watch?v=CjbqcbkU0so&t=73s) How does a cloud-native solution architecture

[01:16](https://www.youtube.com/watch?v=CjbqcbkU0so&t=76s) help solve some of those challenges?

[01:18](https://www.youtube.com/watch?v=CjbqcbkU0so&t=78s) What kind of challenges we face along the way,

[01:22](https://www.youtube.com/watch?v=CjbqcbkU0so&t=82s) our learnings along the way, and how we course corrected

[01:26](https://www.youtube.com/watch?v=CjbqcbkU0so&t=86s) over the period of time where we started

[01:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=89s) to where we are today.

[01:31](https://www.youtube.com/watch?v=CjbqcbkU0so&t=91s) That's, in a nutshell, what we are gonna cover today.

[01:33](https://www.youtube.com/watch?v=CjbqcbkU0so&t=93s) Along the next 60 minutes, my colleagues will talk to you

[01:38](https://www.youtube.com/watch?v=CjbqcbkU0so&t=98s) about some of the specific considerations

[01:40](https://www.youtube.com/watch?v=CjbqcbkU0so&t=100s) that we had put in place as we built the solution

[01:43](https://www.youtube.com/watch?v=CjbqcbkU0so&t=103s) and how we went about operationalizing the solution

[01:47](https://www.youtube.com/watch?v=CjbqcbkU0so&t=107s) and where we are today

[01:48](https://www.youtube.com/watch?v=CjbqcbkU0so&t=108s) and what the future looks like for us.

[01:50](https://www.youtube.com/watch?v=CjbqcbkU0so&t=110s) So, that said, wanted to open by talking a little bit

[01:56](https://www.youtube.com/watch?v=CjbqcbkU0so&t=116s) about what are some of the common challenges that we see

[01:59](https://www.youtube.com/watch?v=CjbqcbkU0so&t=119s) that our clients face in the marketplace?

[02:02](https://www.youtube.com/watch?v=CjbqcbkU0so&t=122s) This is the four that we've shown here are primarily

[02:09](https://www.youtube.com/watch?v=CjbqcbkU0so&t=129s) the most common scenarios

[02:10](https://www.youtube.com/watch?v=CjbqcbkU0so&t=130s) that we've seen our clients face, right?

[02:13](https://www.youtube.com/watch?v=CjbqcbkU0so&t=133s) They either have a scenario where they wanted to focus on

[02:18](https://www.youtube.com/watch?v=CjbqcbkU0so&t=138s) building solutions and deploying them

[02:20](https://www.youtube.com/watch?v=CjbqcbkU0so&t=140s) and releasing them at the speed at which

[02:23](https://www.youtube.com/watch?v=CjbqcbkU0so&t=143s) you could actually experience in the cloud

[02:25](https://www.youtube.com/watch?v=CjbqcbkU0so&t=145s) the capabilities provided by service providers like AWS.

[02:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=149s) Perhaps they are interested in focusing most of their energy

[02:33](https://www.youtube.com/watch?v=CjbqcbkU0so&t=153s) on actually building applications that are either

[02:37](https://www.youtube.com/watch?v=CjbqcbkU0so&t=157s) revenue generating, customer facing applications

[02:40](https://www.youtube.com/watch?v=CjbqcbkU0so&t=160s) and not having to worry about managing hardware,

[02:43](https://www.youtube.com/watch?v=CjbqcbkU0so&t=163s) managing infrastructure and leave that to people

[02:47](https://www.youtube.com/watch?v=CjbqcbkU0so&t=167s) who are dedicated and who are behind the scenes

[02:49](https://www.youtube.com/watch?v=CjbqcbkU0so&t=169s) who are helping stand up the solution.

[02:52](https://www.youtube.com/watch?v=CjbqcbkU0so&t=172s) The other aspect that comes up a lot

[02:56](https://www.youtube.com/watch?v=CjbqcbkU0so&t=176s) is there's a lot of change happening in the marketplace.

[02:59](https://www.youtube.com/watch?v=CjbqcbkU0so&t=179s) Every company is innovating and you have a very fixed

[03:02](https://www.youtube.com/watch?v=CjbqcbkU0so&t=182s) amount of time to be able to reach the market segment,

[03:05](https://www.youtube.com/watch?v=CjbqcbkU0so&t=185s) and that was one of the scenarios

[03:07](https://www.youtube.com/watch?v=CjbqcbkU0so&t=187s) that we had at ETS as well.

[03:09](https://www.youtube.com/watch?v=CjbqcbkU0so&t=189s) We had, like we had a time limit imposed on us.

[03:13](https://www.youtube.com/watch?v=CjbqcbkU0so&t=193s) We had a very short amount of time,

[03:15](https://www.youtube.com/watch?v=CjbqcbkU0so&t=195s) we had a very limited set of resources

[03:18](https://www.youtube.com/watch?v=CjbqcbkU0so&t=198s) and we had to make the best use of it to be able

[03:20](https://www.youtube.com/watch?v=CjbqcbkU0so&t=200s) to stand up a solution within a certain amount of time.

[03:22](https://www.youtube.com/watch?v=CjbqcbkU0so&t=202s) So, we'll talk a little bit about what some of those factors

[03:26](https://www.youtube.com/watch?v=CjbqcbkU0so&t=206s) were in detail, but at the high level,

[03:28](https://www.youtube.com/watch?v=CjbqcbkU0so&t=208s) these are the common challenges that we face

[03:30](https://www.youtube.com/watch?v=CjbqcbkU0so&t=210s) whenever we are trying to stand up

[03:33](https://www.youtube.com/watch?v=CjbqcbkU0so&t=213s) a cloud-native solution in the cloud.

[03:36](https://www.youtube.com/watch?v=CjbqcbkU0so&t=216s) Now, how does cloud-native architecture help?

[03:41](https://www.youtube.com/watch?v=CjbqcbkU0so&t=221s) The founding principles at a highest level

[03:44](https://www.youtube.com/watch?v=CjbqcbkU0so&t=224s) are these services are managed.

[03:46](https://www.youtube.com/watch?v=CjbqcbkU0so&t=226s) When AWS originally started,

[03:48](https://www.youtube.com/watch?v=CjbqcbkU0so&t=228s) there was a lot of platform services

[03:50](https://www.youtube.com/watch?v=CjbqcbkU0so&t=230s) that used them for compute and storage,

[03:52](https://www.youtube.com/watch?v=CjbqcbkU0so&t=232s) but eventually now AWS has a depth and breadth

[03:56](https://www.youtube.com/watch?v=CjbqcbkU0so&t=236s) of services that allow you to build solutions very,

[04:00](https://www.youtube.com/watch?v=CjbqcbkU0so&t=240s) very quickly and be able to test your hypothesis

[04:03](https://www.youtube.com/watch?v=CjbqcbkU0so&t=243s) and then release to the production environment,

[04:06](https://www.youtube.com/watch?v=CjbqcbkU0so&t=246s) so that's the beauty of the managed services

[04:07](https://www.youtube.com/watch?v=CjbqcbkU0so&t=247s) that are already available there

[04:09](https://www.youtube.com/watch?v=CjbqcbkU0so&t=249s) that we were able to take advantage of

[04:12](https://www.youtube.com/watch?v=CjbqcbkU0so&t=252s) for our faster release cycles to test them and to be able

[04:17](https://www.youtube.com/watch?v=CjbqcbkU0so&t=257s) to scale at the speed and the capacity that you would have

[04:20](https://www.youtube.com/watch?v=CjbqcbkU0so&t=260s) normally not been able to.

[04:23](https://www.youtube.com/watch?v=CjbqcbkU0so&t=263s) We also, as part of managed services, do one thing that

[04:26](https://www.youtube.com/watch?v=CjbqcbkU0so&t=266s) we learned over a period of time and we implemented here

[04:31](https://www.youtube.com/watch?v=CjbqcbkU0so&t=271s) was the need to automate right from the get-go,

[04:35](https://www.youtube.com/watch?v=CjbqcbkU0so&t=275s) so every sprint, there was not just

[04:38](https://www.youtube.com/watch?v=CjbqcbkU0so&t=278s) the application development and testing,

[04:40](https://www.youtube.com/watch?v=CjbqcbkU0so&t=280s) but we had the checks and balances in place

[04:43](https://www.youtube.com/watch?v=CjbqcbkU0so&t=283s) from a platform as well as from an application perspective

[04:45](https://www.youtube.com/watch?v=CjbqcbkU0so&t=285s) to be able to automate most of our pipelines

[04:49](https://www.youtube.com/watch?v=CjbqcbkU0so&t=289s) and be able to test them on a sprint by sprint basis.

[04:54](https://www.youtube.com/watch?v=CjbqcbkU0so&t=294s) The, what it also allows you to do is to be able to scale

[04:58](https://www.youtube.com/watch?v=CjbqcbkU0so&t=298s) at a rate at which you would typically not be able to

[05:04](https://www.youtube.com/watch?v=CjbqcbkU0so&t=304s) if you had gone in with managing your own hardware

[05:06](https://www.youtube.com/watch?v=CjbqcbkU0so&t=306s) and software, so we were able to put in the right controls

[05:10](https://www.youtube.com/watch?v=CjbqcbkU0so&t=310s) and design patterns in place to be able to scale,

[05:14](https://www.youtube.com/watch?v=CjbqcbkU0so&t=314s) to be able to roll back,

[05:15](https://www.youtube.com/watch?v=CjbqcbkU0so&t=315s) and we heavily leveraged feature toggles to be able

[05:19](https://www.youtube.com/watch?v=CjbqcbkU0so&t=319s) to make the solution flexible and customizable.

[05:24](https://www.youtube.com/watch?v=CjbqcbkU0so&t=324s) Now, I wanted to pass it on to Brian,

[05:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=329s) who will talk about ETS's journey and where they are.

[05:33](https://www.youtube.com/watch?v=CjbqcbkU0so&t=333s) Hello everyone, Brian Hersh, I'm from ETS.

[05:36](https://www.youtube.com/watch?v=CjbqcbkU0so&t=336s) Many of you might know ETS.

[05:38](https://www.youtube.com/watch?v=CjbqcbkU0so&t=338s) You may have taken one of our very many tests.

[05:41](https://www.youtube.com/watch?v=CjbqcbkU0so&t=341s) We have the practice tests, the GRE, TOEFL exams.

[05:46](https://www.youtube.com/watch?v=CjbqcbkU0so&t=346s) We're also a heavy research company,

[05:49](https://www.youtube.com/watch?v=CjbqcbkU0so&t=349s) largest private-based educational research company

[05:53](https://www.youtube.com/watch?v=CjbqcbkU0so&t=353s) in the world, and with that comes many challenges

[05:57](https://www.youtube.com/watch?v=CjbqcbkU0so&t=357s) where we're all over the world

[05:59](https://www.youtube.com/watch?v=CjbqcbkU0so&t=359s) in many, many, many countries.

[06:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=361s) One of the funny things our partners tell us

[06:04](https://www.youtube.com/watch?v=CjbqcbkU0so&t=364s) is they work with retail companies

[06:07](https://www.youtube.com/watch?v=CjbqcbkU0so&t=367s) and other types of payment, companies that take payments.

[06:11](https://www.youtube.com/watch?v=CjbqcbkU0so&t=371s) ETS has presented a very major challenge for them

[06:14](https://www.youtube.com/watch?v=CjbqcbkU0so&t=374s) because culturally, our company is diverse,

[06:18](https://www.youtube.com/watch?v=CjbqcbkU0so&t=378s) our product is diverse,

[06:19](https://www.youtube.com/watch?v=CjbqcbkU0so&t=379s) our tests are diverse, everything is diverse,

[06:22](https://www.youtube.com/watch?v=CjbqcbkU0so&t=382s) and that creates an interesting challenge.

[06:24](https://www.youtube.com/watch?v=CjbqcbkU0so&t=384s) So, you can see here, we have 50 million tests

[06:28](https://www.youtube.com/watch?v=CjbqcbkU0so&t=388s) that we deliver annually in more than 9,000 locations,

[06:33](https://www.youtube.com/watch?v=CjbqcbkU0so&t=393s) and so one of the challenges we have

[06:36](https://www.youtube.com/watch?v=CjbqcbkU0so&t=396s) is keeping up with the marketplace, and in years past,

[06:41](https://www.youtube.com/watch?v=CjbqcbkU0so&t=401s) we struggled with those challenges,

[06:44](https://www.youtube.com/watch?v=CjbqcbkU0so&t=404s) and so one of the things we did was we set out to reinvent

[06:51](https://www.youtube.com/watch?v=CjbqcbkU0so&t=411s) our payment process, and we worked together with PwC

[06:57](https://www.youtube.com/watch?v=CjbqcbkU0so&t=417s) to come up with what was just a really amazing experience,

[07:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=421s) and every day that goes on, we experience amazing benefits

[07:08](https://www.youtube.com/watch?v=CjbqcbkU0so&t=428s) that are, how could I say?

[07:11](https://www.youtube.com/watch?v=CjbqcbkU0so&t=431s) Lightspeed.

[07:12](https://www.youtube.com/watch?v=CjbqcbkU0so&t=432s) It's just very, a very good journey.

[07:16](https://www.youtube.com/watch?v=CjbqcbkU0so&t=436s) So, where were we?

[07:19](https://www.youtube.com/watch?v=CjbqcbkU0so&t=439s) ETS had a vendor who was very static in nature,

[07:23](https://www.youtube.com/watch?v=CjbqcbkU0so&t=443s) so one of the things that we were limited to

[07:26](https://www.youtube.com/watch?v=CjbqcbkU0so&t=446s) was what payment methods did they have?

[07:30](https://www.youtube.com/watch?v=CjbqcbkU0so&t=450s) We were basically tied with those.

[07:34](https://www.youtube.com/watch?v=CjbqcbkU0so&t=454s) Our lines of business would ask,

[07:36](https://www.youtube.com/watch?v=CjbqcbkU0so&t=456s) hey, can we try this payment method,

[07:39](https://www.youtube.com/watch?v=CjbqcbkU0so&t=459s) or can we go after this market with these new payments?

[07:42](https://www.youtube.com/watch?v=CjbqcbkU0so&t=462s) Because let's say the payments that we're accepting

[07:45](https://www.youtube.com/watch?v=CjbqcbkU0so&t=465s) are very US centric, so how do we get to that global rollout

[07:50](https://www.youtube.com/watch?v=CjbqcbkU0so&t=470s) and be able to support people throughout the world?

[07:53](https://www.youtube.com/watch?v=CjbqcbkU0so&t=473s) And that was a really tough challenge.

[07:57](https://www.youtube.com/watch?v=CjbqcbkU0so&t=477s) Other things we struggled with,

[07:59](https://www.youtube.com/watch?v=CjbqcbkU0so&t=479s) we had minimal control over our outages and upgrades.

[08:04](https://www.youtube.com/watch?v=CjbqcbkU0so&t=484s) The vendor did whatever they want.

[08:06](https://www.youtube.com/watch?v=CjbqcbkU0so&t=486s) We had a hosted solution, but at the end of the day,

[08:09](https://www.youtube.com/watch?v=CjbqcbkU0so&t=489s) we had very little control over what was going on.

[08:12](https://www.youtube.com/watch?v=CjbqcbkU0so&t=492s) That was all happening based on what was going on

[08:16](https://www.youtube.com/watch?v=CjbqcbkU0so&t=496s) in their data center,

[08:17](https://www.youtube.com/watch?v=CjbqcbkU0so&t=497s) how they were handling the maintenance of our application.

[08:20](https://www.youtube.com/watch?v=CjbqcbkU0so&t=500s) So ETS had been thinking, how can we get more flexible?

[08:24](https://www.youtube.com/watch?v=CjbqcbkU0so&t=504s) How can we take over more control

[08:26](https://www.youtube.com/watch?v=CjbqcbkU0so&t=506s) without having staff of hundreds of people

[08:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=509s) to maintain and support our global presence around the world

[08:33](https://www.youtube.com/watch?v=CjbqcbkU0so&t=513s) and be able to take payments in a real-time fashion?

[08:37](https://www.youtube.com/watch?v=CjbqcbkU0so&t=517s) So, one of the things we also found was the enhancements,

[08:42](https://www.youtube.com/watch?v=CjbqcbkU0so&t=522s) they were costly and they were very slow to occur.

[08:45](https://www.youtube.com/watch?v=CjbqcbkU0so&t=525s) Sometimes we would wait six months to a year

[08:48](https://www.youtube.com/watch?v=CjbqcbkU0so&t=528s) to get enhancements to the system,

[08:51](https://www.youtube.com/watch?v=CjbqcbkU0so&t=531s) and that wasn't something that was,

[08:53](https://www.youtube.com/watch?v=CjbqcbkU0so&t=533s) well, wasn't happening nicely for our customers.

[08:58](https://www.youtube.com/watch?v=CjbqcbkU0so&t=538s) So customers would ask us for different things,

[09:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=541s) and in IT, our customers are our business units

[09:06](https://www.youtube.com/watch?v=CjbqcbkU0so&t=546s) and ETS has different silos of different business units,

[09:10](https://www.youtube.com/watch?v=CjbqcbkU0so&t=550s) so each of those business units kind of operates

[09:14](https://www.youtube.com/watch?v=CjbqcbkU0so&t=554s) slightly independent of another,

[09:16](https://www.youtube.com/watch?v=CjbqcbkU0so&t=556s) so the TOEFL folks may have different requirements than GRE

[09:21](https://www.youtube.com/watch?v=CjbqcbkU0so&t=561s) or teacher licensure within praxis,

[09:23](https://www.youtube.com/watch?v=CjbqcbkU0so&t=563s) so each of these units have different needs,

[09:26](https://www.youtube.com/watch?v=CjbqcbkU0so&t=566s) and so we had to find a way to be able to provide that

[09:30](https://www.youtube.com/watch?v=CjbqcbkU0so&t=570s) in a more timely fashion.

[09:32](https://www.youtube.com/watch?v=CjbqcbkU0so&t=572s) Also, cross-organizational communication.

[09:36](https://www.youtube.com/watch?v=CjbqcbkU0so&t=576s) One of the jokes is we're trying to give this presentation

[09:40](https://www.youtube.com/watch?v=CjbqcbkU0so&t=580s) and you have PwC and ETS, two highly technical companies

[09:44](https://www.youtube.com/watch?v=CjbqcbkU0so&t=584s) trying to coordinate with the AWS folks

[09:47](https://www.youtube.com/watch?v=CjbqcbkU0so&t=587s) to put the presentation together.

[09:48](https://www.youtube.com/watch?v=CjbqcbkU0so&t=588s) It's basically like rocket science,

[09:51](https://www.youtube.com/watch?v=CjbqcbkU0so&t=591s) and imagine trying to communicate all your requirements

[09:54](https://www.youtube.com/watch?v=CjbqcbkU0so&t=594s) and your features and your infrastructure needs

[09:57](https://www.youtube.com/watch?v=CjbqcbkU0so&t=597s) to a vendor who also has other challenges, right?

[10:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=601s) Just a silly presentation, not a silly presentation,

[10:04](https://www.youtube.com/watch?v=CjbqcbkU0so&t=604s) but a somewhat simplistic presentation

[10:06](https://www.youtube.com/watch?v=CjbqcbkU0so&t=606s) that we're trying to give today,

[10:08](https://www.youtube.com/watch?v=CjbqcbkU0so&t=608s) just illustrates how difficult that type of thing can be.

[10:13](https://www.youtube.com/watch?v=CjbqcbkU0so&t=613s) And the system wasn't scalable,

[10:15](https://www.youtube.com/watch?v=CjbqcbkU0so&t=615s) so seasonal challenges prevent or present

[10:20](https://www.youtube.com/watch?v=CjbqcbkU0so&t=620s) different opportunities for ETS to reach more test-takers

[10:26](https://www.youtube.com/watch?v=CjbqcbkU0so&t=626s) around the world during certain peaks and troughs.

[10:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=629s) The system wasn't very responsive, because it was hosted

[10:34](https://www.youtube.com/watch?v=CjbqcbkU0so&t=634s) in a data center and because it was physical infrastructure

[10:37](https://www.youtube.com/watch?v=CjbqcbkU0so&t=637s) or hardware or constraints based on a contractual nature.

[10:42](https://www.youtube.com/watch?v=CjbqcbkU0so&t=642s) We couldn't just scale up very easily,

[10:44](https://www.youtube.com/watch?v=CjbqcbkU0so&t=644s) so those were things we had to pre,

[10:47](https://www.youtube.com/watch?v=CjbqcbkU0so&t=647s) premeditate or have discussions with our vendor

[10:51](https://www.youtube.com/watch?v=CjbqcbkU0so&t=651s) about those types of things.

[10:53](https://www.youtube.com/watch?v=CjbqcbkU0so&t=653s) So, these were the things that we were mainly looking for

[10:57](https://www.youtube.com/watch?v=CjbqcbkU0so&t=657s) when we were trying to build a system,

[10:59](https://www.youtube.com/watch?v=CjbqcbkU0so&t=659s) problems we were trying to solve,

[11:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=661s) and at the same time with all of this,

[11:04](https://www.youtube.com/watch?v=CjbqcbkU0so&t=664s) ETS was going through a technological change.

[11:08](https://www.youtube.com/watch?v=CjbqcbkU0so&t=668s) We're basically adapting to the new world,

[11:12](https://www.youtube.com/watch?v=CjbqcbkU0so&t=672s) shifting our entire platform on to AWS corporate,

[11:17](https://www.youtube.com/watch?v=CjbqcbkU0so&t=677s) just throughout the entire company,

[11:20](https://www.youtube.com/watch?v=CjbqcbkU0so&t=680s) also moving to an Agile-based development model,

[11:25](https://www.youtube.com/watch?v=CjbqcbkU0so&t=685s) so lot of things happening all at once.

[11:30](https://www.youtube.com/watch?v=CjbqcbkU0so&t=690s) Okay, now I'd like to introduce Mrinal.

[11:35](https://www.youtube.com/watch?v=CjbqcbkU0so&t=695s) You wanna, oh, you're gonna?

[11:36](https://www.youtube.com/watch?v=CjbqcbkU0so&t=696s) All right, no worries.

[11:39](https://www.youtube.com/watch?v=CjbqcbkU0so&t=699s) So, I think I'll take a couple of minutes to quickly

[11:42](https://www.youtube.com/watch?v=CjbqcbkU0so&t=702s) talk through, before we get into the technical architecture,

[11:44](https://www.youtube.com/watch?v=CjbqcbkU0so&t=704s) what were some of the principles or the guiding principles

[11:47](https://www.youtube.com/watch?v=CjbqcbkU0so&t=707s) that we use before we designed the solution?

[11:50](https://www.youtube.com/watch?v=CjbqcbkU0so&t=710s) AWS has a lot of services.

[11:52](https://www.youtube.com/watch?v=CjbqcbkU0so&t=712s) Great, you can leverage them.

[11:54](https://www.youtube.com/watch?v=CjbqcbkU0so&t=714s) We decided to go with managed services.

[11:56](https://www.youtube.com/watch?v=CjbqcbkU0so&t=716s) That was great, but from an architectural standpoint,

[11:58](https://www.youtube.com/watch?v=CjbqcbkU0so&t=718s) we had to put certain principles and building blocks

[12:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=721s) in place so that everybody understands

[12:03](https://www.youtube.com/watch?v=CjbqcbkU0so&t=723s) what is the expectation and how we work together as we,

[12:06](https://www.youtube.com/watch?v=CjbqcbkU0so&t=726s) like Brian said, this is, there's a global customer base,

[12:09](https://www.youtube.com/watch?v=CjbqcbkU0so&t=729s) there's different business units

[12:10](https://www.youtube.com/watch?v=CjbqcbkU0so&t=730s) looking for the standardized solution,

[12:13](https://www.youtube.com/watch?v=CjbqcbkU0so&t=733s) so we first set about thinking through how are we

[12:18](https://www.youtube.com/watch?v=CjbqcbkU0so&t=738s) going to completely re-architect the existing solution?

[12:20](https://www.youtube.com/watch?v=CjbqcbkU0so&t=740s) The existing solution was vendor managed.

[12:23](https://www.youtube.com/watch?v=CjbqcbkU0so&t=743s) We were building a solution from the ground up,

[12:26](https://www.youtube.com/watch?v=CjbqcbkU0so&t=746s) and then we were gonna stand up in AWS.

[12:28](https://www.youtube.com/watch?v=CjbqcbkU0so&t=748s) So we looked at the payment process as a whole,

[12:31](https://www.youtube.com/watch?v=CjbqcbkU0so&t=751s) and we started at all the sub-processes

[12:33](https://www.youtube.com/watch?v=CjbqcbkU0so&t=753s) that our payment flows actually required.

[12:35](https://www.youtube.com/watch?v=CjbqcbkU0so&t=755s) So how does the customer come,

[12:36](https://www.youtube.com/watch?v=CjbqcbkU0so&t=756s) and what kind of payments is the customer looking to do?

[12:39](https://www.youtube.com/watch?v=CjbqcbkU0so&t=759s) What kind of products is the customer looking to purchase

[12:42](https://www.youtube.com/watch?v=CjbqcbkU0so&t=762s) and what kind of features and functionalities

[12:46](https://www.youtube.com/watch?v=CjbqcbkU0so&t=766s) does a typical payment flow have?

[12:47](https://www.youtube.com/watch?v=CjbqcbkU0so&t=767s) And so there's an order processing,

[12:49](https://www.youtube.com/watch?v=CjbqcbkU0so&t=769s) there is a payment solution that's happening,

[12:51](https://www.youtube.com/watch?v=CjbqcbkU0so&t=771s) there is a reconciliation that happens in the backend,

[12:53](https://www.youtube.com/watch?v=CjbqcbkU0so&t=773s) there is the refunds that happen,

[12:54](https://www.youtube.com/watch?v=CjbqcbkU0so&t=774s) so there's a number of different flows happen,

[12:56](https://www.youtube.com/watch?v=CjbqcbkU0so&t=776s) so we started breaking down everything,

[12:59](https://www.youtube.com/watch?v=CjbqcbkU0so&t=779s) that huge monolith into a sequence of sub-processes.

[13:02](https://www.youtube.com/watch?v=CjbqcbkU0so&t=782s) The minute we did that,

[13:03](https://www.youtube.com/watch?v=CjbqcbkU0so&t=783s) we were able to identify that a lot of these can actually

[13:08](https://www.youtube.com/watch?v=CjbqcbkU0so&t=788s) work independently without having to rely on each other,

[13:11](https://www.youtube.com/watch?v=CjbqcbkU0so&t=791s) so that was one of the founding principles that we set.

[13:13](https://www.youtube.com/watch?v=CjbqcbkU0so&t=793s) We want to make it loosely coupled.

[13:15](https://www.youtube.com/watch?v=CjbqcbkU0so&t=795s) We want it to have fault tolerance

[13:18](https://www.youtube.com/watch?v=CjbqcbkU0so&t=798s) by isolation in our environment,

[13:19](https://www.youtube.com/watch?v=CjbqcbkU0so&t=799s) so we went with the microservice-based approach.

[13:22](https://www.youtube.com/watch?v=CjbqcbkU0so&t=802s) We also wanted to make sure, the next question, obviously,

[13:26](https://www.youtube.com/watch?v=CjbqcbkU0so&t=806s) once you've decided on microservice

[13:27](https://www.youtube.com/watch?v=CjbqcbkU0so&t=807s) is what is the medium of communication,

[13:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=809s) how are you gonna actually communicate, right?

[13:31](https://www.youtube.com/watch?v=CjbqcbkU0so&t=811s) Is it gonna be synchronous or asynchronous?

[13:33](https://www.youtube.com/watch?v=CjbqcbkU0so&t=813s) What are we gonna do?

[13:34](https://www.youtube.com/watch?v=CjbqcbkU0so&t=814s) We, based on the flow and the use cases

[13:37](https://www.youtube.com/watch?v=CjbqcbkU0so&t=817s) that we had then charted out,

[13:39](https://www.youtube.com/watch?v=CjbqcbkU0so&t=819s) we then identified that an event-based mechanism

[13:42](https://www.youtube.com/watch?v=CjbqcbkU0so&t=822s) is the best means to be able to implement

[13:46](https://www.youtube.com/watch?v=CjbqcbkU0so&t=826s) the end-to-end payment journey

[13:47](https://www.youtube.com/watch?v=CjbqcbkU0so&t=827s) without being able to rely on different parts

[13:50](https://www.youtube.com/watch?v=CjbqcbkU0so&t=830s) of the same flow, so we went with an event-based approach

[13:57](https://www.youtube.com/watch?v=CjbqcbkU0so&t=837s) that, again, helped us from a fault tolerance perspective.

[14:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=841s) It helped us to be able to manage features

[14:05](https://www.youtube.com/watch?v=CjbqcbkU0so&t=845s) independently of each other.

[14:06](https://www.youtube.com/watch?v=CjbqcbkU0so&t=846s) We were able to test out different features

[14:08](https://www.youtube.com/watch?v=CjbqcbkU0so&t=848s) at different points in time, so that,

[14:09](https://www.youtube.com/watch?v=CjbqcbkU0so&t=849s) all that helped the microservice and the human-based

[14:12](https://www.youtube.com/watch?v=CjbqcbkU0so&t=852s) architecture set us the foundation for that, right,

[14:14](https://www.youtube.com/watch?v=CjbqcbkU0so&t=854s) and when we did this, we actually did a,

[14:17](https://www.youtube.com/watch?v=CjbqcbkU0so&t=857s) almost like a pilot tested out our hypothesis,

[14:19](https://www.youtube.com/watch?v=CjbqcbkU0so&t=859s) we did one payment method, worked great,

[14:22](https://www.youtube.com/watch?v=CjbqcbkU0so&t=862s) and then we started building at a larger scale, right?

[14:25](https://www.youtube.com/watch?v=CjbqcbkU0so&t=865s) One of the things that we also did when we started out

[14:30](https://www.youtube.com/watch?v=CjbqcbkU0so&t=870s) was we clearly had a deadline to hit.

[14:33](https://www.youtube.com/watch?v=CjbqcbkU0so&t=873s) We, there was a need by which we had to have the system

[14:36](https://www.youtube.com/watch?v=CjbqcbkU0so&t=876s) up and running, and there was a limited amount

[14:40](https://www.youtube.com/watch?v=CjbqcbkU0so&t=880s) of capabilities or resources available in front of us

[14:43](https://www.youtube.com/watch?v=CjbqcbkU0so&t=883s) to be able to put that in place.

[14:45](https://www.youtube.com/watch?v=CjbqcbkU0so&t=885s) So we, at the get-go, we worked with the ETS team,

[14:49](https://www.youtube.com/watch?v=CjbqcbkU0so&t=889s) the architecture team and their product team

[14:51](https://www.youtube.com/watch?v=CjbqcbkU0so&t=891s) to think cloud-native first, right?

[14:54](https://www.youtube.com/watch?v=CjbqcbkU0so&t=894s) So leverage the power of what is already available,

[14:58](https://www.youtube.com/watch?v=CjbqcbkU0so&t=898s) speed up the process of setting up your platform

[15:02](https://www.youtube.com/watch?v=CjbqcbkU0so&t=902s) and then very quickly building something on it

[15:04](https://www.youtube.com/watch?v=CjbqcbkU0so&t=904s) and then testing on it, right?

[15:06](https://www.youtube.com/watch?v=CjbqcbkU0so&t=906s) So we've went with,

[15:09](https://www.youtube.com/watch?v=CjbqcbkU0so&t=909s) most of you will see when Mrinal talks about it,

[15:11](https://www.youtube.com/watch?v=CjbqcbkU0so&t=911s) most of our capabilities are,

[15:13](https://www.youtube.com/watch?v=CjbqcbkU0so&t=913s) were based on native capabilities that AWS provided.

[15:18](https://www.youtube.com/watch?v=CjbqcbkU0so&t=918s) One of the motivating factors were also to make sure

[15:20](https://www.youtube.com/watch?v=CjbqcbkU0so&t=920s) that we keep an eye on operational overhead,

[15:23](https://www.youtube.com/watch?v=CjbqcbkU0so&t=923s) and this solution, after it's built,

[15:25](https://www.youtube.com/watch?v=CjbqcbkU0so&t=925s) it needs to be managed,

[15:26](https://www.youtube.com/watch?v=CjbqcbkU0so&t=926s) it needs to be cared for and fed for,

[15:28](https://www.youtube.com/watch?v=CjbqcbkU0so&t=928s) so we wanted to keep that to a bare minimum as well,

[15:31](https://www.youtube.com/watch?v=CjbqcbkU0so&t=931s) so that was one of the motivating factors that we looked at

[15:34](https://www.youtube.com/watch?v=CjbqcbkU0so&t=934s) when we went cloud-native.

[15:35](https://www.youtube.com/watch?v=CjbqcbkU0so&t=935s) We also want to, obviously, be in a position

[15:38](https://www.youtube.com/watch?v=CjbqcbkU0so&t=938s) where we can very quickly swap features in and out,

[15:41](https://www.youtube.com/watch?v=CjbqcbkU0so&t=941s) so we put on a lot of feature toggles

[15:43](https://www.youtube.com/watch?v=CjbqcbkU0so&t=943s) that allowed us to do that.

[15:47](https://www.youtube.com/watch?v=CjbqcbkU0so&t=947s) So, what were some of the key considerations

[15:50](https://www.youtube.com/watch?v=CjbqcbkU0so&t=950s) that we looked at when we actually stood up the solution?

[15:57](https://www.youtube.com/watch?v=CjbqcbkU0so&t=957s) The feature development, the backlog that came in was great,

[16:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=961s) but we also had to have, like,

[16:03](https://www.youtube.com/watch?v=CjbqcbkU0so&t=963s) the foundational set of building blocks in place.

[16:06](https://www.youtube.com/watch?v=CjbqcbkU0so&t=966s) This was a payment solution.

[16:07](https://www.youtube.com/watch?v=CjbqcbkU0so&t=967s) This was an internet facing solution, right,

[16:09](https://www.youtube.com/watch?v=CjbqcbkU0so&t=969s) so you needed to have the right set of

[16:11](https://www.youtube.com/watch?v=CjbqcbkU0so&t=971s) these kinds of functional capabilities in place

[16:13](https://www.youtube.com/watch?v=CjbqcbkU0so&t=973s) to be able to run this at scale.

[16:15](https://www.youtube.com/watch?v=CjbqcbkU0so&t=975s) So, as an example, this had PII data,

[16:21](https://www.youtube.com/watch?v=CjbqcbkU0so&t=981s) this had PCII data, so our application needed a good means

[16:25](https://www.youtube.com/watch?v=CjbqcbkU0so&t=985s) to be able to handle both kinds of information

[16:28](https://www.youtube.com/watch?v=CjbqcbkU0so&t=988s) in the application,

[16:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=989s) and you will see in the architecture

[16:31](https://www.youtube.com/watch?v=CjbqcbkU0so&t=991s) how some of these services were designed to handle

[16:34](https://www.youtube.com/watch?v=CjbqcbkU0so&t=994s) that security focused needs.

[16:38](https://www.youtube.com/watch?v=CjbqcbkU0so&t=998s) We also wanted the ability to have support.

[16:41](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1001s) This being a payment application, you want to be able

[16:45](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1005s) to provide a vast number range of payment options

[16:47](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1007s) that a customer wants to take advantage of.

[16:50](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1010s) This might be using a credit card,

[16:52](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1012s) this might be using PayPal,

[16:53](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1013s) this might be just calling in and making the payment,

[16:56](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1016s) so you need to take advantage or provide the user

[16:59](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1019s) with the most number of options,

[17:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1021s) and you need to make it look seamless

[17:05](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1025s) in the background for the customer,

[17:07](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1027s) so we had to put that resilience and those capabilities

[17:10](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1030s) in place for you to be able to do that.

[17:12](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1032s) So let's say a customer calls,

[17:13](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1033s) and one of the payment methods is not available.

[17:16](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1036s) The customer should seamlessly

[17:18](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1038s) be able to pick another alternate payment method

[17:21](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1041s) and still be able to go through with this order.

[17:26](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1046s) This was a global, the customer base was global payments

[17:32](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1052s) and orders would come in from anywhere in the globe, so,

[17:35](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1055s) which means automatically, it's not just local currency,

[17:38](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1058s) you're looking at international currencies as well,

[17:40](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1060s) so the ability to support those

[17:43](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1063s) was a big part in how the system was defined by

[17:47](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1067s) these means of these microservices.

[17:52](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1072s) We did leverage on, like, there was a number of,

[17:55](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1075s) like Brian said, there was a, the upstream was maybe

[17:59](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1079s) about 15 plus applications, which were being in a position

[18:02](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1082s) to take orders and send all this

[18:04](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1084s) to the downstream application, which is a payment solution,

[18:06](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1086s) the standardized payment solution.

[18:08](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1088s) You need a way to handle every single request,

[18:11](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1091s) every single transaction,

[18:13](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1093s) take it all the way to the payment,

[18:15](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1095s) get back the confirmation number, and you still need a way

[18:17](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1097s) to be able to trace it end-to-end, right?

[18:20](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1100s) So observability was a huge factor.

[18:23](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1103s) The golden signals of observability were put in place.

[18:25](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1105s) We looked at end-to-end tracing, logging and monitoring,

[18:28](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1108s) which we will cover shortly.

[18:31](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1111s) The other motivating factor,

[18:33](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1113s) as we thought through the solution,

[18:35](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1115s) was the payment solution needs keep changing.

[18:39](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1119s) There are new innovations in the market,

[18:41](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1121s) new innovations that keep coming in, and as a company

[18:45](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1125s) who's providing that or enabling the payment solution

[18:47](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1127s) for its customers need to be able to take that in

[18:50](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1130s) at a very quick pace without a lot of re-architecture

[18:54](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1134s) that was required in the system.

[18:55](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1135s) So again, we put in a lot of flexibility, configurability

[18:59](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1139s) in the environment to make sure that the solution

[19:02](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1142s) was easily maintainable and it could easily scale

[19:06](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1146s) in the environment.

[19:07](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1147s) So to do a deep dive,

[19:08](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1148s) I'm gonna call Mrinal, who was the architect

[19:11](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1151s) on the solution to talk us through

[19:13](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1153s) the key factors and the considerations.

[19:23](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1163s) Thank you, Gokul and hello, everyone.

[19:25](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1165s) So, yeah, to explain the architecture,

[19:30](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1170s) I'll take you through a use case.

[19:32](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1172s) Let's consider a scenario where the user has filled out

[19:36](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1176s) all the details, provided all the details,

[19:37](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1177s) and then it clicks on the pay button.

[19:40](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1180s) What happens then?

[19:41](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1181s) The call first reaches our system via our combine,

[19:45](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1185s) which performs the role of the web application firewall.

[19:48](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1188s) It hits the API Gateway.

[19:50](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1190s) The API Gateway uses custom Lambda phrases,

[19:54](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1194s) because we are to integrate with our homegrown solution

[19:58](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1198s) from ETS, which manages the tokens,

[20:02](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1202s) so it essentially, it sent it over from the request,

[20:06](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1206s) validates against ETS, which is the homegrown solution,

[20:09](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1209s) and then sees whether it's a valid request or not,

[20:10](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1210s) and then lets it through.

[20:12](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1212s) Once it lets it through,

[20:13](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1213s) it goes to the payment service,

[20:16](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1216s) which is hosted in ECS Fargate.

[20:19](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1219s) Now, the premium service has to be

[20:22](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1222s) sent to a payment gateway, which is an external system,

[20:27](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1227s) or a third party provided system.

[20:30](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1230s) To that, it first needs to find out what's the URL

[20:34](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1234s) and the credentials.

[20:36](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1236s) Now, URL and all these kinds of things

[20:37](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1237s) are stored in Parameter Store.

[20:39](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1239s) Credentials are stored in Secrets Manager

[20:42](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1242s) where it's rotated, so it gets from these sources,

[20:45](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1245s) makes a call to the third party gateway, get a response,

[20:51](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1251s) then it does some additional processing.

[20:53](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1253s) So, what it does is it creates an event object,

[20:57](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1257s) it populates all the request and response

[20:59](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1259s) and all the transaction related details for the event object

[21:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1261s) and puts it in place queues and then sends a response

[21:05](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1265s) back to the user and user sees what happens to the payment

[21:08](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1268s) and is redirected to the originating system

[21:11](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1271s) or whichever system from the request came.

[21:14](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1274s) Now, what happens to the event now,

[21:17](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1277s) when you've got that event in our queue?

[21:20](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1280s) We have a data service, which listens to this queue.

[21:25](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1285s) It gets the event, it kind of extract the request

[21:28](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1288s) and response, matches it, puts it into S3,

[21:31](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1291s) which is one of the,

[21:32](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1292s) which was one of the requests to early comment to archive

[21:35](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1295s) all the question responses for future audits and everything.

[21:40](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1300s) Then it creates a transaction record in the database.

[21:43](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1303s) Again, database means that you need to know

[21:45](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1305s) where the database is, where it comes from,

[21:48](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1308s) Parameter Store, credentials,

[21:50](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1310s) Secrets Manager where it's located and everything.

[21:54](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1314s) Then, again, you're storing data in the database,

[21:57](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1317s) which needs to be encrypted.

[22:00](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1320s) How the keys are managed,

[22:02](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1322s) we have new schemas for managing the keys.

[22:05](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1325s) So after this transaction processing is done,

[22:07](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1327s) there are a few more steps.

[22:08](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1328s) So, we need to notify the parent on the upstream system

[22:15](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1335s) that everything has gone through fine,

[22:16](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1336s) so we have to send the post back,

[22:18](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1338s) so data service puts another message in another queue

[22:23](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1343s) with all the details, like what happened to the transaction,

[22:26](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1346s) which system needs to be informed and everything,

[22:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1349s) and there is one more system,

[22:31](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1351s) which is listening to the queue.

[22:32](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1352s) It gets the response, it reads the queue,

[22:37](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1357s) gets the message, sees that, okay, this,

[22:39](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1359s) this has to go to some other system, and then sends it.

[22:42](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1362s) So, we have kind of given you an idea like,

[22:46](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1366s) how we had implemented the wind-driven system,

[22:50](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1370s) a loosely coupled set of microservices

[22:53](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1373s) handling various aspects of payment.

[22:55](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1375s) There are other use cases also.

[22:57](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1377s) Like, for example,

[22:58](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1378s) there are cases where we had to do batch processing,

[23:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1381s) like for example, settlement records,

[23:03](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1383s) which comes at an IT level for multiple transactions.

[23:07](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1387s) What we did is we had a job schedule live in CloudWatch,

[23:11](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1391s) which will trigger this, triggered the ETS job,

[23:16](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1396s) which would pick up the file, process it

[23:19](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1399s) and then update all the records.

[23:22](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1402s) So this is the, what our architecture kind of,

[23:27](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1407s) how it solves the payment flow,

[23:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1409s) but there, obviously there are so many use cases,

[23:31](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1411s) but this is one representative use case, we would say.

[23:35](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1415s) Now, this is the design.

[23:38](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1418s) We would go into a little bit detail,

[23:40](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1420s) like how this particular design

[23:42](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1422s) actually addresses the key areas, which opened up the work.

[23:49](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1429s) First was availability.

[23:52](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1432s) As you saw, most of the solutions that we used

[23:56](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1436s) are AWS managed solutions, and the wonder of that

[24:00](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1440s) is they come with high availability out of the box.

[24:05](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1445s) AWS does it by distributing the underlying infrastructure

[24:08](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1448s) across multiple availability zones.

[24:10](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1450s) However, in certain scenarios or in certain services,

[24:14](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1454s) they are a little bit of considerations.

[24:15](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1455s) For example, when you're using Lambda or Fargate,

[24:20](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1460s) like if you are attaching a VPC to your Lambda,

[24:25](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1465s) you have to ensure that the subnets within the VPC

[24:28](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1468s) are in multiple availability zone.

[24:31](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1471s) That only ensures that your functions are distributed

[24:35](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1475s) in multiple availability zones.

[24:36](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1476s) But for most of the others, it comes out of the box.

[24:39](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1479s) You don't have to do a lot of configurations,

[24:41](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1481s) so that really helps.

[24:43](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1483s) Another aspect of availability is generally

[24:46](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1486s) distributing a system across multiple regions.

[24:49](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1489s) Currently, the system is not designed to do it,

[24:53](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1493s) but once the enterprise lays out its multi-region strategy,

[24:59](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1499s) it's very easy to evolve this design

[25:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1501s) to be distributed across multiple regions.

[25:06](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1506s) Next is security.

[25:08](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1508s) It's a payment application that is accessed,

[25:12](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1512s) like, from worldwide customers, which stores PII data,

[25:18](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1518s) so security is, was very, it was and is a very,

[25:22](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1522s) very critical aspect of the entire design.

[25:26](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1526s) So, let's go in layer by layer.

[25:28](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1528s) So first, API access.

[25:30](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1530s) How we secured our API access was using API Gateway.

[25:36](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1536s) Again, there was a little bit of challenge here

[25:39](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1539s) because we had to integrate with one of our custom solution

[25:43](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1543s) to validate the token

[25:46](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1546s) and see whether the incoming requests are valid.

[25:49](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1549s) For that, we use Lambda operators,

[25:51](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1551s) which kind of indicates with the homegrown solution,

[25:54](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1554s) which is called Redis, and so it will take the token,

[26:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1561s) validate the token against Redis

[26:03](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1563s) and then forward the request only if it's a valid token.

[26:06](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1566s) Next was encryption across various levels.

[26:10](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1570s) So first is encryption for data in transit.

[26:14](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1574s) We kind of enforced HTTPS at the load balancer

[26:18](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1578s) as well as the API Gateway level, so that way,

[26:20](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1580s) that kind of ensured

[26:22](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1582s) that all the data in transit was encrypted.

[26:26](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1586s) Moreover, we had one more additional layer of security

[26:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1589s) wherein the request body coming from the incoming systems

[26:33](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1593s) were encrypted using keys, which was mutually agreed upon

[26:38](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1598s) between this payment gateway solution

[26:40](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1600s) and the upstream system.

[26:43](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1603s) Apart from that, since we are storing PII data,

[26:47](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1607s) we also had additional comments of encrypting

[26:50](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1610s) any data at rest using customer managed keys.

[26:55](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1615s) How we were managing these keys,

[26:56](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1616s) the UI manually uses keys using KMS, and KMS integrates

[27:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1621s) very well with all the solutions that we are using, namely,

[27:04](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1624s) sorry, namely S3, RDS, SQS, ElastiCache, Secrets Manager,

[27:11](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1631s) so all these solutions integrates very well with KMS,

[27:15](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1635s) and that enabled us to encrypt the data at rest

[27:19](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1639s) using customer managed keys.

[27:22](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1642s) Another aspect of it is how the,

[27:23](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1643s) how we secured the AWS services as such,

[27:27](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1647s) how did we secure AWS S3 bucket or SQS queue?

[27:32](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1652s) How we did it was, as the design principle states,

[27:35](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1655s) that this access should be provided at a very fine granular,

[27:41](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1661s) like at a very low level,

[27:43](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1663s) so we had individual roles created for each of the tasks

[27:47](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1667s) that have provisioned,

[27:48](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1668s) and the access to each of the resources

[27:51](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1671s) were provided at that particular role level.

[27:54](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1674s) So the access, the scope of access

[27:56](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1676s) was limited to very, the funnel was very small.

[28:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1681s) Moving on to the next, resilience.

[28:05](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1685s) This was, again, one of our key considerations,

[28:09](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1689s) and we had to take care of it right from the design level.

[28:15](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1695s) We had, we did it in like two ideas or two angles,

[28:21](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1701s) I would say.

[28:22](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1702s) One is loose coupling.

[28:24](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1704s) How we did that is we ensured that whenever we could use

[28:28](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1708s) asynchronous communication between the two services,

[28:31](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1711s) we used that using SQS queues.

[28:35](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1715s) How we would monitor that is if there is a particular system

[28:39](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1719s) which is at fault or which is facing issues,

[28:43](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1723s) it gives that time to that system or service

[28:45](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1725s) to recover without actually affecting the other systems.

[28:50](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1730s) The other area was fault isolation, so when we,

[28:54](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1734s) when we looked at the entire payment solution,

[28:57](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1737s) we first broke it down into individual processes, like,

[29:02](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1742s) the processes which can operate within itself and not,

[29:05](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1745s) does not depend on any other processes,

[29:07](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1747s) and then we created services for that.

[29:10](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1750s) So what happens is if one of the processes goes wrong,

[29:14](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1754s) the other process can still operate.

[29:18](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1758s) And another thing that we did is we implemented

[29:21](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1761s) feature roles where we could dynamically turn on

[29:25](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1765s) and off features if there are any issues.

[29:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1769s) So, I'll give you an example regarding that.

[29:31](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1771s) So let's say today, we noticed that a particular type

[29:35](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1775s) of transaction, let's just for namesake, let's use PayPal,

[29:38](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1778s) payer transaction is facing issues with it.

[29:42](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1782s) We have the capability in our system to turn off

[29:47](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1787s) just the PayPal payment option.

[29:50](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1790s) That will remove the PayPal option, even from the UI,

[29:52](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1792s) and the user does not get to see the PayPal option at all,

[29:56](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1796s) but all other types of payment,

[29:58](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1798s) like the card and everything will work absolutely fine,

[30:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1801s) and that gives us the time for our supporting industry

[30:04](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1804s) to go back, look at what's exactly happening wrong

[30:07](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1807s) in our system, fix it and then test it and then again,

[30:10](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1810s) roll it back, and then we turn

[30:11](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1811s) or turn it off automatically,

[30:14](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1814s) sorry, turn it on, and the system is back to normal

[30:17](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1817s) and there is zero downtime, literally.

[30:20](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1820s) So yeah, let's, so yeah, these two kind of

[30:26](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1826s) give us the capability to isolate the area of a problem,

[30:33](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1833s) isolate the damage and then recover from it

[30:36](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1836s) and then get the system back to normal as fast as we can.

[30:41](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1841s) Next was scalability.

[30:44](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1844s) Again, managed services to the rescue here.

[30:47](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1847s) We are using Fargate and Lambda

[30:51](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1851s) for most of our computation requirements,

[30:53](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1853s) and these, in our experience, scale extremely well,

[30:58](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1858s) so that kind of takes care of

[31:00](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1860s) most of our scaling requirement.

[31:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1861s) However, from our experience, we would strongly recommend

[31:05](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1865s) performance testing your application.

[31:08](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1868s) Every application's traffic patterns are different,

[31:13](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1873s) scaling characteristics are different,

[31:15](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1875s) so you should really do your application

[31:18](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1878s) based on your scaling characteristics

[31:20](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1880s) and your traffic pattern.

[31:23](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1883s) AWS provides you all the tools,

[31:25](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1885s) but it is our responsibility to you,

[31:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1889s) in our application to make most of it.

[31:34](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1894s) I mean, we did performance testing on our application.

[31:37](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1897s) Based on the observations, we did a lot of changes,

[31:40](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1900s) and that helped us tune our applications better.

[31:42](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1902s) For example, we changed the CPU and the memory

[31:47](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1907s) that was provided at the basic task level, ETS task level.

[31:51](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1911s) We also changed the scaling thresholds

[31:55](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1915s) based on how the application was,

[31:56](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1916s) the amount of time it was taking to provision new tasks.

[32:00](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1920s) We also changed the grace period

[32:03](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1923s) for the load balancer health check,

[32:05](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1925s) just so it does not conflict with the server startup times.

[32:09](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1929s) So, once we did all that, our application was performing

[32:14](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1934s) way better and it was able to handle the kind of loads

[32:17](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1937s) that AWS was expecting.

[32:19](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1939s) Apart from that,

[32:20](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1940s) there's one more, one bit of performance testing.

[32:22](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1942s) We validated that during the peak load,

[32:25](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1945s) we were not violating any kind of thresholds,

[32:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1949s) not the sort of quotas or any rate limitations

[32:33](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1953s) that are actually imposed,

[32:34](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1954s) so you need to test that, because you don't want to expose,

[32:38](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1958s) you don't want to face that in your production,

[32:39](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1959s) so it's better to face that

[32:42](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1962s) and then either get those rating mutations increased

[32:46](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1966s) or tune your application or design your application

[32:50](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1970s) in a different way.

[32:55](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1975s) Yeah, again, it's a enterprise application,

[32:57](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1977s) so support is a big part of it,

[32:59](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1979s) and to provide effective support,

[33:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1981s) you need to know exactly what's going on in your system,

[33:06](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1986s) not only at the infrastructure level,

[33:08](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1988s) but also at a process level, like whatever is,

[33:11](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1991s) what exactly happened to each and every transaction

[33:13](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1993s) that went through your system.

[33:15](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1995s) Now, observability generally consists of three pillars.

[33:19](https://www.youtube.com/watch?v=CjbqcbkU0so&t=1999s) I'll go one by one through each of them.

[33:22](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2002s) So, first was logging.

[33:24](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2004s) So we, our application,

[33:26](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2006s) our system generated two types of log.

[33:28](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2008s) One is the application log.

[33:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2009s) Obligation log is noting the record of events

[33:33](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2013s) that occurred in the system,

[33:35](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2015s) so it will record something like this event occurred,

[33:39](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2019s) this was the service that handled it,

[33:41](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2021s) what's the timestamp, what's the details of it,

[33:44](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2024s) even what was the outcome, was it a success or a failure,

[33:47](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2027s) et cetera, and these application logs

[33:51](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2031s) were pumped into Splunk,

[33:53](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2033s) which kind of gave us the capability to search the logs,

[33:57](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2037s) like effectively search the logs.

[34:00](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2040s) The other type of log that our application do

[34:03](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2043s) was the request and response log,

[34:06](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2046s) so whatever requests and response we sent to our gateway,

[34:10](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2050s) we logged them in our buckets, in our S3 bucket.

[34:14](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2054s) Now, the interesting part of it is these,

[34:17](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2057s) since it's a request and response, it did have PII data,

[34:22](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2062s) and the moment you're talking about PII data,

[34:24](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2064s) you have additional set of restrictions

[34:26](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2066s) that you have to handle,

[34:27](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2067s) additional encryption that you have to handle,

[34:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2069s) so distributing these two types of logs in different sources

[34:34](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2074s) or different storage patterns helped us,

[34:36](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2076s) so using S3, how it helped us

[34:39](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2079s) is it helped us to enable encryption at rest.

[34:45](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2085s) That was one of our compliance requirement.

[34:48](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2088s) It also helped us create separate set of access routes

[34:52](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2092s) around these kind of logs,

[34:54](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2094s) because you can create a separate access control

[34:56](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2096s) for the buckets, and another area where it helps

[34:58](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2098s) is having the lifecycle policies.

[35:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2101s) It helped us automatically transition the logs

[35:04](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2104s) to archive it based on the business rules

[35:07](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2107s) that were specified.

[35:10](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2110s) Second here is metrics.

[35:11](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2111s) We use Dynatrace as our APM.

[35:15](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2115s) It's an agent-based solution where we had to install

[35:17](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2117s) these agents in our containers,

[35:19](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2119s) and that gives us a lot of visibility,

[35:21](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2121s) not only in terms of resources,

[35:24](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2124s) like how your servers are doing,

[35:26](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2126s) how, the application health and everything,

[35:28](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2128s) but it also lets you create a request call

[35:32](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2132s) across multiple services, so, and then obviously

[35:36](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2136s) it gives you a lot of monitoring capabilities

[35:37](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2137s) where you can configure alerts

[35:39](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2139s) based on multiple rules.

[35:41](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2141s) So, the third part is tracing.

[35:43](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2143s) Now, a transaction has got multiple stages

[35:49](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2149s) that across through the day, I would say, so there,

[35:54](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2154s) there are authorizations,

[35:55](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2155s) then there are capture, fraud detect,

[35:59](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2159s) and then the settlement,

[36:00](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2160s) which happens at a different time in the computation.

[36:03](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2163s) Now, some of these are valid API calls,

[36:07](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2167s) some of them are happening in a batch process,

[36:09](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2169s) but to effectively identify what happened in a transaction,

[36:13](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2173s) you need to be able to pull out all the details

[36:17](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2177s) corresponding to a transaction,

[36:19](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2179s) so what we did is there were two aspects to it again.

[36:24](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2184s) One thing was you had Dynatrace, which given us,

[36:28](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2188s) it gave us the ability to trace a request

[36:31](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2191s) across multiple services.

[36:33](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2193s) So you see like, oh, what was the,

[36:36](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2196s) if there was a failure, which service failed,

[36:39](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2199s) and what was the issue there?

[36:41](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2201s) Apart from that, we generated the logs in a certain pattern,

[36:45](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2205s) so we used descent format to export,

[36:48](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2208s) create the log increase, and one of the attributes

[36:51](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2211s) of the log descent was a tracing ID,

[36:54](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2214s) which in our case was transaction ID,

[36:56](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2216s) but all the services, be them batch processes

[36:59](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2219s) or being the APIs followed this pattern,

[37:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2221s) and now, and all of the logs being in the same source,

[37:05](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2225s) when you search with the particular transaction ID,

[37:07](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2227s) you could get all the events

[37:09](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2229s) that happened in a transaction in one shot,

[37:12](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2232s) and that will give you complete visibility

[37:14](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2234s) regarding what happened in a transaction.

[37:17](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2237s) So, yeah, so across these three areas, it covered that,

[37:22](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2242s) the application was very easy to support,

[37:24](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2244s) and it was very easy to find what happened to a transaction

[37:27](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2247s) or where the system was failing.

[37:33](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2253s) Next, another area of key area was maintainability.

[37:38](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2258s) Like, when we talk about maintainability,

[37:40](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2260s) these are the things that we are concerned about.

[37:45](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2265s) How easy it is to identify your fault.

[37:50](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2270s) Like, was there, where is the problem?

[37:53](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2273s) Next is how easy it is to introduce the fix into the system

[37:59](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2279s) or how easy it is to change the system.

[38:03](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2283s) If it might be a new feature, or it might be fixed,

[38:05](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2285s) but how easy it is to change the system.

[38:08](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2288s) And the third is how easy it is

[38:10](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2290s) to actually do a production release.

[38:12](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2292s) Like, do you have enough confidence in it?

[38:16](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2296s) Now, there are a few areas that helped us do that.

[38:19](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2299s) One was using microservices again.

[38:22](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2302s) Very, each service having very isolated,

[38:25](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2305s) already specific purpose,

[38:28](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2308s) so whenever you see an issue in production,

[38:30](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2310s) you know exactly which service is responsible for it

[38:33](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2313s) and what you will have to change.

[38:36](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2316s) So, your focus is restricted to a very small area,

[38:41](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2321s) and thereby it's very easy to change.

[38:42](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2322s) Also, the things that you are doing,

[38:45](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2325s) you're pretty sure that

[38:46](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2326s) it's not effecting a lot of areas.

[38:48](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2328s) You know exactly that,

[38:50](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2330s) which area of the code is getting affected by it,

[38:53](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2333s) so that kind of reduces the risk of a change in your system.

[38:57](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2337s) Next was, okay, I've done the change.

[39:00](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2340s) Now, how do I ensure that

[39:03](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2343s) it does not have any collateral damage?

[39:05](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2345s) Like, did it break anything else?

[39:07](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2347s) For that, all our testing integration, as well as innate,

[39:11](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2351s) obviously, but everything was automated,

[39:15](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2355s) so every time we did a small or a big thing, doesn't matter,

[39:18](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2358s) we run the entire suit, and having it automated means

[39:21](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2361s) it was fast and there was hardly any cost of running it.

[39:24](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2364s) So, you validate your system,

[39:27](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2367s) you're okay with the change now, but then it's a production.

[39:30](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2370s) That means you're always scared.

[39:32](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2372s) So, having a very effective CI/CD pipeline helps.

[39:37](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2377s) What CI/CD does is not only reduces your window,

[39:41](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2381s) but it also, it reduces the chances of any error

[39:47](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2387s) or manual edits in the process,

[39:50](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2390s) so you're more confident that,

[39:53](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2393s) about your releases and what will go into the production.

[39:56](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2396s) So again, with the combination of all these three areas,

[40:00](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2400s) what it does is it gives the developer a confidence

[40:04](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2404s) to do a change, as well as the business

[40:06](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2406s) to introduce this into production.

[40:10](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2410s) Now, this, all this is,

[40:13](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2413s) was how the, how it was designed to address all the areas,

[40:19](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2419s) our concerns of ETS,

[40:21](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2421s) and the question is whether it did or not.

[40:24](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2424s) I'll let Brian answer that.

[40:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2429s) This is, I'm a talker, so this is now my chance to talk.

[40:35](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2435s) It'll kind of be a little funny.

[40:37](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2437s) So, I have a love/hate relationship with this project.

[40:41](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2441s) The love was that it exceeded every expectation

[40:46](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2446s) from the standpoint.

[40:47](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2447s) Oh, my mic.

[40:51](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2451s) Yeah, so sorry, a love/hate relationship with this project,

[40:55](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2455s) because number one, we were under extreme duress.

[41:00](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2460s) Our vendor came to us, gave us 15 months.

[41:03](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2463s) We had already been planning to do a long-term investment

[41:07](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2467s) and get off the platform,

[41:08](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2468s) but we had a very short period of time.

[41:10](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2470s) So, what I'll say is extreme exuberation when last,

[41:16](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2476s) this past June, we went live with our payment system,

[41:20](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2480s) thanks to our partners PwC and my great team,

[41:24](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2484s) and everybody at ETS that supported us,

[41:27](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2487s) but the thing is it would not have been possible

[41:30](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2490s) with a technology that was not available to us.

[41:35](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2495s) The AWS platform really made it possible.

[41:38](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2498s) I currently operate six different environments,

[41:42](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2502s) which I can freely unencumber.

[41:45](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2505s) It is a little bit costly from an overhead,

[41:48](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2508s) like, time perspective, like when we're doing releases,

[41:53](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2513s) but the thing is I've done 20 releases since June.

[41:57](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2517s) We do a release every sprint into production.

[42:00](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2520s) It's very quick.

[42:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2521s) It, everything kind of, we do all of

[42:03](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2523s) our feature refinements, do our bug fixing,

[42:07](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2527s) whatever we have, and then every release

[42:10](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2530s) goes out like clockwork.

[42:11](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2531s) Pretty much two weeks, you can set your watch to it.

[42:14](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2534s) So through automation,

[42:16](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2536s) through everything that's been talked about,

[42:18](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2538s) like, it's unimaginable as to what we can do.

[42:22](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2542s) It's also unimaginable in terms of what we've talked about

[42:26](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2546s) having features being able to be turned on and turned off.

[42:30](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2550s) When we went live,

[42:31](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2551s) we thought the big bang was gonna be great.

[42:34](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2554s) This is where I talk about love/hate, right?

[42:36](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2556s) The exuberance of going live in June

[42:39](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2559s) was a huge weight off the shoulders.

[42:41](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2561s) I manage the application.

[42:43](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2563s) I have a team.

[42:44](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2564s) We were all very excited,

[42:46](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2566s) only to find out not everything is perfect.

[42:49](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2569s) We're trying to make that transparent to our customers,

[42:51](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2571s) trying to make that transparent

[42:53](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2573s) to our accounting department.

[42:54](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2574s) We're trying to make that transparent

[42:56](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2576s) to our management, right, in how we handle things.

[43:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2581s) Everything that we talked about from an example standpoint,

[43:05](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2585s) that's not just talk, that, what they're,

[43:09](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2589s) what they're presenting in terms of their architecture,

[43:12](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2592s) all of that actually came true.

[43:14](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2594s) So, our cycle times were cut down

[43:16](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2596s) from our ability to bug fix.

[43:19](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2599s) We can turn off a problematic payment method

[43:22](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2602s) when our partner has an issue,

[43:25](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2605s) like the authorizations aren't happening properly

[43:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2609s) or the fraud detection engine isn't quite tweaked properly,

[43:33](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2613s) we can easily go in and turn off these features.

[43:36](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2616s) I can turn off these features.

[43:38](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2618s) I mean, I can't stress enough.

[43:40](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2620s) ETS has like, 15 maybe internal payment systems

[43:44](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2624s) or internal order systems to handle

[43:47](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2627s) each of these test registrations distinctly,

[43:50](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2630s) so it's like having 15 different partnerships.

[43:53](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2633s) Then I have external companies who do work

[43:55](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2635s) on behalf of ETS that connect to us,

[43:58](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2638s) so I'm effectively a service provider

[44:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2641s) and I'm providing all of this service every two weeks,

[44:04](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2644s) releasing production, customers don't know we have,

[44:09](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2649s) we do our deployments, the microservice bleeds out

[44:13](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2653s) or the container bleeds out,

[44:15](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2655s) and then the next one comes up and start handling the load.

[44:18](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2658s) So, we don't necessarily have to stop, integrate,

[44:22](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2662s) do all this testing,

[44:23](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2663s) bless you, with all of the different systems that we have.

[44:27](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2667s) If I had to stop and do testing

[44:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2669s) really rigidly with all these different vendors

[44:34](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2674s) and different payment systems we have,

[44:36](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2676s) we'd never get anything out the door.

[44:38](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2678s) And so from an iterative approach and from our environment

[44:43](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2683s) approach with having all these environments,

[44:45](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2685s) it allows us to be extremely flexible.

[44:48](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2688s) Internally we have, we modeled a,

[44:52](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2692s) like a mock payment system.

[44:54](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2694s) So basically we have our own internal,

[44:58](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2698s) we don't go out to the vendor

[45:00](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2700s) so we can do performance testing.

[45:02](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2702s) We can do all kinds of different testing

[45:05](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2705s) on different environments and have different purposes

[45:07](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2707s) for those types of things,

[45:09](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2709s) and so with AWS, it's been extremely easy.

[45:14](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2714s) I can turn off the environment.

[45:16](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2716s) So if I need right now, I need them all,

[45:18](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2718s) but I couldn't imagine doing this

[45:21](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2721s) back in our previous arrangements.

[45:25](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2725s) We've already processed 1.5 million transactions

[45:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2729s) since we started, which is really incredible.

[45:32](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2732s) I've had almost no service issues whatsoever.

[45:37](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2737s) As a matter of fact, this morning, before this presentation,

[45:41](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2741s) I won't get too much into the detail,

[45:42](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2742s) but I had like a little flare up.

[45:45](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2745s) So Dynatrace sends me a note, I get an instance,

[45:48](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2748s) I contact my lead developer, we look into the issue,

[45:53](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2753s) I talk to the product owner, we come to a resolution,

[45:56](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2756s) we wait 15 minutes,

[45:58](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2758s) the services are self-resolving, self-healing,

[46:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2761s) we find out there's a issue with our vendor, temporary,

[46:04](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2764s) but all of that, within a matter of a half an hour,

[46:07](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2767s) it literally took me longer to log and document the incident

[46:11](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2771s) for the rest of the company than it did to handle

[46:15](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2775s) and understand, troubleshoot,

[46:16](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2776s) get to the bottom of it and make sure

[46:19](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2779s) that my customers weren't impacted.

[46:21](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2781s) So, that's a reality that is just the part of

[46:24](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2784s) the love of where we are with this system.

[46:28](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2788s) Earlier, they talked about,

[46:30](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2790s) I'm gonna leave some time for questions,

[46:32](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2792s) but ETS struggled with currency

[46:35](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2795s) and providing local currency options to customers.

[46:40](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2800s) So we have a dynamic currency conversion option,

[46:43](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2803s) so if you have a credit card that's issued

[46:46](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2806s) in a particular country, and you want to use

[46:49](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2809s) that payment method and that is gonna be

[46:52](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2812s) in a particular method of currency, instead of having to pay

[46:55](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2815s) in US currency, we can now dynamically offer

[46:58](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2818s) almost any currency in the world,

[47:00](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2820s) which is converted into real time,

[47:02](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2822s) and so that's a flexibility option

[47:06](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2826s) we never thought we'd have.

[47:10](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2830s) The other thing is I talked about

[47:12](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2832s) adding new payment methods.

[47:14](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2834s) When we first went live, we had all these payment with it.

[47:18](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2838s) So we went with a big bang, we started them all,

[47:21](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2841s) and then we realized, oops, this one needs tweaking,

[47:24](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2844s) we shut it off, we turned it back on, we shut it off,

[47:27](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2847s) we turned it back on.

[47:28](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2848s) We had multiple attempts, but we had that flexibility.

[47:30](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2850s) I didn't need to do releases.

[47:33](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2853s) One of the things about managing this application,

[47:35](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2855s) which is really great, is I can have like one service.

[47:39](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2859s) I can say, oops, break, fix, we need to go

[47:42](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2862s) and identify the payment UI service.

[47:44](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2864s) We go particularly get that service up and running

[47:49](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2869s) or get that container up and running and deal with that.

[47:52](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2872s) We don't have to deploy the entire application

[47:55](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2875s) across its mass.

[47:57](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2877s) We have, I dunno, probably somewhere between 15

[48:00](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2880s) and 20 different services that are running.

[48:03](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2883s) So, I can surgically do whatever I need to do

[48:07](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2887s) or the team needs to do in order to manage the application.

[48:10](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2890s) It's a really, a really great thing.

[48:16](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2896s) And with any system,

[48:18](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2898s) you want to be able to pay back your investment,

[48:21](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2901s) so for a lot of different reasons,

[48:23](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2903s) we're on target to definitely recover our investment

[48:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2909s) within the amortization period that we put together,

[48:32](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2912s) so that's a positive for ETS.

[48:35](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2915s) So, anytime you want to invest,

[48:38](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2918s) you always want to make back your money,

[48:41](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2921s) and I look at our infrastructure and you think like, hey,

[48:44](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2924s) we got six of these different environments

[48:47](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2927s) that should be costing, like in a data center,

[48:49](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2929s) it would cost us tons and tons of money,

[48:52](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2932s) and in AWS, our monthly costs are pretty reasonable,

[48:56](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2936s) so again, that's something we couldn't have really,

[49:00](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2940s) couldn't have planned it better, so.

[49:04](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2944s) I think that's about all I want to cover.

[49:08](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2948s) So, we thank you very much for coming.

[49:11](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2951s) I appreciate everybody's attention today.

[49:13](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2953s) Gokul, do you have any final thoughts

[49:15](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2955s) or want to open it up for questions?

[49:26](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2966s) So thank you everyone for coming today

[49:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2969s) and listening to our experience

[49:32](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2972s) and patiently listening to us

[49:36](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2976s) talk about how we built the system.

[49:37](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2977s) So, happy to take any questions if you have.

[49:40](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2980s) We are also available here,

[49:42](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2982s) we have a booth here in, for PwC,

[49:44](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2984s) so happy if you want to stop by there

[49:46](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2986s) and have some questions, have a chat on the solution,

[49:47](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2987s) happy to do that as well, so.

[49:53](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2993s) I'm just curious, something I had back of mind

[49:55](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2995s) when I read your request.

[49:56](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2996s) Is there a reason why you didn't use load primes

[49:57](https://www.youtube.com/watch?v=CjbqcbkU0so&t=2997s) or M1 theme templates?

[50:00](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3000s) Yeah, so I'm happy to answer that.

[50:02](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3002s) So there are, there are some areas where, like I said,

[50:07](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3007s) speed to market was very important.

[50:08](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3008s) There was some existing investments already in play.

[50:12](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3012s) It was working very well.

[50:14](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3014s) We didn't want to really boil the option.

[50:15](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3015s) We wanted to make sure that it works with,

[50:18](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3018s) because this is not the only solution

[50:19](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3019s) that is leveraging this.

[50:20](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3020s) There are other parts of the enterprise,

[50:22](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3022s) which are leveraging that'll all work together,

[50:25](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3025s) so we wanted to make sure that continues,

[50:26](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3026s) and we didn't have to worry about

[50:27](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3027s) that part of the equation.

[50:32](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3032s) Yes.

[50:37](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3037s) Was there anything you could query specifically

[50:39](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3039s) that you could think of that ADM did not grow

[50:42](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3042s) or slow down the building process?

[50:44](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3044s) Yeah, like our, so one of the things we did,

[50:48](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3048s) just in an agile manner,

[50:50](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3050s) I've always had an embedded testing group,

[50:52](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3052s) so they wrote the tests, they wrote the automated tests,

[50:55](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3055s) we built that into the pipeline,

[50:57](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3057s) so each battery of tests is set to run

[51:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3061s) on its particular environment, and as I mentioned,

[51:04](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3064s) some of those environments connect to the vendors,

[51:06](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3066s) some of them are mock, so basically we've canned responses,

[51:10](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3070s) so when I have a application system contact me,

[51:14](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3074s) it's part of the hate relationship.

[51:16](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3076s) So I'm effectively managing my own gateway

[51:19](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3079s) because if you sent me a transaction for $50,

[51:23](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3083s) I've got a canned response for that

[51:25](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3085s) to give you an accept or decline.

[51:27](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3087s) I've given you a card, so I maintain that environment,

[51:30](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3090s) so I'm able to continuously run that with my partners

[51:33](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3093s) and let them do that consistently, and internally,

[51:37](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3097s) we just run those tests all,

[51:39](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3099s) like every day there's regression being run

[51:42](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3102s) that the tester runs it on every environment

[51:46](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3106s) because they're slightly different,

[51:48](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3108s) but from that standpoint,

[51:51](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3111s) it really has not been a hindrance to us.

[51:56](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3116s) Any other like, thoughts or more specificity

[51:59](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3119s) that you wanted?

[52:00](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3120s) , No, really,

[52:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3121s) we're going into a major release of our accounting software.

[52:04](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3124s) Okay.

[52:05](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3125s) It seems that having to monitor everything,

[52:07](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3127s) real monitoring is when you, everything is set up

[52:10](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3130s) in terms of a testing environment,

[52:11](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3131s) and that is a real problem.

[52:14](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3134s) It takes longer and longer to run.

[52:15](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3135s) Sure, yeah, yeah.

[52:18](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3138s) Yeah, I get that.

[52:20](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3140s) We limited the number of tests

[52:23](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3143s) that we were able to like, run, so I don't, that's,

[52:27](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3147s) that was one of the reasons why we had the mock system,

[52:30](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3150s) so there's only X number of scenarios they could run,

[52:34](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3154s) but it's probably different for an accounting system

[52:36](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3156s) versus the payment system, because I have X number

[52:39](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3159s) of card types, or a decline of 3DS.

[52:43](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3163s) I mean, I'd say there's probably, maybe 40 scenarios or so,

[52:48](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3168s) maybe slightly more, but yeah,

[52:51](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3171s) like the more features you have, the different, but again,

[52:54](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3174s) if you're in a microservice environment,

[52:56](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3176s) you're not touching one aspect,

[52:58](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3178s) you don't necessarily have to worry

[53:00](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3180s) about the intensive testing there.

[53:02](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3182s) You can focus.

[53:03](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3183s) That's correct.

[53:04](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3184s) Exactly, yeah.

[53:05](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3185s) So one more area that we,

[53:07](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3187s) what we did was used to tag the test cases,

[53:11](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3191s) and so that would let you run specific test cases

[53:15](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3195s) corresponding to the release.

[53:16](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3196s) So not always in all releases

[53:19](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3199s) we would run the entire battery of the test,

[53:21](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3201s) so we would focus on the areas where we are touching.

[53:24](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3204s) So for example again, if you are touching the credit card,

[53:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3209s) there's not like,

[53:30](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3210s) PayPal is not really required to be tested, right?

[53:34](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3214s) So we had like, correct tags,

[53:37](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3217s) I will say, to each test cases, and then during the release,

[53:39](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3219s) we would run only the tags which are relevant to it,

[53:42](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3222s) not the entire battery.

[53:45](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3225s) There was another question here, I thought, somewhere.

[53:48](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3228s) Yeah, I was wondering if we can come back to

[53:51](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3231s) the log subtypes, so what are these meant to do

[53:54](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3234s) to log and secure and downsize risk?

[53:58](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3238s) I don't think that was made very clear.

[53:59](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3239s) Yeah, so when Mrinal was talking about

[54:02](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3242s) the different levels of security,

[54:04](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3244s) so we have tokens that people need to use,

[54:08](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3248s) so we have external systems and internal systems

[54:12](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3252s) that are connecting to us,

[54:13](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3253s) so each of those needs a unique token.

[54:16](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3256s) Also, we need to have a valid signing, field signing,

[54:21](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3261s) so when you send me data,

[54:23](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3263s) I know we have a mutual understanding of what that hash is,

[54:27](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3267s) so if you send me data that doesn't match,

[54:30](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3270s) I'm pretty much not gonna accept it

[54:31](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3271s) because it doesn't meet the hash requirement as well,

[54:36](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3276s) and then at each entry point, each touch point,

[54:39](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3279s) we have all security measures related to the tokens

[54:43](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3283s) and the handshakes that are happening,

[54:47](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3287s) plus the encryption across the entire system.

[54:51](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3291s) And also, like, your question is like,

[54:53](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3293s) it's too broad to answer them like one simple tool,

[54:56](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3296s) but like, any incoming traffic, you have the gateway,

[55:00](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3300s) you had the firewalls in place to be able to handle that.

[55:04](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3304s) Right, and then there's Akamai on the outside,

[55:06](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3306s) so it's just, there's a whole lot of different points,

[55:09](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3309s) not one single point of security.

[55:11](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3311s) That was also key,

[55:12](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3312s) was to have different varied levels of security.

[55:17](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3317s) Thanks.

[55:19](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3319s) Yeah.

[55:20](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3320s) Okay, so I wanted to know,

[55:23](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3323s) are there other gateways that we can use in terms of the?

[55:27](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3327s) Yeah, so first of all, ETS

[55:30](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3330s) and its gateway provider Fiserv,

[55:33](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3333s) the reason we chose them was,

[55:35](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3335s) or one of the implementation methods that we chose with them

[55:40](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3340s) was to keep our existing PCI level,

[55:42](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3342s) so ETS does not collect PAN data, credit card data,

[55:47](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3347s) our payment vendor does that,

[55:49](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3349s) and so we get an insecure token that comes back,

[55:54](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3354s) so it's basically just a number that has nothing to do

[55:57](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3357s) with the person's credit card data,

[55:59](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3359s) so I don't have to worry about protecting that

[56:02](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3362s) because the Fiserv's embedded payment JS,

[56:06](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3366s) they're the ones who directly take that,

[56:08](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3368s) they provide me a token value in return and they handle

[56:11](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3371s) the credit card part of it.

[56:13](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3373s) From our standpoint, from PII,

[56:16](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3376s) personally identifiable information for customers,

[56:19](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3379s) it's very important to us.

[56:20](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3380s) So, as these guys talked about,

[56:22](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3382s) we have KMS encryption on every piece of data at rest,

[56:26](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3386s) so it's extremely important for ETS to make sure

[56:31](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3391s) that all of our data's secure in that manner,

[56:34](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3394s) and so, even in our logs,

[56:36](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3396s) so we don't have any credit card data,

[56:39](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3399s) and in addition to not storing the credit card data,

[56:42](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3402s) the customer's personal data is also protected

[56:45](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3405s) by being encrypted.

[56:46](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3406s) The only people who have access to view any of that data

[56:50](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3410s) are people who are vetted within our system,

[56:53](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3413s) and they have access to those logs through the,

[56:57](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3417s) we built a backend management tool.

[57:00](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3420s) So for example, if I'm doing an order search

[57:02](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3422s) and I'm looking for your transaction, I go in,

[57:05](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3425s) I look up your transaction,

[57:06](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3426s) and if I need to know what happened to that,

[57:09](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3429s) so there's a lay person's view,

[57:12](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3432s) but then you can also click on a button

[57:14](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3434s) right in the transaction and it'll present the log,

[57:17](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3437s) which is useful for troubleshooting.

[57:18](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3438s) So customer service representatives

[57:20](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3440s) or our internal treasury department can look up

[57:23](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3443s) that information and get to the bottom

[57:25](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3445s) of why a customer's payment might've been declined,

[57:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3449s) because we interpret things from our vendors like Fiserv

[57:33](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3453s) for example, but sometimes you need to look at

[57:35](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3455s) the raw message to see exactly what happened,

[57:38](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3458s) so that's the point of why we kept the logs,

[57:40](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3460s) but it was very important that we have both user level,

[57:44](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3464s) as well as disk level encryption on being able

[57:48](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3468s) to access those logs.

[57:49](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3469s) Not anybody can get to them.

[57:51](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3471s) Yep.

[57:53](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3473s) Yes.

[57:55](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3475s) First wanted to say that I enjoyed the presentation.

[57:59](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3479s) Thank you.

[58:00](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3480s) Second part is what service do you use ECS

[58:06](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3486s) of the literally the thousands of ECS in the market?

[58:11](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3491s) So I'll answer the first question first.

[58:13](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3493s) There was no challenges.

[58:14](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3494s) I mean like, like every system, right,

[58:17](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3497s) you need to, there's a level of tuning that needs to happen,

[58:22](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3502s) which is what Mrinal was talking about.

[58:23](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3503s) As you start scaling up workloads,

[58:25](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3505s) as you start doing your testing,

[58:27](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3507s) there's a level of configuration changes that you'll have

[58:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3509s) to do with that comes with any service.

[58:33](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3513s) It's just easier if it's a managed service.

[58:35](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3515s) The question around ECS with like an EKS

[58:38](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3518s) is more directionally where an organization is

[58:41](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3521s) and what services are allowed, services at that part of time

[58:45](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3525s) when the decision was made,

[58:46](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3526s) so that was a big part of why we went with ECS.

[58:50](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3530s) It was not a technical challenge,

[58:52](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3532s) it was more an operational perspective.

[58:54](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3534s) Yeah, at the time, at ETS,

[58:56](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3536s) we didn't have a lot of operational support and knowledge

[58:59](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3539s) on the IT side to support a lot of Lambda functions,

[59:02](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3542s) so we mainly went with the ECS, yep,

[59:08](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3548s) and I, it's been great, actually, I can't complain at all.

[59:13](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3553s) How do you manage the process?

[59:16](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3556s) Cold start.

[59:17](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3557s) So we used, we did not use Lambda as part of

[59:23](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3563s) any of our direct synchronous processes.

[59:26](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3566s) We used Lambda mainly for our backend processes.

[59:29](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3569s) So cold start was not an issue for us

[59:31](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3571s) because in the backend processes for,

[59:33](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3573s) even if it's one or two seconds delayed,

[59:35](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3575s) it didn't matter to us, with ECS Fargate,

[59:38](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3578s) and that was one of our considerations also.

[59:41](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3581s) That's why we picked and choose where we would use Lambda

[59:45](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3585s) and where we would use ECS Fargate.

[59:46](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3586s) Yeah, and I was gonna say like,

[59:48](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3588s) I'm constantly, as the nervous application manager,

[59:52](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3592s) I'm constantly saying, is this gonna impact,

[59:55](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3595s) do we have to report a service downtime

[59:57](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3597s) when we're doing this release?

[59:58](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3598s) And the bottom line is nine times out of 10,

[01:00:02](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3602s) the answer always came back as no.

[01:00:04](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3604s) My engineer is saying, nope, this is gonna bleed out

[01:00:07](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3607s) the other container is gonna come up,

[01:00:09](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3609s) and then you're gonna have that capability in production,

[01:00:12](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3612s) just like that, and it's kind of like a seamless fail over.

[01:00:15](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3615s) So, that was another benefit, I think,

[01:00:18](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3618s) to doing that technology versus having the cold start.

[01:00:23](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3623s) And just to finish off, a stat that I didn't report out:

[01:00:27](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3627s) we've had, in that six months or so, close to six months,

[01:00:32](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3632s) one planned downtime in that entire time in 20 releases,

[01:00:38](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3638s) so only one time did I have to tell

[01:00:40](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3640s) all the application systems, we're bleeding out,

[01:00:44](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3644s) I need everybody to shut down,

[01:00:45](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3645s) and it was because we basically had multiple

[01:00:49](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3649s) database infrastructure type things that we needed to do

[01:00:52](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3652s) at that time, but that's like a dream come true.

[01:00:56](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3656s) It's just been great in that sense.

[01:00:59](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3659s) All right, thank you.

[01:01:00](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3660s) Thank you very much, everyone.

[01:01:01](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3661s) We appreciate it.

[01:01:03](https://www.youtube.com/watch?v=CjbqcbkU0so&t=3663s) (audience applauds)

