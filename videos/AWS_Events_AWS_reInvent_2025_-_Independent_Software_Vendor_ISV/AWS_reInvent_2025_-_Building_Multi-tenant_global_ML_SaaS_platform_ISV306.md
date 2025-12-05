# AWS re:Invent 2025 - Building Multi-tenant global ML SaaS platform (ISV306)

[Video Link](https://www.youtube.com/watch?v=flGdaoQsXc4)

## Description

Get insight into how Qlik built a multi-tenant ML SaaS that processes 100,000 GPU-intensive training jobs monthly with 99.99% reliability. Learn about Qlik's proven patterns for scaling ML operations across global regions while optimizing costs through dynamic resource allocation. We'll share the architectural decisions that enabled supporting 2,500 organizations and 167,000 trained models. Essential knowledge for ISVs transforming ML capabilities into scalable SaaS solutions.

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

- All right, welcome to re:Invent. Are you guys all excited? We have... All right, I
like that spirit over there. I guess we have over 2,000 sessions and workshops lined up this week, so make the most out of it. Any first timers over here for re:Invent? All right, that's great. I'm going to recommend to install or activate your pedometer on your phone. Count the number of steps
you're gonna walk this week, and then I'm telling you, you're gonna be pleasantly surprised. A warm welcome to this
presentation. My name is Vin Dahake. I lead solutions architect
team for ISV Private Equity. I've been with AWS for five years now and I'm based out of New York City. Gonna let my partner introduce himself. - Yeah, and thank you, Vin.
Really a pleasure to be here. My name is Sean Stauth. I'm Global Director of AI
and Machine Learning at Qlik, and I have the opportunity to work with our customers worldwide in a variety of different industries
on their cutting-edge AI and machine learning solutions. - All right, thanks, Sean. - All right, before we
get started, you know, a quick show of hands, how many of you have built
machine learning applications, analytics applications that have worked for the first time in production? Oh, that's good. That's good. We have few hands up
over here. It's not easy. I mean, I was hoping everybody
would raise their hand and I would just walk
off from the stage away, say thank you very much, but
this is the reason we are here. You know, building
machine learning platforms which are enterprise ready,
scalable is not easy. And that's why we have Qlik
at our doorsteps today. But before we get started, let me tell you a little bit about Qlik. Qlik has been a global leader for the last 30 years
in data analytics space. They have helped companies,
you know, transform by processing data, getting
insights from the data. Qlik has three core
expertise that we are seeing. They've done a lot of work in
real-time data integration. They've done work in analytics,
business intelligence, visualization, and
third, AI, ML and AutoML. And that's the reason we're here to discuss about Qlik Predict. Today Qlik has over 40,000 customers across 100 different countries. And in 2004, AWS and Qlik, we signed a strategic
collaboration agreement. And I'm excited to tell you the result of this agreement is Qlik Predict. This is a fully managed multi-tenant, global machine learning SaaS platform, which is entirely built on AWS. All right, let's take a quick
look at the agenda over here. You know, we will talk about what this machine learning
predictive analytics platform is. We will do a deep dive
into the architecture. We will look at, you know,
some of the case studies and then we'll talk about
the challenges that we faced and how we can learn from that. 70% of forecasting programs fail. Really, 70%. This is not an academic study. This is, you know, real money,
real business, you know, real challenges that people face. Most of the traditional
forecasting programs fail because, you know, they
look at data in isolation. You know, that's not how real world is. We have seen, you know,
when programs are doing, let's say, for example, sales forecasting, they look at okay, what was
my sales data for last month? It was X so maybe next
month is X plus delta. But that's not how it works in reality. There are multiple variables that need to be taken into consideration, you know, when you're doing forecasting. It could be seasonality,
it is your inventory, economic conditions, it could
be your competitor's action. There are multiple factors. As a matter of fact, there could be up to 50 different factors that
can impact your forecasting. You know, simple models
probably can look at seasonality and make predictions, but for this particular case, when we have 50 plus different variables which interact with each other, we need complex, advanced algorithms like encoder-decoder, perceptron, or recurrent neural networks
to do the forecasting. These models are very
computationally intensive and they need GPUs to, you
know, perform the calculations. As I mentioned, you know,
we've worked with Qlik and we formed this strategic
collaboration agreement and I'm happy, the result of
that was building Qlik Predict. Sean, you wanna share a
little bit more story? - Yeah, yeah, and thank you
because as VIN mentioned, this opportunity is massive and with machine learning, real companies are getting massive results around their supply
chains, their logistics, around their HR and more. And so to start to share a
quick story around a company called Software Logistik
Artland or SLA in Germany. They have a very complex
network of suppliers, distributors, manufacturing that they have to run on a daily basis where even small changes in
their operations can lead to massive impacts around
finances and staffing. And so with Qlik Predict, they're able to build a
forecasting capability and able predict over with
90% accuracy the demand that they needed to
produce every single month. And that led to a 50% reduction
in annual planning needs. And the result is that while they're... This is really complex, they
have a business that is dynamic and they need a capability
that can match that reality. And so today we're talking
about taking the next leap, having a multivariate
forecasting capability that can have smarter
forecasting at a global scale. And so to start this stage, I wanna talk a little bit
about what machine learning is and what AutoML is,
automated machine learning and why the demands of time series are fundamentally different. So machine learning is being able to predict future results
based on past occurrences and understand why things are happening so that you can take a corrective action. And what automated machine
learning is taking a lot of the time-consuming tasks,
whether data preparation, feature engineering, ML
selection, ModelOps, and more so that you can deploy these at scale where they're needed for the business. Time series modeling is the
subset of machine learning where you're looking at forecasting on a continuous time window. Let me give you an example
of why this is needed. If we think about retail,
retail is a really good example and we work with retail
companies worldwide. In retail you have
products, you have SKUs, you have customers, you have
locations, you have online, you have retail, you have a multitude of different factors that are impacting your business
every day and in real time. This leads to a web of
exponential dependencies where one factor is actually
in fact impacting another. This leads to billions of interactions. And traditionally, a
lot of the forecasting has been univariate. And what this means is looking
at one historical variable to forecast a future result. But as mentioned, in reality,
businesses are complex, they're dynamic, there are thousands of different interactions
from channels to products. Even weather has a large
impact on business operations. And each added input leads to a multiplying effect of complexity. And this is why we need
multivariate time series, the ability to capture all
these different signals to create an accurate, actionable forecast where you can run your business. But this also leads to a
massive compute challenge, billions of potential interactions. And so today, this is why
we're happy to announce and talk about our multivariate
time series capability with AWS partnership that's based on GPUs and elastic just-in-time compute at scale. - All right, so why AWS? When Qlik was looking
to build this platform, they just didn't want, you
know, any cloud platform. They were looking for someone
who can help them scale and build enterprise, you know, models serving 40,000 customers
that they have today. There were three key things
that Qlik was looking at. Number one, you know, global
scale with data sovereignty. Today AWS has, I believe, 38 regions and three more coming up, and I probably will
stand corrected tomorrow when Matt Garman speaks and
maybe he'll announce a few more. But AWS has the global scale, which can serve Qlik's customers
in 100 different countries. Also, data sovereignty. As you're aware, you know,
with GDPR and other compliance, data needs to reside in that country. So AWS provides, you
know, the global scale, as well as data sovereignty
for building the application. Second, we talked about GPU scaling. GPUs are expensive, so you
need to be able to scale, as well as control the costs. So you need to be able to
scale down to zero as required. Third, we're looking at
enterprise-grade reliability. You know, when customers are
running these applications, they're mission-critical applications. They need a platform that needs to be up and running 99.9% of the time. Not only that, they also want
to have the right, you know, high availability,
disaster recovery in place for running these
mission-critical applications. Now let's take a quick
look at the architecture for Qlik Predict. Qlik Predict is a completely
cloud native application built on AWS. The three core components
that we've looked at is, you know, we have GPU clusters, we have regional training
models that we are using, as well as we have, you know,
scale-to-zero architecture to keep the costs low. Also, we have used several native services like Amazon MQ, we have Amazon S3, RDS. Also for realtime integration, we've leveraged webhooks and AWS Lambda. Sean, you wanna take us into this architecture, do a deep dive? - Well, what is so
amazing is that with AWS, we're able to take this to scale and make it a reality, these complex algorithms
that are necessary for these billions of
interactions in real time for our customers. We're talking about deep
neural architectures, GPU acceleration, elastic
compute at the reliability, the scalability, and with
the security requirements that our customer needs. And this is what AWS can deliver, which is forecasting for the real world. The compute demands are
enormous, learning relationships across thousands of variables,
thousands of signals that impact businesses
every day from supply chain to demand, seasonality,
the temporal patterns, the cross-correlation,
really looking at things in a systematic way, a holistic way that is more representative of a business. And to work with these
deep recurrent networks where the combination explode,
we need the GPU power. And that was so exciting
about working with Amazon to have these GPUs that can really do this in the speed that's necessary for the businesses to take action. It all starts with the API gateway where when a request is
routed, it can be routed to the correct region across the world where it's needed within its boundary so that it can meet the data sovereignty and regulations for
each particular region. The heavy lifting with EKS and Karpenter allows for
that just-in-time scaling of these workloads, being able to scale up to these massive demands when needed. And the GPU EC2 instances can be tuned for different neural workloads,
depending on the use case. And so together it's a
globally distributed, GPU-accelerated SaaS
capability, one SaaS capability for each region worldwide. - All right, that's great, Sean. So let's talk about the real
impact of building on AWS, you know, speed to market. You know, when Qlik was
building this platform, they didn't have to worry about, you know, building their infrastructure. Leveraging AWS's managed services, you know, they were training their models where competitors were
still trying to figure out how to set up their environment. That's the key over there. Scale, today Qlik runs
100,000 plus training jobs on a monthly basis. That's literally 3,300 jobs a day. So they have the scale
today to, you know, process and train the models. Third, let's look at, you
know, cost efficiency. Using Karpenter, as Sean mentioned, along with spot instances,
you can control your cost, you can bring down your
cost 60 to 70%, you know, leveraging a scale-to-zero architecture along with spot instances so that it doesn't become very expensive. Also look at, you know, regionality. You know, with the 38 regions
that we have today, you know, Qlik could easily expand to any new region to serve their customers and did not have to spend
a lot of time, you know, building their infrastructure over there. And finally is reliability. You know, leveraging,
as I mentioned, HADR, intelligent workload balancing,
you can take care of, you know, availability
of your application, see to it it's up and running - And so the results are amazing. Just looking at our telemetry, currently we have over 4,500
active users on Qlik Predict generating over 167,000 trained models and 1.5 billion predictions to date, all of this with over 99.99% uptime. And with our GPUs versus a CPU equivalent, we're able to run our training
jobs up to nine times faster. But I would really like
to talk about outcomes because it's the actual tangible business outcomes that matter. We of course work with
industries all across the world, from financial services,
healthcare, retail and more. I'd like to just share
a couple examples today. One with Appalachian Regional Healthcare, a hospital network
based on the East Coast, they're able to reduce
their patient no-shows, their patient cancellation rates, saving over $6 million a year. With Qlik Predict, what they're able to do is
not only be able to predict and understand why a
patient is going to cancel, but take the corrective action so that they can not only get the patient to show up when they need to, but also have better patient outcomes. In financial services, Integra Financial is a really good example of integrating this into
an external workflow with a real-time API for
automated lead scoring, which has led to today over $1
million in automated savings. And Village Roadshow,
which is an entertainment and hospitality group in
the Asia-Pacific region. They have very complex business operations with staffing, customers and more, and they were able to use Qlik
Predict to forecast demand and staffing for faster
data-driven decisions. - Thanks, Sean. All right, so what is
the key takeaway here? You know, building
enterprise-level machine learning SaaS platform isn't something
that is in the future. This is happening today. Qlik has built Predict platform, which is serving, you know, multiple enterprise-level customers. They are doing millions of predictions and saving customers, you
know, millions of dollars for the sales forecasting at this point. The three core things that
I want, you know, everybody to learn from this, you know,
number one is scale by design. You know, multi-tenancy isn't something that you can retrofit. It is expensive, as well
as, you know, risky. So think about multi-tenancy when you're building the
application from day one. Second, you know, is telemetry,
you know, and observability. See to it that you integrate observability in your application from day one. You know, when you're
running 100,000 jobs, your customers want to
have the transparency and see what is under the hood. So leverage like CloudWatch,
for example, to see to it that the customers have
the full visibility into the application that is running. And then finally, you know,
machine learning applications, they cannot run in silos. You know, integration is everything. See to it that you can
integrate your applications, along with your workflows so that you can derive
the maximum benefits. You can use APIs, you can use webhooks, you can use Lambda
event-driven architecture. You know, AWS has a lot of services that can help you do that. So leverage, like for
example, EventBridge. I mean, this will help you
integrate your application and not run in silos to get the maximum
business value out of it. All right, so this is an excellent example where you've seen how Qlik
and AWS work together. You know, we had a strategic
collaboration agreement. We leveraged Qlik's domain expertise with AWS's global infrastructure to make Qlik Predict happen, which is saving customers
millions of dollars doing, you know, sales, financial, even operations predictions at this point. Qlik Predict is also
available on AWS Marketplace. I encourage all of you guys to, you know, take a look at it and you can
see it actually up and running where you can build a machine learning job with absolutely like very little code. You can take the maximum use of the machine learning models over there. - All right, Sean, do you wanna? - Yeah, and so really thanks for having this conversation today. Please come visit us at our booth, 1727. Happy to talk about our journey in building this architecture. We have some engineers here as well to talk about their experiences
and also your challenges and aspirations around machine learning and multivariate time series. And so really happy to be here today. - Thanks, Sean, my name is Vin and I'll be around if you
guys have any questions. More than happy to answer them.
Thank you, enjoy re:Invent.

## Subtitles with Timestamps

[00:01](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1s) - All right, welcome to re:Invent.

[00:04](https://www.youtube.com/watch?v=flGdaoQsXc4&t=4s) Are you guys all excited?

[00:06](https://www.youtube.com/watch?v=flGdaoQsXc4&t=6s) We have... All right, I
like that spirit over there.

[00:10](https://www.youtube.com/watch?v=flGdaoQsXc4&t=10s) I guess we have over 2,000 sessions

[00:12](https://www.youtube.com/watch?v=flGdaoQsXc4&t=12s) and workshops lined up this week,

[00:14](https://www.youtube.com/watch?v=flGdaoQsXc4&t=14s) so make the most out of it.

[00:17](https://www.youtube.com/watch?v=flGdaoQsXc4&t=17s) Any first timers over here for re:Invent?

[00:20](https://www.youtube.com/watch?v=flGdaoQsXc4&t=20s) All right, that's great.

[00:22](https://www.youtube.com/watch?v=flGdaoQsXc4&t=22s) I'm going to recommend to install

[00:25](https://www.youtube.com/watch?v=flGdaoQsXc4&t=25s) or activate your pedometer on your phone.

[00:28](https://www.youtube.com/watch?v=flGdaoQsXc4&t=28s) Count the number of steps
you're gonna walk this week,

[00:30](https://www.youtube.com/watch?v=flGdaoQsXc4&t=30s) and then I'm telling you,

[00:31](https://www.youtube.com/watch?v=flGdaoQsXc4&t=31s) you're gonna be pleasantly surprised.

[00:35](https://www.youtube.com/watch?v=flGdaoQsXc4&t=35s) A warm welcome to this
presentation. My name is Vin Dahake.

[00:40](https://www.youtube.com/watch?v=flGdaoQsXc4&t=40s) I lead solutions architect
team for ISV Private Equity.

[00:45](https://www.youtube.com/watch?v=flGdaoQsXc4&t=45s) I've been with AWS for five years now

[00:47](https://www.youtube.com/watch?v=flGdaoQsXc4&t=47s) and I'm based out of New York City.

[00:50](https://www.youtube.com/watch?v=flGdaoQsXc4&t=50s) Gonna let my partner introduce himself.

[00:52](https://www.youtube.com/watch?v=flGdaoQsXc4&t=52s) - Yeah, and thank you, Vin.
Really a pleasure to be here.

[00:54](https://www.youtube.com/watch?v=flGdaoQsXc4&t=54s) My name is Sean Stauth.

[00:55](https://www.youtube.com/watch?v=flGdaoQsXc4&t=55s) I'm Global Director of AI
and Machine Learning at Qlik,

[00:58](https://www.youtube.com/watch?v=flGdaoQsXc4&t=58s) and I have the opportunity to work

[01:00](https://www.youtube.com/watch?v=flGdaoQsXc4&t=60s) with our customers worldwide in a variety

[01:02](https://www.youtube.com/watch?v=flGdaoQsXc4&t=62s) of different industries
on their cutting-edge AI

[01:05](https://www.youtube.com/watch?v=flGdaoQsXc4&t=65s) and machine learning solutions.

[01:08](https://www.youtube.com/watch?v=flGdaoQsXc4&t=68s) - All right, thanks, Sean.

[01:10](https://www.youtube.com/watch?v=flGdaoQsXc4&t=70s) - All right, before we
get started, you know,

[01:12](https://www.youtube.com/watch?v=flGdaoQsXc4&t=72s) a quick show of hands,

[01:13](https://www.youtube.com/watch?v=flGdaoQsXc4&t=73s) how many of you have built
machine learning applications,

[01:18](https://www.youtube.com/watch?v=flGdaoQsXc4&t=78s) analytics applications that have worked

[01:21](https://www.youtube.com/watch?v=flGdaoQsXc4&t=81s) for the first time in production?

[01:24](https://www.youtube.com/watch?v=flGdaoQsXc4&t=84s) Oh, that's good. That's good.

[01:26](https://www.youtube.com/watch?v=flGdaoQsXc4&t=86s) We have few hands up
over here. It's not easy.

[01:29](https://www.youtube.com/watch?v=flGdaoQsXc4&t=89s) I mean, I was hoping everybody
would raise their hand

[01:32](https://www.youtube.com/watch?v=flGdaoQsXc4&t=92s) and I would just walk
off from the stage away,

[01:33](https://www.youtube.com/watch?v=flGdaoQsXc4&t=93s) say thank you very much, but
this is the reason we are here.

[01:38](https://www.youtube.com/watch?v=flGdaoQsXc4&t=98s) You know, building
machine learning platforms

[01:41](https://www.youtube.com/watch?v=flGdaoQsXc4&t=101s) which are enterprise ready,
scalable is not easy.

[01:45](https://www.youtube.com/watch?v=flGdaoQsXc4&t=105s) And that's why we have Qlik
at our doorsteps today.

[01:48](https://www.youtube.com/watch?v=flGdaoQsXc4&t=108s) But before we get started,

[01:50](https://www.youtube.com/watch?v=flGdaoQsXc4&t=110s) let me tell you a little bit about Qlik.

[01:53](https://www.youtube.com/watch?v=flGdaoQsXc4&t=113s) Qlik has been a global leader

[01:56](https://www.youtube.com/watch?v=flGdaoQsXc4&t=116s) for the last 30 years
in data analytics space.

[02:00](https://www.youtube.com/watch?v=flGdaoQsXc4&t=120s) They have helped companies,
you know, transform

[02:04](https://www.youtube.com/watch?v=flGdaoQsXc4&t=124s) by processing data, getting
insights from the data.

[02:10](https://www.youtube.com/watch?v=flGdaoQsXc4&t=130s) Qlik has three core
expertise that we are seeing.

[02:13](https://www.youtube.com/watch?v=flGdaoQsXc4&t=133s) They've done a lot of work in
real-time data integration.

[02:18](https://www.youtube.com/watch?v=flGdaoQsXc4&t=138s) They've done work in analytics,
business intelligence,

[02:21](https://www.youtube.com/watch?v=flGdaoQsXc4&t=141s) visualization, and
third, AI, ML and AutoML.

[02:27](https://www.youtube.com/watch?v=flGdaoQsXc4&t=147s) And that's the reason we're here

[02:29](https://www.youtube.com/watch?v=flGdaoQsXc4&t=149s) to discuss about Qlik Predict.

[02:31](https://www.youtube.com/watch?v=flGdaoQsXc4&t=151s) Today Qlik has over 40,000 customers

[02:34](https://www.youtube.com/watch?v=flGdaoQsXc4&t=154s) across 100 different countries.

[02:38](https://www.youtube.com/watch?v=flGdaoQsXc4&t=158s) And in 2004, AWS and Qlik,

[02:42](https://www.youtube.com/watch?v=flGdaoQsXc4&t=162s) we signed a strategic
collaboration agreement.

[02:45](https://www.youtube.com/watch?v=flGdaoQsXc4&t=165s) And I'm excited to tell you the result

[02:48](https://www.youtube.com/watch?v=flGdaoQsXc4&t=168s) of this agreement is Qlik Predict.

[02:50](https://www.youtube.com/watch?v=flGdaoQsXc4&t=170s) This is a fully managed multi-tenant,

[02:54](https://www.youtube.com/watch?v=flGdaoQsXc4&t=174s) global machine learning SaaS platform,

[02:56](https://www.youtube.com/watch?v=flGdaoQsXc4&t=176s) which is entirely built on AWS.

[03:03](https://www.youtube.com/watch?v=flGdaoQsXc4&t=183s) All right, let's take a quick
look at the agenda over here.

[03:05](https://www.youtube.com/watch?v=flGdaoQsXc4&t=185s) You know, we will talk about

[03:07](https://www.youtube.com/watch?v=flGdaoQsXc4&t=187s) what this machine learning
predictive analytics platform is.

[03:11](https://www.youtube.com/watch?v=flGdaoQsXc4&t=191s) We will do a deep dive
into the architecture.

[03:14](https://www.youtube.com/watch?v=flGdaoQsXc4&t=194s) We will look at, you know,
some of the case studies

[03:18](https://www.youtube.com/watch?v=flGdaoQsXc4&t=198s) and then we'll talk about
the challenges that we faced

[03:20](https://www.youtube.com/watch?v=flGdaoQsXc4&t=200s) and how we can learn from that.

[03:31](https://www.youtube.com/watch?v=flGdaoQsXc4&t=211s) 70% of forecasting programs fail.

[03:36](https://www.youtube.com/watch?v=flGdaoQsXc4&t=216s) Really, 70%.

[03:39](https://www.youtube.com/watch?v=flGdaoQsXc4&t=219s) This is not an academic study.

[03:41](https://www.youtube.com/watch?v=flGdaoQsXc4&t=221s) This is, you know, real money,
real business, you know,

[03:44](https://www.youtube.com/watch?v=flGdaoQsXc4&t=224s) real challenges that people face.

[03:48](https://www.youtube.com/watch?v=flGdaoQsXc4&t=228s) Most of the traditional
forecasting programs fail

[03:53](https://www.youtube.com/watch?v=flGdaoQsXc4&t=233s) because, you know, they
look at data in isolation.

[03:57](https://www.youtube.com/watch?v=flGdaoQsXc4&t=237s) You know, that's not how real world is.

[04:01](https://www.youtube.com/watch?v=flGdaoQsXc4&t=241s) We have seen, you know,
when programs are doing,

[04:06](https://www.youtube.com/watch?v=flGdaoQsXc4&t=246s) let's say, for example, sales forecasting,

[04:08](https://www.youtube.com/watch?v=flGdaoQsXc4&t=248s) they look at okay, what was
my sales data for last month?

[04:12](https://www.youtube.com/watch?v=flGdaoQsXc4&t=252s) It was X so maybe next
month is X plus delta.

[04:15](https://www.youtube.com/watch?v=flGdaoQsXc4&t=255s) But that's not how it works in reality.

[04:20](https://www.youtube.com/watch?v=flGdaoQsXc4&t=260s) There are multiple variables

[04:22](https://www.youtube.com/watch?v=flGdaoQsXc4&t=262s) that need to be taken into consideration,

[04:25](https://www.youtube.com/watch?v=flGdaoQsXc4&t=265s) you know, when you're doing forecasting.

[04:26](https://www.youtube.com/watch?v=flGdaoQsXc4&t=266s) It could be seasonality,
it is your inventory,

[04:29](https://www.youtube.com/watch?v=flGdaoQsXc4&t=269s) economic conditions, it could
be your competitor's action.

[04:32](https://www.youtube.com/watch?v=flGdaoQsXc4&t=272s) There are multiple factors.

[04:34](https://www.youtube.com/watch?v=flGdaoQsXc4&t=274s) As a matter of fact, there could be up

[04:35](https://www.youtube.com/watch?v=flGdaoQsXc4&t=275s) to 50 different factors that
can impact your forecasting.

[04:40](https://www.youtube.com/watch?v=flGdaoQsXc4&t=280s) You know, simple models
probably can look at seasonality

[04:44](https://www.youtube.com/watch?v=flGdaoQsXc4&t=284s) and make predictions,

[04:45](https://www.youtube.com/watch?v=flGdaoQsXc4&t=285s) but for this particular case,

[04:47](https://www.youtube.com/watch?v=flGdaoQsXc4&t=287s) when we have 50 plus different variables

[04:50](https://www.youtube.com/watch?v=flGdaoQsXc4&t=290s) which interact with each other,

[04:52](https://www.youtube.com/watch?v=flGdaoQsXc4&t=292s) we need complex, advanced algorithms

[04:55](https://www.youtube.com/watch?v=flGdaoQsXc4&t=295s) like encoder-decoder, perceptron,

[04:58](https://www.youtube.com/watch?v=flGdaoQsXc4&t=298s) or recurrent neural networks
to do the forecasting.

[05:01](https://www.youtube.com/watch?v=flGdaoQsXc4&t=301s) These models are very
computationally intensive

[05:05](https://www.youtube.com/watch?v=flGdaoQsXc4&t=305s) and they need GPUs to, you
know, perform the calculations.

[05:09](https://www.youtube.com/watch?v=flGdaoQsXc4&t=309s) As I mentioned, you know,
we've worked with Qlik

[05:12](https://www.youtube.com/watch?v=flGdaoQsXc4&t=312s) and we formed this strategic
collaboration agreement

[05:14](https://www.youtube.com/watch?v=flGdaoQsXc4&t=314s) and I'm happy, the result of
that was building Qlik Predict.

[05:19](https://www.youtube.com/watch?v=flGdaoQsXc4&t=319s) Sean, you wanna share a
little bit more story?

[05:21](https://www.youtube.com/watch?v=flGdaoQsXc4&t=321s) - Yeah, yeah, and thank you
because as VIN mentioned,

[05:24](https://www.youtube.com/watch?v=flGdaoQsXc4&t=324s) this opportunity is massive

[05:25](https://www.youtube.com/watch?v=flGdaoQsXc4&t=325s) and with machine learning,

[05:27](https://www.youtube.com/watch?v=flGdaoQsXc4&t=327s) real companies are getting massive results

[05:29](https://www.youtube.com/watch?v=flGdaoQsXc4&t=329s) around their supply
chains, their logistics,

[05:31](https://www.youtube.com/watch?v=flGdaoQsXc4&t=331s) around their HR and more.

[05:33](https://www.youtube.com/watch?v=flGdaoQsXc4&t=333s) And so to start to share a
quick story around a company

[05:35](https://www.youtube.com/watch?v=flGdaoQsXc4&t=335s) called Software Logistik
Artland or SLA in Germany.

[05:38](https://www.youtube.com/watch?v=flGdaoQsXc4&t=338s) They have a very complex
network of suppliers,

[05:41](https://www.youtube.com/watch?v=flGdaoQsXc4&t=341s) distributors, manufacturing that they have

[05:43](https://www.youtube.com/watch?v=flGdaoQsXc4&t=343s) to run on a daily basis

[05:45](https://www.youtube.com/watch?v=flGdaoQsXc4&t=345s) where even small changes in
their operations can lead

[05:48](https://www.youtube.com/watch?v=flGdaoQsXc4&t=348s) to massive impacts around
finances and staffing.

[05:52](https://www.youtube.com/watch?v=flGdaoQsXc4&t=352s) And so with Qlik Predict,

[05:53](https://www.youtube.com/watch?v=flGdaoQsXc4&t=353s) they're able to build a
forecasting capability

[05:56](https://www.youtube.com/watch?v=flGdaoQsXc4&t=356s) and able predict over with
90% accuracy the demand

[06:00](https://www.youtube.com/watch?v=flGdaoQsXc4&t=360s) that they needed to
produce every single month.

[06:02](https://www.youtube.com/watch?v=flGdaoQsXc4&t=362s) And that led to a 50% reduction
in annual planning needs.

[06:09](https://www.youtube.com/watch?v=flGdaoQsXc4&t=369s) And the result is that while they're...

[06:12](https://www.youtube.com/watch?v=flGdaoQsXc4&t=372s) This is really complex, they
have a business that is dynamic

[06:15](https://www.youtube.com/watch?v=flGdaoQsXc4&t=375s) and they need a capability
that can match that reality.

[06:19](https://www.youtube.com/watch?v=flGdaoQsXc4&t=379s) And so today we're talking
about taking the next leap,

[06:21](https://www.youtube.com/watch?v=flGdaoQsXc4&t=381s) having a multivariate
forecasting capability

[06:25](https://www.youtube.com/watch?v=flGdaoQsXc4&t=385s) that can have smarter
forecasting at a global scale.

[06:31](https://www.youtube.com/watch?v=flGdaoQsXc4&t=391s) And so to start this stage,

[06:32](https://www.youtube.com/watch?v=flGdaoQsXc4&t=392s) I wanna talk a little bit
about what machine learning is

[06:35](https://www.youtube.com/watch?v=flGdaoQsXc4&t=395s) and what AutoML is,
automated machine learning

[06:38](https://www.youtube.com/watch?v=flGdaoQsXc4&t=398s) and why the demands of time series

[06:40](https://www.youtube.com/watch?v=flGdaoQsXc4&t=400s) are fundamentally different.

[06:41](https://www.youtube.com/watch?v=flGdaoQsXc4&t=401s) So machine learning is being able

[06:43](https://www.youtube.com/watch?v=flGdaoQsXc4&t=403s) to predict future results
based on past occurrences

[06:47](https://www.youtube.com/watch?v=flGdaoQsXc4&t=407s) and understand why things are happening

[06:49](https://www.youtube.com/watch?v=flGdaoQsXc4&t=409s) so that you can take a corrective action.

[06:52](https://www.youtube.com/watch?v=flGdaoQsXc4&t=412s) And what automated machine
learning is taking a lot

[06:55](https://www.youtube.com/watch?v=flGdaoQsXc4&t=415s) of the time-consuming tasks,
whether data preparation,

[06:58](https://www.youtube.com/watch?v=flGdaoQsXc4&t=418s) feature engineering, ML
selection, ModelOps, and more

[07:02](https://www.youtube.com/watch?v=flGdaoQsXc4&t=422s) so that you can deploy these at scale

[07:04](https://www.youtube.com/watch?v=flGdaoQsXc4&t=424s) where they're needed for the business.

[07:07](https://www.youtube.com/watch?v=flGdaoQsXc4&t=427s) Time series modeling is the
subset of machine learning

[07:10](https://www.youtube.com/watch?v=flGdaoQsXc4&t=430s) where you're looking at forecasting

[07:12](https://www.youtube.com/watch?v=flGdaoQsXc4&t=432s) on a continuous time window.

[07:15](https://www.youtube.com/watch?v=flGdaoQsXc4&t=435s) Let me give you an example
of why this is needed.

[07:17](https://www.youtube.com/watch?v=flGdaoQsXc4&t=437s) If we think about retail,
retail is a really good example

[07:20](https://www.youtube.com/watch?v=flGdaoQsXc4&t=440s) and we work with retail
companies worldwide.

[07:22](https://www.youtube.com/watch?v=flGdaoQsXc4&t=442s) In retail you have
products, you have SKUs,

[07:25](https://www.youtube.com/watch?v=flGdaoQsXc4&t=445s) you have customers, you have
locations, you have online,

[07:28](https://www.youtube.com/watch?v=flGdaoQsXc4&t=448s) you have retail, you have a multitude

[07:31](https://www.youtube.com/watch?v=flGdaoQsXc4&t=451s) of different factors

[07:32](https://www.youtube.com/watch?v=flGdaoQsXc4&t=452s) that are impacting your business
every day and in real time.

[07:36](https://www.youtube.com/watch?v=flGdaoQsXc4&t=456s) This leads to a web of
exponential dependencies

[07:40](https://www.youtube.com/watch?v=flGdaoQsXc4&t=460s) where one factor is actually
in fact impacting another.

[07:43](https://www.youtube.com/watch?v=flGdaoQsXc4&t=463s) This leads to billions of interactions.

[07:49](https://www.youtube.com/watch?v=flGdaoQsXc4&t=469s) And traditionally, a
lot of the forecasting

[07:51](https://www.youtube.com/watch?v=flGdaoQsXc4&t=471s) has been univariate.

[07:53](https://www.youtube.com/watch?v=flGdaoQsXc4&t=473s) And what this means is looking
at one historical variable

[07:56](https://www.youtube.com/watch?v=flGdaoQsXc4&t=476s) to forecast a future result.

[07:58](https://www.youtube.com/watch?v=flGdaoQsXc4&t=478s) But as mentioned, in reality,
businesses are complex,

[08:01](https://www.youtube.com/watch?v=flGdaoQsXc4&t=481s) they're dynamic, there are thousands

[08:03](https://www.youtube.com/watch?v=flGdaoQsXc4&t=483s) of different interactions
from channels to products.

[08:06](https://www.youtube.com/watch?v=flGdaoQsXc4&t=486s) Even weather has a large
impact on business operations.

[08:11](https://www.youtube.com/watch?v=flGdaoQsXc4&t=491s) And each added input leads

[08:13](https://www.youtube.com/watch?v=flGdaoQsXc4&t=493s) to a multiplying effect of complexity.

[08:17](https://www.youtube.com/watch?v=flGdaoQsXc4&t=497s) And this is why we need
multivariate time series,

[08:20](https://www.youtube.com/watch?v=flGdaoQsXc4&t=500s) the ability to capture all
these different signals

[08:23](https://www.youtube.com/watch?v=flGdaoQsXc4&t=503s) to create an accurate, actionable forecast

[08:26](https://www.youtube.com/watch?v=flGdaoQsXc4&t=506s) where you can run your business.

[08:28](https://www.youtube.com/watch?v=flGdaoQsXc4&t=508s) But this also leads to a
massive compute challenge,

[08:33](https://www.youtube.com/watch?v=flGdaoQsXc4&t=513s) billions of potential interactions.

[08:35](https://www.youtube.com/watch?v=flGdaoQsXc4&t=515s) And so today, this is why
we're happy to announce

[08:38](https://www.youtube.com/watch?v=flGdaoQsXc4&t=518s) and talk about our multivariate
time series capability

[08:41](https://www.youtube.com/watch?v=flGdaoQsXc4&t=521s) with AWS partnership that's based on GPUs

[08:45](https://www.youtube.com/watch?v=flGdaoQsXc4&t=525s) and elastic just-in-time compute at scale.

[08:55](https://www.youtube.com/watch?v=flGdaoQsXc4&t=535s) - All right, so why AWS?

[08:58](https://www.youtube.com/watch?v=flGdaoQsXc4&t=538s) When Qlik was looking
to build this platform,

[09:00](https://www.youtube.com/watch?v=flGdaoQsXc4&t=540s) they just didn't want, you
know, any cloud platform.

[09:03](https://www.youtube.com/watch?v=flGdaoQsXc4&t=543s) They were looking for someone
who can help them scale

[09:07](https://www.youtube.com/watch?v=flGdaoQsXc4&t=547s) and build enterprise, you know, models

[09:12](https://www.youtube.com/watch?v=flGdaoQsXc4&t=552s) serving 40,000 customers
that they have today.

[09:16](https://www.youtube.com/watch?v=flGdaoQsXc4&t=556s) There were three key things
that Qlik was looking at.

[09:19](https://www.youtube.com/watch?v=flGdaoQsXc4&t=559s) Number one, you know, global
scale with data sovereignty.

[09:22](https://www.youtube.com/watch?v=flGdaoQsXc4&t=562s) Today AWS has, I believe, 38 regions

[09:26](https://www.youtube.com/watch?v=flGdaoQsXc4&t=566s) and three more coming up,

[09:28](https://www.youtube.com/watch?v=flGdaoQsXc4&t=568s) and I probably will
stand corrected tomorrow

[09:30](https://www.youtube.com/watch?v=flGdaoQsXc4&t=570s) when Matt Garman speaks and
maybe he'll announce a few more.

[09:33](https://www.youtube.com/watch?v=flGdaoQsXc4&t=573s) But AWS has the global scale,

[09:36](https://www.youtube.com/watch?v=flGdaoQsXc4&t=576s) which can serve Qlik's customers
in 100 different countries.

[09:41](https://www.youtube.com/watch?v=flGdaoQsXc4&t=581s) Also, data sovereignty.

[09:43](https://www.youtube.com/watch?v=flGdaoQsXc4&t=583s) As you're aware, you know,
with GDPR and other compliance,

[09:46](https://www.youtube.com/watch?v=flGdaoQsXc4&t=586s) data needs to reside in that country.

[09:48](https://www.youtube.com/watch?v=flGdaoQsXc4&t=588s) So AWS provides, you
know, the global scale,

[09:51](https://www.youtube.com/watch?v=flGdaoQsXc4&t=591s) as well as data sovereignty
for building the application.

[09:55](https://www.youtube.com/watch?v=flGdaoQsXc4&t=595s) Second, we talked about GPU scaling.

[09:57](https://www.youtube.com/watch?v=flGdaoQsXc4&t=597s) GPUs are expensive, so you
need to be able to scale,

[10:00](https://www.youtube.com/watch?v=flGdaoQsXc4&t=600s) as well as control the costs.

[10:02](https://www.youtube.com/watch?v=flGdaoQsXc4&t=602s) So you need to be able to
scale down to zero as required.

[10:07](https://www.youtube.com/watch?v=flGdaoQsXc4&t=607s) Third, we're looking at
enterprise-grade reliability.

[10:12](https://www.youtube.com/watch?v=flGdaoQsXc4&t=612s) You know, when customers are
running these applications,

[10:15](https://www.youtube.com/watch?v=flGdaoQsXc4&t=615s) they're mission-critical applications.

[10:17](https://www.youtube.com/watch?v=flGdaoQsXc4&t=617s) They need a platform that needs

[10:18](https://www.youtube.com/watch?v=flGdaoQsXc4&t=618s) to be up and running 99.9% of the time.

[10:23](https://www.youtube.com/watch?v=flGdaoQsXc4&t=623s) Not only that, they also want
to have the right, you know,

[10:27](https://www.youtube.com/watch?v=flGdaoQsXc4&t=627s) high availability,
disaster recovery in place

[10:31](https://www.youtube.com/watch?v=flGdaoQsXc4&t=631s) for running these
mission-critical applications.

[10:39](https://www.youtube.com/watch?v=flGdaoQsXc4&t=639s) Now let's take a quick
look at the architecture

[10:41](https://www.youtube.com/watch?v=flGdaoQsXc4&t=641s) for Qlik Predict.

[10:45](https://www.youtube.com/watch?v=flGdaoQsXc4&t=645s) Qlik Predict is a completely
cloud native application

[10:48](https://www.youtube.com/watch?v=flGdaoQsXc4&t=648s) built on AWS.

[10:50](https://www.youtube.com/watch?v=flGdaoQsXc4&t=650s) The three core components
that we've looked at

[10:53](https://www.youtube.com/watch?v=flGdaoQsXc4&t=653s) is, you know, we have GPU clusters,

[10:56](https://www.youtube.com/watch?v=flGdaoQsXc4&t=656s) we have regional training
models that we are using,

[11:00](https://www.youtube.com/watch?v=flGdaoQsXc4&t=660s) as well as we have, you know,
scale-to-zero architecture

[11:03](https://www.youtube.com/watch?v=flGdaoQsXc4&t=663s) to keep the costs low.

[11:05](https://www.youtube.com/watch?v=flGdaoQsXc4&t=665s) Also, we have used several native services

[11:10](https://www.youtube.com/watch?v=flGdaoQsXc4&t=670s) like Amazon MQ, we have Amazon S3, RDS.

[11:15](https://www.youtube.com/watch?v=flGdaoQsXc4&t=675s) Also for realtime integration,

[11:18](https://www.youtube.com/watch?v=flGdaoQsXc4&t=678s) we've leveraged webhooks and AWS Lambda.

[11:21](https://www.youtube.com/watch?v=flGdaoQsXc4&t=681s) Sean, you wanna take us

[11:22](https://www.youtube.com/watch?v=flGdaoQsXc4&t=682s) into this architecture, do a deep dive?

[11:24](https://www.youtube.com/watch?v=flGdaoQsXc4&t=684s) - Well, what is so
amazing is that with AWS,

[11:27](https://www.youtube.com/watch?v=flGdaoQsXc4&t=687s) we're able to take this to scale

[11:29](https://www.youtube.com/watch?v=flGdaoQsXc4&t=689s) and make it a reality,

[11:31](https://www.youtube.com/watch?v=flGdaoQsXc4&t=691s) these complex algorithms
that are necessary

[11:33](https://www.youtube.com/watch?v=flGdaoQsXc4&t=693s) for these billions of
interactions in real time

[11:36](https://www.youtube.com/watch?v=flGdaoQsXc4&t=696s) for our customers.

[11:37](https://www.youtube.com/watch?v=flGdaoQsXc4&t=697s) We're talking about deep
neural architectures,

[11:39](https://www.youtube.com/watch?v=flGdaoQsXc4&t=699s) GPU acceleration, elastic
compute at the reliability,

[11:43](https://www.youtube.com/watch?v=flGdaoQsXc4&t=703s) the scalability, and with
the security requirements

[11:45](https://www.youtube.com/watch?v=flGdaoQsXc4&t=705s) that our customer needs.

[11:47](https://www.youtube.com/watch?v=flGdaoQsXc4&t=707s) And this is what AWS can deliver,

[11:50](https://www.youtube.com/watch?v=flGdaoQsXc4&t=710s) which is forecasting for the real world.

[11:53](https://www.youtube.com/watch?v=flGdaoQsXc4&t=713s) The compute demands are
enormous, learning relationships

[11:57](https://www.youtube.com/watch?v=flGdaoQsXc4&t=717s) across thousands of variables,
thousands of signals

[12:01](https://www.youtube.com/watch?v=flGdaoQsXc4&t=721s) that impact businesses
every day from supply chain

[12:04](https://www.youtube.com/watch?v=flGdaoQsXc4&t=724s) to demand, seasonality,
the temporal patterns,

[12:08](https://www.youtube.com/watch?v=flGdaoQsXc4&t=728s) the cross-correlation,
really looking at things

[12:11](https://www.youtube.com/watch?v=flGdaoQsXc4&t=731s) in a systematic way, a holistic way

[12:14](https://www.youtube.com/watch?v=flGdaoQsXc4&t=734s) that is more representative of a business.

[12:16](https://www.youtube.com/watch?v=flGdaoQsXc4&t=736s) And to work with these
deep recurrent networks

[12:19](https://www.youtube.com/watch?v=flGdaoQsXc4&t=739s) where the combination explode,
we need the GPU power.

[12:23](https://www.youtube.com/watch?v=flGdaoQsXc4&t=743s) And that was so exciting
about working with Amazon

[12:25](https://www.youtube.com/watch?v=flGdaoQsXc4&t=745s) to have these GPUs that can really do this

[12:28](https://www.youtube.com/watch?v=flGdaoQsXc4&t=748s) in the speed that's necessary

[12:30](https://www.youtube.com/watch?v=flGdaoQsXc4&t=750s) for the businesses to take action.

[12:33](https://www.youtube.com/watch?v=flGdaoQsXc4&t=753s) It all starts with the API gateway

[12:35](https://www.youtube.com/watch?v=flGdaoQsXc4&t=755s) where when a request is
routed, it can be routed

[12:38](https://www.youtube.com/watch?v=flGdaoQsXc4&t=758s) to the correct region across the world

[12:40](https://www.youtube.com/watch?v=flGdaoQsXc4&t=760s) where it's needed within its boundary

[12:42](https://www.youtube.com/watch?v=flGdaoQsXc4&t=762s) so that it can meet the data sovereignty

[12:45](https://www.youtube.com/watch?v=flGdaoQsXc4&t=765s) and regulations for
each particular region.

[12:48](https://www.youtube.com/watch?v=flGdaoQsXc4&t=768s) The heavy lifting with EKS

[12:50](https://www.youtube.com/watch?v=flGdaoQsXc4&t=770s) and Karpenter allows for
that just-in-time scaling

[12:55](https://www.youtube.com/watch?v=flGdaoQsXc4&t=775s) of these workloads, being able to scale up

[12:57](https://www.youtube.com/watch?v=flGdaoQsXc4&t=777s) to these massive demands when needed.

[13:01](https://www.youtube.com/watch?v=flGdaoQsXc4&t=781s) And the GPU EC2 instances can be tuned

[13:04](https://www.youtube.com/watch?v=flGdaoQsXc4&t=784s) for different neural workloads,
depending on the use case.

[13:09](https://www.youtube.com/watch?v=flGdaoQsXc4&t=789s) And so together it's a
globally distributed,

[13:11](https://www.youtube.com/watch?v=flGdaoQsXc4&t=791s) GPU-accelerated SaaS
capability, one SaaS capability

[13:16](https://www.youtube.com/watch?v=flGdaoQsXc4&t=796s) for each region worldwide.

[13:19](https://www.youtube.com/watch?v=flGdaoQsXc4&t=799s) - All right, that's great, Sean.

[13:21](https://www.youtube.com/watch?v=flGdaoQsXc4&t=801s) So let's talk about the real
impact of building on AWS,

[13:25](https://www.youtube.com/watch?v=flGdaoQsXc4&t=805s) you know, speed to market.

[13:27](https://www.youtube.com/watch?v=flGdaoQsXc4&t=807s) You know, when Qlik was
building this platform,

[13:29](https://www.youtube.com/watch?v=flGdaoQsXc4&t=809s) they didn't have to worry about, you know,

[13:30](https://www.youtube.com/watch?v=flGdaoQsXc4&t=810s) building their infrastructure.

[13:32](https://www.youtube.com/watch?v=flGdaoQsXc4&t=812s) Leveraging AWS's managed services,

[13:35](https://www.youtube.com/watch?v=flGdaoQsXc4&t=815s) you know, they were training their models

[13:37](https://www.youtube.com/watch?v=flGdaoQsXc4&t=817s) where competitors were
still trying to figure out

[13:39](https://www.youtube.com/watch?v=flGdaoQsXc4&t=819s) how to set up their environment.

[13:41](https://www.youtube.com/watch?v=flGdaoQsXc4&t=821s) That's the key over there.

[13:42](https://www.youtube.com/watch?v=flGdaoQsXc4&t=822s) Scale, today Qlik runs
100,000 plus training jobs

[13:49](https://www.youtube.com/watch?v=flGdaoQsXc4&t=829s) on a monthly basis.

[13:50](https://www.youtube.com/watch?v=flGdaoQsXc4&t=830s) That's literally 3,300 jobs a day.

[13:53](https://www.youtube.com/watch?v=flGdaoQsXc4&t=833s) So they have the scale
today to, you know, process

[13:57](https://www.youtube.com/watch?v=flGdaoQsXc4&t=837s) and train the models.

[13:59](https://www.youtube.com/watch?v=flGdaoQsXc4&t=839s) Third, let's look at, you
know, cost efficiency.

[14:04](https://www.youtube.com/watch?v=flGdaoQsXc4&t=844s) Using Karpenter, as Sean mentioned,

[14:08](https://www.youtube.com/watch?v=flGdaoQsXc4&t=848s) along with spot instances,
you can control your cost,

[14:11](https://www.youtube.com/watch?v=flGdaoQsXc4&t=851s) you can bring down your
cost 60 to 70%, you know,

[14:14](https://www.youtube.com/watch?v=flGdaoQsXc4&t=854s) leveraging a scale-to-zero architecture

[14:17](https://www.youtube.com/watch?v=flGdaoQsXc4&t=857s) along with spot instances

[14:19](https://www.youtube.com/watch?v=flGdaoQsXc4&t=859s) so that it doesn't become very expensive.

[14:21](https://www.youtube.com/watch?v=flGdaoQsXc4&t=861s) Also look at, you know, regionality.

[14:25](https://www.youtube.com/watch?v=flGdaoQsXc4&t=865s) You know, with the 38 regions
that we have today, you know,

[14:28](https://www.youtube.com/watch?v=flGdaoQsXc4&t=868s) Qlik could easily expand to any new region

[14:31](https://www.youtube.com/watch?v=flGdaoQsXc4&t=871s) to serve their customers

[14:32](https://www.youtube.com/watch?v=flGdaoQsXc4&t=872s) and did not have to spend
a lot of time, you know,

[14:35](https://www.youtube.com/watch?v=flGdaoQsXc4&t=875s) building their infrastructure over there.

[14:38](https://www.youtube.com/watch?v=flGdaoQsXc4&t=878s) And finally is reliability.

[14:40](https://www.youtube.com/watch?v=flGdaoQsXc4&t=880s) You know, leveraging,
as I mentioned, HADR,

[14:45](https://www.youtube.com/watch?v=flGdaoQsXc4&t=885s) intelligent workload balancing,
you can take care of,

[14:48](https://www.youtube.com/watch?v=flGdaoQsXc4&t=888s) you know, availability
of your application,

[14:50](https://www.youtube.com/watch?v=flGdaoQsXc4&t=890s) see to it it's up and running

[14:57](https://www.youtube.com/watch?v=flGdaoQsXc4&t=897s) - And so the results are amazing.

[14:59](https://www.youtube.com/watch?v=flGdaoQsXc4&t=899s) Just looking at our telemetry,

[15:00](https://www.youtube.com/watch?v=flGdaoQsXc4&t=900s) currently we have over 4,500
active users on Qlik Predict

[15:05](https://www.youtube.com/watch?v=flGdaoQsXc4&t=905s) generating over 167,000 trained models

[15:10](https://www.youtube.com/watch?v=flGdaoQsXc4&t=910s) and 1.5 billion predictions to date,

[15:14](https://www.youtube.com/watch?v=flGdaoQsXc4&t=914s) all of this with over 99.99% uptime.

[15:18](https://www.youtube.com/watch?v=flGdaoQsXc4&t=918s) And with our GPUs versus a CPU equivalent,

[15:22](https://www.youtube.com/watch?v=flGdaoQsXc4&t=922s) we're able to run our training
jobs up to nine times faster.

[15:28](https://www.youtube.com/watch?v=flGdaoQsXc4&t=928s) But I would really like
to talk about outcomes

[15:31](https://www.youtube.com/watch?v=flGdaoQsXc4&t=931s) because it's the actual

[15:32](https://www.youtube.com/watch?v=flGdaoQsXc4&t=932s) tangible business outcomes that matter.

[15:35](https://www.youtube.com/watch?v=flGdaoQsXc4&t=935s) We of course work with
industries all across the world,

[15:38](https://www.youtube.com/watch?v=flGdaoQsXc4&t=938s) from financial services,
healthcare, retail and more.

[15:41](https://www.youtube.com/watch?v=flGdaoQsXc4&t=941s) I'd like to just share
a couple examples today.

[15:44](https://www.youtube.com/watch?v=flGdaoQsXc4&t=944s) One with Appalachian Regional Healthcare,

[15:46](https://www.youtube.com/watch?v=flGdaoQsXc4&t=946s) a hospital network
based on the East Coast,

[15:48](https://www.youtube.com/watch?v=flGdaoQsXc4&t=948s) they're able to reduce
their patient no-shows,

[15:50](https://www.youtube.com/watch?v=flGdaoQsXc4&t=950s) their patient cancellation rates,

[15:55](https://www.youtube.com/watch?v=flGdaoQsXc4&t=955s) saving over $6 million a year.

[15:58](https://www.youtube.com/watch?v=flGdaoQsXc4&t=958s) With Qlik Predict,

[16:00](https://www.youtube.com/watch?v=flGdaoQsXc4&t=960s) what they're able to do is
not only be able to predict

[16:02](https://www.youtube.com/watch?v=flGdaoQsXc4&t=962s) and understand why a
patient is going to cancel,

[16:05](https://www.youtube.com/watch?v=flGdaoQsXc4&t=965s) but take the corrective action

[16:06](https://www.youtube.com/watch?v=flGdaoQsXc4&t=966s) so that they can not only get the patient

[16:08](https://www.youtube.com/watch?v=flGdaoQsXc4&t=968s) to show up when they need to,

[16:09](https://www.youtube.com/watch?v=flGdaoQsXc4&t=969s) but also have better patient outcomes.

[16:12](https://www.youtube.com/watch?v=flGdaoQsXc4&t=972s) In financial services,

[16:13](https://www.youtube.com/watch?v=flGdaoQsXc4&t=973s) Integra Financial is a really good example

[16:15](https://www.youtube.com/watch?v=flGdaoQsXc4&t=975s) of integrating this into
an external workflow

[16:18](https://www.youtube.com/watch?v=flGdaoQsXc4&t=978s) with a real-time API for
automated lead scoring,

[16:21](https://www.youtube.com/watch?v=flGdaoQsXc4&t=981s) which has led to today over $1
million in automated savings.

[16:25](https://www.youtube.com/watch?v=flGdaoQsXc4&t=985s) And Village Roadshow,
which is an entertainment

[16:28](https://www.youtube.com/watch?v=flGdaoQsXc4&t=988s) and hospitality group in
the Asia-Pacific region.

[16:31](https://www.youtube.com/watch?v=flGdaoQsXc4&t=991s) They have very complex business operations

[16:35](https://www.youtube.com/watch?v=flGdaoQsXc4&t=995s) with staffing, customers and more,

[16:37](https://www.youtube.com/watch?v=flGdaoQsXc4&t=997s) and they were able to use Qlik
Predict to forecast demand

[16:41](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1001s) and staffing for faster
data-driven decisions.

[16:48](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1008s) - Thanks, Sean.

[16:50](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1010s) All right, so what is
the key takeaway here?

[16:56](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1016s) You know, building
enterprise-level machine learning

[16:59](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1019s) SaaS platform isn't something
that is in the future.

[17:03](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1023s) This is happening today.

[17:05](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1025s) Qlik has built Predict platform,

[17:07](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1027s) which is serving, you know,

[17:10](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1030s) multiple enterprise-level customers.

[17:14](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1034s) They are doing millions of predictions

[17:17](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1037s) and saving customers, you
know, millions of dollars

[17:20](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1040s) for the sales forecasting at this point.

[17:23](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1043s) The three core things that
I want, you know, everybody

[17:26](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1046s) to learn from this, you know,
number one is scale by design.

[17:29](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1049s) You know, multi-tenancy isn't something

[17:31](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1051s) that you can retrofit.

[17:33](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1053s) It is expensive, as well
as, you know, risky.

[17:36](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1056s) So think about multi-tenancy

[17:38](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1058s) when you're building the
application from day one.

[17:42](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1062s) Second, you know, is telemetry,
you know, and observability.

[17:46](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1066s) See to it that you integrate observability

[17:49](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1069s) in your application from day one.

[17:51](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1071s) You know, when you're
running 100,000 jobs,

[17:53](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1073s) your customers want to
have the transparency

[17:56](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1076s) and see what is under the hood.

[17:57](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1077s) So leverage like CloudWatch,
for example, to see to it

[18:01](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1081s) that the customers have
the full visibility

[18:04](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1084s) into the application that is running.

[18:06](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1086s) And then finally, you know,
machine learning applications,

[18:10](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1090s) they cannot run in silos.

[18:12](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1092s) You know, integration is everything.

[18:14](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1094s) See to it that you can
integrate your applications,

[18:19](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1099s) along with your workflows

[18:22](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1102s) so that you can derive
the maximum benefits.

[18:24](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1104s) You can use APIs, you can use webhooks,

[18:27](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1107s) you can use Lambda
event-driven architecture.

[18:30](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1110s) You know, AWS has a lot of services

[18:34](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1114s) that can help you do that.

[18:36](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1116s) So leverage, like for
example, EventBridge.

[18:39](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1119s) I mean, this will help you
integrate your application

[18:42](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1122s) and not run in silos

[18:43](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1123s) to get the maximum
business value out of it.

[18:49](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1129s) All right, so this is an excellent example

[18:53](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1133s) where you've seen how Qlik
and AWS work together.

[18:57](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1137s) You know, we had a strategic
collaboration agreement.

[18:59](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1139s) We leveraged Qlik's domain expertise

[19:02](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1142s) with AWS's global infrastructure

[19:04](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1144s) to make Qlik Predict happen,

[19:07](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1147s) which is saving customers
millions of dollars doing,

[19:10](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1150s) you know, sales, financial,

[19:12](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1152s) even operations predictions at this point.

[19:15](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1155s) Qlik Predict is also
available on AWS Marketplace.

[19:19](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1159s) I encourage all of you guys to, you know,

[19:22](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1162s) take a look at it and you can
see it actually up and running

[19:25](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1165s) where you can build a machine learning job

[19:27](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1167s) with absolutely like very little code.

[19:31](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1171s) You can take the maximum use

[19:33](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1173s) of the machine learning models over there.

[19:36](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1176s) - All right, Sean, do you wanna?

[19:37](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1177s) - Yeah, and so really thanks

[19:39](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1179s) for having this conversation today.

[19:41](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1181s) Please come visit us at our booth, 1727.

[19:44](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1184s) Happy to talk about our journey

[19:45](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1185s) in building this architecture.

[19:47](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1187s) We have some engineers here as well

[19:48](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1188s) to talk about their experiences
and also your challenges

[19:52](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1192s) and aspirations around machine learning

[19:54](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1194s) and multivariate time series.

[19:56](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1196s) And so really happy to be here today.

[19:58](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1198s) - Thanks, Sean, my name is Vin

[20:00](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1200s) and I'll be around if you
guys have any questions.

[20:03](https://www.youtube.com/watch?v=flGdaoQsXc4&t=1203s) More than happy to answer them.
Thank you, enjoy re:Invent.

