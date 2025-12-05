# AWS re:Invent 2021 - Beyond five 9s: Lessons from our highest available data planes

[Video Link](https://www.youtube.com/watch?v=GTLfM8ofmwE)

## Description

Every AWS service is designed to be highly available, but a small number of what we call Tier 0 services get extra-special attention. In this session, discover how AWS has built and architected Amazon Route 53 and the AWS authentication system, which is designed to survive cataclysmic failures, enormous load increases, and more. Learn our approach to redundancy and resilience at the infrastructure, software, and team levels. Explore how teams tasked with keeping the internet running manage themselves and keep up with the pace of change that AWS customers demand.

Learn more about re:Invent 2021 at https://bit.ly/3IvOLtK

Subscribe: 
More AWS videos http://bit.ly/2O3zS75 
More AWS events videos http://bit.ly/316g9t4

ABOUT AWS
Amazon Web Services (AWS) hosts events, both online and in-person, bringing the cloud computing community together to connect, collaborate, and learn from AWS experts.

AWS is the world’s most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally. Millions of customers—including the fastest-growing startups, largest enterprises, and leading government agencies—are using AWS to lower costs, become more agile, and innovate faster.

#AWS #AmazonWebServices #CloudComputing

## Transcript

(upbeat music) - Hi, welcome to Beyond five 9s, which is all about lessons from our highest availability data planes. I'm Colm, I'm a VP and
distinguished engineer here at Amazon Web Services, and we're gonna be joined by Yasemin who's a principal engineer
at Amazon Web Services who works on Kinesis. And today we're gonna
share a bunch of insights into how we build our most
highly available systems. What's going on under the hood or behind the scenes, so to speak. We've gone into great detail
about some of these topics in our Amazon Builders Library series, but today we're gonna cherry pick some of the best lessons
and condense them down into 10 simple things
hopefully you can take away and apply to your own
systems as you build them. These lessons come from systems that have stood the test of time and had very good availability records, which is not easy to achieve. We've talked about this before and some of the lessons are eternal and some of the lessons are new. But the first one that
we're gonna start with is definitely one that's eternal, which is it's all about insisting
on high standards. Nothing we're gonna go into,
there's no tip or trick or magic that we have for you
that can ever replace paying very strong attention to
detail in how we build systems. There's a few things I'm
always reminded about when I think of this. One is something I learned
from Werner Vogels, our CTO a long time ago,
which is that when you have systems that are processing
billions of requests, or even trillions of requests over short periods of time, pretty much anything that
could go wrong in the system will be going wrong at some point in time. Some request somewhere
is probably experiencing, even a one in a billion failure, because you have billions of requests. And so it requires paying
enormous attention to detail, looking for every single error case, looking for everything that
could possibly go wrong and having a plan for that in the code and in testing and everywhere. And that kind of culture at team level, there's just no substitute for it. Having teams who are willing to constantly raise the bar on testing,
constantly write new and interesting tests or come up with ways to make testing itself easier. A lot of that is where the
quality and high availability in our systems comes from, and like I say, there's no substitute for it. And I often think that
that kind of quality comes about from great habits. It's from what we do over
and over and over again, and it's really hard to
approach a system and go "I'm just gonna add quality to it. "I'm just gonna try to make
it better than it was before." It's more like something pervasive that has to be there from the beginning. And so something we've been
paying special attention to on this kind of quality
dimension for a long time now is deployment safety. Where we write our code and
we go through code review, collaborative code review and so on in back and forth processes, like you'd be very familiar with. But once we've checked in our code, we actually have quite
sophisticated deployment systems that take over after that and take charge of getting that code from the fact that it's been checked in all the way to running in production. And that system has been designed in a way where it generates a
lot of positive safety for our systems. Whenever we're deploying new code, that always means some risk. We try to be very paranoid
about our testing, we try to be very creative in our testing and test it in every possible way, and I'll talk more about that later, but new code that hasn't been
run in production before, there's always some chance
that it might encounter some condition that we didn't plan for. And so we've got CI/CD
processes that make sure that without us having to be too involved, that code will go through pretty careful, deliberate testing and
deployment as it goes. So we'll deploy it to maybe
just one box to start with and see how it goes,
there'll be some tests run and that box will have to
pass all of those tests under every condition. And if it doesn't, we've got
fast and reliable rollback, that's actually pretty important too. But if it does go well, it gets promoted and the idea is the
more and more confidence we have in that code,
the broader we're willing to run that code. So as we develop confidence in it because it's passing more and more tests, we'll promote it from just
one box to one cell maybe, or one availability zone, one region, multiple regions and so on. And this is something we've gone really, really deep in our culture. Every development team at
AWS knows and understands this deployment process pretty intricately and knows how to get the most out of it and designed our deployments
and code in a way where they're gonna extract
the most benefit from them. We've seen a lot of return from this. It's been a great mechanism for us to deliver high availability in systems, and the occasional issues that it catches are well, well worth it. So that's our first first thing and the first example of
insisting on high standards. The next, and certainly we
haven't really talked too much about before, is how
we manage our systems, So there's this concept out there, which really condensed it
down for me and I love, about you wanna manage your systems more like cattle than pets, in that you wanna be able to think of them in abstractions and not be managing literally one host or
one server at a time, because that's not very scalable. And actually most systems
at AWS have long been beyond the scale that
can be managed by hand. Even the systems at AWS
when I joined 13 years ago, were already quite far beyond that scale. Today we use the same
concepts you'd be familiar with to manage systems. We have auto scaling
groups, VPCs, subnets, security groups, all of these things. Internally, we have this
concept called host classes that are very similar, and
they just let us manage collections of machines without having to think about the individual machines. And our deployment systems,
they work on top of that. They clone these entire abstractions between regions, for example. But we've actually been
going much, much further. So we've learned that
we we have to be able to operate our systems in hands-off ways, both for safety, operational
safety, and for security. And typically AWS operators,
like me as a developer, just simply don't have
access to every AWS region. And so I could never
really plan on being able to log in or access the
system to do something. It's just not our
operational model at all. And then we have some
systems like AWS Outposts and Snowball that are
designed to be disconnected for periods of time. We may just have no access to them. Nobody may have any
access to them for a while because of the nature of the product. And so we've really had
to double and triple down on the the automation that it takes to be able to operate in that environment, to have systems that are self-healing, and that can take care of themselves. We have two classes of systems these days. We've got Bastion systems where
we have very limited access to those systems via what
we call Bastion servers or Bastion hosts that let us recover systems typically if
there were some urgent need to or something like that. But with a strong record of the fact that folks have had to do something with that system and
notification processes for that and so on. But we also have systems
where increasingly that's just not an option. There's no general purpose, interactive, administrative access,
and even in the event of having to recover a system, there's simply no general
purpose way to access it. And instead we have to
have built in in advance all the mechanisms that we would need. The AWS Nitro System is a
really strong example of that. That's the system that runs
our modern EC2 instance types. There's simply no mechanism at all where I or someone else could go run a command on that system or access it in
some kind of interactive way. Instead, everything's done via preplanned, pre-secured, fully authenticated
and encrypted APIs, and that's the only way
for things to happen. And we found great motivation
for this is security, but this talk is about availability and a great benefit for availability too is it just means there's no possibility of any on-track changes
and there's no possibility of somebody did something to fix something and then forgot about it
or anything like that. It can't be that kind of system; instead, it's much more hermetic. So that's our second item. I'm gonna hand over to the Yasemin who's gonna now tell us about
the third item on our list. - Thank you, Colm. Well, while we design to
avoid failures altogether, we also design with failures in mind. This is mainly because we know that failures may happen in rare cases and we want to make sure
that the blast radius of such events are as minimal as possible. I will discuss four techniques
that we use for this purpose. The first technique we
use is regional isolation. AWS Cloud spans 25 geographic
regions around the world, and there will be eight more regions that are announced to be launching soon. Each AWS region region is
isolated from each other, both geographically, as well
as on the software stack. AWS services offer regional endpoints, enabling direct access to that region. Using regional isolation, any
rare failure that may come up in one region, stays in that region. Say for example, we have an
event going on in us-west-1, it will be contained within the region and will not spread to
any of the other regions. The next technique we
use is zonal isolation. Each AWS region offers
multiple availability zones within its periphery. Availability zones are data centers that are miles away from each other. AWS Cloud has 81 availability zones across the world with
24 more launching soon. Similar to regions, AZs are
also isolated from each other. A failing in one AZ, let's say us-west-2a is having an event, will not spread to any of the other AZs. One example why we leverage this property is regional services. There'll be multiple availability
zones serving traffic rather than to a regional endpoint. This way, in the event of
availability zone failures, traffic will be redirected
to healthy zones behind the region and
customers will not be experiencing any degradation. So far, we discussed
physical compartmentalization of architecture by using AWS
regions and availability zones. These two have regional and zonal blast radius impact accordingly. We apply cellular isolation to further reduce the blast
radius impact of events. In this technique, we build
dedicated software stacks, which we call cells. Cells are isolated from each other, with their own dedicated endpoints. Customers get assigned
to one of these cells. Imagine there are eight
customers and four cells. We have two customers
assigned to each of them. Since cells are isolated from each other, failure in one cell, let's say
cell two is having an event, will not spread to any of the other cells. That means it's only the
customers assigned to that cell, the palm tree and stars in this case, will be impacted, but no other
customers will be impacted. This is pretty good. It's much better than a zonal
and regional blast radius that we discussed before,
but can we do better? We do better by using shuffle sharding. In shuffle sharding, we divide the service into smaller compartments, which I will call partitions;
in this case, the blue boxes. And we assign customers to
partitions, not one-to-one, but we assign multiple
partitions to a single customer. In this case, I have two partitions assigned to each customer. So let's evaluate the blast radius impact of failures in this case. Let's say partition
one is having an event. In that case, both palm tree and stars have another partition that's healthy. Therefore they will not see impact and they will continue
to operate just fine. It's only the time when both partitions of a single a customer having an event that that customer will see the impact. And in this case, when
partition four is also out, it's the stars that will see the impact because those two are
shared partition for stars, but palm tree and hiker
will not observe any impact. So there are two benefits that
I'd like to highlight here. The very first one is
creating customer impact is much harder with shuffle sharding. This is mainly because it
takes multiple partitions to have a failure to create an impact and the probability of having a failure across multiple partitions is much lower than the probability
also of having a failure on a single partition. The second benefit is
that even in the event of those very, very
rare probability events that are happening across partitions, the impact created to the
customer is much lower. We have one customer being impacted in the case of two partition failures, compared to impacting multiple customers than the regular sharding
scheme would actually create. Next I'll discuss circuit breakers. Circuit breakers is
one of those techniques we use to eliminate failures, and I will discuss two examples. The first one is load shedding. We know systems can slow down or sometimes even fall
over on the access log. We design to make sure that our services are not
vulnerable to this problem. To address this issue, we first identify the maximum capacity of every individual component. We use stress testing
to get this information, then we install the load shedders locally within the services to monitor
the traffic being served. Once it starts receiving traffic more than its predefined
maximum capacity limit, the load shedders start
rejecting any excess load. They are designed to reject
the load very quickly without spanning much off
the system's resources. This way we ensure that systems continue to operate successfully under excess load. The other circuit breaker that I'll discuss is bullet counters. This pattern gets used frequently on external monitoring applications, like health guardians in this case. These applications are common across AWS because we want to make sure
that we are the first ones to detect any problem that may be ongoing and mitigate it right away before customers are even noticing it. For example, these applications then pair the health checks to each
and every node of the system to ensure that they are all healthy. If there's a bad node being detected, they would replace the node. While it sounds straightforward, the part that's interesting
about these systems is that they are very, very powerful. Replacing a node is that powerful action. Imagine a health guardian determined that half of the fleet is unhealthy. Should it go head and just
replace all those nodes? Maybe, but usually not. It really depends on what the problem is. We built to not have such
large failures anyways. So to avoid these automations to take significant actions that will lead to significant changes, we installed both counters in place so that they don't act on
positive signals incorrectly. So bullets counter in this example would be the one that we say
what's the maximum percentage of the fleet that could be
replaced safely at a given time? The bullet counters
monitor the actions taken by the health guardian and whenever there is an
event where there are nodes that are being determined as more than the predefined maximum limit, they will stop the execution and instead, they will notify the operators to show up and assess the situation. Using bullet counters, we
ensure that automation always operate within known and safe limits. With that, I will hand it over to Colm. - Thanks, Yasemin. So, as I mentioned briefly earlier, testing is of enormous importance and we invest a lot in testing. In fact, for our most
highly available systems, it's not unusual to spend
much more time on testing code than writing the code itself. We have unit tests, we've
got end-to-end tests, we've got integration tests and we've even got formal verification. We've got pre-production environments. Even these days we'll
test how a system copes with rolling forward through
a deployment process, as well as rolling back
through the deployment process before we ever really
deploy to production, just to make sure that if
we had to do those things, we would be able to. If you wanna see examples of how we raised the bar on testing, you can look at our open
source projects on GitHub. So our s2n project which
is our open source SSL and TLS library is developed
by a team in Amazon who work just like any
other team in Amazon. And it's a really simple,
open view into how we work. And you can see just the
sheer staggering number of tests that are there that are running on every single build. We don't just run those
tests before we deploy, they're integrated into our CI/CD process and every time we check
in, we run them all and we make sure that they all pass before promoting, just to make sure that there are no regressions. And that's very, very typical for these high availability systems. But we've been going further. And so in the last few years, we've actually been
going further and further with automated reasoning
and formal verification. So this is something we've
been doing for a long time. On the s2n project, we've
been formally verifying the correctness of parts of
s2n for about six years now, but in the last few years, we've been able to get to the point where now I'm gonna say regular developers who don't have specialized
training in automated reasoning or formal verification are
able to use these techniques because we've improved the tooling. It's getting easier and easier. And this is amazing because
formal verification tests can always prove that code is correct for a particular input, but formal verification can prove that that code is correct for
any particular input. So it's very, very powerful. It can find really hard-to-find edge cases that you won't find using
any other technique. And it's pretty awesome
now that we're able to get to the point where regular software developers like me can actually use these tools and improve things about their code. And if you're interested in some of that, I'd encourage you to check out CBMC, which is a tool we've been using on s2n that is very intuitive and I found very easy
to use for developers. So the next item on our list is something called lifecycle management, which we've found that
to get high availability over long periods of time in our systems, we need be very, very
intentional about how we manage the life cycle of a lot of
aspects of those systems. And in particular, any kind of credentials that are used by those systems, so that's things like keys
and certificates and so on. So modern security and
compliance frameworks demand that credentials be frequently rotated, and that makes sense. No-one wants a key or a certificate around that could be used for
very long periods of time, but at the same time expired
and mismatched credentials could be a source of outages. If a certificate or key expires and it's still in your system,
that's not gonna be good. So we've learned to decouple
that expiry from alarming. So we alarm well before the expiry time of any key or credential. And we've learned to be super intentional and go into overkill on how to monitor it. So we've got time to expiry metrics for anything that expires. We look at that from both
the server side perspective, so the thing that might
be serving a certificate or using a key, and the client side, the thing that's connecting to it. Like I said, we alarm and investigate well before there's any kind of a problem. And then on top of that, we've
got additional fail-safes and canaries that are constantly scanning for anything that looks
like it's even close to expiry so that we've got
another safety net there too. And then with all of
those systems combined, we've learned that that means we need to deploy any new key or credential, make sure it's absolutely everywhere that could need it before we activate it, and only then activate
it and kinda do the same in reverse whenever we're deactivating or revoking a key or certificate. And we found that paying
particular attention to detail in those processes
has been really key to avoiding just any kind
of outage you could see from just expired or mismatched
keys and credentials. And so with that, I'll
hand over to Yasemin who's gonna tell us about
modular separations. - Thank you, Colm. Modular separation. We avoid multiple architectures and decoupling individually
responsibilities into their own dedicated components. Control plane versus data plane separation is a good example of this. Most AWS services have this
notion of control plane and data plane APIs. Let's take Kinesis data
streams as an example. Kinesis data streams is a
real-time streaming service that enables customers to write records into a log stream and read them later on. The very first thing customers do when they start using the service, they go ahead and create a stream. Create stream is a control plane API. Once the stream is created, producer applications can start ingesting the data continuously
and consumer applications read those records within milliseconds. The APIs used by the producer and consumer applications
are the data plane APIs. As we see in this example, access patterns of these two
types of APIs are different. Consequently, their dependencies
are very different as well. For example, control
plane APIs are depending on the asynchronous workflows to execute the steps of creating a stream, versus data plane APIs are
dependent on the data store to fetch the records within milliseconds. By decoupling the two API types, we limit the impact their
dependencies could be creating. For example, if there's
an event that's going on on the async workflows,
then it's going to be only the control plane APIs
that are being impacted while the data place
APIs continue to work. The next technique is static stability, and this technique works hand-to-hand with modular separation. Availability of a system can be as good as the availability of its dependencies. For this reason, we strive
to keep the dependencies of systems to an absolute minimum. Let's get back to control plane versus data plane discussion again. The dependency here that I didn't discuss before is the metadata store. Metadata store is the one
that parses information about resources, Kinesis
streams in this case. So stream creation execution
has direct dependency to the availability of metadata store because it needs to parse the information that the stream is creating. Imagine there's an
outage on metadata store. We expect the async
workflows to be impacted because it cannot access
the data story anymore therefore, the control
plane APS are impacted. Let's check the impact of
metadata store on data plan APIs. Well, data plane APIs also need to know about these streams and
where they are located so that they can serve,
put and get APIs on them. So if the data plane APIs have direct and synchronous dependency
on metadata store, then its outage will also
impact the data plane APIs. Well, that's not great. It's a large blast radius impact. So the sole dependency of data
plane API is really the data store that are responsible
for serving customer records. So considering the static
stability principle, let's look at this design and see how we can eliminate
the metadata store dependency from data plan APIs. We eliminate this dependency by moving the metadata store
dependency of data plane from being a synchronous dependency to be an asynchronous dependency. In this architecture, the
metadata store keeps track of the streamer and information. And here it has a copy of
this information stored within the data plane itself. Any updates that are being
applied to this metadata gets propagated the data plane and its own snapshot asynchronously. In this case, if there's an
outage in the metadata store, it's the control place
APIs that will be impacted, but the data plane APIs
will continue to work by using the smaller
version of their snapshots they stored within themselves. This way we ensure that the
data plane is statically stable by using its absolute
minimum set of dependencies. - Thanks, Yasemin. So our ninth and penultimate
item is constant work, which is whenever we were learning big O notation, if you studied computer science, you probably learnt about
systems that are constant work. That means O1 right at big O notation and that turns out to be
a very important concept for some of our highly available systems. In general, risk is proportionate to rates of change in systems. A spike in load, for example, can cause the system to slow down, and then the system gets into a mode that it's not used to operating in, things don't really
know how to handle that, they might start timing out and so on. And issues like that can
cause cascading failures. And so we've learned that
reducing the overall dynamism in a system, the amount of
change it can even go through is a useful way to make them simpler and to reduce all that risk. And a counter-intuitive solution to wrangle that risk is
actually to run the system at maximum load all the time. And even though that sounds like, well, now the system is gonna
be maxed out all the time, it actually reduces the amount of dynamism and change that's in the
system, and therefore risk. A really simple example
of that is how we apply this constant work pattern to,
say, configuration changes. So really common pattern in how developers manage configuration changes
is a customer makes a change, that change gets ingested into the system, it's like a delta. Do this thing, do X, do Y. And that goes into our workflow and the workflow manager
is getting that change out to all of the systems that
need to reflect that change. That works, that's a simple pattern, but the problem is when
lots of changes happen from lots of customers at the same time, maybe it's a particularly
busy day or whatever, the overall system slows down, because the workflow
has got more work to do. And as I said, it could hit
you in ways that cascade. So a simpler version of this
is imagine every customer, they make their change and
it's just reflected as, say, a file or key in S3. That's it, they just make their change and it's effectively
a file or a key in S3. And the system on the other side, instead of using a workflow, all it's doing is checking
all of those files every single time, just
downloading every single file from S3 and using that
as its configuration. And so even when lots of lots
of customers make changes at the same time, so
maybe 100 files changed, if the system was always pulling all 100 files or all 1,000 files, if there's 1,000 customers, and just doing that as configuration, there's no change or
difference or dynamism on the right-hand side of these diagrams, which reduces the overall risk and it could be enormously effective. And we've learned to apply this pattern in some really key places. We've got a Builders Library article where we talk about how we apply this in our health check systems
and our DNS failover systems so that they can be incredibly reliable, and I found it really, really useful. And with that, Yasemin's gonna
take over and close us out and tell us our final lesson. - Retries, retries are
somewhat well-known. When there is a failure, we retry and that helps
resolving the problem. But do they always help? Let's dig it out a little bit. The problem with retries is that when they are not used properly, they can cause a larger event compared to what they
are trying to mitigate. We call this Thundering Herd problem. I'll first explain what this problem is and then I'll discuss two
techniques to avoid it. Imagine that a transit failure
is going on in the system. Clients start to retry. As clients retry more, there's more traffic being generated, so the system gets overloaded. And when systems get overloaded, we discussed they start
more load shedding, and there are more failures
and there are more retries. And it's this vicious
cycle that keeps going. Creating more work in
the system with retries doesn't really help to solve the problem. So how do we avoid the
Thundering Herd issue? The first technique I'll discuss is exponential backoff and jitter. When clients retry without
exponential backoff and jitter, the same amount of
traffic hits the service right around the same time
with the same frequency. In this example, there's a
second delay between each retry and the same set of calls are being hit. Calls are used to hit the service. So I have two clients represented here with the shades of colors, and the first client is doing one TPS, second one is doing three, and the third one is doing five TPS, transactions per second. And they're hitting
servers again and again. So this doesn't help to lower
the load on the servers. With exponential backoff
and jitter being used, we apply two techniques. The first one is we give
wait time between each retry and that wait time increases exponentially in between every retries. And the second last
practice of this jitter. We add randomness so that
when the retry comes in, the retries will not come
in right at the same second, but rather it will be
distributed across the timeframe. This technique helps, but we've found it's not always sufficient at scale. Let's look at client throttling. We find client throttling to be a much more effective technique. AWS SDKs has built this part
for client throttling as well. This technique keeps
local state on the client and decides to retry or not
according to the local state that it's keeping track of. The token back algorithm is being used to delivery this property. Let's say we have a
client that's making 1,000 requests per second, it's
the purple line that I have on the graph. And it's static, it's not changing, always making 1,000 requests per second. And the red line on the
graph is the failure rate. Let's imagine that the service
starting to have failure, initially it's healthy and unstressed, having more and more failures
by the middle of the graph there's a 100% failures
going on in the system. And then the failures start
to get better over time. Back to zero. So let's look at the system when there is no client
throttling is used. What happens is the
client starts retrying, as it starts to observe the failures and that excess traffic that's
being created by the clients is following the same
shape as the failure graph that we were just looking at. As there are more failures, there is more work being created, and towards the end of
the middle of the graph, the service is at 100%, let's say. The retry count is the maximum. It's the maximum amount
of traffic being generated and none of that is being served. So retrying, in this case, is not helping to resolve the issue. So let's see how client
throttling helps this problem. So when the client throttling is enabled, as a server starts having
more and more failures, the clients actually recognize it and starts lowering the retry
rate on the client side. And by the time the servers
are having 100% failing in the middle of the graph,
there are no retries going on. It's just a flat number of requests that are still being sent and that failure is saying no retry because it knows that
retrying will not help. But as soon as service starts recovering in the second half of the graph, the retries start to pick up again, because now it knows
that there is a chance a second retry might actually
get a successful response. We've found that this technique
is much more effective to improve availability
posture of client applications while not generating any
unnecessary work on the system. All right, that concludes
our ten points today, and thank you for watching. (upbeat music)

## Subtitles with Timestamps

[00:01](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1s) (upbeat music)

[00:10](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=10s) - Hi, welcome to Beyond five 9s,

[00:14](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=14s) which is all about lessons

[00:16](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=16s) from our highest availability data planes.

[00:18](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=18s) I'm Colm, I'm a VP and
distinguished engineer

[00:20](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=20s) here at Amazon Web Services,

[00:22](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=22s) and we're gonna be joined by Yasemin

[00:23](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=23s) who's a principal engineer
at Amazon Web Services

[00:26](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=26s) who works on Kinesis.

[00:28](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=28s) And today we're gonna
share a bunch of insights

[00:33](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=33s) into how we build our most
highly available systems.

[00:36](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=36s) What's going on under the hood

[00:38](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=38s) or behind the scenes, so to speak.

[00:41](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=41s) We've gone into great detail
about some of these topics

[00:44](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=44s) in our Amazon Builders Library series,

[00:46](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=46s) but today we're gonna cherry pick

[00:49](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=49s) some of the best lessons
and condense them down

[00:53](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=53s) into 10 simple things
hopefully you can take away

[00:56](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=56s) and apply to your own
systems as you build them.

[01:00](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=60s) These lessons come from systems that have

[01:04](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=64s) stood the test of time

[01:06](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=66s) and had very good availability records,

[01:08](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=68s) which is not easy to achieve.

[01:12](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=72s) We've talked about this before

[01:14](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=74s) and some of the lessons are eternal

[01:16](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=76s) and some of the lessons are new.

[01:18](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=78s) But the first one that
we're gonna start with

[01:20](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=80s) is definitely one that's eternal, which is

[01:24](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=84s) it's all about insisting
on high standards.

[01:26](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=86s) Nothing we're gonna go into,
there's no tip or trick

[01:30](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=90s) or magic that we have for you
that can ever replace paying

[01:35](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=95s) very strong attention to
detail in how we build systems.

[01:41](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=101s) There's a few things I'm
always reminded about

[01:44](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=104s) when I think of this.

[01:46](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=106s) One is something I learned
from Werner Vogels,

[01:47](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=107s) our CTO a long time ago,
which is that when you have

[01:52](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=112s) systems that are processing
billions of requests,

[01:54](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=114s) or even trillions of requests over

[01:58](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=118s) short periods of time,

[02:00](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=120s) pretty much anything that
could go wrong in the system

[02:03](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=123s) will be going wrong at some point in time.

[02:06](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=126s) Some request somewhere
is probably experiencing,

[02:10](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=130s) even a one in a billion failure,

[02:11](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=131s) because you have billions of requests.

[02:13](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=133s) And so it requires paying
enormous attention to detail,

[02:17](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=137s) looking for every single error case,

[02:19](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=139s) looking for everything that
could possibly go wrong

[02:22](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=142s) and having a plan for that in the code

[02:24](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=144s) and in testing and everywhere.

[02:26](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=146s) And that kind of culture at team level,

[02:29](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=149s) there's just no substitute for it.

[02:32](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=152s) Having teams who are willing to constantly

[02:35](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=155s) raise the bar on testing,
constantly write new

[02:38](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=158s) and interesting tests or come up with ways

[02:41](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=161s) to make testing itself easier.

[02:44](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=164s) A lot of that is where the
quality and high availability

[02:47](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=167s) in our systems comes from, and like I say,

[02:50](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=170s) there's no substitute for it.

[02:52](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=172s) And I often think that
that kind of quality

[02:56](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=176s) comes about from great habits.

[02:57](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=177s) It's from what we do over
and over and over again,

[03:01](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=181s) and it's really hard to
approach a system and go

[03:04](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=184s) "I'm just gonna add quality to it.

[03:05](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=185s) "I'm just gonna try to make
it better than it was before."

[03:08](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=188s) It's more like something pervasive

[03:10](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=190s) that has to be there from the beginning.

[03:12](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=192s) And so something we've been
paying special attention to

[03:15](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=195s) on this kind of quality
dimension for a long time now

[03:19](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=199s) is deployment safety.

[03:21](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=201s) Where we write our code and
we go through code review,

[03:26](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=206s) collaborative code review and so on

[03:28](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=208s) in back and forth processes,

[03:30](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=210s) like you'd be very familiar with.

[03:32](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=212s) But once we've checked in our code,

[03:34](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=214s) we actually have quite
sophisticated deployment systems

[03:37](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=217s) that take over after that and take charge

[03:40](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=220s) of getting that code from the fact

[03:43](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=223s) that it's been checked in

[03:44](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=224s) all the way to running in production.

[03:46](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=226s) And that system has been designed in a way

[03:49](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=229s) where it generates a
lot of positive safety

[03:52](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=232s) for our systems.

[03:54](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=234s) Whenever we're deploying new code,

[03:56](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=236s) that always means some risk.

[03:58](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=238s) We try to be very paranoid
about our testing,

[04:01](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=241s) we try to be very creative in our testing

[04:03](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=243s) and test it in every possible way,

[04:05](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=245s) and I'll talk more about that later,

[04:07](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=247s) but new code that hasn't been
run in production before,

[04:10](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=250s) there's always some chance
that it might encounter

[04:13](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=253s) some condition that we didn't plan for.

[04:15](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=255s) And so we've got CI/CD
processes that make sure

[04:20](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=260s) that without us having to be too involved,

[04:23](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=263s) that code will go through pretty careful,

[04:26](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=266s) deliberate testing and
deployment as it goes.

[04:30](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=270s) So we'll deploy it to maybe
just one box to start with

[04:35](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=275s) and see how it goes,
there'll be some tests run

[04:38](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=278s) and that box will have to
pass all of those tests

[04:40](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=280s) under every condition.

[04:42](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=282s) And if it doesn't, we've got
fast and reliable rollback,

[04:46](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=286s) that's actually pretty important too.

[04:48](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=288s) But if it does go well, it gets promoted

[04:51](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=291s) and the idea is the
more and more confidence

[04:54](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=294s) we have in that code,
the broader we're willing

[04:59](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=299s) to run that code.

[05:00](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=300s) So as we develop confidence in it

[05:02](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=302s) because it's passing more and more tests,

[05:04](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=304s) we'll promote it from just
one box to one cell maybe,

[05:08](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=308s) or one availability zone, one region,

[05:11](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=311s) multiple regions and so on.

[05:13](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=313s) And this is something we've gone really,

[05:16](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=316s) really deep in our culture.

[05:17](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=317s) Every development team at
AWS knows and understands

[05:20](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=320s) this deployment process pretty intricately

[05:24](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=324s) and knows how to get the most out of it

[05:27](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=327s) and designed our deployments
and code in a way

[05:30](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=330s) where they're gonna extract
the most benefit from them.

[05:33](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=333s) We've seen a lot of return from this.

[05:34](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=334s) It's been

[05:37](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=337s) a great mechanism for us to deliver

[05:41](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=341s) high availability in systems,

[05:43](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=343s) and the occasional issues that it catches

[05:46](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=346s) are well, well worth it.

[05:48](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=348s) So that's our first first thing

[05:51](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=351s) and the first example of
insisting on high standards.

[05:54](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=354s) The next, and certainly we
haven't really talked too much

[05:56](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=356s) about before, is how
we manage our systems,

[06:00](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=360s) So there's this concept out there,

[06:02](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=362s) which really condensed it
down for me and I love,

[06:05](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=365s) about you wanna manage your systems

[06:08](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=368s) more like cattle than pets,

[06:11](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=371s) in that you wanna be able to think of them

[06:13](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=373s) in abstractions and not be managing

[06:17](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=377s) literally one host or
one server at a time,

[06:19](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=379s) because that's not very scalable.

[06:22](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=382s) And actually most systems
at AWS have long been

[06:26](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=386s) beyond the scale that
can be managed by hand.

[06:29](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=389s) Even the systems at AWS
when I joined 13 years ago,

[06:33](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=393s) were already quite far beyond that scale.

[06:37](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=397s) Today we use the same
concepts you'd be familiar

[06:40](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=400s) with to manage systems.

[06:41](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=401s) We have auto scaling
groups, VPCs, subnets,

[06:43](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=403s) security groups, all of these things.

[06:45](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=405s) Internally, we have this
concept called host classes

[06:48](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=408s) that are very similar, and
they just let us manage

[06:52](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=412s) collections of machines without having

[06:55](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=415s) to think about the individual machines.

[06:57](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=417s) And our deployment systems,
they work on top of that.

[07:00](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=420s) They clone these entire abstractions

[07:01](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=421s) between regions, for example.

[07:04](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=424s) But we've actually been
going much, much further.

[07:07](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=427s) So we've learned that
we we have to be able

[07:10](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=430s) to operate our systems in hands-off ways,

[07:13](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=433s) both for safety, operational
safety, and for security.

[07:18](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=438s) And typically AWS operators,
like me as a developer,

[07:24](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=444s) just simply don't have
access to every AWS region.

[07:29](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=449s) And so I could never
really plan on being able

[07:32](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=452s) to log in or access the
system to do something.

[07:34](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=454s) It's just not our
operational model at all.

[07:39](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=459s) And then we have some
systems like AWS Outposts

[07:41](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=461s) and Snowball that are
designed to be disconnected

[07:44](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=464s) for periods of time.

[07:45](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=465s) We may just have no access to them.

[07:47](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=467s) Nobody may have any
access to them for a while

[07:50](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=470s) because of the nature of the product.

[07:52](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=472s) And so we've really had
to double and triple down

[07:55](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=475s) on the the automation that it takes

[07:57](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=477s) to be able to operate in that environment,

[07:58](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=478s) to have systems that are self-healing,

[08:00](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=480s) and that can take care of themselves.

[08:04](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=484s) We have two classes of systems these days.

[08:07](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=487s) We've got Bastion systems where
we have very limited access

[08:12](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=492s) to those systems via what
we call Bastion servers

[08:16](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=496s) or Bastion hosts that let us

[08:20](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=500s) recover systems typically if
there were some urgent need to

[08:24](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=504s) or something like that.

[08:25](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=505s) But with a strong record of the fact

[08:28](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=508s) that folks have had to do something

[08:31](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=511s) with that system and
notification processes

[08:35](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=515s) for that and so on.

[08:36](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=516s) But we also have systems
where increasingly

[08:39](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=519s) that's just not an option.

[08:41](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=521s) There's no general purpose, interactive,

[08:44](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=524s) administrative access,
and even in the event

[08:46](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=526s) of having to recover a system,

[08:49](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=529s) there's simply no general
purpose way to access it.

[08:53](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=533s) And instead we have to
have built in in advance

[08:56](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=536s) all the mechanisms that we would need.

[08:59](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=539s) The AWS Nitro System is a
really strong example of that.

[09:02](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=542s) That's the system that runs
our modern EC2 instance types.

[09:09](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=549s) There's simply no mechanism at all where I

[09:13](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=553s) or someone else could go run a command

[09:15](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=555s) on that system or access it in
some kind of interactive way.

[09:20](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=560s) Instead, everything's done via preplanned,

[09:23](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=563s) pre-secured, fully authenticated
and encrypted APIs,

[09:26](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=566s) and that's the only way
for things to happen.

[09:29](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=569s) And we found great motivation
for this is security,

[09:33](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=573s) but this talk is about availability

[09:35](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=575s) and a great benefit for availability too

[09:37](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=577s) is it just means there's no possibility

[09:39](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=579s) of any on-track changes
and there's no possibility

[09:42](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=582s) of somebody did something to fix something

[09:45](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=585s) and then forgot about it
or anything like that.

[09:47](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=587s) It can't be that kind of system;

[09:49](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=589s) instead, it's much more hermetic.

[09:52](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=592s) So that's our second item.

[09:54](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=594s) I'm gonna hand over to the Yasemin

[09:55](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=595s) who's gonna now tell us about
the third item on our list.

[10:00](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=600s) - Thank you, Colm.

[10:02](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=602s) Well, while we design to
avoid failures altogether,

[10:06](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=606s) we also design with failures in mind.

[10:09](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=609s) This is mainly because we know

[10:12](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=612s) that failures may happen in rare cases

[10:15](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=615s) and we want to make sure
that the blast radius

[10:18](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=618s) of such events are as minimal as possible.

[10:23](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=623s) I will discuss four techniques
that we use for this purpose.

[10:27](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=627s) The first technique we
use is regional isolation.

[10:31](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=631s) AWS Cloud spans 25 geographic
regions around the world,

[10:37](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=637s) and there will be eight more regions

[10:39](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=639s) that are announced to be launching soon.

[10:44](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=644s) Each AWS region region is
isolated from each other,

[10:48](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=648s) both geographically, as well
as on the software stack.

[10:52](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=652s) AWS services offer regional endpoints,

[10:56](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=656s) enabling direct access to that region.

[10:59](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=659s) Using regional isolation, any
rare failure that may come up

[11:04](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=664s) in one region, stays in that region.

[11:07](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=667s) Say for example, we have an
event going on in us-west-1,

[11:12](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=672s) it will be contained within the region

[11:14](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=674s) and will not spread to
any of the other regions.

[11:21](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=681s) The next technique we
use is zonal isolation.

[11:25](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=685s) Each AWS region offers
multiple availability zones

[11:29](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=689s) within its periphery.

[11:31](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=691s) Availability zones are data centers

[11:34](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=694s) that are miles away from each other.

[11:37](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=697s) AWS Cloud has 81 availability zones

[11:40](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=700s) across the world with
24 more launching soon.

[11:45](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=705s) Similar to regions, AZs are
also isolated from each other.

[11:50](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=710s) A failing in one AZ,

[11:52](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=712s) let's say us-west-2a is having an event,

[11:56](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=716s) will not spread to any of the other AZs.

[12:01](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=721s) One example why we leverage this property

[12:04](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=724s) is regional services.

[12:06](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=726s) There'll be multiple availability
zones serving traffic

[12:11](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=731s) rather than to a regional endpoint.

[12:13](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=733s) This way, in the event of
availability zone failures,

[12:17](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=737s) traffic will be redirected
to healthy zones

[12:21](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=741s) behind the region and
customers will not be

[12:26](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=746s) experiencing any degradation.

[12:28](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=748s) So far, we discussed
physical compartmentalization

[12:32](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=752s) of architecture by using AWS
regions and availability zones.

[12:37](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=757s) These two have regional

[12:39](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=759s) and zonal blast radius impact accordingly.

[12:43](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=763s) We apply cellular isolation

[12:45](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=765s) to further reduce the blast
radius impact of events.

[12:49](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=769s) In this technique, we build
dedicated software stacks,

[12:52](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=772s) which we call cells.

[12:54](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=774s) Cells are isolated from each other,

[12:56](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=776s) with their own dedicated endpoints.

[13:00](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=780s) Customers get assigned
to one of these cells.

[13:03](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=783s) Imagine there are eight
customers and four cells.

[13:06](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=786s) We have two customers
assigned to each of them.

[13:09](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=789s) Since cells are isolated from each other,

[13:12](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=792s) failure in one cell, let's say
cell two is having an event,

[13:16](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=796s) will not spread to any of the other cells.

[13:18](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=798s) That means it's only the
customers assigned to that cell,

[13:21](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=801s) the palm tree and stars in this case,

[13:24](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=804s) will be impacted, but no other
customers will be impacted.

[13:29](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=809s) This is pretty good.

[13:30](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=810s) It's much better than a zonal
and regional blast radius

[13:35](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=815s) that we discussed before,
but can we do better?

[13:39](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=819s) We do better by using shuffle sharding.

[13:43](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=823s) In shuffle sharding, we divide the service

[13:45](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=825s) into smaller compartments,

[13:47](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=827s) which I will call partitions;
in this case, the blue boxes.

[13:52](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=832s) And we assign customers to
partitions, not one-to-one,

[13:56](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=836s) but we assign multiple
partitions to a single customer.

[14:01](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=841s) In this case, I have two partitions

[14:04](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=844s) assigned to each customer.

[14:06](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=846s) So let's evaluate the blast radius impact

[14:09](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=849s) of failures in this case.

[14:11](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=851s) Let's say partition
one is having an event.

[14:15](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=855s) In that case, both palm tree and stars

[14:18](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=858s) have another partition that's healthy.

[14:21](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=861s) Therefore they will not see impact

[14:24](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=864s) and they will continue
to operate just fine.

[14:29](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=869s) It's only the time when both partitions

[14:32](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=872s) of a single a customer having an event

[14:35](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=875s) that that customer will see the impact.

[14:38](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=878s) And in this case, when
partition four is also out,

[14:42](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=882s) it's the stars that will see the impact

[14:44](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=884s) because those two are
shared partition for stars,

[14:48](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=888s) but palm tree and hiker
will not observe any impact.

[14:54](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=894s) So there are two benefits that
I'd like to highlight here.

[14:58](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=898s) The very first one is
creating customer impact

[15:02](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=902s) is much harder with shuffle sharding.

[15:04](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=904s) This is mainly because it
takes multiple partitions

[15:08](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=908s) to have a failure to create an impact

[15:11](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=911s) and the probability of having a failure

[15:14](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=914s) across multiple partitions is much lower

[15:18](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=918s) than the probability
also of having a failure

[15:20](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=920s) on a single partition.

[15:23](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=923s) The second benefit is
that even in the event

[15:26](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=926s) of those very, very
rare probability events

[15:30](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=930s) that are happening across partitions,

[15:32](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=932s) the impact created to the
customer is much lower.

[15:37](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=937s) We have one customer being impacted

[15:39](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=939s) in the case of two partition failures,

[15:42](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=942s) compared to impacting multiple customers

[15:45](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=945s) than the regular sharding
scheme would actually create.

[15:48](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=948s) Next I'll discuss circuit breakers.

[15:51](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=951s) Circuit breakers is
one of those techniques

[15:54](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=954s) we use to eliminate failures,

[15:56](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=956s) and I will discuss two examples.

[15:59](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=959s) The first one is load shedding.

[16:01](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=961s) We know systems can slow down

[16:04](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=964s) or sometimes even fall
over on the access log.

[16:08](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=968s) We design to make sure

[16:09](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=969s) that our services are not
vulnerable to this problem.

[16:13](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=973s) To address this issue,

[16:15](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=975s) we first identify the maximum capacity

[16:18](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=978s) of every individual component.

[16:21](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=981s) We use stress testing
to get this information,

[16:25](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=985s) then we install the load shedders locally

[16:27](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=987s) within the services to monitor
the traffic being served.

[16:31](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=991s) Once it starts receiving traffic

[16:34](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=994s) more than its predefined
maximum capacity limit,

[16:37](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=997s) the load shedders start
rejecting any excess load.

[16:42](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1002s) They are designed to reject
the load very quickly

[16:45](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1005s) without spanning much off
the system's resources.

[16:48](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1008s) This way we ensure that systems continue

[16:51](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1011s) to operate successfully under excess load.

[16:57](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1017s) The other circuit breaker

[16:58](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1018s) that I'll discuss is bullet counters.

[17:01](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1021s) This pattern gets used frequently

[17:04](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1024s) on external monitoring applications,

[17:06](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1026s) like health guardians in this case.

[17:09](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1029s) These applications are common across AWS

[17:12](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1032s) because we want to make sure
that we are the first ones

[17:16](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1036s) to detect any problem that may be ongoing

[17:19](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1039s) and mitigate it right away

[17:21](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1041s) before customers are even noticing it.

[17:25](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1045s) For example, these applications then pair

[17:28](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1048s) the health checks to each
and every node of the system

[17:31](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1051s) to ensure that they are all healthy.

[17:34](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1054s) If there's a bad node being detected,

[17:37](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1057s) they would replace the node.

[17:39](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1059s) While it sounds straightforward,

[17:42](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1062s) the part that's interesting
about these systems

[17:45](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1065s) is that they are very, very powerful.

[17:48](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1068s) Replacing a node is that powerful action.

[17:52](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1072s) Imagine a health guardian determined

[17:54](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1074s) that half of the fleet is unhealthy.

[17:58](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1078s) Should it go head and just
replace all those nodes?

[18:02](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1082s) Maybe, but usually not.

[18:04](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1084s) It really depends on what the problem is.

[18:08](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1088s) We built to not have such
large failures anyways.

[18:13](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1093s) So to avoid these automations

[18:17](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1097s) to take significant actions that will lead

[18:22](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1102s) to significant changes,

[18:25](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1105s) we installed both counters in place

[18:29](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1109s) so that they don't act on
positive signals incorrectly.

[18:34](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1114s) So bullets counter in this example

[18:36](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1116s) would be the one that we say
what's the maximum percentage

[18:41](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1121s) of the fleet that could be
replaced safely at a given time?

[18:47](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1127s) The bullet counters
monitor the actions taken

[18:51](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1131s) by the health guardian

[18:53](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1133s) and whenever there is an
event where there are nodes

[18:57](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1137s) that are being determined as more

[18:59](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1139s) than the predefined maximum limit,

[19:02](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1142s) they will stop the execution and instead,

[19:06](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1146s) they will notify the operators to show up

[19:09](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1149s) and assess the situation.

[19:13](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1153s) Using bullet counters, we
ensure that automation always

[19:16](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1156s) operate within known and safe limits.

[19:23](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1163s) With that, I will hand it over to Colm.

[19:26](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1166s) - Thanks, Yasemin.

[19:29](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1169s) So, as I mentioned briefly earlier,

[19:31](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1171s) testing is of enormous importance

[19:34](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1174s) and we invest a lot in testing.

[19:37](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1177s) In fact, for our most
highly available systems,

[19:41](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1181s) it's not unusual to spend
much more time on testing code

[19:47](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1187s) than writing the code itself.

[19:52](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1192s) We have unit tests, we've
got end-to-end tests,

[19:55](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1195s) we've got integration tests

[19:57](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1197s) and we've even got formal verification.

[20:02](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1202s) We've got pre-production environments.

[20:05](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1205s) Even these days we'll
test how a system copes

[20:10](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1210s) with rolling forward through
a deployment process,

[20:13](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1213s) as well as rolling back
through the deployment process

[20:15](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1215s) before we ever really
deploy to production,

[20:18](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1218s) just to make sure that if
we had to do those things,

[20:21](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1221s) we would be able to.

[20:24](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1224s) If you wanna see examples

[20:26](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1226s) of how we raised the bar on testing,

[20:30](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1230s) you can look at our open
source projects on GitHub.

[20:32](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1232s) So our s2n project which
is our open source SSL

[20:37](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1237s) and TLS library is developed
by a team in Amazon

[20:41](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1241s) who work just like any
other team in Amazon.

[20:44](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1244s) And it's a really simple,
open view into how we work.

[20:50](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1250s) And you can see just the
sheer staggering number

[20:52](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1252s) of tests that are there that are running

[20:55](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1255s) on every single build.

[20:57](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1257s) We don't just run those
tests before we deploy,

[21:01](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1261s) they're integrated into our CI/CD process

[21:05](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1265s) and every time we check
in, we run them all

[21:08](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1268s) and we make sure that they all pass

[21:10](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1270s) before promoting, just to make sure

[21:13](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1273s) that there are no regressions.

[21:14](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1274s) And that's very, very typical

[21:16](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1276s) for these high availability systems.

[21:19](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1279s) But we've been going further.

[21:22](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1282s) And so in the last few years,

[21:24](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1284s) we've actually been
going further and further

[21:26](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1286s) with automated reasoning
and formal verification.

[21:30](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1290s) So this is something we've
been doing for a long time.

[21:33](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1293s) On the s2n project, we've
been formally verifying

[21:36](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1296s) the correctness of parts of
s2n for about six years now,

[21:42](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1302s) but in the last few years, we've been able

[21:45](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1305s) to get to the point where now

[21:50](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1310s) I'm gonna say regular developers

[21:52](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1312s) who don't have specialized
training in automated reasoning

[21:55](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1315s) or formal verification are
able to use these techniques

[21:58](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1318s) because we've improved the tooling.

[22:00](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1320s) It's getting easier and easier.

[22:03](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1323s) And this is amazing because
formal verification tests

[22:06](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1326s) can always prove that code is correct

[22:09](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1329s) for a particular input,

[22:10](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1330s) but formal verification can prove that

[22:11](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1331s) that code is correct for
any particular input.

[22:14](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1334s) So it's very, very powerful.

[22:16](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1336s) It can find really hard-to-find edge cases

[22:20](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1340s) that you won't find using
any other technique.

[22:22](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1342s) And it's pretty awesome
now that we're able

[22:24](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1344s) to get to the point where

[22:28](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1348s) regular software developers like me

[22:30](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1350s) can actually use these tools

[22:32](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1352s) and improve things about their code.

[22:35](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1355s) And if you're interested in some of that,

[22:36](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1356s) I'd encourage you to check out CBMC,

[22:39](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1359s) which is a tool we've been using on s2n

[22:41](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1361s) that is very intuitive

[22:44](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1364s) and I found very easy
to use for developers.

[22:48](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1368s) So the next item on our list is something

[22:52](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1372s) called lifecycle management,

[22:54](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1374s) which we've found that
to get high availability

[22:59](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1379s) over long periods of time in our systems,

[23:02](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1382s) we need be very, very
intentional about how we manage

[23:05](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1385s) the life cycle of a lot of
aspects of those systems.

[23:10](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1390s) And in particular, any kind of credentials

[23:14](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1394s) that are used by those systems,

[23:15](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1395s) so that's things like keys
and certificates and so on.

[23:18](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1398s) So modern security and
compliance frameworks demand

[23:21](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1401s) that credentials be frequently rotated,

[23:23](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1403s) and that makes sense.

[23:24](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1404s) No-one wants a key or a certificate around

[23:27](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1407s) that could be used for
very long periods of time,

[23:30](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1410s) but at the same time expired
and mismatched credentials

[23:33](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1413s) could be a source of outages.

[23:35](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1415s) If a certificate or key expires

[23:37](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1417s) and it's still in your system,
that's not gonna be good.

[23:40](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1420s) So we've learned to decouple
that expiry from alarming.

[23:43](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1423s) So we alarm well before the expiry time

[23:47](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1427s) of any key or credential.

[23:49](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1429s) And we've learned to be super intentional

[23:52](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1432s) and go into overkill on how to monitor it.

[23:56](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1436s) So we've got time to expiry metrics

[23:58](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1438s) for anything that expires.

[24:00](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1440s) We look at that from both
the server side perspective,

[24:03](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1443s) so the thing that might
be serving a certificate

[24:05](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1445s) or using a key, and the client side,

[24:08](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1448s) the thing that's connecting to it.

[24:10](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1450s) Like I said, we alarm and investigate

[24:11](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1451s) well before there's any kind of a problem.

[24:14](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1454s) And then on top of that, we've
got additional fail-safes

[24:18](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1458s) and canaries that are constantly scanning

[24:20](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1460s) for anything that looks
like it's even close

[24:22](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1462s) to expiry so that we've got
another safety net there too.

[24:26](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1466s) And then with all of
those systems combined,

[24:28](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1468s) we've learned that that means we need

[24:30](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1470s) to deploy any new key or credential,

[24:33](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1473s) make sure it's absolutely everywhere

[24:35](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1475s) that could need it before we activate it,

[24:37](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1477s) and only then activate
it and kinda do the same

[24:39](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1479s) in reverse whenever we're deactivating

[24:42](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1482s) or revoking a key or certificate.

[24:44](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1484s) And we found that paying
particular attention

[24:47](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1487s) to detail in those processes
has been really key

[24:49](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1489s) to avoiding just any kind
of outage you could see

[24:53](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1493s) from just expired or mismatched
keys and credentials.

[24:58](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1498s) And so with that, I'll
hand over to Yasemin

[25:01](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1501s) who's gonna tell us about
modular separations.

[25:04](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1504s) - Thank you, Colm.

[25:06](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1506s) Modular separation.

[25:09](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1509s) We avoid multiple architectures

[25:11](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1511s) and decoupling individually
responsibilities

[25:13](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1513s) into their own dedicated components.

[25:18](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1518s) Control plane versus data plane separation

[25:20](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1520s) is a good example of this.

[25:22](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1522s) Most AWS services have this
notion of control plane

[25:27](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1527s) and data plane APIs.

[25:29](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1529s) Let's take Kinesis data
streams as an example.

[25:32](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1532s) Kinesis data streams is a
real-time streaming service

[25:36](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1536s) that enables customers to write records

[25:38](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1538s) into a log stream and read them later on.

[25:43](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1543s) The very first thing customers do

[25:45](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1545s) when they start using the service,

[25:48](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1548s) they go ahead and create a stream.

[25:50](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1550s) Create stream is a control plane API.

[25:53](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1553s) Once the stream is created,

[25:55](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1555s) producer applications can start ingesting

[25:58](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1558s) the data continuously
and consumer applications

[26:01](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1561s) read those records within milliseconds.

[26:04](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1564s) The APIs used by the producer

[26:06](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1566s) and consumer applications
are the data plane APIs.

[26:11](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1571s) As we see in this example,

[26:13](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1573s) access patterns of these two
types of APIs are different.

[26:21](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1581s) Consequently, their dependencies
are very different as well.

[26:25](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1585s) For example, control
plane APIs are depending

[26:29](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1589s) on the asynchronous workflows

[26:31](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1591s) to execute the steps of creating a stream,

[26:36](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1596s) versus data plane APIs are
dependent on the data store

[26:41](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1601s) to fetch the records within milliseconds.

[26:44](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1604s) By decoupling the two API types,

[26:47](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1607s) we limit the impact their
dependencies could be creating.

[26:52](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1612s) For example, if there's
an event that's going on

[26:55](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1615s) on the async workflows,
then it's going to be

[26:58](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1618s) only the control plane APIs
that are being impacted

[27:01](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1621s) while the data place
APIs continue to work.

[27:08](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1628s) The next technique is static stability,

[27:11](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1631s) and this technique works hand-to-hand

[27:13](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1633s) with modular separation.

[27:16](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1636s) Availability of a system can be as good

[27:20](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1640s) as the availability of its dependencies.

[27:23](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1643s) For this reason, we strive
to keep the dependencies

[27:26](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1646s) of systems to an absolute minimum.

[27:31](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1651s) Let's get back to control plane

[27:33](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1653s) versus data plane discussion again.

[27:36](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1656s) The dependency here that I didn't discuss

[27:38](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1658s) before is the metadata store.

[27:41](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1661s) Metadata store is the one
that parses information

[27:45](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1665s) about resources, Kinesis
streams in this case.

[27:49](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1669s) So stream creation execution
has direct dependency

[27:53](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1673s) to the availability of metadata store

[27:55](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1675s) because it needs to parse the information

[27:57](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1677s) that the stream is creating.

[27:59](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1679s) Imagine there's an
outage on metadata store.

[28:03](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1683s) We expect the async
workflows to be impacted

[28:05](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1685s) because it cannot access
the data story anymore

[28:08](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1688s) therefore, the control
plane APS are impacted.

[28:11](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1691s) Let's check the impact of
metadata store on data plan APIs.

[28:16](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1696s) Well, data plane APIs also need to know

[28:20](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1700s) about these streams and
where they are located

[28:23](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1703s) so that they can serve,
put and get APIs on them.

[28:27](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1707s) So if the data plane APIs have direct

[28:30](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1710s) and synchronous dependency
on metadata store,

[28:33](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1713s) then its outage will also
impact the data plane APIs.

[28:38](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1718s) Well, that's not great.

[28:39](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1719s) It's a large blast radius impact.

[28:43](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1723s) So the sole dependency of data
plane API is really the data

[28:47](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1727s) store that are responsible
for serving customer records.

[28:51](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1731s) So considering the static
stability principle,

[28:55](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1735s) let's look at this design

[28:57](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1737s) and see how we can eliminate
the metadata store dependency

[29:02](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1742s) from data plan APIs.

[29:04](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1744s) We eliminate this dependency by moving

[29:08](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1748s) the metadata store
dependency of data plane

[29:12](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1752s) from being a synchronous dependency

[29:14](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1754s) to be an asynchronous dependency.

[29:17](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1757s) In this architecture, the
metadata store keeps track

[29:23](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1763s) of the streamer and information.

[29:25](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1765s) And here it has a copy of
this information stored

[29:31](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1771s) within the data plane itself.

[29:36](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1776s) Any updates that are being
applied to this metadata

[29:40](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1780s) gets propagated the data plane

[29:41](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1781s) and its own snapshot asynchronously.

[29:46](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1786s) In this case, if there's an
outage in the metadata store,

[29:49](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1789s) it's the control place
APIs that will be impacted,

[29:53](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1793s) but the data plane APIs
will continue to work

[29:56](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1796s) by using the smaller
version of their snapshots

[30:00](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1800s) they stored within themselves.

[30:04](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1804s) This way we ensure that the
data plane is statically stable

[30:08](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1808s) by using its absolute
minimum set of dependencies.

[30:13](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1813s) - Thanks, Yasemin.

[30:16](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1816s) So our ninth and penultimate
item is constant work, which is

[30:23](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1823s) whenever we were learning big O notation,

[30:25](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1825s) if you studied computer science,

[30:26](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1826s) you probably learnt about
systems that are constant work.

[30:29](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1829s) That means O1 right at big O notation

[30:33](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1833s) and that turns out to be
a very important concept

[30:35](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1835s) for some of our highly available systems.

[30:40](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1840s) In general, risk is proportionate to rates

[30:43](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1843s) of change in systems.

[30:46](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1846s) A spike in load, for example,

[30:48](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1848s) can cause the system to slow down,

[30:50](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1850s) and then the system gets into a mode

[30:52](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1852s) that it's not used to operating in,

[30:54](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1854s) things don't really
know how to handle that,

[30:56](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1856s) they might start timing out and so on.

[30:59](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1859s) And issues like that can
cause cascading failures.

[31:03](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1863s) And so we've learned that
reducing the overall dynamism

[31:06](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1866s) in a system, the amount of
change it can even go through

[31:10](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1870s) is a useful way to make them simpler

[31:12](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1872s) and to reduce all that risk.

[31:14](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1874s) And a counter-intuitive solution

[31:16](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1876s) to wrangle that risk is
actually to run the system

[31:19](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1879s) at maximum load all the time.

[31:20](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1880s) And even though that sounds like,

[31:22](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1882s) well, now the system is gonna
be maxed out all the time,

[31:24](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1884s) it actually reduces the amount of dynamism

[31:27](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1887s) and change that's in the
system, and therefore risk.

[31:30](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1890s) A really simple example
of that is how we apply

[31:33](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1893s) this constant work pattern to,
say, configuration changes.

[31:38](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1898s) So really common pattern in how developers

[31:41](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1901s) manage configuration changes
is a customer makes a change,

[31:45](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1905s) that change gets ingested into the system,

[31:47](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1907s) it's like a delta.

[31:49](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1909s) Do this thing, do X, do Y.

[31:51](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1911s) And that goes into our workflow

[31:53](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1913s) and the workflow manager
is getting that change out

[31:55](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1915s) to all of the systems that
need to reflect that change.

[31:58](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1918s) That works, that's a simple pattern,

[32:01](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1921s) but the problem is when
lots of changes happen

[32:03](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1923s) from lots of customers at the same time,

[32:05](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1925s) maybe it's a particularly
busy day or whatever,

[32:07](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1927s) the overall system slows down,

[32:09](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1929s) because the workflow
has got more work to do.

[32:13](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1933s) And as I said, it could hit
you in ways that cascade.

[32:18](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1938s) So a simpler version of this
is imagine every customer,

[32:21](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1941s) they make their change and
it's just reflected as,

[32:24](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1944s) say, a file or key in S3.

[32:27](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1947s) That's it, they just make their change

[32:30](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1950s) and it's effectively
a file or a key in S3.

[32:33](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1953s) And the system on the other side,

[32:35](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1955s) instead of using a workflow,

[32:36](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1956s) all it's doing is checking
all of those files

[32:39](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1959s) every single time, just
downloading every single file

[32:42](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1962s) from S3 and using that
as its configuration.

[32:45](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1965s) And so even when lots of lots
of customers make changes

[32:48](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1968s) at the same time, so
maybe 100 files changed,

[32:51](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1971s) if the system was always pulling

[32:53](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1973s) all 100 files or all 1,000 files,

[32:56](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1976s) if there's 1,000 customers,

[32:57](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1977s) and just doing that as configuration,

[32:59](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1979s) there's no change or
difference or dynamism

[33:03](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1983s) on the right-hand side of these diagrams,

[33:05](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1985s) which reduces the overall risk

[33:07](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1987s) and it could be enormously effective.

[33:09](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1989s) And we've learned to apply this pattern

[33:11](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1991s) in some really key places.

[33:13](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1993s) We've got a Builders Library article

[33:14](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1994s) where we talk about how we apply this

[33:16](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=1996s) in our health check systems
and our DNS failover systems

[33:20](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2000s) so that they can be incredibly reliable,

[33:23](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2003s) and I found it really, really useful.

[33:25](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2005s) And with that, Yasemin's gonna
take over and close us out

[33:29](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2009s) and tell us our final lesson.

[33:33](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2013s) - Retries, retries are
somewhat well-known.

[33:36](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2016s) When there is a failure,

[33:39](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2019s) we retry and that helps
resolving the problem.

[33:42](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2022s) But do they always help?

[33:45](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2025s) Let's dig it out a little bit.

[33:47](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2027s) The problem with retries is that

[33:49](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2029s) when they are not used properly,

[33:51](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2031s) they can cause a larger event

[33:54](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2034s) compared to what they
are trying to mitigate.

[33:57](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2037s) We call this Thundering Herd problem.

[33:59](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2039s) I'll first explain what this problem is

[34:01](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2041s) and then I'll discuss two
techniques to avoid it.

[34:06](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2046s) Imagine that a transit failure
is going on in the system.

[34:11](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2051s) Clients start to retry.

[34:13](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2053s) As clients retry more,

[34:15](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2055s) there's more traffic being generated,

[34:17](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2057s) so the system gets overloaded.

[34:19](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2059s) And when systems get overloaded,

[34:20](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2060s) we discussed they start
more load shedding,

[34:23](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2063s) and there are more failures
and there are more retries.

[34:26](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2066s) And it's this vicious
cycle that keeps going.

[34:31](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2071s) Creating more work in
the system with retries

[34:34](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2074s) doesn't really help to solve the problem.

[34:36](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2076s) So how do we avoid the
Thundering Herd issue?

[34:40](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2080s) The first technique I'll discuss

[34:42](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2082s) is exponential backoff and jitter.

[34:45](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2085s) When clients retry without
exponential backoff and jitter,

[34:49](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2089s) the same amount of
traffic hits the service

[34:53](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2093s) right around the same time
with the same frequency.

[34:57](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2097s) In this example, there's a
second delay between each retry

[35:02](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2102s) and the same set of calls are being hit.

[35:07](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2107s) Calls are used to hit the service.

[35:10](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2110s) So I have two clients represented here

[35:13](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2113s) with the shades of colors,

[35:15](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2115s) and the first client is doing one TPS,

[35:17](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2117s) second one is doing three,

[35:18](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2118s) and the third one is doing five TPS,

[35:21](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2121s) transactions per second.

[35:23](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2123s) And they're hitting
servers again and again.

[35:28](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2128s) So this doesn't help to lower
the load on the servers.

[35:34](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2134s) With exponential backoff
and jitter being used,

[35:37](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2137s) we apply two techniques.

[35:39](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2139s) The first one is we give
wait time between each retry

[35:46](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2146s) and that wait time increases exponentially

[35:49](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2149s) in between every retries.

[35:51](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2151s) And the second last
practice of this jitter.

[35:54](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2154s) We add randomness so that
when the retry comes in,

[36:00](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2160s) the retries will not come
in right at the same second,

[36:04](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2164s) but rather it will be
distributed across the timeframe.

[36:09](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2169s) This technique helps, but we've found

[36:12](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2172s) it's not always sufficient at scale.

[36:18](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2178s) Let's look at client throttling.

[36:20](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2180s) We find client throttling

[36:20](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2180s) to be a much more effective technique.

[36:24](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2184s) AWS SDKs has built this part
for client throttling as well.

[36:29](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2189s) This technique keeps
local state on the client

[36:32](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2192s) and decides to retry or not
according to the local state

[36:37](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2197s) that it's keeping track of.

[36:39](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2199s) The token back algorithm is being used

[36:41](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2201s) to delivery this property.

[36:43](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2203s) Let's say we have a
client that's making 1,000

[36:46](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2206s) requests per second, it's
the purple line that I have

[36:49](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2209s) on the graph.

[36:51](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2211s) And it's static, it's not changing,

[36:52](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2212s) always making 1,000 requests per second.

[36:55](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2215s) And the red line on the
graph is the failure rate.

[36:59](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2219s) Let's imagine that the service
starting to have failure,

[37:03](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2223s) initially it's healthy and unstressed,

[37:06](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2226s) having more and more failures
by the middle of the graph

[37:09](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2229s) there's a 100% failures
going on in the system.

[37:12](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2232s) And then the failures start
to get better over time.

[37:15](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2235s) Back to zero.

[37:17](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2237s) So let's look at the system

[37:19](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2239s) when there is no client
throttling is used.

[37:22](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2242s) What happens is the
client starts retrying,

[37:27](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2247s) as it starts to observe the failures

[37:30](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2250s) and that excess traffic that's
being created by the clients

[37:34](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2254s) is following the same
shape as the failure graph

[37:39](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2259s) that we were just looking at.

[37:41](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2261s) As there are more failures,

[37:43](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2263s) there is more work being created,

[37:45](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2265s) and towards the end of
the middle of the graph,

[37:47](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2267s) the service is at 100%, let's say.

[37:55](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2275s) The retry count is the maximum.

[37:56](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2276s) It's the maximum amount
of traffic being generated

[37:59](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2279s) and none of that is being served.

[38:02](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2282s) So retrying, in this case, is not helping

[38:06](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2286s) to resolve the issue.

[38:08](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2288s) So let's see how client
throttling helps this problem.

[38:14](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2294s) So when the client throttling is enabled,

[38:18](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2298s) as a server starts having
more and more failures,

[38:21](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2301s) the clients actually recognize it

[38:24](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2304s) and starts lowering the retry
rate on the client side.

[38:28](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2308s) And by the time the servers
are having 100% failing

[38:31](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2311s) in the middle of the graph,
there are no retries going on.

[38:34](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2314s) It's just a flat number of requests

[38:36](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2316s) that are still being sent

[38:38](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2318s) and that failure is saying no retry

[38:40](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2320s) because it knows that
retrying will not help.

[38:43](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2323s) But as soon as service starts recovering

[38:46](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2326s) in the second half of the graph,

[38:47](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2327s) the retries start to pick up again,

[38:51](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2331s) because now it knows
that there is a chance

[38:53](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2333s) a second retry might actually
get a successful response.

[38:58](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2338s) We've found that this technique
is much more effective

[39:00](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2340s) to improve availability
posture of client applications

[39:04](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2344s) while not generating any
unnecessary work on the system.

[39:08](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2348s) All right, that concludes
our ten points today,

[39:12](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2352s) and thank you for watching.

[39:15](https://www.youtube.com/watch?v=GTLfM8ofmwE&t=2355s) (upbeat music)

