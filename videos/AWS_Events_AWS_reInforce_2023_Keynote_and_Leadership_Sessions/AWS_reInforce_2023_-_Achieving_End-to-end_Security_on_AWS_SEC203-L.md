# AWS re:Inforce 2023 - Achieving End-to-end Security on AWS (SEC203-L)

[Video Link](https://www.youtube.com/watch?v=Khhni4Ce-Ow)

## Description

Kurt Kufeld, VP, AWS Platforms, and Jesse Dougherty, VP, AWS Network Edge Services, discuss how strong security at the core of an organization fosters digital transformation and innovation. Learn how AWS helps organizations implement every step of their security posture, from identifying risks to remediating issues. In this session, AWS leaders share their vision for security services, AWS Partner solutions, and how these can help your organization achieve end-to-end security.

Learn more about AWS re:Inforce at https://go.aws/3NbR5Jy.

Subscribe: 
More AWS videos - http://bit.ly/2O3zS75 
More AWS events videos - http://bit.ly/316g9t4

ABOUT AWS
Amazon Web Services (AWS) is the world’s most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally. Millions of customers — including the fastest-growing startups, largest enterprises, and leading government agencies — are using AWS to lower costs, become more agile, and innovate faster.

#reInforce2023 #CloudSecurity #AWS #AmazonWebServices #CloudComputing

## Transcript

Please welcome Jesse Dougherty, Vice President,
AWS Network Edge Services, and Kurt Kufeld,
Vice President, AWS Platforms. [music playing] Hello, everyone.
Good afternoon. Thanks for coming. My name is Jesse Dougherty,
as I was introduced. I'm the vice president
for Edge Services. The best way to think about that
is we have Regions, as you're all familiar with, and they have to connect
out to the internet, and I own and am responsible
for the infrastructure and software that is used to connect
and deliver that data out. So, if you think about our media
streaming services, our content acceleration,
like CDN, CloudFront, and AGA, and also, relevant to this talk,
is all of our defense systems, all of the software design
to make sure that AWS is safe from the wild world
of the internet, so anti-DDoS, bot protection,
and other types of security that run between the internet
and our regions. I've been at AWS for ten years, which is, in AWS years,
that's 70 years in the real world. Pretty much, yeah. Yeah. So, that's kind of what
I'm responsible for. Kurt? My name is Kurt Kufeld. I am the VP of AWS Platform,
which is completely non-explanatory, but the way that I like
to describe it is I own all of the pieces
that make it possible to run AWS. So, I'll just go through
those real quickly. So, I own commerce platform. You can think about that as billing,
although it's a lot more than that. It is metering, it's bill generation, it's pricing plans, it's payments,
it's foreign exchange. It's basically everything
except the books for AWS itself. I also own identity, and identity, you know, the most common thing
that you probably know is IAM, but it's also everything else related
to identity and access management. So, it's organizations, it's Cognito, it's tagging,
it's the legacy identities, like Managed Active Directory, and that service,
basically every single API call to AWS goes through IAM. I also own the console platform, so not the individual consoles
from the service teams, but the overall platforms,
so what we use to really try and derive some consistency
across the platform. If you think about AWS five,
six, seven years ago, there was, you know,
pretty disparate experiences, and we've really tried to bring
that experience together and to provide a much
better experience for our customers. I also own infrastructure as code. So, you can think about that
as CloudFormation and the CDK. I know I forget something
here somewhere. I own external security services. So, think about that as things
like GuardDuty, Inspector, Security Lake,
which we announced earlier this [INDISCERNIBLE] last week,
and then I own automated reasoning, which is, we say mathematically
provable security, but really, use mathematics to prove
correctness of certain things, and this has been done for years,
but we've really managed to kind of bring that more out
into the mainstream and make it more… make it easier for people, and I'm certain I've forgotten
something in there. Oh, I've been with Amazon 23.5 years
and with AWS for ten. So, Kurt, as someone
who predates AWS, has been around for a while,
and we're here to talk about… I remember sitting in the lobby
when they were going to talk to Jeff about doing AWS. That's a pretty cool… we'll get to the origin story
maybe later, but so, I mean, I'd be curious
to hear your talk, your take on what does
end-to-end security mean in AWS? It's a good question, and one of the things
that I really want to do as, you know, kind of owning
a lot of that today is I see a future
where really security is simplifying
all of the disparate things that you see today
and simplifying the complex and making it just easier
for our customers to implement that. You know, too many leaders have
traditionally viewed security as kind of cumbersome, like it's
something you do at the end. It's this carbuncle
that you kind of put on top, and it's complicated, you know, by the global shortage
of security professionals and by the threat landscape, which is changing
pretty significantly, plus there are data
protection privacy commands, demands, excuse me,
that are coming up over time. So, it's really getting a lot
more complicated out there, and I really look at using, taking all those things together and using them to simplify
security implementation. Maybe a terrible analogy,
but I'll use an analogy. That simplification,
I want to use security as really an opportunity
to move faster. Think about it like brakes on a car. Brakes on a car are to
slow a car down, right? Well, no. Brakes in our car are there
so that you can actually go faster, because it makes it safer, and the way that I think
about my job, as security, is I want to take,
and our team wants to take. and AWS wants to take
and make it easier for you, so that you can move
faster as a business. Yeah, what's interesting
about this, too, is when you… when you think about security
as an idea… - Don't look at me as you're talking.
- I'm not. - Okay.
- I refuse to. We did actually practice that part. You know, when you start to change
your mental model from security being an enforcement wing to being something
that can make you go faster, it does change the way
you look at a lot of it. You start thinking of it as being
a proactive part of your business and not a reactive part, and that's certainly how
we've looked at it internally, is that security is part of
the products we build, and actually, often,
in our own design discussions, it's like the most important part, because it doesn't really much matter
what feature you add if the system isn't
really trustworthy, and you don't want to put
that kind of critical data in it, then it's not that useful. So, we'll spend a lot of time
making sure that it's secure right at the very beginning
and automated out of the gate. So, I think that's what I feel like
when I hear you say all that. It's critical. Can I just… I want to add
a little bit on to that. Is that all right? Yeah, of course. So, here's the way that we think
about our priorities at AWS. The single most important thing
we do is security. The second most important thing
that we do is durability. Never lose anybody's data. The third most important thing
is availability, and then features and service
launches are everything else. What's it, and now, obviously,
security, durability, availability,
they're deeply interconnected, but that security is first,
and that happens all the way through. So, it's not like you have
a security team that kind of comes in and tells you
what security to implement. Every single developer,
every single person at AWS is responsible for security
every single day, and our security team
is there to provide guidance and to basically help us
move more quickly. In many companies,
security is the Department of No, and for us, the way we think
about security is how do we enable our developers
to move more quickly. Does that make sense? Absolutely. So, when I think about it
from within our groups, how does it actually help us
move more quickly, when we take the security process, like kind of reviewing
what's being built and deciding how safe it is, the earlier we move
that into the design process with the engineers and builders,
the more creative we can be, the more degrees of freedom we have,
and the more flexible we can be. So, if you've got this…
the term is often used shift left, but if you bring that into a robust,
creative discussion with the builders and product groups
at the very beginning, you'll find a few things
that you can enable with security, and you'll very early identify
some things that you should absolutely not do
in order to create a secure platform, and finding those
at the beginning is critical, and doing it as
a collaboration is critical, and one thing I was
thinking earlier today, an analogy is in some
software design systems, you remember like
there's the sequence where the product manager
comes up with an idea, hands it to the engineer,
who interprets it and builds it, who then takes it over, and maybe we get some feedback
through an alpha, maybe not, and then you ship, and that sequencing can lose
a lot of fidelity and creativity. There's not as much of that kind
of iterating internally about how innovation
supports new functionality and how new functionality
can drive innovation. So, if you think about it,
the shift now, of course, is to have product and engineering
very closely connected and iterating. So, now, just shift your thinking
and say, well, let's put security in there
too, or security expertise. So, that becomes exactly part
of that same rich discussion, and I've seen many situations
where we've taken a very hard line on the security stance for a product. We will only do this, and it
would almost sound impossible, the thing we were going to do,
but it wasn't, because we thought about it
at the beginning, and we could actually
invent something that hadn't been done before,
that would enable significant value, because it happened at the beginning,
and that creates a lot of speed, because I bet you many of you here
have had the experience, where later in a project,
you discover something, and it's a hard lesson, because the cost of undoing that
and trying to figure out how to address could be as much
as this project's going nowhere to months
and months of rework, and so, there, you can see
that as being a headwind to productivity and speed. I actually have a great example,
if you don't mind. Sure. So, hopefully, everyone here
uses encryption on S3, and when we built encryption into S3, we rethought how we did everything,
because had we not done that, had it been something we just
added on, it wouldn't have worked. It would have been too slow. It would have been
extremely expensive, and the way that encryption
is implemented in S3, it's literally invisible
to our customers, certainly, from
a performance perspective and just really enables
that ability to do that, and the reason that that's possible is because you think about it
as part of the design process, and today, with encryption,
we do that for everything. You can find equivalents
in our network, in the way we've designed
the EC2 network, to allow security to be built
in right at the foundation. The same is true of almost
all of our systems, because it was brought in
at the very beginning, and the nice thing about
when you bring in, like, this early innovation
with builders is you now have security
becomes more like teachers and a creative role
as opposed to a restrictive role, because you'll see
these really fun discussions where security professionals
start to become really well-versed in
architectural possibilities. like, hey, we could do this,
I learned from this other project, and it becomes an enabler, and so, your security folks
are doing more strategic work, moving out of kind of
an audit and control, though that's still very important,
into a design and innovate mode, and I think that creates more
long-term value for the business, when you start to have
that creativity upfront, because you'll start
inventing things that, I think, like S3 encryption,
like our network technologies, they pay off over the very long-term,
because you're able to invent that, and a secure platform
means you're going to be able to move into
new markets more quickly. You're going to be able to take
on new workloads more flexibly. All of those things become options that would have been expensive to do
if you late minded them, and then I think one more way
it makes you fast: sometimes, if you think
about the security aspects of a product too late, it creates a lot of toil
and randomization for your team, just lots of extra work
they have to do. Like, think about a product
that wasn't necessarily designed to be operated in the environment
you're putting it in and just how much extra
work your builders and your technologists have to do. It's a retrofit. It's a retrofit, and as a result, you spend too much
of your builder's time on stuff that isn't direct value,
because you're not using it. It's not fit for purpose
in that sense. So, if you think about it, like,
fewer surprises at the end, security doing more strategic work, and less toil are all ways
that thinking about this end-to-end can really help you move
more quickly with security. I just want to add on to that
a little bit. Like, when you, I actually
hate the term shift left, but when you shift left, and you start doing
a lot of that early, it turns out a lot of the systems that I own are security related,
just like yours are, and the security team is not this
outside team that comes in. They're our partners,
and we work with them on a day-to-day,
regular basis, even though, and I think this is
the right thing to do, they report up through
a different structure in order to have that accountability, but we really work together
on a continuous basis. Yeah, you know, I was thinking
about this toil concept too. Like, if you think about dealing
with security situations in an organization, there's often a lot
of what I call squabbling, but finding logs, moving here,
connecting things together, trying to figure out
the relationship between things, and I was going to say,
this feels like something GuardDuty has really been helping people with. Yeah, it has. -Thank you.
-You're welcome. I happen to own GuardDuty. So, we've launched a bunch
of stuff in GuardDuty to help with some of this
undifferentiated heavy lifting, the toil. We've launched GuardDuty protection
for containers, so that it's easy for you
to bring all of that information in from inside of your containers. We've launched GuardDuty protection
for databases, so that we know, and you know
what's going on in those databases, and for your other serverless
workloads, GuardDuty for Lambda, so that you can bring
all of that data together, and with just a few clicks
in the AWS management console, you can now achieve
and activate GuardDuty across all of that estate,
multiple accounts, multiple regions, and you can do that in a very simple, secure by design infrastructure,
the AWS cloud infrastructure, and migrate and mitigate sorry,
migrate, mitigate those threats early and simply by just using GuardDuty
to do the analysis, initiate the automated responses, initiate the automated finding of
any issues that may come up. So, GuardDuty is really one of
those things that we're trying to use and that we're really focusing on in order to make that much simpler
for our customers, so that you don't have to bring
all those bits and pieces together and make it…
do it in a very complex fashion. Let me provide you with an example. So, Warner Bros Discovery
recently paired GuardDuty and Amazon Detective
to help them really kind of simplify a lot of their anomaly
detection and their agility. You know, before they did this, their security engineers would have
to take logs from various systems. They'd have to take logs from AWS, they'd have to take logs
from their cloud providers, they'd have to take logs
from their services, and they'd have to put them on a sim, and then they'd have to look
and build systems to detect anomalous activity. It's tedious, right? It's just work, and it doesn't
really allow them to innovate on the core value
that they bring to the customers, but with GuardDuty, they were able
to simplify a lot of that and reduce
some of the complex querying and some of this massive
disjoint datasets, and we could just work with them
and do it for them. That's cool. So, one of the things… What would you like to…
what else do you want to talk about? I'm going to talk about how we create
the culture for this stuff. Sure. So, once you're trying to figure out,
okay, I like this end-to-end security idea that these guys are talking about,
I want to be fast. There's always this question
about, okay, so, what do you do to enable it, and I can share with you that what
I learned when I first joined AWS and what I've learned
since is what has been really critical has been the creation
of the culture that enables it. And I remember, like very early
when I joined AWS, I had heard before, you know,
security is important from… many companies say that, but this is the first place
I had seen where it was modeled daily
by senior leadership. At the time, Andy Jassy as our CEO, would personally get involved
in auditing and getting deep into issues and making sure
everyone understood them and reinforcing, on a regular basis, that security is absolutely
our top priority, and you'd not find
very many people who would… Can we talk about
weekly security meeting? Yeah, sure. Go ahead. So, one of the things that we do
is we basically review, whether it's an operational issue,
whether it's a security issue, we have a process that we use
to drive continuous improvement. Security is one of those, and our most senior leaders
get involved in that. One of the things that we do
is the CEO of AWS has a weekly meeting where they
review any security issues, any things that we may be driving, and this is not the meeting
you want to get invited to. I have the dubious honor
of being there every week, but what's really important
about this is it sets the tone. Everybody cares. Everybody drives it,
and it is about teaching. It's about understanding, and it's about
that continuous improvement. I think one thing that's important
about this too, so, I have a similar, smaller scale, slightly less scary meeting
with my team, and we get together on a regular
basis, on a weekly basis, and we get into
very high levels of detail on the security programs
we're operating, any the security issues
we need to work on, and the reason we get into
the high level of detail is there's a couple of them. One of them is I'm
an incredibly curious person, and I can't help it. Second one is by having
those rich discussions about the deep details,
the technical and the ones related to software/hardware,
my teams all understand that they have to know
that stuff when they come, and for them to know that stuff, they had to have been
deeply in it themselves, and their directors
had to be deeply in it, and because, by having those,
as a senior person, getting into the details like that
and paying attention to them, asking the tough questions, understanding them
on a regular basis, it creates a machine whereby your whole org
pays attention to it constantly, and I have, if you let off the gas, it will get overrun by the other
major priorities in the business, feature launches, like whatever other pressures
are coming into that business, and so, staying closely connected and very into the details
helps maintain it, and I think, coupled with that,
you can't always be about bad news. My own experience as well
is it's also just as powerful
to celebrate progress, and celebrating progress in this
is not just the big things. I find it's really powerful
to celebrate an individual builder making a simple choice
to improve that improved security, even in the smallest way, because they chose
to raise that in a meeting. They chose to potentially change the way the product
was going to evolve, or they spent some
extra time working on it. Rewarding the small things
reinforces the culture, I would say almost more
than recognizing the big things. I think the big things feel a little
bit performative sometimes, like, hey, way to go on that launch, and also, what happens
is you encourage people to bring those ideas up
in the meetings that may be disruptive
but may be critical, because they know that they're
respected and required by leaders. So, I think that part of
creating a culture and the leadership dedication to it is absolutely critical to giving
the team members permission to prioritize this work
and stand up for it in all the meetings you can't be in, which is where a lot
of these decisions get made. Yeah, it's interesting
that you bring that up, because my team runs the same way. I run weekly security meetings
for my various teams and the same sort of thing,
and we go very, very deep into those. For some of them, I have…
where I can't participate, I have leaders that are at my level,
and they participate there too, and it's not just the, you know,
when something happens, but when the good things
happen and celebrate those. It's really interesting. When you've got security integrated
end-to-end, like, it's a great optimization
of time and resources, and when you think about it early,
you end up in a different place. Since we're using car examples,
I'll provide you with a car example. This is a…
I love to use this example. So, there are two car manufacturers,
whose names I will not use, but I'm certain
you are familiar with, and one car manufacturer starts off
as building a luxury car and adds performance. The other car manufacturer starts off as building a performance car
and adds luxury. They're both great cars, but they end up
in very different places, and the point there is if you start
with security at the beginning, and then you build,
you will end up in a different place. You'll be more secure. Now, one of the things that we
really worry about at AWS is how do we give our customers
more bang for the buck, how can we build services together? How do we make that easier
for our customers, and one of the things that you get,
I think, out of the cloud, which is different
than what you got on-prem, is that you get improvements
on a continuous basis. So, whether you're using
GuardDuty today, or IAM today, tomorrow,
it'll be different. The day after that
it will be different, and we're continuously improving. We're continuously changing,
and you get that for free, because we just do that. It's part of what we do. So, you're continuously improving
the infrastructure that you're running on. You're not buying a fixed
set of capabilities and then having to upgrade
to the next of the security or the next, next of that. You're just getting it
as part of the services. It's the continuous investment
and improvement in technologies that you just get out of the cloud. Before you get on with that. Sure. In my space, we do… we have, in the Internet safety
and security space, we have very active adversaries,
if you think about it. Really? People never noticed. You've got people who basically
run these services like their own little businesses and try and find ways to disrupt
your businesses in general, and so, as an infrastructure… Let me interrupt you there, actually, there is a, I'm trying to remember
the name of the company, but there is… they literally
run them as a company. They do, yeah. They have HR departments. They have, like,
employee of the month, like, it is… these these adversarial businesses
are run as a company. Secretly, I prefer it
when they do it that way, because they're easier
to find and shut down, but when you think about choosing
an infrastructure provider for security,
you want one that has it built in. You want one that has obsession
with security, like we've talked about, and you want one that's going to,
like, constantly evolve, but sometimes that rate of evolution
has to be very fast, like in a situation where
you've got an adversary, you know, we have, in my group, we have these dedicated
researchers across the globe who are able to look at,
and this is kind of cool, so, we have like a global backbone. It connects to basically everything. It spans the Earth, connects almost
every ASN on the planet, and we're able to gather
incredibly interesting telemetry about what traffic looks like
in various situations, when there's a soccer game,
a football game. In certain European cities,
their network looks amazing. There's all sorts of cool stuff
happening. The same thing is true of
when there's news events, or when there's other
legitimate events, we can tell, and we can see the difference
between that and malicious activity, and we can learn
from such a broad estate and be able to bring that in,
apply machine learning to that, apply our judgment
from our security researchers, and develop security practices
that prevent attacks before customers see them, before any of you see them. That's another example where you're, by betting on a piece
of infrastructure, a cloud infrastructure, and moving
that security practice down, you get the benefit
of this constant evolution, but at a very fast pace,
so that you don't have to, which is really kind of the key, because you want to
spend your resources on building your businesses, not building up
your own defenses against… you don't want to end up
an invention battle with these motivated adversaries. Great callouts. I'll give them an example
of one of the ways that we're continuing to innovate. So, I own AWS
Private Certificate Authority, and I'm happy to pre-announce today
the availability of AWS Private CA Connector for Active Directory,
and enterprises that use Active Directory and use AD
to manage their Windows environments need this
in order to basically do PKI with their environments. With AWS AD Connector for Private CA, you can replace all of this expensive Microsoft Private CA with a secure,
easy-to-use, and available service
that we manage directly. It's another one of those places
where we just want to make it easier and remove that undifferentiated
heavy lifting for our customers. I'll give you another example. We recently launched AWS… Hold it. Do you want to interrupt me? No, no. I was about to cough. I'm sorry, go ahead. No problem. We recently launched
AWS Payment Cryptography. So, if you are in the payments
industry, that is,
you have to process payments, you probably are familiar
with the fact that you need to run payments HSMs. You need to create
a constellation of payments HSMs, you need to put them
in datacenters, you need to hire people
who can manage these, and they're pretty fragile, and it's just stuff that you need
to manage in order for you to really do your core business, which is processing those payments
or doing other parts of that, but with the launch of AWS
Payment Cryptography, it was… I always try to say payments,
but Payment Cryptography, you can secure your data,
and you can do that without having to run
any of these payments MSMs. It's a service that helps you reduce
your operational burden, and it uses a fully managed service to meet all of your payments
and PCI requirements. So, we've just launched that, another example where you kind of
get things in the cloud as they as they come through. Do you want to talk about Zero Trust,
or should I talk about Zero Trust? -Why don't you kick us off?
-All right. One of the big buzz phrases
out there these days is Zero Trust. I actually don't like that phrase, but I think it's a good phrase
to maybe just say, how do you make sure that,
on a continuous basis, you are checking every API
call every time you access something, every time that you want
to do something, reevaluating and checking to ensure that the request is coming
from a trusted source. Used to be, remember
the eggshell, the squishy egg? Yeah, yeah. Right? Hard outside, soft and gooey inside. We want to make sure that everything
is hard all the way through. I'll give you just an example. Amazon as a company has been working
on this for quite a while, and the laptops
that we carry these days, as an example, we don't connect
to a corporate network. We evaluate our access
to all of our applications, to everything we do,
on a continuous basis. So, we do analysis of are you
running on a supported platform, are you up to date, are you connecting
from a trusted network or an untrusted network,
and we may treat you differently. So, Zero Trust also comes up a lot
with our customers today, because a lot of customers
want to go to this environment where you effectively
never trust anything, and you have to keep doing that
on a continuous basis, and we deeply believe
in the outcomes and benefits that this model delivers for us. So, you know, you can apply
Zero Trust concepts, rethinking identity,
authentication authorization, and do that in meaningful ways
in order to improve your security. The next chapter for us in this is to comprehensively address
those cases for our customers without the need to stitch
together those multiple services. For example, every time
developers build an app, they have to create permissions
for application resources, and we believe we can simplify this. We can reduce the toil
that's involved, and AWS can help you
establish common ground when you build these applications. I've gone blank on the name
of the service that we just launched, the language that we just launched. Cedar. Thank you. I actually hadn't gone blank. I just wanted to give him
something to talk about. So, late last year,
we launched Cedar. Cedar is an open-source system that allows you to define
access management in your applications,
so not as you access AWS, but how do you
build access management into your applications themselves,
and what's interesting here is that nobody's really addressed
this problem before, and when you've built applications, you've had to figure
all this out yourself. So, with Cedar, you can define
the access management for your applications, and we once again remove
that undifferentiated heavy lifting, and then once you need
to evaluate it, we launched AWS Verified Access, where you can use that service
to actually evaluate those Cedar policies every time that
you need to get at something. Yeah, when you think about it,
we've kind of covered… we think about Zero Trust…
I'm a network guy. So, I think about Zero Trust
as being… considering a lot of the things
you talked about, but also, network conditions, and so, if you think about
the mix of things we've launched, we've launched Verified Access, so, kind of like remote access
for a desktop. We've launched VPC Lattice, which allows you to do
constant reanalysis of the access or the flows between your VPCs
and data in a very simple way, and then Verified Permissions,
so that when you build an app, you can build all this in yourself, so that you can control
the permissions between tiers in your own application and make sure that that Zero Trust
is carried all the way through. So, if you use all these together, you can get kind of an end-to-end
Zero Trust story. The thing I like about both Cedar
and the Verified Permissions is not only have we made
it easier for customers, but we've used automated reasoning to prove correctness in those spaces. Yeah, it's a pretty cool
characteristic of Cedar, that it can be done that way. I think that's worth
paying attention to. One of the hard things to do
in security, of course, it's easy to say,
let's stop Kurt from accessing this. It's very hard to say
who can access this. I think those sorts of problems
are going to be critical and part of the powers of Cedar. So, one thing about cedar
that's interesting, too, -is it's open source.
-Yes. So, this is part of… is an important
part of our Zero Trust story here, which is it needs to be adopted
broadly, and it needs to be… it needs to engage
with the community. So, I'm curious to hear
your thoughts, Kurt, on end-to-end security, Cedar, and just the partner landscape
that we work with. Absolutely, and we've worked
with partners on this, not only partners
helping our customers, but partners helping us
to define the language, and by using security technologies and consulting services
with these partners, they're with us in the trenches
as we innovate for our customers. So, these customers help us,
and these partners help us, to really be successful. I'll give you another example. Just two weeks ago,
we launched Amazon, sorry, GA, excuse me, for Security Lake,
for Amazon Security Lake, and which automatically centralizes
your organization's security data, and when we built this,
and we built OCSF, the language, the protocol for how you get
everything into Security Lake, we built this with over 35 of the biggest providers of security
out there: CrowdStrike, Datadog, and others that were really
with us on this journey, so that you can bring
all of that data together within your AWS account,
your on-prem data, and then do analysis on top of that, regardless of where
the data comes from. You can use your, you know,
also, it turns out some companies are better
at some things than others, and thus, you can use
your preferred provider for your security and your analytics and do so with a centralized data lake, so that you don't have to
build all of this yourself. We worked with partners
to build all of this, and, you know, our customers
put all of this into action, and when I think about
how they should start with not just bringing
all of that data together, but how should we think about that
end-to-end security for our partners and for our customers. True. Well, so, so, far, we talked about
what end-to-end security is. We talked about some cool innovation
to make it possible. So, now, I think we should
probably talk about how do you actually
start and get there. Yep. It's kind of my favorite part. So, I talked earlier about step
one being the mindset, right? The cultural transition. How does leadership apply themselves
to start making the change? Moving to a partner as opposed
to the police model, and that sounds… it's easy to say. It's an enormous amount of work, and it requires a lot of commitment
from a leadership team to put in the time to maintain that. So, it sounds simple.
It's not at all. It might even be the hardest
part of this discussion. Once you're in that mode, you look
at what you're building, and you need to think about which
of the parts of my security practice really should be part of my platform and not part of my general
application and business. Which parts do I want to delegate
to a platform provider and which ones do I want to own? And the answers will be different when you ask that question
for this year and for the long-term, right, so, if you look at them
over two time horizons, and start to say,
look, I really want, over time, to be betting on this security
being deeper in the infrastructure
that I build on. So, I have to build less of it
myself, and again, that sounds really simple, but it will drive a lot of
interesting debates internally as to what the true business is
and where to invest, but I think it's a critical step, and this is where I think
it's really important to think about, when you're looking at
an infrastructure provider partner, you're looking for a place
where that security is going to be
constantly pulled down. You want to make sure that you're
aligning with a provider that is… that that is their mojo. That's what they do. For us, for example,
as we mentioned earlier, we build it into everything we do
at the very beginning. That's made the infrastructure
suitable for financial companies, government agencies,
healthcare agencies. Because we thought about S3
encryption and network protection at the very beginning,
now, these heavily regulated and heavily security
conscious companies can move on, and because we keep doing that, it makes it kind of easy
to bet on our infrastructure as the place security
will continue to grow, and so, one thing,
I'll give you an example of this, which is one of my favorite ones,
because it was such… it was something that we really
didn't have to do, and that's Nitro. I'm sure many of you
are familiar with Nitro here. Nitro, if you're not,
is a hardware device that we built for our hypervisor. The hypervisor is the thing that
switches between virtual machines, makes sure that it does scheduling
of CPU and memory access, so that you can virtualize hosts, and one of the things
that we decided early on is it is unacceptable
for anyone in AWS to have access, administrative
access, to the virtual machines. It's interesting. I was in those discussions early on, and there was a lot of back
and forth about it, but in the end, the right thing to do was to ensure that nobody could get
access to Nitro when it was running. And so, what's fascinating about that is you've got a company debating
about spending resources and inventing something
that will reduce their own ability to access and manage something,
knowing it's the right thing to do, and that's just…
and that has paid off very well, because now, we have all the systems
we need around that to manage and make sure things
are operationally strong, but at the same time,
we can easily say to you, look, we've provably made it
such that these are yours. These are not something
that we can access. It's also interesting
because one of the things that, you know, I talk to customers about, and that customers worry about
is, well, what happens… because let's face it,
software is complicated, what happens if somebody,
you know, owns the hypervisor. Well, with AWS Nitro,
that's not even possible, because there is no hypervisor. The hypervisor literally
is in a separate system that is inaccessible from the systems where the virtual machines
are running. Yeah. So, I think if you
look at the steps to take, there's this identifying the things that you want to move down
into your infrastructure, and then there's operationalizing
what you're doing. Right? There's this idea that you now
need to figure out how to work, build the processes and mechanisms
around what you're doing, such that you're keeping
security early in the design system, and that you're making sure that
you're betting on the infrastructure, because as you all know, a decision made once
has an effect once, but if you build
an ongoing mechanism, you can ensure that drives
the change you're looking for. -If I can share an example.
-Sure. So, there's a company
that we worked with, Unqork, and it's a great example of how the organizations
really embrace this security is a partnership
with development example and shifting that security earlier
into the development process. You know, their security teams,
over the years, used to be point-and-click
security operations, you know, really to building security
in as part of their code. You know, they've operationalized
the way security interacts with their developers and engineers, making sure that they build
that security into that development process early, just like we have done
over the years, and, you know, everything from
pre-commit to pre-commit hooks, pre-vetting, pre-approving
design patterns, and working with them early on. They're even helping develop
their teams and development teams kind of level up their own skills,
level up their own security, to be able to threat model
their own applications, and this is really
something that you… that I would certainly
strongly encourage is it's every developer's job
to build security and to be secure all the time. So, you know, I love that example. It's important, and I love seeing
customers pick it up and start to get the speed
benefits of it as well. It's really part of the things
that makes my job really, really rewarding. Once you've gone through
the first steps I mentioned,
you're moving things down, moving things early, and then of course,
you need to step back and say, well, am I reasonably covering
all of the levels of security and compliance that I need to cover
as part of this program? And so, having a programmatic way to measure your progress against this
is a key part of it. And here, there's usually a framework
that will be adopted, something like NIST or the AWS Well-Architected Framework
that you can, if you're using a consistent
infrastructure for your security, it makes it much simpler
to measure against that, and you can use something
like Security Hub to go and say, oh, let me look at my applications,
my true infrastructure, and give me a sense of where I stand
against these on an ongoing basis. And what's interesting here
is you select your frameworks, you start to understand
where you're at, you can use that to drive
your practices over time and ensure that
you're staying current, and of course, as you mature in this, you can develop your own
frameworks and decide, oh, I would like to focus
more on this and this. And I think that that framework
approach, plus getting help from partners
who have expertise in this area, is an important part of
making sure that, as you're shifting, you are getting really good coverage
across the security landscape and what you're attempting to do. Yeah, I mean,
I'll give you an example. So, we have more than 300 services
and features, I think, related to security at AWS, and this can be
a little overwhelming, but you're talking about frameworks. Like, one of the things
that you can do is you can use something
like Control Tower to kind of set up your landing zones and kind of set up
that baseline for you, so that you know that,
within this framework, you've met the Well-Architected
design suggestions that we have, and then not only,
and you've mentioned this already, but not only do you have them set up, but do they continue
to be set up the right way. You can use Config to check that. You can use AWS Systems Manager
to manage that, and we have predefined
a lot of those controls, a lot of the standards
that are out there in order to help you meet
PCI or HIPAA or things like that, and you can just do that kind of
right out of the box, without you having
to do all that work. It's critical to automate
all of these things. I think automation is a really
important part of this. Automating your audit, automating the testing
of your security infrastructure is all very key, and I think, because again, you don't want to be
dedicating fixed time to that, resources to that. The one thing I would say, too, is once you kind of
get into this idea of you've got your framework, you've moved your engineering
to the right places, you really need to start
thinking about, okay, well, how am I
going to scale this. I have, in our case,
very many hundreds of teams, but you could say, I've got… More than 850 the last time
I checked. So, you're starting
to scale this out, you're growing your businesses,
and you're investing in new things, and learning how to make sure
that each one is building on this philosophy, I suppose, this set of mechanisms
that you've created, and I think this is really important
is to do intentionally, is to say, okay, now,
I really want to make sure that I'm planning on
how to scale this, so that my teams can pick it up
and move quickly, and so, it's something that requires
programmatic focus from leadership, and in here, you need
to bet on something that's going to provide you
immutable infrastructure. You want to be able to provide people with really nice places to start. So, you use landing zones
and Control Tower to set up the account infrastructure,
use Organizations to set policies, but then you use something
like CloudFormation, some of these things to start setting what are the ways that a client
facing mobile app looks in our world, what is the shape and size
and the configuration of that, and when you're designing that
in an intentional way, you can also use things
like serverless, something to extend
and automate that. So, the automation goes with it, so that the people who are
running the applications don't have to go and design that. They simply take this off the shelf,
they put in their logic, their bits, and they're already taking advantage
of all the other standardization and the other work that you've done, and then they're able to deploy
this safely in your infrastructure, and then you can iterate
on that over time. You can grow it, but then you don't
have to worry about the quality of this end-to-end security program
you're running degrading as you grow, because I think that's a really
important part of this practice, is paying attention to it,
and I'll go back, because I've only been there
for ten years. So, I'm a junior
compared to Kurt here, but when I started,
I remember going to our regular, one of our regular audit meetings, and at the time,
the meeting was small enough. This is our ops meeting at the time. Yeah. You all go into this one big room,
and I remember being just awestruck, because we had 13 AWS services, 13. I was like, there's absolutely no way we're going to be able
to scale beyond this. It's just it's just too much at 13. I think we have, in terms
of actual services now, I believe, we're well over 300 now. We've got… Yeah, I know the last number
I saw was over 285. So, it could be over 300. But that scaling from 13 to 285 is exactly based on what
we've been talking about, and it has been an intentional
set of efforts by leadership to create that scale environment
without increasing risk, and as I've been through it,
and I'll admit, a few times, I was like,
we're not going to make it. The next level is going to be
too much scale, too much pressure, and the truth is, with a lot
of leadership dedication, a set of systems like this, it does create very few barriers
to continuing to scale while maintaining
your security rigor. Yeah, totally agree. Which I would say is probably
going to be very difficult if you stick with
a traditional police or kind of a post-facto audit model. It doesn't it doesn't scale at all. In fact, the bigger you get,
the slower you go. And I think, yeah, you end up
having to hire, you end up trying to solve
the problem with more hiring. You end up with increasing risk
when you increase your velocity. Like, these things
start to work against you. And as the world changes, and the world's changing
very quickly right now, that type of an approach
doesn't really keep up, does it? No. No, I mean, the world
changes so quickly. Like, think about
where technology is today versus where technology
was even six months ago. As a business, trying to govern
your infrastructure and technology, you have new things to think
about and to innovate on. What are you thinking about here? Well, it's funny you should
mention that, Kurt. Personally, I think about things
like generative AI, and how it will put pressure
on and change the way we think
about data governance and being smart about how to put
the right boundaries around it. I'm curious to hear
your thoughts on this. Well, it's interesting. So, let me actually spin it
the other way first. We're already seeing generative
AI being used in attacks, and so, not only is it going
to be interesting in how we can use it for security, but it turns out some of those folks
out there are very smart, and they're using it
the exact opposite, to help them really try and take down
some of the security barriers we have today, but I think here
there are several areas. One that we're going
to use generative AI with is I think we can use it to help actually make implementation
of security easier, and that's an area
that we're looking at. Also, I think the other area, and this is an area
that a lot of companies, this is kind of where a lot
of companies are right now, is they're thinking, all right,
I've got these models. Now, I've got my own data. How do I use my own data to help, you know, kind of train some of this? But I don't want my data to leak out, and, you know, we have some systems
that we've recently announced, like Amazon Bedrock, so that customers can start
using generative AI and use it in a safe way and use it such that they are able
to improve the models but still keep their own data
for themselves. It's a multi-layered approach. It has bar-raising
security controls around it, and you get all of the standard
AWS controls as well, plus you get Config and CloudTrail to make sure that you continue
to be protected as you're doing this. Also, as you continue to scale,
and as you grow your business, what can I use generative AI, or what can I use other systems
for in order to help with this? I think this is the point of the talk where I admit that I jumped
into part of this a bit early. I think what would be interesting, Kurt, actually, is let's talk
about the scale part. I think you had a great example around who's been effective
at actually scaling. -You mean by Botprise?
-Yeah. Okay. So, there's a company
that we work with, Botprise, a great example of scale. They're a startup in cloud security and the automation industry. They've aggressive growth goals. They were challenged
with scaling effectively, because they needed
to meet stringent requirements for their own security
operations and automation, and what they did is, in 2022,
they went through the AWS Well-Architected review process, where they learned
kind of how to measure, how to build architectural
best practices and do that security early. They reviewed the provided guidance on how they could work
with some of those security gaps, and by building
their automation solutions on the AWS infrastructure,
using AWS security solutions, like Security Hub,
GuardDuty, Inspector, they were able to move more quickly. Botprise built their security
solution in one year, when their usual time-to-market
was double that. So, it's really helped them
accelerate. They continue to increase
their customer base, and now, the company can scale
in a cost-effective way as they're continuing to scale,
just by scaling AWS. Yeah, I think that's really
the key takeaway here. I mean, that's of the things
I've tried to highlight here today. -What's that?
-Did you just call me Peter. No, I didn't. I said that's one of the one
of the great takeaways from today, Peter, is, you know, there's a series
of technological changes, the products you need to consume, and there's a set of cultural
and leadership techniques that are necessary
to make this happen. It's not a simple use
this product; this will happen. It's not a simple use
this leadership approach; this will happen. You have to think of it holistically
to get end-to-end security to work. You have to think of a cloud platform
that has this built into its DNA, that you can bet on growing
with your business, and then you need to think about
how you're going to get your teams and practices to start
bringing security earlier and then scale those practices
out as you grow and make sure your cloud
can do it with you. And I think all of that adds up
to this last story, which I don't want to undersell here, which is this will
all make you faster, and I think, in the end,
this is really one of the keys here, is being able to innovate
and adapt to new challenges, deliver more for customers, and do so through
the practice of security, as opposed to in spite
of the practice of security, and I think it's really important. If you left with one thought
after this whole discussion, it would be that. It would be that if I tweak the way
I approach security, and I think about it as a creative
part of my building process on a strong infrastructure,
I think what you'll find is that you'll be able
to deliver much more quickly and with much more security, and I think it'll be much better
for your business and your builders. Yes, your builders
will love it in the end. So, great example.
Great story. Love it. I hope we've been able,
we're getting towards the end, I hope we've been able to provide
some inspiration today on how everybody can take some time
and build your own security culture, build the guardrails
that you need to, and then keep the innovation flowing, and be able to actually
move more quickly. [music playing]

## Subtitles with Timestamps

[00:01](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1s) Please welcome Jesse Dougherty,

[00:03](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3s) Vice President,
AWS Network Edge Services,

[00:06](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=6s) and Kurt Kufeld,
Vice President, AWS Platforms.

[00:11](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=11s) [music playing]

[00:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=21s) Hello, everyone.
Good afternoon. Thanks for coming.

[00:24](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=24s) My name is Jesse Dougherty,
as I was introduced.

[00:27](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=27s) I'm the vice president
for Edge Services.

[00:31](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=31s) The best way to think about that
is we have Regions,

[00:34](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=34s) as you're all familiar with,

[00:36](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=36s) and they have to connect
out to the internet,

[00:38](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=38s) and I own and am responsible
for the infrastructure and software

[00:42](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=42s) that is used to connect
and deliver that data out.

[00:44](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=44s) So, if you think about our media
streaming services,

[00:49](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=49s) our content acceleration,
like CDN, CloudFront, and AGA,

[00:54](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=54s) and also, relevant to this talk,
is all of our defense systems,

[00:58](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=58s) all of the software design
to make sure that AWS

[01:00](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=60s) is safe from the wild world
of the internet,

[01:02](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=62s) so anti-DDoS, bot protection,
and other types of security

[01:06](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=66s) that run between the internet
and our regions.

[01:09](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=69s) I've been at AWS for ten years,

[01:11](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=71s) which is, in AWS years,
that's 70 years in the real world.

[01:14](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=74s) Pretty much, yeah.

[01:15](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=75s) Yeah.

[01:17](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=77s) So, that's kind of what
I'm responsible for.

[01:18](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=78s) Kurt? My name is Kurt Kufeld.

[01:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=81s) I am the VP of AWS Platform,
which is completely non-explanatory,

[01:27](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=87s) but the way that I like
to describe it

[01:29](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=89s) is I own all of the pieces
that make it possible to run AWS.

[01:33](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=93s) So, I'll just go through
those real quickly.

[01:36](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=96s) So, I own commerce platform.

[01:38](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=98s) You can think about that as billing,
although it's a lot more than that.

[01:40](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=100s) It is metering, it's bill generation,

[01:42](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=102s) it's pricing plans, it's payments,
it's foreign exchange.

[01:46](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=106s) It's basically everything
except the books for AWS itself.

[01:49](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=109s) I also own identity, and identity,

[01:52](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=112s) you know, the most common thing
that you probably know is IAM,

[01:56](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=116s) but it's also everything else related
to identity and access management.

[01:59](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=119s) So, it's organizations, it's Cognito,

[02:02](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=122s) it's tagging,
it's the legacy identities,

[02:06](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=126s) like Managed Active Directory,

[02:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=128s) and that service,
basically every single API

[02:12](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=132s) call to AWS goes through IAM.

[02:16](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=136s) I also own the console platform,

[02:18](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=138s) so not the individual consoles
from the service teams,

[02:20](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=140s) but the overall platforms,
so what we use to really try

[02:24](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=144s) and derive some consistency
across the platform.

[02:27](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=147s) If you think about AWS five,
six, seven years ago,

[02:29](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=149s) there was, you know,
pretty disparate experiences,

[02:32](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=152s) and we've really tried to bring
that experience together

[02:34](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=154s) and to provide a much
better experience for our customers.

[02:38](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=158s) I also own infrastructure as code.

[02:41](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=161s) So, you can think about that
as CloudFormation and the CDK.

[02:48](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=168s) I know I forget something
here somewhere.

[02:50](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=170s) I own external security services.

[02:52](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=172s) So, think about that as things
like GuardDuty,

[02:54](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=174s) Inspector, Security Lake,
which we announced earlier this

[02:59](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=179s) [INDISCERNIBLE] last week,
and then I own automated reasoning,

[03:04](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=184s) which is, we say mathematically
provable security,

[03:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=188s) but really, use mathematics to prove
correctness of certain things,

[03:13](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=193s) and this has been done for years,
but we've really managed to kind of

[03:17](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=197s) bring that more out
into the mainstream and make it more…

[03:19](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=199s) make it easier for people,

[03:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=201s) and I'm certain I've forgotten
something in there.

[03:23](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=203s) Oh, I've been with Amazon 23.5 years
and with AWS for ten.

[03:30](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=210s) So, Kurt, as someone
who predates AWS,

[03:33](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=213s) has been around for a while,
and we're here to talk about…

[03:35](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=215s) I remember sitting in the lobby
when they were going to talk to Jeff

[03:38](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=218s) about doing AWS.

[03:40](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=220s) That's a pretty cool…

[03:41](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=221s) we'll get to the origin story
maybe later,

[03:43](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=223s) but so, I mean, I'd be curious
to hear your talk,

[03:48](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=228s) your take on what does
end-to-end security mean in AWS?

[03:54](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=234s) It's a good question,

[03:55](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=235s) and one of the things
that I really want to do as,

[03:58](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=238s) you know, kind of owning
a lot of that today

[04:01](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=241s) is I see a future
where really security

[04:06](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=246s) is simplifying
all of the disparate things

[04:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=248s) that you see today
and simplifying the complex

[04:12](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=252s) and making it just easier
for our customers to implement that.

[04:15](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=255s) You know, too many leaders have
traditionally viewed security

[04:18](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=258s) as kind of cumbersome, like it's
something you do at the end.

[04:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=261s) It's this carbuncle
that you kind of put on top,

[04:24](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=264s) and it's complicated, you know,

[04:26](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=266s) by the global shortage
of security professionals

[04:30](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=270s) and by the threat landscape,

[04:32](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=272s) which is changing
pretty significantly,

[04:36](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=276s) plus there are data
protection privacy commands,

[04:38](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=278s) demands, excuse me,
that are coming up over time.

[04:41](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=281s) So, it's really getting a lot
more complicated out there,

[04:44](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=284s) and I really look at using,

[04:49](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=289s) taking all those things together

[04:52](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=292s) and using them to simplify
security implementation.

[04:57](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=297s) Maybe a terrible analogy,
but I'll use an analogy.

[04:59](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=299s) That simplification,
I want to use security

[05:02](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=302s) as really an opportunity
to move faster.

[05:06](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=306s) Think about it like brakes on a car.

[05:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=308s) Brakes on a car are to
slow a car down, right?

[05:10](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=310s) Well, no.

[05:11](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=311s) Brakes in our car are there
so that you can actually go faster,

[05:15](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=315s) because it makes it safer,

[05:17](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=317s) and the way that I think
about my job,

[05:19](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=319s) as security, is I want to take,
and our team wants to take.

[05:23](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=323s) and AWS wants to take
and make it easier for you,

[05:27](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=327s) so that you can move
faster as a business.

[05:33](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=333s) Yeah, what's interesting
about this, too, is when you…

[05:37](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=337s) when you think about security
as an idea…

[05:38](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=338s) - Don't look at me as you're talking.
- I'm not.

[05:40](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=340s) - Okay.
- I refuse to.

[05:43](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=343s) We did actually practice that part.

[05:49](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=349s) You know, when you start to change
your mental model from security

[05:52](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=352s) being an enforcement wing

[05:53](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=353s) to being something
that can make you go faster,

[05:56](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=356s) it does change the way
you look at a lot of it.

[05:58](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=358s) You start thinking of it as being
a proactive part of your business

[06:01](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=361s) and not a reactive part,

[06:02](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=362s) and that's certainly how
we've looked at it internally,

[06:04](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=364s) is that security is part of
the products we build,

[06:07](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=367s) and actually, often,
in our own design discussions,

[06:10](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=370s) it's like the most important part,

[06:12](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=372s) because it doesn't really much matter
what feature you add

[06:15](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=375s) if the system isn't
really trustworthy,

[06:17](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=377s) and you don't want to put
that kind of critical data in it,

[06:19](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=379s) then it's not that useful.

[06:20](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=380s) So, we'll spend a lot of time
making sure that it's secure

[06:23](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=383s) right at the very beginning
and automated out of the gate.

[06:28](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=388s) So, I think that's what I feel like
when I hear you say all that.

[06:32](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=392s) It's critical.

[06:33](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=393s) Can I just… I want to add
a little bit on to that.

[06:35](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=395s) Is that all right?

[06:36](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=396s) Yeah, of course.

[06:37](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=397s) So, here's the way that we think
about our priorities at AWS.

[06:42](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=402s) The single most important thing
we do is security.

[06:45](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=405s) The second most important thing
that we do is durability.

[06:48](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=408s) Never lose anybody's data.

[06:51](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=411s) The third most important thing
is availability,

[06:53](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=413s) and then features and service
launches are everything else.

[06:58](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=418s) What's it, and now, obviously,
security, durability,

[07:00](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=420s) availability,
they're deeply interconnected,

[07:02](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=422s) but that security is first,
and that happens all the way through.

[07:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=428s) So, it's not like you have
a security team that kind of comes in

[07:14](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=434s) and tells you
what security to implement.

[07:16](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=436s) Every single developer,
every single person at AWS

[07:20](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=440s) is responsible for security
every single day,

[07:23](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=443s) and our security team
is there to provide guidance

[07:26](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=446s) and to basically help us
move more quickly.

[07:28](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=448s) In many companies,
security is the Department of No,

[07:33](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=453s) and for us, the way we think
about security

[07:36](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=456s) is how do we enable our developers
to move more quickly.

[07:40](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=460s) Does that make sense?

[07:42](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=462s) Absolutely.

[07:43](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=463s) So, when I think about it
from within our groups,

[07:46](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=466s) how does it actually help us
move more quickly,

[07:50](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=470s) when we take the security process,

[07:52](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=472s) like kind of reviewing
what's being built

[07:54](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=474s) and deciding how safe it is,

[07:57](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=477s) the earlier we move
that into the design process

[07:59](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=479s) with the engineers and builders,
the more creative we can be,

[08:01](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=481s) the more degrees of freedom we have,
and the more flexible we can be.

[08:05](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=485s) So, if you've got this…
the term is often used shift left,

[08:09](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=489s) but if you bring that into a robust,
creative discussion

[08:11](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=491s) with the builders and product groups
at the very beginning,

[08:14](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=494s) you'll find a few things
that you can enable with security,

[08:19](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=499s) and you'll very early identify
some things

[08:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=501s) that you should absolutely not do
in order to create a secure platform,

[08:25](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=505s) and finding those
at the beginning is critical,

[08:27](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=507s) and doing it as
a collaboration is critical,

[08:30](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=510s) and one thing I was
thinking earlier today,

[08:32](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=512s) an analogy is in some
software design systems,

[08:35](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=515s) you remember like
there's the sequence

[08:38](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=518s) where the product manager
comes up with an idea,

[08:40](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=520s) hands it to the engineer,
who interprets it and builds it,

[08:42](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=522s) who then takes it over,

[08:44](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=524s) and maybe we get some feedback
through an alpha,

[08:46](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=526s) maybe not, and then you ship,

[08:49](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=529s) and that sequencing can lose
a lot of fidelity and creativity.

[08:52](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=532s) There's not as much of that kind
of iterating internally

[08:55](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=535s) about how innovation
supports new functionality

[08:58](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=538s) and how new functionality
can drive innovation.

[09:01](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=541s) So, if you think about it,
the shift now, of course,

[09:03](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=543s) is to have product and engineering
very closely connected and iterating.

[09:07](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=547s) So, now, just shift your thinking
and say,

[09:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=548s) well, let's put security in there
too, or security expertise.

[09:12](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=552s) So, that becomes exactly part
of that same rich discussion,

[09:15](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=555s) and I've seen many situations
where we've taken a very hard line

[09:20](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=560s) on the security stance for a product.

[09:22](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=562s) We will only do this, and it
would almost sound impossible,

[09:25](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=565s) the thing we were going to do,
but it wasn't,

[09:27](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=567s) because we thought about it
at the beginning,

[09:29](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=569s) and we could actually
invent something

[09:31](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=571s) that hadn't been done before,
that would enable significant value,

[09:34](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=574s) because it happened at the beginning,
and that creates a lot of speed,

[09:37](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=577s) because I bet you many of you here
have had the experience,

[09:40](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=580s) where later in a project,
you discover something,

[09:43](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=583s) and it's a hard lesson,

[09:45](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=585s) because the cost of undoing that
and trying to figure out

[09:47](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=587s) how to address could be as much
as this project's

[09:50](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=590s) going nowhere to months
and months of rework,

[09:54](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=594s) and so, there, you can see
that as being a headwind

[09:56](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=596s) to productivity and speed.

[09:57](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=597s) I actually have a great example,
if you don't mind.

[09:59](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=599s) Sure.

[10:00](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=600s) So, hopefully, everyone here
uses encryption on S3,

[10:05](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=605s) and when we built encryption into S3,

[10:09](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=609s) we rethought how we did everything,
because had we not done that,

[10:12](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=612s) had it been something we just
added on, it wouldn't have worked.

[10:16](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=616s) It would have been too slow.

[10:18](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=618s) It would have been
extremely expensive,

[10:20](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=620s) and the way that encryption
is implemented in S3,

[10:24](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=624s) it's literally invisible
to our customers,

[10:27](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=627s) certainly, from
a performance perspective

[10:29](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=629s) and just really enables
that ability to do that,

[10:32](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=632s) and the reason that that's possible

[10:34](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=634s) is because you think about it
as part of the design process,

[10:38](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=638s) and today, with encryption,
we do that for everything.

[10:41](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=641s) You can find equivalents
in our network,

[10:43](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=643s) in the way we've designed
the EC2 network,

[10:45](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=645s) to allow security to be built
in right at the foundation.

[10:48](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=648s) The same is true of almost
all of our systems,

[10:50](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=650s) because it was brought in
at the very beginning,

[10:52](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=652s) and the nice thing about
when you bring in,

[10:54](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=654s) like, this early innovation
with builders

[10:57](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=657s) is you now have security
becomes more like teachers

[11:02](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=662s) and a creative role
as opposed to a restrictive role,

[11:06](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=666s) because you'll see
these really fun discussions

[11:07](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=667s) where security professionals
start to become

[11:10](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=670s) really well-versed in
architectural possibilities.

[11:12](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=672s) like, hey, we could do this,
I learned from this other project,

[11:14](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=674s) and it becomes an enabler,

[11:16](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=676s) and so, your security folks
are doing more strategic work,

[11:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=681s) moving out of kind of
an audit and control,

[11:24](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=684s) though that's still very important,
into a design and innovate mode,

[11:28](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=688s) and I think that creates more
long-term value for the business,

[11:33](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=693s) when you start to have
that creativity upfront,

[11:34](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=694s) because you'll start
inventing things that,

[11:36](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=696s) I think, like S3 encryption,
like our network technologies,

[11:40](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=700s) they pay off over the very long-term,
because you're able to invent that,

[11:44](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=704s) and a secure platform
means you're going to be able

[11:45](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=705s) to move into
new markets more quickly.

[11:47](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=707s) You're going to be able to take
on new workloads more flexibly.

[11:49](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=709s) All of those things become options

[11:51](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=711s) that would have been expensive to do
if you late minded them,

[11:54](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=714s) and then I think one more way
it makes you fast:

[11:58](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=718s) sometimes, if you think
about the security aspects

[12:00](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=720s) of a product too late,

[12:02](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=722s) it creates a lot of toil
and randomization for your team,

[12:06](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=726s) just lots of extra work
they have to do.

[12:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=728s) Like, think about a product
that wasn't necessarily designed

[12:10](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=730s) to be operated in the environment
you're putting it in

[12:13](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=733s) and just how much extra
work your builders

[12:16](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=736s) and your technologists have to do.

[12:18](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=738s) It's a retrofit.

[12:20](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=740s) It's a retrofit, and as a result,

[12:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=741s) you spend too much
of your builder's time on stuff

[12:24](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=744s) that isn't direct value,
because you're not using it.

[12:26](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=746s) It's not fit for purpose
in that sense.

[12:29](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=749s) So, if you think about it, like,
fewer surprises at the end,

[12:33](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=753s) security doing more strategic work,

[12:35](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=755s) and less toil are all ways
that thinking about this end-to-end

[12:39](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=759s) can really help you move
more quickly with security.

[12:42](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=762s) I just want to add on to that
a little bit.

[12:44](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=764s) Like, when you, I actually
hate the term shift left,

[12:47](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=767s) but when you shift left,

[12:49](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=769s) and you start doing
a lot of that early,

[12:52](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=772s) it turns out a lot of the systems

[12:53](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=773s) that I own are security related,
just like yours are,

[12:56](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=776s) and the security team is not this
outside team that comes in.

[13:00](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=780s) They're our partners,
and we work with them

[13:03](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=783s) on a day-to-day,
regular basis, even though,

[13:06](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=786s) and I think this is
the right thing to do,

[13:07](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=787s) they report up through
a different structure

[13:09](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=789s) in order to have that accountability,

[13:11](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=791s) but we really work together
on a continuous basis.

[13:15](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=795s) Yeah, you know, I was thinking
about this toil concept too.

[13:18](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=798s) Like, if you think about dealing
with security situations

[13:23](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=803s) in an organization,

[13:24](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=804s) there's often a lot
of what I call squabbling,

[13:27](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=807s) but finding logs, moving here,
connecting things together,

[13:29](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=809s) trying to figure out
the relationship between things,

[13:31](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=811s) and I was going to say,
this feels like something GuardDuty

[13:33](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=813s) has really been helping people with.

[13:35](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=815s) Yeah, it has.

[13:36](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=816s) -Thank you.
-You're welcome.

[13:37](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=817s) I happen to own GuardDuty.

[13:40](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=820s) So, we've launched a bunch
of stuff in GuardDuty

[13:42](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=822s) to help with some of this
undifferentiated heavy lifting,

[13:45](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=825s) the toil.

[13:47](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=827s) We've launched GuardDuty protection
for containers,

[13:51](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=831s) so that it's easy for you
to bring all of that information

[13:54](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=834s) in from inside of your containers.

[13:56](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=836s) We've launched GuardDuty protection
for databases,

[14:00](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=840s) so that we know, and you know
what's going on in those databases,

[14:04](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=844s) and for your other serverless
workloads, GuardDuty for Lambda,

[14:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=848s) so that you can bring
all of that data together,

[14:11](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=851s) and with just a few clicks
in the AWS management console,

[14:15](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=855s) you can now achieve
and activate GuardDuty

[14:18](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=858s) across all of that estate,
multiple accounts, multiple regions,

[14:24](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=864s) and you can do that in a very simple,

[14:28](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=868s) secure by design infrastructure,
the AWS cloud infrastructure,

[14:33](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=873s) and migrate and mitigate sorry,
migrate, mitigate those threats early

[14:38](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=878s) and simply by just using GuardDuty
to do the analysis,

[14:44](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=884s) initiate the automated responses,

[14:45](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=885s) initiate the automated finding of
any issues that may come up.

[14:50](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=890s) So, GuardDuty is really one of
those things that we're trying to use

[14:53](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=893s) and that we're really focusing on

[14:55](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=895s) in order to make that much simpler
for our customers,

[14:58](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=898s) so that you don't have to bring
all those bits and pieces together

[15:02](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=902s) and make it…
do it in a very complex fashion.

[15:06](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=906s) Let me provide you with an example.

[15:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=908s) So, Warner Bros Discovery
recently paired GuardDuty

[15:14](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=914s) and Amazon Detective
to help them really kind of simplify

[15:19](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=919s) a lot of their anomaly
detection and their agility.

[15:22](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=922s) You know, before they did this,

[15:25](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=925s) their security engineers would have
to take logs from various systems.

[15:28](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=928s) They'd have to take logs from AWS,

[15:30](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=930s) they'd have to take logs
from their cloud providers,

[15:33](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=933s) they'd have to take logs
from their services,

[15:35](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=935s) and they'd have to put them on a sim,

[15:36](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=936s) and then they'd have to look
and build systems

[15:39](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=939s) to detect anomalous activity.

[15:42](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=942s) It's tedious, right?

[15:44](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=944s) It's just work, and it doesn't
really allow them

[15:48](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=948s) to innovate on the core value
that they bring to the customers,

[15:53](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=953s) but with GuardDuty, they were able
to simplify a lot of that

[15:58](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=958s) and reduce
some of the complex querying

[16:01](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=961s) and some of this massive
disjoint datasets,

[16:04](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=964s) and we could just work with them
and do it for them.

[16:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=968s) That's cool.

[16:13](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=973s) So, one of the things…

[16:16](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=976s) What would you like to…
what else do you want to talk about?

[16:18](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=978s) I'm going to talk about how we create
the culture for this stuff.

[16:20](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=980s) Sure.

[16:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=981s) So, once you're trying to figure out,
okay,

[16:24](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=984s) I like this end-to-end security idea

[16:26](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=986s) that these guys are talking about,
I want to be fast.

[16:28](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=988s) There's always this question
about, okay,

[16:29](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=989s) so, what do you do to enable it,

[16:32](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=992s) and I can share with you that what
I learned when I first joined AWS

[16:35](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=995s) and what I've learned
since is what has been

[16:38](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=998s) really critical has been the creation
of the culture that enables it.

[16:44](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1004s) And I remember, like very early
when I joined AWS,

[16:49](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1009s) I had heard before, you know,
security is important from…

[16:51](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1011s) many companies say that,

[16:52](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1012s) but this is the first place
I had seen

[16:54](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1014s) where it was modeled daily
by senior leadership.

[16:58](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1018s) At the time, Andy Jassy as our CEO,

[17:00](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1020s) would personally get involved
in auditing

[17:02](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1022s) and getting deep into issues

[17:03](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1023s) and making sure
everyone understood them

[17:05](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1025s) and reinforcing, on a regular basis,

[17:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1028s) that security is absolutely
our top priority,

[17:10](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1030s) and you'd not find
very many people who would…

[17:12](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1032s) Can we talk about
weekly security meeting?

[17:13](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1033s) Yeah, sure. Go ahead.

[17:16](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1036s) So, one of the things that we do
is we basically review,

[17:20](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1040s) whether it's an operational issue,
whether it's a security issue,

[17:23](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1043s) we have a process that we use
to drive continuous improvement.

[17:28](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1048s) Security is one of those,

[17:29](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1049s) and our most senior leaders
get involved in that.

[17:32](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1052s) One of the things that we do
is the CEO of AWS

[17:36](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1056s) has a weekly meeting where they
review any security issues,

[17:40](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1060s) any things that we may be driving,

[17:42](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1062s) and this is not the meeting
you want to get invited to.

[17:46](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1066s) I have the dubious honor
of being there every week,

[17:49](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1069s) but what's really important
about this is it sets the tone.

[17:53](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1073s) Everybody cares.

[17:55](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1075s) Everybody drives it,
and it is about teaching.

[17:57](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1077s) It's about understanding,

[17:59](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1079s) and it's about
that continuous improvement.

[18:01](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1081s) I think one thing that's important
about this too,

[18:03](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1083s) so, I have a similar, smaller scale,

[18:04](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1084s) slightly less scary meeting
with my team,

[18:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1088s) and we get together on a regular
basis, on a weekly basis,

[18:11](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1091s) and we get into
very high levels of detail

[18:14](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1094s) on the security programs
we're operating,

[18:17](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1097s) any the security issues
we need to work on,

[18:19](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1099s) and the reason we get into
the high level of detail

[18:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1101s) is there's a couple of them.

[18:22](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1102s) One of them is I'm
an incredibly curious person,

[18:24](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1104s) and I can't help it.

[18:25](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1105s) Second one is by having
those rich discussions

[18:29](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1109s) about the deep details,
the technical and the ones

[18:32](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1112s) related to software/hardware,
my teams all understand

[18:35](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1115s) that they have to know
that stuff when they come,

[18:37](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1117s) and for them to know that stuff,

[18:39](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1119s) they had to have been
deeply in it themselves,

[18:41](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1121s) and their directors
had to be deeply in it,

[18:43](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1123s) and because, by having those,
as a senior person,

[18:46](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1126s) getting into the details like that
and paying attention to them,

[18:51](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1131s) asking the tough questions,

[18:52](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1132s) understanding them
on a regular basis,

[18:54](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1134s) it creates a machine

[18:55](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1135s) whereby your whole org
pays attention to it constantly,

[18:58](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1138s) and I have, if you let off the gas,

[19:00](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1140s) it will get overrun by the other
major priorities in the business,

[19:04](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1144s) feature launches,

[19:06](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1146s) like whatever other pressures
are coming into that business,

[19:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1148s) and so, staying closely connected

[19:11](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1151s) and very into the details
helps maintain it,

[19:15](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1155s) and I think, coupled with that,
you can't always be about bad news.

[19:18](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1158s) My own experience as well
is it's also

[19:20](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1160s) just as powerful
to celebrate progress,

[19:23](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1163s) and celebrating progress in this
is not just the big things.

[19:28](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1168s) I find it's really powerful
to celebrate an individual builder

[19:32](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1172s) making a simple choice
to improve that improved security,

[19:35](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1175s) even in the smallest way,

[19:37](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1177s) because they chose
to raise that in a meeting.

[19:38](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1178s) They chose to potentially change

[19:42](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1182s) the way the product
was going to evolve,

[19:44](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1184s) or they spent some
extra time working on it.

[19:46](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1186s) Rewarding the small things
reinforces the culture,

[19:49](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1189s) I would say almost more
than recognizing the big things.

[19:53](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1193s) I think the big things feel a little
bit performative sometimes,

[19:55](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1195s) like, hey, way to go on that launch,

[19:58](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1198s) and also, what happens
is you encourage people

[20:01](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1201s) to bring those ideas up
in the meetings

[20:03](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1203s) that may be disruptive
but may be critical,

[20:05](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1205s) because they know that they're
respected and required by leaders.

[20:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1208s) So, I think that part of
creating a culture

[20:11](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1211s) and the leadership dedication to it

[20:12](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1212s) is absolutely critical to giving
the team members permission

[20:16](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1216s) to prioritize this work
and stand up for it

[20:19](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1219s) in all the meetings you can't be in,

[20:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1221s) which is where a lot
of these decisions get made.

[20:23](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1223s) Yeah, it's interesting
that you bring that up,

[20:26](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1226s) because my team runs the same way.

[20:28](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1228s) I run weekly security meetings
for my various teams

[20:30](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1230s) and the same sort of thing,
and we go very, very deep into those.

[20:34](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1234s) For some of them, I have…
where I can't participate,

[20:37](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1237s) I have leaders that are at my level,
and they participate there too,

[20:41](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1241s) and it's not just the, you know,
when something happens,

[20:46](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1246s) but when the good things
happen and celebrate those.

[20:52](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1252s) It's really interesting.

[20:54](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1254s) When you've got security integrated
end-to-end, like,

[20:57](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1257s) it's a great optimization
of time and resources,

[21:00](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1260s) and when you think about it early,
you end up in a different place.

[21:04](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1264s) Since we're using car examples,
I'll provide you with a car example.

[21:07](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1267s) This is a…
I love to use this example.

[21:09](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1269s) So, there are two car manufacturers,
whose names I will not use,

[21:13](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1273s) but I'm certain
you are familiar with,

[21:15](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1275s) and one car manufacturer starts off
as building a luxury car

[21:19](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1279s) and adds performance.

[21:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1281s) The other car manufacturer starts off

[21:24](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1284s) as building a performance car
and adds luxury.

[21:27](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1287s) They're both great cars,

[21:29](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1289s) but they end up
in very different places,

[21:32](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1292s) and the point there is if you start
with security at the beginning,

[21:37](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1297s) and then you build,
you will end up in a different place.

[21:40](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1300s) You'll be more secure.

[21:46](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1306s) Now, one of the things that we
really worry about at AWS

[21:49](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1309s) is how do we give our customers
more bang for the buck,

[21:52](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1312s) how can we build services together?

[21:53](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1313s) How do we make that easier
for our customers,

[21:59](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1319s) and one of the things that you get,
I think, out of the cloud,

[22:02](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1322s) which is different
than what you got on-prem,

[22:04](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1324s) is that you get improvements
on a continuous basis.

[22:09](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1329s) So, whether you're using
GuardDuty today,

[22:11](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1331s) or IAM today, tomorrow,
it'll be different.

[22:15](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1335s) The day after that
it will be different,

[22:17](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1337s) and we're continuously improving.

[22:18](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1338s) We're continuously changing,
and you get that for free,

[22:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1341s) because we just do that.

[22:23](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1343s) It's part of what we do.

[22:25](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1345s) So, you're continuously improving
the infrastructure

[22:28](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1348s) that you're running on.

[22:30](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1350s) You're not buying a fixed
set of capabilities

[22:32](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1352s) and then having to upgrade
to the next of the security

[22:36](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1356s) or the next, next of that.

[22:39](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1359s) You're just getting it
as part of the services.

[22:41](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1361s) It's the continuous investment
and improvement in technologies

[22:44](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1364s) that you just get out of the cloud.

[22:46](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1366s) Before you get on with that.

[22:47](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1367s) Sure.

[22:48](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1368s) In my space, we do… we have,

[22:51](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1371s) in the Internet safety
and security space,

[22:54](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1374s) we have very active adversaries,
if you think about it.

[22:56](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1376s) Really?

[22:57](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1377s) People never noticed.

[22:58](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1378s) You've got people who basically
run these services

[23:01](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1381s) like their own little businesses

[23:02](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1382s) and try and find ways to disrupt
your businesses in general,

[23:07](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1387s) and so, as an infrastructure…

[23:09](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1389s) Let me interrupt you there, actually,

[23:10](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1390s) there is a, I'm trying to remember
the name of the company,

[23:12](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1392s) but there is… they literally
run them as a company.

[23:14](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1394s) They do, yeah.

[23:15](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1395s) They have HR departments.

[23:17](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1397s) They have, like,
employee of the month, like, it is…

[23:19](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1399s) these these adversarial businesses
are run as a company.

[23:23](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1403s) Secretly, I prefer it
when they do it that way,

[23:25](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1405s) because they're easier
to find and shut down,

[23:29](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1409s) but when you think about choosing
an infrastructure provider

[23:31](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1411s) for security,
you want one that has it built in.

[23:33](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1413s) You want one that has obsession
with security,

[23:36](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1416s) like we've talked about,

[23:37](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1417s) and you want one that's going to,
like, constantly evolve,

[23:40](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1420s) but sometimes that rate of evolution
has to be very fast,

[23:44](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1424s) like in a situation where
you've got an adversary,

[23:46](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1426s) you know, we have, in my group,

[23:48](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1428s) we have these dedicated
researchers across the globe

[23:52](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1432s) who are able to look at,
and this is kind of cool,

[23:54](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1434s) so, we have like a global backbone.

[23:55](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1435s) It connects to basically everything.

[23:57](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1437s) It spans the Earth, connects almost
every ASN on the planet,

[24:00](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1440s) and we're able to gather
incredibly interesting telemetry

[24:03](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1443s) about what traffic looks like
in various situations,

[24:05](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1445s) when there's a soccer game,
a football game.

[24:07](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1447s) In certain European cities,
their network looks amazing.

[24:10](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1450s) There's all sorts of cool stuff
happening.

[24:11](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1451s) The same thing is true of
when there's news events,

[24:15](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1455s) or when there's other
legitimate events, we can tell,

[24:18](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1458s) and we can see the difference
between that and malicious activity,

[24:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1461s) and we can learn
from such a broad estate

[24:24](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1464s) and be able to bring that in,
apply machine learning to that,

[24:28](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1468s) apply our judgment
from our security researchers,

[24:30](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1470s) and develop security practices
that prevent attacks before customers

[24:34](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1474s) see them, before any of you see them.

[24:35](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1475s) That's another example where you're,

[24:38](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1478s) by betting on a piece
of infrastructure,

[24:39](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1479s) a cloud infrastructure, and moving
that security practice down,

[24:43](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1483s) you get the benefit
of this constant evolution,

[24:46](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1486s) but at a very fast pace,
so that you don't have to,

[24:48](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1488s) which is really kind of the key,

[24:50](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1490s) because you want to
spend your resources

[24:52](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1492s) on building your businesses,

[24:53](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1493s) not building up
your own defenses against…

[24:56](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1496s) you don't want to end up
an invention battle

[24:59](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1499s) with these motivated adversaries.

[25:04](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1504s) Great callouts.

[25:06](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1506s) I'll give them an example
of one of the ways

[25:07](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1507s) that we're continuing to innovate.

[25:09](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1509s) So, I own AWS
Private Certificate Authority,

[25:14](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1514s) and I'm happy to pre-announce today
the availability of AWS Private CA

[25:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1521s) Connector for Active Directory,
and enterprises that use

[25:27](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1527s) Active Directory and use AD
to manage their Windows

[25:30](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1530s) environments need this
in order to basically do

[25:35](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1535s) PKI with their environments.

[25:37](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1537s) With AWS AD Connector for Private CA,

[25:45](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1545s) you can replace all of this expensive

[25:48](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1548s) Microsoft Private CA with a secure,
easy-to-use,

[25:53](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1553s) and available service
that we manage directly.

[25:56](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1556s) It's another one of those places
where we just want to make it easier

[26:00](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1560s) and remove that undifferentiated
heavy lifting for our customers.

[26:04](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1564s) I'll give you another example.

[26:06](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1566s) We recently launched AWS… Hold it.

[26:10](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1570s) Do you want to interrupt me?

[26:11](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1571s) No, no. I was about to cough.

[26:12](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1572s) I'm sorry, go ahead.

[26:14](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1574s) No problem.

[26:15](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1575s) We recently launched
AWS Payment Cryptography.

[26:20](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1580s) So, if you are in the payments
industry,

[26:23](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1583s) that is,
you have to process payments,

[26:26](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1586s) you probably are familiar
with the fact

[26:28](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1588s) that you need to run payments HSMs.

[26:30](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1590s) You need to create
a constellation of payments

[26:32](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1592s) HSMs, you need to put them
in datacenters,

[26:35](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1595s) you need to hire people
who can manage these,

[26:37](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1597s) and they're pretty fragile,

[26:40](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1600s) and it's just stuff that you need
to manage in order for you

[26:44](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1604s) to really do your core business,

[26:47](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1607s) which is processing those payments
or doing other parts of that,

[26:51](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1611s) but with the launch of AWS
Payment Cryptography, it was…

[26:56](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1616s) I always try to say payments,
but Payment Cryptography,

[27:01](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1621s) you can secure your data,
and you can do that

[27:03](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1623s) without having to run
any of these payments MSMs.

[27:07](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1627s) It's a service that helps you reduce
your operational burden,

[27:11](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1631s) and it uses a fully managed service

[27:13](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1633s) to meet all of your payments
and PCI requirements.

[27:16](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1636s) So, we've just launched that,

[27:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1641s) another example where you kind of
get things in the cloud

[27:24](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1644s) as they as they come through.

[27:26](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1646s) Do you want to talk about Zero Trust,
or should I talk about Zero Trust?

[27:29](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1649s) -Why don't you kick us off?
-All right.

[27:34](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1654s) One of the big buzz phrases
out there these days is Zero Trust.

[27:38](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1658s) I actually don't like that phrase,

[27:40](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1660s) but I think it's a good phrase
to maybe just say,

[27:44](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1664s) how do you make sure that,
on a continuous basis,

[27:48](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1668s) you are checking every API
call every time you access something,

[27:54](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1674s) every time that you want
to do something, reevaluating

[27:58](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1678s) and checking to ensure

[27:59](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1679s) that the request is coming
from a trusted source.

[28:02](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1682s) Used to be, remember
the eggshell, the squishy egg?

[28:06](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1686s) Yeah, yeah.

[28:07](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1687s) Right?

[28:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1688s) Hard outside, soft and gooey inside.

[28:11](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1691s) We want to make sure that everything
is hard all the way through.

[28:16](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1696s) I'll give you just an example.

[28:17](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1697s) Amazon as a company has been working
on this for quite a while,

[28:22](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1702s) and the laptops
that we carry these days,

[28:24](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1704s) as an example, we don't connect
to a corporate network.

[28:28](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1708s) We evaluate our access
to all of our applications,

[28:32](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1712s) to everything we do,
on a continuous basis.

[28:35](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1715s) So, we do analysis of are you
running on a supported platform,

[28:39](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1719s) are you up to date,

[28:40](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1720s) are you connecting
from a trusted network

[28:42](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1722s) or an untrusted network,
and we may treat you differently.

[28:45](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1725s) So, Zero Trust also comes up a lot
with our customers today,

[28:51](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1731s) because a lot of customers
want to go to this environment

[28:54](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1734s) where you effectively
never trust anything,

[28:56](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1736s) and you have to keep doing that
on a continuous basis,

[29:00](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1740s) and we deeply believe
in the outcomes and benefits

[29:03](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1743s) that this model delivers for us.

[29:07](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1747s) So, you know, you can apply
Zero Trust concepts,

[29:11](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1751s) rethinking identity,
authentication authorization,

[29:15](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1755s) and do that in meaningful ways
in order to improve your security.

[29:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1761s) The next chapter for us in this

[29:23](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1763s) is to comprehensively address
those cases for our customers

[29:27](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1767s) without the need to stitch
together those multiple services.

[29:31](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1771s) For example, every time
developers build an app,

[29:34](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1774s) they have to create permissions
for application resources,

[29:37](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1777s) and we believe we can simplify this.

[29:40](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1780s) We can reduce the toil
that's involved,

[29:43](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1783s) and AWS can help you
establish common ground

[29:46](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1786s) when you build these applications.

[29:50](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1790s) I've gone blank on the name
of the service that we just launched,

[29:55](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1795s) the language that we just launched.

[29:56](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1796s) Cedar. Thank you.

[29:58](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1798s) I actually hadn't gone blank.

[29:59](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1799s) I just wanted to give him
something to talk about.

[30:02](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1802s) So, late last year,
we launched Cedar.

[30:06](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1806s) Cedar is an open-source system

[30:10](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1810s) that allows you to define
access management

[30:14](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1814s) in your applications,
so not as you access AWS,

[30:18](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1818s) but how do you
build access management

[30:20](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1820s) into your applications themselves,
and what's interesting here

[30:24](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1824s) is that nobody's really addressed
this problem before,

[30:27](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1827s) and when you've built applications,

[30:29](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1829s) you've had to figure
all this out yourself.

[30:31](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1831s) So, with Cedar, you can define
the access management

[30:36](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1836s) for your applications,

[30:37](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1837s) and we once again remove
that undifferentiated heavy lifting,

[30:41](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1841s) and then once you need
to evaluate it,

[30:46](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1846s) we launched AWS Verified Access,

[30:50](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1850s) where you can use that service
to actually evaluate

[30:56](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1856s) those Cedar policies every time that
you need to get at something.

[31:02](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1862s) Yeah, when you think about it,
we've kind of covered…

[31:03](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1863s) we think about Zero Trust…
I'm a network guy.

[31:06](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1866s) So, I think about Zero Trust
as being…

[31:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1868s) considering a lot of the things
you talked about,

[31:10](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1870s) but also, network conditions, and so,

[31:14](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1874s) if you think about
the mix of things we've launched,

[31:17](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1877s) we've launched Verified Access,

[31:18](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1878s) so, kind of like remote access
for a desktop.

[31:20](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1880s) We've launched VPC Lattice,

[31:22](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1882s) which allows you to do
constant reanalysis of the access

[31:25](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1885s) or the flows between your VPCs
and data in a very simple way,

[31:29](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1889s) and then Verified Permissions,
so that when you build an app,

[31:33](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1893s) you can build all this in yourself,

[31:34](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1894s) so that you can control
the permissions

[31:37](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1897s) between tiers in your own application

[31:39](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1899s) and make sure that that Zero Trust
is carried all the way through.

[31:42](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1902s) So, if you use all these together,

[31:43](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1903s) you can get kind of an end-to-end
Zero Trust story.

[31:46](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1906s) The thing I like about both Cedar
and the Verified Permissions

[31:53](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1913s) is not only have we made
it easier for customers,

[31:57](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1917s) but we've used automated reasoning

[31:59](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1919s) to prove correctness in those spaces.

[32:01](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1921s) Yeah, it's a pretty cool
characteristic of Cedar,

[32:04](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1924s) that it can be done that way.

[32:06](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1926s) I think that's worth
paying attention to.

[32:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1928s) One of the hard things to do
in security,

[32:09](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1929s) of course, it's easy to say,
let's stop Kurt from accessing this.

[32:14](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1934s) It's very hard to say
who can access this.

[32:17](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1937s) I think those sorts of problems
are going to be critical

[32:19](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1939s) and part of the powers of Cedar.

[32:22](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1942s) So, one thing about cedar
that's interesting, too,

[32:24](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1944s) -is it's open source.
-Yes.

[32:26](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1946s) So, this is part of… is an important
part of our Zero Trust story here,

[32:32](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1952s) which is it needs to be adopted
broadly, and it needs to be…

[32:36](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1956s) it needs to engage
with the community.

[32:38](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1958s) So, I'm curious to hear
your thoughts, Kurt,

[32:39](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1959s) on end-to-end security, Cedar,

[32:43](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1963s) and just the partner landscape
that we work with.

[32:45](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1965s) Absolutely, and we've worked
with partners on this,

[32:47](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1967s) not only partners
helping our customers,

[32:49](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1969s) but partners helping us
to define the language,

[32:52](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1972s) and by using security technologies

[32:55](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1975s) and consulting services
with these partners,

[32:57](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1977s) they're with us in the trenches
as we innovate for our customers.

[33:00](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1980s) So, these customers help us,
and these partners help us,

[33:04](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1984s) to really be successful.

[33:07](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1987s) I'll give you another example.

[33:09](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1989s) Just two weeks ago,
we launched Amazon, sorry,

[33:12](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1992s) GA, excuse me, for Security Lake,
for Amazon Security Lake,

[33:17](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=1997s) and which automatically centralizes
your organization's security data,

[33:23](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2003s) and when we built this,
and we built OCSF,

[33:27](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2007s) the language,

[33:31](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2011s) the protocol for how you get
everything into Security Lake,

[33:35](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2015s) we built this with over 35

[33:38](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2018s) of the biggest providers of security
out there: CrowdStrike, Datadog,

[33:44](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2024s) and others that were really
with us on this journey,

[33:48](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2028s) so that you can bring
all of that data

[33:49](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2029s) together within your AWS account,
your on-prem data,

[33:55](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2035s) and then do analysis on top of that,

[33:57](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2037s) regardless of where
the data comes from.

[34:00](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2040s) You can use your, you know,
also, it turns out some companies

[34:04](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2044s) are better
at some things than others,

[34:05](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2045s) and thus, you can use
your preferred provider

[34:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2048s) for your security and your analytics

[34:12](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2052s) and do so

[34:13](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2053s) with a centralized data lake,

[34:19](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2059s) so that you don't have to
build all of this yourself.

[34:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2061s) We worked with partners
to build all of this,

[34:25](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2065s) and, you know, our customers
put all of this into action,

[34:29](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2069s) and when I think about
how they should start with

[34:33](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2073s) not just bringing
all of that data together,

[34:35](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2075s) but how should we think about that
end-to-end security for our partners

[34:41](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2081s) and for our customers.

[34:43](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2083s) True.

[34:44](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2084s) Well, so, so, far, we talked about
what end-to-end security is.

[34:46](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2086s) We talked about some cool innovation
to make it possible.

[34:48](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2088s) So, now, I think we should
probably talk about

[34:49](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2089s) how do you actually
start and get there.

[34:50](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2090s) Yep.

[34:52](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2092s) It's kind of my favorite part.

[34:53](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2093s) So, I talked earlier about step
one being the mindset, right?

[34:57](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2097s) The cultural transition.

[34:58](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2098s) How does leadership apply themselves
to start making the change?

[35:03](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2103s) Moving to a partner as opposed
to the police model,

[35:06](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2106s) and that sounds… it's easy to say.

[35:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2108s) It's an enormous amount of work,

[35:09](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2109s) and it requires a lot of commitment
from a leadership team

[35:11](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2111s) to put in the time to maintain that.

[35:14](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2114s) So, it sounds simple.
It's not at all.

[35:16](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2116s) It might even be the hardest
part of this discussion.

[35:20](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2120s) Once you're in that mode, you look
at what you're building,

[35:23](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2123s) and you need to think about which
of the parts of my security practice

[35:28](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2128s) really should be part of my platform

[35:30](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2130s) and not part of my general
application and business.

[35:33](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2133s) Which parts do I want to delegate
to a platform provider

[35:35](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2135s) and which ones do I want to own?

[35:37](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2137s) And the answers will be different

[35:38](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2138s) when you ask that question
for this year

[35:41](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2141s) and for the long-term, right, so,

[35:43](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2143s) if you look at them
over two time horizons,

[35:45](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2145s) and start to say,
look, I really want, over time,

[35:48](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2148s) to be betting on this security
being deeper

[35:51](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2151s) in the infrastructure
that I build on.

[35:52](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2152s) So, I have to build less of it
myself,

[35:54](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2154s) and again, that sounds really simple,

[35:56](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2156s) but it will drive a lot of
interesting debates internally

[35:58](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2158s) as to what the true business is
and where to invest,

[36:01](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2161s) but I think it's a critical step,

[36:04](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2164s) and this is where I think
it's really important to think about,

[36:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2168s) when you're looking at
an infrastructure provider partner,

[36:12](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2172s) you're looking for a place
where that security

[36:14](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2174s) is going to be
constantly pulled down.

[36:16](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2176s) You want to make sure that you're
aligning with a provider that is…

[36:18](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2178s) that that is their mojo.

[36:20](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2180s) That's what they do.

[36:22](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2182s) For us, for example,
as we mentioned earlier,

[36:24](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2184s) we build it into everything we do
at the very beginning.

[36:26](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2186s) That's made the infrastructure
suitable for financial companies,

[36:29](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2189s) government agencies,
healthcare agencies.

[36:31](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2191s) Because we thought about S3
encryption and network protection

[36:33](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2193s) at the very beginning,
now, these heavily regulated

[36:37](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2197s) and heavily security
conscious companies can move on,

[36:40](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2200s) and because we keep doing that,

[36:41](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2201s) it makes it kind of easy
to bet on our infrastructure

[36:43](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2203s) as the place security
will continue to grow,

[36:47](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2207s) and so, one thing,
I'll give you an example of this,

[36:50](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2210s) which is one of my favorite ones,
because it was such…

[36:52](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2212s) it was something that we really
didn't have to do, and that's Nitro.

[36:55](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2215s) I'm sure many of you
are familiar with Nitro here.

[36:58](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2218s) Nitro, if you're not,
is a hardware device

[37:02](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2222s) that we built for our hypervisor.

[37:04](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2224s) The hypervisor is the thing that
switches between virtual machines,

[37:07](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2227s) makes sure that it does scheduling
of CPU and memory access,

[37:10](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2230s) so that you can virtualize hosts,

[37:12](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2232s) and one of the things
that we decided early on

[37:15](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2235s) is it is unacceptable
for anyone in AWS

[37:18](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2238s) to have access, administrative
access, to the virtual machines.

[37:20](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2240s) It's interesting.

[37:22](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2242s) I was in those discussions early on,

[37:23](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2243s) and there was a lot of back
and forth about it,

[37:25](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2245s) but in the end, the right thing to do

[37:27](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2247s) was to ensure that nobody could get
access to Nitro when it was running.

[37:31](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2251s) And so, what's fascinating about that

[37:33](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2253s) is you've got a company debating
about spending resources

[37:37](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2257s) and inventing something
that will reduce their own ability

[37:40](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2260s) to access and manage something,
knowing it's the right thing to do,

[37:45](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2265s) and that's just…
and that has paid off very well,

[37:47](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2267s) because now, we have all the systems
we need around that to manage

[37:50](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2270s) and make sure things
are operationally strong,

[37:52](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2272s) but at the same time,
we can easily say to you,

[37:55](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2275s) look, we've provably made it
such that these are yours.

[37:57](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2277s) These are not something
that we can access.

[37:59](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2279s) It's also interesting
because one of the things that,

[38:01](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2281s) you know, I talk to customers about,

[38:03](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2283s) and that customers worry about
is, well, what happens…

[38:06](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2286s) because let's face it,
software is complicated,

[38:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2288s) what happens if somebody,
you know, owns the hypervisor.

[38:12](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2292s) Well, with AWS Nitro,
that's not even possible,

[38:16](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2296s) because there is no hypervisor.

[38:17](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2297s) The hypervisor literally
is in a separate system

[38:20](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2300s) that is inaccessible from the systems

[38:25](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2305s) where the virtual machines
are running.

[38:28](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2308s) Yeah. So, I think if you
look at the steps to take,

[38:32](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2312s) there's this identifying the things

[38:34](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2314s) that you want to move down
into your infrastructure,

[38:37](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2317s) and then there's operationalizing
what you're doing. Right?

[38:41](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2321s) There's this idea that you now
need to figure out how to work,

[38:45](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2325s) build the processes and mechanisms
around what you're doing,

[38:48](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2328s) such that you're keeping
security early in the design system,

[38:51](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2331s) and that you're making sure that
you're betting on the infrastructure,

[38:53](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2333s) because as you all know,

[38:55](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2335s) a decision made once
has an effect once,

[38:58](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2338s) but if you build
an ongoing mechanism,

[39:00](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2340s) you can ensure that drives
the change you're looking for.

[39:03](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2343s) -If I can share an example.
-Sure.

[39:05](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2345s) So, there's a company
that we worked with, Unqork,

[39:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2348s) and it's a great example

[39:09](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2349s) of how the organizations
really embrace this security

[39:15](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2355s) is a partnership
with development example

[39:18](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2358s) and shifting that security earlier
into the development process.

[39:22](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2362s) You know, their security teams,
over the years,

[39:24](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2364s) used to be point-and-click
security operations,

[39:27](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2367s) you know, really to building security
in as part of their code.

[39:31](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2371s) You know, they've operationalized
the way security interacts

[39:34](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2374s) with their developers and engineers,

[39:37](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2377s) making sure that they build
that security

[39:39](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2379s) into that development process early,

[39:41](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2381s) just like we have done
over the years,

[39:43](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2383s) and, you know, everything from
pre-commit to pre-commit hooks,

[39:47](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2387s) pre-vetting, pre-approving
design patterns,

[39:49](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2389s) and working with them early on.

[39:52](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2392s) They're even helping develop
their teams and development teams

[39:55](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2395s) kind of level up their own skills,
level up their own security,

[39:59](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2399s) to be able to threat model
their own applications,

[40:02](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2402s) and this is really
something that you…

[40:04](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2404s) that I would certainly
strongly encourage

[40:07](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2407s) is it's every developer's job
to build security

[40:11](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2411s) and to be secure all the time.

[40:13](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2413s) So, you know, I love that example.

[40:17](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2417s) It's important, and I love seeing
customers pick it up

[40:19](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2419s) and start to get the speed
benefits of it as well.

[40:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2421s) It's really part of the things
that makes my job really,

[40:23](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2423s) really rewarding.

[40:25](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2425s) Once you've gone through
the first steps

[40:28](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2428s) I mentioned,
you're moving things down,

[40:31](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2431s) moving things early,

[40:32](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2432s) and then of course,
you need to step back and say,

[40:34](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2434s) well, am I reasonably covering
all of the levels of security

[40:39](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2439s) and compliance that I need to cover
as part of this program?

[40:42](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2442s) And so, having a programmatic way

[40:43](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2443s) to measure your progress against this
is a key part of it.

[40:47](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2447s) And here, there's usually a framework
that will be adopted,

[40:50](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2450s) something like NIST or the AWS

[40:51](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2451s) Well-Architected Framework
that you can,

[40:54](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2454s) if you're using a consistent
infrastructure for your security,

[40:57](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2457s) it makes it much simpler
to measure against that,

[40:59](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2459s) and you can use something
like Security Hub to go and say,

[41:02](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2462s) oh, let me look at my applications,
my true infrastructure,

[41:05](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2465s) and give me a sense of where I stand
against these on an ongoing basis.

[41:09](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2469s) And what's interesting here
is you select your frameworks,

[41:12](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2472s) you start to understand
where you're at,

[41:14](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2474s) you can use that to drive
your practices over time

[41:16](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2476s) and ensure that
you're staying current,

[41:17](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2477s) and of course, as you mature in this,

[41:19](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2479s) you can develop your own
frameworks and decide,

[41:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2481s) oh, I would like to focus
more on this and this.

[41:24](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2484s) And I think that that framework
approach,

[41:27](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2487s) plus getting help from partners
who have expertise in this area,

[41:31](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2491s) is an important part of
making sure that, as you're shifting,

[41:34](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2494s) you are getting really good coverage
across the security landscape

[41:37](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2497s) and what you're attempting to do.

[41:39](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2499s) Yeah, I mean,
I'll give you an example.

[41:42](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2502s) So, we have more than 300 services
and features,

[41:46](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2506s) I think, related to security at AWS,

[41:48](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2508s) and this can be
a little overwhelming,

[41:50](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2510s) but you're talking about frameworks.

[41:51](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2511s) Like, one of the things
that you can do

[41:53](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2513s) is you can use something
like Control Tower

[41:55](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2515s) to kind of set up your landing zones

[41:57](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2517s) and kind of set up
that baseline for you,

[42:00](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2520s) so that you know that,
within this framework,

[42:03](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2523s) you've met the Well-Architected
design suggestions

[42:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2528s) that we have, and then not only,
and you've mentioned this already,

[42:11](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2531s) but not only do you have them set up,

[42:13](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2533s) but do they continue
to be set up the right way.

[42:16](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2536s) You can use Config to check that.

[42:18](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2538s) You can use AWS Systems Manager
to manage that,

[42:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2541s) and we have predefined
a lot of those controls,

[42:25](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2545s) a lot of the standards
that are out there

[42:28](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2548s) in order to help you meet
PCI or HIPAA or things like that,

[42:33](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2553s) and you can just do that kind of
right out of the box,

[42:35](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2555s) without you having
to do all that work.

[42:38](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2558s) It's critical to automate
all of these things.

[42:40](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2560s) I think automation is a really
important part of this.

[42:42](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2562s) Automating your audit,

[42:43](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2563s) automating the testing
of your security infrastructure

[42:46](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2566s) is all very key, and I think,

[42:47](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2567s) because again, you don't want to be
dedicating fixed time to that,

[42:50](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2570s) resources to that.

[42:56](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2576s) The one thing I would say, too,

[42:57](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2577s) is once you kind of
get into this idea

[43:00](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2580s) of you've got your framework,

[43:03](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2583s) you've moved your engineering
to the right places,

[43:06](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2586s) you really need to start
thinking about,

[43:07](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2587s) okay, well, how am I
going to scale this.

[43:10](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2590s) I have, in our case,
very many hundreds of teams,

[43:14](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2594s) but you could say, I've got…

[43:16](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2596s) More than 850 the last time
I checked.

[43:19](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2599s) So, you're starting
to scale this out,

[43:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2601s) you're growing your businesses,
and you're investing in new things,

[43:24](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2604s) and learning how to make sure
that each one

[43:26](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2606s) is building on this philosophy,

[43:30](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2610s) I suppose, this set of mechanisms
that you've created,

[43:33](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2613s) and I think this is really important
is to do intentionally,

[43:36](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2616s) is to say, okay, now,
I really want to make sure

[43:38](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2618s) that I'm planning on
how to scale this,

[43:39](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2619s) so that my teams can pick it up
and move quickly,

[43:42](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2622s) and so, it's something that requires
programmatic focus from leadership,

[43:46](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2626s) and in here, you need
to bet on something

[43:47](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2627s) that's going to provide you
immutable infrastructure.

[43:49](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2629s) You want to be able to provide people

[43:51](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2631s) with really nice places to start.

[43:52](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2632s) So, you use landing zones
and Control Tower

[43:54](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2634s) to set up the account infrastructure,
use Organizations to set policies,

[43:58](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2638s) but then you use something
like CloudFormation,

[43:59](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2639s) some of these things to start setting

[44:01](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2641s) what are the ways that a client
facing mobile app looks in our world,

[44:06](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2646s) what is the shape and size
and the configuration of that,

[44:10](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2650s) and when you're designing that
in an intentional way,

[44:12](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2652s) you can also use things
like serverless,

[44:15](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2655s) something to extend
and automate that.

[44:16](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2656s) So, the automation goes with it,

[44:18](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2658s) so that the people who are
running the applications

[44:19](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2659s) don't have to go and design that.

[44:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2661s) They simply take this off the shelf,
they put in their logic, their bits,

[44:25](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2665s) and they're already taking advantage
of all the other standardization

[44:28](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2668s) and the other work that you've done,

[44:30](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2670s) and then they're able to deploy
this safely in your infrastructure,

[44:33](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2673s) and then you can iterate
on that over time.

[44:35](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2675s) You can grow it, but then you don't
have to worry about the quality

[44:38](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2678s) of this end-to-end security program
you're running degrading as you grow,

[44:42](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2682s) because I think that's a really
important part of this practice,

[44:45](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2685s) is paying attention to it,
and I'll go back,

[44:47](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2687s) because I've only been there
for ten years.

[44:49](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2689s) So, I'm a junior
compared to Kurt here,

[44:51](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2691s) but when I started,
I remember going to our regular,

[44:54](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2694s) one of our regular audit meetings,

[44:56](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2696s) and at the time,
the meeting was small enough.

[44:57](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2697s) This is our ops meeting at the time.

[44:59](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2699s) Yeah.

[45:00](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2700s) You all go into this one big room,
and I remember being just awestruck,

[45:04](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2704s) because we had 13 AWS services, 13.

[45:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2708s) I was like, there's absolutely no way

[45:10](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2710s) we're going to be able
to scale beyond this.

[45:12](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2712s) It's just it's just too much at 13.

[45:14](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2714s) I think we have, in terms
of actual services now,

[45:16](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2716s) I believe, we're well over 300 now.

[45:18](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2718s) We've got…

[45:19](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2719s) Yeah, I know the last number
I saw was over 285.

[45:22](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2722s) So, it could be over 300.

[45:23](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2723s) But that scaling from 13 to 285

[45:27](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2727s) is exactly based on what
we've been talking about,

[45:29](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2729s) and it has been an intentional
set of efforts by leadership

[45:33](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2733s) to create that scale environment
without increasing risk,

[45:36](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2736s) and as I've been through it,
and I'll admit, a few times,

[45:40](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2740s) I was like,
we're not going to make it.

[45:42](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2742s) The next level is going to be
too much scale, too much pressure,

[45:45](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2745s) and the truth is, with a lot
of leadership dedication,

[45:49](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2749s) a set of systems like this,

[45:51](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2751s) it does create very few barriers
to continuing to scale

[45:55](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2755s) while maintaining
your security rigor.

[45:57](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2757s) Yeah, totally agree.

[45:58](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2758s) Which I would say is probably
going to be very difficult

[46:00](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2760s) if you stick with
a traditional police

[46:02](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2762s) or kind of a post-facto audit model.

[46:04](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2764s) It doesn't it doesn't scale at all.

[46:06](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2766s) In fact, the bigger you get,
the slower you go.

[46:09](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2769s) And I think, yeah, you end up
having to hire,

[46:12](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2772s) you end up trying to solve
the problem with more hiring.

[46:14](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2774s) You end up with increasing risk
when you increase your velocity.

[46:17](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2777s) Like, these things
start to work against you.

[46:19](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2779s) And as the world changes,

[46:20](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2780s) and the world's changing
very quickly right now,

[46:25](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2785s) that type of an approach
doesn't really keep up, does it?

[46:27](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2787s) No.

[46:28](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2788s) No, I mean, the world
changes so quickly.

[46:30](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2790s) Like, think about
where technology is today

[46:33](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2793s) versus where technology
was even six months ago.

[46:35](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2795s) As a business, trying to govern
your infrastructure and technology,

[46:38](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2798s) you have new things to think
about and to innovate on.

[46:41](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2801s) What are you thinking about here?

[46:42](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2802s) Well, it's funny you should
mention that, Kurt.

[46:46](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2806s) Personally, I think about things
like generative AI,

[46:49](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2809s) and how it will put pressure
on and change

[46:51](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2811s) the way we think
about data governance and being smart

[46:53](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2813s) about how to put
the right boundaries around it.

[46:55](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2815s) I'm curious to hear
your thoughts on this.

[46:57](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2817s) Well, it's interesting.

[46:58](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2818s) So, let me actually spin it
the other way first.

[47:00](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2820s) We're already seeing generative
AI being used in attacks,

[47:05](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2825s) and so, not only is it going
to be interesting

[47:09](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2829s) in how we can use it for security,

[47:11](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2831s) but it turns out some of those folks
out there are very smart,

[47:14](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2834s) and they're using it
the exact opposite,

[47:16](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2836s) to help them really try and take down
some of the security barriers

[47:20](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2840s) we have today,

[47:22](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2842s) but I think here
there are several areas.

[47:26](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2846s) One that we're going
to use generative AI with

[47:29](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2849s) is I think we can use it to help

[47:31](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2851s) actually make implementation
of security easier,

[47:35](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2855s) and that's an area
that we're looking at.

[47:38](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2858s) Also, I think the other area,

[47:40](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2860s) and this is an area
that a lot of companies,

[47:41](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2861s) this is kind of where a lot
of companies are right now,

[47:44](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2864s) is they're thinking, all right,
I've got these models.

[47:46](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2866s) Now, I've got my own data.

[47:47](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2867s) How do I use my own data to help,

[47:50](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2870s) you know, kind of train some of this?

[47:52](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2872s) But I don't want my data to leak out,

[47:55](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2875s) and, you know, we have some systems
that we've recently announced,

[47:59](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2879s) like Amazon Bedrock,

[48:02](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2882s) so that customers can start
using generative AI

[48:06](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2886s) and use it in a safe way

[48:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2888s) and use it such that they are able
to improve the models

[48:12](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2892s) but still keep their own data
for themselves.

[48:15](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2895s) It's a multi-layered approach.

[48:18](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2898s) It has bar-raising
security controls around it,

[48:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2901s) and you get all of the standard
AWS controls as well,

[48:25](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2905s) plus you get Config and CloudTrail

[48:26](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2906s) to make sure that you continue
to be protected

[48:32](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2912s) as you're doing this.

[48:37](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2917s) Also, as you continue to scale,
and as you grow your business,

[48:44](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2924s) what can I use generative AI,

[48:46](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2926s) or what can I use other systems
for in order to help with this?

[48:52](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2932s) I think this is the point of the talk

[48:53](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2933s) where I admit that I jumped
into part of this a bit early.

[48:56](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2936s) I think what would be interesting,

[48:58](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2938s) Kurt, actually, is let's talk
about the scale part.

[49:01](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2941s) I think you had a great example

[49:03](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2943s) around who's been effective
at actually scaling.

[49:06](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2946s) -You mean by Botprise?
-Yeah.

[49:08](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2948s) Okay.

[49:09](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2949s) So, there's a company
that we work with,

[49:11](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2951s) Botprise, a great example of scale.

[49:13](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2953s) They're a startup in cloud security

[49:15](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2955s) and the automation industry.

[49:17](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2957s) They've aggressive growth goals.

[49:20](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2960s) They were challenged
with scaling effectively,

[49:22](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2962s) because they needed
to meet stringent requirements

[49:25](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2965s) for their own security
operations and automation,

[49:27](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2967s) and what they did is, in 2022,
they went through the AWS

[49:32](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2972s) Well-Architected review process,

[49:35](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2975s) where they learned
kind of how to measure,

[49:38](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2978s) how to build architectural
best practices

[49:41](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2981s) and do that security early.

[49:43](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2983s) They reviewed the provided guidance

[49:45](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2985s) on how they could work
with some of those security gaps,

[49:48](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2988s) and by building
their automation solutions

[49:51](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2991s) on the AWS infrastructure,
using AWS security solutions,

[49:56](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=2996s) like Security Hub,
GuardDuty, Inspector,

[50:00](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3000s) they were able to move more quickly.

[50:02](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3002s) Botprise built their security
solution in one year,

[50:07](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3007s) when their usual time-to-market
was double that.

[50:11](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3011s) So, it's really helped them
accelerate.

[50:13](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3013s) They continue to increase
their customer base,

[50:16](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3016s) and now, the company can scale
in a cost-effective way

[50:20](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3020s) as they're continuing to scale,
just by scaling AWS.

[50:24](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3024s) Yeah, I think that's really
the key takeaway here.

[50:27](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3027s) I mean, that's of the things
I've tried to highlight here today.

[50:30](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3030s) -What's that?
-Did you just call me Peter.

[50:31](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3031s) No, I didn't.

[50:32](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3032s) I said that's one of the one
of the great takeaways from today,

[50:35](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3035s) Peter, is, you know, there's a series
of technological changes,

[50:41](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3041s) the products you need to consume,

[50:43](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3043s) and there's a set of cultural
and leadership techniques

[50:48](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3048s) that are necessary
to make this happen.

[50:49](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3049s) It's not a simple use
this product; this will happen.

[50:52](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3052s) It's not a simple use
this leadership approach;

[50:54](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3054s) this will happen.

[50:56](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3056s) You have to think of it holistically
to get end-to-end security to work.

[50:58](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3058s) You have to think of a cloud platform
that has this built into its DNA,

[51:05](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3065s) that you can bet on growing
with your business,

[51:09](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3069s) and then you need to think about
how you're going to get your teams

[51:13](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3073s) and practices to start
bringing security earlier

[51:16](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3076s) and then scale those practices
out as you grow

[51:19](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3079s) and make sure your cloud
can do it with you.

[51:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3081s) And I think all of that adds up
to this last story,

[51:23](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3083s) which I don't want to undersell here,

[51:24](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3084s) which is this will
all make you faster,

[51:28](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3088s) and I think, in the end,
this is really one of the keys here,

[51:31](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3091s) is being able to innovate
and adapt to new challenges,

[51:33](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3093s) deliver more for customers,

[51:34](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3094s) and do so through
the practice of security,

[51:38](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3098s) as opposed to in spite
of the practice of security,

[51:41](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3101s) and I think it's really important.

[51:43](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3103s) If you left with one thought
after this whole discussion,

[51:45](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3105s) it would be that.

[51:46](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3106s) It would be that if I tweak the way
I approach security,

[51:49](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3109s) and I think about it as a creative
part of my building process

[51:53](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3113s) on a strong infrastructure,
I think what you'll find

[51:56](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3116s) is that you'll be able
to deliver much more quickly

[52:00](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3120s) and with much more security,

[52:02](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3122s) and I think it'll be much better
for your business and your builders.

[52:05](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3125s) Yes, your builders
will love it in the end.

[52:07](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3127s) So, great example.
Great story. Love it.

[52:12](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3132s) I hope we've been able,
we're getting towards the end,

[52:14](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3134s) I hope we've been able to provide
some inspiration today

[52:17](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3137s) on how everybody can take some time
and build your own security culture,

[52:21](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3141s) build the guardrails
that you need to,

[52:23](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3143s) and then keep the innovation flowing,

[52:25](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3145s) and be able to actually
move more quickly.

[52:27](https://www.youtube.com/watch?v=Khhni4Ce-Ow&t=3147s) [music playing]

