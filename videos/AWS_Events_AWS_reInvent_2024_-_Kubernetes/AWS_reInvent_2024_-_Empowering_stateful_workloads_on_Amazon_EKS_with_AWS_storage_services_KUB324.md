# AWS re:Invent 2024 - Empowering stateful workloads on Amazon EKS with AWS storage services (KUB324)

[Video Link](https://www.youtube.com/watch?v=XCH6Kum1_FI)

## Description

Attend this session to learn proven methods for unlocking scalability, flexibility, and resiliency. Explore the integration of AWS storage services with Amazon EKS to effectively run stateful applications. Discover best practices for allowing thousands of pods to access shared data volumes concurrently. This session demonstrates simple ways to deploy stateful workloads on EKS while optimizing performance. Attendees leave this demo-packed session with actionable insights and resources to start mastering stateful applications on Amazon EKS right away.

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

- Hello, everyone. Thanks for coming. I have a very exciting
opportunity for each of you. Imagine you are solution architect and engaged by a forward
thinking digital company who want to transform
their digital landscape. You task here is going to design a real-time inference application. So it's simple, right? You need to have front end to
receive requests from end user and talk to your inference endpoint. And load model files and generate output. Sounds simple. However, this is stable application because each user have different prompt. They generate different image. So we need to have three
main challenges here. How you ensure the whole
solution is reliable from front end or the back end? How you going to ensure end-user don't wait too long for that image? How you can scale in and scale out your application on demand? Are you ready to take
this journey with me? Awesome, awesome. I have a question.
Basically want to check you. I have two options. I have a pre-recorded
demo, 100% will work. And I have a live demo. Together, we take some risk. Show your hands if you
wanna do a live demo. Surprise. All right, you are very brave. Let's take do a live demo. Basically what I'm going to do is show you this solution we already
built for your reference. Okay, let's game on. So this is Stable Diffusion
we used as foundation model. I just probably use a very
simple running prompt, a running horse and then
let's generate image. While we are waiting,
I will explain, right? So this, refresh pricing,
basically give you opportunity to use different type of instance type like different size, different family. You can say the price because
this very reliable even for stable application,
you can use sport instance, sport instance to save you money. Here we go. We already
have image generated. We use g6e instance type and we use two models here. Can you see the difference? This one is Stable Diffusion and another one is Flux with another popular foundation model. So this solution, we already built. You can see some challenges we mentioned. We can easily switch model, flexible. We can ensure the whole environment can leverage different instance type and ensure use sport instance
to provide reliability. Even a sport sometimes is not available. Okay, let's switch back to our PowerPoint. I will show you how you
exactly the technology behind. And then reliability. So in terms of reliability, we need to think about
how you gonna architect the whole environment because
this stable application, we wanna ensure in the event
of failure over the back end or front end, you don't
have impact to end-user. So we chose to use the
asynchronous model. What that mean? The front end, you have
end-user on the left hand side and send a request to API gateway and then lambda function
will do the transformation of the message, validate the
message, and send to AWS SNS, simple notification service. From there, I will distribute the message to the queue, SQS, simple queue service. So this whole process here, what it does is just receive
message from end-user and pull that in queue. That's the first half, it's done. The second half, you have message already in the queue, right? So if you follow me, look
at the icon, step one. Step one, I have a queue agent. This agent, I will pull the image, sorry, pull the message from that SQS and then start to talk with SD Runtime. SD Runtime is a open source project called Stable Diffusion web UI here. As an inference endpoint
to talk with my model file and do the inference work. One, the image generated, it'll be saved into the
step two, S3 bucket. Have we finished? Not yet. Because you need to notify the user, hey, you send back to the call
back to the step three, SNS. This is your message.
The job completed, right? This is whole stable connection finished. Eventually, if everything
working perfectly, step four, it will delete
that message from the queue. KO series is setup up, right? Because we decouple this two
phases in the event of failure of the backend, for example, I have my inference end
point have a failure. Don't worry, the message
in SQSQ is still there. The new trust will come up to retry. So as you can see even
this stable application, I leverage the front
end and manage services, make my back end still stateless, right? You still run stateless containers on EKS. All right, so let's
properly performance side. Basically, again, we want to first load these models, three steps. I want to quickly scale
out my environment adding to the EKS environment, and
I want to load image quickly. I want to load model quickly, three steps. I will show you how to do that. So basically, this is a
step we are going to take to load the model quickly
in these three steps. And from a scalability perspective, what we are going to do is in the event of the significant traffic come in, today I only have one node, right? Running one port, but it's not enough. We need to scale our environment. So we leverage the KEDA which
is open source mechanism to scale out my ports. Here, I have lots of task coming in. I have ports pending. We need backend resources here. I have Karpenter to
scale up my nodes quickly to fulfill this jobs. So now, you have port are running. So that's way how we quickly
scaling out, enough talking. I need to do a real demo here and let's jump to my environment. So basically, I will show
you how we set it up. So this my EKS environment. This result is already put in. Here, I have this
inference runtime running as a port and service. And here, there's a Keda to do the scaling and Karpenter is a mechanism to scale out my backend EC2 instances. So having said that, how can we load our model file quickly when you jump into these settings here, go to the, this is the
resources we already have. But what we need to do
a quickly testing is can I start a new task, right? Generate, oh, by the way, I wanna show you the model files here. We already enabled the S3 CSIDrivers. Here, you can see S3?
Already enabled that. Enable to use S3 bucket
as a persistent volume. You can see the persistent volume is here and I load all the model
files into this bucket, right? Now, let's probably switch to here. I will start a job. What I will going to do is I will just quickly
start with one test. So here, remember the
picture we generated? I make some minor changes here, and you will see the difference because the flexibility we are able to have opportunity to have another model. For this image generation, we have foundation model
which is Stable Diffusion. Lora is another extension
model can work together, right? I still use the exactly same prompt, a very simple prompt, a horse running. But let's say, what's the
difference it going to make? All right, this is going
to send this prompt to my API gateway and then
let's say the difference, I will go to my S3 bucket. That's where I have my
image generated, right? It's already there and that's happened. Can you see a difference, right? Very different from the two
pictures, you know, before. It's Chinese painting style because we use as a lora model. All right, here we are talking
about image generation, but how about you're running
this in a large environment. There are many, many nodes,
many many requests come in. How can you ensure this
environment can scale out quickly and also scale in while it's
quite to save your cost. So I need to simulate a
testing, a load testing. Do you wanna see how
creative we can scale out? If you wanna see that? You wanna see that? All right, cool. Okay, I will generally load, the loads of request come in here. So what I will do is going
to generate the load, but I need to start
with this load testing. So basically, all right, load test. So this is already starting and then I will go to
my console here, right? Before and then I'll just do a fresh. All right, before I do a load testing, I wanna show you the current
settings here, right? So basically, this is the two. All right. This is the two environment. I want to show you the current nodes, only one node, right? And let's make it, and this one I will do the, all right, only one pods running. So let's start the scaling. I will put five users here and then start. So one is running very soon. You can see some request
is going up, right? 17 more. And if you switch back to our console, let's see what's happening here. So lots of ports, right? It's pending. It's waiting for backend. And then from here, we are going to show you some metrics. All right, it's pending here. So you can see the new nodes just brought
up lots of backend new nodes to fulfill this ports. You can CPU is going to increase. But in that, while you
get a new port up running, the CPU new nodes up
running the CPU utilizing will be reduced. Here we go. And what I can show you is in the backend what's happening. This is our dashboard. So I just quickly show the
last probably three minutes and then I will do the refresh. So you can see the difference, right? Because we trigger that low testing, you can see this number going up. When it's going up, reach to a threshold, the backend will trigger
the scaling of my ports. And then because I have lots
of pending ports, right? I will trigger the nodes
to fulfill that tasks, to fulfill that ports. And then if we go back
to this environment, we already have lots of the
nodes up running, right? So it's all running and we
have lots of backend nodes. So it's scaling very fast, you can see. And very soon, if you like, okay. Can you see here? Because it's going up
number of the messages to trigger the backend. So what we'll do is we just stop and very so you will say
this whole environment will be scale in to save your cost. So overall, this is how we
set up the whole environment. What I want to show you is basically the end-to-end visibility because if you look at some
testing here, we just did, we should pick up one of them. So this is end-to-end how it works, whole environment, right? We start with end-user to
send request to API gateway and then pass on to a Lambda
to validate the message. And from here, Lambda will pass on to the SNS and put in the queue. And of that, we'll start the, agent will pull the image from
queue and finish inference. So this whole end-to-end
environment, how it works. So let's probably quickly show you, switch back to our slides. So this is the whole environment
already available for you. You can just go to this solution library. Half an hour, you deploy the whole stack. You can play with that
and also have details, the architecture decisions
we made in this solution. If you want to know more
these some sessions, you can watch the recording
or focus on this sessions. I will cover some details tomorrow around this similar solution on ECS. And then if you want to continue learning this whole solution, how we set the whole solution step by step and also block articles, so this is a URL. You can take a picture. I
already put lots of links. You can easily just look for more details. And overall, I thank you
very much for coming. If you can do a survey,
we'll be much appreciated, so we can make the session better.

## Subtitles with Timestamps

[00:01](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=1s) - Hello, everyone.

[00:03](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=3s) Thanks for coming.

[00:05](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=5s) I have a very exciting
opportunity for each of you.

[00:08](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=8s) Imagine you are solution architect

[00:12](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=12s) and engaged by a forward
thinking digital company

[00:16](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=16s) who want to transform
their digital landscape.

[00:20](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=20s) You task here is going to design

[00:26](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=26s) a real-time inference application.

[00:31](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=31s) So it's simple, right?

[00:34](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=34s) You need to have front end to
receive requests from end user

[00:39](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=39s) and talk to your inference endpoint.

[00:43](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=43s) And load model files and generate output.

[00:48](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=48s) Sounds simple.

[00:51](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=51s) However, this is stable application

[00:54](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=54s) because each user have different prompt.

[00:57](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=57s) They generate different image.

[01:00](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=60s) So we need to have three
main challenges here.

[01:06](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=66s) How you ensure the whole
solution is reliable

[01:09](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=69s) from front end or the back end?

[01:12](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=72s) How you going to ensure end-user

[01:14](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=74s) don't wait too long for that image?

[01:18](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=78s) How you can scale in and scale out

[01:21](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=81s) your application on demand?

[01:25](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=85s) Are you ready to take
this journey with me?

[01:28](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=88s) Awesome, awesome.

[01:31](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=91s) I have a question.
Basically want to check you.

[01:35](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=95s) I have two options.

[01:37](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=97s) I have a pre-recorded
demo, 100% will work.

[01:42](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=102s) And I have a live demo.

[01:45](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=105s) Together, we take some risk.

[01:48](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=108s) Show your hands if you
wanna do a live demo.

[01:52](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=112s) Surprise. All right, you are very brave.

[01:55](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=115s) Let's take do a live demo.

[01:59](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=119s) Basically what I'm going to do is show you

[02:02](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=122s) this solution we already
built for your reference.

[02:05](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=125s) Okay, let's game on.

[02:09](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=129s) So this is Stable Diffusion
we used as foundation model.

[02:13](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=133s) I just probably use a very
simple running prompt,

[02:17](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=137s) a running horse and then
let's generate image.

[02:21](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=141s) While we are waiting,
I will explain, right?

[02:24](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=144s) So this, refresh pricing,
basically give you opportunity

[02:28](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=148s) to use different type of instance type

[02:30](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=150s) like different size, different family.

[02:33](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=153s) You can say the price because
this very reliable even

[02:36](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=156s) for stable application,
you can use sport instance,

[02:41](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=161s) sport instance to save you money.

[02:43](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=163s) Here we go. We already
have image generated.

[02:46](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=166s) We use g6e instance type

[02:49](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=169s) and we use two models here.

[02:51](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=171s) Can you see the difference?

[02:52](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=172s) This one is Stable Diffusion

[02:54](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=174s) and another one is Flux

[02:57](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=177s) with another popular foundation model.

[03:00](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=180s) So this solution, we already built.

[03:02](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=182s) You can see some challenges we mentioned.

[03:05](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=185s) We can easily switch model, flexible.

[03:08](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=188s) We can ensure the whole environment

[03:10](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=190s) can leverage different instance type

[03:13](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=193s) and ensure use sport instance
to provide reliability.

[03:17](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=197s) Even a sport sometimes is not available.

[03:20](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=200s) Okay, let's switch back to our PowerPoint.

[03:25](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=205s) I will show you how you
exactly the technology behind.

[03:31](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=211s) And then reliability.

[03:33](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=213s) So in terms of reliability,

[03:36](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=216s) we need to think about
how you gonna architect

[03:39](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=219s) the whole environment because
this stable application,

[03:43](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=223s) we wanna ensure in the event
of failure over the back end

[03:47](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=227s) or front end, you don't
have impact to end-user.

[03:51](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=231s) So we chose to use the
asynchronous model. What that mean?

[03:57](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=237s) The front end, you have
end-user on the left hand side

[04:00](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=240s) and send a request to API gateway

[04:04](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=244s) and then lambda function
will do the transformation

[04:07](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=247s) of the message, validate the
message, and send to AWS SNS,

[04:13](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=253s) simple notification service.

[04:15](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=255s) From there, I will distribute the message

[04:20](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=260s) to the queue, SQS, simple queue service.

[04:24](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=264s) So this whole process here,

[04:26](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=266s) what it does is just receive
message from end-user

[04:30](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=270s) and pull that in queue.

[04:31](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=271s) That's the first half, it's done.

[04:34](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=274s) The second half, you have message already

[04:37](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=277s) in the queue, right?

[04:39](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=279s) So if you follow me, look
at the icon, step one.

[04:43](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=283s) Step one, I have a queue agent.

[04:45](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=285s) This agent, I will pull the image, sorry,

[04:49](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=289s) pull the message from that SQS

[04:52](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=292s) and then start to talk with SD Runtime.

[04:55](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=295s) SD Runtime is a open source project

[04:58](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=298s) called Stable Diffusion web UI here.

[05:02](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=302s) As an inference endpoint
to talk with my model file

[05:07](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=307s) and do the inference work.

[05:09](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=309s) One, the image generated,

[05:11](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=311s) it'll be saved into the
step two, S3 bucket.

[05:17](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=317s) Have we finished? Not yet.

[05:19](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=319s) Because you need to notify the user,

[05:21](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=321s) hey, you send back to the call
back to the step three, SNS.

[05:27](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=327s) This is your message.
The job completed, right?

[05:29](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=329s) This is whole stable connection finished.

[05:33](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=333s) Eventually, if everything
working perfectly,

[05:36](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=336s) step four, it will delete
that message from the queue.

[05:41](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=341s) KO series is setup up, right?

[05:43](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=343s) Because we decouple this two
phases in the event of failure

[05:48](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=348s) of the backend, for example,

[05:50](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=350s) I have my inference end
point have a failure.

[05:53](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=353s) Don't worry, the message
in SQSQ is still there.

[05:59](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=359s) The new trust will come up to retry.

[06:02](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=362s) So as you can see even
this stable application,

[06:05](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=365s) I leverage the front
end and manage services,

[06:09](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=369s) make my back end still stateless, right?

[06:12](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=372s) You still run stateless containers on EKS.

[06:16](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=376s) All right, so let's
properly performance side.

[06:20](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=380s) Basically, again, we want

[06:23](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=383s) to first load these models, three steps.

[06:25](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=385s) I want to quickly scale
out my environment adding

[06:29](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=389s) to the EKS environment, and
I want to load image quickly.

[06:34](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=394s) I want to load model quickly, three steps.

[06:36](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=396s) I will show you how to do that.

[06:38](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=398s) So basically, this is a
step we are going to take

[06:42](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=402s) to load the model quickly
in these three steps.

[06:46](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=406s) And from a scalability perspective,

[06:50](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=410s) what we are going to do is in the event

[06:55](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=415s) of the significant traffic come in,

[06:59](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=419s) today I only have one node, right?

[07:01](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=421s) Running one port, but it's not enough.

[07:04](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=424s) We need to scale our environment.

[07:06](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=426s) So we leverage the KEDA which
is open source mechanism

[07:11](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=431s) to scale out my ports.

[07:13](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=433s) Here, I have lots of task coming in.

[07:17](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=437s) I have ports pending.

[07:19](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=439s) We need backend resources here.

[07:22](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=442s) I have Karpenter to
scale up my nodes quickly

[07:25](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=445s) to fulfill this jobs.

[07:28](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=448s) So now, you have port are running.

[07:31](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=451s) So that's way how we quickly
scaling out, enough talking.

[07:35](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=455s) I need to do a real demo here

[07:37](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=457s) and let's jump to my environment.

[07:40](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=460s) So basically, I will show
you how we set it up.

[07:44](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=464s) So this my EKS environment.

[07:46](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=466s) This result is already put in.

[07:49](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=469s) Here, I have this
inference runtime running

[07:53](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=473s) as a port and service.

[07:57](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=477s) And here, there's a Keda to do the scaling

[08:00](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=480s) and Karpenter is a mechanism

[08:02](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=482s) to scale out my backend EC2 instances.

[08:06](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=486s) So having said that,

[08:07](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=487s) how can we load our model file quickly

[08:10](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=490s) when you jump into these settings here,

[08:15](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=495s) go to the, this is the
resources we already have.

[08:21](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=501s) But what we need to do
a quickly testing is

[08:24](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=504s) can I start a new task, right?

[08:27](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=507s) Generate, oh, by the way, I wanna show you

[08:31](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=511s) the model files here.

[08:32](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=512s) We already enabled the S3 CSIDrivers.

[08:38](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=518s) Here, you can see S3?
Already enabled that.

[08:41](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=521s) Enable to use S3 bucket
as a persistent volume.

[08:45](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=525s) You can see the persistent volume is here

[08:49](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=529s) and I load all the model
files into this bucket, right?

[08:53](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=533s) Now, let's probably switch to here.

[08:57](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=537s) I will start a job.

[08:59](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=539s) What I will going to do

[09:00](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=540s) is I will just quickly
start with one test.

[09:05](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=545s) So here, remember the
picture we generated?

[09:08](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=548s) I make some minor changes here,

[09:10](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=550s) and you will see the difference

[09:13](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=553s) because the flexibility we are able

[09:15](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=555s) to have opportunity to have another model.

[09:22](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=562s) For this image generation,

[09:23](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=563s) we have foundation model
which is Stable Diffusion.

[09:26](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=566s) Lora is another extension
model can work together, right?

[09:30](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=570s) I still use the exactly same prompt,

[09:33](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=573s) a very simple prompt, a horse running.

[09:35](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=575s) But let's say, what's the
difference it going to make?

[09:39](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=579s) All right, this is going
to send this prompt

[09:43](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=583s) to my API gateway and then
let's say the difference,

[09:47](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=587s) I will go to my S3 bucket.

[09:50](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=590s) That's where I have my
image generated, right?

[09:54](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=594s) It's already there and that's happened.

[09:58](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=598s) Can you see a difference, right?

[09:59](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=599s) Very different from the two
pictures, you know, before.

[10:01](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=601s) It's Chinese painting style

[10:03](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=603s) because we use as a lora model.

[10:06](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=606s) All right, here we are talking
about image generation,

[10:11](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=611s) but how about you're running
this in a large environment.

[10:16](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=616s) There are many, many nodes,
many many requests come in.

[10:20](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=620s) How can you ensure this
environment can scale out quickly

[10:25](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=625s) and also scale in while it's
quite to save your cost.

[10:29](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=629s) So I need to simulate a
testing, a load testing.

[10:33](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=633s) Do you wanna see how
creative we can scale out?

[10:36](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=636s) If you wanna see that? You wanna see that?

[10:39](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=639s) All right, cool.

[10:41](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=641s) Okay, I will generally load,

[10:44](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=644s) the loads of request come in here.

[10:47](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=647s) So what I will do is going
to generate the load,

[10:52](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=652s) but I need to start
with this load testing.

[10:56](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=656s) So basically, all right, load test.

[10:59](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=659s) So this is already starting

[11:04](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=664s) and then I will go to
my console here, right?

[11:08](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=668s) Before and then I'll just do a fresh.

[11:12](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=672s) All right, before I do a load testing,

[11:15](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=675s) I wanna show you the current
settings here, right?

[11:20](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=680s) So basically, this is the two.

[11:28](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=688s) All right. This is the two environment.

[11:31](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=691s) I want to show you the current nodes,

[11:36](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=696s) only one node, right?

[11:38](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=698s) And let's make it,

[11:43](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=703s) and this one I will do the,

[11:54](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=714s) all right, only one pods running.

[11:58](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=718s) So let's start the scaling.

[12:02](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=722s) I will put five users here and then start.

[12:08](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=728s) So one is running very soon.

[12:12](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=732s) You can see some request
is going up, right?

[12:16](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=736s) 17 more.

[12:18](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=738s) And if you switch back to our console,

[12:23](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=743s) let's see what's happening here.

[12:26](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=746s) So lots of ports, right?

[12:28](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=748s) It's pending. It's waiting for backend.

[12:36](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=756s) And then from here,

[12:38](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=758s) we are going to show you some metrics.

[12:41](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=761s) All right, it's pending here.

[12:49](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=769s) So you can see

[12:53](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=773s) the new nodes just brought
up lots of backend new nodes

[12:56](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=776s) to fulfill this ports.

[12:59](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=779s) You can CPU is going to increase.

[13:02](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=782s) But in that, while you
get a new port up running,

[13:07](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=787s) the CPU new nodes up
running the CPU utilizing

[13:10](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=790s) will be reduced.

[13:14](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=794s) Here we go.

[13:16](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=796s) And what I can show you is

[13:18](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=798s) in the backend what's happening.

[13:23](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=803s) This is our dashboard.

[13:25](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=805s) So I just quickly show the
last probably three minutes

[13:31](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=811s) and then I will do the refresh.

[13:36](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=816s) So you can see the difference, right?

[13:38](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=818s) Because we trigger that low testing,

[13:41](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=821s) you can see this number going up.

[13:44](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=824s) When it's going up, reach to a threshold,

[13:47](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=827s) the backend will trigger
the scaling of my ports.

[13:51](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=831s) And then because I have lots
of pending ports, right?

[13:55](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=835s) I will trigger the nodes
to fulfill that tasks,

[13:58](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=838s) to fulfill that ports.

[14:03](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=843s) And then if we go back
to this environment,

[14:08](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=848s) we already have lots of the
nodes up running, right?

[14:12](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=852s) So it's all running and we
have lots of backend nodes.

[14:15](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=855s) So it's scaling very fast, you can see.

[14:19](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=859s) And very soon, if you like, okay.

[14:23](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=863s) Can you see here?

[14:24](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=864s) Because it's going up
number of the messages

[14:27](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=867s) to trigger the backend.

[14:29](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=869s) So what we'll do is we just stop

[14:33](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=873s) and very so you will say
this whole environment

[14:37](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=877s) will be scale in to save your cost.

[14:40](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=880s) So overall, this is how we
set up the whole environment.

[14:44](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=884s) What I want to show you is basically

[14:48](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=888s) the end-to-end visibility

[14:49](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=889s) because if you look at some
testing here, we just did,

[14:55](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=895s) we should pick up one of them.

[14:57](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=897s) So this is end-to-end how it works,

[15:01](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=901s) whole environment, right?

[15:03](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=903s) We start with end-user to
send request to API gateway

[15:07](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=907s) and then pass on to a Lambda
to validate the message.

[15:11](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=911s) And from here, Lambda will pass

[15:15](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=915s) on to the SNS and put in the queue.

[15:19](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=919s) And of that, we'll start the,

[15:22](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=922s) agent will pull the image from
queue and finish inference.

[15:26](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=926s) So this whole end-to-end
environment, how it works.

[15:31](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=931s) So let's probably quickly show you,

[15:35](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=935s) switch back to our slides.

[15:41](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=941s) So this is the whole environment
already available for you.

[15:43](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=943s) You can just go to this solution library.

[15:47](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=947s) Half an hour, you deploy the whole stack.

[15:50](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=950s) You can play with that
and also have details,

[15:54](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=954s) the architecture decisions
we made in this solution.

[16:00](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=960s) If you want to know more
these some sessions,

[16:02](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=962s) you can watch the recording
or focus on this sessions.

[16:06](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=966s) I will cover some details tomorrow

[16:08](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=968s) around this similar solution on ECS.

[16:15](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=975s) And then if you want

[16:17](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=977s) to continue learning this whole solution,

[16:21](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=981s) how we set the whole solution step by step

[16:23](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=983s) and also block articles, so this is a URL.

[16:27](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=987s) You can take a picture. I
already put lots of links.

[16:30](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=990s) You can easily just look for more details.

[16:35](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=995s) And overall, I thank you
very much for coming.

[16:40](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=1000s) If you can do a survey,
we'll be much appreciated,

[16:43](https://www.youtube.com/watch?v=XCH6Kum1_FI&t=1003s) so we can make the session better.

