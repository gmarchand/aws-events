# AWS re:Invent 2024 - How generative AI is transforming legal tech with AWS (NTA311)

[Video Link](https://www.youtube.com/watch?v=i7E2LHcQtlU)

## Description

NetDocuments leads in cloud-based document management for the legal sector. Their platform enables global document storage, sharing, and collaboration. Learn how ND advances document management with innovative solutions and semantic search, processing millions of documents daily. The legal industry, including law firms and corporate legal departments, often grapples with large, complex documents. As generative AI evolves, new productivity-enhancing applications emerge: searching vast document repositories, summarizing files, powering Q&A systems, and drafting documents. This session explores how generative AI can transform legal work, boost efficiency, and streamline document-heavy workflows, revolutionizing the profession.

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

- Yeah, generative AI, that's what is... It's so impressive and exciting, and that's what we are
here to talk about today. So welcome everyone to NTA311, transforming how generative
AI is transforming legal tech with AWS. My name is Pallavi Nargund, I'm a principal solutions
architect at AWS, and I'm also a chief technologist for the legal tech community within AWS. Joined with me today is John
Motz, CTO of NetDocuments and Olta Alushi, who is also a co-founder of Legal Tech community within AWS Alta. Olta, to you. - Thank you, Pallavi. Hi everyone. I'm excited to be here with all of you. For the next hour, we'll be talking about the
legal industry, the landscape, and the technology adoption
within legal industry. And then John here will walk us through the innovative journey with generative AI and AWS within NetDocuments. And then Pallavi will close us
with use cases in legal tech and reference architectures. Imagine a future where
the legal technology and legal industry is revolutionized by the generative AI. Picture all these tedious
tasks being automated, allowing legal professionals to focus on the most important
aspects of their profession. Think of legal research
being not just faster but smarter and more
comprehensive than ever before. Data in the 21st century is the equivalent of
gold in the 19th century, and through artificial intelligence, we have been able to
open up new data sources that were not reachable before. Imagine legal profession
undergoing a transformation as revolutionary as other
industries have seen, like finance or healthcare, where through AI assisted research, we have been able to
expand the global markets, introduce instantaneous payments, improve customer experience, and even expand our lifespans. Now, imagine the same innovative
spirit applied to law, but what if we could
amplify the capabilities shortening the contract
drafting that it takes lawyers or legal professionals to do today, or the way that it... Like how much time it takes
them to predict cases. Up to 44% of legal tasks
today based on research can be automated, which is a figure that
outstrips many other industries, so this can actually be done. The real magic though of generative AI is in freeing the legal professionals to focus on the most human
aspects of their profession, and that is to exercise
empathy, strategy and advocacy. But let's first define legal tech. Legal tech is a combination
of digital tools, software and applications that get
applied to legal companies, and that includes law firms, legal counsels within large corporations to boost the productivity,
to enhance the value of their legal services
and to reduce costs all through the automation
of legal workflow. When it comes to applying
technology within the industry, we first want to
understand its challenges. Technology set up today should be able to support
processing large documents of unstructured text of any size and form, and that setup has to be
enabling the end users not creating a bottleneck. The second is balancing skill and value. We have seen a growing concern with devaluation of legal skills. As we know, as an example, junior lawyers spend a lot
of time doing research, contract drafting and other legal tasks, and the question becomes how does the next generation
of lawyers, for instance, gain that practical experience
if automation is in the loop? And how do law firms in fact
justify work like billing for work that now gets
implemented by machines? The third concern that we
see is with data privacy and security, and we
know that legal companies handle sensitive information that goes from corporate
data to client data. And as this data gets digitized and moves to the cloud,
there is a growing perception that risk of data breaches
also grows exponentially. But in fact, the data
shows that organizations that have reported data breaches within the cloud environments, they are attributing those
breaches to human error and misconfiguration
of cloud environments. And the last one is the
challenge with productivity. That is a complex one to execute, but what it means in itself
is reducing the time it takes for you to do this
repeatable, mundane tasks. And if you don't select the right systems, the right architecture and the technology to complement that legal workflow, productivity may actually decline. At AWS, we believe that
technology should enhance not replace the human elements
of the legal practice. In legal tech, there is
this concept of a flywheel, which is this idea that
the small initial effort leads to significant
positive outcome over time. After each revolution, we see positive ROI and positive outcome for customers that implement their process, their data, and their people against
this flywheel concept. Let's illustrate that concept through a document handling approach. We start by mapping document repositories, organizing and centralizing this data so that it is searchable by
everyone in the organization. Then we process this with
natural language processing to understand its content, and then we extract the metadata from it to better organize it. Then third, we add the AI and
machine learning capabilities to analyze patterns and
to learn to create systems that actually learn contextually what that data actually represents. And so at the end of the day, there is a system that gets
deployed for legal professionals to now run very complex
queries against this data set, and that produces this precise
context aware responses in a matter of minutes. And as we said, after each revolution, the ROI improves over time. And the customers that
have worked with AWS and AWS technologies, they tell us that they see
contract generation completion within hours versus weeks and productivity improvement by up to 15%. But your numbers here could be different. Your use cases could be different. Let's talk now for a little
bit about why legal customers choose to work with AWS. For 18 years, AWS has been
delivering cloud services to millions of customers around the world in a variety of use cases and workloads. The AWS region and availability model is recognized by Gartner as the recommended approach
to run enterprise applications with high availability and
the 108 availability zones, 34 regions that are available today give you the opportunity to
run enterprise applications across the globe, especially
when you have to abide to country data residency laws. AWS is the most secure with
300 plus security services around compliance and governance, and that includes features as well as supporting
143 security standards and certifications. AWS cloud is sovereign by design, and we will talk more
about this in a little bit, but what that means is that our pledge to digital sovereignty allows us to build services and features that meet always the customer's
regulatory requirements. And we are at the
forefront of generative AI with 100,000 plus
customers already using AI and ML services. Now, when it comes to generative AI, our mission is to
democratize generative AI by offering flexibility and choice for our customers that want to
run workloads and production. And we look at generative AI
in three layers of a stack, and we'll go deeper on this
in a little bit as well. When it comes to deploying
generative AI in production, at the bottom of the stack, we see models where we provide AWS build silicon chips so that you can train
models from the ground up, but in a more cost effective way, that is applicable to training and inference type workloads as well. In the middle of the stack, we provide you a secure way to build and scale applications
leveraging leading AI, generative AI or large foundation models so that you can switch between
these large language models made available through our
Amazon Bedrock service, which you may have heard multiple
times throughout the week. And that is our fully managed service, which in very short terms
gives you the ability to switch between models. You can customize these
models for better performance and even allow it to do automated tasks
without writing any code. And at the top of the
stack, we have applications that use these large language models, but that help you to get up
and running pretty quickly. So all you have to do is
point your data sources to the application and then you can ask it
questions, create content or even add additional actions
that you wanted to take all while leveraging the intelligence that exists in your
organization's data repositories. Now, we talked about security,
privacy, and responsible AI. That is at the top of our priorities when it comes to working
with legal tech customers. And we place this in the forefront of every technology that we build. Any architecture and any
service that you place on AWS inherits the same security
standards that we build. We provide that enterprise grade security, meaning that anything like we said is built on AWS inherits (indistinct) and we give you full control of the data, full control of your data,
while also giving you options to enable encryption keys
to manage encryption keys, and in addition, apply data protection policies
across your data's journey in your organization. Our identity management system
also allows you to enable and manage user access policies so that you can enable tight controls over who accesses which data and when. When you customize, and this is important, a foundational model, your data does not leave
your virtual private cloud on AWS and it does not get used to update that base foundational model. And we'll talk more about
this in a little bit. Now, at the beginning of the session, we talked about re-imagining
document handling, and we also talked about why customers choose to work with AWS and they say that they
need security, privacy, the right performance,
the right cost structure, and the right solutions that
are relevant to their business. Having said that, I would like to introduce
John Motz on stage, CTO of NetDocuments. - Thanks, Olta. So I'm gonna start with
a little bit of context about NetDocuments. If you don't know NetDocuments, we've been around 20 plus or so years. I've been here as CTO for about two years. We're all over the world. We're global. Six regions doing business
in many, many countries around those regions, about 5,000 firms, although we're adding it seems
like several a day frankly. So we're growing pretty rapidly right now. There was a big push into cloud services through the pandemic with legal. It saw a very big burst
relative to some industries that had already shifted to
cloud quite a bit before then. 185,000 users globally, and
that's legal professionals, assistants, things like that. Over 8 billion documents, and that's greater than 20 billion files. And so we're adding millions
and millions of files every day with our customer
base into the platform. 21 petabytes of data. Although again, this changes
almost every single day. I think most importantly, and probably most impressive for me is we're doing roughly about
650 million transactions a day. And so when you think about the platform as a legal professional,
you get a document, you get a new case, you get a new matter, the first thing you're doing
is ingesting that document into your document management system. So every single day you're interacting. Once it's in the system,
every piece of your workflow is running through our platform, whether you're checking it in,
checking it out, editing it, changing it, sharing it, all runs through the
NetDocuments platform. And then we are ingesting quite a bit. And so when you think about the process, and you'll see some of this
coming up in the slides, it's not just about storing a document. We do a lot of processing,
a lot of metadata extraction and creation on that document, and we're doing about 25
million new documents a day through that process, which
is pretty incredible frankly. As you think about that, the legal space started
with this foundation and it's been pretty much
the same for 15 or 20 years within document management. And for the first time in a long time, we're seeing that change. And so first and foremost, lexical search. So if you're a legal professional and you're looking for
something in a document system and think... Think about this. A firm, a large firm could have literally hundreds
of millions of documents in their document management system. You have to be able to find it. And lexical search is how
we've done it for years. I can tell you in
talking to our customers, the holy grail for them
has been semantic search. It's just really been out of reach and it's been out of reach
for reasons tied to cost, the ability to even actually
process and manage it well. And then it is a change. And sometimes change can be challenging. I think the generative AI push that has happened in the last year is changing the expectations
for professionals and particularly legal professionals. They want to find items as they would ask for them naturally. And that's what we're seeing. And so a pretty significant change moving to semantic search, and
it's deep within our roadmap and what we're already delivering today. Beyond that is this concept
of check in and checkout. And if you are a legal
professional, you know what this is. If you're not a legal professional, this is essentially putting
a document into the system and taking a document out. In the legal world, it's
a lot more complex though because there's controls,
very tight controls. A big part of our platform is being able to have permissions,
rights, authorizations, not just for people
working within the firm or the corporate legal, but also customers as
well as counsel outside that you have to share documents with. So checking in and checking out is a very, very important
part of the architecture as well as the platform. What we're seeing though is
that is getting to a point where we want co-authoring. We want to be able to work in
a document at the same time. We don't want to have to
check things in and out in multiple copies and some documents in a
document management system could have thousands of versions depending on how long the
case or the matter ran. We wanna move to co-authoring. This is again, an expectation
our customers have. And then security. Security, we've already talked
about this, critical for AWS. Frankly, it's one of the primary reasons we've chosen AWS for our cloud strategy. For us, security is paramount. These are the most sensitive documents that you can find in the world, frankly, you have to make sure they're secure. I think the thing that is
really interesting right now from a security perspective is
it's evolving to include AI. And so you're gonna see
here in a few minutes how we're leveraging AI within our document management workflow. What's getting really, really interesting is now AI is doing things
like generating content for legal professionals. It's analyzing documents
for legal professionals. We need to understand what
the AI is actually analyzing. We need to understand
what the AI is authoring. We need to understand when
changes are being made by AI and ensure we apply the same
security we've applied to users for the last two decades
to AI within the platform. So critical part for us. So when you think about
that and NetDocuments we're shifting our thinking. Document management with workflow is what we've been doing
again for two decades plus. Where we're evolving to is this concept of an intelligent and simple platform. And when you think about that, a lot of customers and a
lot of companies, frankly, and if you literally
walk through re:Invent, you'll see, I'm guessing,
a couple hundred companies that are solving AI for
a very niche problem. We think about AI across
the entire platform. And so we're building the platform to enable AI in every
aspect of the workflow. We want this to be a workflow
engine driven by AI and data that delivers a very, very
intelligent and smart experience. And so what you'll see, you'll see a little bit of
us solving niche problems as we started this,
call it late last year, where it's moving through
very rapidly with AWS is this underlying data platform that drives an intelligent experience and an AI experience through
every single workflow. So why AWS? I've gotta touch on this. This is a relatively new journey for us. We're 12-ish months into our push into AWS and it was a pretty big decision for us. So imagine a company 20 years plus running in a private environment for many, many years since day one, proprietary encryption, Anthropic encryption that
we built 20 so years ago, big HSMs everywhere securing
all of our data and content. So a pretty big change for us. When you think about this, and
Olta touched on this as well, I wanna touch on a couple things. Mainly my data's a little wrong with 99. It's apparently 108,
it's probably 112 now. But the level of cultural matching that we had with AWS and our
team internally was astounding. And when you look at these
metrics, they're all impressive. You know, the regions, the
security, the ecosystem. For us, it was AWS really thinks like us. They think about innovating quickly. The fact that we're here every year and I literally was
typing emails yesterday after the keynote to my team. "We gotta do this, we're gonna do that. Let's pivot over here." You
have to be able to do that. And if you wanna stay viable and you want to meet the customer's needs, which is what we're
here to do as a company, we needed that kind of a partner. So a lot of great
capabilities drove us to AWS. I think if I had to pick one, I would lean deeply into security. When you think about the
security model that AWS is using and the ability to secure
at the silicon level, the ability to isolate security
down to single data elements and objects is really,
really important for us. And we felt by a long, long
margin, the future state and the kind of the forward thinking from a security perspective was critical. Absolutely critical.
So what does this mean? How is this changing how we're building? Where are we applying
this over the last year to build this platform,
this intelligent platform? And I think of three things. I think of data-driven experiences, I think of right tools for the job, and then I think of nurturing
a culture of innovation. And when you think about
data-driven experiences, for me it's about flexibility. And I just talked about sending the email to the team yesterday. We have to have a platform
that can adapt to technologies and be able to move quickly. And so we're building
an architecture with AWS that will allow us to switch
to their mesh framework when it comes out 'cause we asked for it
about seven months ago and we love that, we wanna be
able to take advantage of it and not take nine months to do that or even a year or more. And so the architecture is built for that. We need to be flexible,
we need to be responsive and not as in a UI and
stretching across screens. We need to... Someone got that. We need to be able to respond
to the customer's needs as we understand how they're
using the platform, right? Because we're introducing new experiences, we're introducing AI into our workflows. We're learning a ton right now. We're understanding how
customers are using the platform. We've gotta be able to
respond to that behavior and change how the data
is driving the experience. And then scale, and scale, again, I'm not talking
about EC2s and Fargate, I'm talking about being able
to scale the organization and the technology because there's too many new
things that are coming at us. We've gotta be able to
scale and move fast. And so for us, this is
organizational structure. How have we organized our teams? And we shifted over the last two years from teams of about 10
or so, in some cases even a little larger, most of them tightly
coupled with dependencies. And we're shifting the models where our teams are as
small as four to five. We have incredible adoption
of AI generated code that's being embedded in our workflows with our development teams to get more scale from smaller
teams and more efficiencies. Critical part for us being successful over the next few years. Right tools for the job,
event driven architecture. And I'm not saying we don't
believe in APIs anymore. We definitely believe in APIs, but we are leveraging Amazon to build an event driven architecture because we're moving away from the response request
model in our platform and our applications. We want to be able to take those events, understand what our customers and users have done in the system and trigger actions and jobs. And you'll see some of those, you know, here in a few minutes, without any intervention from
the customer or the user. That's incredibly important When you think about
leveraging generative AI in the workflow. You've gotta be able to be proactive and reacting to those events versus waiting for someone to take action. AI and automation, again,
another big part for us. Our company as a whole, outside of what we're
doing with our customers, we are looking at AI and automation across every segment of our business. We think it's that important and we're leveraging that to work faster. We're leveraging that to deliver better
metrics to our customers, better metrics to our operations team so we can manage the
environments better with AWS. Very, very important part
of what we're doing here. It's interesting when you
think about AI automation, you have to be comfortable picking up new and different tools that
you haven't used before to run your business. And sometimes that can be a little hard and frankly you have to
account for that cost model because you're going to have that overlap. But I can tell you our experience
is once you make that call and you get into that new world,
it becomes so much better. You get much more efficient and you get past that
overlap cost very quickly. And I think the thing that's... For me that's really been
insightful with our teams is they're actually happier employees. They're able to do their jobs better with higher quality and higher efficiency. The last one here, not
very important at all. It's just the cloud
service partners like AWS. We couldn't do this without
AWS, there's no way we could and our decision to move
into AWS was really simple. We couldn't keep up, we couldn't
keep a private environment anywhere close to the level of innovation we're going to get from AWS. And again, you don't
have to look any further than this event this week to see that. Nurturing a culture of innovation. So it's interesting, I built this slide and it said adopting a
culture of innovation and my CEO corrected me and he said, "Well, we've been
innovative for 20 years." And so we made a tune there,
but it really is the truth. I mean, we came up with Anthropic
encryption 20 years ago, which is pretty darn innovative. We were doing cloud document management when most people were doing on-premise. And so it is true, we are
definitely an innovative company and an innovative group. It's really important to understand, we do that through engaging with customers and I think a lot of people lose sight of how important that is. Our engineering teams spend
time with our customers, our engineering teams go through
the same product training and onboarding training that our customers and
partners go through. We're organized for agility. We're a company of empowered engineering and operations and design. We want our teams to go
figure out the problems and then literally build
three or four concepts and see which one works,
see one doesn't work and make decisions that way. We move very, very fast for
an organization our size. And you know, I think generally
we're doing daily releases on most of our applications and then we push our teams
to challenge the status quo. And this is gonna sound
a lot like the Amazon and it's not a surprise. Like we have adopted a lot
of the same core values. I wanna hear the challenges. I wanna hear why the solution
that we created 15 years ago that was incredible at the
time isn't good enough today. And so we're not just
building new applications, we're reinventing and re-imagining
the problems we solved 10 or 20 years ago based on the technology that's available today. A critical part of how we're building and how we're innovating. All right, so what does
that leave us with? It's pretty straightforward. Maximum performance, maximum security, maximum innovation and maximum value. And really that is the
number one objective for us in that partnership with Amazon. Very straightforward goals,
very straightforward targets, which I also think is really critical for getting your team
centered in moving forward. So the last slide around Amazon and how we're doing this, if you will, I wanted to talk about why Amazon. And this is a screenshot of our kind of an analysis evaluation. And I always joke with our Amazon rep, I don't think they ever thought
the deal was gonna close. We went through the ringer on the analysis to the point where we were
building our infrastructure during the evaluation. This wasn't a PowerPoint
slide exercise for us. We built the new data objects, we built all the new EC2 instances, we ran them at scale as well. We had a lot of sizing done. So again, we're a year into this, we got to a 90% accuracy
on our cost to run. And so far holding true to that. Frankly it's come down a little bit because of some of the graviton releases that have happened since
we made the decision. We also really looked at a cloud partner. And for me, taking an organization that has never run a public cloud, you can't just turn an organization over. These are incredibly talented people, but there's also a learning curve. And so we were very,
very explicit in saying, we're gonna resource this
with a critical partner for about 50% of our resource
allocation and then train up and create a bridge for our existing team. Really, really cool to see if you're looking at
the data that I look at. As of now, 95% of our
existing team within CTO, which is operations,
engineering, security, have taken and have
been certified with AWS in the first year, which is incredible. Frankly, the fastest
I've ever seen it happen. I've done this more than a couple times. And so we give 'em the platform
and the ability to learn and grow along the journey, not expecting them to be
AWS experts on day one. And then the last thing I
would say is the architecture. We really wanted to understand what the complete architecture
was gonna look like before we started doing the work. And it was really important for us because it allowed us to make
very thoughtful decisions around what we're going to do first. And a lot of folks go
after the easy stuff first. We did the exact opposite. We went after the four hardest things that we knew we had to get after because we knew we were gonna pivot. We knew we were gonna find
the changes we wanna make, we knew we were gonna struggle frankly. And so we figured if we can knock off the four hardest aspects
of our architecture in our platform in year one, the second year would be pretty easy. And sure enough, that's where we are. We're fighting through some
of that stuff right now, but we're also doing it the right way and we're not sacrificing
the architecture for time. We're very focused on
building it the right way and leveraging our well
architecture reviews and our Amazon partners to do that, which is pretty incredible. Okay, so I'm gonna jump
in to AI in action. So as you think about the cloud journey, keep in mind we didn't
just shut down a roadmap. Like we can't do that. We're a business, we have customer needs, we have a space with GenAI
that is exploding right now. And so we had to get after
a roadmap at the same time. So we're literally doing
our cloud transformation with our existing platform and building new capabilities in parallel. And so when you think about AI, which for us is one of the biggest markets we've seen open up in the last 20 years. Real quick award here. We have an application,
PatternBuilder MAX, and this is pretty cool. This is not a solicited media, this is just someone that
went to a conference, saw Scott Kelly who leads our AI group demoing PatternBuilder MAX
and was just blown away by it. And this is a to... If you're in legal you
know, this is a tough space. It's gotta be right, it's gotta work, it's got to make the job easier or else no one's ever going to adopt it. And so just some really cool accolades, best artificial intelligence for 2024, which is a pretty big deal. I think if you went to a legal
tech conference this year, there's probably 600 legal
tech popups that have happened. And so to win that award
was pretty awesome. When you think about PatternBuilder MAX and some of the value, I'm gonna click through this real quick. A couple things we can do. We're plugged into an LLM. I loved the comment yesterday with Matt, how important choice was. And so we're building models and we're building applications, but we're also allowing our customers to bring their own models
and applications as well. And so if you think
about PatternBuilder MAX, it allows you as a user,
as a no-code solution to build custom applications. And so if you're a immigration firm and you have 35 documents
that you have to do for every single person
that's coming in for a visa or an immigration application,
you can build an application with PatternBuilder that'll
automate that form creation, automate that form completion for you and literally take what would
normally be several hours if not a couple of days
down to 20 or 30 minutes. You can actually auto
profile data now with us. And so when you think
about the auto profiling, you have a document
and in the current day, if you go backwards, documents
had very limited metadata. Most of it was human generated. And so the quality was generally
lacking or poor, very... At least it was inconsistent
across the firm. And so we're now leveraging LLMs as well as some of our
vectorized data with Titan and Symantec to auto
profile documents at scale. Think about dropping a million documents in the document management system and you have a consistent taxonomy that can literally update
hundreds of metadata fields on every single document
within literally a few minutes. And you have that consistency that frankly legal professionals have been looking for for decades. Incredible value and
incredible time savings. Doing this in the background as well. And so up until about a month ago, you could run an application,
you could select documents, we can now run an application against your entire corpus of data. And so the days of
having to select 10 or 20 or 100 documents are moving away. The customers, our customers'
expectations are changing. We need to be able to run this at scale across their entire corpus of documents. And again, some of those customers, that's a hundred million
documents or more. I'm gonna give you an example here. I glossed over redlining, which is probably the coolest
thing we're doing right now. So I shouldn't do that. We are now getting to a place where we are redlining
documents with generative AI. And so when you think about
that, think of an attorney, they have certain ways
of writing contracts or writing summaries or briefs,
the AI can understand that. It'll actually auto redline the documents, something a legal assistant
would typically do, send it back to the partner to review, accept changes and
streamline that process. You're talking about in some
cases two or three steps of editing and redlining that are being done
now with generative AI, which is pretty incredible. So I wanted to give you an example here, just a quick screenshot. Normally we demo this, but I made a rule 20 years
ago to never do live demos. So what you have here is a
typical old way, manual limited, somewhat inaccurate, and
the new way you can see here some of the examples of the metadata, and this is a leasing contract. And think about this in a firm. You have these management companies that will have thousands, potentially tens of thousand of contracts. They have rules, they have
compliance, they have parameters like what's my out clause. A lot of these companies
are acquiring contracts through acquisition. This simple auto-profiling capability will allow someone to run
those contracts in bulk, it'll flag exceptions within the contracts that they need to have
an attorney look at. So out of a hundred thousand contracts, these 15 have a really,
really bad exit clause. You need to go look at this
and potentially repaper. Just a simple example
where this would take weeks for a firm to dig through that's happening in just a few minutes. And then a streamlining risk. It's actually reducing the risk
within the firm dramatically by flagging and automating that process. So at the end of the day,
the next big thing for us, PatternBuilder MAX has been amazing. We've got a lot of customers using it. Where we see the kind of the sphere tipping over a little
bit is the AI assistant, this agent to agent conversation. And Pallavi's gonna talk to the details in which we need to get to. For us, it's a simple front door. There is a learning curve with AI and what we found with our adoption is the fast adopters are leaned in, but there's a large segment of people that are still a little nervous about AI. And so we need that door to be wide open and it needs to be a very
simple, wide open door. Conversational threads
are what people like, it's what they do. They're used to doing that now, it's a pretty common practice. I joke two years ago, my wife
would've never used Siri. And now she doesn't send a
text that's not Siri based. And the world is getting
much more comfortable with that conversational
based interaction. And then safe and secure. We have a saying in NetDocuments, we're gonna bring AI to your documents, we're not gonna push your documents to AI. So keeping the AI services
within our platform and contained within our
walls that we've built, literally the most secure
walls you're gonna see for a document management system. We want the AI inside, not outside. So it's a critical part of our strategy. Okay, last thing. I wanna give you a couple
examples of the legal AI assistant and we have this in beta right now. It's just getting out
the door. Ask a question. Are there a key man provisions in the PSA? What are the remedies on breach? What are the non-compete and non-solicit provisions
in the agreement? Can you give me a timeline of the facts presented in the documents? We're doing this now at scale and the results are incredible. And the reason the results are incredible, we're not just connected to an LLM because you saw today
like the LLMs changed. Every single week they're getting better. It's like a foot race. We did something very unique and Pallavi's gonna walk you
through the technology here. We're leveraging
vectorized data with Titan, with Symantec data, with
Elastic, with the LLM services as a kind of a trifecta
to analyze the documents and provide responses back. Very unique right now. And the results and the
quality of the results are through the roof. It's allowing us to get to a
place where we can do redlining with accuracy that lawyers will trust. Last thing to say here,
October we launched, we launched this in October of last year. We have 6,000 apps that have
been created by our customers. We're averaging 30 new apps
a week within our customers and we're doing 6,000 sessions
a week on this platform. So we're seeing rapid adoption and if there's any question of are our customers gonna
adopt generative AI in legal, I think we've answered
the question in spades. They're adopting and they're
adopting very, very quickly. All right, Pallavi, I
went long, I apologize so I hope we give you enough time. - Thank you very much, John. Actually that was a fantastic journey of your cloud journey migrating to AWS as well as innovations in the
document management space. So Olta and John covered a lot about challenges in the
legal industry and how the... Especially within the legal industry, the documents or unstructured
data is the core object. And we saw the challenges that these are in massive amount of scale. I was actually zapped by the scale, it's billions of documents in a year that we are talking about. So imagine searching
through such document scale and bringing that as a
forefront to the user so that they can converse
naturally with those documents as well as how honoring
the security permissions because that's going
to be super important. So this is where we are
seeing a lot of use cases that are being asked by our customers and we broadly categorize
those into three categories. The first one is summarization and shortly, I mean, John
talked about the legal assistant and there was... You can summarize contracts where you need to understand
what are the agreements and where are the risk areas
that are associated with it or generating case
summary is very critical in the legal research field. So summarizing the document, having generative AI summarize
that document for you and make it accessible to your users saves a lot of amount of time
for the legal professionals. So the key here is optimizing
your legal processes and then improving legal
professional's capability. We talked about legal
AI assistant a slide ago where idea is you have these
massive amount of documents, you make them searchable and when you are at that scale,
just writing semantic search and making those accessible
is a huge amount of task. And that is where we are using the generative AI advancements. And it's not just searching
through the documents but it is conversing
in a natural like flow. So the idea here is to
turn matter management into knowledge management, you need to be able to get good handle on the amount of unstructured
data or matters that you have and make that categorized,
well organized and searchable. The third use case broad category that we see is the text generation. And you would have seen
this is mainly about if you have standardized templates you can draft standardized
contracts or even RFI processes. The goal here is to remove that undifferentiated
heavy lifting and prepare or automate the workflows in such a way that you are able to create the draft versions of documents. Now, remember one thing we
will be very cautious here or one thing we follow the
principle for legal professionals is your documents need to be A, first of all honor all the permissions, it needs to follow the permissions that you are allowed to within the data. The context accuracy
is extremely important. They are very context aware documents and again we are giving
you the draft documents so that the legal professionals
can use their expertise, review the document and provide the final
human in the loop picture. So we did talk a lot about
generative AI and LLMs and foundation models, but let's put that into
perspective just real quickly here. So generative AI again is a
subset of deep learning model where you are using
large pre-trained models, which are foundation models to
create new content or ideas. And large language models, LLMs that we kept referring to are subset of or the specific foundation models that cater towards text
generation or text related task. Now, a quick poll to the audience. How many of you are building generative
AI applications today? Okay, I see quite a few hand raised. How many of you are training your users to write better prompts? Okay, all right, so we all know that we cannot use the foundation models and the large language models as is, they need to be customized. And this is where you're familiar with these four different steps. I'm just going to quickly
walk through them. So you start always with
the prompt engineering where you specify specific instructions on how to tailor the output
of the foundation model for your needs. The second one is the
retrieval augmented generation, where the key here is
to identify the right or relevant context from
large corpus of data. And it's not just one data source. You may have multiple data sources. So you wanna get the right context from those large corpus of data
and then augment your prompt with the relevant information. However, sometimes what
happens is RAG architecture is not enough. Sometimes you don't get
the model performance that you're looking for,
either it could suffer, it may not meet the accuracy
needs of your use case or it could be related to latency or both. In those cases, we have seen our customers take small amount of data and adjust the foundation models weights in such a way that you
are creating a model with specialized task, but again retaining the underlying
generative capabilities. So that's where you would fine tune or pre-train the underlying
foundation model. There are certain cases where
that is also not enough. It's either the foundation
model has biases that doesn't work for your use case or you have large amount of private data that is not being seen by these models when
they were being trained. And in those cases you would go for training
the model from scratch. Now remember, as you are
going through all these steps, the time, cost and complexity increases, but it also increases the accuracy. So we encourage you to look
at what your use cases, evaluate the different steps, and then use the right methodology to customize the foundation model. So let's take a look at
the generative AI stack and Olta talked about it at length that we do have the generative AI stack that's divided into three macro layers and there is infrastructure layer where Olta went into details
about Tranium and Inferentia, and you saw the announcements
that came in yesterday with Matt and Amazon SageMaker. So Amazon SageMaker is actually in the
infrastructure layer here because just having the
right chip set is good thing, but you need to have
additional capabilities such as distributed training, automated model tuning, et cetera. So this is where Amazon SageMaker, which is our managed
service to build, train, and deploy models at
scale, has these features such as distributed training where it can handle large amount of data and then give you options to
flexibily deploy these models as well as responsible
AI features and ML ops. So we did talk about if... But majority of our
customers do wanna build with existing foundation models and that's where Amazon
Bedrock comes into picture. Now, Amazon Bedrock, Olta
went into detail about this. It's our managed service
where you do get a choice of large foundation... Selection of foundation
models to choose from. And these are foundation models
from leading model providers as well as there are features that can help you build your
generative AI application. And then on top is the applications that leverage the LLMs or FMs, which means these applications
are completely built for you. Sometimes it may happen that you may not have
the specialized skills to build the generative AI applications or it could be that you just wanna explore the dataset real quickly. There is a new data source, you wanna see what the
data source looks like. Instead of building a
generative AI application, you can use what is already built in. So this is where Amazon
Q comes into picture. It can help you get that access to the enterprise data, again, with the right level of permission. And that is where Amazon Q
security comes into picture. So Amazon Q security, the way it is built is if user doesn't have access to data outside of Q, the user will not have access
to the data inside of Q and that's already built in. So you integrate with your data sources and get started with Amazon Q. Again, Amazon Q helps you
interact with your enterprise data as well as generate code,
create generative dashboards. So there are a lot of
features that Amazon Q offers. So let's take a look at our architectures. I mean we are going to talk
about few architecture patterns, but before that I wanna quickly highlight the Bedrock features that we will be using to go through those architectures. So one of the core
principles that we believe in is to give our customers... Our core value is mainly
to give you model choice, data privacy and customization. So from model choice perspective, John touched upon this
a little bit earlier that it's a race. There's new models that are
always coming into picture and no one model fits all use cases. So we want our customers to have a choice. So using Amazon Bedrock, you have a choice to select from the leading
foundation model providers such as Athropic, we have
Meta, we have Cohere, and this slide is already outdated because we have announced
our own model yesterday that Nova came into picture. So this is where... I mean it is like it's just a day old and my slide is already outdated. So this is what the fast innovation that is happening in this space. So we want you to have the
access to the right model that meets your cost, security
and latency requirement. This is going to be the key when you wanna choose a foundation
model that works for you. Think about the accuracy requirement, think about how much
it's going to cost you and think about the security practices. Having a choice of model is
great, but what about security? And that's the common question. That's the first question
we always get asked. So first thing is,
first, none of your data will be used by any of
this foundation model to better their models. So that's the first thing. Bedrock is built on
this security principle. Other thing that of
course the data that... Just like any other services, the data is encrypted in transit and at rest as well as it
does have the permissions, the right set of permissions that you have with
other AWS services also. So there's a specific
control that you can define on what features are accessible. Responsible AI, we cannot move forward without talking about responsible AI. So definitely wanna talk
about Amazon Guardrails, Bedrock Guardrails. Now Bedrock Guardrails provide
you additional safe guards that are built on top of the
foundation model providers. So using short natural description, it helps you define certain
topics that should be avoided by your generative AI application. And then you can also, the
guardrails also help you detect and block user inputs and
foundation model responses that fall into those specific topics. The other thing I wanna highlight, I mean you can also define... You can also control thresholds where you're protecting
against the harmful content, jailbreak or the prompt ingestion attack. The other thing I wanna
highlight is the guardrails. You define them once and
then they are model agnostic. That means you can really configure it with any model which is
offered within Bedrock. And again, Bedrock
offers number of features and those are the guardrail integration is native to those features. So we are going to go through
reference architectures for a couple of use cases and how we build using Bedrock features. But the first important point that I wanna talk about is RAG in action. And how many of you are
building applications with RAG architecture? Okay, so let's jump through
a little bit of details. So RAG typically has two workflows. A lot of times I hear complaints
from my customers that, well, the RAG is... Our documents are not coming out well, there's some accuracy issues, et cetera. So I highly recommend the customers looking at their data
ingestion workflow closely. Well, let's take a look at that. So we talked about earlier, there are large number of
documents and the goal here is to make those documents
available via Symantec search. In those cases, when you wanna make
such documents available via Symantec search, there
are certain processes or decision points that are involved. The first thing you would do is you wanna put these documents
in a vectorized database. Now you cannot put that entire document which is 500 pages sometimes, it cannot go in the
vectorized database as is. So it has to be chunked, which means there is specific paragraphs, a specific text that
is going to be chunked and that's how it is
going to be then embedded into a vector representation
and goes into the vector store. So there are document chunking. Choosing the right embedding model and choosing the right vector store for your use case are going
to be the key decision points that you have to make. And this is where I have
seen majority of the times that document accuracy suffers When you are building
the RAG architectures. In the legal space, the documents
that are going to come in, they're going to come in various formats. They are going to be PDFs,
they are going to be Words, they are going to be text
files or PDFs, scan PDFs. They're not laid out well. So this is where understanding
how those documents needs to be chunked and vectorized is going to be a key activity. And let's say I'm a user who wants to search
through specific contract and understand whereby if I
have a NDA with organization A. When that query comes in from a user, and this is where the text
generation flow happens, this is where the embedding model is going to translate that query
into vector representation, which then searches
through the vector database and generates context out of it. And that context is provided
along with the prompt that you will write to get the... Will get passed on to
a large language model and then you get your output. That sounds very cumbersome, right? There are a lot of things that you have to worry about chunking and moving the documents, et cetera. Well, that is where Amazon
Bedrock knowledge bases come into picture. Knowledge bases gives you that... It removes that
undifferentiated heavy lifting and gives you the choice to choose the right embedding model, choose the right chunking strategy, it is natively integrated with
the choice of vector stores. And then you can spin up
your manage RAG architecture to understand your document workflows. The important aspect
about why knowledge basis is the improved accuracy. And this is core, this
is a core architecture and core point to any time you wanna build semantic
search related capabilities or you wanna understand,
analyze the large documents. Understanding how well
your documents are chunked is important and that
is why knowledge bases offers you different... It offers you a control
over your chunking strategy such as hierarchical chunking. If a document has
parent-child relationship, it will automatically group the chunk, the document together in such a way that that
hierarchy is maintained. So when you are searching
through that document, the document accuracy improves because you have that
hierarchy maintained. Similar to semantic search, especially in the legal documents, semantic chunking capability
is extremely important because the document has related text scattered throughout the document. So the idea here would
be grouping that text and then storing that
in the specific chunk. Now, there are a lot of features that knowledge bases offer in terms of improving our accuracy, which I cannot go in
the next three minutes, but there is a session
that I will have it listed that tomorrow is happening, which goes through the deep
dive into knowledge bases and how to improve accuracy. I would highly recommend you attend that. So let's take a look at a couple of architectures real quick. So our architecture with
respect to a contract and tech process is
something that pretty much all organizations have,
whether it's a legal or whether you are an enterprise
who has a legal department. So let's put what we
learned, which is creating... I mean when you have matters,
turning the matter management or contract management into
a knowledge management. So let's put those learnings into practice where we have taken the executed contracts and then we are not only
doing the executed contracts, but we are extracting the metadata and attaching that metadata
to the vector store. This will help when you
have millions of documents and you need to understand that
when I retrieve my documents from Symantec search perspective, I have it filtered based
on what I'm asking. So this becomes a key that
these are the features that the knowledge base will support. So I have taken the list
of executed contracts, I have added them, extracted the metadata, attached that metadata to vector databases and created a knowledge base. So when a user like me who comes in and I ask, I need NDA with org A, let's say there is a
conversational user interface. Now you just heard Dr. Swamy Subramanian announce agent tech interfaces,
there are multiple... There is prompt, there is a model routing,
prompt caching, et cetera. A lot of beautiful features have come in. So using that, you can build a conversational interface which is going to take that query, understand what the ask is, extract the specific
metadata that this is NDA and the party is organization A is going to search through
the knowledge base, build the right results and
send the final response. Now, in my case I'm saying
that well, there is no NDA with org A, do you wanna create one? And this is where you can use
a conversational assistant where we haven't created
a rules based system. There is no if else happening here. The knowledge base or the agentic approach understands from the
existing executed contracts and it learns from the standard template. And also it's in own inherent knowledge about how contracts work
or different contracts is going to ask specific questions and get those draft contract created for a legal professional to review. Similarly, text generation RFI process, I hear there are multiple
weeks that are gone in. And this is where, again, you create and execute historical
RFI contracts, search, create a knowledge base
and search through them. And this process, actually the screenshot
that you're seeing, we have implemented this RFI process. It does save from weeks
to days of creating, generating a new RFI from
previously executed RFIs, improving the productivity of employees. Now, similarly, if you have a quick way, similarly if you have, let's say... We talked a lot about documents, but let's say you have videos and images. In those cases, you can
also make those accessible. For example, you have a lot of videos where there's testimony. In those cases, using our AI service, which is Amazon Transcribed, you can transcribe the
text, put that into S3 and simply put it to
Amazon Q for business, which is going to then
make that accessible. And then you can quickly start looking through asking questions such as who testified and what was there? Can you summarize this testimony? Again, maintaining who has
access to what that is core and a very important conversation. So having said that, in
closing, just a quick takeaways. So we learned from NetDocuments
about their journey and how they're bringing user efficiency and what their roadmap is to build more. So I want you to think about
the top three use cases and situations that can
improve your business process or workflows and what
brings the most value in generative AI use cases. What's the ROI associated
with those use cases? So as a final ask, I want you
to leverage the AWS community and start working on those, you have a access to maybe account access, you're working with the partners, or if you're not clear
about the mechanisms, please reach out to us. We can help you put in
the right direction. But this space, as John
earlier said, it is expanding. It is for you to remain
viable and competitive. This is going to be an important
task that you have to do, is you have to adopt. You wanna adopt generative
AI, improve efficiencies, optimize your workflows,
build automated workflows, and take advantage of it. That's it for now from me.
Here are the upcoming sessions. If you wanna take a picture of it. AIM305 is where you can go learn more about the RAG architectures and
how to improve the accuracy. Thank you very much for
staying with us today and please complete the survey. Your feedback is important
so we can improve. Thank you very much. (audience applauding)

## Subtitles with Timestamps

[00:00](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=0s) - Yeah, generative AI, that's what is...

[00:03](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3s) It's so impressive and exciting,

[00:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=5s) and that's what we are
here to talk about today.

[00:07](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=7s) So welcome everyone to NTA311,

[00:11](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=11s) transforming how generative
AI is transforming legal tech

[00:14](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=14s) with AWS.

[00:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=16s) My name is Pallavi Nargund,

[00:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=18s) I'm a principal solutions
architect at AWS,

[00:21](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=21s) and I'm also a chief technologist

[00:23](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=23s) for the legal tech community within AWS.

[00:27](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=27s) Joined with me today is John
Motz, CTO of NetDocuments

[00:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=32s) and Olta Alushi, who is also a co-founder

[00:36](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=36s) of Legal Tech community within AWS Alta.

[00:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=39s) Olta, to you.

[00:41](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=41s) - Thank you, Pallavi. Hi everyone.

[00:43](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=43s) I'm excited to be here with all of you.

[00:46](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=46s) For the next hour,

[00:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=48s) we'll be talking about the
legal industry, the landscape,

[00:52](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=52s) and the technology adoption
within legal industry.

[00:55](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=55s) And then John here will walk us through

[00:57](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=57s) the innovative journey with generative AI

[01:00](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=60s) and AWS within NetDocuments.

[01:02](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=62s) And then Pallavi will close us
with use cases in legal tech

[01:07](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=67s) and reference architectures.

[01:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=72s) Imagine a future where
the legal technology

[01:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=76s) and legal industry is revolutionized

[01:19](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=79s) by the generative AI.

[01:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=82s) Picture all these tedious
tasks being automated,

[01:25](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=85s) allowing legal professionals

[01:27](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=87s) to focus on the most important
aspects of their profession.

[01:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=92s) Think of legal research
being not just faster

[01:36](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=96s) but smarter and more
comprehensive than ever before.

[01:42](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=102s) Data in the 21st century

[01:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=105s) is the equivalent of
gold in the 19th century,

[01:49](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=109s) and through artificial intelligence,

[01:51](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=111s) we have been able to
open up new data sources

[01:55](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=115s) that were not reachable before.

[01:58](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=118s) Imagine legal profession
undergoing a transformation

[02:03](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=123s) as revolutionary as other
industries have seen,

[02:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=126s) like finance or healthcare,

[02:08](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=128s) where through AI assisted research,

[02:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=132s) we have been able to
expand the global markets,

[02:14](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=134s) introduce instantaneous payments,

[02:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=137s) improve customer experience,

[02:19](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=139s) and even expand our lifespans.

[02:23](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=143s) Now, imagine the same innovative
spirit applied to law,

[02:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=148s) but what if we could
amplify the capabilities

[02:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=152s) shortening the contract
drafting that it takes lawyers

[02:36](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=156s) or legal professionals to do today,

[02:38](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=158s) or the way that it...

[02:40](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=160s) Like how much time it takes
them to predict cases.

[02:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=164s) Up to 44% of legal tasks
today based on research

[02:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=168s) can be automated,

[02:50](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=170s) which is a figure that
outstrips many other industries,

[02:55](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=175s) so this can actually be done.

[02:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=179s) The real magic though of generative AI

[03:01](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=181s) is in freeing the legal professionals

[03:04](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=184s) to focus on the most human
aspects of their profession,

[03:08](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=188s) and that is to exercise
empathy, strategy and advocacy.

[03:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=196s) But let's first define legal tech.

[03:19](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=199s) Legal tech is a combination
of digital tools, software

[03:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=204s) and applications that get
applied to legal companies,

[03:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=208s) and that includes law firms,

[03:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=210s) legal counsels within large corporations

[03:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=213s) to boost the productivity,
to enhance the value

[03:38](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=218s) of their legal services
and to reduce costs

[03:41](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=221s) all through the automation
of legal workflow.

[03:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=225s) When it comes to applying
technology within the industry,

[03:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=228s) we first want to
understand its challenges.

[03:52](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=232s) Technology set up today

[03:54](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=234s) should be able to support
processing large documents

[03:58](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=238s) of unstructured text of any size and form,

[04:02](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=242s) and that setup has to be
enabling the end users

[04:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=246s) not creating a bottleneck.

[04:09](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=249s) The second is balancing skill and value.

[04:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=252s) We have seen a growing concern

[04:14](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=254s) with devaluation of legal skills.

[04:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=257s) As we know, as an example,

[04:19](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=259s) junior lawyers spend a lot
of time doing research,

[04:23](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=263s) contract drafting and other legal tasks,

[04:26](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=266s) and the question becomes

[04:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=268s) how does the next generation
of lawyers, for instance,

[04:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=272s) gain that practical experience
if automation is in the loop?

[04:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=277s) And how do law firms in fact
justify work like billing

[04:41](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=281s) for work that now gets
implemented by machines?

[04:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=287s) The third concern that we
see is with data privacy

[04:50](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=290s) and security, and we
know that legal companies

[04:54](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=294s) handle sensitive information

[04:56](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=296s) that goes from corporate
data to client data.

[05:00](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=300s) And as this data gets digitized

[05:02](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=302s) and moves to the cloud,
there is a growing perception

[05:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=305s) that risk of data breaches
also grows exponentially.

[05:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=310s) But in fact, the data
shows that organizations

[05:13](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=313s) that have reported data breaches

[05:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=316s) within the cloud environments,

[05:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=317s) they are attributing those
breaches to human error

[05:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=322s) and misconfiguration
of cloud environments.

[05:26](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=326s) And the last one is the
challenge with productivity.

[05:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=330s) That is a complex one to execute,

[05:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=333s) but what it means in itself
is reducing the time it takes

[05:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=337s) for you to do this
repeatable, mundane tasks.

[05:42](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=342s) And if you don't select the right systems,

[05:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=344s) the right architecture and the technology

[05:46](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=346s) to complement that legal workflow,

[05:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=348s) productivity may actually decline.

[05:51](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=351s) At AWS, we believe that
technology should enhance

[05:56](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=356s) not replace the human elements
of the legal practice.

[06:03](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=363s) In legal tech, there is
this concept of a flywheel,

[06:07](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=367s) which is this idea that
the small initial effort

[06:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=370s) leads to significant
positive outcome over time.

[06:14](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=374s) After each revolution, we see positive ROI

[06:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=378s) and positive outcome for customers

[06:19](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=379s) that implement their process, their data,

[06:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=382s) and their people against
this flywheel concept.

[06:25](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=385s) Let's illustrate that concept

[06:26](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=386s) through a document handling approach.

[06:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=390s) We start by mapping document repositories,

[06:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=393s) organizing and centralizing this data

[06:36](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=396s) so that it is searchable by
everyone in the organization.

[06:40](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=400s) Then we process this with
natural language processing

[06:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=404s) to understand its content,

[06:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=405s) and then we extract the metadata from it

[06:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=408s) to better organize it.

[06:50](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=410s) Then third, we add the AI and
machine learning capabilities

[06:55](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=415s) to analyze patterns and
to learn to create systems

[06:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=419s) that actually learn contextually

[07:01](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=421s) what that data actually represents.

[07:04](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=424s) And so at the end of the day,

[07:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=425s) there is a system that gets
deployed for legal professionals

[07:08](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=428s) to now run very complex
queries against this data set,

[07:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=432s) and that produces this precise
context aware responses

[07:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=437s) in a matter of minutes.

[07:19](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=439s) And as we said, after each revolution,

[07:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=442s) the ROI improves over time.

[07:25](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=445s) And the customers that
have worked with AWS

[07:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=448s) and AWS technologies,

[07:29](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=449s) they tell us that they see
contract generation completion

[07:34](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=454s) within hours versus weeks

[07:36](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=456s) and productivity improvement by up to 15%.

[07:40](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=460s) But your numbers here could be different.

[07:42](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=462s) Your use cases could be different.

[07:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=465s) Let's talk now for a little
bit about why legal customers

[07:50](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=470s) choose to work with AWS.

[07:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=473s) For 18 years, AWS has been
delivering cloud services

[07:56](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=476s) to millions of customers around the world

[07:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=479s) in a variety of use cases and workloads.

[08:02](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=482s) The AWS region and availability model

[08:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=486s) is recognized by Gartner

[08:07](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=487s) as the recommended approach
to run enterprise applications

[08:11](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=491s) with high availability and
the 108 availability zones,

[08:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=496s) 34 regions that are available today

[08:19](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=499s) give you the opportunity to
run enterprise applications

[08:23](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=503s) across the globe, especially
when you have to abide

[08:27](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=507s) to country data residency laws.

[08:31](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=511s) AWS is the most secure with
300 plus security services

[08:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=517s) around compliance and governance,

[08:38](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=518s) and that includes features

[08:40](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=520s) as well as supporting
143 security standards

[08:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=524s) and certifications.

[08:46](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=526s) AWS cloud is sovereign by design,

[08:50](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=530s) and we will talk more
about this in a little bit,

[08:52](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=532s) but what that means is that our pledge

[08:55](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=535s) to digital sovereignty

[08:56](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=536s) allows us to build services and features

[09:00](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=540s) that meet always the customer's
regulatory requirements.

[09:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=546s) And we are at the
forefront of generative AI

[09:09](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=549s) with 100,000 plus
customers already using AI

[09:14](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=554s) and ML services.

[09:15](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=555s) Now, when it comes to generative AI,

[09:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=558s) our mission is to
democratize generative AI

[09:21](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=561s) by offering flexibility and choice

[09:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=564s) for our customers that want to
run workloads and production.

[09:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=568s) And we look at generative AI
in three layers of a stack,

[09:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=572s) and we'll go deeper on this
in a little bit as well.

[09:35](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=575s) When it comes to deploying
generative AI in production,

[09:38](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=578s) at the bottom of the stack, we see models

[09:42](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=582s) where we provide AWS build silicon chips

[09:46](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=586s) so that you can train
models from the ground up,

[09:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=588s) but in a more cost effective way,

[09:51](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=591s) that is applicable to training

[09:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=593s) and inference type workloads as well.

[09:55](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=595s) In the middle of the stack,

[09:57](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=597s) we provide you a secure way to build

[10:00](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=600s) and scale applications
leveraging leading AI,

[10:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=605s) generative AI or large foundation models

[10:08](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=608s) so that you can switch between
these large language models

[10:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=612s) made available through our
Amazon Bedrock service,

[10:15](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=615s) which you may have heard multiple
times throughout the week.

[10:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=618s) And that is our fully managed service,

[10:20](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=620s) which in very short terms
gives you the ability

[10:23](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=623s) to switch between models.

[10:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=624s) You can customize these
models for better performance

[10:27](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=627s) and even allow it

[10:29](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=629s) to do automated tasks
without writing any code.

[10:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=633s) And at the top of the
stack, we have applications

[10:36](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=636s) that use these large language models,

[10:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=639s) but that help you to get up
and running pretty quickly.

[10:42](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=642s) So all you have to do is
point your data sources

[10:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=645s) to the application

[10:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=647s) and then you can ask it
questions, create content

[10:50](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=650s) or even add additional actions
that you wanted to take

[10:54](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=654s) all while leveraging the intelligence

[10:57](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=657s) that exists in your
organization's data repositories.

[11:02](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=662s) Now, we talked about security,
privacy, and responsible AI.

[11:08](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=668s) That is at the top of our priorities

[11:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=672s) when it comes to working
with legal tech customers.

[11:15](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=675s) And we place this in the forefront

[11:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=677s) of every technology that we build.

[11:20](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=680s) Any architecture and any
service that you place on AWS

[11:25](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=685s) inherits the same security
standards that we build.

[11:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=688s) We provide that enterprise grade security,

[11:31](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=691s) meaning that anything like we said

[11:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=693s) is built on AWS inherits (indistinct)

[11:35](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=695s) and we give you full control of the data,

[11:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=699s) full control of your data,
while also giving you options

[11:43](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=703s) to enable encryption keys
to manage encryption keys,

[11:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=707s) and in addition,

[11:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=708s) apply data protection policies
across your data's journey

[11:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=713s) in your organization.

[11:55](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=715s) Our identity management system
also allows you to enable

[12:00](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=720s) and manage user access policies

[12:02](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=722s) so that you can enable tight controls

[12:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=725s) over who accesses which data and when.

[12:11](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=731s) When you customize, and this is important,

[12:13](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=733s) a foundational model,

[12:15](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=735s) your data does not leave
your virtual private cloud

[12:20](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=740s) on AWS and it does not get used to update

[12:23](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=743s) that base foundational model.

[12:26](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=746s) And we'll talk more about
this in a little bit.

[12:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=750s) Now, at the beginning of the session,

[12:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=752s) we talked about re-imagining
document handling,

[12:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=757s) and we also talked about

[12:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=759s) why customers choose to work with AWS

[12:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=764s) and they say that they
need security, privacy,

[12:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=767s) the right performance,
the right cost structure,

[12:49](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=769s) and the right solutions that
are relevant to their business.

[12:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=773s) Having said that,

[12:54](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=774s) I would like to introduce
John Motz on stage,

[12:57](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=777s) CTO of NetDocuments.

[13:00](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=780s) - Thanks, Olta.

[13:01](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=781s) So I'm gonna start with
a little bit of context

[13:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=786s) about NetDocuments.

[13:07](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=787s) If you don't know NetDocuments,

[13:09](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=789s) we've been around 20 plus or so years.

[13:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=792s) I've been here as CTO for about two years.

[13:15](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=795s) We're all over the world. We're global.

[13:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=797s) Six regions doing business
in many, many countries

[13:21](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=801s) around those regions, about 5,000 firms,

[13:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=804s) although we're adding it seems
like several a day frankly.

[13:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=808s) So we're growing pretty rapidly right now.

[13:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=810s) There was a big push into cloud services

[13:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=813s) through the pandemic with legal.

[13:35](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=815s) It saw a very big burst
relative to some industries

[13:38](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=818s) that had already shifted to
cloud quite a bit before then.

[13:40](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=820s) 185,000 users globally, and
that's legal professionals,

[13:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=825s) assistants, things like that.

[13:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=827s) Over 8 billion documents,

[13:49](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=829s) and that's greater than 20 billion files.

[13:51](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=831s) And so we're adding millions
and millions of files

[13:54](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=834s) every day with our customer
base into the platform.

[13:57](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=837s) 21 petabytes of data.

[13:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=839s) Although again, this changes
almost every single day.

[14:03](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=843s) I think most importantly,

[14:04](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=844s) and probably most impressive for me

[14:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=846s) is we're doing roughly about
650 million transactions a day.

[14:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=850s) And so when you think about the platform

[14:13](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=853s) as a legal professional,
you get a document,

[14:15](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=855s) you get a new case, you get a new matter,

[14:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=857s) the first thing you're doing
is ingesting that document

[14:20](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=860s) into your document management system.

[14:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=862s) So every single day you're interacting.

[14:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=864s) Once it's in the system,
every piece of your workflow

[14:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=868s) is running through our platform,

[14:29](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=869s) whether you're checking it in,
checking it out, editing it,

[14:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=872s) changing it, sharing it,

[14:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=873s) all runs through the
NetDocuments platform.

[14:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=877s) And then we are ingesting quite a bit.

[14:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=879s) And so when you think about the process,

[14:41](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=881s) and you'll see some of this
coming up in the slides,

[14:43](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=883s) it's not just about storing a document.

[14:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=885s) We do a lot of processing,
a lot of metadata extraction

[14:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=888s) and creation on that document,

[14:50](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=890s) and we're doing about 25
million new documents a day

[14:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=893s) through that process, which
is pretty incredible frankly.

[14:56](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=896s) As you think about that,

[14:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=899s) the legal space started
with this foundation

[15:02](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=902s) and it's been pretty much
the same for 15 or 20 years

[15:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=906s) within document management.

[15:07](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=907s) And for the first time in a long time,

[15:09](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=909s) we're seeing that change.

[15:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=910s) And so first and foremost, lexical search.

[15:14](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=914s) So if you're a legal professional

[15:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=916s) and you're looking for
something in a document system

[15:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=918s) and think...

[15:19](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=919s) Think about this.

[15:20](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=920s) A firm, a large firm

[15:21](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=921s) could have literally hundreds
of millions of documents

[15:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=924s) in their document management system.

[15:26](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=926s) You have to be able to find it.

[15:27](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=927s) And lexical search is how
we've done it for years.

[15:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=930s) I can tell you in
talking to our customers,

[15:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=933s) the holy grail for them
has been semantic search.

[15:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=937s) It's just really been out of reach

[15:38](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=938s) and it's been out of reach
for reasons tied to cost,

[15:40](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=940s) the ability to even actually
process and manage it well.

[15:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=944s) And then it is a change.

[15:46](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=946s) And sometimes change can be challenging.

[15:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=947s) I think the generative AI push

[15:49](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=949s) that has happened in the last year

[15:51](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=951s) is changing the expectations
for professionals

[15:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=953s) and particularly legal professionals.

[15:55](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=955s) They want to find items

[15:57](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=957s) as they would ask for them naturally.

[15:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=959s) And that's what we're seeing.

[16:00](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=960s) And so a pretty significant change

[16:02](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=962s) moving to semantic search, and
it's deep within our roadmap

[16:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=965s) and what we're already delivering today.

[16:07](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=967s) Beyond that is this concept
of check in and checkout.

[16:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=970s) And if you are a legal
professional, you know what this is.

[16:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=972s) If you're not a legal professional,

[16:13](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=973s) this is essentially putting
a document into the system

[16:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=976s) and taking a document out.

[16:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=977s) In the legal world, it's
a lot more complex though

[16:20](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=980s) because there's controls,
very tight controls.

[16:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=982s) A big part of our platform

[16:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=984s) is being able to have permissions,
rights, authorizations,

[16:29](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=989s) not just for people
working within the firm

[16:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=992s) or the corporate legal,

[16:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=992s) but also customers as
well as counsel outside

[16:36](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=996s) that you have to share documents with.

[16:38](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=998s) So checking in and checking out

[16:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=999s) is a very, very important
part of the architecture

[16:42](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1002s) as well as the platform.

[16:43](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1003s) What we're seeing though is
that is getting to a point

[16:46](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1006s) where we want co-authoring.

[16:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1008s) We want to be able to work in
a document at the same time.

[16:51](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1011s) We don't want to have to
check things in and out

[16:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1013s) in multiple copies

[16:55](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1015s) and some documents in a
document management system

[16:58](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1018s) could have thousands of versions

[16:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1019s) depending on how long the
case or the matter ran.

[17:02](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1022s) We wanna move to co-authoring.

[17:03](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1023s) This is again, an expectation
our customers have.

[17:08](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1028s) And then security.

[17:09](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1029s) Security, we've already talked
about this, critical for AWS.

[17:14](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1034s) Frankly, it's one of the primary reasons

[17:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1036s) we've chosen AWS for our cloud strategy.

[17:19](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1039s) For us, security is paramount.

[17:21](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1041s) These are the most sensitive documents

[17:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1042s) that you can find in the world, frankly,

[17:25](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1045s) you have to make sure they're secure.

[17:27](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1047s) I think the thing that is
really interesting right now

[17:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1050s) from a security perspective is
it's evolving to include AI.

[17:35](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1055s) And so you're gonna see
here in a few minutes

[17:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1057s) how we're leveraging AI

[17:38](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1058s) within our document management workflow.

[17:40](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1060s) What's getting really, really interesting

[17:43](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1063s) is now AI is doing things
like generating content

[17:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1067s) for legal professionals.

[17:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1068s) It's analyzing documents
for legal professionals.

[17:51](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1071s) We need to understand what
the AI is actually analyzing.

[17:56](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1076s) We need to understand
what the AI is authoring.

[17:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1079s) We need to understand when
changes are being made by AI

[18:02](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1082s) and ensure we apply the same
security we've applied to users

[18:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1085s) for the last two decades
to AI within the platform.

[18:09](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1089s) So critical part for us.

[18:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1092s) So when you think about
that and NetDocuments

[18:15](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1095s) we're shifting our thinking.

[18:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1097s) Document management with workflow

[18:19](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1099s) is what we've been doing
again for two decades plus.

[18:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1102s) Where we're evolving to is this concept

[18:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1104s) of an intelligent and simple platform.

[18:26](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1106s) And when you think about that,

[18:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1108s) a lot of customers and a
lot of companies, frankly,

[18:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1110s) and if you literally
walk through re:Invent,

[18:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1113s) you'll see, I'm guessing,
a couple hundred companies

[18:35](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1115s) that are solving AI for
a very niche problem.

[18:40](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1120s) We think about AI across
the entire platform.

[18:42](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1122s) And so we're building the platform

[18:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1124s) to enable AI in every
aspect of the workflow.

[18:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1128s) We want this to be a workflow
engine driven by AI and data

[18:52](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1132s) that delivers a very, very
intelligent and smart experience.

[18:56](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1136s) And so what you'll see,

[18:57](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1137s) you'll see a little bit of
us solving niche problems

[19:00](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1140s) as we started this,
call it late last year,

[19:03](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1143s) where it's moving through
very rapidly with AWS

[19:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1146s) is this underlying data platform

[19:08](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1148s) that drives an intelligent experience

[19:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1150s) and an AI experience through
every single workflow.

[19:15](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1155s) So why AWS?

[19:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1157s) I've gotta touch on this.

[19:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1158s) This is a relatively new journey for us.

[19:20](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1160s) We're 12-ish months into our push into AWS

[19:26](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1166s) and it was a pretty big decision for us.

[19:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1168s) So imagine a company 20 years plus

[19:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1170s) running in a private environment

[19:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1173s) for many, many years since day one,

[19:35](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1175s) proprietary encryption,

[19:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1177s) Anthropic encryption that
we built 20 so years ago,

[19:42](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1182s) big HSMs everywhere securing
all of our data and content.

[19:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1185s) So a pretty big change for us.

[19:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1187s) When you think about this, and
Olta touched on this as well,

[19:51](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1191s) I wanna touch on a couple things.

[19:52](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1192s) Mainly my data's a little wrong with 99.

[19:55](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1195s) It's apparently 108,
it's probably 112 now.

[19:58](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1198s) But the level of cultural matching

[20:03](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1203s) that we had with AWS and our
team internally was astounding.

[20:07](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1207s) And when you look at these
metrics, they're all impressive.

[20:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1210s) You know, the regions, the
security, the ecosystem.

[20:15](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1215s) For us, it was AWS really thinks like us.

[20:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1218s) They think about innovating quickly.

[20:20](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1220s) The fact that we're here every year

[20:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1222s) and I literally was
typing emails yesterday

[20:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1224s) after the keynote to my team.

[20:26](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1226s) "We gotta do this, we're gonna do that.

[20:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1228s) Let's pivot over here." You
have to be able to do that.

[20:31](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1231s) And if you wanna stay viable

[20:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1233s) and you want to meet the customer's needs,

[20:35](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1235s) which is what we're
here to do as a company,

[20:38](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1238s) we needed that kind of a partner.

[20:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1239s) So a lot of great
capabilities drove us to AWS.

[20:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1244s) I think if I had to pick one,

[20:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1245s) I would lean deeply into security.

[20:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1248s) When you think about the
security model that AWS is using

[20:51](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1251s) and the ability to secure
at the silicon level,

[20:54](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1254s) the ability to isolate security
down to single data elements

[20:58](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1258s) and objects is really,
really important for us.

[21:01](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1261s) And we felt by a long, long
margin, the future state

[21:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1265s) and the kind of the forward thinking

[21:07](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1267s) from a security perspective was critical.

[21:11](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1271s) Absolutely critical.
So what does this mean?

[21:14](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1274s) How is this changing how we're building?

[21:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1276s) Where are we applying
this over the last year

[21:20](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1280s) to build this platform,
this intelligent platform?

[21:23](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1283s) And I think of three things.

[21:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1284s) I think of data-driven experiences,

[21:26](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1286s) I think of right tools for the job,

[21:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1288s) and then I think of nurturing
a culture of innovation.

[21:31](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1291s) And when you think about
data-driven experiences,

[21:34](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1294s) for me it's about flexibility.

[21:36](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1296s) And I just talked about sending the email

[21:38](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1298s) to the team yesterday.

[21:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1299s) We have to have a platform
that can adapt to technologies

[21:43](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1303s) and be able to move quickly.

[21:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1304s) And so we're building
an architecture with AWS

[21:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1307s) that will allow us to switch
to their mesh framework

[21:50](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1310s) when it comes out

[21:51](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1311s) 'cause we asked for it
about seven months ago

[21:54](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1314s) and we love that, we wanna be
able to take advantage of it

[21:57](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1317s) and not take nine months to do that

[21:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1319s) or even a year or more.

[22:01](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1321s) And so the architecture is built for that.

[22:04](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1324s) We need to be flexible,
we need to be responsive

[22:07](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1327s) and not as in a UI and
stretching across screens.

[22:11](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1331s) We need to...

[22:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1332s) Someone got that.

[22:14](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1334s) We need to be able to respond
to the customer's needs

[22:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1338s) as we understand how they're
using the platform, right?

[22:21](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1341s) Because we're introducing new experiences,

[22:23](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1343s) we're introducing AI into our workflows.

[22:25](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1345s) We're learning a ton right now.

[22:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1348s) We're understanding how
customers are using the platform.

[22:31](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1351s) We've gotta be able to
respond to that behavior

[22:34](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1354s) and change how the data
is driving the experience.

[22:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1357s) And then scale, and scale,

[22:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1359s) again, I'm not talking
about EC2s and Fargate,

[22:42](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1362s) I'm talking about being able
to scale the organization

[22:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1365s) and the technology

[22:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1367s) because there's too many new
things that are coming at us.

[22:49](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1369s) We've gotta be able to
scale and move fast.

[22:52](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1372s) And so for us, this is
organizational structure.

[22:54](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1374s) How have we organized our teams?

[22:56](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1376s) And we shifted over the last two years

[22:58](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1378s) from teams of about 10
or so, in some cases

[23:03](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1383s) even a little larger,

[23:04](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1384s) most of them tightly
coupled with dependencies.

[23:07](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1387s) And we're shifting the models

[23:08](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1388s) where our teams are as
small as four to five.

[23:11](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1391s) We have incredible adoption
of AI generated code

[23:15](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1395s) that's being embedded in our workflows

[23:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1397s) with our development teams

[23:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1398s) to get more scale from smaller
teams and more efficiencies.

[23:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1402s) Critical part for us being successful

[23:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1404s) over the next few years.

[23:26](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1406s) Right tools for the job,
event driven architecture.

[23:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1410s) And I'm not saying we don't
believe in APIs anymore.

[23:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1413s) We definitely believe in APIs,

[23:34](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1414s) but we are leveraging Amazon

[23:36](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1416s) to build an event driven architecture

[23:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1417s) because we're moving away

[23:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1419s) from the response request
model in our platform

[23:42](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1422s) and our applications.

[23:43](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1423s) We want to be able to take those events,

[23:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1425s) understand what our customers

[23:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1427s) and users have done in the system

[23:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1428s) and trigger actions and jobs.

[23:50](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1430s) And you'll see some of those,

[23:51](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1431s) you know, here in a few minutes,

[23:52](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1432s) without any intervention from
the customer or the user.

[23:55](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1435s) That's incredibly important

[23:56](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1436s) When you think about
leveraging generative AI

[23:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1439s) in the workflow.

[23:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1439s) You've gotta be able to be proactive

[24:02](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1442s) and reacting to those events

[24:04](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1444s) versus waiting for someone to take action.

[24:07](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1447s) AI and automation, again,
another big part for us.

[24:11](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1451s) Our company as a whole,

[24:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1452s) outside of what we're
doing with our customers,

[24:15](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1455s) we are looking at AI and automation

[24:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1457s) across every segment of our business.

[24:19](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1459s) We think it's that important

[24:20](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1460s) and we're leveraging that to work faster.

[24:23](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1463s) We're leveraging that

[24:23](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1463s) to deliver better
metrics to our customers,

[24:26](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1466s) better metrics to our operations team

[24:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1468s) so we can manage the
environments better with AWS.

[24:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1470s) Very, very important part
of what we're doing here.

[24:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1473s) It's interesting when you
think about AI automation,

[24:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1477s) you have to be comfortable picking up new

[24:40](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1480s) and different tools that
you haven't used before

[24:42](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1482s) to run your business.

[24:43](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1483s) And sometimes that can be a little hard

[24:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1485s) and frankly you have to
account for that cost model

[24:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1488s) because you're going to have that overlap.

[24:50](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1490s) But I can tell you our experience
is once you make that call

[24:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1493s) and you get into that new world,
it becomes so much better.

[24:56](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1496s) You get much more efficient

[24:58](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1498s) and you get past that
overlap cost very quickly.

[25:01](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1501s) And I think the thing that's...

[25:02](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1502s) For me that's really been
insightful with our teams

[25:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1505s) is they're actually happier employees.

[25:08](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1508s) They're able to do their jobs better

[25:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1510s) with higher quality and higher efficiency.

[25:13](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1513s) The last one here, not
very important at all.

[25:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1516s) It's just the cloud
service partners like AWS.

[25:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1518s) We couldn't do this without
AWS, there's no way we could

[25:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1522s) and our decision to move
into AWS was really simple.

[25:26](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1526s) We couldn't keep up, we couldn't
keep a private environment

[25:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1530s) anywhere close to the level of innovation

[25:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1532s) we're going to get from AWS.

[25:34](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1534s) And again, you don't
have to look any further

[25:36](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1536s) than this event this week to see that.

[25:40](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1540s) Nurturing a culture of innovation.

[25:41](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1541s) So it's interesting, I built this slide

[25:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1545s) and it said adopting a
culture of innovation

[25:49](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1549s) and my CEO corrected me and he said,

[25:52](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1552s) "Well, we've been
innovative for 20 years."

[25:54](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1554s) And so we made a tune there,
but it really is the truth.

[25:58](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1558s) I mean, we came up with Anthropic
encryption 20 years ago,

[26:02](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1562s) which is pretty darn innovative.

[26:03](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1563s) We were doing cloud document management

[26:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1565s) when most people were doing on-premise.

[26:08](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1568s) And so it is true, we are
definitely an innovative company

[26:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1570s) and an innovative group.

[26:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1572s) It's really important to understand,

[26:13](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1573s) we do that through engaging with customers

[26:15](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1575s) and I think a lot of people

[26:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1576s) lose sight of how important that is.

[26:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1578s) Our engineering teams spend
time with our customers,

[26:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1582s) our engineering teams go through
the same product training

[26:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1584s) and onboarding training

[26:25](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1585s) that our customers and
partners go through.

[26:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1588s) We're organized for agility.

[26:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1590s) We're a company of empowered engineering

[26:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1592s) and operations and design.

[26:34](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1594s) We want our teams to go
figure out the problems

[26:38](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1598s) and then literally build
three or four concepts

[26:41](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1601s) and see which one works,
see one doesn't work

[26:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1604s) and make decisions that way.

[26:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1605s) We move very, very fast for
an organization our size.

[26:49](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1609s) And you know, I think generally
we're doing daily releases

[26:52](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1612s) on most of our applications

[26:54](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1614s) and then we push our teams
to challenge the status quo.

[26:58](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1618s) And this is gonna sound
a lot like the Amazon

[27:00](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1620s) and it's not a surprise.

[27:02](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1622s) Like we have adopted a lot
of the same core values.

[27:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1625s) I wanna hear the challenges.

[27:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1626s) I wanna hear why the solution
that we created 15 years ago

[27:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1630s) that was incredible at the
time isn't good enough today.

[27:13](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1633s) And so we're not just
building new applications,

[27:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1636s) we're reinventing and re-imagining
the problems we solved

[27:19](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1639s) 10 or 20 years ago based on the technology

[27:21](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1641s) that's available today.

[27:23](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1643s) A critical part of how we're building

[27:25](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1645s) and how we're innovating.

[27:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1648s) All right, so what does
that leave us with?

[27:31](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1651s) It's pretty straightforward.

[27:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1652s) Maximum performance, maximum security,

[27:36](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1656s) maximum innovation and maximum value.

[27:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1659s) And really that is the
number one objective for us

[27:42](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1662s) in that partnership with Amazon.

[27:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1664s) Very straightforward goals,
very straightforward targets,

[27:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1667s) which I also think is really critical

[27:49](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1669s) for getting your team
centered in moving forward.

[27:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1673s) So the last slide around Amazon

[27:57](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1677s) and how we're doing this, if you will,

[27:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1679s) I wanted to talk about why Amazon.

[28:00](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1680s) And this is a screenshot

[28:02](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1682s) of our kind of an analysis evaluation.

[28:07](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1687s) And I always joke with our Amazon rep,

[28:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1690s) I don't think they ever thought
the deal was gonna close.

[28:13](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1693s) We went through the ringer on the analysis

[28:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1697s) to the point where we were
building our infrastructure

[28:20](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1700s) during the evaluation.

[28:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1702s) This wasn't a PowerPoint
slide exercise for us.

[28:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1704s) We built the new data objects,

[28:27](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1707s) we built all the new EC2 instances,

[28:31](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1711s) we ran them at scale as well.

[28:35](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1715s) We had a lot of sizing done.

[28:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1717s) So again, we're a year into this,

[28:40](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1720s) we got to a 90% accuracy
on our cost to run.

[28:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1724s) And so far holding true to that.

[28:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1727s) Frankly it's come down a little bit

[28:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1728s) because of some of the graviton releases

[28:50](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1730s) that have happened since
we made the decision.

[28:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1733s) We also really looked at a cloud partner.

[28:58](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1738s) And for me, taking an organization

[29:01](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1741s) that has never run a public cloud,

[29:04](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1744s) you can't just turn an organization over.

[29:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1746s) These are incredibly talented people,

[29:09](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1749s) but there's also a learning curve.

[29:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1750s) And so we were very,
very explicit in saying,

[29:14](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1754s) we're gonna resource this
with a critical partner

[29:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1756s) for about 50% of our resource
allocation and then train up

[29:21](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1761s) and create a bridge for our existing team.

[29:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1764s) Really, really cool to see

[29:25](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1765s) if you're looking at
the data that I look at.

[29:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1768s) As of now, 95% of our
existing team within CTO,

[29:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1773s) which is operations,
engineering, security,

[29:35](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1775s) have taken and have
been certified with AWS

[29:38](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1778s) in the first year, which is incredible.

[29:40](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1780s) Frankly, the fastest
I've ever seen it happen.

[29:41](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1781s) I've done this more than a couple times.

[29:43](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1783s) And so we give 'em the platform
and the ability to learn

[29:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1787s) and grow along the journey,

[29:49](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1789s) not expecting them to be
AWS experts on day one.

[29:54](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1794s) And then the last thing I
would say is the architecture.

[29:58](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1798s) We really wanted to understand

[30:01](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1801s) what the complete architecture
was gonna look like

[30:04](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1804s) before we started doing the work.

[30:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1805s) And it was really important for us

[30:07](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1807s) because it allowed us to make
very thoughtful decisions

[30:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1810s) around what we're going to do first.

[30:11](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1811s) And a lot of folks go
after the easy stuff first.

[30:15](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1815s) We did the exact opposite.

[30:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1816s) We went after the four hardest things

[30:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1818s) that we knew we had to get after

[30:20](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1820s) because we knew we were gonna pivot.

[30:21](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1821s) We knew we were gonna find
the changes we wanna make,

[30:25](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1825s) we knew we were gonna struggle frankly.

[30:27](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1827s) And so we figured if we can knock off

[30:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1830s) the four hardest aspects
of our architecture

[30:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1832s) in our platform in year one,

[30:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1833s) the second year would be pretty easy.

[30:36](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1836s) And sure enough, that's where we are.

[30:38](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1838s) We're fighting through some
of that stuff right now,

[30:42](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1842s) but we're also doing it the right way

[30:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1844s) and we're not sacrificing
the architecture for time.

[30:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1847s) We're very focused on
building it the right way

[30:49](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1849s) and leveraging our well
architecture reviews

[30:52](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1852s) and our Amazon partners to do that,

[30:54](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1854s) which is pretty incredible.

[30:56](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1856s) Okay, so I'm gonna jump
in to AI in action.

[30:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1859s) So as you think about the cloud journey,

[31:01](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1861s) keep in mind we didn't
just shut down a roadmap.

[31:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1865s) Like we can't do that.

[31:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1866s) We're a business, we have customer needs,

[31:08](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1868s) we have a space with GenAI
that is exploding right now.

[31:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1872s) And so we had to get after
a roadmap at the same time.

[31:15](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1875s) So we're literally doing
our cloud transformation

[31:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1877s) with our existing platform

[31:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1878s) and building new capabilities in parallel.

[31:20](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1880s) And so when you think about AI,

[31:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1882s) which for us is one of the biggest markets

[31:27](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1887s) we've seen open up in the last 20 years.

[31:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1890s) Real quick award here.

[31:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1892s) We have an application,
PatternBuilder MAX,

[31:35](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1895s) and this is pretty cool.

[31:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1897s) This is not a solicited media,

[31:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1899s) this is just someone that
went to a conference,

[31:41](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1901s) saw Scott Kelly who leads our AI group

[31:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1905s) demoing PatternBuilder MAX
and was just blown away by it.

[31:49](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1909s) And this is a to...

[31:50](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1910s) If you're in legal you
know, this is a tough space.

[31:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1913s) It's gotta be right, it's gotta work,

[31:55](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1915s) it's got to make the job easier

[31:57](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1917s) or else no one's ever going to adopt it.

[31:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1919s) And so just some really cool accolades,

[32:02](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1922s) best artificial intelligence for 2024,

[32:04](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1924s) which is a pretty big deal.

[32:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1926s) I think if you went to a legal
tech conference this year,

[32:09](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1929s) there's probably 600 legal
tech popups that have happened.

[32:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1932s) And so to win that award
was pretty awesome.

[32:15](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1935s) When you think about PatternBuilder MAX

[32:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1938s) and some of the value,

[32:20](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1940s) I'm gonna click through this real quick.

[32:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1944s) A couple things we can do.

[32:25](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1945s) We're plugged into an LLM.

[32:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1948s) I loved the comment yesterday with Matt,

[32:31](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1951s) how important choice was.

[32:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1952s) And so we're building models

[32:34](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1954s) and we're building applications,

[32:35](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1955s) but we're also allowing our customers

[32:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1957s) to bring their own models
and applications as well.

[32:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1959s) And so if you think
about PatternBuilder MAX,

[32:42](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1962s) it allows you as a user,
as a no-code solution

[32:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1965s) to build custom applications.

[32:46](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1966s) And so if you're a immigration firm

[32:49](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1969s) and you have 35 documents
that you have to do

[32:52](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1972s) for every single person
that's coming in for a visa

[32:55](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1975s) or an immigration application,
you can build an application

[32:58](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1978s) with PatternBuilder that'll
automate that form creation,

[33:01](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1981s) automate that form completion for you

[33:04](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1984s) and literally take what would
normally be several hours

[33:08](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1988s) if not a couple of days
down to 20 or 30 minutes.

[33:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1992s) You can actually auto
profile data now with us.

[33:15](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1995s) And so when you think
about the auto profiling,

[33:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=1998s) you have a document
and in the current day,

[33:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2002s) if you go backwards, documents
had very limited metadata.

[33:26](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2006s) Most of it was human generated.

[33:27](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2007s) And so the quality was generally
lacking or poor, very...

[33:31](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2011s) At least it was inconsistent
across the firm.

[33:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2013s) And so we're now leveraging LLMs

[33:35](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2015s) as well as some of our
vectorized data with Titan

[33:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2019s) and Symantec to auto
profile documents at scale.

[33:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2024s) Think about dropping a million documents

[33:46](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2026s) in the document management system

[33:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2027s) and you have a consistent taxonomy

[33:50](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2030s) that can literally update
hundreds of metadata fields

[33:54](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2034s) on every single document
within literally a few minutes.

[33:57](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2037s) And you have that consistency

[33:58](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2038s) that frankly legal professionals

[34:00](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2040s) have been looking for for decades.

[34:03](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2043s) Incredible value and
incredible time savings.

[34:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2046s) Doing this in the background as well.

[34:08](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2048s) And so up until about a month ago,

[34:11](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2051s) you could run an application,
you could select documents,

[34:13](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2053s) we can now run an application

[34:15](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2055s) against your entire corpus of data.

[34:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2057s) And so the days of
having to select 10 or 20

[34:19](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2059s) or 100 documents are moving away.

[34:21](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2061s) The customers, our customers'
expectations are changing.

[34:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2064s) We need to be able to run this at scale

[34:26](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2066s) across their entire corpus of documents.

[34:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2068s) And again, some of those customers,

[34:29](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2069s) that's a hundred million
documents or more.

[34:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2073s) I'm gonna give you an example here.

[34:34](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2074s) I glossed over redlining,

[34:36](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2076s) which is probably the coolest
thing we're doing right now.

[34:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2077s) So I shouldn't do that.

[34:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2079s) We are now getting to a place

[34:40](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2080s) where we are redlining
documents with generative AI.

[34:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2085s) And so when you think about
that, think of an attorney,

[34:49](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2089s) they have certain ways
of writing contracts

[34:52](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2092s) or writing summaries or briefs,
the AI can understand that.

[34:56](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2096s) It'll actually auto redline the documents,

[34:58](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2098s) something a legal assistant
would typically do,

[35:00](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2100s) send it back to the partner to review,

[35:03](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2103s) accept changes and
streamline that process.

[35:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2106s) You're talking about in some
cases two or three steps

[35:09](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2109s) of editing and redlining

[35:11](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2111s) that are being done
now with generative AI,

[35:13](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2113s) which is pretty incredible.

[35:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2116s) So I wanted to give you an example here,

[35:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2117s) just a quick screenshot.

[35:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2118s) Normally we demo this,

[35:20](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2120s) but I made a rule 20 years
ago to never do live demos.

[35:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2124s) So what you have here is a
typical old way, manual limited,

[35:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2128s) somewhat inaccurate, and
the new way you can see here

[35:31](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2131s) some of the examples of the metadata,

[35:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2133s) and this is a leasing contract.

[35:35](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2135s) And think about this in a firm.

[35:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2137s) You have these management companies

[35:40](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2140s) that will have thousands,

[35:41](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2141s) potentially tens of thousand of contracts.

[35:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2144s) They have rules, they have
compliance, they have parameters

[35:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2147s) like what's my out clause.

[35:49](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2149s) A lot of these companies
are acquiring contracts

[35:52](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2152s) through acquisition.

[35:54](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2154s) This simple auto-profiling capability

[35:56](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2156s) will allow someone to run
those contracts in bulk,

[36:00](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2160s) it'll flag exceptions within the contracts

[36:03](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2163s) that they need to have
an attorney look at.

[36:04](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2164s) So out of a hundred thousand contracts,

[36:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2166s) these 15 have a really,
really bad exit clause.

[36:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2170s) You need to go look at this
and potentially repaper.

[36:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2172s) Just a simple example
where this would take weeks

[36:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2176s) for a firm to dig through

[36:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2177s) that's happening in just a few minutes.

[36:20](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2180s) And then a streamlining risk.

[36:21](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2181s) It's actually reducing the risk
within the firm dramatically

[36:26](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2186s) by flagging and automating that process.

[36:31](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2191s) So at the end of the day,
the next big thing for us,

[36:34](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2194s) PatternBuilder MAX has been amazing.

[36:36](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2196s) We've got a lot of customers using it.

[36:38](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2198s) Where we see the kind of the sphere

[36:41](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2201s) tipping over a little
bit is the AI assistant,

[36:43](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2203s) this agent to agent conversation.

[36:46](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2206s) And Pallavi's gonna talk to the details

[36:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2208s) in which we need to get to.

[36:50](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2210s) For us, it's a simple front door.

[36:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2213s) There is a learning curve with AI

[36:56](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2216s) and what we found with our adoption

[36:58](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2218s) is the fast adopters are leaned in,

[37:01](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2221s) but there's a large segment of people

[37:02](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2222s) that are still a little nervous about AI.

[37:04](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2224s) And so we need that door to be wide open

[37:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2226s) and it needs to be a very
simple, wide open door.

[37:08](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2228s) Conversational threads
are what people like,

[37:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2230s) it's what they do.

[37:11](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2231s) They're used to doing that now,

[37:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2232s) it's a pretty common practice.

[37:13](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2233s) I joke two years ago, my wife
would've never used Siri.

[37:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2236s) And now she doesn't send a
text that's not Siri based.

[37:19](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2239s) And the world is getting
much more comfortable

[37:21](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2241s) with that conversational
based interaction.

[37:23](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2243s) And then safe and secure.

[37:25](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2245s) We have a saying in NetDocuments,

[37:27](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2247s) we're gonna bring AI to your documents,

[37:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2248s) we're not gonna push your documents to AI.

[37:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2250s) So keeping the AI services
within our platform

[37:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2253s) and contained within our
walls that we've built,

[37:35](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2255s) literally the most secure
walls you're gonna see

[37:38](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2258s) for a document management system.

[37:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2259s) We want the AI inside, not outside.

[37:41](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2261s) So it's a critical part of our strategy.

[37:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2264s) Okay, last thing.

[37:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2265s) I wanna give you a couple
examples of the legal AI assistant

[37:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2268s) and we have this in beta right now.

[37:50](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2270s) It's just getting out
the door. Ask a question.

[37:54](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2274s) Are there a key man provisions in the PSA?

[37:58](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2278s) What are the remedies on breach?

[38:00](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2280s) What are the non-compete

[38:01](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2281s) and non-solicit provisions
in the agreement?

[38:04](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2284s) Can you give me a timeline

[38:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2285s) of the facts presented in the documents?

[38:08](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2288s) We're doing this now at scale

[38:09](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2289s) and the results are incredible.

[38:11](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2291s) And the reason the results are incredible,

[38:14](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2294s) we're not just connected to an LLM

[38:15](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2295s) because you saw today
like the LLMs changed.

[38:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2298s) Every single week they're getting better.

[38:20](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2300s) It's like a foot race.

[38:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2302s) We did something very unique

[38:23](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2303s) and Pallavi's gonna walk you
through the technology here.

[38:26](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2306s) We're leveraging
vectorized data with Titan,

[38:29](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2309s) with Symantec data, with
Elastic, with the LLM services

[38:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2313s) as a kind of a trifecta
to analyze the documents

[38:36](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2316s) and provide responses back.

[38:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2317s) Very unique right now.

[38:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2319s) And the results and the
quality of the results

[38:42](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2322s) are through the roof.

[38:43](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2323s) It's allowing us to get to a
place where we can do redlining

[38:46](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2326s) with accuracy that lawyers will trust.

[38:49](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2329s) Last thing to say here,
October we launched,

[38:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2333s) we launched this in October of last year.

[38:55](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2335s) We have 6,000 apps that have
been created by our customers.

[38:58](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2338s) We're averaging 30 new apps
a week within our customers

[39:01](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2341s) and we're doing 6,000 sessions
a week on this platform.

[39:04](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2344s) So we're seeing rapid adoption

[39:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2345s) and if there's any question

[39:07](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2347s) of are our customers gonna
adopt generative AI in legal,

[39:09](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2349s) I think we've answered
the question in spades.

[39:11](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2351s) They're adopting and they're
adopting very, very quickly.

[39:15](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2355s) All right, Pallavi, I
went long, I apologize

[39:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2357s) so I hope we give you enough time.

[39:20](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2360s) - Thank you very much, John.

[39:21](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2361s) Actually that was a fantastic journey

[39:23](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2363s) of your cloud journey migrating to AWS

[39:27](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2367s) as well as innovations in the
document management space.

[39:31](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2371s) So Olta and John covered a lot

[39:34](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2374s) about challenges in the
legal industry and how the...

[39:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2379s) Especially within the legal industry,

[39:42](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2382s) the documents or unstructured
data is the core object.

[39:46](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2386s) And we saw the challenges

[39:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2388s) that these are in massive amount of scale.

[39:51](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2391s) I was actually zapped by the scale,

[39:52](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2392s) it's billions of documents in a year

[39:54](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2394s) that we are talking about.

[39:56](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2396s) So imagine searching
through such document scale

[40:00](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2400s) and bringing that as a
forefront to the user

[40:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2405s) so that they can converse
naturally with those documents

[40:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2410s) as well as how honoring
the security permissions

[40:14](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2414s) because that's going
to be super important.

[40:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2416s) So this is where we are
seeing a lot of use cases

[40:19](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2419s) that are being asked by our customers

[40:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2422s) and we broadly categorize
those into three categories.

[40:25](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2425s) The first one is summarization

[40:27](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2427s) and shortly, I mean, John
talked about the legal assistant

[40:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2430s) and there was...

[40:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2432s) You can summarize contracts

[40:34](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2434s) where you need to understand
what are the agreements

[40:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2437s) and where are the risk areas
that are associated with it

[40:41](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2441s) or generating case
summary is very critical

[40:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2444s) in the legal research field.

[40:46](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2446s) So summarizing the document,

[40:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2447s) having generative AI summarize
that document for you

[40:51](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2451s) and make it accessible to your users

[40:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2453s) saves a lot of amount of time
for the legal professionals.

[40:56](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2456s) So the key here is optimizing
your legal processes

[41:00](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2460s) and then improving legal
professional's capability.

[41:04](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2464s) We talked about legal
AI assistant a slide ago

[41:08](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2468s) where idea is you have these
massive amount of documents,

[41:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2472s) you make them searchable

[41:13](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2473s) and when you are at that scale,
just writing semantic search

[41:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2478s) and making those accessible
is a huge amount of task.

[41:20](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2480s) And that is where we are using

[41:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2482s) the generative AI advancements.

[41:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2484s) And it's not just searching
through the documents

[41:27](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2487s) but it is conversing
in a natural like flow.

[41:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2490s) So the idea here is to
turn matter management

[41:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2493s) into knowledge management,

[41:34](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2494s) you need to be able to get good handle

[41:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2497s) on the amount of unstructured
data or matters that you have

[41:41](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2501s) and make that categorized,
well organized and searchable.

[41:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2505s) The third use case broad category

[41:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2508s) that we see is the text generation.

[41:50](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2510s) And you would have seen
this is mainly about

[41:52](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2512s) if you have standardized templates

[41:54](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2514s) you can draft standardized
contracts or even RFI processes.

[41:58](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2518s) The goal here is to remove

[42:00](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2520s) that undifferentiated
heavy lifting and prepare

[42:04](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2524s) or automate the workflows

[42:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2525s) in such a way that you are able to create

[42:08](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2528s) the draft versions of documents.

[42:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2530s) Now, remember one thing we
will be very cautious here

[42:13](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2533s) or one thing we follow the
principle for legal professionals

[42:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2536s) is your documents need to be A,

[42:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2538s) first of all honor all the permissions,

[42:21](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2541s) it needs to follow the permissions

[42:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2542s) that you are allowed to within the data.

[42:25](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2545s) The context accuracy
is extremely important.

[42:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2548s) They are very context aware documents

[42:31](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2551s) and again we are giving
you the draft documents

[42:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2553s) so that the legal professionals
can use their expertise,

[42:36](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2556s) review the document

[42:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2557s) and provide the final
human in the loop picture.

[42:41](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2561s) So we did talk a lot about
generative AI and LLMs

[42:46](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2566s) and foundation models,

[42:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2567s) but let's put that into
perspective just real quickly here.

[42:51](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2571s) So generative AI again is a
subset of deep learning model

[42:56](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2576s) where you are using
large pre-trained models,

[43:00](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2580s) which are foundation models to
create new content or ideas.

[43:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2585s) And large language models, LLMs

[43:08](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2588s) that we kept referring to are subset of

[43:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2592s) or the specific foundation models

[43:13](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2593s) that cater towards text
generation or text related task.

[43:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2598s) Now, a quick poll to the audience.

[43:21](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2601s) How many of you

[43:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2602s) are building generative
AI applications today?

[43:26](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2606s) Okay, I see quite a few hand raised.

[43:29](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2609s) How many of you are training your users

[43:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2612s) to write better prompts?

[43:35](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2615s) Okay, all right, so we all know

[43:38](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2618s) that we cannot use the foundation models

[43:40](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2620s) and the large language models as is,

[43:42](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2622s) they need to be customized.

[43:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2624s) And this is where you're familiar

[43:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2627s) with these four different steps.

[43:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2628s) I'm just going to quickly
walk through them.

[43:50](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2630s) So you start always with
the prompt engineering

[43:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2633s) where you specify specific instructions

[43:56](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2636s) on how to tailor the output
of the foundation model

[43:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2639s) for your needs.

[44:01](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2641s) The second one is the
retrieval augmented generation,

[44:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2645s) where the key here is
to identify the right

[44:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2650s) or relevant context from
large corpus of data.

[44:13](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2653s) And it's not just one data source.

[44:15](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2655s) You may have multiple data sources.

[44:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2657s) So you wanna get the right context

[44:20](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2660s) from those large corpus of data
and then augment your prompt

[44:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2664s) with the relevant information.

[44:26](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2666s) However, sometimes what
happens is RAG architecture

[44:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2670s) is not enough.

[44:31](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2671s) Sometimes you don't get
the model performance

[44:34](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2674s) that you're looking for,
either it could suffer,

[44:36](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2676s) it may not meet the accuracy
needs of your use case

[44:41](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2681s) or it could be related to latency or both.

[44:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2684s) In those cases, we have seen our customers

[44:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2687s) take small amount of data

[44:49](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2689s) and adjust the foundation models weights

[44:52](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2692s) in such a way that you
are creating a model

[44:57](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2697s) with specialized task,

[44:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2699s) but again retaining the underlying
generative capabilities.

[45:03](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2703s) So that's where you would fine tune

[45:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2705s) or pre-train the underlying
foundation model.

[45:09](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2709s) There are certain cases where
that is also not enough.

[45:13](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2713s) It's either the foundation
model has biases

[45:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2716s) that doesn't work for your use case

[45:19](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2719s) or you have large amount of private data

[45:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2722s) that is not being seen

[45:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2724s) by these models when
they were being trained.

[45:26](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2726s) And in those cases

[45:27](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2727s) you would go for training
the model from scratch.

[45:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2730s) Now remember, as you are
going through all these steps,

[45:34](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2734s) the time, cost and complexity increases,

[45:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2739s) but it also increases the accuracy.

[45:41](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2741s) So we encourage you to look
at what your use cases,

[45:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2745s) evaluate the different steps,

[45:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2747s) and then use the right methodology

[45:50](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2750s) to customize the foundation model.

[45:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2753s) So let's take a look at
the generative AI stack

[45:57](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2757s) and Olta talked about it at length

[45:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2759s) that we do have the generative AI stack

[46:02](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2762s) that's divided into three macro layers

[46:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2765s) and there is infrastructure layer

[46:07](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2767s) where Olta went into details
about Tranium and Inferentia,

[46:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2770s) and you saw the announcements
that came in yesterday

[46:13](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2773s) with Matt and Amazon SageMaker.

[46:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2776s) So Amazon SageMaker

[46:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2777s) is actually in the
infrastructure layer here

[46:20](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2780s) because just having the
right chip set is good thing,

[46:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2782s) but you need to have
additional capabilities

[46:25](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2785s) such as distributed training,

[46:26](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2786s) automated model tuning, et cetera.

[46:29](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2789s) So this is where Amazon SageMaker,

[46:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2790s) which is our managed
service to build, train,

[46:34](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2794s) and deploy models at
scale, has these features

[46:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2797s) such as distributed training

[46:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2799s) where it can handle large amount of data

[46:41](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2801s) and then give you options to
flexibily deploy these models

[46:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2805s) as well as responsible
AI features and ML ops.

[46:51](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2811s) So we did talk about if...

[46:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2813s) But majority of our
customers do wanna build

[46:56](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2816s) with existing foundation models

[46:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2819s) and that's where Amazon
Bedrock comes into picture.

[47:02](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2822s) Now, Amazon Bedrock, Olta
went into detail about this.

[47:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2826s) It's our managed service
where you do get a choice

[47:09](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2829s) of large foundation...

[47:11](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2831s) Selection of foundation
models to choose from.

[47:13](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2833s) And these are foundation models
from leading model providers

[47:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2836s) as well as there are features

[47:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2838s) that can help you build your
generative AI application.

[47:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2844s) And then on top is the applications

[47:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2848s) that leverage the LLMs or FMs,

[47:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2850s) which means these applications
are completely built for you.

[47:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2853s) Sometimes it may happen

[47:35](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2855s) that you may not have
the specialized skills

[47:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2857s) to build the generative AI applications

[47:41](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2861s) or it could be that you just wanna explore

[47:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2864s) the dataset real quickly.

[47:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2865s) There is a new data source,

[47:46](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2866s) you wanna see what the
data source looks like.

[47:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2868s) Instead of building a
generative AI application,

[47:49](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2869s) you can use what is already built in.

[47:52](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2872s) So this is where Amazon
Q comes into picture.

[47:55](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2875s) It can help you get that access

[47:57](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2877s) to the enterprise data, again,

[47:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2879s) with the right level of permission.

[48:01](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2881s) And that is where Amazon Q
security comes into picture.

[48:04](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2884s) So Amazon Q security,

[48:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2886s) the way it is built is if user

[48:09](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2889s) doesn't have access to data outside of Q,

[48:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2892s) the user will not have access
to the data inside of Q

[48:15](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2895s) and that's already built in.

[48:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2897s) So you integrate with your data sources

[48:19](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2899s) and get started with Amazon Q.

[48:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2902s) Again, Amazon Q helps you
interact with your enterprise data

[48:27](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2907s) as well as generate code,
create generative dashboards.

[48:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2912s) So there are a lot of
features that Amazon Q offers.

[48:36](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2916s) So let's take a look at our architectures.

[48:40](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2920s) I mean we are going to talk
about few architecture patterns,

[48:42](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2922s) but before that I wanna quickly highlight

[48:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2924s) the Bedrock features that we will be using

[48:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2927s) to go through those architectures.

[48:50](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2930s) So one of the core
principles that we believe in

[48:54](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2934s) is to give our customers...

[48:56](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2936s) Our core value is mainly
to give you model choice,

[49:00](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2940s) data privacy and customization.

[49:04](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2944s) So from model choice perspective,

[49:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2946s) John touched upon this
a little bit earlier

[49:08](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2948s) that it's a race.

[49:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2950s) There's new models that are
always coming into picture

[49:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2952s) and no one model fits all use cases.

[49:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2956s) So we want our customers to have a choice.

[49:19](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2959s) So using Amazon Bedrock, you have a choice

[49:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2962s) to select from the leading
foundation model providers

[49:26](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2966s) such as Athropic, we have
Meta, we have Cohere,

[49:29](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2969s) and this slide is already outdated

[49:31](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2971s) because we have announced
our own model yesterday

[49:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2973s) that Nova came into picture.

[49:35](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2975s) So this is where...

[49:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2977s) I mean it is like it's just a day old

[49:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2979s) and my slide is already outdated.

[49:41](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2981s) So this is what the fast innovation

[49:43](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2983s) that is happening in this space.

[49:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2985s) So we want you to have the
access to the right model

[49:49](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2989s) that meets your cost, security
and latency requirement.

[49:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2993s) This is going to be the key

[49:55](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2995s) when you wanna choose a foundation
model that works for you.

[49:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=2999s) Think about the accuracy requirement,

[50:02](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3002s) think about how much
it's going to cost you

[50:04](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3004s) and think about the security practices.

[50:08](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3008s) Having a choice of model is
great, but what about security?

[50:11](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3011s) And that's the common question.

[50:13](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3013s) That's the first question
we always get asked.

[50:14](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3014s) So first thing is,
first, none of your data

[50:19](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3019s) will be used by any of
this foundation model

[50:23](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3023s) to better their models.

[50:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3024s) So that's the first thing.

[50:25](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3025s) Bedrock is built on
this security principle.

[50:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3028s) Other thing that of
course the data that...

[50:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3030s) Just like any other services,

[50:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3032s) the data is encrypted in transit

[50:34](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3034s) and at rest as well as it
does have the permissions,

[50:38](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3038s) the right set of permissions

[50:40](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3040s) that you have with
other AWS services also.

[50:43](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3043s) So there's a specific
control that you can define

[50:46](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3046s) on what features are accessible.

[50:50](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3050s) Responsible AI, we cannot move forward

[50:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3053s) without talking about responsible AI.

[50:54](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3054s) So definitely wanna talk
about Amazon Guardrails,

[50:57](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3057s) Bedrock Guardrails.

[50:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3059s) Now Bedrock Guardrails provide
you additional safe guards

[51:02](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3062s) that are built on top of the
foundation model providers.

[51:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3066s) So using short natural description,

[51:09](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3069s) it helps you define certain
topics that should be avoided

[51:15](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3075s) by your generative AI application.

[51:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3078s) And then you can also, the
guardrails also help you detect

[51:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3082s) and block user inputs and
foundation model responses

[51:27](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3087s) that fall into those specific topics.

[51:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3090s) The other thing I wanna highlight,

[51:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3092s) I mean you can also define...

[51:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3093s) You can also control thresholds

[51:35](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3095s) where you're protecting
against the harmful content,

[51:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3099s) jailbreak or the prompt ingestion attack.

[51:42](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3102s) The other thing I wanna
highlight is the guardrails.

[51:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3104s) You define them once and
then they are model agnostic.

[51:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3107s) That means you can really configure it

[51:49](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3109s) with any model which is
offered within Bedrock.

[51:52](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3112s) And again, Bedrock
offers number of features

[51:56](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3116s) and those are the guardrail integration

[51:58](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3118s) is native to those features.

[52:01](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3121s) So we are going to go through
reference architectures

[52:03](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3123s) for a couple of use cases

[52:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3125s) and how we build using Bedrock features.

[52:09](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3129s) But the first important point

[52:11](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3131s) that I wanna talk about is RAG in action.

[52:13](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3133s) And how many of you are
building applications

[52:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3137s) with RAG architecture?

[52:21](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3141s) Okay, so let's jump through
a little bit of details.

[52:25](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3145s) So RAG typically has two workflows.

[52:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3148s) A lot of times I hear complaints
from my customers that,

[52:31](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3151s) well, the RAG is...

[52:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3153s) Our documents are not coming out well,

[52:35](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3155s) there's some accuracy issues, et cetera.

[52:38](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3158s) So I highly recommend the customers

[52:40](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3160s) looking at their data
ingestion workflow closely.

[52:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3164s) Well, let's take a look at that.

[52:46](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3166s) So we talked about earlier,

[52:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3168s) there are large number of
documents and the goal here

[52:51](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3171s) is to make those documents
available via Symantec search.

[52:55](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3175s) In those cases,

[52:57](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3177s) when you wanna make
such documents available

[52:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3179s) via Symantec search, there
are certain processes

[53:01](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3181s) or decision points that are involved.

[53:04](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3184s) The first thing you would do

[53:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3185s) is you wanna put these documents
in a vectorized database.

[53:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3190s) Now you cannot put that entire document

[53:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3192s) which is 500 pages sometimes,

[53:14](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3194s) it cannot go in the
vectorized database as is.

[53:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3198s) So it has to be chunked,

[53:20](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3200s) which means there is specific paragraphs,

[53:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3202s) a specific text that
is going to be chunked

[53:26](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3206s) and that's how it is
going to be then embedded

[53:29](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3209s) into a vector representation
and goes into the vector store.

[53:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3213s) So there are document chunking.

[53:36](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3216s) Choosing the right embedding model

[53:38](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3218s) and choosing the right vector store

[53:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3219s) for your use case are going
to be the key decision points

[53:43](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3223s) that you have to make.

[53:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3225s) And this is where I have
seen majority of the times

[53:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3228s) that document accuracy suffers

[53:51](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3231s) When you are building
the RAG architectures.

[53:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3233s) In the legal space, the documents
that are going to come in,

[53:57](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3237s) they're going to come in various formats.

[53:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3239s) They are going to be PDFs,
they are going to be Words,

[54:01](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3241s) they are going to be text
files or PDFs, scan PDFs.

[54:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3245s) They're not laid out well.

[54:07](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3247s) So this is where understanding
how those documents

[54:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3250s) needs to be chunked and vectorized

[54:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3252s) is going to be a key activity.

[54:14](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3254s) And let's say I'm a user

[54:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3256s) who wants to search
through specific contract

[54:19](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3259s) and understand whereby if I
have a NDA with organization A.

[54:25](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3265s) When that query comes in from a user,

[54:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3268s) and this is where the text
generation flow happens,

[54:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3270s) this is where the embedding model

[54:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3272s) is going to translate that query
into vector representation,

[54:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3277s) which then searches
through the vector database

[54:40](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3280s) and generates context out of it.

[54:42](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3282s) And that context is provided
along with the prompt

[54:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3285s) that you will write to get the...

[54:49](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3289s) Will get passed on to
a large language model

[54:51](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3291s) and then you get your output.

[54:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3293s) That sounds very cumbersome, right?

[54:55](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3295s) There are a lot of things

[54:56](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3296s) that you have to worry about chunking

[54:58](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3298s) and moving the documents, et cetera.

[54:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3299s) Well, that is where Amazon
Bedrock knowledge bases

[55:03](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3303s) come into picture.

[55:04](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3304s) Knowledge bases gives you that...

[55:07](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3307s) It removes that
undifferentiated heavy lifting

[55:09](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3309s) and gives you the choice

[55:11](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3311s) to choose the right embedding model,

[55:13](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3313s) choose the right chunking strategy,

[55:15](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3315s) it is natively integrated with
the choice of vector stores.

[55:19](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3319s) And then you can spin up
your manage RAG architecture

[55:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3324s) to understand your document workflows.

[55:27](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3327s) The important aspect
about why knowledge basis

[55:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3330s) is the improved accuracy.

[55:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3332s) And this is core, this
is a core architecture

[55:35](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3335s) and core point to any time

[55:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3337s) you wanna build semantic
search related capabilities

[55:41](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3341s) or you wanna understand,
analyze the large documents.

[55:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3344s) Understanding how well
your documents are chunked

[55:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3348s) is important and that
is why knowledge bases

[55:50](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3350s) offers you different...

[55:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3353s) It offers you a control
over your chunking strategy

[55:57](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3357s) such as hierarchical chunking.

[55:58](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3358s) If a document has
parent-child relationship,

[56:01](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3361s) it will automatically group the chunk,

[56:03](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3363s) the document together

[56:04](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3364s) in such a way that that
hierarchy is maintained.

[56:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3366s) So when you are searching
through that document,

[56:08](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3368s) the document accuracy improves

[56:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3370s) because you have that
hierarchy maintained.

[56:14](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3374s) Similar to semantic search,

[56:15](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3375s) especially in the legal documents,

[56:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3377s) semantic chunking capability
is extremely important

[56:21](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3381s) because the document has related text

[56:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3384s) scattered throughout the document.

[56:26](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3386s) So the idea here would
be grouping that text

[56:29](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3389s) and then storing that
in the specific chunk.

[56:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3393s) Now, there are a lot of features

[56:35](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3395s) that knowledge bases offer

[56:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3399s) in terms of improving our accuracy,

[56:41](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3401s) which I cannot go in
the next three minutes,

[56:43](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3403s) but there is a session
that I will have it listed

[56:46](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3406s) that tomorrow is happening,

[56:47](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3407s) which goes through the deep
dive into knowledge bases

[56:51](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3411s) and how to improve accuracy.

[56:52](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3412s) I would highly recommend you attend that.

[56:55](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3415s) So let's take a look

[56:56](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3416s) at a couple of architectures real quick.

[56:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3419s) So our architecture with
respect to a contract

[57:01](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3421s) and tech process is
something that pretty much

[57:03](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3423s) all organizations have,
whether it's a legal

[57:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3426s) or whether you are an enterprise
who has a legal department.

[57:09](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3429s) So let's put what we
learned, which is creating...

[57:14](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3434s) I mean when you have matters,
turning the matter management

[57:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3437s) or contract management into
a knowledge management.

[57:19](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3439s) So let's put those learnings into practice

[57:25](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3445s) where we have taken the executed contracts

[57:29](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3449s) and then we are not only
doing the executed contracts,

[57:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3452s) but we are extracting the metadata

[57:34](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3454s) and attaching that metadata
to the vector store.

[57:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3459s) This will help when you
have millions of documents

[57:42](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3462s) and you need to understand that
when I retrieve my documents

[57:46](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3466s) from Symantec search perspective,

[57:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3468s) I have it filtered based
on what I'm asking.

[57:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3473s) So this becomes a key that
these are the features

[57:55](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3475s) that the knowledge base will support.

[57:57](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3477s) So I have taken the list
of executed contracts,

[58:01](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3481s) I have added them, extracted the metadata,

[58:05](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3485s) attached that metadata to vector databases

[58:07](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3487s) and created a knowledge base.

[58:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3490s) So when a user like me who comes in

[58:13](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3493s) and I ask, I need NDA with org A,

[58:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3497s) let's say there is a
conversational user interface.

[58:20](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3500s) Now you just heard Dr. Swamy Subramanian

[58:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3502s) announce agent tech interfaces,
there are multiple...

[58:26](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3506s) There is prompt,

[58:29](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3509s) there is a model routing,
prompt caching, et cetera.

[58:31](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3511s) A lot of beautiful features have come in.

[58:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3513s) So using that,

[58:34](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3514s) you can build a conversational interface

[58:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3517s) which is going to take that query,

[58:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3519s) understand what the ask is,

[58:41](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3521s) extract the specific
metadata that this is NDA

[58:43](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3523s) and the party is organization A

[58:46](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3526s) is going to search through
the knowledge base,

[58:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3528s) build the right results and
send the final response.

[58:51](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3531s) Now, in my case I'm saying
that well, there is no NDA

[58:56](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3536s) with org A, do you wanna create one?

[58:59](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3539s) And this is where you can use
a conversational assistant

[59:03](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3543s) where we haven't created
a rules based system.

[59:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3546s) There is no if else happening here.

[59:09](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3549s) The knowledge base or the agentic approach

[59:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3552s) understands from the
existing executed contracts

[59:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3556s) and it learns from the standard template.

[59:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3558s) And also it's in own inherent knowledge

[59:21](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3561s) about how contracts work
or different contracts

[59:23](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3563s) is going to ask specific questions

[59:25](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3565s) and get those draft contract created

[59:29](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3569s) for a legal professional to review.

[59:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3572s) Similarly, text generation RFI process,

[59:35](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3575s) I hear there are multiple
weeks that are gone in.

[59:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3579s) And this is where, again, you create

[59:41](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3581s) and execute historical
RFI contracts, search,

[59:46](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3586s) create a knowledge base
and search through them.

[59:48](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3588s) And this process,

[59:50](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3590s) actually the screenshot
that you're seeing,

[59:52](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3592s) we have implemented this RFI process.

[59:54](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3594s) It does save from weeks
to days of creating,

[59:58](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3598s) generating a new RFI from
previously executed RFIs,

[01:00:03](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3603s) improving the productivity of employees.

[01:00:07](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3607s) Now, similarly, if you have a quick way,

[01:00:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3610s) similarly if you have, let's say...

[01:00:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3612s) We talked a lot about documents,

[01:00:14](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3614s) but let's say you have videos and images.

[01:00:16](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3616s) In those cases, you can
also make those accessible.

[01:00:20](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3620s) For example, you have a lot of videos

[01:00:21](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3621s) where there's testimony.

[01:00:23](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3623s) In those cases, using our AI service,

[01:00:27](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3627s) which is Amazon Transcribed,

[01:00:28](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3628s) you can transcribe the
text, put that into S3

[01:00:33](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3633s) and simply put it to
Amazon Q for business,

[01:00:36](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3636s) which is going to then
make that accessible.

[01:00:38](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3638s) And then you can quickly start looking

[01:00:40](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3640s) through asking questions such as

[01:00:42](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3642s) who testified and what was there?

[01:00:44](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3644s) Can you summarize this testimony?

[01:00:46](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3646s) Again, maintaining who has
access to what that is core

[01:00:50](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3650s) and a very important conversation.

[01:00:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3653s) So having said that, in
closing, just a quick takeaways.

[01:00:57](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3657s) So we learned from NetDocuments
about their journey

[01:01:03](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3663s) and how they're bringing user efficiency

[01:01:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3666s) and what their roadmap is to build more.

[01:01:10](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3670s) So I want you to think about
the top three use cases

[01:01:14](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3674s) and situations that can
improve your business process

[01:01:18](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3678s) or workflows and what
brings the most value

[01:01:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3682s) in generative AI use cases.

[01:01:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3684s) What's the ROI associated
with those use cases?

[01:01:27](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3687s) So as a final ask, I want you
to leverage the AWS community

[01:01:32](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3692s) and start working on those,

[01:01:34](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3694s) you have a access to maybe account access,

[01:01:37](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3697s) you're working with the partners,

[01:01:39](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3699s) or if you're not clear
about the mechanisms,

[01:01:40](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3700s) please reach out to us.

[01:01:42](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3702s) We can help you put in
the right direction.

[01:01:45](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3705s) But this space, as John
earlier said, it is expanding.

[01:01:49](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3709s) It is for you to remain
viable and competitive.

[01:01:53](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3713s) This is going to be an important
task that you have to do,

[01:01:55](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3715s) is you have to adopt.

[01:01:57](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3717s) You wanna adopt generative
AI, improve efficiencies,

[01:02:01](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3721s) optimize your workflows,
build automated workflows,

[01:02:06](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3726s) and take advantage of it.

[01:02:09](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3729s) That's it for now from me.
Here are the upcoming sessions.

[01:02:12](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3732s) If you wanna take a picture of it.

[01:02:13](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3733s) AIM305 is where you can go learn more

[01:02:17](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3737s) about the RAG architectures and
how to improve the accuracy.

[01:02:22](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3742s) Thank you very much for
staying with us today

[01:02:24](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3744s) and please complete the survey.

[01:02:27](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3747s) Your feedback is important
so we can improve.

[01:02:30](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3750s) Thank you very much.

[01:02:31](https://www.youtube.com/watch?v=i7E2LHcQtlU&t=3751s) (audience applauding)

