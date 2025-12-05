# AWS re:Invent 2021 - The architect elevator: Connecting IT and the boardroom

[Video Link](https://www.youtube.com/watch?v=nNbnXTl2VFQ)

## Description

Today’s successful systems architects forge a connection between an organization’s strategy, its technology choices, and its operational capabilities. Building executive awareness and securing buy-in requires you to communicate technical decisions and trade-offs clearly without confusing or lecturing your audience. This session prepares architects to “ride the elevator” between the IT engine room, where software is built, and the boardroom, where executive decisions are made. Learn from customer examples how developing a deeper understanding of a system’s architecture allows you to communicate clearly to a diverse set of stakeholders.

Learn more about re:Invent 2021 at https://bit.ly/3IvOLtK

Subscribe: 
More AWS videos http://bit.ly/2O3zS75 
More AWS events videos http://bit.ly/316g9t4

ABOUT AWS
Amazon Web Services (AWS) hosts events, both online and in-person, bringing the cloud computing community together to connect, collaborate, and learn from AWS experts.

AWS is the world’s most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally. Millions of customers—including the fastest-growing startups, largest enterprises, and leading government agencies—are using AWS to lower costs, become more agile, and innovate faster.

#AWS #AmazonWebServices #CloudComputing

## Transcript

(upbeat music) - This talk is about
architects and architecture. You might wonder whether it's
worth spending 45 minutes listening about roles and titles instead of hearing the
latest product features. I certainly believe so
because I am convinced that architects and
architecture play a central role in the success of any complex IT project and especially cloud projects and if that isn't convincing enough, software and cloud architects
are routinely ranked amongst the most sought after and highly compensated job roles. So, let's look at what it means to be a successful architect. We talk a lot about modern applications and system architectures. In fact, most of re:Invent
covers modern architectures, but I believe it's time
to not just upgrade our architectures, we also
need to upgrade our definition of what it means to be an architect and I can give you a hint, it's not about drawing YouMail diagrams or setting coding standards. As always at Amazon, we
like to work backwards. So we should think first about the values that the modern architect provides. So, which architect is most valuable? I have carried the
title of chief architect at a major financial services institution. Now did that make me the
most valuable architect? Or perhaps it should be the architect who knows the most design patterns or the one who has the most certifications or the one who is hands-on
with the development teams? Well, I am convinced
that in our modern world, the most valuable
architects are not the ones who carry a specific title or
have specific certifications. Instead, it's those who
can connect the most levels of the organization. Large organizations, and
many not so large ones, have many different layers and too often, they're disconnected. So the organization is playing
some sort of telephone game where the folks setting
the business strategy up in the penthouse have little idea about the technology and vice versa. So, it's easy to see that that
doesn't work terribly well. As an architect, if you're
up in the penthouse, but all you do is, you know, spool at words like agile or cloud-native, your impact is actually very small. I wouldn't even call
that being an architect. I might call you a parrot if
I want to be more poignant and I have met a lot
of parrots in my career and I have to say, I prefer
the ones who can fly. Likewise, if your world's
foremost helm chart expert and have written dozens
of Kubernetes operators, but you've never worked
on a project that provided real business value, you're
also not very valuable. It's the connection that
provides the most value. So, let me prove that to
you with an architecture. Architects like diagrams, so
here's an architecture diagram. It shows one of the most
fundamental architecture patterns, it's called layering. Layering divides the
system into multiple parts, such that any part only
depends on lower parts. I'm sure you've seen or
drawn a diagram like this. Now, why is this type of
architecture so popular? Well, because it has a number
of distinct advantages. Each layer does one thing, so it's a neat separation of concerns that abstracts away the details behind well-defined interfaces. For example, a lower layer
might deal with persistence, so that the upper layers
don't depend on the type of data store that's being used. Also, dependencies flow
nicely from top to bottom, meaning the application logic will depend on the persistence layer, but the persistence layer doesn't
depend on the application. It can be reused for
many other applications. Now this also means that the
data store can be replaced without impacting the
remainder of the application. Well, that's pretty cool,
you have to admit, right? Shouldn't we layer all applications then? Well, not quite so fast. Architecture is in the
business of trade-offs. So we should expect this architecture to also have downsides. Dividing a system into
layers can slow things down, perhaps, you know, the
ideal database optimization that you wanna do isn't available in the shared layer beneath and connecting the layers
also carries overhead, especially if you're using
a text-based data format like JSON or perhaps XML and if you have many, many layers, managing all the layers can become tedious and lead to teams
optimizing their own layer, but forgetting the end-to-end flow. Lastly, we have all seen how a
simple change in the UI layer requires an update in the
back and front-end layer, the application logic
layer, the API layer, the persistence layer and
in the data source schema. So such change propagation
also slows you down. Slowing down is not a good thing. Now you might wonder,
what does this have to do with the value that architects
bring to an organization? Well, actually quite a lot. All the benefits and
liabilities listed here don't just apply to technical systems, they also apply to organizations. Departments use well-defined interfaces, but are also prone to
optimizing locally, right? They make you take a number
and fill out endless forms or making a change
requires you to coordinate across 20 different teams. On the upshot, replaceability
can be a major benefit. We call this outsourcing. So what we are realizing is that, architectural thinking
applies equally well to technical and organizational systems and that means that you
as technical architects understand a lot more
about organizational design than you might've realized,
and that's perfect because you can't be a
successful architect these days without also influencing the organization and because that's such
a critical insight, let's dig a little deeper. What do the properties on
the left and on the right have in common when
compared with each other? As you will see, architects
are expected to see things that not everybody else sees. So if you look carefully,
you will find the properties on the left are largely structural. We talk about interfaces and abstraction. In contrast, the downsides on the right, they are largely behavioral. We talk about latency
and change propagation. So that gives us, as architects, a hint as to when layering is beneficial and when it can become a hindrance. If the rate of change is
slow or changes are local, then layering works well. When the rate of change increases or we're dealing with systemic changes, then it becomes a hindrance. Now, large organizations are
divided into many layers, right, from strategic planning to finance, accounting, payroll, manufacturing
and facility services and that used to work well for them when the business environment was stable. These days, we talk a lot
about digital disruption and transformation, the
environment keeps changing faster and all those layers are
now becoming a hindrance, but it's not easy to take layers out. That's why you need folks
to connect the layers and architects are best suited to do that. I call this riding the architect elevator. Instead of walking from floor to floor, you provide a fast
connection between the levels and in fact, I've written a
whole book that teaches you how to ride this architect elevator from the engine room to
the penthouse and back and this describes how
architects provide value at the different layers
and manage to connect them. Starting from the top,
architects need to make sure that business and IT
strategy are connected. If the two tunnels don't meet, nothing else will really help you. Second, you'll never be in an ideal state. Architects are also
expected to affect change. Complexity is your biggest enemy, you will need to minimize and tackle it. You do that by explaining
and de-mystifying. Don't make things more
complicated than they already are. Now down in the engine room, there's a ton of technical topics like building resilient
and scalable systems, agile delivery, automation,
and much, much more, but there's hundreds of other
sessions on those topics, so I'll only focus on the top half. There's one question though, that I often do get
from aspiring architects when I show the idea of
the architect elevator, and that is, will the folks up
in the penthouse welcome me? The answer is very simple, yes, they will. People who can translate
the technical details into meaningful insights
for the penthouse, without dumbing things down, are extremely rare and
highly sought after. If anything, your biggest problem might be that the folks in the penthouse don't want to let you get back
down into the engine room. So, let's have a look at how you can ride this architect elevator. To me, architect is not something that's written on your business card. Rather, it's really a way of thinking. The first thing that comes to mind when we consider what
architects do are diagrams. We could draw diagrams and that's good because diagrams are abstractions and they're the best
tools we have to manage the complexity we inherently face. Now, when we think about the
diagrams that architects draw, we usually think about boxes and lines, like the typical system
kind of architectures. However, if we compare this
with real-life architects, with famous architects
who design buildings, they do not draw blueprints. Rather, they make sketches. This is a sketch from Oscar Niemeyer, one of my favorite architects
who designed these buildings in the city of Brasilia in Brazil. Now, this is not a blueprint, there's a lot of detail that's missing, but most importantly,
it captures the essence. It expresses what the essential structure and property of the system is going to be and it incorporates the major
decisions and the context in which the system is going to be built and if you're wondering
whether this napkin sketch matches reality, you can be
assured that the real building matches the essence of this architecture. They are a lot of details to be filled in, a lot of blueprints to be drawn but the core decisions
and the core system image, so to speak, follow this
sketch of the architect. So first, learning about
how architects think is that architects don't
draw blueprints, they sketch. The second part of being an architect is to see more dimensions. You've surely been in
situations where people argue back and forth between,
are you going to do X or are you going to do Y? Should our code run in a container? Should we make it serverless? Do I need an API gateway? Do I need a service mesh? Do I need a document database
or do I need a graph database? And people can go back and
forth for very, very long time because they both believe they are right and it's just like in this picture where one person is very, very
sure that they see a circle while the other person is equally sure that they see a rectangle. Architects, our job is
to see more dimensions, to see the problems from
different points of view and show that both are right. They just need to look at things from their respective point of view. Once you show them the cylinder, they can have a much more
meaningful conversation. For example, people might argue that we need to speed up software delivery while others argue that we
need to improve quality. They each see one dimension and consider these properties
opposites of each other, but modern architects know
that test and build automation speed up delivery while
actually increasing quality. So, we see these as independent dimensions and know how to achieve both. Now, this is the second major part of thinking like an architect, we do stand to see more dimensions and not only do we see more dimensions, we're also good at zooming in
and zooming out of the system and this isn't like a camera
lens where you zoom in and you see the same thing
just a little bit bigger. It's much more like this Mandelbrot set where if you zoom in, you will
see very different things. Our world is also fractal. It covers things from
business architecture and business strategy to
high level architecture and then you go deep
down into the engine room to make sure you have the
right number of spaces in your YAML file and all
of those different levels of zooming in and zooming out
look very, very different. So, when we talk about what
it means to be an architect, you can see that it's a way of thinking. It's about sketching to express
the essence of something, that is about seeing more dimensions to allow folks to have
more meaningful discussions and it's about zooming in and zooming out to see different things. Now that we understand what
goes on in an architect's head, how do we articulate the
value that an architect and architecture bring? Most people, including
myself, would say that if your system is still running, if it's still running
well after several years and continues to absorb change, then it likely has a good architecture and perhaps a good architect behind it. But there should be a better metric for the value of architecture
than hindsight, we would say. Now I have found that
you can express the value of architects with this simple formula. Well, actually, you don't need
to understand the formula, the gentlemen, Fischer
Black and Myron Scholes, you know, got a Nobel Prize
in Economics for this one, which is known as the
Black-Scholes formula of options pricing. What you do need to understand though, is how architects provide options and why these options are valuable. Options are a way to defer decisions. In financial markets, these
options usually entitle you to purchase a share of
stock at a given date, for example, in one year, for
a set price, let's say $100. Now, the great thing about
having such an option is that in one year, the decision
whether to use that option becomes trivial, right? If the stock trades at more than $100, you use your option to buy at 100 and you have money in the bank. If the stock trades at below 100, well, you don't use the option,
it's optional after all. So, options defer a
decision into the future. So almost like time travel, in the future, you'll be smarter than today and you can make better decisions. So, it's not surprising that
these options have a value and Black and Scholes have
calculated that value. That's what this formula
is actually about. Now, as architects, we
can also create options to defer decisions and
that's how we provide value. Let's look at a simple
example of how this works in modern architectures. In classic IT, hardware sizing is one of the most
depressing activities, right? You have an application
and you need to estimate how much hardware is needed
to run this application well. Now, the reason it's depressing is because it leads to only
one of two possible outcomes. You either end up with too
much hardware and waste money or too little hardware and you end up with a poorly
performing application. Now as cloud architects, we know a great option
that we can provide, it's called a scale-out architecture, coupled with an elastic infrastructure. Now, you have the option
to add compute resources once you see the actual
application performance and you can easily see that this option has made the decision much simpler and allows you to make a better decision. Well, you can further increase
the value of this option if you break your application
into even smaller pieces, so you can scale individual
components, right? That'll be an even better option. Of course, that's exactly
what a serverless architecture allows you to do. Now, those are fantastic options to have. They defer a decision
about hardware sizing until you have more information, like the load of the application and as a result, you can
make a much better decision. Now, you might've noticed that I said architects sell options, I didn't say they're giving them away. Sometimes architects believe
that teams should use all their great ideas,
meaning their options, but they forget that those
options also have a cost and that cost comes in three main forms. First, implementing the option
requires some work, right? For example, you need to
decompose the application, wrap it into container,
automate deployment to spool up new instances. You know, second, the options tend to make your architecture slightly
more complex, right? Scaling out requires you
to have a load balancer and you have to manage and
replicate state as well. No one is ever looking
for more complexity, so this is an important cost to consider and last, options can
lead to under utilization. For example, if you
want to have the option to run your application in
many different environments, you might hesitate to use
all the services provided by one environment and that
might lead to an application that doesn't perform as well or one that takes longer to build. In either case, that's a very real cost. So, architects are in the
business of trade-offs. So we consider both the value
of an option and its cost. So when is it worth getting
this horizontal scaling options? You will find that the higher
the degree of uncertainty, the more valuable deferring
a decision becomes. That's intuitive because
if nothing ever changes, making the decision today is just as good as making it tomorrow. But if you're building
a mobile application that might have 100
users or 100,000 users, this scaling option
becomes highly valuable. So, we find that architecture
provides more value in uncertain times, and we
live in uncertain times, so architecture becomes more valuable. Now, we know another popular
method that also starts with A and that's called agile methods and oddly, architecture is sometimes seen as in conflict with being agile. You might've heard people say, oh, we don't need much
architecture because we're agile. Now, interestingly, agile methods also thrive on uncertainty. If you know everything upfront, you don't need to be agile, right? We just write it all
down and you code it out. So when you, as an
architect, meet somebody who prefers agile methods, you
can say, since you're agile, I'm guessing that you have
to deal with uncertainty and that's exactly what
architecture options do too. So when being agile, you should
invest in more architecture. Now that we understand
how architects think and how they provide value with options, it's time to get on the elevator, right? After all, we have some
connections to make, we need to connect the levels. We start on the top in
the corporate penthouse and up in the penthouse is usually a CIO, a chief information officer. In most organizations, IT
staff report to the CIO and the CIO is responsible
for the overall IT budget, but who does a CIO report to, right? That's actually a very good question. When you're up in the
organization's penthouse, you need to understand
what IT is measured by and you'll find that
the CIO's reporting line has a direct correlation to this. I blogged about this many years ago after visiting many
different organizations. For example, the CIO reporting into a CFO, the chief financial officer,
as we see on the far left, then implies that IT is
seen as a single number, it's seen as a cost figure. You know, trying to pitch
agility to such an organization is going to be difficult. An organization further on the right that sees IT as a
critical business enabler, they will be much more
interested in agility and speed as topics. Now, you will observe
that many organizations actually change their CIO
reporting line over time and luckily, almost always to the right. I just spoke to a CIO recently who said that her biggest success
so far was changing the reporting line away from
the chief financial officer. So again, we see that
organizational structures have a lot to do with architecture. Understanding the organization allows you to translate technical capabilities into the specific business priorities. Now, let me give you a concrete example. You know, as an engine room architect, you often build systems that
have automated deployments, they enable software delivery velocity and they increase observability. Now, you'd think that every IT executive must be excited to have such a system. However, you find out that up
in the corporate penthouse, IT executives have very
different priorities given by the CIO or by the
CEO or by the business. You know, it's gotta be secure, right? They don't wanna be in the
news for a data breach, right? The IT must be up and
running, it must be available. Nobody likes to pay for
something that's not running and of course, it's better
to spend less money. So you might find yourself
pitching something that you find exciting,
but that's perceived as of limited value by the
folks that you're speaking to. Now sure, you could just now say, I just pitch cost and availability, but you can do something
much more valuable. You can ride the architect elevator by showing how the items on the left actually enable the items on the right. Observability, velocity and automation are critical elements of security because they allow rapid
detection, served containment and maintaining off patch levels. Likewise, observability
allows you to detect or even predict system issues
to increase availability. Automation allows you rapid
fail over or scaling up and high velocity allows you
to roll out application fixers and reduce downtime. So again, all three elements
on the left work together to increase availability and last, elastic scaling
enabled by automation reduces costs and increased observability allows you to optimize sizing. So, this is a perfect elevator example where you show how the
items from the engine room connect to the concerns of
the organizational penthouse. It's like zooming in and
zooming out in action. What you notice on the
previous slide is that, we are not throwing out new buzzwords. Folks in the penthouse might
be a lot less interested in the latest open source
project names than you are. Instead, you're focusing
on forging connections. It's like learning a new language. There's way too much vocabulary, well, especially in IT there is, but if you learn the grammar, you can make connections
and express meaning. So when up in the penthouse,
focus on the grammar of IT, not all the buzzwords. Now riding the elevator is
about connecting levels. Now, that's why the
mid-levels are very important. They tell you how to
connect the engine room with the corporate penthouse. Your biggest challenge in
the mid-levels is complexity. Systems we build today,
they are amazingly powerful, but let's face it, they're also complex. At the same time, these
systems have a great relevance for the business and IT strategy. The role of IT has dramatically changed thanks to these systems, so
we can't just ignore them. So one more time, let's
borrow from real architects and see how we deal with the complexity. Real architects build models. Models are great because they're
cheaper and easier to build than the real thing, allowing
architects to iterate until they reach a final
design that they can implement. For us IT architects, models
are also extremely useful and models allow us to predict a system's essential properties. For example, will the system scale? We saw a simple model for
that just a few slides ago when we discussed options. Models filter out the noise. For example, our model for layering just showed the essence and
allowed us to think clearly and because we can think more clearly, we can make better decisions and last, models should
appeal to a broader audience, so that stakeholders can
understand the implications of the decisions and the trade-offs we make in the engine room. There's one important property that all models have in common though and that is models aren't reality. They are simplifications
to help our thinking. They're by definition wrong, so at least let's make sure they're useful and as George Box eloquently pointed out, it's the simple models that do this best. Most models I have used
in this talk, so far, they're very, very simple. They were designed to get
a specific point across. So, let's try two more very simple models. So here are two very,
very simple system models. In fact, they use the same
components, A, B, C and D. However, they are wired
together differently. Do you think the systems
represented by these models have different essential properties? Well, I think so. In fact, they're almost the
exact opposite of each other. The system on the left is, correct, a layered architecture, right? This means a clean structure,
easy replaceability, but also longer latency and possibly single points of failure. All right if C fails, A
can no longer talk to D. The model on the right
is the exact opposite. It has many more dependencies, but shorter paths and
more resilience, right? A can talk to D directly when needed. So two things we learned
here, less is really more. You can express more with simple models. All the irrelevant aspects
like programming languages and data times and whatnot are omitted, so we can focus on the essence and second, architectural
models without lines are mostly meaningless. All the properties we just discussed are a result of the lines. After all, we use the same boxes and that's how architects
see more dimensions and use models as their best allies in the mid-level of the elevator. So, models aren't making
things superficial or trivial. They place important abstractions to sharpen and deepen our thinking. Many IT architects draw
these giant tapestries. Those are not useful models. They lack abstraction
and they lack emphasis and they also don't widen your audience. As George Box would say,
they're the mark of mediocrity. So how do we pick the best model? The best model is the
one that helps you answer your questions and helps
you make better decisions. Now, that means before you draw a model, you must be clear about which question you're trying to answer. All the models here depict
a very well-known system, planet Earth, which of
these models is the best? Well, that's a trick
question because it depends on which question you're trying to answer. If you're going for a hike
or you're trying to build a ski resort or avoid
building in the flood zone, a topographic map is an excellent model. Political maps are great
to understanding elections. Highway maps tell you how shortest drive from one town to another and where there's a good
place to take a rest and lastly, if you happen
to be in the business of building distribution centers, a population density map
is the best map for you. So, the next time you're being asked to draw an architecture diagram, a model, you should first ask which question are you looking to answer
because that will tell me which model I should be drawing. Now, we saw that simple models
are better, but careful. George said simple, but evocative. Now, how is a model evocative? Well, here is one that isn't. You might say, oh, that's
a nice architecture, has a front-end, oh, has a
back-end and the database and look, the front-end
talks to the back-end. No kidding, right? This model doesn't evoke much
in me besides maybe boredom. So, why is this model not useful? Because it doesn't convey
meaningful decisions. It's like saying my car has four wheels. Like, all right, now some
cars have only three or six, but highlighting that you have four doesn't actually convey very much and that's why good models
not only answer questions, they also convey meaningful decisions 'cause otherwise, it's not really worth drawing up a picture. Okay, it's time to apply this to a real architecture diagram, not a building one, but a cloud one and we have a whole website full of them, so I found this great
architecture diagram. Actually, I think Corey
Quinn had already picked on this one before, but
to the author's defense, I have to highlight that this
is third architecture diagram in a paper showing the high end
option of hosting WordPress, the most scalable and resilient option. Now, there are probably a lot of questions that this diagram answers, but it also seems to struggle a bit to be simple and evocative, right? The nine footnotes in the
picture might give you a hint. So how would I simplify this and emphasize the key decisions
without losing meaning? I can see three major
decisions in this model. The first important decisions I see is the split between
static and dynamic content, right, that's a very sensible choice and one that we should make
very apparent in our model. The second fundamental decision
is to split the dynamic part across two availability zones. Also, a very sensible
choice for high availability and last, we extract the state
into a replicated database and a shared file system, so that we can auto scale
our compute instances because they're stateless. Now, not having spelled out the questions that this model is looking to answer, it's a safe bet that we're
interested in system availability and scalability, right? And scalability is really
just a special case of availability under load. Now, one part is missing
from this picture though. It doesn't show the AWS
services being used. Your product selection is important, but it should follow your
critical architecture decisions. So, let's add them in. Now, admittedly, this is probably
not the best architecture diagram I have ever drawn,
but it does bring out the key decisions around scaling, plus the AWS services that it use and I can imagine sharing this model with a much wider audience
than the original one. It's much easier to understand
what's going on here. Now, once we have answered
the core questions in a simpler way, we have
freed up mental capacity to address additional concerns that the audience is likely to have. Now, I'm not gonna dive into all of those, but there's a good chance that you get one or more
of the following questions. People might wonder, how can you maximize the percentage of traffic
that is served statically and how much costs this would save? They might also wonder how the
solution not only scales up, but how it scales down, right? What is your minimum run cost per month when you have very little or no traffic? You show auto scaling for
the stateless compute nodes but what about Amazon Aurora? Do you use a cluster for
that to also auto scale? You know, could the compute
nodes rather than EC2 be containers and run in EKS or ECS? Would that be better? Would it have an impact
on the other aspects of availability or cost? Users might wonder whether
hosting static content separately right, in S3, requires
them to use specific URLs and lastly, folks might want
to calculate the overall system availability
based on the architecture and the stated service after this. The real list is likely much longer. What we learn here is
that reducing your models to the essence gives
you room to dig deeper and answer more questions. I'd like to sum this up
with one important message. As cloud architects, we often over index on the services we select. The services are, of course, important, just like good ingredients are important to making a tasty meal,
but first and foremost, you need a good chef. So, every once in a while, remind yourself that as an
architect, you are the chef, you are not just shopping for groceries. Now remember, a good model describes a system's essential properties. So, how about this model? Pretty nice one. So, the essential properties
that will come to your mind are gonna be pretty awesome, yeah. This solution is serverless,
meaning it's lightweight, without the need to
manage any infrastructure. It's event driven and it
uses Amazon EventBridge as serverless event bus which makes the solution loosely coupled. Almost without saying, the
solution is distributed, is highly scalable and
of course, automated. So, you deserve to be pretty
stoked about your architecture, but remember that the mid-levels
of the architect elevator also need to anticipate questions from the organizational penthouse. Here, you might find interest in a very different set
of essential properties. What's the business value of this solution and of this particular architecture? Do I have cost predictability? How do I budget my run cost with a solution that scales up and down? Do I have the right people and skillset to build and operate such a solution? And event driven systems are known to have highly dynamic
runtime to behaviors. How do I manage those? And if I need to take my
system to another platform, how high will the switching cost be? Once again, the questions
you get at different levels will be different. Tying these aspects together is where the power of the
architect elevator lies. But how far do you have to
go when translating benefits? Let's take one popular
buzzword and try it out. Now, I wrote a whole
book about loose coupling many years ago, so it's one
of my favorite buzzwords. It's also widely considered
to be a good thing, but don't assume all
floors in the elevator will take that at face value. So you have some explaining to do. Coupling is a measure of the
dependency between components. The more dependencies,
the tighter the coupling. Loose coupling allows
systems to vary independently without propagating the changes
throughout the whole system. It's not an all or nothing affair, but a gradation with multiple dimensions. So for example, temporal
decoupling can be achieved with asynchronous communication
such as Amazon SQS. Programming language
decoupling can be achieved with common data formats like JSON. Next, coupling doesn't come for free. So you'll need sort of a tooling and you should also expect some overhead like we've seen with other architectures and I'm sure you could add
much, much more about this and I want that you could write a whole book about loose coupling. So how do you make this
digestible for the penthouse? Just spooling out the buzzword, waving your arms and
claiming it's important certainly doesn't do the trick. So you need to focus on
a few key properties. I pick a limited change radius
and a limited error radius as the most important properties. But you need to realize
that these are still proxies for benefits that the
folks in the penthouse really care about. You're gonna need to do
one more translation. The limited change radius affords you a higher rate of change and the limited error
radius makes this system more tolerant of failure. Meaning, it degrades more gracefully. It's like a limp home mode on some cars. Now, if you had more slide space, you could offset those benefits against the increased
complexity and overhead and then you can have a very fruitful and an intelligent discussion whether the system's
anticipated rate of change is high enough to
justify those trade-offs. We have seen that by
translating the buzzword, you can get into a much deeper
discussion with the audience. Most importantly, you made your audience part of the thought process. Spooling out buzzwords not
only makes you look dumb, it also makes your audience dislike you because it shuts them out from taking part in the thought process. Don't do that to the
folks in the penthouse. All right, now you're
armed with the best models and the best metaphors to
bring architecture thinking to the penthouse. But unfortunately,
that's not quite enough. It cannot be boring. Luckily, you're not the first
person to try to persuade an audience, so you can
fall back on one more model and this time, one that's
about 2,400 years old from Aristotle. Your audience will view your presentation or any talk you give from
three different lenses. They will hear your logical
arguments, that's logos, they will consider your
authority and trustworthiness, that's your ethos, and they will consider
the emotions you invoke, we call that pathos. Now, the problem with most
technical presentations is that the logos bubble is way too big and that's understandable,
we come from the engine room, but it cannot be 90% logos
and 5% ethos and pathos. Your audience isn't a compiler. Luckily there are
several simple techniques to improve the balance. Stating your experience and affiliation boosts your ethos, your credibility. So does citing external sources. Gregor said that loose
coupling has a cost. Now you have help in making your argument. When it comes to emotions, my main advice is don't fall
back to fear all the time. If we aren't serverless by
tomorrow, we will be extinct. Now, that might be somewhat
true, but as humans, we have many more fruitful emotions like anticipation, surprise, joy, pride. So anecdotes and metaphors and great ways to stir such positive emotions. I have one last piece
of advice that I used to become a better presenter and this time, it's not
about building architects. Instead it's about DJs. No one captures their
audience like a good DJ and you know what? Most of the time, you
know the content already but you're still mesmerized
by the live performance, but you wanna see the smooth
transitions, the buildups and the secret to success is
that, a DJ reads the audience. A DJ works off prepared segments, but a DJ will improvise and fine tune based on how the audience reacts. Now, if you're able to work this into your technical presentations,
the penthouse is yours. Now I hope you enjoyed this short ride in the architect elevator. Now you understand how architects think, you have a clever way of articulating the value of architecture, you know how to read org
charts, build evocative models, translate technical
properties into benefits and deliver it like a DJ. Now, there's a ton more to say, so I invite you to check
out my book and the website, or to connect with me online. For now, it's time for
me to yield the stage to all you architect superstars. I already pushed the button
to the top floor for you. Thank you very much. (upbeat music)

## Subtitles with Timestamps

[00:01](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1s) (upbeat music)

[00:11](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=11s) - This talk is about
architects and architecture.

[00:14](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=14s) You might wonder whether it's
worth spending 45 minutes

[00:18](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=18s) listening about roles and titles

[00:20](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=20s) instead of hearing the
latest product features.

[00:23](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=23s) I certainly believe so
because I am convinced

[00:25](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=25s) that architects and
architecture play a central role

[00:29](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=29s) in the success of any complex IT project

[00:32](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=32s) and especially cloud projects

[00:35](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=35s) and if that isn't convincing enough,

[00:37](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=37s) software and cloud architects
are routinely ranked

[00:40](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=40s) amongst the most sought after

[00:42](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=42s) and highly compensated job roles.

[00:45](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=45s) So, let's look at what it means

[00:47](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=47s) to be a successful architect.

[00:56](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=56s) We talk a lot about modern applications

[00:59](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=59s) and system architectures.

[01:01](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=61s) In fact, most of re:Invent
covers modern architectures,

[01:05](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=65s) but I believe it's time
to not just upgrade

[01:08](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=68s) our architectures, we also
need to upgrade our definition

[01:12](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=72s) of what it means to be an architect

[01:14](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=74s) and I can give you a hint,

[01:16](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=76s) it's not about drawing YouMail diagrams

[01:18](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=78s) or setting coding standards.

[01:23](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=83s) As always at Amazon, we
like to work backwards.

[01:27](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=87s) So we should think first about the values

[01:29](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=89s) that the modern architect provides.

[01:31](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=91s) So, which architect is most valuable?

[01:37](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=97s) I have carried the
title of chief architect

[01:39](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=99s) at a major financial services institution.

[01:42](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=102s) Now did that make me the
most valuable architect?

[01:46](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=106s) Or perhaps it should be the architect

[01:48](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=108s) who knows the most design patterns

[01:51](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=111s) or the one who has the most certifications

[01:53](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=113s) or the one who is hands-on
with the development teams?

[01:58](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=118s) Well, I am convinced
that in our modern world,

[02:01](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=121s) the most valuable
architects are not the ones

[02:06](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=126s) who carry a specific title or
have specific certifications.

[02:09](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=129s) Instead, it's those who
can connect the most levels

[02:13](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=133s) of the organization.

[02:15](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=135s) Large organizations, and
many not so large ones,

[02:18](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=138s) have many different layers

[02:21](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=141s) and too often, they're disconnected.

[02:24](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=144s) So the organization is playing
some sort of telephone game

[02:28](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=148s) where the folks setting
the business strategy

[02:30](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=150s) up in the penthouse have little idea

[02:33](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=153s) about the technology and vice versa.

[02:36](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=156s) So, it's easy to see that that
doesn't work terribly well.

[02:41](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=161s) As an architect, if you're
up in the penthouse,

[02:43](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=163s) but all you do is, you know,

[02:45](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=165s) spool at words like agile or cloud-native,

[02:48](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=168s) your impact is actually very small.

[02:51](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=171s) I wouldn't even call
that being an architect.

[02:53](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=173s) I might call you a parrot if
I want to be more poignant

[02:57](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=177s) and I have met a lot
of parrots in my career

[02:59](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=179s) and I have to say, I prefer
the ones who can fly.

[03:03](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=183s) Likewise, if your world's
foremost helm chart expert

[03:07](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=187s) and have written dozens
of Kubernetes operators,

[03:10](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=190s) but you've never worked
on a project that provided

[03:13](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=193s) real business value, you're
also not very valuable.

[03:17](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=197s) It's the connection that
provides the most value.

[03:21](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=201s) So, let me prove that to
you with an architecture.

[03:25](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=205s) Architects like diagrams, so
here's an architecture diagram.

[03:30](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=210s) It shows one of the most
fundamental architecture patterns,

[03:34](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=214s) it's called layering.

[03:35](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=215s) Layering divides the
system into multiple parts,

[03:39](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=219s) such that any part only
depends on lower parts.

[03:43](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=223s) I'm sure you've seen or
drawn a diagram like this.

[03:46](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=226s) Now, why is this type of
architecture so popular?

[03:50](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=230s) Well, because it has a number
of distinct advantages.

[03:55](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=235s) Each layer does one thing,

[03:57](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=237s) so it's a neat separation of concerns

[03:59](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=239s) that abstracts away the details

[04:02](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=242s) behind well-defined interfaces.

[04:04](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=244s) For example, a lower layer
might deal with persistence,

[04:08](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=248s) so that the upper layers
don't depend on the type

[04:10](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=250s) of data store that's being used.

[04:12](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=252s) Also, dependencies flow
nicely from top to bottom,

[04:17](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=257s) meaning the application logic will depend

[04:20](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=260s) on the persistence layer,

[04:21](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=261s) but the persistence layer doesn't
depend on the application.

[04:25](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=265s) It can be reused for
many other applications.

[04:28](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=268s) Now this also means that the
data store can be replaced

[04:31](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=271s) without impacting the
remainder of the application.

[04:35](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=275s) Well, that's pretty cool,
you have to admit, right?

[04:37](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=277s) Shouldn't we layer all applications then?

[04:40](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=280s) Well, not quite so fast.

[04:42](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=282s) Architecture is in the
business of trade-offs.

[04:45](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=285s) So we should expect this architecture

[04:47](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=287s) to also have downsides.

[04:50](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=290s) Dividing a system into
layers can slow things down,

[04:54](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=294s) perhaps, you know, the
ideal database optimization

[04:57](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=297s) that you wanna do isn't available

[04:59](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=299s) in the shared layer beneath

[05:02](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=302s) and connecting the layers
also carries overhead,

[05:05](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=305s) especially if you're using
a text-based data format

[05:08](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=308s) like JSON or perhaps XML

[05:10](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=310s) and if you have many, many layers,

[05:13](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=313s) managing all the layers can become tedious

[05:16](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=316s) and lead to teams
optimizing their own layer,

[05:19](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=319s) but forgetting the end-to-end flow.

[05:22](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=322s) Lastly, we have all seen how a
simple change in the UI layer

[05:26](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=326s) requires an update in the
back and front-end layer,

[05:30](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=330s) the application logic
layer, the API layer,

[05:32](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=332s) the persistence layer and
in the data source schema.

[05:36](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=336s) So such change propagation
also slows you down.

[05:40](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=340s) Slowing down is not a good thing.

[05:43](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=343s) Now you might wonder,
what does this have to do

[05:45](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=345s) with the value that architects
bring to an organization?

[05:49](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=349s) Well, actually quite a lot.

[05:51](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=351s) All the benefits and
liabilities listed here

[05:54](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=354s) don't just apply to technical systems,

[05:57](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=357s) they also apply to organizations.

[06:00](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=360s) Departments use well-defined interfaces,

[06:03](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=363s) but are also prone to
optimizing locally, right?

[06:06](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=366s) They make you take a number
and fill out endless forms

[06:10](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=370s) or making a change
requires you to coordinate

[06:12](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=372s) across 20 different teams.

[06:15](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=375s) On the upshot, replaceability
can be a major benefit.

[06:18](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=378s) We call this outsourcing.

[06:21](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=381s) So what we are realizing is that,

[06:24](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=384s) architectural thinking
applies equally well

[06:27](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=387s) to technical and organizational systems

[06:31](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=391s) and that means that you
as technical architects

[06:34](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=394s) understand a lot more
about organizational design

[06:37](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=397s) than you might've realized,
and that's perfect

[06:41](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=401s) because you can't be a
successful architect these days

[06:44](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=404s) without also influencing the organization

[06:49](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=409s) and because that's such
a critical insight,

[06:51](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=411s) let's dig a little deeper.

[06:53](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=413s) What do the properties on
the left and on the right

[06:57](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=417s) have in common when
compared with each other?

[07:01](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=421s) As you will see, architects
are expected to see things

[07:05](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=425s) that not everybody else sees.

[07:07](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=427s) So if you look carefully,
you will find the properties

[07:11](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=431s) on the left are largely structural.

[07:14](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=434s) We talk about interfaces and abstraction.

[07:19](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=439s) In contrast, the downsides on the right,

[07:22](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=442s) they are largely behavioral.

[07:24](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=444s) We talk about latency
and change propagation.

[07:29](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=449s) So that gives us, as architects, a hint

[07:32](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=452s) as to when layering is beneficial

[07:35](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=455s) and when it can become a hindrance.

[07:37](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=457s) If the rate of change is
slow or changes are local,

[07:42](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=462s) then layering works well.

[07:45](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=465s) When the rate of change increases

[07:48](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=468s) or we're dealing with systemic changes,

[07:50](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=470s) then it becomes a hindrance.

[07:53](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=473s) Now, large organizations are
divided into many layers,

[07:58](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=478s) right, from strategic planning to finance,

[08:00](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=480s) accounting, payroll, manufacturing
and facility services

[08:04](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=484s) and that used to work well for them

[08:06](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=486s) when the business environment was stable.

[08:10](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=490s) These days, we talk a lot
about digital disruption

[08:12](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=492s) and transformation, the
environment keeps changing faster

[08:17](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=497s) and all those layers are
now becoming a hindrance,

[08:22](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=502s) but it's not easy to take layers out.

[08:25](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=505s) That's why you need folks
to connect the layers

[08:28](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=508s) and architects are best suited to do that.

[08:31](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=511s) I call this riding the architect elevator.

[08:35](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=515s) Instead of walking from floor to floor,

[08:38](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=518s) you provide a fast
connection between the levels

[08:43](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=523s) and in fact, I've written a
whole book that teaches you

[08:46](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=526s) how to ride this architect elevator

[08:49](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=529s) from the engine room to
the penthouse and back

[08:52](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=532s) and this describes how
architects provide value

[08:55](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=535s) at the different layers
and manage to connect them.

[08:59](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=539s) Starting from the top,
architects need to make sure

[09:02](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=542s) that business and IT
strategy are connected.

[09:05](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=545s) If the two tunnels don't meet,

[09:07](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=547s) nothing else will really help you.

[09:10](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=550s) Second, you'll never be in an ideal state.

[09:13](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=553s) Architects are also
expected to affect change.

[09:17](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=557s) Complexity is your biggest enemy,

[09:20](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=560s) you will need to minimize and tackle it.

[09:23](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=563s) You do that by explaining
and de-mystifying.

[09:26](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=566s) Don't make things more
complicated than they already are.

[09:30](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=570s) Now down in the engine room,

[09:31](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=571s) there's a ton of technical topics

[09:33](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=573s) like building resilient
and scalable systems,

[09:36](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=576s) agile delivery, automation,
and much, much more,

[09:39](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=579s) but there's hundreds of other
sessions on those topics,

[09:42](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=582s) so I'll only focus on the top half.

[09:46](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=586s) There's one question though,

[09:48](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=588s) that I often do get
from aspiring architects

[09:51](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=591s) when I show the idea of
the architect elevator,

[09:55](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=595s) and that is, will the folks up
in the penthouse welcome me?

[10:00](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=600s) The answer is very simple, yes, they will.

[10:03](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=603s) People who can translate
the technical details

[10:07](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=607s) into meaningful insights
for the penthouse,

[10:10](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=610s) without dumbing things down,

[10:11](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=611s) are extremely rare and
highly sought after.

[10:15](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=615s) If anything, your biggest problem might be

[10:17](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=617s) that the folks in the penthouse

[10:18](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=618s) don't want to let you get back
down into the engine room.

[10:22](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=622s) So, let's have a look at how you can ride

[10:25](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=625s) this architect elevator.

[10:29](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=629s) To me, architect is not something

[10:31](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=631s) that's written on your business card.

[10:33](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=633s) Rather, it's really a way of thinking.

[10:36](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=636s) The first thing that comes to mind

[10:37](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=637s) when we consider what
architects do are diagrams.

[10:41](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=641s) We could draw diagrams and that's good

[10:44](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=644s) because diagrams are abstractions

[10:47](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=647s) and they're the best
tools we have to manage

[10:49](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=649s) the complexity we inherently face.

[10:52](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=652s) Now, when we think about the
diagrams that architects draw,

[10:55](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=655s) we usually think about boxes and lines,

[10:58](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=658s) like the typical system
kind of architectures.

[11:02](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=662s) However, if we compare this
with real-life architects,

[11:05](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=665s) with famous architects
who design buildings,

[11:08](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=668s) they do not draw blueprints.

[11:11](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=671s) Rather, they make sketches.

[11:14](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=674s) This is a sketch from Oscar Niemeyer,

[11:16](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=676s) one of my favorite architects
who designed these buildings

[11:20](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=680s) in the city of Brasilia in Brazil.

[11:23](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=683s) Now, this is not a blueprint,

[11:24](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=684s) there's a lot of detail that's missing,

[11:27](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=687s) but most importantly,
it captures the essence.

[11:30](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=690s) It expresses what the essential structure

[11:33](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=693s) and property of the system is going to be

[11:36](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=696s) and it incorporates the major
decisions and the context

[11:40](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=700s) in which the system is going to be built

[11:44](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=704s) and if you're wondering
whether this napkin sketch

[11:46](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=706s) matches reality, you can be
assured that the real building

[11:50](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=710s) matches the essence of this architecture.

[11:53](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=713s) They are a lot of details to be filled in,

[11:55](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=715s) a lot of blueprints to be drawn

[11:57](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=717s) but the core decisions
and the core system image,

[12:00](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=720s) so to speak, follow this
sketch of the architect.

[12:04](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=724s) So first, learning about
how architects think

[12:07](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=727s) is that architects don't
draw blueprints, they sketch.

[12:12](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=732s) The second part of being an architect

[12:14](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=734s) is to see more dimensions.

[12:17](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=737s) You've surely been in
situations where people argue

[12:20](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=740s) back and forth between,
are you going to do X

[12:23](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=743s) or are you going to do Y?

[12:26](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=746s) Should our code run in a container?

[12:27](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=747s) Should we make it serverless?

[12:29](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=749s) Do I need an API gateway?

[12:31](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=751s) Do I need a service mesh?

[12:32](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=752s) Do I need a document database
or do I need a graph database?

[12:36](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=756s) And people can go back and
forth for very, very long time

[12:39](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=759s) because they both believe they are right

[12:42](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=762s) and it's just like in this picture

[12:44](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=764s) where one person is very, very
sure that they see a circle

[12:48](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=768s) while the other person is equally sure

[12:51](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=771s) that they see a rectangle.

[12:53](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=773s) Architects, our job is
to see more dimensions,

[12:57](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=777s) to see the problems from
different points of view

[12:59](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=779s) and show that both are right.

[13:02](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=782s) They just need to look at things

[13:03](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=783s) from their respective point of view.

[13:06](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=786s) Once you show them the cylinder,

[13:08](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=788s) they can have a much more
meaningful conversation.

[13:13](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=793s) For example, people might argue that

[13:15](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=795s) we need to speed up software delivery

[13:18](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=798s) while others argue that we
need to improve quality.

[13:22](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=802s) They each see one dimension

[13:24](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=804s) and consider these properties
opposites of each other,

[13:28](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=808s) but modern architects know
that test and build automation

[13:31](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=811s) speed up delivery while
actually increasing quality.

[13:36](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=816s) So, we see these as independent dimensions

[13:39](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=819s) and know how to achieve both.

[13:42](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=822s) Now, this is the second major part

[13:44](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=824s) of thinking like an architect,

[13:46](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=826s) we do stand to see more dimensions

[13:49](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=829s) and not only do we see more dimensions,

[13:52](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=832s) we're also good at zooming in
and zooming out of the system

[13:56](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=836s) and this isn't like a camera
lens where you zoom in

[14:00](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=840s) and you see the same thing
just a little bit bigger.

[14:03](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=843s) It's much more like this Mandelbrot set

[14:06](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=846s) where if you zoom in, you will
see very different things.

[14:10](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=850s) Our world is also fractal.

[14:12](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=852s) It covers things from
business architecture

[14:15](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=855s) and business strategy to
high level architecture

[14:17](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=857s) and then you go deep
down into the engine room

[14:19](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=859s) to make sure you have the
right number of spaces

[14:22](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=862s) in your YAML file and all
of those different levels

[14:25](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=865s) of zooming in and zooming out
look very, very different.

[14:29](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=869s) So, when we talk about what
it means to be an architect,

[14:32](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=872s) you can see that it's a way of thinking.

[14:35](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=875s) It's about sketching to express
the essence of something,

[14:39](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=879s) that is about seeing more dimensions

[14:41](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=881s) to allow folks to have
more meaningful discussions

[14:44](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=884s) and it's about zooming in and zooming out

[14:47](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=887s) to see different things.

[14:51](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=891s) Now that we understand what
goes on in an architect's head,

[14:55](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=895s) how do we articulate the
value that an architect

[14:59](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=899s) and architecture bring?

[15:01](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=901s) Most people, including
myself, would say that

[15:04](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=904s) if your system is still running,

[15:07](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=907s) if it's still running
well after several years

[15:09](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=909s) and continues to absorb change,

[15:11](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=911s) then it likely has a good architecture

[15:13](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=913s) and perhaps a good architect behind it.

[15:17](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=917s) But there should be a better metric

[15:18](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=918s) for the value of architecture
than hindsight, we would say.

[15:22](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=922s) Now I have found that
you can express the value

[15:25](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=925s) of architects with this simple formula.

[15:29](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=929s) Well, actually, you don't need
to understand the formula,

[15:32](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=932s) the gentlemen, Fischer
Black and Myron Scholes,

[15:35](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=935s) you know, got a Nobel Prize
in Economics for this one,

[15:37](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=937s) which is known as the
Black-Scholes formula

[15:40](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=940s) of options pricing.

[15:42](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=942s) What you do need to understand though,

[15:44](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=944s) is how architects provide options

[15:48](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=948s) and why these options are valuable.

[15:52](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=952s) Options are a way to defer decisions.

[15:55](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=955s) In financial markets, these
options usually entitle you

[15:59](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=959s) to purchase a share of
stock at a given date,

[16:02](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=962s) for example, in one year, for
a set price, let's say $100.

[16:06](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=966s) Now, the great thing about
having such an option

[16:09](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=969s) is that in one year, the decision
whether to use that option

[16:12](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=972s) becomes trivial, right?

[16:14](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=974s) If the stock trades at more than $100,

[16:17](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=977s) you use your option to buy at 100

[16:19](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=979s) and you have money in the bank.

[16:22](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=982s) If the stock trades at below 100,

[16:24](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=984s) well, you don't use the option,
it's optional after all.

[16:28](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=988s) So, options defer a
decision into the future.

[16:31](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=991s) So almost like time travel, in the future,

[16:33](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=993s) you'll be smarter than today

[16:35](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=995s) and you can make better decisions.

[16:38](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=998s) So, it's not surprising that
these options have a value

[16:42](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1002s) and Black and Scholes have
calculated that value.

[16:45](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1005s) That's what this formula
is actually about.

[16:48](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1008s) Now, as architects, we
can also create options

[16:52](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1012s) to defer decisions and
that's how we provide value.

[16:56](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1016s) Let's look at a simple
example of how this works

[16:59](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1019s) in modern architectures.

[17:02](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1022s) In classic IT, hardware sizing

[17:04](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1024s) is one of the most
depressing activities, right?

[17:07](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1027s) You have an application
and you need to estimate

[17:10](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1030s) how much hardware is needed
to run this application well.

[17:14](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1034s) Now, the reason it's depressing

[17:16](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1036s) is because it leads to only
one of two possible outcomes.

[17:21](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1041s) You either end up with too
much hardware and waste money

[17:24](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1044s) or too little hardware

[17:26](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1046s) and you end up with a poorly
performing application.

[17:29](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1049s) Now as cloud architects,

[17:31](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1051s) we know a great option
that we can provide,

[17:33](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1053s) it's called a scale-out architecture,

[17:36](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1056s) coupled with an elastic infrastructure.

[17:39](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1059s) Now, you have the option
to add compute resources

[17:42](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1062s) once you see the actual
application performance

[17:46](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1066s) and you can easily see that this option

[17:48](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1068s) has made the decision much simpler

[17:50](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1070s) and allows you to make a better decision.

[17:53](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1073s) Well, you can further increase
the value of this option

[17:56](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1076s) if you break your application
into even smaller pieces,

[17:59](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1079s) so you can scale individual
components, right?

[18:03](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1083s) That'll be an even better option.

[18:06](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1086s) Of course, that's exactly
what a serverless architecture

[18:09](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1089s) allows you to do.

[18:10](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1090s) Now, those are fantastic options to have.

[18:13](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1093s) They defer a decision
about hardware sizing

[18:16](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1096s) until you have more information,

[18:19](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1099s) like the load of the application

[18:21](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1101s) and as a result, you can
make a much better decision.

[18:26](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1106s) Now, you might've noticed that

[18:27](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1107s) I said architects sell options,

[18:30](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1110s) I didn't say they're giving them away.

[18:33](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1113s) Sometimes architects believe
that teams should use

[18:36](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1116s) all their great ideas,
meaning their options,

[18:39](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1119s) but they forget that those
options also have a cost

[18:43](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1123s) and that cost comes in three main forms.

[18:46](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1126s) First, implementing the option
requires some work, right?

[18:50](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1130s) For example, you need to
decompose the application,

[18:53](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1133s) wrap it into container,
automate deployment

[18:55](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1135s) to spool up new instances.

[18:57](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1137s) You know, second, the options tend to make

[18:59](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1139s) your architecture slightly
more complex, right?

[19:03](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1143s) Scaling out requires you
to have a load balancer

[19:05](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1145s) and you have to manage and
replicate state as well.

[19:09](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1149s) No one is ever looking
for more complexity,

[19:11](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1151s) so this is an important cost to consider

[19:14](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1154s) and last, options can
lead to under utilization.

[19:18](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1158s) For example, if you
want to have the option

[19:21](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1161s) to run your application in
many different environments,

[19:24](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1164s) you might hesitate to use
all the services provided

[19:27](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1167s) by one environment and that
might lead to an application

[19:30](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1170s) that doesn't perform as well

[19:32](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1172s) or one that takes longer to build.

[19:34](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1174s) In either case, that's a very real cost.

[19:38](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1178s) So, architects are in the
business of trade-offs.

[19:41](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1181s) So we consider both the value
of an option and its cost.

[19:46](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1186s) So when is it worth getting
this horizontal scaling options?

[19:51](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1191s) You will find that the higher
the degree of uncertainty,

[19:54](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1194s) the more valuable deferring
a decision becomes.

[19:58](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1198s) That's intuitive because
if nothing ever changes,

[20:01](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1201s) making the decision today is just as good

[20:04](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1204s) as making it tomorrow.

[20:06](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1206s) But if you're building
a mobile application

[20:08](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1208s) that might have 100
users or 100,000 users,

[20:12](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1212s) this scaling option
becomes highly valuable.

[20:16](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1216s) So, we find that architecture
provides more value

[20:20](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1220s) in uncertain times, and we
live in uncertain times,

[20:24](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1224s) so architecture becomes more valuable.

[20:28](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1228s) Now, we know another popular
method that also starts with A

[20:32](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1232s) and that's called agile methods

[20:34](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1234s) and oddly, architecture is sometimes seen

[20:37](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1237s) as in conflict with being agile.

[20:39](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1239s) You might've heard people say,

[20:41](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1241s) oh, we don't need much
architecture because we're agile.

[20:45](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1245s) Now, interestingly, agile methods

[20:48](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1248s) also thrive on uncertainty.

[20:49](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1249s) If you know everything upfront,

[20:51](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1251s) you don't need to be agile, right?

[20:52](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1252s) We just write it all
down and you code it out.

[20:55](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1255s) So when you, as an
architect, meet somebody

[20:58](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1258s) who prefers agile methods, you
can say, since you're agile,

[21:02](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1262s) I'm guessing that you have
to deal with uncertainty

[21:06](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1266s) and that's exactly what
architecture options do too.

[21:10](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1270s) So when being agile, you should
invest in more architecture.

[21:16](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1276s) Now that we understand
how architects think

[21:18](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1278s) and how they provide value with options,

[21:20](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1280s) it's time to get on the elevator, right?

[21:23](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1283s) After all, we have some
connections to make,

[21:25](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1285s) we need to connect the levels.

[21:27](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1287s) We start on the top in
the corporate penthouse

[21:31](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1291s) and up in the penthouse is usually a CIO,

[21:34](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1294s) a chief information officer.

[21:36](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1296s) In most organizations, IT
staff report to the CIO

[21:39](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1299s) and the CIO is responsible
for the overall IT budget,

[21:44](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1304s) but who does a CIO report to, right?

[21:47](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1307s) That's actually a very good question.

[21:50](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1310s) When you're up in the
organization's penthouse,

[21:53](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1313s) you need to understand
what IT is measured by

[21:57](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1317s) and you'll find that
the CIO's reporting line

[21:59](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1319s) has a direct correlation to this.

[22:03](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1323s) I blogged about this many years ago

[22:04](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1324s) after visiting many
different organizations.

[22:08](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1328s) For example, the CIO reporting into a CFO,

[22:12](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1332s) the chief financial officer,
as we see on the far left,

[22:15](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1335s) then implies that IT is
seen as a single number,

[22:17](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1337s) it's seen as a cost figure.

[22:20](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1340s) You know, trying to pitch
agility to such an organization

[22:23](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1343s) is going to be difficult.

[22:25](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1345s) An organization further on the right

[22:28](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1348s) that sees IT as a
critical business enabler,

[22:31](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1351s) they will be much more
interested in agility

[22:35](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1355s) and speed as topics.

[22:37](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1357s) Now, you will observe
that many organizations

[22:39](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1359s) actually change their CIO
reporting line over time

[22:43](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1363s) and luckily, almost always to the right.

[22:46](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1366s) I just spoke to a CIO recently who said

[22:49](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1369s) that her biggest success
so far was changing

[22:52](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1372s) the reporting line away from
the chief financial officer.

[22:56](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1376s) So again, we see that
organizational structures

[22:59](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1379s) have a lot to do with architecture.

[23:02](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1382s) Understanding the organization allows you

[23:04](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1384s) to translate technical capabilities

[23:07](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1387s) into the specific business priorities.

[23:10](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1390s) Now, let me give you a concrete example.

[23:13](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1393s) You know, as an engine room architect,

[23:15](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1395s) you often build systems that
have automated deployments,

[23:18](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1398s) they enable software delivery velocity

[23:21](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1401s) and they increase observability.

[23:23](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1403s) Now, you'd think that every IT executive

[23:26](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1406s) must be excited to have such a system.

[23:30](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1410s) However, you find out that up
in the corporate penthouse,

[23:34](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1414s) IT executives have very
different priorities

[23:37](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1417s) given by the CIO or by the
CEO or by the business.

[23:40](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1420s) You know, it's gotta be secure, right?

[23:42](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1422s) They don't wanna be in the
news for a data breach, right?

[23:45](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1425s) The IT must be up and
running, it must be available.

[23:47](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1427s) Nobody likes to pay for
something that's not running

[23:50](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1430s) and of course, it's better
to spend less money.

[23:54](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1434s) So you might find yourself
pitching something

[23:57](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1437s) that you find exciting,
but that's perceived

[24:00](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1440s) as of limited value by the
folks that you're speaking to.

[24:04](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1444s) Now sure, you could just now say,

[24:06](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1446s) I just pitch cost and availability,

[24:08](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1448s) but you can do something
much more valuable.

[24:12](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1452s) You can ride the architect elevator

[24:14](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1454s) by showing how the items on the left

[24:17](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1457s) actually enable the items on the right.

[24:21](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1461s) Observability, velocity and automation

[24:24](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1464s) are critical elements of security

[24:26](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1466s) because they allow rapid
detection, served containment

[24:30](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1470s) and maintaining off patch levels.

[24:33](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1473s) Likewise, observability
allows you to detect

[24:36](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1476s) or even predict system issues
to increase availability.

[24:40](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1480s) Automation allows you rapid
fail over or scaling up

[24:44](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1484s) and high velocity allows you
to roll out application fixers

[24:47](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1487s) and reduce downtime.

[24:49](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1489s) So again, all three elements
on the left work together

[24:52](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1492s) to increase availability

[24:55](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1495s) and last, elastic scaling
enabled by automation

[24:58](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1498s) reduces costs and increased observability

[25:02](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1502s) allows you to optimize sizing.

[25:05](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1505s) So, this is a perfect elevator example

[25:08](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1508s) where you show how the
items from the engine room

[25:11](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1511s) connect to the concerns of
the organizational penthouse.

[25:15](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1515s) It's like zooming in and
zooming out in action.

[25:20](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1520s) What you notice on the
previous slide is that,

[25:22](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1522s) we are not throwing out new buzzwords.

[25:24](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1524s) Folks in the penthouse might
be a lot less interested

[25:27](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1527s) in the latest open source
project names than you are.

[25:30](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1530s) Instead, you're focusing
on forging connections.

[25:35](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1535s) It's like learning a new language.

[25:37](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1537s) There's way too much vocabulary,

[25:39](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1539s) well, especially in IT there is,

[25:41](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1541s) but if you learn the grammar,

[25:43](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1543s) you can make connections
and express meaning.

[25:47](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1547s) So when up in the penthouse,
focus on the grammar of IT,

[25:52](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1552s) not all the buzzwords.

[25:55](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1555s) Now riding the elevator is
about connecting levels.

[25:58](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1558s) Now, that's why the
mid-levels are very important.

[26:01](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1561s) They tell you how to
connect the engine room

[26:04](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1564s) with the corporate penthouse.

[26:07](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1567s) Your biggest challenge in
the mid-levels is complexity.

[26:10](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1570s) Systems we build today,
they are amazingly powerful,

[26:14](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1574s) but let's face it, they're also complex.

[26:17](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1577s) At the same time, these
systems have a great relevance

[26:21](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1581s) for the business and IT strategy.

[26:23](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1583s) The role of IT has dramatically changed

[26:25](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1585s) thanks to these systems, so
we can't just ignore them.

[26:30](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1590s) So one more time, let's
borrow from real architects

[26:34](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1594s) and see how we deal with the complexity.

[26:37](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1597s) Real architects build models.

[26:40](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1600s) Models are great because they're
cheaper and easier to build

[26:43](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1603s) than the real thing, allowing
architects to iterate

[26:46](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1606s) until they reach a final
design that they can implement.

[26:50](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1610s) For us IT architects, models
are also extremely useful

[26:54](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1614s) and models allow us to predict

[26:56](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1616s) a system's essential properties.

[26:59](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1619s) For example, will the system scale?

[27:01](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1621s) We saw a simple model for
that just a few slides ago

[27:04](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1624s) when we discussed options.

[27:07](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1627s) Models filter out the noise.

[27:09](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1629s) For example, our model for layering

[27:11](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1631s) just showed the essence and
allowed us to think clearly

[27:16](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1636s) and because we can think more clearly,

[27:18](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1638s) we can make better decisions

[27:20](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1640s) and last, models should
appeal to a broader audience,

[27:24](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1644s) so that stakeholders can
understand the implications

[27:28](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1648s) of the decisions and the trade-offs

[27:30](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1650s) we make in the engine room.

[27:33](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1653s) There's one important property

[27:35](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1655s) that all models have in common though

[27:38](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1658s) and that is models aren't reality.

[27:41](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1661s) They are simplifications
to help our thinking.

[27:45](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1665s) They're by definition wrong,

[27:47](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1667s) so at least let's make sure they're useful

[27:51](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1671s) and as George Box eloquently pointed out,

[27:53](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1673s) it's the simple models that do this best.

[27:57](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1677s) Most models I have used
in this talk, so far,

[27:59](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1679s) they're very, very simple.

[28:01](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1681s) They were designed to get
a specific point across.

[28:05](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1685s) So, let's try two more very simple models.

[28:09](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1689s) So here are two very,
very simple system models.

[28:13](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1693s) In fact, they use the same
components, A, B, C and D.

[28:17](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1697s) However, they are wired
together differently.

[28:21](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1701s) Do you think the systems
represented by these models

[28:24](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1704s) have different essential properties?

[28:27](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1707s) Well, I think so.

[28:28](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1708s) In fact, they're almost the
exact opposite of each other.

[28:32](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1712s) The system on the left is, correct,

[28:34](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1714s) a layered architecture, right?

[28:36](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1716s) This means a clean structure,
easy replaceability,

[28:40](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1720s) but also longer latency

[28:42](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1722s) and possibly single points of failure.

[28:45](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1725s) All right if C fails, A
can no longer talk to D.

[28:49](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1729s) The model on the right
is the exact opposite.

[28:52](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1732s) It has many more dependencies,

[28:54](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1734s) but shorter paths and
more resilience, right?

[28:57](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1737s) A can talk to D directly when needed.

[29:00](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1740s) So two things we learned
here, less is really more.

[29:04](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1744s) You can express more with simple models.

[29:08](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1748s) All the irrelevant aspects
like programming languages

[29:10](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1750s) and data times and whatnot are omitted,

[29:13](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1753s) so we can focus on the essence

[29:16](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1756s) and second, architectural
models without lines

[29:19](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1759s) are mostly meaningless.

[29:21](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1761s) All the properties we just discussed

[29:24](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1764s) are a result of the lines.

[29:25](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1765s) After all, we use the same boxes

[29:29](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1769s) and that's how architects
see more dimensions

[29:32](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1772s) and use models as their best allies

[29:35](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1775s) in the mid-level of the elevator.

[29:38](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1778s) So, models aren't making
things superficial or trivial.

[29:43](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1783s) They place important abstractions

[29:45](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1785s) to sharpen and deepen our thinking.

[29:48](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1788s) Many IT architects draw
these giant tapestries.

[29:53](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1793s) Those are not useful models.

[29:55](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1795s) They lack abstraction
and they lack emphasis

[29:59](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1799s) and they also don't widen your audience.

[30:03](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1803s) As George Box would say,
they're the mark of mediocrity.

[30:07](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1807s) So how do we pick the best model?

[30:11](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1811s) The best model is the
one that helps you answer

[30:14](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1814s) your questions and helps
you make better decisions.

[30:18](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1818s) Now, that means before you draw a model,

[30:21](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1821s) you must be clear about which question

[30:23](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1823s) you're trying to answer.

[30:26](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1826s) All the models here depict
a very well-known system,

[30:29](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1829s) planet Earth, which of
these models is the best?

[30:33](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1833s) Well, that's a trick
question because it depends

[30:35](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1835s) on which question you're trying to answer.

[30:38](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1838s) If you're going for a hike
or you're trying to build

[30:42](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1842s) a ski resort or avoid
building in the flood zone,

[30:44](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1844s) a topographic map is an excellent model.

[30:48](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1848s) Political maps are great
to understanding elections.

[30:51](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1851s) Highway maps tell you how shortest drive

[30:53](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1853s) from one town to another

[30:54](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1854s) and where there's a good
place to take a rest

[30:57](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1857s) and lastly, if you happen
to be in the business

[30:59](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1859s) of building distribution centers,

[31:01](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1861s) a population density map
is the best map for you.

[31:06](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1866s) So, the next time you're being asked

[31:09](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1869s) to draw an architecture diagram, a model,

[31:12](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1872s) you should first ask which question

[31:15](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1875s) are you looking to answer
because that will tell me

[31:18](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1878s) which model I should be drawing.

[31:21](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1881s) Now, we saw that simple models
are better, but careful.

[31:26](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1886s) George said simple, but evocative.

[31:30](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1890s) Now, how is a model evocative?

[31:31](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1891s) Well, here is one that isn't.

[31:34](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1894s) You might say, oh, that's
a nice architecture,

[31:36](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1896s) has a front-end, oh, has a
back-end and the database

[31:39](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1899s) and look, the front-end
talks to the back-end.

[31:42](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1902s) No kidding, right?

[31:43](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1903s) This model doesn't evoke much
in me besides maybe boredom.

[31:49](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1909s) So, why is this model not useful?

[31:52](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1912s) Because it doesn't convey
meaningful decisions.

[31:56](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1916s) It's like saying my car has four wheels.

[31:59](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1919s) Like, all right, now some
cars have only three or six,

[32:01](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1921s) but highlighting that you have four

[32:03](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1923s) doesn't actually convey very much

[32:07](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1927s) and that's why good models
not only answer questions,

[32:11](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1931s) they also convey meaningful decisions

[32:14](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1934s) 'cause otherwise, it's not really worth

[32:16](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1936s) drawing up a picture.

[32:19](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1939s) Okay, it's time to apply this

[32:21](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1941s) to a real architecture diagram,

[32:23](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1943s) not a building one, but a cloud one

[32:25](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1945s) and we have a whole website full of them,

[32:27](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1947s) so I found this great
architecture diagram.

[32:31](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1951s) Actually, I think Corey
Quinn had already picked

[32:34](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1954s) on this one before, but
to the author's defense,

[32:37](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1957s) I have to highlight that this
is third architecture diagram

[32:41](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1961s) in a paper showing the high end
option of hosting WordPress,

[32:45](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1965s) the most scalable and resilient option.

[32:49](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1969s) Now, there are probably a lot of questions

[32:51](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1971s) that this diagram answers,

[32:54](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1974s) but it also seems to struggle a bit

[32:56](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1976s) to be simple and evocative, right?

[32:59](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1979s) The nine footnotes in the
picture might give you a hint.

[33:03](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1983s) So how would I simplify this

[33:06](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1986s) and emphasize the key decisions
without losing meaning?

[33:12](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1992s) I can see three major
decisions in this model.

[33:16](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1996s) The first important decisions I see

[33:19](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=1999s) is the split between
static and dynamic content,

[33:23](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2003s) right, that's a very sensible choice

[33:25](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2005s) and one that we should make
very apparent in our model.

[33:30](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2010s) The second fundamental decision
is to split the dynamic part

[33:34](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2014s) across two availability zones.

[33:37](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2017s) Also, a very sensible
choice for high availability

[33:42](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2022s) and last, we extract the state
into a replicated database

[33:48](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2028s) and a shared file system,

[33:51](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2031s) so that we can auto scale
our compute instances

[33:54](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2034s) because they're stateless.

[33:57](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2037s) Now, not having spelled out the questions

[33:59](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2039s) that this model is looking to answer,

[34:01](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2041s) it's a safe bet that we're
interested in system availability

[34:06](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2046s) and scalability, right?

[34:08](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2048s) And scalability is really
just a special case

[34:11](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2051s) of availability under load.

[34:15](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2055s) Now, one part is missing
from this picture though.

[34:17](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2057s) It doesn't show the AWS
services being used.

[34:21](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2061s) Your product selection is important,

[34:24](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2064s) but it should follow your
critical architecture decisions.

[34:28](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2068s) So, let's add them in.

[34:32](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2072s) Now, admittedly, this is probably
not the best architecture

[34:36](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2076s) diagram I have ever drawn,
but it does bring out

[34:40](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2080s) the key decisions around scaling,

[34:42](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2082s) plus the AWS services that it use

[34:46](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2086s) and I can imagine sharing this model

[34:48](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2088s) with a much wider audience
than the original one.

[34:52](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2092s) It's much easier to understand
what's going on here.

[34:56](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2096s) Now, once we have answered
the core questions

[34:58](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2098s) in a simpler way, we have
freed up mental capacity

[35:02](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2102s) to address additional concerns

[35:05](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2105s) that the audience is likely to have.

[35:07](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2107s) Now, I'm not gonna dive into all of those,

[35:10](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2110s) but there's a good chance

[35:12](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2112s) that you get one or more
of the following questions.

[35:16](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2116s) People might wonder, how can you maximize

[35:18](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2118s) the percentage of traffic
that is served statically

[35:22](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2122s) and how much costs this would save?

[35:25](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2125s) They might also wonder how the
solution not only scales up,

[35:28](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2128s) but how it scales down, right?

[35:31](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2131s) What is your minimum run cost per month

[35:33](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2133s) when you have very little or no traffic?

[35:36](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2136s) You show auto scaling for
the stateless compute nodes

[35:40](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2140s) but what about Amazon Aurora?

[35:42](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2142s) Do you use a cluster for
that to also auto scale?

[35:45](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2145s) You know, could the compute
nodes rather than EC2

[35:48](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2148s) be containers and run in EKS or ECS?

[35:51](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2151s) Would that be better?

[35:53](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2153s) Would it have an impact
on the other aspects

[35:55](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2155s) of availability or cost?

[35:58](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2158s) Users might wonder whether
hosting static content separately

[36:02](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2162s) right, in S3, requires
them to use specific URLs

[36:07](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2167s) and lastly, folks might want
to calculate the overall

[36:10](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2170s) system availability
based on the architecture

[36:13](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2173s) and the stated service after this.

[36:16](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2176s) The real list is likely much longer.

[36:19](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2179s) What we learn here is
that reducing your models

[36:22](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2182s) to the essence gives
you room to dig deeper

[36:25](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2185s) and answer more questions.

[36:30](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2190s) I'd like to sum this up
with one important message.

[36:33](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2193s) As cloud architects, we often over index

[36:36](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2196s) on the services we select.

[36:38](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2198s) The services are, of course, important,

[36:40](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2200s) just like good ingredients are important

[36:42](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2202s) to making a tasty meal,
but first and foremost,

[36:46](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2206s) you need a good chef.

[36:48](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2208s) So, every once in a while,

[36:50](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2210s) remind yourself that as an
architect, you are the chef,

[36:54](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2214s) you are not just shopping for groceries.

[36:58](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2218s) Now remember, a good model describes

[37:02](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2222s) a system's essential properties.

[37:04](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2224s) So, how about this model? Pretty nice one.

[37:08](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2228s) So, the essential properties
that will come to your mind

[37:11](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2231s) are gonna be pretty awesome, yeah.

[37:14](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2234s) This solution is serverless,
meaning it's lightweight,

[37:17](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2237s) without the need to
manage any infrastructure.

[37:20](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2240s) It's event driven and it
uses Amazon EventBridge

[37:23](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2243s) as serverless event bus

[37:24](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2244s) which makes the solution loosely coupled.

[37:27](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2247s) Almost without saying, the
solution is distributed,

[37:30](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2250s) is highly scalable and
of course, automated.

[37:33](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2253s) So, you deserve to be pretty
stoked about your architecture,

[37:38](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2258s) but remember that the mid-levels
of the architect elevator

[37:41](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2261s) also need to anticipate questions

[37:44](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2264s) from the organizational penthouse.

[37:47](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2267s) Here, you might find interest

[37:49](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2269s) in a very different set
of essential properties.

[37:52](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2272s) What's the business value of this solution

[37:55](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2275s) and of this particular architecture?

[37:59](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2279s) Do I have cost predictability?

[38:01](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2281s) How do I budget my run cost

[38:03](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2283s) with a solution that scales up and down?

[38:06](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2286s) Do I have the right people and skillset

[38:09](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2289s) to build and operate such a solution?

[38:11](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2291s) And event driven systems are known

[38:13](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2293s) to have highly dynamic
runtime to behaviors.

[38:16](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2296s) How do I manage those?

[38:18](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2298s) And if I need to take my
system to another platform,

[38:21](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2301s) how high will the switching cost be?

[38:24](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2304s) Once again, the questions
you get at different levels

[38:27](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2307s) will be different.

[38:29](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2309s) Tying these aspects together

[38:31](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2311s) is where the power of the
architect elevator lies.

[38:36](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2316s) But how far do you have to
go when translating benefits?

[38:40](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2320s) Let's take one popular
buzzword and try it out.

[38:44](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2324s) Now, I wrote a whole
book about loose coupling

[38:46](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2326s) many years ago, so it's one
of my favorite buzzwords.

[38:50](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2330s) It's also widely considered
to be a good thing,

[38:53](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2333s) but don't assume all
floors in the elevator

[38:55](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2335s) will take that at face value.

[38:58](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2338s) So you have some explaining to do.

[39:01](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2341s) Coupling is a measure of the
dependency between components.

[39:06](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2346s) The more dependencies,
the tighter the coupling.

[39:09](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2349s) Loose coupling allows
systems to vary independently

[39:13](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2353s) without propagating the changes
throughout the whole system.

[39:18](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2358s) It's not an all or nothing affair,

[39:19](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2359s) but a gradation with multiple dimensions.

[39:23](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2363s) So for example, temporal
decoupling can be achieved

[39:26](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2366s) with asynchronous communication
such as Amazon SQS.

[39:31](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2371s) Programming language
decoupling can be achieved

[39:33](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2373s) with common data formats like JSON.

[39:37](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2377s) Next, coupling doesn't come for free.

[39:40](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2380s) So you'll need sort of a tooling

[39:41](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2381s) and you should also expect some overhead

[39:44](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2384s) like we've seen with other architectures

[39:46](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2386s) and I'm sure you could add
much, much more about this

[39:49](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2389s) and I want that you could write

[39:51](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2391s) a whole book about loose coupling.

[39:54](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2394s) So how do you make this
digestible for the penthouse?

[39:58](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2398s) Just spooling out the buzzword,

[40:00](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2400s) waving your arms and
claiming it's important

[40:02](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2402s) certainly doesn't do the trick.

[40:05](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2405s) So you need to focus on
a few key properties.

[40:09](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2409s) I pick a limited change radius
and a limited error radius

[40:14](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2414s) as the most important properties.

[40:16](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2416s) But you need to realize
that these are still proxies

[40:20](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2420s) for benefits that the
folks in the penthouse

[40:23](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2423s) really care about.

[40:24](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2424s) You're gonna need to do
one more translation.

[40:28](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2428s) The limited change radius affords you

[40:30](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2430s) a higher rate of change

[40:33](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2433s) and the limited error
radius makes this system

[40:36](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2436s) more tolerant of failure.

[40:38](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2438s) Meaning, it degrades more gracefully.

[40:39](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2439s) It's like a limp home mode on some cars.

[40:43](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2443s) Now, if you had more slide space,

[40:45](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2445s) you could offset those benefits

[40:47](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2447s) against the increased
complexity and overhead

[40:50](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2450s) and then you can have a very fruitful

[40:52](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2452s) and an intelligent discussion

[40:54](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2454s) whether the system's
anticipated rate of change

[40:57](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2457s) is high enough to
justify those trade-offs.

[41:02](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2462s) We have seen that by
translating the buzzword,

[41:05](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2465s) you can get into a much deeper
discussion with the audience.

[41:09](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2469s) Most importantly, you made your audience

[41:12](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2472s) part of the thought process.

[41:15](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2475s) Spooling out buzzwords not
only makes you look dumb,

[41:19](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2479s) it also makes your audience dislike you

[41:22](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2482s) because it shuts them out from taking part

[41:24](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2484s) in the thought process.

[41:26](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2486s) Don't do that to the
folks in the penthouse.

[41:31](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2491s) All right, now you're
armed with the best models

[41:33](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2493s) and the best metaphors to
bring architecture thinking

[41:36](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2496s) to the penthouse.

[41:38](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2498s) But unfortunately,
that's not quite enough.

[41:41](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2501s) It cannot be boring.

[41:44](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2504s) Luckily, you're not the first
person to try to persuade

[41:47](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2507s) an audience, so you can
fall back on one more model

[41:50](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2510s) and this time, one that's
about 2,400 years old

[41:53](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2513s) from Aristotle.

[41:56](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2516s) Your audience will view your presentation

[41:59](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2519s) or any talk you give from
three different lenses.

[42:03](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2523s) They will hear your logical
arguments, that's logos,

[42:07](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2527s) they will consider your
authority and trustworthiness,

[42:11](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2531s) that's your ethos,

[42:13](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2533s) and they will consider
the emotions you invoke,

[42:16](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2536s) we call that pathos.

[42:18](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2538s) Now, the problem with most
technical presentations

[42:21](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2541s) is that the logos bubble is way too big

[42:25](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2545s) and that's understandable,
we come from the engine room,

[42:28](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2548s) but it cannot be 90% logos
and 5% ethos and pathos.

[42:33](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2553s) Your audience isn't a compiler.

[42:37](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2557s) Luckily there are
several simple techniques

[42:40](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2560s) to improve the balance.

[42:42](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2562s) Stating your experience and affiliation

[42:44](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2564s) boosts your ethos, your credibility.

[42:47](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2567s) So does citing external sources.

[42:50](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2570s) Gregor said that loose
coupling has a cost.

[42:52](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2572s) Now you have help in making your argument.

[42:56](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2576s) When it comes to emotions,

[42:57](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2577s) my main advice is don't fall
back to fear all the time.

[43:02](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2582s) If we aren't serverless by
tomorrow, we will be extinct.

[43:06](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2586s) Now, that might be somewhat
true, but as humans,

[43:10](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2590s) we have many more fruitful emotions

[43:13](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2593s) like anticipation, surprise, joy, pride.

[43:17](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2597s) So anecdotes and metaphors and great ways

[43:20](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2600s) to stir such positive emotions.

[43:23](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2603s) I have one last piece
of advice that I used

[43:27](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2607s) to become a better presenter

[43:29](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2609s) and this time, it's not
about building architects.

[43:33](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2613s) Instead it's about DJs.

[43:36](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2616s) No one captures their
audience like a good DJ

[43:40](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2620s) and you know what?

[43:41](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2621s) Most of the time, you
know the content already

[43:45](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2625s) but you're still mesmerized
by the live performance,

[43:48](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2628s) but you wanna see the smooth
transitions, the buildups

[43:52](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2632s) and the secret to success is
that, a DJ reads the audience.

[43:57](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2637s) A DJ works off prepared segments,

[44:00](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2640s) but a DJ will improvise and fine tune

[44:02](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2642s) based on how the audience reacts.

[44:06](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2646s) Now, if you're able to work this

[44:07](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2647s) into your technical presentations,
the penthouse is yours.

[44:13](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2653s) Now I hope you enjoyed this short ride

[44:15](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2655s) in the architect elevator.

[44:16](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2656s) Now you understand how architects think,

[44:19](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2659s) you have a clever way of articulating

[44:20](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2660s) the value of architecture,

[44:22](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2662s) you know how to read org
charts, build evocative models,

[44:26](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2666s) translate technical
properties into benefits

[44:28](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2668s) and deliver it like a DJ.

[44:31](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2671s) Now, there's a ton more to say,

[44:33](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2673s) so I invite you to check
out my book and the website,

[44:36](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2676s) or to connect with me online.

[44:38](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2678s) For now, it's time for
me to yield the stage

[44:41](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2681s) to all you architect superstars.

[44:44](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2684s) I already pushed the button
to the top floor for you.

[44:48](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2688s) Thank you very much.

[44:50](https://www.youtube.com/watch?v=nNbnXTl2VFQ&t=2690s) (upbeat music)

