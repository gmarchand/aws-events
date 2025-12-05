# AWS re:Invent 2024 - Observability strategies for Amazon EKS workloads (KUB323)

[Video Link](https://www.youtube.com/watch?v=Icz8MBHCPuQ)

## Description

Containerized applications deployed on Amazon EKS present unique observability challenges. This lightning talk explores effective strategies to gain visibility into your Amazon EKS workloads. See a complete observability strategy with AWS services like Amazon CloudWatch Container Insights, application signals, and Amazon CloudWatch Logs Insights. See how these services can be used to track down and quickly gain insights into your Amazon EKS workloads. Leave this talk with a toolkit to proactively monitor the health and performance of your Amazon EKS–hosted applications. This talk equips you with the observability foundation needed to ensure reliability and quick issue resolution in your Kubernetes environment.

Learn more:
AWS re:Invent: https://go.aws/reinvent.
More AWS events: https://go.aws/3kss9CP 

Subscribe:
More AWS videos: http://bit.ly/2O3zS75
More AWS events videos: http://bit.ly/316g9t4

About AWS:
Amazon Web Services (AWS) hosts events, both online and in-person, bringing the cloud computing community together to connect, collaborate, and learn from AWS experts. AWS is the world's most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally. Millions of customers—including the fastest-growing startups, largest enterprises, and leading government agencies—are using AWS to lower costs, become more agile, and innovate faster.

#AWSreInvent  #AWSreInvent2024

## Transcript

- Observability strategies with EKS. We're gonna start in a little more broad with a bit of basic
foundational information on observability as a whole, and then we'll focus in on
some of the things you can do and approaches for
getting insights into EKS and get understanding your clusters. Really basic level set. Why
are we doing observability? What's the point here? We're trying to detect,
investigate things. We're trying to make sure
that we can figure out how to remediate our clusters or anything that's happening there. We're also really trying
to get deeper insights into the clusters and understand, okay, how can I improve the performance? How can I make this something where I'm really having a
better solution over time? Or I'm fixing something that is occurring in the moment, right? And the way that we get at that is we have kind of these three pillars that are pretty strong
that you'll need to have. You need to have your logs, you need to have your metrics,
you need to have your traces. Each of these are kind
of foundational things for you to get at to get that information. So then it becomes, how
do I get this information? What am I using it for? And what is my main way
of getting at it in a way that is truly accessible for my team or for the people that are
working on these clusters, right? So we get in there, we want
to collect that information, we want to know what we're doing with it, but there's some barriers to
making this happen, right? So onboarding can be a barrier. Right off I'm saying, "Hey, I
wanna gather this information, but what way do I gather?" Is it an OTel approach
to doing these things? Is it something that's
maybe cloud-specific to the vendor that I'm using? What do I do to gather this information and how do I get it into my solutions? Like how can I make that simpler? 'Cause there are multiple
approaches for doing this. Which one's the right
approach for me and my people? What metrics to collect?
I can collect everything. Do I need everything? Probably not. Probably
you don't need everything. Let's look at your clusters,
see what it's doing, and pick and choose which metrics are of the most value to you, or follow an opinionated approach that gives you some
guidance on, as an industry, we've said this is the best way to collect some of these metrics, right? And then analyze that impact, right? Understand like, okay,
I've got the metrics, I've got the logs, the traces are telling
me some information. Kind of so what? What does it mean? What does connecting
them actually, you know, how do I take that data and
turn it into information? How do I make it something
where I can look at it and say, "Okay, this is value
that I'm getting out of this." Not just, "Okay, there's an error here." Like, is it an important error? Is it actually causing problems? Is it more like something's going wrong, but I'm recovering nicely from it? Understand these things. And then what is the
right opinionated approach to make this occur? Can I just take, you know,
somebody else's perspective or does my company need to have
its own approach to do this? This tends to take some thought, and so some effort to go after it. And if I have a decision, you know, can I change it over time? Is this something where
I can evaluate this and move it along? And with a lot of our
solutions, you can do that, in fact, that's one of
the things that's nicer, is I can choose to start with one solution and then go over and say, you know what? I really need move over to this
other approach to doing it. And then finally, cost. Observability is great, but it can't cost more than
your application, right? Like we've gotta have a balance there on how much we're paying
to get that insight and understand what we're getting. So in AWS we like to
give you options, right? So there's several ways you
can kind of approach this. This is a kind of an overview
of our tool set that's there. I wanna point out kind of
three overall approaches that we have to do it. One, you can go with like a
managed open source approach. This is gonna be more like your Prometheus Grafana type services, things like that where you're saying, look, these are open source solutions, they're available to us, they're
things that we can leverage and we know we can use
that in multiple locations. Sometimes that's the right
approach to make that happen. You should really have a
strong tool set in that space. Another type option might be down there where you see our Amazon
OpenSearch service. And that's another place
where I can pump all my logs, I can pump my metrics,
I can pump my traces, and I can get insights from that service. And that could be a strong approach for doing your observability, actually getting those
insights into one window where I can go ahead and check it out and make sure that I understand this is how my teams are gonna solve this. And then the last approach
is our cloud native services, which is a number of the ones up there, but they focus around CloudWatch and the tools that we've built into that. That's gonna be things like our, you know, container insights, our
logs, all these things. I'm gonna focus on that last
one 'cause it's 15 minute talk, I can't deep dive on each of them, but there's good use cases for all those approaches
and those solutions. If you wanna talk more about
that, just to catch me after, we can dive into that. All right, so one of the first
problems I brought up was, okay, how do I collect the metrics, right? Do I use ADOT, do I go ahead and say, you know, I'm gonna do, you know, these various open, you
know, telemetry approaches to gathering my metrics. One of the things we've done is we've done a big improvement
with the CloudWatch agent. In the CloudWatch agent,
essentially now you can use that and you will have fewer things
that you need to get deployed instead of have to have your X-Ray daemon, your OTel collector, or some kind of tracing
daemon in your OTel collector. You can just do it all
with a CloudWatch agent. You can deploy that, you just
have that one side car running and that's gonna be able
to take care of all that for your logs, your
metrics, and your traces. It kind of enables all of that now. So that's been a big improvement. It is backwards-compatible and it does work with
OpenTelemetry, right? Which is a big deal. You can then take it, your code is pushing out
OpenTelemetry metrics, that is able to be gathered
by your CloudWatch agent. If you change your mind and you wanna do something
that's more open source, you can still do that, right? So it's not locking you into it, but it is pretty powerful for making it so that you can rapidly at
least gather the metrics and gather the traces and
stuff, things like that, and your logs, basically all of them. So let's look at these a little bit. So CloudWatch Logs has a number of tools, we have like anomalies, we have a lot of ways
to get the information. Today, I just wanna highlight insights. It's a great way for you to
basically be able to say, you know what, I've got my logs, and I'll do a demo in a little bit, I've got my logs and I wanna understand what's the pattern with these logs, what's going on with them? Can I filter them, search them? Can I do basically deep analysis
and understand, you know, is there a repeating pattern
over time with my system so I can actually get
to the root of things? And CloudWatch Insights really kind of highlights that space. And it, you know,
integrates, you know, deeply with several of our services. I think the main thing that I
find really powerful about it is there's not just the logs here, but when I show the demo, it also shows when the logs are happening, as you can see visually, like
a set of spikes and dips, and then you can also just
dig into the actual content that's coming out of those logs, which can be really powerful. Like, hey, everything
looked like it was fine, we published something new and now I've got a whole
bunch of logs coming out. I'm like, "Ah, okay, that's
not normal, you know, let's go look at that spiked area," and I'll show that in a little bit. The next service that I wanna
highlight a little bit of is our Container Insights. I know we're focused on EKS here, but we have enhanced Container Insights, that's been a big deal for
EKS for a little while, we now offer it in ECS, that's
a newer release for that. But what's really interesting here that I wanna make sure
y'all get a good sense of is you can kind of slice and dice it. You start off looking at
the whole cluster, great. You can use that to dig down and say, "Hey, the problem tends to be the service. I've got the service and it's what's causing
the most issues," right? And then from there, you
know, maybe I look down and see which pod that's
associated with that service is the one that's, you
know, I need to dig into. And do I have any alarms or
any messaging around that to make it more obvious
to me how I get at it. This tool, which we'll show a little bit, is a key part of figuring that out. And at a different kind of level, whereas I like Container Insights, It does a good job of giving
you a sense of the components. Hey, these are my pods
that are having issues. These are, you know, my specific nodes that are having an issue. And I can look at it that level. With Application Signals,
I'm looking at it from a kind of a pivoted view. It's more like what
part of my application, so this APM manager, what
part of my application is having a problem? And then I can trace that down, even down to it's my pet service, I have a pet website. It's my pet service, but not just all of the pet service, it's the GET calls on the pet service, you know, like my GET list pets. That's the one thing
that's having the issue, that's more application-oriented, but it connects the dots on that and has an opinionated approach to some of the metrics you do there. We'll talk about that more basically now. So I wanted to do a
brief demo for you guys. So I come in here. Ooh, look at that. And it should start playing. Okay, there we go. Okay, so we go straight
into Container Insights. I'm getting a sense of what's
going on with my application. I wanna pause that real quick. Right away, I've got multiple clusters that are showing up here, right? So I've got this nice
honeycomb looking thing here. My red clusters, the one I'm probably gonna
pay the most attention, that means I've got some alerts, I've got some alarms that are going on. My green clusters here are pretty healthy, and I can highlight over
them to kinda get a sense of what's going on, right? I can see, you know, right now I'm just showing you the alarms, you know, low utilization, my low blue ones aren't
being used very much. I can click on that cluster and it gives me some general information. I can see where the cluster
alarms are coming off. Are they happening in my cluster? Are they happening in my nodes? Where am I getting the alarm from, right? I can get a sense of that. My green one I can see is
doing just what? Just fine. These blue, I'll pause there for a second. It's not that something's
wrong with the dark blue ones, it's that they're using a lot of memory, and I wanna be aware of that, because I might be under
allocating the amount of memory that's going on in there. So it gives me a nice visual cue. There's something there that I might need to
be paying attention to. It might be on its way to being something that we really need to focus in on. So, great, I get that, I understand the memory
that's going on there. It gives me this high level information. These are basically
underutilized clusters. I might wanna look at those
just from an efficiency and a cost perspective, you
know, to see what's going on. I get some performance
metrics up in the top left and some cluster control plane metrics. And this is kinda interesting, so you can see what's happening
with your control plane, and you kinda get a
summary view of it there. As I scroll down, my
cluster here just has CPU, but if I have GPU, I can
also pivot through GPU and GPU memory as well. I can gather that information here and get a good sense of what services and what machines are using
the most amount of power. And at this level, I'm looking
at it at the cluster level, so it's more focused
on the actual machines. Those are the machines associated
with my computer, right? Once I have that, you know, I'm getting this nice high level here, but I might wanna dig
into something, right? I might wanna go in and
say, "Okay, now I know what's happening in this
space with my cluster. If I wanna go into the next level, I can dive in a little bit more." And here I'm just
looking to see, you know, which ones are performant. I got one more overview page here at the bottom which I like, and it shows me kind of a
snapshot of individual clusters and what their kind of profile looks like from a memory and CPU perspective. Let's go look at the
one that has the error. So with the error one, I load
it up, the data loads on me, and I can go ahead and
see at a cluster level, it'll come in where I basically have this. Hold on, it shouldn't be
taking that long to load. Hang on a sec. There it goes. Okay. So I can go ahead and see right
at the top, at my clusters, it's showing me which alarms
I actually triggered, right? So it's providing that kind of
deeper insight for me, right? I knew I had alarms, now it's like, okay, specifically, which alarms got triggered? And then I have a bunch of other metrics that are coming here all the way down to kind of a deeper set of metrics on like your network traffic, what's going on with the bytes received for the different pods,
your node performance, there's quite a bit of
information that's there. And again, I can slice and dice it, right now I'm at the cluster level, but as we go in, I'll
be able to slice it down to be more specific and
dig into those components that I wanna get to, right? So here you go. I slipped, clicked on my alarm and it basically took me down and said, "Okay, let's go look at the containers that are having this potential issue." And I can see my containers
are pretty spiky, right? I can get some insight from that. I potentially investigate that
to see where do I, you know, where do I wanna, you know, go discover what issues are occurring, what's happening in this space? Frankly, with most of
this, it looks like, okay, it's probably not too bad. Maybe I'll look at it at a workload level to see if at that level,
if I have more insights to be gained from the system. And I like that you can get
the same kind of metrics at each of these levels. You can get some consistency
across your systems. And that's something we've done in this, we've made an opinionated
drive towards, you know, having some level set
metrics that you'll go after. So, okay, great, I've looked
at the workloads, I go in here, maybe I need to look at this from a little bit of a
different perspective. Let me go look at my application signals and say rather than looking
at the individual components, let's look from the
application how it's working. And I can see here now
I've got another clue that I've got some stuff that's unhealthy with this vet service that I'm looking at. And I'll take just a second here. The vet service, I'm right now, all the metrics that you're
seeing across the top, these metrics are associated
with that GET /vets. It's just that one method, if I wanna see what's
happening with, you know, get accrual information or there's several other
ones that are down there, I can get the same kind of
golden metrics we have here which are our volume and availability, our latency, and our error rates. And that gives me a chance
to have the same kind of data across each of my services. I can look in here, I can
see what the availability. Notice my availability is a hundred. I can see my volume's
kind of going up and down. That's that orange line,
that's the amount of people that are using my service. Okay, not a big deal. My latency is kind of spiking
on some of these things, and all those data points, if
I want to, I can click on them and see what correlated information I have with that service, right? So if I end up clicking on one of those, I end up loading up a new
window, then it will go ahead and show me additional information I have, including the correlated traces. So now I went from seeing
a high level of the metrics and a little bit of
which particular method is getting called. So I have the traces, I
click one of the traces, I can come in and see my service. It tells me, you know, my map tells me a little
bit of information on where I might be having the issues. And you can kind of dig
in from that perspective. And I can see, okay, is any
of this look like, you know, it might be, you know, part
of the issue that's going on. I'll scroll down here in a second, and when I do that, then you
can go in and see the paths and what's going on with the paths. So obviously there's a fault going, there's a couple of faults that are happy, and those would be ones that
I investigate pretty quickly to see, okay, this is probably
where I'm having the issue. I can track that down and
say, "here's the faults, here's what's going on in that space." Maybe I'm also curious,
you know, what are the logs that I've been having with this service? So I'm not gonna click on the faults, we figured out likely it's
gonna be that 500 error. I need to do something about that, right? And I've been able to
make that connection. But let's go just look at the logs, we'll look at the logs for
the vet service quickly, just so we get a chance to
see what's happening there. Oh, hold on, first I'm coming
into the vet service for this. Let me see if I can zip that
for. I gotta let it run. So here, I'm doing one more
last look at the pod level to understand, you know, if
I see what's happening there. And I can definitely see
the one I just passed up, I'm capping out on utilization in the pod, and that's probably
what's causing the issue. Basically I'm hitting the
peak on the amount of memory that I'm getting. Now I'm gonna deep dive into the logs. So that's, you know, I'm
able to see a little more about that error if I wanted to dig in. And I just wanted to show in Log Insights how I can kind of trim and see the information
a little differently. So first, I do a query,
I've got a filter here where I'm just filtering it
by the logs that I care about. So I'm doing that specific service. And the real thing I wanna point out here, is yes, I can go open each of these logs, I can dig in and do that, but that little visual
chart across the top, I found to be very powerful. Like, if it's normally this near zero, near zero,
near zero, really small, and then 400, those logs are
probably pretty interesting to go look at, right? You do that, you can
get at that information from that direction as well. And that's the last thing I
wanted to highlight in the demo. Really what we're able to
do is we're able to take it where you can with using
these services in connection, you take those metrics, you take the logs, you take the traces, and you're interacting with
each of them, you know, in a very seamless way, right? You're kind of going back and forth. You don't have to say, "Oh,
I was looking at this metric, now open up this other window
and go look at these logs. I was looking at these logs, let me open up this other
window, go look at these traces." I can kind of navigate back
and forth between all of them as I'm doing my investigation. And I think that's really
natural and a good way for you to get strategic insights in there. So quickly, I think with CloudWatch agent, we're able to onboard a lot faster. It's a lot easier to get
past that initial hurdle of how do we take it and say,
"We just wanna get there, we wanna get into the
system and make it happen." You get an opinion of view, you get basically a set of all the metrics you might need from these dashboards and what's going in there. If you wanna change them, you
wanna add to them and modify, you can do some of those things. You can make some of your own dashboards and your own approaches to doing it. But you don't have to start from zero. You've got experts that
have been feeding us what we, you know, what you think is the
best approach, right? Like, we're telling you
a lot of our customers are saying this is a good way
to get at solving problems. You have application signals, it does a great job of like end
to end integration of those, you know, metrics, logs, and traces so that you can really
dig into that solution. We are opinionated, we
are giving, you know, a perspective on this. You know, we're not expecting you to know everything coming in. You come in, you can get a
direct start going in that. Cost and pricing, I
didn't highlight in here, but we have something
called split data costs, which is a newer feature we released over the last year or so. And it allows you to gather your metrics from EKS and from ECS, and then split them so you can see by task or by service, by pod, by node, you know, where you're spending the money. And that's also a really
interesting kind of approach to making that happen. And that's it. Thank y'all very much. (audience applauding) Please fill out the survey.

## Subtitles with Timestamps

[00:01](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1s) - Observability strategies with EKS.

[00:03](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=3s) We're gonna start in a little more broad

[00:05](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=5s) with a bit of basic
foundational information

[00:07](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=7s) on observability as a whole,

[00:09](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=9s) and then we'll focus in on
some of the things you can do

[00:11](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=11s) and approaches for
getting insights into EKS

[00:14](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=14s) and get understanding your clusters.

[00:17](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=17s) Really basic level set. Why
are we doing observability?

[00:20](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=20s) What's the point here?

[00:20](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=20s) We're trying to detect,
investigate things.

[00:22](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=22s) We're trying to make sure
that we can figure out

[00:24](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=24s) how to remediate our clusters

[00:27](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=27s) or anything that's happening there.

[00:28](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=28s) We're also really trying
to get deeper insights

[00:29](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=29s) into the clusters and understand, okay,

[00:32](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=32s) how can I improve the performance?

[00:33](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=33s) How can I make this something

[00:34](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=34s) where I'm really having a
better solution over time?

[00:38](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=38s) Or I'm fixing something

[00:39](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=39s) that is occurring in the moment, right?

[00:42](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=42s) And the way that we get at that

[00:44](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=44s) is we have kind of these three pillars

[00:46](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=46s) that are pretty strong
that you'll need to have.

[00:49](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=49s) You need to have your logs,

[00:50](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=50s) you need to have your metrics,
you need to have your traces.

[00:52](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=52s) Each of these are kind
of foundational things

[00:54](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=54s) for you to get at to get that information.

[00:55](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=55s) So then it becomes, how
do I get this information?

[00:58](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=58s) What am I using it for?

[00:59](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=59s) And what is my main way
of getting at it in a way

[01:02](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=62s) that is truly accessible for my team

[01:05](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=65s) or for the people that are
working on these clusters, right?

[01:09](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=69s) So we get in there, we want
to collect that information,

[01:12](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=72s) we want to know what we're doing with it,

[01:14](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=74s) but there's some barriers to
making this happen, right?

[01:16](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=76s) So onboarding can be a barrier.

[01:18](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=78s) Right off I'm saying, "Hey, I
wanna gather this information,

[01:21](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=81s) but what way do I gather?"

[01:23](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=83s) Is it an OTel approach
to doing these things?

[01:25](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=85s) Is it something that's
maybe cloud-specific

[01:27](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=87s) to the vendor that I'm using?

[01:28](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=88s) What do I do to gather this information

[01:30](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=90s) and how do I get it into my solutions?

[01:32](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=92s) Like how can I make that simpler?

[01:34](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=94s) 'Cause there are multiple
approaches for doing this.

[01:35](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=95s) Which one's the right
approach for me and my people?

[01:39](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=99s) What metrics to collect?
I can collect everything.

[01:41](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=101s) Do I need everything?

[01:42](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=102s) Probably not. Probably
you don't need everything.

[01:44](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=104s) Let's look at your clusters,
see what it's doing,

[01:46](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=106s) and pick and choose which metrics

[01:48](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=108s) are of the most value to you,

[01:49](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=109s) or follow an opinionated approach

[01:51](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=111s) that gives you some
guidance on, as an industry,

[01:54](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=114s) we've said this is the best way

[01:55](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=115s) to collect some of these metrics, right?

[01:57](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=117s) And then analyze that impact, right?

[01:59](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=119s) Understand like, okay,
I've got the metrics,

[02:02](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=122s) I've got the logs,

[02:04](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=124s) the traces are telling
me some information.

[02:06](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=126s) Kind of so what? What does it mean?

[02:07](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=127s) What does connecting
them actually, you know,

[02:11](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=131s) how do I take that data and
turn it into information?

[02:14](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=134s) How do I make it something
where I can look at it

[02:16](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=136s) and say, "Okay, this is value
that I'm getting out of this."

[02:19](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=139s) Not just, "Okay, there's an error here."

[02:21](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=141s) Like, is it an important error?

[02:22](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=142s) Is it actually causing problems?

[02:24](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=144s) Is it more like something's going wrong,

[02:26](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=146s) but I'm recovering nicely from it?

[02:28](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=148s) Understand these things.

[02:29](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=149s) And then what is the
right opinionated approach

[02:31](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=151s) to make this occur?

[02:32](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=152s) Can I just take, you know,
somebody else's perspective

[02:35](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=155s) or does my company need to have
its own approach to do this?

[02:38](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=158s) This tends to take some thought,

[02:39](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=159s) and so some effort to go after it.

[02:42](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=162s) And if I have a decision, you know,

[02:45](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=165s) can I change it over time?

[02:46](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=166s) Is this something where
I can evaluate this

[02:48](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=168s) and move it along?

[02:50](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=170s) And with a lot of our
solutions, you can do that,

[02:52](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=172s) in fact, that's one of
the things that's nicer,

[02:54](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=174s) is I can choose to start with one solution

[02:56](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=176s) and then go over and say, you know what?

[02:58](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=178s) I really need move over to this
other approach to doing it.

[03:01](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=181s) And then finally, cost.

[03:03](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=183s) Observability is great,

[03:03](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=183s) but it can't cost more than
your application, right?

[03:05](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=185s) Like we've gotta have a balance there

[03:09](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=189s) on how much we're paying
to get that insight

[03:10](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=190s) and understand what we're getting.

[03:14](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=194s) So in AWS we like to
give you options, right?

[03:16](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=196s) So there's several ways you
can kind of approach this.

[03:18](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=198s) This is a kind of an overview
of our tool set that's there.

[03:21](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=201s) I wanna point out kind of
three overall approaches

[03:24](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=204s) that we have to do it.

[03:25](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=205s) One, you can go with like a
managed open source approach.

[03:29](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=209s) This is gonna be more like

[03:29](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=209s) your Prometheus Grafana type services,

[03:32](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=212s) things like that where you're saying,

[03:33](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=213s) look, these are open source solutions,

[03:36](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=216s) they're available to us, they're
things that we can leverage

[03:39](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=219s) and we know we can use
that in multiple locations.

[03:41](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=221s) Sometimes that's the right
approach to make that happen.

[03:44](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=224s) You should really have a
strong tool set in that space.

[03:46](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=226s) Another type option might be down there

[03:49](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=229s) where you see our Amazon
OpenSearch service.

[03:51](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=231s) And that's another place
where I can pump all my logs,

[03:55](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=235s) I can pump my metrics,
I can pump my traces,

[03:57](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=237s) and I can get insights from that service.

[04:00](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=240s) And that could be a strong approach

[04:01](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=241s) for doing your observability,

[04:03](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=243s) actually getting those
insights into one window

[04:06](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=246s) where I can go ahead and check it out

[04:08](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=248s) and make sure that I understand

[04:09](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=249s) this is how my teams are gonna solve this.

[04:12](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=252s) And then the last approach
is our cloud native services,

[04:15](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=255s) which is a number of the ones up there,

[04:16](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=256s) but they focus around CloudWatch

[04:19](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=259s) and the tools that we've built into that.

[04:20](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=260s) That's gonna be things like our, you know,

[04:23](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=263s) container insights, our
logs, all these things.

[04:26](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=266s) I'm gonna focus on that last
one 'cause it's 15 minute talk,

[04:28](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=268s) I can't deep dive on each of them,

[04:30](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=270s) but there's good use cases

[04:32](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=272s) for all those approaches
and those solutions.

[04:35](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=275s) If you wanna talk more about
that, just to catch me after,

[04:38](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=278s) we can dive into that.

[04:41](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=281s) All right, so one of the first
problems I brought up was,

[04:45](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=285s) okay, how do I collect the metrics, right?

[04:47](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=287s) Do I use ADOT, do I go ahead and say,

[04:50](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=290s) you know, I'm gonna do, you know,

[04:51](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=291s) these various open, you
know, telemetry approaches

[04:53](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=293s) to gathering my metrics.

[04:55](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=295s) One of the things we've done

[04:56](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=296s) is we've done a big improvement
with the CloudWatch agent.

[04:58](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=298s) In the CloudWatch agent,
essentially now you can use that

[05:01](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=301s) and you will have fewer things
that you need to get deployed

[05:04](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=304s) instead of have to have your X-Ray daemon,

[05:07](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=307s) your OTel collector,

[05:08](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=308s) or some kind of tracing
daemon in your OTel collector.

[05:11](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=311s) You can just do it all
with a CloudWatch agent.

[05:13](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=313s) You can deploy that, you just
have that one side car running

[05:16](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=316s) and that's gonna be able
to take care of all that

[05:17](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=317s) for your logs, your
metrics, and your traces.

[05:19](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=319s) It kind of enables all of that now.

[05:21](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=321s) So that's been a big improvement.

[05:23](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=323s) It is backwards-compatible

[05:24](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=324s) and it does work with
OpenTelemetry, right?

[05:26](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=326s) Which is a big deal.

[05:28](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=328s) You can then take it,

[05:29](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=329s) your code is pushing out
OpenTelemetry metrics,

[05:32](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=332s) that is able to be gathered
by your CloudWatch agent.

[05:35](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=335s) If you change your mind

[05:36](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=336s) and you wanna do something
that's more open source,

[05:38](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=338s) you can still do that, right?

[05:40](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=340s) So it's not locking you into it,

[05:42](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=342s) but it is pretty powerful for making it

[05:43](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=343s) so that you can rapidly at
least gather the metrics

[05:46](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=346s) and gather the traces and
stuff, things like that,

[05:48](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=348s) and your logs, basically all of them.

[05:53](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=353s) So let's look at these a little bit.

[05:54](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=354s) So CloudWatch Logs has a number of tools,

[05:55](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=355s) we have like anomalies,

[05:57](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=357s) we have a lot of ways
to get the information.

[06:00](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=360s) Today, I just wanna highlight insights.

[06:02](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=362s) It's a great way for you to
basically be able to say,

[06:04](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=364s) you know what, I've got my logs,

[06:06](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=366s) and I'll do a demo in a little bit,

[06:07](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=367s) I've got my logs and I wanna understand

[06:10](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=370s) what's the pattern with these logs,

[06:11](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=371s) what's going on with them?

[06:12](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=372s) Can I filter them, search them?

[06:13](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=373s) Can I do basically deep analysis
and understand, you know,

[06:18](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=378s) is there a repeating pattern
over time with my system

[06:22](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=382s) so I can actually get
to the root of things?

[06:23](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=383s) And CloudWatch Insights really kind of

[06:25](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=385s) highlights that space.

[06:28](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=388s) And it, you know,
integrates, you know, deeply

[06:30](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=390s) with several of our services.

[06:32](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=392s) I think the main thing that I
find really powerful about it

[06:34](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=394s) is there's not just the logs here,

[06:36](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=396s) but when I show the demo,

[06:36](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=396s) it also shows when the logs are happening,

[06:39](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=399s) as you can see visually, like
a set of spikes and dips,

[06:42](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=402s) and then you can also just
dig into the actual content

[06:44](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=404s) that's coming out of those logs,

[06:45](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=405s) which can be really powerful.

[06:46](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=406s) Like, hey, everything
looked like it was fine,

[06:49](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=409s) we published something new

[06:50](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=410s) and now I've got a whole
bunch of logs coming out.

[06:53](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=413s) I'm like, "Ah, okay, that's
not normal, you know,

[06:57](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=417s) let's go look at that spiked area,"

[06:58](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=418s) and I'll show that in a little bit.

[07:02](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=422s) The next service that I wanna
highlight a little bit of

[07:03](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=423s) is our Container Insights.

[07:05](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=425s) I know we're focused on EKS here,

[07:07](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=427s) but we have enhanced Container Insights,

[07:08](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=428s) that's been a big deal for
EKS for a little while,

[07:11](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=431s) we now offer it in ECS, that's
a newer release for that.

[07:14](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=434s) But what's really interesting here

[07:15](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=435s) that I wanna make sure
y'all get a good sense of

[07:17](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=437s) is you can kind of slice and dice it.

[07:19](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=439s) You start off looking at
the whole cluster, great.

[07:21](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=441s) You can use that to dig down and say,

[07:23](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=443s) "Hey, the problem tends to be the service.

[07:25](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=445s) I've got the service

[07:25](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=445s) and it's what's causing
the most issues," right?

[07:28](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=448s) And then from there, you
know, maybe I look down

[07:30](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=450s) and see which pod that's
associated with that service

[07:32](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=452s) is the one that's, you
know, I need to dig into.

[07:34](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=454s) And do I have any alarms or
any messaging around that

[07:37](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=457s) to make it more obvious
to me how I get at it.

[07:40](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=460s) This tool, which we'll show a little bit,

[07:42](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=462s) is a key part of figuring that out.

[07:47](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=467s) And at a different kind of level,

[07:48](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=468s) whereas I like Container Insights,

[07:50](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=470s) It does a good job of giving
you a sense of the components.

[07:54](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=474s) Hey, these are my pods
that are having issues.

[07:56](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=476s) These are, you know, my specific nodes

[07:59](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=479s) that are having an issue.

[08:00](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=480s) And I can look at it that level.

[08:02](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=482s) With Application Signals,
I'm looking at it

[08:03](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=483s) from a kind of a pivoted view.

[08:05](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=485s) It's more like what
part of my application,

[08:08](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=488s) so this APM manager, what
part of my application

[08:10](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=490s) is having a problem?

[08:11](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=491s) And then I can trace that down,

[08:12](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=492s) even down to it's my pet service,

[08:15](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=495s) I have a pet website.

[08:17](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=497s) It's my pet service,

[08:18](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=498s) but not just all of the pet service,

[08:19](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=499s) it's the GET calls on the pet service,

[08:22](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=502s) you know, like my GET list pets.

[08:24](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=504s) That's the one thing
that's having the issue,

[08:25](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=505s) that's more application-oriented,

[08:27](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=507s) but it connects the dots on that

[08:28](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=508s) and has an opinionated approach

[08:30](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=510s) to some of the metrics you do there.

[08:31](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=511s) We'll talk about that more basically now.

[08:36](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=516s) So I wanted to do a
brief demo for you guys.

[08:39](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=519s) So I come in here.

[08:41](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=521s) Ooh, look at that.

[08:44](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=524s) And it should start playing.

[08:51](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=531s) Okay, there we go.

[08:53](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=533s) Okay, so we go straight
into Container Insights.

[08:56](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=536s) I'm getting a sense of what's
going on with my application.

[08:59](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=539s) I wanna pause that real quick.

[09:01](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=541s) Right away, I've got multiple clusters

[09:03](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=543s) that are showing up here, right?

[09:04](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=544s) So I've got this nice
honeycomb looking thing here.

[09:06](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=546s) My red clusters,

[09:07](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=547s) the one I'm probably gonna
pay the most attention,

[09:08](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=548s) that means I've got some alerts,

[09:09](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=549s) I've got some alarms that are going on.

[09:12](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=552s) My green clusters here are pretty healthy,

[09:15](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=555s) and I can highlight over
them to kinda get a sense

[09:17](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=557s) of what's going on, right?

[09:19](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=559s) I can see, you know,

[09:20](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=560s) right now I'm just showing you the alarms,

[09:21](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=561s) you know, low utilization,

[09:23](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=563s) my low blue ones aren't
being used very much.

[09:25](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=565s) I can click on that cluster

[09:26](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=566s) and it gives me some general information.

[09:28](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=568s) I can see where the cluster
alarms are coming off.

[09:30](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=570s) Are they happening in my cluster?

[09:31](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=571s) Are they happening in my nodes?

[09:32](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=572s) Where am I getting the alarm from, right?

[09:34](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=574s) I can get a sense of that.

[09:35](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=575s) My green one I can see is
doing just what? Just fine.

[09:38](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=578s) These blue, I'll pause there for a second.

[09:40](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=580s) It's not that something's
wrong with the dark blue ones,

[09:43](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=583s) it's that they're using a lot of memory,

[09:44](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=584s) and I wanna be aware of that,

[09:46](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=586s) because I might be under
allocating the amount of memory

[09:49](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=589s) that's going on in there.

[09:50](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=590s) So it gives me a nice visual cue.

[09:52](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=592s) There's something there

[09:53](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=593s) that I might need to
be paying attention to.

[09:54](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=594s) It might be on its way to being something

[09:56](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=596s) that we really need to focus in on.

[09:59](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=599s) So, great, I get that,

[10:00](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=600s) I understand the memory
that's going on there.

[10:02](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=602s) It gives me this high level information.

[10:04](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=604s) These are basically
underutilized clusters.

[10:06](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=606s) I might wanna look at those
just from an efficiency

[10:08](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=608s) and a cost perspective, you
know, to see what's going on.

[10:10](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=610s) I get some performance
metrics up in the top left

[10:13](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=613s) and some cluster control plane metrics.

[10:15](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=615s) And this is kinda interesting,

[10:15](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=615s) so you can see what's happening
with your control plane,

[10:18](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=618s) and you kinda get a
summary view of it there.

[10:21](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=621s) As I scroll down, my
cluster here just has CPU,

[10:25](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=625s) but if I have GPU, I can
also pivot through GPU

[10:27](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=627s) and GPU memory as well.

[10:29](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=629s) I can gather that information here

[10:31](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=631s) and get a good sense of what services

[10:34](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=634s) and what machines are using
the most amount of power.

[10:37](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=637s) And at this level, I'm looking
at it at the cluster level,

[10:39](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=639s) so it's more focused
on the actual machines.

[10:41](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=641s) Those are the machines associated
with my computer, right?

[10:45](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=645s) Once I have that, you know,

[10:47](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=647s) I'm getting this nice high level here,

[10:48](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=648s) but I might wanna dig
into something, right?

[10:50](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=650s) I might wanna go in and
say, "Okay, now I know

[10:53](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=653s) what's happening in this
space with my cluster.

[10:56](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=656s) If I wanna go into the next level,

[10:57](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=657s) I can dive in a little bit more."

[10:59](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=659s) And here I'm just
looking to see, you know,

[11:01](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=661s) which ones are performant.

[11:04](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=664s) I got one more overview page

[11:06](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=666s) here at the bottom which I like,

[11:07](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=667s) and it shows me kind of a
snapshot of individual clusters

[11:12](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=672s) and what their kind of profile looks like

[11:14](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=674s) from a memory and CPU perspective.

[11:16](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=676s) Let's go look at the
one that has the error.

[11:19](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=679s) So with the error one, I load
it up, the data loads on me,

[11:24](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=684s) and I can go ahead and
see at a cluster level,

[11:26](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=686s) it'll come in where I basically have this.

[11:30](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=690s) Hold on, it shouldn't be
taking that long to load.

[11:33](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=693s) Hang on a sec.

[11:37](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=697s) There it goes. Okay.

[11:39](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=699s) So I can go ahead and see right
at the top, at my clusters,

[11:43](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=703s) it's showing me which alarms
I actually triggered, right?

[11:45](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=705s) So it's providing that kind of
deeper insight for me, right?

[11:48](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=708s) I knew I had alarms, now it's like, okay,

[11:50](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=710s) specifically, which alarms got triggered?

[11:53](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=713s) And then I have a bunch of other metrics

[11:54](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=714s) that are coming here all the way down

[11:56](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=716s) to kind of a deeper set of metrics

[11:58](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=718s) on like your network traffic,

[11:59](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=719s) what's going on with the bytes received

[12:02](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=722s) for the different pods,
your node performance,

[12:04](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=724s) there's quite a bit of
information that's there.

[12:06](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=726s) And again, I can slice and dice it,

[12:08](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=728s) right now I'm at the cluster level,

[12:10](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=730s) but as we go in, I'll
be able to slice it down

[12:12](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=732s) to be more specific and
dig into those components

[12:15](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=735s) that I wanna get to, right?

[12:19](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=739s) So here you go.

[12:20](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=740s) I slipped, clicked on my alarm

[12:22](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=742s) and it basically took me down and said,

[12:24](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=744s) "Okay, let's go look at the containers

[12:27](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=747s) that are having this potential issue."

[12:29](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=749s) And I can see my containers
are pretty spiky, right?

[12:32](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=752s) I can get some insight from that.

[12:33](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=753s) I potentially investigate that
to see where do I, you know,

[12:37](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=757s) where do I wanna, you know,

[12:38](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=758s) go discover what issues are occurring,

[12:40](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=760s) what's happening in this space?

[12:41](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=761s) Frankly, with most of
this, it looks like, okay,

[12:43](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=763s) it's probably not too bad.

[12:46](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=766s) Maybe I'll look at it at a workload level

[12:47](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=767s) to see if at that level,
if I have more insights

[12:51](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=771s) to be gained from the system.

[12:57](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=777s) And I like that you can get
the same kind of metrics

[12:59](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=779s) at each of these levels.

[13:00](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=780s) You can get some consistency
across your systems.

[13:03](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=783s) And that's something we've done in this,

[13:04](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=784s) we've made an opinionated
drive towards, you know,

[13:08](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=788s) having some level set
metrics that you'll go after.

[13:11](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=791s) So, okay, great, I've looked
at the workloads, I go in here,

[13:14](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=794s) maybe I need to look at this

[13:15](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=795s) from a little bit of a
different perspective.

[13:16](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=796s) Let me go look at my application signals

[13:18](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=798s) and say rather than looking
at the individual components,

[13:21](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=801s) let's look from the
application how it's working.

[13:23](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=803s) And I can see here now
I've got another clue

[13:24](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=804s) that I've got some stuff that's unhealthy

[13:26](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=806s) with this vet service that I'm looking at.

[13:29](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=809s) And I'll take just a second here.

[13:31](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=811s) The vet service, I'm right now,

[13:33](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=813s) all the metrics that you're
seeing across the top,

[13:36](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=816s) these metrics are associated
with that GET /vets.

[13:38](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=818s) It's just that one method,

[13:40](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=820s) if I wanna see what's
happening with, you know,

[13:42](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=822s) get accrual information

[13:43](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=823s) or there's several other
ones that are down there,

[13:45](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=825s) I can get the same kind of
golden metrics we have here

[13:47](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=827s) which are our volume and availability,

[13:48](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=828s) our latency, and our error rates.

[13:51](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=831s) And that gives me a chance
to have the same kind of data

[13:55](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=835s) across each of my services.

[13:58](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=838s) I can look in here, I can
see what the availability.

[14:01](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=841s) Notice my availability is a hundred.

[14:02](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=842s) I can see my volume's
kind of going up and down.

[14:04](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=844s) That's that orange line,
that's the amount of people

[14:05](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=845s) that are using my service.

[14:07](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=847s) Okay, not a big deal.

[14:08](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=848s) My latency is kind of spiking
on some of these things,

[14:11](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=851s) and all those data points, if
I want to, I can click on them

[14:14](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=854s) and see what correlated information I have

[14:16](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=856s) with that service, right?

[14:17](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=857s) So if I end up clicking on one of those,

[14:19](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=859s) I end up loading up a new
window, then it will go ahead

[14:21](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=861s) and show me additional information I have,

[14:23](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=863s) including the correlated traces.

[14:26](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=866s) So now I went from seeing
a high level of the metrics

[14:28](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=868s) and a little bit of
which particular method

[14:30](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=870s) is getting called.

[14:31](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=871s) So I have the traces, I
click one of the traces,

[14:33](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=873s) I can come in and see my service.

[14:35](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=875s) It tells me, you know,

[14:36](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=876s) my map tells me a little
bit of information

[14:37](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=877s) on where I might be having the issues.

[14:40](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=880s) And you can kind of dig
in from that perspective.

[14:42](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=882s) And I can see, okay, is any
of this look like, you know,

[14:46](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=886s) it might be, you know, part
of the issue that's going on.

[14:49](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=889s) I'll scroll down here in a second,

[14:53](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=893s) and when I do that, then you
can go in and see the paths

[14:56](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=896s) and what's going on with the paths.

[14:57](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=897s) So obviously there's a fault going,

[14:59](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=899s) there's a couple of faults that are happy,

[15:00](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=900s) and those would be ones that
I investigate pretty quickly

[15:02](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=902s) to see, okay, this is probably
where I'm having the issue.

[15:06](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=906s) I can track that down and
say, "here's the faults,

[15:08](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=908s) here's what's going on in that space."

[15:10](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=910s) Maybe I'm also curious,
you know, what are the logs

[15:13](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=913s) that I've been having with this service?

[15:14](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=914s) So I'm not gonna click on the faults,

[15:16](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=916s) we figured out likely it's
gonna be that 500 error.

[15:19](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=919s) I need to do something about that, right?

[15:22](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=922s) And I've been able to
make that connection.

[15:23](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=923s) But let's go just look at the logs,

[15:24](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=924s) we'll look at the logs for
the vet service quickly,

[15:26](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=926s) just so we get a chance to
see what's happening there.

[15:32](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=932s) Oh, hold on, first I'm coming
into the vet service for this.

[15:34](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=934s) Let me see if I can zip that
for. I gotta let it run.

[15:42](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=942s) So here, I'm doing one more
last look at the pod level

[15:45](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=945s) to understand, you know, if
I see what's happening there.

[15:49](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=949s) And I can definitely see
the one I just passed up,

[15:53](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=953s) I'm capping out on utilization in the pod,

[15:55](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=955s) and that's probably
what's causing the issue.

[15:57](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=957s) Basically I'm hitting the
peak on the amount of memory

[15:59](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=959s) that I'm getting.

[16:00](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=960s) Now I'm gonna deep dive into the logs.

[16:02](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=962s) So that's, you know, I'm
able to see a little more

[16:05](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=965s) about that error if I wanted to dig in.

[16:07](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=967s) And I just wanted to show in Log Insights

[16:09](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=969s) how I can kind of trim

[16:10](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=970s) and see the information
a little differently.

[16:15](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=975s) So first, I do a query,
I've got a filter here

[16:17](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=977s) where I'm just filtering it
by the logs that I care about.

[16:20](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=980s) So I'm doing that specific service.

[16:22](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=982s) And the real thing I wanna point out here,

[16:25](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=985s) is yes, I can go open each of these logs,

[16:27](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=987s) I can dig in and do that,

[16:28](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=988s) but that little visual
chart across the top,

[16:30](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=990s) I found to be very powerful.

[16:31](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=991s) Like, if it's normally this

[16:33](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=993s) near zero, near zero,
near zero, really small,

[16:35](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=995s) and then 400, those logs are
probably pretty interesting

[16:38](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=998s) to go look at, right?

[16:40](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1000s) You do that, you can
get at that information

[16:41](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1001s) from that direction as well.

[16:43](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1003s) And that's the last thing I
wanted to highlight in the demo.

[16:46](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1006s) Really what we're able to
do is we're able to take it

[16:48](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1008s) where you can with using
these services in connection,

[16:52](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1012s) you take those metrics, you take the logs,

[16:54](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1014s) you take the traces,

[16:55](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1015s) and you're interacting with
each of them, you know,

[16:57](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1017s) in a very seamless way, right?

[16:58](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1018s) You're kind of going back and forth.

[17:00](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1020s) You don't have to say, "Oh,
I was looking at this metric,

[17:01](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1021s) now open up this other window
and go look at these logs.

[17:04](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1024s) I was looking at these logs,

[17:05](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1025s) let me open up this other
window, go look at these traces."

[17:08](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1028s) I can kind of navigate back
and forth between all of them

[17:10](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1030s) as I'm doing my investigation.

[17:11](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1031s) And I think that's really
natural and a good way for you

[17:14](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1034s) to get strategic insights in there.

[17:17](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1037s) So quickly, I think with CloudWatch agent,

[17:22](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1042s) we're able to onboard a lot faster.

[17:23](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1043s) It's a lot easier to get
past that initial hurdle

[17:27](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1047s) of how do we take it and say,
"We just wanna get there,

[17:29](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1049s) we wanna get into the
system and make it happen."

[17:33](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1053s) You get an opinion of view,

[17:34](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1054s) you get basically a set of all the metrics

[17:36](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1056s) you might need from these dashboards

[17:39](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1059s) and what's going in there.

[17:40](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1060s) If you wanna change them, you
wanna add to them and modify,

[17:42](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1062s) you can do some of those things.

[17:43](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1063s) You can make some of your own dashboards

[17:45](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1065s) and your own approaches to doing it.

[17:47](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1067s) But you don't have to start from zero.

[17:49](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1069s) You've got experts that
have been feeding us

[17:51](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1071s) what we, you know,

[17:52](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1072s) what you think is the
best approach, right?

[17:54](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1074s) Like, we're telling you
a lot of our customers

[17:55](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1075s) are saying this is a good way
to get at solving problems.

[17:59](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1079s) You have application signals,

[18:00](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1080s) it does a great job of like end
to end integration of those,

[18:03](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1083s) you know, metrics, logs, and traces

[18:05](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1085s) so that you can really
dig into that solution.

[18:09](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1089s) We are opinionated, we
are giving, you know,

[18:10](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1090s) a perspective on this.

[18:12](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1092s) You know, we're not expecting you to know

[18:13](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1093s) everything coming in.

[18:14](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1094s) You come in, you can get a
direct start going in that.

[18:19](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1099s) Cost and pricing, I
didn't highlight in here,

[18:21](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1101s) but we have something
called split data costs,

[18:23](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1103s) which is a newer feature

[18:26](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1106s) we released over the last year or so.

[18:27](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1107s) And it allows you to gather your metrics

[18:30](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1110s) from EKS and from ECS,

[18:32](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1112s) and then split them so you can see by task

[18:34](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1114s) or by service, by pod, by node,

[18:36](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1116s) you know, where you're spending the money.

[18:38](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1118s) And that's also a really
interesting kind of approach

[18:40](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1120s) to making that happen.

[18:44](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1124s) And that's it. Thank y'all very much.

[18:46](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1126s) (audience applauding)

[18:48](https://www.youtube.com/watch?v=Icz8MBHCPuQ&t=1128s) Please fill out the survey.

