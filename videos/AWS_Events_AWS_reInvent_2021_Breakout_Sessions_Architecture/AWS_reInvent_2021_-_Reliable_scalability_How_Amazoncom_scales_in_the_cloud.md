# AWS re:Invent 2021 - Reliable scalability: How Amazon.com scales in the cloud

[Video Link](https://www.youtube.com/watch?v=_AhfV5LZmvo)

## Description

Amazon.com launched in 1995 with a modest architecture and a grand vision to be Earth’s most customer-centric company. Learn how Amazon.com got big fast, and see their evolution from a monolithic architecture to a massively scalable system based on service-oriented architecture and microservices. With examples of real-world production workloads from Amazon.com, Ring, and Prime Video, learn how Amazon uses mechanisms to review and test cloud workloads at scale, and how they reliably process millions of transactions per day using the elasticity of the AWS Cloud. Come see how Amazon.com uses AWS to achieve customer obsession at scale.

Speakers:
Seth Eliot, Principal Reliability Solutions Architect
Kieran Kavanagh, Principal AI/ML Solutions Architect

Learn more about re:Invent 2021 at https://bit.ly/3IvOLtK

 
Subscribe: 
More AWS videos http://bit.ly/2O3zS75 
More AWS events videos http://bit.ly/316g9t4

ABOUT AWS
Amazon Web Services (AWS) hosts events, both online and in-person, bringing the cloud computing community together to connect, collaborate, and learn from AWS experts.

AWS is the world’s most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally. Millions of customers—including the fastest-growing startups, largest enterprises, and leading government agencies—are using AWS to lower costs, become more agile, and innovate faster.

#AWS #AmazonWebServices #CloudComputing

## Transcript

- All right, I think
it's time to start here. Welcome, everyone. I am so thrilled to be here in front of a live
audience after two years, and I'm so glad you're all here with us. You're here to talk about
reliable scalability, how Amazon.com scales in the cloud. My name is Seth Eliot. Just a little bit about me. I'm with AWS now. I'm the reliability lead
for AWS Well-Architected and been with AWS for
a couple of years now, but I spent the prior eight
years with Amazon.com. And so, when we talk about
Amazon.com in this case, we're talking about the
site you buy stuff from. We're talking about where you
go to buy a Kindle, or a book, or even download or stream
a movie from Prime Video. So that's the Amazon.com
we're talking about today, whenever we were refer to Amazon.com. I had several roles. I've been on the Prime Video team when it was founded way back when. In 2008, I've been on the content ingestion team, Amazon Fresh. But my most recent role
before I transferred to AWS was with the team working across
the entirety of Amazon.com with our thousands of
developers of how they develop and implement in AWS. And in that role, I partnered
with our AWS support team. Amazon.com, we, back then, was a customer, is a customer of AWS. And our support team, my counterpart on that
support team, was Kieran, and Kieran's here to
talk with you also today. - Thank you, Seth. Yes, hi everybody, my
name is Kieran Kavanagh, and I'm a principal
solutions architect at AWS. I currently specialize
in machine learning, but prior to that, I
worked as a generalist SA on the Amazon.com account
as Seth was saying. So back then, Seth was
actually a customer of mine. We've been working together
for quite some time now. And where better to
begin our journey today than at the actual beginning. What you see here is the
Amazon.com Books website from 1995, and you can see it's not quite
as advanced and feature-rich as the website that Amazon has nowadays, but this was pretty
standard for the mid '90s. What is impressive here is that they already had 1 million titles, so they were already
earth's largest bookstore. And let's take a look at the
architecture that was used to serve this website, the customers. Started off pretty simple. What you see here is a customer
coming in over the internet. The first thing that they interact with is something called Obidos. That was the web server layer, and that was a single monolithic service. We'll talk a little bit
more about that later. And it connected directly
to a single Oracle database in the backend, which was called the
Amazon.com Books Database, or ACB Database. And this database had
everything that was needed to do business on Amazon's website. You had a table for all of the customers, you had a table for all of the inventory, and you had a table that
tracked what customers were purchasing from the inventory. You can see here also
that Amazon started off with one distribution center for sending out packages to people. And also, you'll see this thing called the credit card motel. What's interesting about
the credit card motel is that once you checked a piece of credit card
information in there, you could no longer humanly read it back. The only piece of code that could access that credit card details was a small piece of code
that actually connected to the banking institutions
to make a purchase when somebody's purchasing
something on Amazon.com. So security was built in
from the very beginning. It was a major priority, even from the very first version
of Amazon's architecture. And Amazon wanted to get big fast. What you see here in the
top right hand corner is a picture of a t-shirt from a company Picnic that
took place back in 1997. And you can see the slogan says, "Get big fast, have another hot dog." That is one way of getting big fast, but that's not what we're
gonna talk about today. We're gonna talk about
scaling out the architecture. I'm just beginning first
with a quick definition. When we talk about scalability, we say it's the ability of a workload to perform its agreed function when the load or scope changes. So if you keep getting
lots of more traffic onto your system, you wanna make sure that
your system scales up and that it continues to do
what you expected it to do. Now, before we dive into how Amazon scaled out their architecture, I wanna first ask you to
take a moment to think about, with pretty much any
web-based architecture, what is one of the first
components in the architecture that becomes a scaling concern? Yes, you guessed it
right, the database layer. And that's exactly what Amazon
started to scale out first. one of the first things
they did in this regard is they created a separate
database called Web 1 that was just for orders. Now, why is this important? When you think of any e-commerce platform, the ability for people to
make orders on that platform is one of the most important things that the platform can do, right? That's one of the most
important functions. And so, there was this dedicated database and a dedicated path for
people to make orders, so that if other stuff was going on with the central ACB database, the orders had its own separate workflow that wouldn't be affected
by any congestion there. And this orders table then was being synchronized periodically back
to the central ACB database. And as Amazon grew over time, they added more distribution
centers of course. If you're sending out more
and more packages to people, you have more and more customers growing, and you need more distribution centers to meet all of their demands. And each distribution center
had its own dedicated database. So this is another way
that they scaled out the database layer. And this continued to grow. The distribution centers grew to about 175 and a number of databases
grew to more than 300. These were all Oracle databases, but they've all recently been deprecated or they've all since then been deprecated. And now Amazon is using all AWS database technologies instead. So the final Oracle
database was shut down by Amazon's retail business back in 2019. And now that we've talked about scaling at the database layer. What is the next component
in our architecture here that we need to think about scaling? Yes, you guessed it right
again, the application layer. And this is the Obidos piece
that I talked about here. This was the single monolithic service that contained all of the business logic required to do everything
on Amazon's websites. And every new feature that was being added was all being added to
this single code base. So when Amazon added one
shopping, for example, that was added to Obidos. Every bug fix, every feature was all being added to
this single code base. And Obidos grew a lot over time. In fact, at one point, it got to the stage where it was taking 12 hours to build it. So if you wanted to make a change and you kick off a build, then you would either go about your day or maybe it's in the evening time, you go to sleep for the night, you come back 12 hours later and you just hope and really hope that what you intended to do worked, 'cause otherwise you have to
go through all of that again. And as you can see, this is not really scalable in the long term, and this is not really scalable, especially as you are employing
more and more developers and they all want to be adding
things to this code base. So one of the first things
that Amazon did in this regard is they started to break it
out into separate components. The first one that they broke
out was the customer service, and this was a service that was used for interacting with customer information. So there was a dedicated customer
database that was created. So they're scaling out the database layer in this case again. And also, the customers were regionalized. So there was a different database for different customers
in different regions. What you're seeing here as an
example is the CustNA database is customers in North America. And if you wanted, if a new
customer wanted to sign up, they would interact with
the customer service in order to get their details
into that customer database. And also if a address was needed for printing a shipping label, the customer service would be
called to fetch that address. So this was one of Amazon's first steps towards a service oriented
architecture approach. And at the very beginning
of the customer service, you could almost say that it
was microservice because it... Even though microservices
weren't really a thing back then in terms of in the industry, people were talking about them a lot. But the customer service started off with a really dedicated set of functions and a dedicated database. And it just had a very
simple set of operations that it was doing. Most of its APIs were wrappers around SQL called into the database. But this then grew over time, and so people started adding more and more to the customer service because they were reluctant to be adding more and more to Obidos. And the architecture continue to scale. And if we look at some details around the kind of growth that Amazon has seen in the past few years, we're having a look at some details here from Prime Day earlier this year, where 175 million items were
purchased by Prime members just during that period. So that's a lot of
commerce that's going on on Amazon's website nowadays. And if we look at what that means in terms of AWS service usage, what kind of scalability
they have achieved there, during Prime Day this year, Amazon DynamoDB handled about almost 90 million requests
per second at peak. And if we take a look
at another example here, Amazon CloudFront processed more than 290 million requests
per minute during that time, totalling to 600 billion
requests during Prime Day. So there's some pretty serious scale that they've been achieving here. And now let's take a
look at what Amazon did to scale out their architecture to handle this kind of growth. Well, it turns out that after that first change that they made, this first thing of breaking
out the customer service. They didn't need to do
anything else after that. That solved all of the
problems from there onwards. Just kidding. This is actually what
Amazon's architecture looks like nowadays. It's an extremely vast and
complex web of microservices. And this is an actual
real picture, by the way. This is a picture from an
internal tool at Amazon that tracks deployed
services under dependencies. And we can even zoom in here
and look at one microservice that's connected to about
400 other microservices here. Everything I've talked about up until now has been around scalability, but this presentation is
called Reliable Scalability. So let's talk about
reliability for a minute. Starting off again with a definition. We said that reliability is
the ability of a workload to perform its required function
correctly and consistently. And when we couple that
with the scalability aspect, it means that no matter how
much your system scales, you want it to have the same service level agreements, et cetera. You wanna have the same kind of experience for your customers. This is the reliability aspect. And reliability is such an important part of pretty much any systems architecture that it has a dedicated pillar in the AWS Well-Architected Framework. The Well-Architected Framework is a collection of best practices that you can use to ensure that your systems are architected
to perform optimally. And reliability has its
own dedicated pillar. A pillar is basically a
category of best practices, and there are five in total. We'll be talking mainly
about reliability today and also operational excellence. This is where the
scalability aspect comes in. All of the pillars are very important. The other three are security
performance efficiency and cost optimization. All of these are very important for pretty much all workloads, but we'll be focusing
mainly on reliability and operational excellence today. And at this point, I wanna
hand you over to Seth to talk about how Amazon
architects these microservices that we've just been showing. - Thank you, Kieran. All right, yeah. So that was a little bit
history lesson on Amazon. Now let's dive into how
things are operating today. And we'll start off by talking about service-oriented architecture and microservices architectures. Now, for each of these subsequent sections we're gonna show you, we're gonna tie them into an
Amazon leadership principle. Now Amazon leadership principles are the 16 principles at all
Amazonians across the company. So keep in mind every day
when they're making decisions or doing tasks at Amazon. Is
this the right thing to do? Oh, let's refer back to
the leadership principles. So this one's bias for action. Speed matters in business. We value calculated risk taking. So I will hopefully tie it in how a service-oriented architecture, also called SOA, or
microservices architecture, can factor into that
speed and bias for action. And just real brief, just so
everybody's on the same page, just a little bit of just the sort of 101 of monolith versus SOA
versus microservices. So the monolith is what Kieran
was talking about, Obidos, a big binary, all changes
go into that binary. Everybody's kind of
beholden to that binary. If you wanna make a change, you gotta hope everybody
else's changes don't break you. It's big. It's unwieldy. There are maybe some valid
applications for monoliths today, but generally we try
to shy away from them. And service-oriented architecture, that's where we take
each of our applications, and make them a separate service, and have them communicating
with each other. So you might have a catalog service or even a catalog
ingestion service, right, as one of your services,
and microservices. Now let's break it down further. You can think about
taking those applications and breaking them down
into individual components, each a separate service
that does its own thing. So for that catalog ingestion service, maybe we have a service dedicated just to taking in merchant data that's being submitted to the catalog, and matching it with the existing catalog. That's a single microservice. So that's a microservices architecture. We're not gonna make a value judgment between SOA and microservices. They both have a place
and they're both good. I'm just gonna lump them together and just talk about them together
as generally not monolith. And towards that end, when you're using
microservices or even SOA, the nice thing about them is
the ability to deploy them and scale them independently, right? So if some need more
capacity in the AWS cloud, you can then ramp them
up with the elastic cloud and supply more capacity to them. Some need less capacity. You can give that capacity back. So you're not paying
for what you don't need. And the nice thing about AWS is using organizations
and consolidated billing. You can share that capacity
between your microservices. So one is scaling down,
you release that capacity, so another one could scale up. So again, it's just a real nice way AWS helps you keep that efficient. And ultimately at Amazon, they have 150 million
deployments per year. Now, to be sure not all of
these are major features, or major functionality, or even customer visible functionality, a lot of them may be
just utility deployments, things that get things out there. But still it just speaks
culture at Amazon. They have a culture of
continuous integration and continuous deployment and that high deployment lets them. So you can imagine this deployment, there's a huge stream going out the door and you could always be putting in the features and functionality
you need onto that stream. All right, so let's look at some examples of the microservices
architecture at Amazon. This is a page I think you should all be pretty familiar with. It's a detail page. It's a page where you go to Amazon.com or your local Amazon.com,
your marketplace, and you can buy stuff. You could look at the picture. You could look at the price.
You could look at the reviews, and then you could click add to cart, or as we talked about one-click ordering, you do one click ordering. So that's a detail page. Now if we take this same page and look at it using an internal tool that's available with an Amazon.com, it might look like this. And I don't know how it's showing
up on the big screen here, but each of those little arrows is pointing to a microservice. There's an image microservice. There's a title microservice. There's a stars rating microservice. So what's happening is
when you see a detail page, it's making hundreds of calls to hundreds of microservices in parallel marshaling them together very quickly and displaying to you
as a single detail page. The advantage here is, let's say the star rating
service is having an issue and it can't show you the star rating, it could still show you
the rest of the page, the image, the title,
the price, add to cart. It results in much higher
availability, reliability, and much higher scalability. Also, when I wanna make a change, if I wanna change the
title feature somehow, I don't have to like make a change to a big monolith, a big binary. I could just change that one microservice. Here's another example from Amazon.com. Back in 2019 Amazon.com
released a new feature called Subscription Boxes. Subscription boxes, you could
sign up to receive monthly a box of high quality items
in a certain category, like Green Kids Crafts, or
kid's toys, or coloring books, or whatever you want, right? There's a whole kind, Marvel merchandise, all kinds of subscription boxes. And they went to launch this in 2019. And this is the architecture for the Subscription Boxes
architecture that they launched. So let me walk you through it. Not that complex, right? You have an API gateway
right there on the front because it's a microservice. It has to present a set of APIs. So that's how it does it. It's got AWS Lambda, which is the AWS serverless functionality where you could deploy. And that contains the business logic. Business logic is deployed to Lambda, so it's able to execute the
business logic serverlessly. DynamoDB, which is the NoSQL database, where it's basically storing state, like who's subscribed to what, and on what date are they expecting to get their merchandise,
that kind of stuff. And the S3 bucket is
pretty much there for logs. Important, but just putting it on there to keep the logs so that they could do the monitoring and go back through the logs, et cetera. That's the architecture. Matter of fact, the team
that put this together comprised of three engineers, and they call it a nano service. They said it's not a
microservice. It's a nano service. It's that small. But ultimately handles
millions of events per day. So how could this be? How could I show you that
great, cool, new feature and yet that's the architecture? Because that's the key about microservice. Does this service have
to worry about pricing? No. Does this service have to
worry about the catalog? No, it calls the catalog
to get information. Is this a kid's craft? Is this a coloring book? Is this highly rated, right? Does it have to worry about fulfillment, sending the merchandise to the customer? No, it just has to worry about
which items they're gonna get and it tells fulfillment to do it. That's the key to microservices. It does one thing and one thing only, and delegates everything else to the other services around it. Ultimately, all right, so this is... We're gonna show several
of these slides today. So what this is... Kieran talked about the
Well-Architected Framework. Well, another part of the
Well-Architected Framework is the Well-Architected tool. The Well-Architected tool is free to use, available through the AWS console. And what the Well-Architected tool does is let you take those best practices that are described by Well-Architected and review your own workloads,
your stuff built in AWS, your own cloud-based workloads, and say, "Am I or am I not
doing these practices?" And based on that, it'll make improvement
recommendations to you. And it's done in a Q&A format. So the question is along the top there. In this case, how will you design your workload service architecture? And you can see in the underlying section, it's talking about SOA and
microservices architecture. The best practices are
the little check boxes. So in this case, the best practice is how you're gonna segment the workload. Are you gonna segment it big,
small microservices, SOA? And also, make sure that
segmentation maps to the business, to the business domains. So those are the best practices that Amazon is exhibiting in
the examples I showed you. And we're gonna refer back
to Well-Architected tool to show you the
Well-Architected best practices. Okay, for the next section, I'm gonna have Kieran talk to you. All right. - Thank you, Seth.
- Sure. - Okay, so now that Seth
has talked a bit more about how Amazon architects their systems in terms of microservices, let's now talk about how they
review and test those systems. Because of course, once
you design a system, you don't just launch it into production and see how it goes. You want to review and test
things before launching to ensure that what you've designed will behave the way you want it to. And this is in alignment
with the leadership principle on insisting on the highest standards where leaders continually raise the bar and drive their teams to
deliver high quality products. Now, it's important for me at this time to introduce the concept of mechanisms, which is a really important
part of Amazon's culture. This goes back to a quote from Jeff Bezos from many years ago,
when he was talking about if you want some kind of real sustainable change in your organization. He said that when you
ask for good intentions, you're not really asking for a change, because people already
had good intentions. Now, most people you meet, they try their best to be a good person. They try their best to be a good employee, to do well in their job. If they architect the system, they hope that that system performs as optimally as possible. So, if you want to improve something and you sit down with
your team and you say, "Hey, everybody, let's
make this thing better." And everybody says, "Yes, let's do it. That's not enough. You need some kind of mechanism to measure what you're doing, to ensure that you're
working towards the goal that you've been setting out. And your mechanism, as you
can see here in the graphic, generally, a mechanism will
take some kind of inputs, put them through some
kind of formalized process to produce some kind of expected outputs. And there will usually be
tools that are involved in making the mechanism work. You will have to drive
adoption of this mechanism so that people actually use it and so that it will be successful. And the really, really important part here is the in inspection part of that cycle, whereby you need to constantly
inspect your mechanism to see if it is having
the intended effect. And if not, then maybe you need to change something about the mechanism. And one of the first
mechanisms I want to talk about here in this review and test
section of our presentation is the code review process at Amazon. Basically, any piece of code that is intended to go through production needs to be code reviewed, needs to be reviewed by a peer developer. So if you're a developer at Amazon and you wanna push a piece of code that is going out to production, you'll need some peer
of yours to review it and agree that this will
have the intended effect that it's supposed to have, that it is really something that should be pushed into production. And if for some reason
you don't reach consensus between the original
developer and the reviewer, then another reviewer will
be pulled in for example. And it's also iterative. So any code review changes
that are suggested, they themselves then will go through another code review process. It's also a formal mechanism. It's not a case of just
sitting down with your friend on your team and saying,
"Hey, take a look at my code and let me know what you think." Basically, if somebody approves your code to go into production, then they also become responsible for its success in production. Another mechanism that Amazon uses is the principal engineering community. Principals at Amazon are
very senior technical leaders and experts in their field, They're seen as exemplary
practitioners in the company, and their job, among many things, is to continuously learn and
improve their own skill sets also to educate others and help others to improve in the company. And very importantly,
they also need to provide clarity when there's
decisions that need to be made under ambiguous circumstances. And there's a few different
ways that people can interact with principals in the company. So one way is a principal consult. That's usually something that happens maybe earlier in a project. If you have some kind of idea and you wanna run it by
a senior technical leader and get feedback from them about is that the right way
to approach it or not. And then there's also the
principal design review. That's a much more thorough engagement whereby you have somebody, you have an actual technical design, you have maybe technical architecture diagram for example that you want to review
with your principal. And they will go through
it in a lot of detail, looking at all of the different API calls and the overall system, and give feedback on any bits
that you may a need to change in that system. And one of the great things about the principal engineering community is that you will find
experts across the company that specialize in different things. So if you need help with
security, or API design, or internationalization, you'll find some expert
who specializes in that, that can help you. And then we've talked about
some of the review mechanisms. Let's move on to testing. And when it comes to testing, we're going to use specific test cases that are used by Prime Video, because we want to give
you real world use cases in addition to the concepts
that we'll be talking about. One of the first things that
we'll focus on in this section is Prime Videos preparation for launching Thursday Night Football, Thursday Night Football
was one of the first live streaming sports events that Prime Video supported
on their platform. And so they wanted to make
sure that everything went well. It's the first time they're
doing this kind of thing. But how do you plan and test for something that
you've never done before? Well, the kinds of tests
that Prime Video used were load testing of course. They knew this was gonna be a big event. They needed to predict how much traffic they were gonna
expect on their system, and then scale their systems up to that and simulate that traffic and ensure that they can
handle it accordingly. There's also performance testing. This is measuring basically
how is your system performing when it's running at that increased load. Are things like latency increasing? Are the number of errors increasing? Then there's also stress testing. This is where you go beyond what you expect your system
to be able to handle. So you keep pushing
more, and more, and more, and try to see if you can find
a breaking point somewhere. Then there's chaos testing. In this case, they are introducing specific failure scenarios
into their testing strategy and seeing how their system behaves under those circumstances. And this is in alignment with
the testing reliability piece under the reliability pillar, specifically around testing, scaling, and performance requirements, and using chaos engineering
to test resiliency. Now, no matter how much you plan and test, there will always be things
that happen in production that you weren't expecting. One of the first examples I'll
show here from Prime Video is when they were streaming
a Bundesliga game. This was a soccer match in Europe. And what you can see here on the graph, the two blue vertical lines are the start and end of the game. And you can see these ramp ups that are happening at the beginning. So you see a ramp up
in the stream starting, and a ramp up in people
signing up to watch the game. All of this of course was expected. Prime Video had planned for this. What was not expected here is
this huge spike that you see right in the middle of the game. Now what happened here? Well, basically, this game
happened to get really exciting. It was a game in which two
teams with a lot of rivalry were playing against each other. And in the middle of the game,
it got really, really heated. And the atmosphere grew a lot. People were posting on
social media about it. People were texting their
friends about it, saying, "You have to watch this
game. It's getting crazy." So lots and lots of people
in the middle of the game subscribed, signed up to watch the game. This is not at all what
Prime Video was expecting. They were not expecting that
in the middle of the game, suddenly a bunch of
people would be signing up to try to watch it. So this is an unexpected thing. And another unexpected
thing that they encountered was when they released a new episode of a very popular TV
show on their platform, and here you can see
the ramp ups happening to when they're launching the episode. All of that was expected. What was not expected in this case was this double spike that happened. Now, what happened here
is that this episode, as I said, it was a very popular TV show, and a lot of people, when they watched it, at the end of the episode,
they re-watched it again. They thought, "Oh wow, that
was a really cool episode. I'm gonna re-watch it again." So this again was unexpected. Prime Video was not planning for this. They didn't think that everybody
or lots and lots of people are gonna re-watch the same episode again right after watching it. Now, in both of these cases, Prime Video was able to react accordingly, and they were able to ensure that the people were able to stream
the content that they needed, but it was a learning experience. They learned that you need to be measuring what's going on in production, measuring what your consumers are doing, and reacting accordingly,
and learning from that, because you can't always
predict ahead of time what they're going to do. And this brings us back
to the mechanisms concept. What Prime Video did is they said, "Okay, let's take these
learnings from production, and let's incorporate these
into our testing strategy for future events that
we will be running." And so, this is this idea of continuously improving over time, using a mechanism to improve your process. Another example of an unexpected thing that Prime Video encountered was when they were doing some stress testing in one of their
pre-production environments. Now, lots of teams at Amazon have pre-production environments that are replicas of their
production environments that you can use for stress testing and integration testing, et cetera. And on one occasion, Prime Video was doing some stress testing in their pre-production environment, and they're pushing more and
more load on their system. But the interesting thing that happened was before they found a
problem with their own system, they suddenly started getting throttled by a downstream dependency that was owned by a different team, a different organization, actually. And what happened was that tickets started getting
sent to this other team. The team reached out
to Prime Video saying, What's going on here? We're suddenly getting
a huge amount of traffic from your system that
we weren't expecting." And it actually caused
problems for that other system. And the learning here was that if you are going to do stress testing, if you do have downstream dependencies that are owned by other
teams or other organizations, ensure that you should
notify them ahead of time so that they can plan accordingly. Now I want to move on to talking about actual failure injection test. Up until now, I was talking about a couple of unexpected
things that kind of happened, but you want to actually understand what are the kinds of
things that could go wrong with your system ahead of
time as much as possible. And what you're seeing here
are failure injection tests that are used by Prime Video, and the magnitude to which they're used. So you can see that they test for things. They have packet loss a lot
down here at the bottom, also latency injection, and things like memory hog, CPU hog. These are the kinds of things that can happen to many systems, especially if you're streaming
content over the internet. Things like packet loss and latency are things that you need to
be aware of and plan for. And it's not enough to
just test for these things. You need to introduce mechanisms to handle them if they occur. And if I go back to the
example I was talking about, about the downstream dependency suddenly throttling their system, what they did in this regard is that they implemented
a circuit breaker approach to handle that thing if
it ever happened again. With a circuit breaker pattern, what you do is that if you detect that some downstream system is not responding the way you expect it to, or it's not responding at all perhaps, then you don't wanna keep hammering that system with more requests. That's not gonna make things better. What you want to do is
gracefully back off, stop sending a request to
that system for some time. And you also want to gracefully
respond to your client that send you the initial request. Either letting them know
that something is wrong or else perhaps you can
use the last cached version of the last good response that you got from the downstream system, whatever is appropriate for your use case. It's also really important to plan for your high velocity events. We talked about the live
sporting events earlier, right? So, if you have a high
velocity event coming, you need to ensure that you're
gonna have contingencies and mitigation levers in place. And you also want to make
sure that you're prioritizing what are the critical workloads
for the intended experience of this event that you're planning for. And if we think about
live sports streaming, if you have a bunch of customers watching a live sports streaming event, then maybe you don't
need to be recommending other content for them to watch when they're consuming that content. So you want to ensure that your resources are dedicated to serving
out that content to them while they're watching that
sports game, for example. And you also wanna make sure this is controlled by customer group. So if you have other
customers on your platform, browsing around and watching
on-demand content, for example, you want to ensure that they
are getting the personalization and all of the other types of experiences that they're expecting. And this is in line with the
mitigating failure section under the reliability pillar. Can any of you guess what are the ones that we've been talking about here? Yes, you guessed it right again. We've been talking about
graceful degradation and implementing emergency levers. Now it's really important to understand that Prime Video didn't come up with all this stuff overnight. They didn't just come up
with all these test cases and this test strategy in
a really short timeframe. It's actually been a multi-year journey that started off with people
doing manual load testing of their own systems. And then Prime Video added a
dedicated engineering branch to build tooling to automate
all of these kinds of tests that we've been talking about. And then this grew over time
into communities of people sharing knowledge with each
other across the company, sharing feedback to help
improve the tooling. And this goes back to that
mechanism approach again, right, where you're constantly getting feedback to improve over time. And now we've talked about reviewing and testing your architectures, I wanna hand you over to Seth again to talk about understanding
your systems and production. - Great, awesome. Thank you.
- Thanks. - All right, yeah. So understanding services
and production that very much aligned with
Amazonian principles that ownership does not end at deployment. Amazon has been practicing
DevOps before DevOps was a term. I arrived in 2005 and was handed a pager, and that was before the
term DevOps existed. So, absolutely, the teams were
expected to own production. But this is about diving deep and about how leaders
operate at all levels, stay connected to details,
and audit frequently. So this is not necessarily
about any errors in production, but conclude that. But it's about how are the
services being used in production and how can you improve them to improve the customer experience. And towards that end, I wanna start off with a
process that happens at Amazon that I think is really important. The weekly ops review. Now the ops review is led by the SVP, the senior vice president in
charge of all of consumer, and then the leads from
directors and leads from all of the department there, as well as representatives
from many service teams. It's a big meeting. It used to be a lot in person and a bunch of people online. These days, it's all online. And what happens in this meeting? So number one is success stories
and technical talks, right? This is the time to celebrate successes. So and so team lowered latency by 50%. So and so team reduced errors, whatever. That kind of stuff is
definitely important to surface when you have that big an audience there. Reviewing the metrics, that can be part of the success stories. This is about the metrics
of consumer as a whole, Amazon.com as a whole. I'm gonna show you a slide of that later, what the order metrics look like. But those kind of metrics across all the different marketplaces. And then what can be improved? So there is a COE or correction
of error process at Amazon. It's really important, so that when something does go wrong, that's customer impacting, that there's a formalized mechanism, as Kieran talked about, to actually deep dive in
not only one of the causes, but what's gonna be implemented to prevent those kinds of things from
happening in the sure. And certainly not every COE
is reviewed in this meeting, but a few of the top ones are, and discussed amongst
the senior leadership. It's a really good
opportunity to get exposure for what your team is doing and to learn from what
other teams are doing. So in this case, we're gonna
dive into the best practices, not for reliability pillar, but for the operational excellence pillar, which says, how do you evolve operation? And you can see there's
set several different best practices around there about learning from what you're doing and making sure that that
knowledge is distributed and reviewing the actual
metrics and things like that. So a lot of good best practices
exhibited in the ops review. Now, one of the things that's
interesting in the ops review, I don't know if you've
heard about this before. It's the wheel. And the wheel is... It used to be a physical a wheel, but now it's done in a
computer program and online. And every tier one service
in consumer is on the wheel, and the wheel gets spun. And at every review meeting, a team gets to share and
go deep on their metrics and what they've been doing. Now, certainly, those metrics and those operational
dashboards that they're sharing are shown at the local level,
at the department level, but there's a chance to
show it at the all up, all consumer level. And amongst the things they share are the metrics dashboards. This is just a piece
of a metrics dashboard. This is like one little piece that just shows the number
of requests in the latencies. A lot more things are
gonna be on this dashboard, things like availability, error rates, throttling, CPU usage, you name it. And there's also operational,
like ticket queue and number of high sub
tickets, things like that. So every team, every team at Amazon, the important thing maintains
one of these dashboards with all these metrics on it. So just showing you this
one little piece of it. There's the number of requests
for some Amazon service. You can see it has a day-night cycle. Again, this is per region. This could be US, or it could be France, or it could be Germany. I don't know. The other thing is the latency. Notice there's multiple
latency lines there. So p50 would be the median latency. At Amazon, They don't care about median latency really that much. What they care about is the
p99 or the p99.9 latency. What does that mean? So the p99 latency is the
latency that 99% of all calls are seeing that latency or better. And by using the p99s or the P 99.9s is a truer measure of all the customers. Ultimately, a service call does somewhere down the down the road correlate to a customer experience. So it's a truer measure of what all or most customers are experiencing then say a median. So I mentioned earlier there's also metrics across the
entirety of Amazon consumer. This is an example of that. This is the orders. The orders are key performance
indicator for Amazon.com. So if something goes weird or wrong with the orders metrics, then it's a strong signal
that there's something wrong. All hands on deck. They need to dive into it, and they have mechanisms
and processes around that. But how do you know if something's wrong with the order count? If you see here, again, it has
that day-night cycle, right? Again, this is for a specific region, whether the US or Japan, I
don't know, but specific region. So how do you know if
the orders are dropping? They go up and down all the time. Well, it's important that
you be able to predict and use anomaly detection. So for instance, CloudWatch has an anomaly
detection capability. That would be a good start in AWS. But here you could see this graph. The purplish lines are the prediction, and there's a range, 'cause predictions have ranges, right? Predictions are never exact. And then the green line, greenish line, the dark line is the actual order. So you could see everything's
within range here, but using that kind of capability and that kind of anomaly
detection is super important when you're looking at things like your key performance measures, your key KPIs. Let's dive into a specific example of another service at Amazon. So Amazon owns Ring. Ring makes cameras, security
cameras for home use, doorbells, hence why they're called Ring, motion detectors, that kind of equipment. It's really, really good products. I own them and I enjoy them. So this is their weekly load pattern for their video processing. So someone rings the
bell, it takes a video. Someone can now look at the video. If someone's in your driveway, the motion detection
detects that it's a person. Again, you can look at the video. So this is their video processing. You can see it has that
same day-night cycle. You could see on weekdays, there's sort of a little
double spike there. That's people leaving
their home in the morning and coming back at the
home in the evening, or more activity during that time. And the weekends, they don't
have that double spike. So, AWS and the cloud are
perfect for this, right? The elasticity of the cloud. When you need capacity, you spin it up. When you don't need it, you give it back. Ring uses a combination
of reserved instances. You can see there's sort
of a baseline there. So keeping that as your
reserved instances, lower prices is good, and then on-demand
instances when they need it, when they need to go up in capacity. Oops, I went backwards, all right. There we go. So now those spikes
from the previous graph are what you see in the
middle of this graph at noon. So that's... Even just the tiny little shallow bump, that was the big bumps
on the previous graph. So at the end of this graph, there's like a 10X thing going on. So at Amazon consumer, they have Prime Day and Black
Friday, which just happened. And in those cases, a huge spike is expected. But what do you think Ring's,
quote unquote, Prime Day? It's not necessarily Prime Day. What do you think, for this
video processing capability, what do you think Ring's big day is? Halloween. Halloween. Yeah. And this is true. I mean, Halloween was not long ago, and I was out trick or
treating with my kids and I kept getting these alerts. There's someone in your driveway. There's someone at your door, someone at your driveway,
someone at your... And I liked it, I loved it, because the worst thing is
buying a big bowl of candy and nobody shows up, right? And especially this year, we didn't know if people gonna show up. So it was wonderful to see
all the people showing up and getting the candy. So I really like that. So when you have a big 10X spike like this and something predictable,
you should prepare for it, and Ring does. They prepare in advance. This is coming. We need this extra capacity. And for many, most AWS workloads, it's a matter of
self-service in the console setting up your reserved instances, making sure that you're ready
and you have things in place. If you are a very large scale service, like Amazon.com or Ring, we do recommend you reach
out to your account team and make sure that capacity's there so that they can make sure
they can accommodate it in exactly the kind of instances you need. But either way, the cloud and
AWS can help you with that. All right, so I said this
is about video processing. This is what we're talking about, okay? So the one on the left is a situation Ring wants to avoid. This is where there's a... I got a alert. This is my driveway, my minivan. Don't be jealous. And I got an alert saying there's some motion in the driveway. And I go to look at the
video, and it's not ready. What they want is on the right. You get the alert, there's
someone in your driveway. You go there. instantaneous or near
instantaneous video processing, that's what they wanna achieve. And why is that? Because if there's a
bunny in your driveway, you don't wanna miss that, right? That's an important event,
seeing a bunny in your driveway. That just happened to be there,
so I thought I's share it. And this, again, I love
sharing these simple, it's gonna be like a new
theme, four icon architectures. This is their architecture
for video processing. Basically, raw video comes in on the left, gets put into an S3 bucket
that creates an event which goes on an SQS queue, and then there's a fleet of EC2 instances running their transcoder. That fleet is pulling the queue. You got anything for
me? Got anything for me? When it gets a job, it
then goes to the bucket, gets the video, transcodes it, processes, and puts it in the bucket on the right. That's it. So the key here is how do they scale up and how do they scale down? Well, the cloud offers
several ways to do this. They considered... Again, they want that near
instant video processing. They considered using like queue length, but queue length is an aggregated metric. It's a trailing metric that
wasn't good enough for them. So they came up with their
own metric that they're using. And it's empty receives. Think about it. If my workers go pull and
they never get an empty, there's always work there,
it means works backing up. If they go there and they're
always getting empties, it means that I processed everything. All the work's gone. And then everywhere in between. But it's not as simple as that, right? There's business logic. There's
proprietary logic in there. How many empty receives means
that we should scale down? How many empty receives
means we should scale up? So what they did is they collect those empty received metrics
using CloudWatch monitoring, and they feed it into step functions. Step functions is a way
you create a state machine and that state machine could run Lambdas. It could do all kinds of arbitrary logic. And that step function is a state machine that can then process using
their proprietary logic. Okay, this is the number
of empty receives. That means scale up. So it's in the scale up signal. This is the number of empty receives. That means scale down,
send a scale down signal. And that's how they achieve
that near instantaneous video processing. So, okay, back to the reliability pillar, adapting to changes on demand. The question is, how do
you design your workload to adapt through changes in demand and use automation and scale
up basically when you need it? Those are the best practices from the Well-Architected Framework that we've been talking to you about. All right, final section, going global. So what is the leadership principle here? It's about customer obsession, which is actually the first
leadership principle, right? So it's about leaders
start with the customer and work backwards. It's a big phrase at Amazon.com, working backwards from the customer. They work vigorously to earn
and keep customer trust. Amazon customers are global. They're all over the world. How does Amazon meet the needs
of those global customers? Well, that's a place
where AWS can really help. And to understand how AWS could help, you look at the AWS global infrastructure. Okay, AWS has 25 regions
all over the world where a region is a set, a multiple set of data center buildings
in a specific region. And there's 25 of these. There's four being added
that were announced as one's being added all the time. This number is just gonna keep going up. But 25 of those around the world. You can see them on the map there. Within each region are
multiple availability zones. An availability zone is
one or more data centers. Okay, so that's important to keep in mind. An availability zone is not
some logical segmentation. It's a physical segmentation. So each availability zone
is one or more data centers separate from the other
availability zones. I can even show you on this last slide. There, one or more data centers. And the thing about availability zones is they have their own power, at least their own backup power, and their own onboarding
onto the power grid. They have their own
separate water supplies. They're located far enough so
they should not share fate. They're in separate flood Plains. Basically, AWS does a lot of
research on flooding and earth, any natural disaster that could happen. They have geologists working on this to put the AZs in places that
they should not share fate if a natural disaster happens, or if a technical failure happens, like a big bulldozer takes
out a big fiber line, right? This means that most AWS workloads can be accommodated with a
high availability architecture just using a single region. I wanna make that super clear. Using a single region across
multiple availability zones, you have high availability. If a fire happens, at most, one availability zone should be affected, the other ones keep operating. And in other talks I have, we talk about how to architect for that. The cases I'm gonna show you
are a little bit the exception, but they're there in case you need it, which is where services feel
they need to go multi-region in order to achieve their goals. And it's not just about reliability. Again, it's about serving a
global worldwide audience. So the first example is Amazon Ads. So Amazon Ads basically is where folks can put in ads onto the ads platform and expect those ads to show up in various places on
the Amazon.com website. And they wanted to go global. They had a globalization initiative. Now ads is already in multiple regions, but they had a separate
isolated stack in each region, maybes isolated is a little hard. But basically, if you
create an ad in one region, it wasn't gonna show up any place else. It was just in that region. And they wanted to find
a better way to share. If I put an ad into one region, it could be shared
across multiple regions. So as you can see in
the last bullet there, DynamoDB global tables to the rescue. So what does that mean this? This is the architecture. So now you see three different regions. And as ads, content ads
artifacts are created, they go into DynamoDB. Now what global tables does
is allow you to take a table and replicate it across multiple regions. So the same table exists across
all three of these regions. And when you write to
any of these regions, it is automatically replicated
to the other regions. That's the key here? Then you see at the bottom, just going down to the bottom where MSK and DynamoDB and cloud, all the other systems are, that's the old local systems, right? So they don't have to rearchitect those. Those systems just see
everything as usual. They don't know that
something's been replicated in the top layer. So what's Lambda in the middle there? Well, that's a nice thing, is once you replicate to those
regions, it creates an event, and Lambda react to the event and do whatever kind of
business logic you need in that region to make that artifact appropriate for that region. Okay, for my next example, I'm gonna refer back to Prime Video, which is something Kieran
talked to you a lot about. And Prime Video, similar to ads, it exists, already exists
in multiple regions, AWS regions around the world. We didn't wanna get into the details of what the specific regions are. So we created our own
little fictional map here, and that little blue dot is an AWS region serving this geographic region there. And that's how AWS operated, generally operated for... AWS, how Prime Video operated
for a really long time. And so, you have a customer down here. They're across the continent, right? So they might have some latency issues. They're not close to the AWS region that's serving their traffic, serving their live playback video. And also, if there's some kind of issue where for some reason,
it could be in the data, or it could be anywhere
along the network path, where that region can't
serve that customer, that customer's now gonna
experience an outage. So Prime Video looked at this
and said how we avoid this. So what they did is kinda similar to ads. Now they can put themselves
in multiple AWS regions within that geographic region. This serves two purposes. One, as you can see, serving the customer much
close to where they are. But the other thing is they architected it so that if one region wasn't
able to serve that customer, the other regions in that
geographic locality still could. That results in that high availability. So what is our best practices here? Use fault isolation. Deploy the workload to multiple locations. And I want you to keep in mind, multiple locations doesn't
have to mean multiple regions. Okay? These two examples I gave
you had reasons for that, but multiple availability zones is a perfectly fine way to
satisfy this best practice. All right, in summary, we gave you a little history
lesson on Amazon.com. I hope you enjoyed that. And then we told you how they evolved into this multi thousands of
microservices architecture. Kieran talked to you. He talked to you about that, And then he talked to you
about reviewing and testing about how Amazon uses mechanisms as part of their scalable
reliability strategy, especially using fault injection testing. We talked about understanding how services operate in production and how we use that to best serve our customers. And we then finished
it out by talking about the globalization and how you can deploy to multiple regions to
meet your customers needs and how Amazon is doing that. So a couple of resources. we're one of the first talks of re:Invent. So we got chock-full of resources here. This is the first of two slides. The first one's on just
Well-Architected in general. That second link I
highly recommend to you, the Well-Architected Labs. I don't know about you,
but I learn by doing. So The Well-Architected labs is a great place where you can go and learn about
Well-Architected best practices by doing labs. Builders' Library is actually
now part of Well-Architected, but it's where those principles
and senior principles have written articles about
how Amazon and AWS operate. and the Well-Architected
Framework white paper is a great place to start
for Well-Architected, and that scan code will take you there. And now this is the part
about being early, right? There's plenty of sessions
we could talk to you about. Now, if you wanna learn
more about Amazon Ads, aside from our two slides, you wanna see a whole deck about that? Go to Under the Hood at Amazon Ads, so they're gonna tell you all about that. Then a lot of other sessions here about how Amazon operates internally, the sustainability session,
approach DevSecOps. Oh, the ones on the bottom, the INO ones, I recommend those too. The Amazon's culture of innovation and how Amazon transforms
experiences using AI/ML. I like those innovation ones 'cause they really talk to you more. If you like that history
lesson part at the beginning, you'd like the innovation talk. So go to those. Any other talks you'd
recommend from there, Kieran? - Not really, I think the ads one would be a specific interest. Jeff Barr, our chief evangelist, just posted something
about that this morning. So there's a lot of traction and there's a lot of press around that. So yeah, so I think that's probably one to definitely catch if you can. - [Seth] How do we get Jeff
Barr to post about ourselves? - I know, right? Yeah, yeah, yeah. - Anybody knows, let me know. And anyway, ultimately, thank you. There's some ways you could
reach Kieran and myself. Appreciate your being here. again, Just so thrilled to be here live in front of you all. And before you go, we'll
be taking questions. We do not have mic runners, but if you're willing to like step up and state your question, we'll repeat it for you
and answer your question. Thank you. (audience applauding) I stepped on my own applause
by saying we take questions, but yes, thank you for the applause. But anybody any questions
that they'd like answered? Yes, please. - [Audience Member] How do you simulate like a global production load in a pre-production environment? - The question is how do you simulate a goal global production load in a pre-production environment? Can I take that one first?
- Yeah, sure, go for it. - So I'd say there's two ways, okay? So it depends on how big is
your global production load, how big is your global system, right? For systems of moderate size, you can stand them up in AWS and be a assured that you have something similar size to production. But I think you are hinting at, okay, I can't possibly
stand up my entire system. It's too big. And in that case, it becomes tricky. It becomes a math question, right? When you stand up something that's of smaller size scaled down, it's not linear that the
traffic is linear, right? So it becomes a little more tricky. I will say your secret weapon there is testing in production. Don't go out and do that right away. Don't do that right away. But once you've done your
pre-production testing with your scale down instance, find a time where everybody's
all hands on deck. It's a game day. Everybody's manning the consoles. You have a runbook with
a rollback procedure. Maybe it's night. And then actually do
load testing production. It's a legitimate way
to test your production. I'm not saying every month. I'm not saying make it part
of your CI/CD pipeline, but it's a legitimate way to test. Yes? - [Audience Member] How do you manage microservices dependencies? - How do you manage
microservices dependencies? You want me to take it
or you wanna take it? - So, one thing that we
showed earlier is that Amazon has built an internal
tool for that purpose, that attracts all
services that are deployed and their dependencies between them. But ways that you can
use AWS services for this is using things like x-ray, for example, that tracks all of your API calls. Whenever you're running
load on your system, you can use x-ray to see
what services are calling, what other services. You can even see what
kinds of latency exists between each call and all
of that kind of stuff. So what Amazon did is that
they took that information and pulled it into a tool that they built to keep track of all of these services and what they're doing. And it's also related
to the CI/CD pipelines. So when something gets
deployed to production, that is registered in the system, and then the systems
that that interacts with are also tracked accordingly. So, building internal tools and using AWS tools for that also. - I'll add to that. Amazon was bad at that
circa 2005, 2010, right? 'Cause we showed you the organic growth, and it was something that Amazon didn't really take into account. And I remember being on
a team in 2006, 2007, where we want to deprecate a service that was called by hundreds, maybe thousands of other services. And they had no idea
who their clients were. That's a problem, right? You could send them all
the emails you want saying, "Hey, if you're a client,
we're gonna be deprecating, but you're not gonna get everybody." So, that's not how it is today. But yeah, I think the
pain of experiencing that led to Amazon building the systems that Kieran was talking about. - And just adding on to
the previous question that Seth was mentioning
about testing in production. When we were showing the
Prime Video stuff earlier, we were showing load testing and performance testing, et cetera. They do actually do some
load testing in production. Of course, in each region,
it would be off peak when people are asleep or whatever, and when you have relatively
low traffic on the system. You don't do it in the middle of the day. But then that that's for load testing. You don't do stress testing in production. You don't try and break
your systems in production. That's an important thing
about chaos testing also. I mean, people often
talk about chaos testing as if it's, oh, you just start rebooting servers in production
and see what happens. That is not at all a good way
to approach chaos testing. When we talked about Prime
Video's testing journey about how it's been this long
term, multiple year thing. They didn't come up with it overnight. They didn't start doing
chaos testing in production. Basically, you do all
of the stress testing and failure objection testing
in your pre-prod environments as much as possible. - Yeah, another thing I wanna add is Amazon.com does load testing and stress testing like
Kieran was talking about. Specifically, all teams are expected to test in pre-production
to the breaking point and measure how long it
takes them to recover. That's actually one of the
metrics of the stress test. - All right.
- Other questions? Anybody? - [Kieran] Oh, there's one over here. - All right. - [Audience Member] How do
you advise doing multi-region when you're serving terabytes
of data with different... (audience member faintly speaking) - How to do multi-region when
you have terabytes of data? Well, I mean, there's a trade-off, right? And doing multi-region doesn't mean all data's copied everywhere, all right? So you can do multi-region
where only a select set of data is copied everywhere,
maybe some of the metadata, but some of the customer data
is stored in a certain region. And when you need to read it or write it, you can route your reads
and writes to that region. That's a partitioned approach. You could even for some. Yeah, so that's one way to do it. I mean, AWS will give you native tools to replicate that data. DynamoDB global tables, S3 cross region replication. The question is, do you want to actually send
all that data over the wire, or can you pick a subset of it? And I think the tools are there, and it'll work with terabytes of data. It would just be costly. - Yeah, the cost,
there's a cost trade-off. That's the thing. So you need to determine, do you nee to replicate all of the data? Is there data that's hot
in different regions? And then for colder calls, you can go cross region, for example. So yeah, it basically
comes down to the workload. I need all data replicated
or just some of it. - [Sean] Hey, more questions. We love the questions part. Yes. - What kind of tools do you
use or have used in this case for testing and monitoring? - Oh, what are the tools
for testing and monitoring? So, the funny thing about
working at Amazon.com is the great stuff you get in AWS actually started off
usually as Amazon.com tools that were then people said, "This is cool. Let's externalize it." So in a lot of ways,
Amazon.com uses plenty of AWS. Don't get me wrong. But a lot of these internal kinda tools tend to be different than the AWS tools, the homegrown tools that
then ultimately become the AWS tools. And then it's hard to everybody
migrated onto the AWS tools. It's working. Why do it? But it does happen? Case in point is monitoring, Amazon had its own internal
monitoring systems. CloudWatch came along.
Now it's all CloudWatch. Actually, it's even better than that. The old monitoring portal is still there, but it's all CloudWatch under the covers. But if you wanna do fault
injection type testing, then FIS, the Fault Injection Simulator, is gonna be a great option. I actually have a workshop
about this this afternoon. That's a native AWS service
and there's lots of other commercial and open source products chaos toolkit comes to mind out there for doing that kind of
fault injection testing. Anything to add? - No, I think you captured that one well. it's mainly CloudWatch, but originated from internal
systems that Amazon had built. - And that was one of the things Kieran talked about onboarding. So I'm get and say Prime Video created their own internal frameworks for fault injection testing,
and monitoring that testing, and then getting ready to adopt was part of the cultural challenge. Yes. - [Audience Member] So you talked about the amount of services,
but eventually AWS services have kinda soft and hard limit. So what if you hit the hard
limit on that specific workflow? - Well, the question is every AWS service has soft and hard limits. What happens when you hit a hard limit? So I guess there's two
kinds of hard limits, right? 'Cause there's limits you
can increase yourself, using quotas, AWS quotas in the tool. Then there's limits
that you need to contact your account team for. Those are sort of like
the medium hard limits. And then there's hard limits. There's just nothing more than that. That's a case by case thing, right? How do you architect around that? I mean, we're not talking
about number of EC2 instances, I don't think, right? I mean-
- No, again, if you have... For example, you show
Lambda or anything else. Do I have permission to do that and try access the same service right now? - Yeah. So yeah, what are the
concurrency limits on Lambda? Do they tap out at a certain hard limit? - Yeah, they do. So, it's also important to remember that limits are per Amazon, per AWS account. - [Sean] Yeah. - So we do work with lots of
very large systems in Amazon that span across many, many accounts, some of them across hundreds
of different AWS accounts. And you can use things
like AWS organizations to share things across
accounts and all of this, but it gets pretty complex at that point. Once you need to go
beyond a single account, then there are ways to architect for using services and sharing resources across accounts, et cetera. It does get pretty complicated. - All right, I think we're out of time. By the way, you folks have stayed for the questions and answers. You're the smart folks. It's the best part of any talk, is when you learn the real stuff. So appreciate your staying.
- It's true. - Appreciate you being here. Thank you so much. - Thanks, Everybody.
- All right. (audience applauding)

## Subtitles with Timestamps

[00:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2s) - All right, I think
it's time to start here.

[00:03](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3s) Welcome, everyone.

[00:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=4s) I am so thrilled to be here

[00:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=7s) in front of a live
audience after two years,

[00:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=8s) and I'm so glad you're all here with us.

[00:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=10s) You're here to talk about
reliable scalability,

[00:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=12s) how Amazon.com scales in the cloud.

[00:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=15s) My name is Seth Eliot.

[00:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=17s) Just a little bit about me.

[00:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=18s) I'm with AWS now.

[00:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=19s) I'm the reliability lead
for AWS Well-Architected

[00:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=21s) and been with AWS for
a couple of years now,

[00:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=23s) but I spent the prior eight
years with Amazon.com.

[00:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=26s) And so, when we talk about
Amazon.com in this case,

[00:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=28s) we're talking about the
site you buy stuff from.

[00:30](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=30s) We're talking about where you
go to buy a Kindle, or a book,

[00:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=34s) or even download or stream
a movie from Prime Video.

[00:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=38s) So that's the Amazon.com
we're talking about today,

[00:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=40s) whenever we were refer to Amazon.com.

[00:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=43s) I had several roles.

[00:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=44s) I've been on the Prime Video team

[00:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=45s) when it was founded way back when.

[00:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=47s) In 2008, I've been on the

[00:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=49s) content ingestion team, Amazon Fresh.

[00:51](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=51s) But my most recent role
before I transferred to AWS

[00:54](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=54s) was with the team working across
the entirety of Amazon.com

[00:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=58s) with our thousands of
developers of how they develop

[01:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=60s) and implement in AWS.

[01:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=62s) And in that role, I partnered
with our AWS support team.

[01:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=67s) Amazon.com, we, back then, was a customer,

[01:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=70s) is a customer of AWS.

[01:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=72s) And our support team,

[01:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=73s) my counterpart on that
support team, was Kieran,

[01:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=75s) and Kieran's here to
talk with you also today.

[01:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=78s) - Thank you, Seth.

[01:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=79s) Yes, hi everybody, my
name is Kieran Kavanagh,

[01:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=81s) and I'm a principal
solutions architect at AWS.

[01:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=84s) I currently specialize
in machine learning,

[01:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=85s) but prior to that, I
worked as a generalist SA

[01:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=88s) on the Amazon.com account
as Seth was saying.

[01:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=91s) So back then, Seth was
actually a customer of mine.

[01:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=93s) We've been working together
for quite some time now.

[01:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=96s) And where better to
begin our journey today

[01:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=98s) than at the actual beginning.

[01:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=100s) What you see here is the
Amazon.com Books website from 1995,

[01:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=105s) and you can see it's not quite
as advanced and feature-rich

[01:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=107s) as the website that Amazon has nowadays,

[01:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=109s) but this was pretty
standard for the mid '90s.

[01:51](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=111s) What is impressive here

[01:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=112s) is that they already had 1 million titles,

[01:54](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=114s) so they were already
earth's largest bookstore.

[01:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=117s) And let's take a look at the
architecture that was used

[02:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=120s) to serve this website, the customers.

[02:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=122s) Started off pretty simple.

[02:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=124s) What you see here is a customer
coming in over the internet.

[02:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=127s) The first thing that they interact with

[02:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=129s) is something called Obidos.

[02:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=130s) That was the web server layer,

[02:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=131s) and that was a single monolithic service.

[02:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=133s) We'll talk a little bit
more about that later.

[02:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=135s) And it connected directly
to a single Oracle database

[02:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=139s) in the backend,

[02:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=140s) which was called the
Amazon.com Books Database,

[02:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=142s) or ACB Database.

[02:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=144s) And this database had
everything that was needed

[02:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=147s) to do business on Amazon's website.

[02:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=149s) You had a table for all of the customers,

[02:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=151s) you had a table for all of the inventory,

[02:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=153s) and you had a table that
tracked what customers

[02:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=155s) were purchasing from the inventory.

[02:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=157s) You can see here also
that Amazon started off

[02:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=159s) with one distribution center

[02:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=160s) for sending out packages to people.

[02:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=163s) And also, you'll see this thing called

[02:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=165s) the credit card motel.

[02:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=167s) What's interesting about
the credit card motel

[02:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=169s) is that once you checked

[02:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=170s) a piece of credit card
information in there,

[02:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=172s) you could no longer humanly read it back.

[02:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=175s) The only piece of code that could access

[02:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=177s) that credit card details

[02:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=178s) was a small piece of code
that actually connected

[03:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=180s) to the banking institutions
to make a purchase

[03:03](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=183s) when somebody's purchasing
something on Amazon.com.

[03:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=186s) So security was built in
from the very beginning.

[03:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=188s) It was a major priority,

[03:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=189s) even from the very first version
of Amazon's architecture.

[03:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=193s) And Amazon wanted to get big fast.

[03:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=195s) What you see here in the
top right hand corner

[03:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=198s) is a picture of a t-shirt

[03:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=201s) from a company Picnic that
took place back in 1997.

[03:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=204s) And you can see the slogan says,

[03:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=206s) "Get big fast, have another hot dog."

[03:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=208s) That is one way of getting big fast,

[03:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=209s) but that's not what we're
gonna talk about today.

[03:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=211s) We're gonna talk about
scaling out the architecture.

[03:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=214s) I'm just beginning first
with a quick definition.

[03:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=216s) When we talk about scalability,

[03:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=217s) we say it's the ability of a workload

[03:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=219s) to perform its agreed function

[03:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=220s) when the load or scope changes.

[03:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=222s) So if you keep getting
lots of more traffic

[03:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=224s) onto your system,

[03:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=225s) you wanna make sure that
your system scales up

[03:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=227s) and that it continues to do
what you expected it to do.

[03:51](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=231s) Now, before we dive into

[03:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=233s) how Amazon scaled out their architecture,

[03:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=235s) I wanna first ask you to
take a moment to think about,

[03:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=237s) with pretty much any
web-based architecture,

[04:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=240s) what is one of the first
components in the architecture

[04:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=242s) that becomes a scaling concern?

[04:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=245s) Yes, you guessed it
right, the database layer.

[04:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=248s) And that's exactly what Amazon
started to scale out first.

[04:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=252s) one of the first things
they did in this regard

[04:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=253s) is they created a separate
database called Web 1

[04:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=257s) that was just for orders.

[04:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=260s) Now, why is this important?

[04:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=260s) When you think of any e-commerce platform,

[04:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=263s) the ability for people to
make orders on that platform

[04:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=265s) is one of the most important things

[04:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=266s) that the platform can do, right?

[04:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=268s) That's one of the most
important functions.

[04:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=269s) And so, there was this dedicated database

[04:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=271s) and a dedicated path for
people to make orders,

[04:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=274s) so that if other stuff was going on

[04:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=276s) with the central ACB database,

[04:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=278s) the orders had its own separate workflow

[04:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=280s) that wouldn't be affected
by any congestion there.

[04:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=284s) And this orders table then was being

[04:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=286s) synchronized periodically back
to the central ACB database.

[04:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=290s) And as Amazon grew over time,

[04:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=292s) they added more distribution
centers of course.

[04:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=295s) If you're sending out more
and more packages to people,

[04:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=296s) you have more and more customers growing,

[04:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=298s) and you need more distribution centers

[05:01](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=301s) to meet all of their demands.

[05:03](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=303s) And each distribution center
had its own dedicated database.

[05:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=306s) So this is another way
that they scaled out

[05:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=308s) the database layer.

[05:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=309s) And this continued to grow.

[05:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=311s) The distribution centers grew to about 175

[05:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=313s) and a number of databases
grew to more than 300.

[05:16](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=316s) These were all Oracle databases,

[05:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=318s) but they've all recently been deprecated

[05:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=320s) or they've all since then been deprecated.

[05:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=323s) And now Amazon is using

[05:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=325s) all AWS database technologies instead.

[05:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=327s) So the final Oracle
database was shut down by

[05:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=332s) Amazon's retail business back in 2019.

[05:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=337s) And now that we've talked about scaling

[05:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=338s) at the database layer.

[05:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=339s) What is the next component
in our architecture here

[05:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=342s) that we need to think about scaling?

[05:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=345s) Yes, you guessed it right
again, the application layer.

[05:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=348s) And this is the Obidos piece
that I talked about here.

[05:51](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=351s) This was the single monolithic service

[05:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=353s) that contained all of the business logic

[05:54](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=354s) required to do everything
on Amazon's websites.

[05:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=357s) And every new feature that was being added

[06:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=360s) was all being added to
this single code base.

[06:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=362s) So when Amazon added one
shopping, for example,

[06:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=366s) that was added to Obidos.

[06:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=367s) Every bug fix, every feature

[06:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=368s) was all being added to
this single code base.

[06:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=370s) And Obidos grew a lot over time.

[06:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=372s) In fact, at one point, it got to the stage

[06:14](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=374s) where it was taking 12 hours to build it.

[06:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=377s) So if you wanted to make a change

[06:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=378s) and you kick off a build,

[06:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=380s) then you would either go about your day

[06:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=382s) or maybe it's in the evening time,

[06:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=383s) you go to sleep for the night,

[06:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=384s) you come back 12 hours later

[06:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=386s) and you just hope and really hope

[06:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=387s) that what you intended to do worked,

[06:30](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=390s) 'cause otherwise you have to
go through all of that again.

[06:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=392s) And as you can see, this is not really

[06:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=394s) scalable in the long term,

[06:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=395s) and this is not really scalable,

[06:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=397s) especially as you are employing
more and more developers

[06:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=400s) and they all want to be adding
things to this code base.

[06:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=403s) So one of the first things
that Amazon did in this regard

[06:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=405s) is they started to break it
out into separate components.

[06:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=409s) The first one that they broke
out was the customer service,

[06:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=412s) and this was a service that was used

[06:54](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=414s) for interacting with customer information.

[06:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=417s) So there was a dedicated customer
database that was created.

[07:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=420s) So they're scaling out the database layer

[07:01](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=421s) in this case again.

[07:03](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=423s) And also, the customers were regionalized.

[07:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=425s) So there was a different database

[07:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=427s) for different customers
in different regions.

[07:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=429s) What you're seeing here as an
example is the CustNA database

[07:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=432s) is customers in North America.

[07:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=435s) And if you wanted, if a new
customer wanted to sign up,

[07:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=438s) they would interact with
the customer service

[07:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=439s) in order to get their details
into that customer database.

[07:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=443s) And also if a address was needed

[07:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=445s) for printing a shipping label,

[07:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=447s) the customer service would be
called to fetch that address.

[07:30](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=450s) So this was one of Amazon's first steps

[07:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=452s) towards a service oriented
architecture approach.

[07:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=455s) And at the very beginning
of the customer service,

[07:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=457s) you could almost say that it
was microservice because it...

[07:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=460s) Even though microservices
weren't really a thing

[07:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=463s) back then in terms of in the industry,

[07:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=465s) people were talking about them a lot.

[07:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=467s) But the customer service started off

[07:51](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=471s) with a really dedicated set of functions

[07:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=473s) and a dedicated database.

[07:54](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=474s) And it just had a very
simple set of operations

[07:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=476s) that it was doing.

[07:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=477s) Most of its APIs were wrappers around

[07:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=479s) SQL called into the database.

[08:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=482s) But this then grew over time,

[08:03](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=483s) and so people started adding more and more

[08:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=485s) to the customer service

[08:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=486s) because they were reluctant to be adding

[08:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=488s) more and more to Obidos.

[08:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=491s) And the architecture continue to scale.

[08:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=493s) And if we look at some details around

[08:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=495s) the kind of growth that Amazon has seen

[08:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=497s) in the past few years,

[08:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=498s) we're having a look at some details here

[08:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=500s) from Prime Day earlier this year,

[08:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=502s) where 175 million items were
purchased by Prime members

[08:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=506s) just during that period.

[08:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=507s) So that's a lot of
commerce that's going on

[08:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=509s) on Amazon's website nowadays.

[08:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=511s) And if we look at what that means

[08:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=512s) in terms of AWS service usage,

[08:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=515s) what kind of scalability
they have achieved there,

[08:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=518s) during Prime Day this year,

[08:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=520s) Amazon DynamoDB handled about

[08:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=522s) almost 90 million requests
per second at peak.

[08:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=525s) And if we take a look
at another example here,

[08:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=528s) Amazon CloudFront processed

[08:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=529s) more than 290 million requests
per minute during that time,

[08:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=533s) totalling to 600 billion
requests during Prime Day.

[08:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=536s) So there's some pretty serious scale

[08:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=538s) that they've been achieving here.

[09:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=540s) And now let's take a
look at what Amazon did

[09:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=542s) to scale out their architecture

[09:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=545s) to handle this kind of growth.

[09:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=549s) Well, it turns out that after that first

[09:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=551s) change that they made,

[09:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=552s) this first thing of breaking
out the customer service.

[09:14](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=554s) They didn't need to do
anything else after that.

[09:16](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=556s) That solved all of the
problems from there onwards.

[09:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=559s) Just kidding.

[09:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=560s) This is actually what
Amazon's architecture

[09:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=561s) looks like nowadays.

[09:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=563s) It's an extremely vast and
complex web of microservices.

[09:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=566s) And this is an actual
real picture, by the way.

[09:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=569s) This is a picture from an
internal tool at Amazon

[09:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=572s) that tracks deployed
services under dependencies.

[09:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=575s) And we can even zoom in here
and look at one microservice

[09:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=579s) that's connected to about
400 other microservices here.

[09:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=583s) Everything I've talked about up until now

[09:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=584s) has been around scalability,

[09:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=586s) but this presentation is
called Reliable Scalability.

[09:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=588s) So let's talk about
reliability for a minute.

[09:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=592s) Starting off again with a definition.

[09:54](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=594s) We said that reliability is
the ability of a workload

[09:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=596s) to perform its required function
correctly and consistently.

[09:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=599s) And when we couple that
with the scalability aspect,

[10:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=602s) it means that no matter how
much your system scales,

[10:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=605s) you want it to have the same

[10:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=606s) service level agreements, et cetera.

[10:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=608s) You wanna have the same kind of experience

[10:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=610s) for your customers.

[10:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=611s) This is the reliability aspect.

[10:14](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=614s) And reliability is such an important part

[10:16](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=616s) of pretty much any systems architecture

[10:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=618s) that it has a dedicated pillar

[10:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=620s) in the AWS Well-Architected Framework.

[10:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=622s) The Well-Architected Framework

[10:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=624s) is a collection of best practices

[10:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=626s) that you can use to ensure that your

[10:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=628s) systems are architected
to perform optimally.

[10:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=632s) And reliability has its
own dedicated pillar.

[10:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=634s) A pillar is basically a
category of best practices,

[10:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=638s) and there are five in total.

[10:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=639s) We'll be talking mainly
about reliability today

[10:41](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=641s) and also operational excellence.

[10:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=643s) This is where the
scalability aspect comes in.

[10:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=645s) All of the pillars are very important.

[10:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=648s) The other three are security
performance efficiency

[10:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=650s) and cost optimization.

[10:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=652s) All of these are very important

[10:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=653s) for pretty much all workloads,

[10:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=655s) but we'll be focusing
mainly on reliability

[10:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=657s) and operational excellence today.

[10:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=659s) And at this point, I wanna
hand you over to Seth

[11:01](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=661s) to talk about how Amazon
architects these microservices

[11:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=664s) that we've just been showing.

[11:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=666s) - Thank you, Kieran.

[11:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=667s) All right, yeah.

[11:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=668s) So that was a little bit
history lesson on Amazon.

[11:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=671s) Now let's dive into how
things are operating today.

[11:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=673s) And we'll start off by talking about

[11:14](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=674s) service-oriented architecture

[11:16](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=676s) and microservices architectures.

[11:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=678s) Now, for each of these subsequent

[11:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=680s) sections we're gonna show you,

[11:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=681s) we're gonna tie them into an
Amazon leadership principle.

[11:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=683s) Now Amazon leadership principles

[11:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=685s) are the 16 principles at all
Amazonians across the company.

[11:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=689s) So keep in mind every day
when they're making decisions

[11:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=692s) or doing tasks at Amazon. Is
this the right thing to do?

[11:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=695s) Oh, let's refer back to
the leadership principles.

[11:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=698s) So this one's bias for action.

[11:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=699s) Speed matters in business.

[11:41](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=701s) We value calculated risk taking.

[11:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=703s) So I will hopefully tie it in

[11:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=705s) how a service-oriented architecture,

[11:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=707s) also called SOA, or
microservices architecture,

[11:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=710s) can factor into that
speed and bias for action.

[11:54](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=714s) And just real brief, just so
everybody's on the same page,

[11:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=716s) just a little bit of just the sort of 101

[11:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=718s) of monolith versus SOA
versus microservices.

[12:01](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=721s) So the monolith is what Kieran
was talking about, Obidos,

[12:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=724s) a big binary, all changes
go into that binary.

[12:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=727s) Everybody's kind of
beholden to that binary.

[12:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=730s) If you wanna make a change,

[12:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=731s) you gotta hope everybody
else's changes don't break you.

[12:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=733s) It's big. It's unwieldy.

[12:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=735s) There are maybe some valid
applications for monoliths today,

[12:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=739s) but generally we try
to shy away from them.

[12:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=741s) And service-oriented architecture,

[12:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=743s) that's where we take
each of our applications,

[12:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=745s) and make them a separate service,

[12:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=746s) and have them communicating
with each other.

[12:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=748s) So you might have a catalog service

[12:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=751s) or even a catalog
ingestion service, right,

[12:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=753s) as one of your services,
and microservices.

[12:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=755s) Now let's break it down further.

[12:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=757s) You can think about
taking those applications

[12:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=759s) and breaking them down
into individual components,

[12:41](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=761s) each a separate service
that does its own thing.

[12:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=763s) So for that catalog ingestion service,

[12:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=765s) maybe we have a service dedicated

[12:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=767s) just to taking in merchant data

[12:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=769s) that's being submitted to the catalog,

[12:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=770s) and matching it with the existing catalog.

[12:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=772s) That's a single microservice.

[12:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=773s) So that's a microservices architecture.

[12:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=775s) We're not gonna make a value judgment

[12:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=776s) between SOA and microservices.

[12:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=777s) They both have a place
and they're both good.

[12:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=779s) I'm just gonna lump them together

[13:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=780s) and just talk about them together
as generally not monolith.

[13:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=784s) And towards that end,

[13:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=785s) when you're using
microservices or even SOA,

[13:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=787s) the nice thing about them is
the ability to deploy them

[13:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=789s) and scale them independently, right?

[13:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=792s) So if some need more
capacity in the AWS cloud,

[13:16](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=796s) you can then ramp them
up with the elastic cloud

[13:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=799s) and supply more capacity to them.

[13:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=800s) Some need less capacity.

[13:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=801s) You can give that capacity back.

[13:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=803s) So you're not paying
for what you don't need.

[13:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=804s) And the nice thing about AWS

[13:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=806s) is using organizations
and consolidated billing.

[13:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=809s) You can share that capacity
between your microservices.

[13:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=812s) So one is scaling down,
you release that capacity,

[13:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=814s) so another one could scale up.

[13:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=815s) So again, it's just a real nice way

[13:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=818s) AWS helps you keep that efficient.

[13:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=820s) And ultimately at Amazon,

[13:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=822s) they have 150 million
deployments per year.

[13:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=824s) Now, to be sure not all of
these are major features,

[13:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=827s) or major functionality,

[13:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=828s) or even customer visible functionality,

[13:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=830s) a lot of them may be
just utility deployments,

[13:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=832s) things that get things out there.

[13:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=833s) But still it just speaks
culture at Amazon.

[13:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=836s) They have a culture of
continuous integration

[13:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=838s) and continuous deployment

[13:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=839s) and that high deployment lets them.

[14:01](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=841s) So you can imagine this deployment,

[14:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=842s) there's a huge stream going out the door

[14:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=845s) and you could always be putting in

[14:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=846s) the features and functionality
you need onto that stream.

[14:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=850s) All right, so let's look at some examples

[14:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=851s) of the microservices
architecture at Amazon.

[14:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=853s) This is a page I think you should all

[14:14](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=854s) be pretty familiar with.

[14:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=855s) It's a detail page.

[14:16](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=856s) It's a page where you go to Amazon.com

[14:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=858s) or your local Amazon.com,
your marketplace,

[14:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=861s) and you can buy stuff.

[14:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=862s) You could look at the picture.

[14:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=863s) You could look at the price.
You could look at the reviews,

[14:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=865s) and then you could click add to cart,

[14:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=867s) or as we talked about one-click ordering,

[14:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=869s) you do one click ordering.

[14:30](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=870s) So that's a detail page.

[14:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=871s) Now if we take this same page

[14:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=872s) and look at it using an internal tool

[14:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=874s) that's available with an Amazon.com,

[14:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=876s) it might look like this.

[14:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=878s) And I don't know how it's showing
up on the big screen here,

[14:41](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=881s) but each of those little arrows

[14:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=882s) is pointing to a microservice.

[14:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=883s) There's an image microservice.

[14:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=885s) There's a title microservice.

[14:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=886s) There's a stars rating microservice.

[14:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=889s) So what's happening is
when you see a detail page,

[14:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=892s) it's making hundreds of calls

[14:54](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=894s) to hundreds of microservices in parallel

[14:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=896s) marshaling them together very quickly

[14:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=898s) and displaying to you
as a single detail page.

[15:01](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=901s) The advantage here is,

[15:03](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=903s) let's say the star rating
service is having an issue

[15:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=905s) and it can't show you the star rating,

[15:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=906s) it could still show you
the rest of the page,

[15:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=907s) the image, the title,
the price, add to cart.

[15:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=910s) It results in much higher
availability, reliability,

[15:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=913s) and much higher scalability.

[15:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=915s) Also, when I wanna make a change,

[15:16](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=916s) if I wanna change the
title feature somehow,

[15:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=919s) I don't have to like make a change

[15:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=921s) to a big monolith, a big binary.

[15:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=923s) I could just change that one microservice.

[15:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=926s) Here's another example from Amazon.com.

[15:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=928s) Back in 2019 Amazon.com
released a new feature

[15:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=931s) called Subscription Boxes.

[15:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=933s) Subscription boxes, you could
sign up to receive monthly

[15:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=936s) a box of high quality items
in a certain category,

[15:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=939s) like Green Kids Crafts, or
kid's toys, or coloring books,

[15:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=943s) or whatever you want, right?

[15:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=943s) There's a whole kind, Marvel merchandise,

[15:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=945s) all kinds of subscription boxes.

[15:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=947s) And they went to launch this in 2019.

[15:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=949s) And this is the architecture

[15:51](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=951s) for the Subscription Boxes
architecture that they launched.

[15:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=953s) So let me walk you through it.

[15:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=956s) Not that complex, right?

[15:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=958s) You have an API gateway
right there on the front

[15:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=959s) because it's a microservice.

[16:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=960s) It has to present a set of APIs.

[16:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=962s) So that's how it does it.

[16:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=964s) It's got AWS Lambda,

[16:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=965s) which is the AWS serverless functionality

[16:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=968s) where you could deploy.

[16:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=969s) And that contains the business logic.

[16:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=971s) Business logic is deployed to Lambda,

[16:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=972s) so it's able to execute the
business logic serverlessly.

[16:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=975s) DynamoDB, which is the NoSQL database,

[16:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=977s) where it's basically storing state,

[16:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=979s) like who's subscribed to what,

[16:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=980s) and on what date are they expecting

[16:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=982s) to get their merchandise,
that kind of stuff.

[16:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=983s) And the S3 bucket is
pretty much there for logs.

[16:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=986s) Important, but just putting it on there

[16:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=988s) to keep the logs so that

[16:30](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=990s) they could do the monitoring

[16:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=991s) and go back through the logs, et cetera.

[16:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=993s) That's the architecture.

[16:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=994s) Matter of fact, the team
that put this together

[16:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=996s) comprised of three engineers,

[16:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=997s) and they call it a nano service.

[16:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=999s) They said it's not a
microservice. It's a nano service.

[16:41](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1001s) It's that small.

[16:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1002s) But ultimately handles
millions of events per day.

[16:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1005s) So how could this be?

[16:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1005s) How could I show you that
great, cool, new feature

[16:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1008s) and yet that's the architecture?

[16:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1009s) Because that's the key about microservice.

[16:51](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1011s) Does this service have
to worry about pricing?

[16:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1013s) No.

[16:54](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1014s) Does this service have to
worry about the catalog?

[16:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1016s) No, it calls the catalog
to get information.

[16:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1018s) Is this a kid's craft?

[16:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1019s) Is this a coloring book?

[17:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1020s) Is this highly rated, right?

[17:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1022s) Does it have to worry about fulfillment,

[17:03](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1023s) sending the merchandise to the customer?

[17:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1024s) No, it just has to worry about
which items they're gonna get

[17:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1027s) and it tells fulfillment to do it.

[17:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1028s) That's the key to microservices.

[17:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1030s) It does one thing and one thing only,

[17:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1032s) and delegates everything else

[17:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1033s) to the other services around it.

[17:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1037s) Ultimately, all right, so this is...

[17:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1038s) We're gonna show several
of these slides today.

[17:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1040s) So what this is...

[17:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1041s) Kieran talked about the
Well-Architected Framework.

[17:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1043s) Well, another part of the
Well-Architected Framework

[17:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1044s) is the Well-Architected tool.

[17:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1047s) The Well-Architected tool is free to use,

[17:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1048s) available through the AWS console.

[17:30](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1050s) And what the Well-Architected tool does

[17:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1052s) is let you take those best practices

[17:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1053s) that are described by Well-Architected

[17:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1055s) and review your own workloads,
your stuff built in AWS,

[17:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1058s) your own cloud-based workloads,

[17:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1060s) and say, "Am I or am I not
doing these practices?"

[17:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1062s) And based on that,

[17:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1063s) it'll make improvement
recommendations to you.

[17:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1065s) And it's done in a Q&A format.

[17:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1067s) So the question is along the top there.

[17:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1069s) In this case, how will you design

[17:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1072s) your workload service architecture?

[17:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1073s) And you can see in the underlying section,

[17:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1075s) it's talking about SOA and
microservices architecture.

[17:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1077s) The best practices are
the little check boxes.

[18:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1080s) So in this case, the best practice

[18:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1082s) is how you're gonna segment the workload.

[18:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1084s) Are you gonna segment it big,
small microservices, SOA?

[18:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1087s) And also, make sure that
segmentation maps to the business,

[18:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1090s) to the business domains.

[18:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1092s) So those are the best practices

[18:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1093s) that Amazon is exhibiting in
the examples I showed you.

[18:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1095s) And we're gonna refer back
to Well-Architected tool

[18:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1097s) to show you the
Well-Architected best practices.

[18:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1101s) Okay, for the next section,

[18:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1102s) I'm gonna have Kieran talk to you.

[18:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1103s) All right.

[18:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1104s) - Thank you, Seth.
- Sure.

[18:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1106s) - Okay, so now that Seth
has talked a bit more about

[18:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1108s) how Amazon architects their systems

[18:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1109s) in terms of microservices,

[18:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1111s) let's now talk about how they
review and test those systems.

[18:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1114s) Because of course, once
you design a system,

[18:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1115s) you don't just launch it into production

[18:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1117s) and see how it goes.

[18:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1118s) You want to review and test
things before launching

[18:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1120s) to ensure that what you've designed

[18:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1122s) will behave the way you want it to.

[18:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1124s) And this is in alignment
with the leadership principle

[18:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1127s) on insisting on the highest standards

[18:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1128s) where leaders continually raise the bar

[18:51](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1131s) and drive their teams to
deliver high quality products.

[18:54](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1134s) Now, it's important for me at this time

[18:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1135s) to introduce the concept of mechanisms,

[18:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1138s) which is a really important
part of Amazon's culture.

[19:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1140s) This goes back to a quote from Jeff Bezos

[19:03](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1143s) from many years ago,
when he was talking about

[19:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1145s) if you want some kind of real

[19:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1147s) sustainable change in your organization.

[19:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1149s) He said that when you
ask for good intentions,

[19:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1151s) you're not really asking for a change,

[19:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1153s) because people already
had good intentions.

[19:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1155s) Now, most people you meet,

[19:16](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1156s) they try their best to be a good person.

[19:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1158s) They try their best to be a good employee,

[19:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1160s) to do well in their job.

[19:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1161s) If they architect the system,

[19:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1163s) they hope that that system performs

[19:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1165s) as optimally as possible.

[19:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1166s) So, if you want to improve something

[19:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1169s) and you sit down with
your team and you say,

[19:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1171s) "Hey, everybody, let's
make this thing better."

[19:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1172s) And everybody says, "Yes, let's do it.

[19:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1174s) That's not enough.

[19:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1175s) You need some kind of mechanism

[19:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1177s) to measure what you're doing,

[19:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1178s) to ensure that you're
working towards the goal

[19:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1180s) that you've been setting out.

[19:41](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1181s) And your mechanism, as you
can see here in the graphic,

[19:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1185s) generally, a mechanism will
take some kind of inputs,

[19:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1187s) put them through some
kind of formalized process

[19:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1190s) to produce some kind of expected outputs.

[19:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1192s) And there will usually be
tools that are involved

[19:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1195s) in making the mechanism work.

[19:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1197s) You will have to drive
adoption of this mechanism

[19:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1199s) so that people actually use it

[20:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1200s) and so that it will be successful.

[20:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1202s) And the really, really important part here

[20:03](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1203s) is the in inspection part of that cycle,

[20:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1206s) whereby you need to constantly
inspect your mechanism

[20:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1209s) to see if it is having
the intended effect.

[20:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1212s) And if not, then maybe you need to change

[20:14](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1214s) something about the mechanism.

[20:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1215s) And one of the first
mechanisms I want to talk about

[20:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1217s) here in this review and test
section of our presentation

[20:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1220s) is the code review process at Amazon.

[20:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1224s) Basically, any piece of code

[20:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1226s) that is intended to go through production

[20:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1228s) needs to be code reviewed,

[20:30](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1230s) needs to be reviewed by a peer developer.

[20:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1232s) So if you're a developer at Amazon

[20:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1234s) and you wanna push a piece of code

[20:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1235s) that is going out to production,

[20:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1237s) you'll need some peer
of yours to review it

[20:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1239s) and agree that this will
have the intended effect

[20:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1242s) that it's supposed to have,

[20:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1243s) that it is really something

[20:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1244s) that should be pushed into production.

[20:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1247s) And if for some reason
you don't reach consensus

[20:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1249s) between the original
developer and the reviewer,

[20:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1252s) then another reviewer will
be pulled in for example.

[20:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1255s) And it's also iterative.

[20:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1256s) So any code review changes
that are suggested,

[20:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1259s) they themselves then will go through

[21:01](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1261s) another code review process.

[21:03](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1263s) It's also a formal mechanism.

[21:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1264s) It's not a case of just
sitting down with your friend

[21:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1267s) on your team and saying,
"Hey, take a look at my code

[21:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1268s) and let me know what you think."

[21:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1270s) Basically, if somebody approves

[21:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1271s) your code to go into production,

[21:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1273s) then they also become responsible

[21:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1275s) for its success in production.

[21:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1278s) Another mechanism that Amazon uses

[21:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1280s) is the principal engineering community.

[21:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1283s) Principals at Amazon are
very senior technical leaders

[21:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1286s) and experts in their field,

[21:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1287s) They're seen as exemplary
practitioners in the company,

[21:30](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1290s) and their job, among many things,

[21:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1292s) is to continuously learn and
improve their own skill sets

[21:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1296s) also to educate others

[21:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1297s) and help others to improve in the company.

[21:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1300s) And very importantly,
they also need to provide

[21:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1303s) clarity when there's
decisions that need to be made

[21:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1305s) under ambiguous circumstances.

[21:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1308s) And there's a few different
ways that people can

[21:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1310s) interact with principals in the company.

[21:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1312s) So one way is a principal consult.

[21:54](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1314s) That's usually something that happens

[21:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1316s) maybe earlier in a project.

[21:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1317s) If you have some kind of idea

[21:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1318s) and you wanna run it by
a senior technical leader

[22:01](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1321s) and get feedback from them about

[22:03](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1323s) is that the right way
to approach it or not.

[22:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1326s) And then there's also the
principal design review.

[22:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1327s) That's a much more thorough engagement

[22:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1330s) whereby you have somebody,

[22:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1331s) you have an actual technical design,

[22:14](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1334s) you have maybe technical

[22:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1335s) architecture diagram for example

[22:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1337s) that you want to review
with your principal.

[22:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1340s) And they will go through
it in a lot of detail,

[22:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1342s) looking at all of the different API calls

[22:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1344s) and the overall system,

[22:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1345s) and give feedback on any bits
that you may a need to change

[22:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1349s) in that system.

[22:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1351s) And one of the great things

[22:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1352s) about the principal engineering community

[22:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1353s) is that you will find
experts across the company

[22:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1356s) that specialize in different things.

[22:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1357s) So if you need help with
security, or API design,

[22:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1360s) or internationalization,

[22:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1362s) you'll find some expert
who specializes in that,

[22:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1364s) that can help you.

[22:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1366s) And then we've talked about
some of the review mechanisms.

[22:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1369s) Let's move on to testing.

[22:51](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1371s) And when it comes to testing,

[22:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1373s) we're going to use specific test cases

[22:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1375s) that are used by Prime Video,

[22:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1376s) because we want to give
you real world use cases

[22:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1378s) in addition to the concepts
that we'll be talking about.

[23:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1382s) One of the first things that
we'll focus on in this section

[23:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1384s) is Prime Videos preparation for

[23:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1386s) launching Thursday Night Football,

[23:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1388s) Thursday Night Football
was one of the first

[23:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1391s) live streaming sports events

[23:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1392s) that Prime Video supported
on their platform.

[23:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1395s) And so they wanted to make
sure that everything went well.

[23:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1398s) It's the first time they're
doing this kind of thing.

[23:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1400s) But how do you plan and test

[23:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1402s) for something that
you've never done before?

[23:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1404s) Well, the kinds of tests
that Prime Video used

[23:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1407s) were load testing of course.

[23:30](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1410s) They knew this was gonna be a big event.

[23:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1411s) They needed to predict how much

[23:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1414s) traffic they were gonna
expect on their system,

[23:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1416s) and then scale their systems up to that

[23:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1418s) and simulate that traffic

[23:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1420s) and ensure that they can
handle it accordingly.

[23:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1423s) There's also performance testing.

[23:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1424s) This is measuring basically
how is your system performing

[23:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1427s) when it's running at that increased load.

[23:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1429s) Are things like latency increasing?

[23:51](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1431s) Are the number of errors increasing?

[23:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1433s) Then there's also stress testing.

[23:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1435s) This is where you go beyond

[23:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1437s) what you expect your system
to be able to handle.

[23:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1439s) So you keep pushing
more, and more, and more,

[24:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1440s) and try to see if you can find
a breaking point somewhere.

[24:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1444s) Then there's chaos testing.

[24:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1445s) In this case, they are introducing

[24:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1448s) specific failure scenarios
into their testing strategy

[24:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1451s) and seeing how their system behaves

[24:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1453s) under those circumstances.

[24:16](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1456s) And this is in alignment with
the testing reliability piece

[24:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1459s) under the reliability pillar,

[24:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1460s) specifically around testing, scaling,

[24:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1462s) and performance requirements,

[24:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1464s) and using chaos engineering
to test resiliency.

[24:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1467s) Now, no matter how much you plan and test,

[24:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1469s) there will always be things
that happen in production

[24:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1472s) that you weren't expecting.

[24:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1474s) One of the first examples I'll
show here from Prime Video

[24:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1478s) is when they were streaming
a Bundesliga game.

[24:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1480s) This was a soccer match in Europe.

[24:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1483s) And what you can see here on the graph,

[24:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1485s) the two blue vertical lines

[24:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1486s) are the start and end of the game.

[24:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1487s) And you can see these ramp ups

[24:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1489s) that are happening at the beginning.

[24:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1490s) So you see a ramp up
in the stream starting,

[24:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1492s) and a ramp up in people
signing up to watch the game.

[24:54](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1494s) All of this of course was expected.

[24:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1496s) Prime Video had planned for this.

[24:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1498s) What was not expected here is
this huge spike that you see

[25:01](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1501s) right in the middle of the game.

[25:03](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1503s) Now what happened here?

[25:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1504s) Well, basically, this game
happened to get really exciting.

[25:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1507s) It was a game in which two
teams with a lot of rivalry

[25:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1510s) were playing against each other.

[25:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1511s) And in the middle of the game,
it got really, really heated.

[25:14](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1514s) And the atmosphere grew a lot.

[25:16](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1516s) People were posting on
social media about it.

[25:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1518s) People were texting their
friends about it, saying,

[25:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1519s) "You have to watch this
game. It's getting crazy."

[25:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1521s) So lots and lots of people
in the middle of the game

[25:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1524s) subscribed, signed up to watch the game.

[25:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1526s) This is not at all what
Prime Video was expecting.

[25:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1529s) They were not expecting that
in the middle of the game,

[25:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1531s) suddenly a bunch of
people would be signing up

[25:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1533s) to try to watch it.

[25:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1534s) So this is an unexpected thing.

[25:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1536s) And another unexpected
thing that they encountered

[25:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1538s) was when they released a new episode

[25:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1542s) of a very popular TV
show on their platform,

[25:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1545s) and here you can see
the ramp ups happening

[25:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1547s) to when they're launching the episode.

[25:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1549s) All of that was expected.

[25:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1550s) What was not expected in this case

[25:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1552s) was this double spike that happened.

[25:54](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1554s) Now, what happened here
is that this episode,

[25:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1558s) as I said, it was a very popular TV show,

[26:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1560s) and a lot of people, when they watched it,

[26:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1562s) at the end of the episode,
they re-watched it again.

[26:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1565s) They thought, "Oh wow, that
was a really cool episode.

[26:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1567s) I'm gonna re-watch it again."

[26:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1568s) So this again was unexpected.

[26:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1569s) Prime Video was not planning for this.

[26:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1571s) They didn't think that everybody
or lots and lots of people

[26:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1573s) are gonna re-watch the same episode again

[26:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1575s) right after watching it.

[26:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1577s) Now, in both of these cases,

[26:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1578s) Prime Video was able to react accordingly,

[26:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1580s) and they were able to ensure that

[26:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1581s) the people were able to stream
the content that they needed,

[26:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1584s) but it was a learning experience.

[26:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1586s) They learned that you need to be

[26:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1587s) measuring what's going on in production,

[26:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1589s) measuring what your consumers are doing,

[26:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1591s) and reacting accordingly,
and learning from that,

[26:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1593s) because you can't always
predict ahead of time

[26:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1595s) what they're going to do.

[26:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1596s) And this brings us back
to the mechanisms concept.

[26:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1600s) What Prime Video did is they said,

[26:41](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1601s) "Okay, let's take these
learnings from production,

[26:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1603s) and let's incorporate these
into our testing strategy

[26:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1605s) for future events that
we will be running."

[26:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1608s) And so, this is this idea

[26:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1609s) of continuously improving over time,

[26:51](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1611s) using a mechanism to improve your process.

[26:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1616s) Another example of an unexpected thing

[26:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1618s) that Prime Video encountered was

[27:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1620s) when they were doing some stress testing

[27:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1622s) in one of their
pre-production environments.

[27:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1624s) Now, lots of teams at Amazon

[27:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1626s) have pre-production environments

[27:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1627s) that are replicas of their
production environments

[27:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1629s) that you can use for stress testing

[27:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1632s) and integration testing, et cetera.

[27:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1633s) And on one occasion, Prime Video

[27:16](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1636s) was doing some stress testing

[27:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1637s) in their pre-production environment,

[27:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1639s) and they're pushing more and
more load on their system.

[27:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1641s) But the interesting thing that happened

[27:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1642s) was before they found a
problem with their own system,

[27:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1645s) they suddenly started getting throttled

[27:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1647s) by a downstream dependency

[27:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1648s) that was owned by a different team,

[27:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1649s) a different organization, actually.

[27:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1652s) And what happened was that

[27:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1655s) tickets started getting
sent to this other team.

[27:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1657s) The team reached out
to Prime Video saying,

[27:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1658s) What's going on here?

[27:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1659s) We're suddenly getting
a huge amount of traffic

[27:41](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1661s) from your system that
we weren't expecting."

[27:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1663s) And it actually caused
problems for that other system.

[27:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1667s) And the learning here was that

[27:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1668s) if you are going to do stress testing,

[27:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1670s) if you do have downstream dependencies

[27:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1672s) that are owned by other
teams or other organizations,

[27:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1677s) ensure that you should
notify them ahead of time

[28:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1680s) so that they can plan accordingly.

[28:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1684s) Now I want to move on to talking about

[28:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1685s) actual failure injection test.

[28:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1687s) Up until now, I was talking about

[28:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1688s) a couple of unexpected
things that kind of happened,

[28:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1690s) but you want to actually understand

[28:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1693s) what are the kinds of
things that could go wrong

[28:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1695s) with your system ahead of
time as much as possible.

[28:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1697s) And what you're seeing here
are failure injection tests

[28:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1699s) that are used by Prime Video,

[28:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1701s) and the magnitude to which they're used.

[28:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1702s) So you can see that they test for things.

[28:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1704s) They have packet loss a lot
down here at the bottom,

[28:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1707s) also latency injection,

[28:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1709s) and things like memory hog, CPU hog.

[28:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1711s) These are the kinds of things

[28:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1712s) that can happen to many systems,

[28:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1713s) especially if you're streaming
content over the internet.

[28:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1716s) Things like packet loss and latency

[28:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1717s) are things that you need to
be aware of and plan for.

[28:41](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1721s) And it's not enough to
just test for these things.

[28:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1724s) You need to introduce mechanisms

[28:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1726s) to handle them if they occur.

[28:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1728s) And if I go back to the
example I was talking about,

[28:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1730s) about the downstream dependency

[28:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1732s) suddenly throttling their system,

[28:54](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1734s) what they did in this regard

[28:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1735s) is that they implemented
a circuit breaker approach

[28:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1738s) to handle that thing if
it ever happened again.

[29:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1740s) With a circuit breaker pattern,

[29:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1742s) what you do is that if you detect that

[29:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1744s) some downstream system is not responding

[29:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1746s) the way you expect it to,

[29:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1748s) or it's not responding at all perhaps,

[29:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1750s) then you don't wanna keep

[29:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1751s) hammering that system with more requests.

[29:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1752s) That's not gonna make things better.

[29:14](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1754s) What you want to do is
gracefully back off,

[29:16](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1756s) stop sending a request to
that system for some time.

[29:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1758s) And you also want to gracefully
respond to your client

[29:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1761s) that send you the initial request.

[29:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1762s) Either letting them know
that something is wrong

[29:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1765s) or else perhaps you can
use the last cached version

[29:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1768s) of the last good response that you got

[29:30](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1770s) from the downstream system,

[29:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1771s) whatever is appropriate for your use case.

[29:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1775s) It's also really important to plan

[29:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1777s) for your high velocity events.

[29:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1778s) We talked about the live
sporting events earlier, right?

[29:41](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1781s) So, if you have a high
velocity event coming,

[29:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1784s) you need to ensure that you're
gonna have contingencies

[29:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1786s) and mitigation levers in place.

[29:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1788s) And you also want to make
sure that you're prioritizing

[29:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1790s) what are the critical workloads
for the intended experience

[29:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1793s) of this event that you're planning for.

[29:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1795s) And if we think about
live sports streaming,

[29:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1798s) if you have a bunch of customers

[30:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1800s) watching a live sports streaming event,

[30:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1802s) then maybe you don't
need to be recommending

[30:03](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1803s) other content for them to watch

[30:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1806s) when they're consuming that content.

[30:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1808s) So you want to ensure that your resources

[30:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1809s) are dedicated to serving
out that content to them

[30:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1812s) while they're watching that
sports game, for example.

[30:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1815s) And you also wanna make sure this is

[30:16](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1816s) controlled by customer group.

[30:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1818s) So if you have other
customers on your platform,

[30:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1820s) browsing around and watching
on-demand content, for example,

[30:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1823s) you want to ensure that they
are getting the personalization

[30:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1825s) and all of the other types of

[30:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1827s) experiences that they're expecting.

[30:30](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1830s) And this is in line with the
mitigating failure section

[30:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1833s) under the reliability pillar.

[30:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1835s) Can any of you guess what are the ones

[30:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1837s) that we've been talking about here?

[30:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1840s) Yes, you guessed it right again.

[30:41](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1841s) We've been talking about
graceful degradation

[30:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1844s) and implementing emergency levers.

[30:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1846s) Now it's really important to understand

[30:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1848s) that Prime Video didn't come up

[30:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1849s) with all this stuff overnight.

[30:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1850s) They didn't just come up
with all these test cases

[30:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1852s) and this test strategy in
a really short timeframe.

[30:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1855s) It's actually been a multi-year journey

[30:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1857s) that started off with people
doing manual load testing

[30:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1859s) of their own systems.

[31:01](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1861s) And then Prime Video added a
dedicated engineering branch

[31:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1864s) to build tooling to automate
all of these kinds of tests

[31:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1867s) that we've been talking about.

[31:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1869s) And then this grew over time
into communities of people

[31:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1872s) sharing knowledge with each
other across the company,

[31:14](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1874s) sharing feedback to help
improve the tooling.

[31:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1877s) And this goes back to that
mechanism approach again, right,

[31:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1879s) where you're constantly getting feedback

[31:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1880s) to improve over time.

[31:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1883s) And now we've talked about

[31:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1884s) reviewing and testing your architectures,

[31:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1886s) I wanna hand you over to Seth again

[31:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1887s) to talk about understanding
your systems and production.

[31:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1889s) - Great, awesome.

[31:30](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1890s) Thank you.
- Thanks.

[31:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1891s) - All right, yeah.

[31:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1892s) So understanding services
and production that

[31:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1895s) very much aligned with
Amazonian principles

[31:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1898s) that ownership does not end at deployment.

[31:41](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1901s) Amazon has been practicing
DevOps before DevOps was a term.

[31:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1904s) I arrived in 2005 and was handed a pager,

[31:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1907s) and that was before the
term DevOps existed.

[31:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1910s) So, absolutely, the teams were
expected to own production.

[31:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1913s) But this is about diving deep

[31:54](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1914s) and about how leaders
operate at all levels,

[31:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1916s) stay connected to details,
and audit frequently.

[31:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1918s) So this is not necessarily
about any errors in production,

[32:01](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1921s) but conclude that.

[32:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1922s) But it's about how are the
services being used in production

[32:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1925s) and how can you improve them

[32:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1926s) to improve the customer experience.

[32:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1929s) And towards that end,

[32:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1930s) I wanna start off with a
process that happens at Amazon

[32:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1933s) that I think is really important.

[32:14](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1934s) The weekly ops review.

[32:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1935s) Now the ops review is led by the SVP,

[32:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1938s) the senior vice president in
charge of all of consumer,

[32:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1940s) and then the leads from
directors and leads

[32:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1943s) from all of the department there,

[32:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1944s) as well as representatives
from many service teams.

[32:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1947s) It's a big meeting.

[32:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1947s) It used to be a lot in person

[32:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1949s) and a bunch of people online.

[32:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1951s) These days, it's all online.

[32:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1952s) And what happens in this meeting?

[32:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1953s) So number one is success stories
and technical talks, right?

[32:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1957s) This is the time to celebrate successes.

[32:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1959s) So and so team lowered latency by 50%.

[32:41](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1961s) So and so team reduced errors, whatever.

[32:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1963s) That kind of stuff is
definitely important to surface

[32:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1965s) when you have that big an audience there.

[32:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1967s) Reviewing the metrics,

[32:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1968s) that can be part of the success stories.

[32:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1970s) This is about the metrics
of consumer as a whole,

[32:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1973s) Amazon.com as a whole.

[32:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1975s) I'm gonna show you a slide of that later,

[32:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1976s) what the order metrics look like.

[32:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1978s) But those kind of metrics

[32:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1979s) across all the different marketplaces.

[33:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1980s) And then what can be improved?

[33:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1982s) So there is a COE or correction
of error process at Amazon.

[33:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1987s) It's really important,

[33:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1987s) so that when something does go wrong,

[33:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1989s) that's customer impacting,

[33:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1990s) that there's a formalized mechanism,

[33:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1992s) as Kieran talked about,

[33:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1993s) to actually deep dive in
not only one of the causes,

[33:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1995s) but what's gonna be implemented to prevent

[33:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1997s) those kinds of things from
happening in the sure.

[33:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=1999s) And certainly not every COE
is reviewed in this meeting,

[33:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2001s) but a few of the top ones are,

[33:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2003s) and discussed amongst
the senior leadership.

[33:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2004s) It's a really good
opportunity to get exposure

[33:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2007s) for what your team is doing

[33:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2008s) and to learn from what
other teams are doing.

[33:30](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2010s) So in this case, we're gonna
dive into the best practices,

[33:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2013s) not for reliability pillar,

[33:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2015s) but for the operational excellence pillar,

[33:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2016s) which says, how do you evolve operation?

[33:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2018s) And you can see there's
set several different

[33:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2020s) best practices around there about

[33:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2023s) learning from what you're doing

[33:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2024s) and making sure that that
knowledge is distributed

[33:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2026s) and reviewing the actual
metrics and things like that.

[33:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2029s) So a lot of good best practices
exhibited in the ops review.

[33:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2033s) Now, one of the things that's
interesting in the ops review,

[33:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2035s) I don't know if you've
heard about this before.

[33:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2036s) It's the wheel.

[33:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2037s) And the wheel is...

[33:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2039s) It used to be a physical a wheel,

[34:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2040s) but now it's done in a
computer program and online.

[34:03](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2043s) And every tier one service
in consumer is on the wheel,

[34:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2046s) and the wheel gets spun.

[34:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2047s) And at every review meeting,

[34:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2049s) a team gets to share and
go deep on their metrics

[34:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2052s) and what they've been doing.

[34:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2053s) Now, certainly, those metrics

[34:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2055s) and those operational
dashboards that they're sharing

[34:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2058s) are shown at the local level,
at the department level,

[34:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2060s) but there's a chance to
show it at the all up,

[34:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2062s) all consumer level.

[34:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2064s) And amongst the things they share

[34:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2065s) are the metrics dashboards.

[34:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2066s) This is just a piece
of a metrics dashboard.

[34:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2069s) This is like one little piece

[34:30](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2070s) that just shows the number
of requests in the latencies.

[34:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2072s) A lot more things are
gonna be on this dashboard,

[34:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2074s) things like availability, error rates,

[34:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2077s) throttling, CPU usage, you name it.

[34:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2079s) And there's also operational,
like ticket queue

[34:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2082s) and number of high sub
tickets, things like that.

[34:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2084s) So every team, every team at Amazon,

[34:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2086s) the important thing maintains
one of these dashboards

[34:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2089s) with all these metrics on it.

[34:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2090s) So just showing you this
one little piece of it.

[34:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2093s) There's the number of requests
for some Amazon service.

[34:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2095s) You can see it has a day-night cycle.

[34:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2098s) Again, this is per region.

[34:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2099s) This could be US, or it could be France,

[35:01](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2101s) or it could be Germany.

[35:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2102s) I don't know.

[35:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2104s) The other thing is the latency.

[35:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2105s) Notice there's multiple
latency lines there.

[35:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2107s) So p50 would be the median latency.

[35:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2109s) At Amazon, They don't care about

[35:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2110s) median latency really that much.

[35:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2112s) What they care about is the
p99 or the p99.9 latency.

[35:16](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2116s) What does that mean?

[35:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2117s) So the p99 latency is the
latency that 99% of all calls

[35:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2121s) are seeing that latency or better.

[35:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2123s) And by using the p99s or the P 99.9s

[35:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2126s) is a truer measure of all the customers.

[35:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2129s) Ultimately, a service call does

[35:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2131s) somewhere down the down the road

[35:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2133s) correlate to a customer experience.

[35:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2134s) So it's a truer measure of what

[35:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2137s) all or most customers are experiencing

[35:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2139s) then say a median.

[35:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2142s) So I mentioned earlier

[35:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2143s) there's also metrics across the
entirety of Amazon consumer.

[35:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2145s) This is an example of that.

[35:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2147s) This is the orders.

[35:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2148s) The orders are key performance
indicator for Amazon.com.

[35:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2152s) So if something goes weird or wrong

[35:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2155s) with the orders metrics,

[35:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2157s) then it's a strong signal
that there's something wrong.

[35:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2159s) All hands on deck.

[36:01](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2161s) They need to dive into it,

[36:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2162s) and they have mechanisms
and processes around that.

[36:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2164s) But how do you know if something's wrong

[36:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2165s) with the order count?

[36:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2166s) If you see here, again, it has
that day-night cycle, right?

[36:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2170s) Again, this is for a specific region,

[36:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2172s) whether the US or Japan, I
don't know, but specific region.

[36:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2175s) So how do you know if
the orders are dropping?

[36:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2177s) They go up and down all the time.

[36:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2179s) Well, it's important that
you be able to predict

[36:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2181s) and use anomaly detection.

[36:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2182s) So for instance,

[36:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2183s) CloudWatch has an anomaly
detection capability.

[36:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2185s) That would be a good start in AWS.

[36:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2187s) But here you could see this graph.

[36:30](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2190s) The purplish lines are the prediction,

[36:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2192s) and there's a range,

[36:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2193s) 'cause predictions have ranges, right?

[36:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2194s) Predictions are never exact.

[36:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2196s) And then the green line, greenish line,

[36:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2198s) the dark line is the actual order.

[36:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2200s) So you could see everything's
within range here,

[36:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2202s) but using that kind of capability

[36:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2204s) and that kind of anomaly
detection is super important

[36:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2207s) when you're looking at things like your

[36:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2208s) key performance measures, your key KPIs.

[36:54](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2214s) Let's dive into a specific example

[36:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2216s) of another service at Amazon.

[36:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2218s) So Amazon owns Ring.

[37:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2220s) Ring makes cameras, security
cameras for home use,

[37:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2225s) doorbells, hence why they're called Ring,

[37:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2227s) motion detectors, that kind of equipment.

[37:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2229s) It's really, really good products.

[37:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2230s) I own them and I enjoy them.

[37:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2232s) So this is their weekly load pattern

[37:14](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2234s) for their video processing.

[37:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2235s) So someone rings the
bell, it takes a video.

[37:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2238s) Someone can now look at the video.

[37:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2239s) If someone's in your driveway,

[37:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2240s) the motion detection
detects that it's a person.

[37:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2243s) Again, you can look at the video.

[37:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2244s) So this is their video processing.

[37:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2246s) You can see it has that
same day-night cycle.

[37:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2248s) You could see on weekdays,

[37:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2249s) there's sort of a little
double spike there.

[37:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2251s) That's people leaving
their home in the morning

[37:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2253s) and coming back at the
home in the evening,

[37:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2255s) or more activity during that time.

[37:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2257s) And the weekends, they don't
have that double spike.

[37:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2258s) So, AWS and the cloud are
perfect for this, right?

[37:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2262s) The elasticity of the cloud.

[37:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2264s) When you need capacity, you spin it up.

[37:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2266s) When you don't need it, you give it back.

[37:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2268s) Ring uses a combination
of reserved instances.

[37:51](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2271s) You can see there's sort
of a baseline there.

[37:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2272s) So keeping that as your
reserved instances,

[37:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2275s) lower prices is good,

[37:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2276s) and then on-demand
instances when they need it,

[37:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2278s) when they need to go up in capacity.

[38:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2282s) Oops, I went backwards, all right.

[38:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2284s) There we go.

[38:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2285s) So now those spikes
from the previous graph

[38:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2288s) are what you see in the
middle of this graph at noon.

[38:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2290s) So that's...

[38:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2291s) Even just the tiny little shallow bump,

[38:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2293s) that was the big bumps
on the previous graph.

[38:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2295s) So at the end of this graph,

[38:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2297s) there's like a 10X thing going on.

[38:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2298s) So at Amazon consumer,

[38:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2301s) they have Prime Day and Black
Friday, which just happened.

[38:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2305s) And in those cases,

[38:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2307s) a huge spike is expected.

[38:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2308s) But what do you think Ring's,
quote unquote, Prime Day?

[38:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2311s) It's not necessarily Prime Day.

[38:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2312s) What do you think, for this
video processing capability,

[38:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2314s) what do you think Ring's big day is?

[38:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2319s) Halloween.

[38:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2320s) Halloween.

[38:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2320s) Yeah.

[38:41](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2321s) And this is true.

[38:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2322s) I mean, Halloween was not long ago,

[38:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2324s) and I was out trick or
treating with my kids

[38:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2325s) and I kept getting these alerts.

[38:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2326s) There's someone in your driveway.

[38:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2327s) There's someone at your door,

[38:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2328s) someone at your driveway,
someone at your...

[38:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2329s) And I liked it, I loved it,

[38:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2330s) because the worst thing is
buying a big bowl of candy

[38:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2332s) and nobody shows up, right?

[38:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2333s) And especially this year,

[38:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2333s) we didn't know if people gonna show up.

[38:54](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2334s) So it was wonderful to see
all the people showing up

[38:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2336s) and getting the candy.

[38:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2337s) So I really like that.

[38:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2338s) So when you have a big 10X spike like this

[39:01](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2341s) and something predictable,
you should prepare for it,

[39:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2344s) and Ring does.

[39:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2346s) They prepare in advance.

[39:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2349s) This is coming.

[39:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2350s) We need this extra capacity.

[39:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2351s) And for many, most AWS workloads,

[39:14](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2354s) it's a matter of
self-service in the console

[39:16](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2356s) setting up your reserved instances,

[39:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2358s) making sure that you're ready
and you have things in place.

[39:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2361s) If you are a very large scale service,

[39:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2363s) like Amazon.com or Ring,

[39:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2365s) we do recommend you reach
out to your account team

[39:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2367s) and make sure that capacity's there

[39:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2369s) so that they can make sure
they can accommodate it

[39:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2371s) in exactly the kind of instances you need.

[39:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2372s) But either way, the cloud and
AWS can help you with that.

[39:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2376s) All right, so I said this
is about video processing.

[39:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2378s) This is what we're talking about, okay?

[39:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2379s) So the one on the left

[39:41](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2381s) is a situation Ring wants to avoid.

[39:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2383s) This is where there's a...

[39:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2385s) I got a alert.

[39:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2385s) This is my driveway, my minivan.

[39:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2387s) Don't be jealous.

[39:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2390s) And I got an alert saying

[39:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2392s) there's some motion in the driveway.

[39:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2393s) And I go to look at the
video, and it's not ready.

[39:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2395s) What they want is on the right.

[39:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2396s) You get the alert, there's
someone in your driveway.

[39:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2398s) You go there.

[39:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2399s) instantaneous or near
instantaneous video processing,

[40:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2402s) that's what they wanna achieve.

[40:03](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2403s) And why is that?

[40:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2404s) Because if there's a
bunny in your driveway,

[40:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2405s) you don't wanna miss that, right?

[40:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2406s) That's an important event,
seeing a bunny in your driveway.

[40:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2408s) That just happened to be there,
so I thought I's share it.

[40:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2412s) And this, again, I love
sharing these simple,

[40:14](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2414s) it's gonna be like a new
theme, four icon architectures.

[40:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2417s) This is their architecture
for video processing.

[40:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2420s) Basically, raw video comes in on the left,

[40:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2422s) gets put into an S3 bucket
that creates an event

[40:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2425s) which goes on an SQS queue,

[40:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2428s) and then there's a fleet of EC2 instances

[40:30](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2430s) running their transcoder.

[40:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2432s) That fleet is pulling the queue.

[40:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2433s) You got anything for
me? Got anything for me?

[40:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2435s) When it gets a job, it
then goes to the bucket,

[40:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2437s) gets the video, transcodes it, processes,

[40:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2440s) and puts it in the bucket on the right.

[40:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2442s) That's it.

[40:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2443s) So the key here is how do they scale up

[40:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2445s) and how do they scale down?

[40:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2446s) Well, the cloud offers
several ways to do this.

[40:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2449s) They considered...

[40:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2450s) Again, they want that near
instant video processing.

[40:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2452s) They considered using like queue length,

[40:54](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2454s) but queue length is an aggregated metric.

[40:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2456s) It's a trailing metric that
wasn't good enough for them.

[40:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2459s) So they came up with their
own metric that they're using.

[41:01](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2461s) And it's empty receives.

[41:03](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2463s) Think about it.

[41:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2464s) If my workers go pull and
they never get an empty,

[41:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2468s) there's always work there,
it means works backing up.

[41:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2471s) If they go there and they're
always getting empties,

[41:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2473s) it means that I processed everything.

[41:14](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2474s) All the work's gone.

[41:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2475s) And then everywhere in between.

[41:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2477s) But it's not as simple as that, right?

[41:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2478s) There's business logic. There's
proprietary logic in there.

[41:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2481s) How many empty receives means
that we should scale down?

[41:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2485s) How many empty receives
means we should scale up?

[41:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2487s) So what they did is they collect

[41:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2488s) those empty received metrics
using CloudWatch monitoring,

[41:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2491s) and they feed it into step functions.

[41:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2493s) Step functions is a way
you create a state machine

[41:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2495s) and that state machine could run Lambdas.

[41:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2497s) It could do all kinds of arbitrary logic.

[41:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2499s) And that step function is a state machine

[41:41](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2501s) that can then process using
their proprietary logic.

[41:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2503s) Okay, this is the number
of empty receives.

[41:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2505s) That means scale up.

[41:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2506s) So it's in the scale up signal.

[41:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2507s) This is the number of empty receives.

[41:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2508s) That means scale down,
send a scale down signal.

[41:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2510s) And that's how they achieve
that near instantaneous

[41:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2512s) video processing.

[41:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2515s) So, okay, back to the reliability pillar,

[41:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2517s) adapting to changes on demand.

[41:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2519s) The question is, how do
you design your workload

[42:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2520s) to adapt through changes in demand

[42:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2522s) and use automation and scale
up basically when you need it?

[42:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2525s) Those are the best practices

[42:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2526s) from the Well-Architected Framework

[42:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2528s) that we've been talking to you about.

[42:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2531s) All right, final section, going global.

[42:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2533s) So what is the leadership principle here?

[42:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2535s) It's about customer obsession,

[42:16](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2536s) which is actually the first
leadership principle, right?

[42:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2538s) So it's about leaders
start with the customer

[42:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2540s) and work backwards.

[42:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2541s) It's a big phrase at Amazon.com,

[42:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2543s) working backwards from the customer.

[42:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2544s) They work vigorously to earn
and keep customer trust.

[42:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2547s) Amazon customers are global.

[42:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2549s) They're all over the world.

[42:30](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2550s) How does Amazon meet the needs
of those global customers?

[42:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2553s) Well, that's a place
where AWS can really help.

[42:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2556s) And to understand how AWS could help,

[42:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2557s) you look at the AWS global infrastructure.

[42:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2560s) Okay, AWS has 25 regions
all over the world

[42:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2563s) where a region is a set, a multiple set

[42:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2566s) of data center buildings
in a specific region.

[42:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2569s) And there's 25 of these.

[42:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2570s) There's four being added
that were announced

[42:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2572s) as one's being added all the time.

[42:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2573s) This number is just gonna keep going up.

[42:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2575s) But 25 of those around the world.

[42:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2576s) You can see them on the map there.

[42:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2579s) Within each region are
multiple availability zones.

[43:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2584s) An availability zone is
one or more data centers.

[43:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2587s) Okay, so that's important to keep in mind.

[43:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2588s) An availability zone is not
some logical segmentation.

[43:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2592s) It's a physical segmentation.

[43:14](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2594s) So each availability zone
is one or more data centers

[43:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2597s) separate from the other
availability zones.

[43:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2600s) I can even show you on this last slide.

[43:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2601s) There, one or more data centers.

[43:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2602s) And the thing about availability zones

[43:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2603s) is they have their own power,

[43:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2605s) at least their own backup power,

[43:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2606s) and their own onboarding
onto the power grid.

[43:30](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2610s) They have their own
separate water supplies.

[43:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2612s) They're located far enough so
they should not share fate.

[43:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2615s) They're in separate flood Plains.

[43:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2617s) Basically, AWS does a lot of
research on flooding and earth,

[43:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2622s) any natural disaster that could happen.

[43:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2624s) They have geologists working on this

[43:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2626s) to put the AZs in places that
they should not share fate

[43:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2629s) if a natural disaster happens,

[43:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2630s) or if a technical failure happens,

[43:51](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2631s) like a big bulldozer takes
out a big fiber line, right?

[43:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2635s) This means that most AWS workloads

[43:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2639s) can be accommodated with a
high availability architecture

[44:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2642s) just using a single region.

[44:03](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2643s) I wanna make that super clear.

[44:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2645s) Using a single region across
multiple availability zones,

[44:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2648s) you have high availability.

[44:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2650s) If a fire happens, at most,

[44:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2653s) one availability zone should be affected,

[44:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2655s) the other ones keep operating.

[44:16](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2656s) And in other talks I have,

[44:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2657s) we talk about how to architect for that.

[44:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2660s) The cases I'm gonna show you
are a little bit the exception,

[44:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2662s) but they're there in case you need it,

[44:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2664s) which is where services feel
they need to go multi-region

[44:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2667s) in order to achieve their goals.

[44:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2668s) And it's not just about reliability.

[44:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2669s) Again, it's about serving a
global worldwide audience.

[44:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2673s) So the first example is Amazon Ads.

[44:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2676s) So Amazon Ads basically is where folks can

[44:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2680s) put in ads onto the ads platform

[44:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2682s) and expect those ads to show up

[44:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2683s) in various places on
the Amazon.com website.

[44:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2686s) And they wanted to go global.

[44:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2688s) They had a globalization initiative.

[44:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2690s) Now ads is already in multiple regions,

[44:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2692s) but they had a separate
isolated stack in each region,

[44:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2695s) maybes isolated is a little hard.

[44:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2696s) But basically, if you
create an ad in one region,

[44:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2698s) it wasn't gonna show up any place else.

[45:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2700s) It was just in that region.

[45:01](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2701s) And they wanted to find
a better way to share.

[45:03](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2703s) If I put an ad into one region,

[45:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2704s) it could be shared
across multiple regions.

[45:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2706s) So as you can see in
the last bullet there,

[45:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2708s) DynamoDB global tables to the rescue.

[45:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2710s) So what does that mean this?

[45:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2711s) This is the architecture.

[45:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2712s) So now you see three different regions.

[45:14](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2714s) And as ads, content ads
artifacts are created,

[45:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2718s) they go into DynamoDB.

[45:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2720s) Now what global tables does
is allow you to take a table

[45:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2723s) and replicate it across multiple regions.

[45:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2726s) So the same table exists across
all three of these regions.

[45:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2729s) And when you write to
any of these regions,

[45:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2731s) it is automatically replicated
to the other regions.

[45:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2734s) That's the key here?

[45:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2736s) Then you see at the bottom,

[45:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2737s) just going down to the bottom

[45:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2738s) where MSK and DynamoDB and cloud,

[45:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2742s) all the other systems are,

[45:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2742s) that's the old local systems, right?

[45:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2745s) So they don't have to rearchitect those.

[45:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2746s) Those systems just see
everything as usual.

[45:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2749s) They don't know that
something's been replicated

[45:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2750s) in the top layer.

[45:51](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2751s) So what's Lambda in the middle there?

[45:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2753s) Well, that's a nice thing,

[45:54](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2754s) is once you replicate to those
regions, it creates an event,

[45:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2757s) and Lambda react to the event

[45:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2758s) and do whatever kind of
business logic you need

[46:01](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2761s) in that region to make that artifact

[46:03](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2763s) appropriate for that region.

[46:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2766s) Okay, for my next example,

[46:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2768s) I'm gonna refer back to Prime Video,

[46:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2769s) which is something Kieran
talked to you a lot about.

[46:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2772s) And Prime Video, similar to ads,

[46:14](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2774s) it exists, already exists
in multiple regions,

[46:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2777s) AWS regions around the world.

[46:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2779s) We didn't wanna get into the details

[46:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2780s) of what the specific regions are.

[46:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2781s) So we created our own
little fictional map here,

[46:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2784s) and that little blue dot is an AWS region

[46:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2786s) serving this geographic region there.

[46:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2788s) And that's how AWS operated,

[46:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2792s) generally operated for...

[46:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2792s) AWS, how Prime Video operated
for a really long time.

[46:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2796s) And so, you have a customer down here.

[46:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2798s) They're across the continent, right?

[46:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2800s) So they might have some latency issues.

[46:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2802s) They're not close to the AWS region

[46:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2806s) that's serving their traffic,

[46:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2807s) serving their live playback video.

[46:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2809s) And also, if there's some kind of issue

[46:51](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2811s) where for some reason,
it could be in the data,

[46:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2813s) or it could be anywhere
along the network path,

[46:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2816s) where that region can't
serve that customer,

[46:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2818s) that customer's now gonna
experience an outage.

[47:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2820s) So Prime Video looked at this
and said how we avoid this.

[47:03](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2823s) So what they did is kinda similar to ads.

[47:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2825s) Now they can put themselves
in multiple AWS regions

[47:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2829s) within that geographic region.

[47:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2830s) This serves two purposes.

[47:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2831s) One, as you can see,

[47:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2833s) serving the customer much
close to where they are.

[47:16](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2836s) But the other thing is they architected it

[47:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2838s) so that if one region wasn't
able to serve that customer,

[47:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2842s) the other regions in that
geographic locality still could.

[47:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2845s) That results in that high availability.

[47:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2849s) So what is our best practices here?

[47:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2851s) Use fault isolation.

[47:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2853s) Deploy the workload to multiple locations.

[47:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2855s) And I want you to keep in mind,

[47:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2856s) multiple locations doesn't
have to mean multiple regions.

[47:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2859s) Okay?

[47:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2860s) These two examples I gave
you had reasons for that,

[47:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2863s) but multiple availability zones

[47:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2864s) is a perfectly fine way to
satisfy this best practice.

[47:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2869s) All right, in summary,

[47:51](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2871s) we gave you a little history
lesson on Amazon.com.

[47:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2875s) I hope you enjoyed that.

[47:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2876s) And then we told you how they evolved

[47:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2877s) into this multi thousands of
microservices architecture.

[48:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2882s) Kieran talked to you.

[48:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2882s) He talked to you about that,

[48:03](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2883s) And then he talked to you
about reviewing and testing

[48:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2885s) about how Amazon uses mechanisms

[48:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2888s) as part of their scalable
reliability strategy,

[48:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2890s) especially using fault injection testing.

[48:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2893s) We talked about understanding how services

[48:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2895s) operate in production and how we use that

[48:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2898s) to best serve our customers.

[48:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2899s) And we then finished
it out by talking about

[48:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2900s) the globalization and how you can deploy

[48:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2902s) to multiple regions to
meet your customers needs

[48:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2904s) and how Amazon is doing that.

[48:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2907s) So a couple of resources.

[48:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2908s) we're one of the first talks of re:Invent.

[48:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2911s) So we got chock-full of resources here.

[48:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2913s) This is the first of two slides.

[48:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2915s) The first one's on just
Well-Architected in general.

[48:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2917s) That second link I
highly recommend to you,

[48:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2919s) the Well-Architected Labs.

[48:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2920s) I don't know about you,
but I learn by doing.

[48:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2923s) So The Well-Architected labs

[48:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2924s) is a great place where you can go

[48:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2926s) and learn about
Well-Architected best practices

[48:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2929s) by doing labs.

[48:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2930s) Builders' Library is actually
now part of Well-Architected,

[48:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2932s) but it's where those principles
and senior principles

[48:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2935s) have written articles about
how Amazon and AWS operate.

[48:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2939s) and the Well-Architected
Framework white paper

[49:01](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2941s) is a great place to start
for Well-Architected,

[49:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2942s) and that scan code will take you there.

[49:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2945s) And now this is the part
about being early, right?

[49:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2947s) There's plenty of sessions
we could talk to you about.

[49:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2949s) Now, if you wanna learn
more about Amazon Ads,

[49:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2951s) aside from our two slides,

[49:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2952s) you wanna see a whole deck about that?

[49:14](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2954s) Go to Under the Hood at Amazon Ads,

[49:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2955s) so they're gonna tell you all about that.

[49:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2957s) Then a lot of other sessions here

[49:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2959s) about how Amazon operates internally,

[49:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2962s) the sustainability session,
approach DevSecOps.

[49:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2965s) Oh, the ones on the bottom, the INO ones,

[49:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2967s) I recommend those too.

[49:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2968s) The Amazon's culture of innovation

[49:30](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2970s) and how Amazon transforms
experiences using AI/ML.

[49:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2973s) I like those innovation ones

[49:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2974s) 'cause they really talk to you more.

[49:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2977s) If you like that history
lesson part at the beginning,

[49:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2979s) you'd like the innovation talk.

[49:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2980s) So go to those.

[49:41](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2981s) Any other talks you'd
recommend from there, Kieran?

[49:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2984s) - Not really, I think the ads one

[49:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2986s) would be a specific interest.

[49:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2988s) Jeff Barr, our chief evangelist,

[49:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2990s) just posted something
about that this morning.

[49:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2992s) So there's a lot of traction

[49:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2993s) and there's a lot of press around that.

[49:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2995s) So yeah, so I think that's probably one

[49:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2997s) to definitely catch if you can.

[49:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=2999s) - [Seth] How do we get Jeff
Barr to post about ourselves?

[50:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3000s) - I know, right?

[50:01](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3001s) Yeah, yeah, yeah.

[50:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3002s) - Anybody knows, let me know.

[50:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3005s) And anyway, ultimately, thank you.

[50:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3006s) There's some ways you could
reach Kieran and myself.

[50:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3009s) Appreciate your being here.

[50:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3010s) again, Just so thrilled to be here

[50:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3012s) live in front of you all.

[50:14](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3014s) And before you go, we'll
be taking questions.

[50:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3015s) We do not have mic runners,

[50:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3017s) but if you're willing to like step up

[50:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3018s) and state your question,

[50:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3020s) we'll repeat it for you
and answer your question.

[50:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3021s) Thank you.

[50:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3025s) (audience applauding)

[50:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3032s) I stepped on my own applause
by saying we take questions,

[50:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3034s) but yes, thank you for the applause.

[50:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3036s) But anybody any questions
that they'd like answered?

[50:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3038s) Yes, please.

[50:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3039s) - [Audience Member] How do you simulate

[50:41](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3041s) like a global production load

[50:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3043s) in a pre-production environment?

[50:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3045s) - The question is how do you simulate

[50:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3045s) a goal global production load

[50:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3047s) in a pre-production environment?

[50:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3049s) Can I take that one first?
- Yeah, sure, go for it.

[50:51](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3051s) - So I'd say there's two ways, okay?

[50:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3053s) So it depends on how big is
your global production load,

[50:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3055s) how big is your global system, right?

[50:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3057s) For systems of moderate size,

[50:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3059s) you can stand them up in AWS

[51:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3062s) and be a assured that you have something

[51:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3064s) similar size to production.

[51:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3065s) But I think you are hinting at,

[51:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3067s) okay, I can't possibly
stand up my entire system.

[51:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3069s) It's too big.

[51:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3071s) And in that case, it becomes tricky.

[51:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3072s) It becomes a math question, right?

[51:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3073s) When you stand up something

[51:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3075s) that's of smaller size scaled down,

[51:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3077s) it's not linear that the
traffic is linear, right?

[51:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3080s) So it becomes a little more tricky.

[51:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3082s) I will say your secret weapon there

[51:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3085s) is testing in production.

[51:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3086s) Don't go out and do that right away.

[51:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3087s) Don't do that right away.

[51:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3089s) But once you've done your
pre-production testing

[51:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3091s) with your scale down instance,

[51:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3093s) find a time where everybody's
all hands on deck.

[51:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3095s) It's a game day.

[51:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3096s) Everybody's manning the consoles.

[51:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3098s) You have a runbook with
a rollback procedure.

[51:41](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3101s) Maybe it's night.

[51:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3102s) And then actually do
load testing production.

[51:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3105s) It's a legitimate way
to test your production.

[51:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3106s) I'm not saying every month.

[51:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3108s) I'm not saying make it part
of your CI/CD pipeline,

[51:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3109s) but it's a legitimate way to test.

[51:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3112s) Yes?

[51:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3113s) - [Audience Member] How do you manage

[51:54](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3114s) microservices dependencies?

[51:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3116s) - How do you manage
microservices dependencies?

[51:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3119s) You want me to take it
or you wanna take it?

[52:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3120s) - So, one thing that we
showed earlier is that

[52:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3124s) Amazon has built an internal
tool for that purpose,

[52:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3126s) that attracts all
services that are deployed

[52:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3128s) and their dependencies between them.

[52:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3129s) But ways that you can
use AWS services for this

[52:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3133s) is using things like x-ray, for example,

[52:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3135s) that tracks all of your API calls.

[52:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3137s) Whenever you're running
load on your system,

[52:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3140s) you can use x-ray to see
what services are calling,

[52:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3143s) what other services.

[52:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3144s) You can even see what
kinds of latency exists

[52:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3146s) between each call and all
of that kind of stuff.

[52:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3148s) So what Amazon did is that
they took that information

[52:32](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3152s) and pulled it into a tool that they built

[52:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3154s) to keep track of all of these services

[52:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3156s) and what they're doing.

[52:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3157s) And it's also related
to the CI/CD pipelines.

[52:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3159s) So when something gets
deployed to production,

[52:41](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3161s) that is registered in the system,

[52:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3163s) and then the systems
that that interacts with

[52:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3166s) are also tracked accordingly.

[52:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3168s) So, building internal tools

[52:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3170s) and using AWS tools for that also.

[52:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3173s) - I'll add to that.

[52:54](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3174s) Amazon was bad at that
circa 2005, 2010, right?

[52:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3177s) 'Cause we showed you the organic growth,

[52:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3179s) and it was something that Amazon

[53:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3180s) didn't really take into account.

[53:01](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3181s) And I remember being on
a team in 2006, 2007,

[53:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3184s) where we want to deprecate a service

[53:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3185s) that was called by hundreds,

[53:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3187s) maybe thousands of other services.

[53:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3188s) And they had no idea
who their clients were.

[53:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3190s) That's a problem, right?

[53:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3191s) You could send them all
the emails you want saying,

[53:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3193s) "Hey, if you're a client,
we're gonna be deprecating,

[53:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3195s) but you're not gonna get everybody."

[53:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3197s) So, that's not how it is today.

[53:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3199s) But yeah, I think the
pain of experiencing that

[53:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3202s) led to Amazon building the systems

[53:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3203s) that Kieran was talking about.

[53:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3206s) - And just adding on to
the previous question

[53:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3209s) that Seth was mentioning
about testing in production.

[53:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3211s) When we were showing the
Prime Video stuff earlier,

[53:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3213s) we were showing load testing

[53:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3215s) and performance testing, et cetera.

[53:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3216s) They do actually do some
load testing in production.

[53:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3219s) Of course, in each region,
it would be off peak

[53:41](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3221s) when people are asleep or whatever,

[53:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3223s) and when you have relatively
low traffic on the system.

[53:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3226s) You don't do it in the middle of the day.

[53:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3228s) But then that that's for load testing.

[53:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3230s) You don't do stress testing in production.

[53:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3232s) You don't try and break
your systems in production.

[53:54](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3234s) That's an important thing
about chaos testing also.

[53:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3237s) I mean, people often
talk about chaos testing

[53:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3239s) as if it's, oh, you just start

[54:01](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3241s) rebooting servers in production
and see what happens.

[54:03](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3243s) That is not at all a good way
to approach chaos testing.

[54:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3246s) When we talked about Prime
Video's testing journey

[54:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3249s) about how it's been this long
term, multiple year thing.

[54:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3252s) They didn't come up with it overnight.

[54:14](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3254s) They didn't start doing
chaos testing in production.

[54:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3257s) Basically, you do all
of the stress testing

[54:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3259s) and failure objection testing
in your pre-prod environments

[54:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3261s) as much as possible.

[54:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3263s) - Yeah, another thing I wanna add

[54:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3264s) is Amazon.com does load testing

[54:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3266s) and stress testing like
Kieran was talking about.

[54:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3268s) Specifically, all teams are expected

[54:30](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3270s) to test in pre-production
to the breaking point

[54:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3273s) and measure how long it
takes them to recover.

[54:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3274s) That's actually one of the
metrics of the stress test.

[54:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3278s) - All right.
- Other questions?

[54:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3282s) Anybody?

[54:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3284s) - [Kieran] Oh, there's one over here.

[54:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3285s) - All right.

[54:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3287s) - [Audience Member] How do
you advise doing multi-region

[54:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3289s) when you're serving terabytes
of data with different...

[54:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3293s) (audience member faintly speaking)

[54:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3298s) - How to do multi-region when
you have terabytes of data?

[55:01](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3301s) Well, I mean, there's a trade-off, right?

[55:03](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3303s) And doing multi-region doesn't mean

[55:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3305s) all data's copied everywhere, all right?

[55:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3307s) So you can do multi-region
where only a select set of data

[55:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3310s) is copied everywhere,
maybe some of the metadata,

[55:13](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3313s) but some of the customer data
is stored in a certain region.

[55:14](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3314s) And when you need to read it or write it,

[55:16](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3316s) you can route your reads
and writes to that region.

[55:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3318s) That's a partitioned approach.

[55:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3321s) You could even for some.

[55:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3323s) Yeah, so that's one way to do it.

[55:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3325s) I mean, AWS will give you native tools

[55:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3328s) to replicate that data.

[55:30](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3330s) DynamoDB global tables,

[55:31](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3331s) S3 cross region replication.

[55:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3334s) The question is,

[55:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3335s) do you want to actually send
all that data over the wire,

[55:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3339s) or can you pick a subset of it?

[55:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3340s) And I think the tools are there,

[55:43](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3343s) and it'll work with terabytes of data.

[55:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3345s) It would just be costly.

[55:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3346s) - Yeah, the cost,
there's a cost trade-off.

[55:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3348s) That's the thing.

[55:49](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3349s) So you need to determine,

[55:50](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3350s) do you nee to replicate all of the data?

[55:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3352s) Is there data that's hot
in different regions?

[55:54](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3354s) And then for colder calls,

[55:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3355s) you can go cross region, for example.

[55:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3357s) So yeah, it basically
comes down to the workload.

[55:59](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3359s) I need all data replicated
or just some of it.

[56:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3364s) - [Sean] Hey, more questions.

[56:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3365s) We love the questions part.

[56:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3368s) Yes.

[56:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3370s) - What kind of tools do you
use or have used in this case

[56:14](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3374s) for testing and monitoring?

[56:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3377s) - Oh, what are the tools
for testing and monitoring?

[56:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3378s) So, the funny thing about
working at Amazon.com

[56:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3382s) is the great stuff you get in AWS

[56:24](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3384s) actually started off
usually as Amazon.com tools

[56:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3387s) that were then people said, "This is cool.

[56:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3389s) Let's externalize it."

[56:30](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3390s) So in a lot of ways,
Amazon.com uses plenty of AWS.

[56:33](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3393s) Don't get me wrong.

[56:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3394s) But a lot of these internal kinda tools

[56:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3395s) tend to be different than the AWS tools,

[56:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3398s) the homegrown tools that
then ultimately become

[56:40](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3400s) the AWS tools.

[56:41](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3401s) And then it's hard to everybody
migrated onto the AWS tools.

[56:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3405s) It's working. Why do it?

[56:46](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3406s) But it does happen?

[56:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3408s) Case in point is monitoring,

[56:51](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3411s) Amazon had its own internal
monitoring systems.

[56:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3413s) CloudWatch came along.
Now it's all CloudWatch.

[56:55](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3415s) Actually, it's even better than that.

[56:57](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3417s) The old monitoring portal is still there,

[57:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3420s) but it's all CloudWatch under the covers.

[57:03](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3423s) But if you wanna do fault
injection type testing,

[57:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3426s) then FIS, the Fault Injection Simulator,

[57:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3429s) is gonna be a great option.

[57:10](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3430s) I actually have a workshop
about this this afternoon.

[57:14](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3434s) That's a native AWS service
and there's lots of other

[57:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3437s) commercial and open source products

[57:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3439s) chaos toolkit comes to mind out there

[57:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3441s) for doing that kind of
fault injection testing.

[57:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3445s) Anything to add?

[57:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3446s) - No, I think you captured that one well.

[57:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3448s) it's mainly CloudWatch,

[57:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3449s) but originated from internal
systems that Amazon had built.

[57:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3455s) - And that was one of the things

[57:36](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3456s) Kieran talked about onboarding.

[57:37](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3457s) So I'm get and say Prime Video created

[57:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3459s) their own internal frameworks for

[57:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3462s) fault injection testing,
and monitoring that testing,

[57:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3464s) and then getting ready to adopt

[57:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3465s) was part of the cultural challenge.

[57:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3467s) Yes.

[57:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3468s) - [Audience Member] So you talked about

[57:48](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3468s) the amount of services,
but eventually AWS services

[57:51](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3471s) have kinda soft and hard limit.

[57:53](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3473s) So what if you hit the hard
limit on that specific workflow?

[57:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3478s) - Well, the question is every AWS service

[58:00](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3480s) has soft and hard limits.

[58:02](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3482s) What happens when you hit a hard limit?

[58:05](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3485s) So I guess there's two
kinds of hard limits, right?

[58:07](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3487s) 'Cause there's limits you
can increase yourself,

[58:09](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3489s) using quotas, AWS quotas in the tool.

[58:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3492s) Then there's limits
that you need to contact

[58:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3495s) your account team for.

[58:16](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3496s) Those are sort of like
the medium hard limits.

[58:17](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3497s) And then there's hard limits.

[58:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3499s) There's just nothing more than that.

[58:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3502s) That's a case by case thing, right?

[58:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3503s) How do you architect around that?

[58:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3505s) I mean, we're not talking
about number of EC2 instances,

[58:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3507s) I don't think, right?

[58:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3508s) I mean-
- No, again, if you have...

[58:30](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3510s) For example, you show
Lambda or anything else.

[58:34](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3514s) Do I have permission to do that

[58:35](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3515s) and try access the same service right now?

[58:38](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3518s) - Yeah.

[58:39](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3519s) So yeah, what are the
concurrency limits on Lambda?

[58:42](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3522s) Do they tap out at a certain hard limit?

[58:44](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3524s) - Yeah, they do.

[58:45](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3525s) So, it's also important to remember that

[58:47](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3527s) limits are per Amazon, per AWS account.

[58:51](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3531s) - [Sean] Yeah.

[58:52](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3532s) - So we do work with lots of
very large systems in Amazon

[58:56](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3536s) that span across many, many accounts,

[58:58](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3538s) some of them across hundreds
of different AWS accounts.

[59:01](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3541s) And you can use things
like AWS organizations

[59:04](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3544s) to share things across
accounts and all of this,

[59:06](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3546s) but it gets pretty complex at that point.

[59:08](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3548s) Once you need to go
beyond a single account,

[59:11](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3551s) then there are ways to architect

[59:12](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3552s) for using services and sharing resources

[59:15](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3555s) across accounts, et cetera.

[59:16](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3556s) It does get pretty complicated.

[59:18](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3558s) - All right, I think we're out of time.

[59:19](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3559s) By the way, you folks have stayed

[59:20](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3560s) for the questions and answers.

[59:21](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3561s) You're the smart folks.

[59:22](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3562s) It's the best part of any talk,

[59:23](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3563s) is when you learn the real stuff.

[59:25](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3565s) So appreciate your staying.
- It's true.

[59:26](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3566s) - Appreciate you being here.

[59:27](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3567s) Thank you so much.

[59:28](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3568s) - Thanks, Everybody.
- All right.

[59:29](https://www.youtube.com/watch?v=_AhfV5LZmvo&t=3569s) (audience applauding)

