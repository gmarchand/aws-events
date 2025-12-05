# AWS re:Invent 2021 - Confluent at the edge on AWS (sponsored by Confluent)

[Video Link](https://www.youtube.com/watch?v=l7fH9FWvz_8)

## Description

In this session, learn about an architecture that uses Confluent technology and AWS edge services, such as AWS Outposts, AWS Wavelength, AWS Local Zones, and AWS Snowball, to run data-in-motion and event-based applications at the edge easier and faster. Confluent for Kubernetes is a tool that makes deploying Confluent to multiple Kubernetes systems at the edge extremely manageable. Discover how to use Cluster Linking, Confluent’s latest replication technology, between Confluent clusters at the edge and Confluent Cloud clusters in AWS Regions, unlocking numerous possibilities downstream with other AWS or ISV services. This presentation is brought to you by Confluent, an AWS Partner. Speakers: Joseph Morais (Confluent) and Justin Lee (Confluent))

Learn more about re:Invent 2021 at https://bit.ly/3IvOLtK

Subscribe: 
More AWS videos http://bit.ly/2O3zS75 
More AWS events videos http://bit.ly/316g9t4

ABOUT AWS
Amazon Web Services (AWS) hosts events, both online and in-person, bringing the cloud computing community together to connect, collaborate, and learn from AWS experts.

AWS is the world’s most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally. Millions of customers—including the fastest-growing startups, largest enterprises, and leading government agencies—are using AWS to lower costs, become more agile, and innovate faster.

#AWS #AmazonWebServices #CloudComputing

## Transcript

All right. Hi, everyone. Welcome to Confluent at the edge on AWS. So we're thrilled to have you in this session today. I know there are many different ways to spend your time at re:Invent and I just wanted to acknowledge how grateful we are to have you here with us. I'm Joseph Morais, Staff Cloud Partner and Solutions Architect at Confluent, and joining me today is Justin Lee, one of our outstanding Staff Solution Engineers. How's it going? Nice to meet everybody. Good to be here. We're gonna discuss data in motion at the edge. There'll be some joy, plenty of insight, and hopefully some fun. So just a quick summary of what we're gonna be diving into today. First, we'll do a quick dive into what Apache Kafka is and the rise of data in motion. We'll then discuss who is Confluent and how do we relate to Kafka. What do we mean by edge and common challenges in these architecture patterns? Then we will explore AWS and Confluent technologies that make working at the edge easier. We'll close today with a discussion of some common edge use cases, a live demonstration of data in motion, and if time permits some Q&A. Buckle up. So at its core, Apache Kafka is a scalable, highly available, event streaming platform, which you can think of as the central nervous system of an enterprise. Kafka also makes it easier to get more value out of your existing systems and to make them real time, so to speak. And I say real time, so to speak, because it depends on your definition of real time. Kafka, we're talking 20 to 30 milliseconds. Some people have those absolute zero millisecond use cases, not exactly a Kafka fit. We now like to focus on a new paradigm, called data in motion, which is centered around event streams and streaming analytics and processing. Here, data is not static and at rest, but continuously evolving and continuously being processed and analyzed in real time. In today's world, the fundamental notion is that data is moving, not sitting at rest. We'll show an example of this in our demo later today. Event streaming or data in motion was first developed at LinkedIn by the founders of Confluent. As we all can see the very best open source technologies make their way from Silicon Valley into the enterprise. And as of today, over 70% of fortune 500 companies use Apache Kafka, the majority of which are Confluent customers. Let's quickly discuss what we see happening around us every day, which is that data is changing the world. Whether through our interactions with mobile applications, seeing real-time metrics from recent SpaceX launches, seeing maintenance workers with tablets or witnessing our doctors working with our digital medical records, our interactions with the world are immersed with data. Data is helping the world build rich front-end customer experiences. And this is important because even if your business has nothing in common with a company like Netflix, this is the type of experience that your customers expect in all aspects of their lives. Data's helping companies move towards realtime backend operations. Amazon warehouses are a great example of how they've driven efficiency and speed through harnessing data. Confluent has the technology, experience and support to make these types of outcomes possible for any organization, anywhere in the world. Let's talk a bit more about Apache Kafka, the open source project that Confluent is built on top off. Outside of the code, Kafka is also about the community. These numbers really speak for themselves. The community loves Kafka and Kafka loves them right back. For the non-Kafka nerds in the audience, us too, a KIP is a Kafka improvement proposal, which is used to submit propositions for major changes to open-source Kafka. The strength of Kafka is not only its completeness as a streaming platform, but the ecosystem around it. Kafka is not an island. Fun fact, there are 1,000, that's right, that's 1-0-0-0 more lines of code for integrations to Kafka than lines of code for Kafka itself. And Kafka is no small project. So how does Confluent fit into all this? As I mentioned earlier, the founders of Confluent, are the original creators of Apache Kafka. And the team here at Confluent has over one million hours of contributing to the Kafka open source code basic managing Kafka clusters at the largest scale. At this time, we have over 5,000 clusters running in Confluent Cloud. Our platform extends Apache Kafka, to be a secure enterprise-ready platform. And we help enterprises all around the world successfully to play Kafka at scale and accelerate their time to market. Because of our success, our customers have achieved, we've won several important awards, including Forbes 100 Best Cloud Companies, Morgan Stanley's CTO Innovation Award, being inducted into JPMorgan Chase's Hall of Innovation and Bank of America's Enterprise Innovation Award. The largest, most innovative organizations in the world are partnering with Confluent, recognizing us as a key element of their success. For those of you who are familiar with Apache Kafka, I just wanted to quickly call out some differentiators. We'll be discussing most of these in further in detail later in the discussion, but I just wanted to prime all of you. We have a set of 130 plus prebuilt connectors to help you easily connect to our different data sources and sync. We enable you to elastically scale saving significant costs by avoiding manual scaling and provision. We offer an event streaming database, ksqlDB, which is the easiest way to build stream processing applications. We have a set of security functionality to ensure enterprise grade security. And last, we have a set of functionality that enables you to increase your operational efficiency while keeping costs low. Excuse me while I catch my breath. So verbose. Before we get into our discussion of the edge, I would like to discuss another important differentiator that deserves its own it's own slide, and it's really kind of the basis of our demo today. And it's that Confluent empowers you to run everywhere, and I do mean everywhere, from a Raspberry PI to a monster bare metal machine, Confluent works. Our customers can choose between a fully managed cloud product in AWS and a software product they can run themselves in their own data centers or VPCs. And of course you can use both. You can interconnect these into a global, central nervous system for data in motion. And this is becoming a critical component of the cloud migration strategy of many of our largest customers, because it allows their new applications to connect their input and output data back into existing legacy systems without requiring a big migration all at once. Both Confluent Cloud and Confluent Platform are subscription services where the spend scales with usage. So you're only paying for what you use. I think a lot of people think of a journey to the cloud as lifting and shifting VMs or instances. That just kind of takes your debt from your on-prem into the cloud, your tech debt. So by replicating your data from on-prem into the cloud, you can build out brand new applications with that replicated data set. And then once you're satisfied with your new applications, you can point your on-prem sources to the cloud. I see customers do it all the time. So what is the edge or edge computing? Wikipedia says, everyone starts a Wikipedia's definition, right, Wikipedia says, "Edge computing is a distributed computing paradigm that brings computation and data storage closer to the location where it is needed to improve response times and save bandwidth." From a practical perspective, edge is really the closest you can get to your workload. That might mean an end user interacting with a mobile application or a weather measurement station in a remote area with no network connectivity. The edge might also be a combination of these use cases. Consider a travel platform which will have events for mobile devices, events from the food inventory systems, updates to travel information manifest and loyalty systems. Even at the edge, having all this data in a single place or system has tremendous potential for enhanced customer experiences. Let's discuss the first of three common edge patterns. The first pattern is remote location, which takes very different forms depending on your type of business. For a retail company, this may include warehouses, storefronts, kiosks, pop-up shops. For a service oriented business, this may include offices around the world, right, your remote locations. For logistics, it may include truck depots, maintenance shops and regional offices. The next pattern is partially disconnected edge. This is a situation where the network connectivity is limited or time bound. Think of a train entering a tunnel that relies on satellite communication. And for the duration of that tunnel, connectivity to the rest of the world is separate. Often with these patterns, we see mechanisms in place to synchronize data once network connectivity is restored. The final pattern we'll be focusing on will be the focus of our demonstration later today, it's a new type of edge battery. MEC or multi-access edge computing allows you to provide computational resources over telco or carrier networks, allowing you to serve as many devices using the same infrastructure securely and with low latency. There are also private mix scenarios. We saw that announced yesterday, where 4G, 5G connectivity and edge computing resources can be provided to a specific customer and location where cell phone towers may not even exist today. So the edge is really cool. It allows you to unlock new experiences for customers, gain insight from data points never previously available, or at least not in a timely fashion or aggregate data from across the globe. The problem is that edge is difficult. The first thing maybe the most important challenge is that of limited resources at the edge. Likely the first thing that jumps to mind is budget, which is certainly part of the issue, but not the only limiting factor. At the edge, we often have little or no technical hands on staff. In a retail scenario, this often means asking a retail associate to physically access equipment. I've been there before. At a remote monitoring station, there may be no one on site for days, weeks, or even months at a time. Change operations at the edge can feel perilous due to the aforementioned limited budgets and lack of handling support, often roll-outs upgrades or changes at the edge can be overwhelming. Outages in any form in today's world, generally result in a loss of confidence to end users of those systems, whether they're internal or external to the organization. Our second challenge is with device integration. Consider just a single department in a hospital. There are devices which with different connectivity types, operating systems, manufacturers, et cetera, getting these device voices to communicate with a single messaging backbone can be very difficult. In this example, we're only looking at one department. Imagine the number of data points across the entire hospital, a network of hospitals, et cetera, Amazon AWS has this concept of well-architected framework, which distills what Amazon and AWS have learned over years of building robust, scalable systems. One of the tenets of well architected is to loosely couple your applications, which means not having one thing talk to another directly because that is brittle and does not scale well. Instead, have something in the middle that scales really well and is highly available. Later in the presentation, we'll go over some of the technologies that Confluent has layered on top of edge Kafka which by design is highly available and scalable. Think about how these features can help you build a global network of loosely coupled data consumers and producers. With our client libraries and connectors, we significantly reduced the burden of this design. And remember that we can run this anywhere, giving you a standard pattern that you can use globally. Finally, processing it at the edge is no joke. You can certainly get connectivity between locations around the world, however trying to process all this data in the cloud or a primary data center can drive up transfer costs and potentially delay insights just due to the sheer volume of data. By having systems at the edge that can provide some type of processing, think of aggregating or merging data, filtering events or serving an embedded machine learning model, having a processing system at the edge is nontrivial, but extremely beneficial. Also, if you are looking at this diagram and when you say to yourself, I've never heard of Core or Near-edge, that's okay, I'm pretty sure I made that up. Because when we're doing the demo today I'll explain what I meant. There are things that sit near the edge, but there's also things that set even further to the edge. And I think it's a good way to disambiguate them. So for the affirmation difficulties, especially limited resources, we can look to the suite of AWS edge services. AWS can help deliver compute options that address all the different edge types we discussed previously. Let's go through each at a bit more detail. AWS outposts is a fully managed service that offers the same AWS infrastructure, AWS services, APIs, and tools to virtually any data center, colo or on-premise facility for a truly consistent hybrid experience. AWS Outpost is ideal for workloads that require low latency access to on-prem systems, local data processing, data residency and migration of applications with local system interdependencies. Outpost is available as a 42U rack that could scale from one to 96 racks to create a pool of compute and storage capacity, coming soon, if not already, Outposts will be available in two smaller form factors, in 1U and 2U rack mountable servers for locations with limited space or capacity requirements. So think about those remote locations we discussed previously. These small form factor outposts would be extremely helpful. AWS Local Zones are a type of AWS infrastructure deployed at places, AWS Compute, Storage, Database and other select services, close to a large population industry or IT centers. With AWS Local Zones, you can easily run applications that need single digit millisecond latency closer to end users in a specific geography. AWS Local Zones are ideal for use cases such as media and entertainment content creation, real-time gaming, live video streaming and machine learning interface. This is also another service when thinking about remote locations, especially if your use case permits data moving over to the internet, albeit with much less hops. AWS Snowball, which is part of the AWS Snow Family is an edge computing data migration and edge storage device that comes in two different options. Snowball edge storage optimized devices provide both block storage and Amazon S3 compatible object storage and 40 vCPUs. They are well-suited for local storage and large scale data transfer. Snowball edge compute optimized devices provide 52 vCPUs, blocks in object storage and an optional, excuse me, an optional GPU for use cases like advanced machine learning and full motion video analysis in disconnected environments. You can use these devices for data collection, machine learning and processing and storage in environments with intermittent connectivity like manufacturing, industrial and transportation or in extremely remote locations, think military or maritime operations. Before shipping them back to AWS, these devices may also be rack mounted and clustered together to build larger temporary installations. I actually had a Snowball edge at my house to ensure that we could run Confluent on it, which proved to be true. But let me tell you that when you power that thing on, you might as well call it an AWS avalanche for the first 15 seconds when it just was spinning up, my primal fear definitely kicked in. It's quiet after that though. The Snow Family could help us address those partially disconnected or even fully disconnected edge scenarios. The final edge service we will cover is AWS Wavelength, which is an AWS infrastructure offering optimized for mobile edge computing applications, remember that MEC. Wavelength zones are AWS infrastructure deployed that embeds AWS compute and storage services within communication service providers, data centers at the edge of the 5G network. So application traffic from 5G and 4G devices can reach application servers running a Wavelength zone without leaving the telecommunication network. This avoids the latency that would often result from the application and traffic having to traverse multiple hops across the internet to reach their destination, enabling customers, to take full advantage of latency and bandwidth benefits offered by modern 5G networks. AWS WAvelength is available in multiple cities across the US or on Verizon's 5G network in Tokyo and Osaka, Japan and on the KDDI 5G network, in Daejeon, South Korea on SK telecom's 5G network and in London Vodafone's 5G network. So combining the power of AWS EC2, robust carrier networks for cutting edge, pun-intended use cases. So AWS helps us get compute and storage pretty much anywhere you need it when you combine all the services we just went through. What is missing though, is a common platform that can easily be deployed across these services that can scale to match your current and future workloads and finally has mechanisms to connect the edge to the rest of your network. Of course, I'm talking about Confluent. By combining AWS services with our technology, we unlock the outcomes highlighted here. Migrations, global data meshes, universal data sharing, increased availability, or providing DR, bridging your on-premise resources to the cloud. And of course the most apt this presentation, aggregating data from the edge. So I mentioned our technology that makes all this easier. So we're now gonna dive deeper into what Confluent brings to the table. The first technology I'm really proud to discuss is Confluent for Kubernetes. Our engineers designed the truly Kube-native way to deploy Confluent and coupled with AWS EKS, we have an ideal architecture to deliver Confluent in a scalable, highly available manner, supported by both AWS and Confluent. Also an important note, Local Zones, Wavelength and Outpost all support EKS. Confluent for Kubernetes introduces a declarative API to deploy and manage Confluent in a variety of infrastructures. This means you can manage topics and securities through infrastructure as code rather than manual processes. It also enables you to integrate with ecosystem toolings to get you cloud native security, reliability, and DevOps automation. Let's expand on some of the benefits of Confluent for Kubernetes across three key differentiators. The first is cloud native. Confluent for Kubernetes allows you to quickly scale to changing business demands with a single command elastic scaling rather than more manual and time-intensive processes that you would typically need to use. It also helps accelerate time to value by simplifying the deployment and management of the platform through infrastructure's code approach that pre-configures everything. This means it provides an enterprise ready platform that takes the guesswork out of deployment and management. In terms of how it's complete, it helps you implement use cases end to end with all of our Confluent platform components ready to use out of box. It is also secure by default and integrates with cloud native Kubernetes ecosystem tooling like HashiCorp Vault or AWS Secrets Manager for managing secrets. Finally, it makes data in motion available everywhere because it provides a consistent operational experience across market leading Kubernetes distributions. It also makes it easy to build hybrid and multi-cloud architectures by simplifying the process of connecting self-managed clusters to Confluent cloud. This helps you get cloud ready and allows them to seamlessly migrate workloads to Confluent cloud when you're ready in the future. Confluent for Kubernetes or C for K or CFK for short, will give you a consistent templatable, source control mechanism for deployment of Confluent across the afforementioned suite for AWS edge services. So Confluent for Kubernetes and AWS edge services make it easy for us to get Confluent everywhere and anywhere we need it. Confluent cluster linking will help us to put our data in motion and allow us to connect all of our sites, edge, regional, headquarters, et cetera, together, to form a global data mesh. Data is syndicated and replicated between on-prem and on-prem, cloud and cloud, on-prem and cloud, edge and cloud and any mix that fits your outcomes. All of this is achieved by leveraging the internal replication mechanism of Kafka and preserving all sense between source and mere topics. Though, not necessarily required for edge use cases, all set preservation is helpful for some multi-region cluster or DR scenarios. Okay, we've got Confluent deployed everywhere and we linked it all together. You're probably wondering how do we actually get data in and out of the system, is pretty important question. Let's first discuss our support of clients. I'm sure that most of these listed up here support your use cases. However, I have no doubt that someone out there is laughing about your remote site running a 4chan application that was developed 20 years ago. We do have an answer for that, which we'll cover in the next couple of slides. So in addition to this bevy of software clients, we also have rest and MQTT proxies, but now let's shift our focus over to Kafka Connect. Connect allows us to source events from other systems like relational databases or mainframes in the Kafka topics and we call those source connectors. We can also use sync connectors to take amends from topics and send them into other data systems like elastic search or S3. Finally, the Kafka Connect framework is fall tolerant and scalable. There are a number of popular open source connectors out there in the wild. However, Confluent has expanded on those open source Kafka connectors to further increase the number of available data sources, sorry about that, data sources and sinks in order to move data in and out of Kafka. A developer working with open source Apache Kafka will have two options, develop their own connectors using the Kafka connect framework or leverage the aforementioned open-source connectors already built by the community. The challenge with the first option is the time and effort it takes. In 2019, Confluent increased its connector portfolio from around 10 to over 100 supportive connectors whose experience we measured, it takes an average of six weeks with a full-time engineer to develop one connector. And this is the time it took the world's Kafka experts. The challenge with the second option is that all of these open source connectors will be unsupported. This would generate significant risk for an organization deploying Kafka into production. What would happen if something breaks? Would the organization feel confident about fixing these issues without help from the experts? This is why Confluent offers a portfolio of over 130 connectors around 100 of which were developed and supported directly by us. Another, around 30, which were developed by our partners and validated fully by Confluent. You can run these connectors yourself anywhere, including the edge, using Confluent platform or fully managed on Confluent cloud. Remember our client libraries in that 4chan application I joked about, if you do have a legacy system that cannot easily integrate with Kafka or Confluent, you can grab the events from the underlying database mainframe or messaging system using these source connectors. You can even scan log files on application hosts and send those to Confluent using our connectors between our client libraries, our rest and MQTT proxies, and finally our connectors, we can bridge almost any data from anywhere to anywhere. Remember the challenge earlier of lean processing at the edge? Kafka streams allows us to build out applications in either Java or Scala to do things with events in real time. You could, for example, filter out specific events for one topic using a stream, and then place the subset of events into another topic. You could transform events from one topic, say teams serialization or aggregating fields, then place them into another topic. You can even take events from multiple topics and combine them. Streams also supports embedded machine learning models. The problem with Streams is that Java or Scala can be difficult and limit how many of our engineers would be able to develop Streams. Fortunately, Confluent built ksqlDB on top of Kafka Streams to provide a lightweight sequel-like interface so we can build the same streaming applications without Java or Scala. Like in the example above, what we see here in this slide is the same task being achieved using a Java application that's consuming events from Kafka and then coded in Java on Kafka Streams. And finally, a single select statement ksqlDB. I think most of you will agree that this powerful abstraction leader will make data and motion applications much more accessible to your teams. As a matter of fact, if you want to learn more about ksqlDB, and our connectors, please check out confluent.awsworkshop.io. So once you and your teams have all these awesome streaming applications running in ksqlDB, we have some tools that will make managing these applications even easier. The first is our stream catalog, which is a knowledge base for data in motion. It's like the company's public library for event streams. The key idea is to centralize all of the Confluent-related metadata from any of your clusters. With all that real-time processing we're gonna do, it's important to determine where did this data come from? Where is it going and where or when or how was it transformed? This is what stream lineage does, providing a gooey to give us the answers to those exact questions. Finally, stream quality via our schema registry ensures that events have proper fields and field type providing a mechanism for scheme evolution without interruption. And in the near future, we'll provide validation built based on business rules. We have covered many of the tools that make it easier to get Confluent and data motion running at the edge. However, the edge sort of implies that there's something in the middle, right? So sourcing and connecting all this data globally is one part of the picture, but eventually you're gonna want to aggregate all this and you might need a pretty significantly sized cluster to hold all that data. Kafka at that scale can be daunting. This is where Confluent Cloud comes in, which is our fully managed service in AWS. Let us at Confluent worry about all the operational burden so you can focus on building things instead of running them. A few Confluent Cloud features provision the cluster instantly, no waiting for a cluster to spin up or concern for large operation teams, large operational teams for large scale workloads. Usage based billing, no need to spend a penny more than you have to. You will always be on the latest version of Kafka. Did we just upgrade your cluster with no downtime interruption or performance degradation? Yup, we did. With this massive global data mesh, you're gonna want industry leading support. Confluent can support clusters running anywhere at the largest scale. We also have some exciting new support features like Health+, which can provide you intelligent alerts that you can get in front of potential issues before they become problematic. We also offer proactive support, which allows our support teams to send out notifications of any probable trouble based on telemetry from your clusters. So we discussed all of the AWS and Confluent services, features and technologies that make the edge easier, but to further cement the concept, let's discuss some use cases. In retail, digital transformation enables many new innovative use cases, including customer 360 degree experiences, cross selling and collaboration with partner vendors. This is relevant for any kind of retailer. No matter if you think about retail stores like Walmart, coffee shops like Starbucks or cutting-edge shops like Amazon Go Store. National or global retailers can have hundreds or thousands of brick and mortar stores, which can generally have some type of on-premise computer storage. Current infrastructure could be displaced by Outposts, Local Zones or Wavelength running Confluent, which allows customers to aggregate, to compute and potentially share data across locations. Less overhead, more possibilities. Consider logistics and edge use cases. Correlation of data in real time is a game changer for any logistics scenario, track and trace end-to-end for package delivery, communication between delivery drones or humans using cars and the local service collection booths, accelerated processing in the logistics center, coordination of planning of car sharing/ride sharing, traffic-like management in a smart city or so on. Think about a smart tractor trailer, communicating with a smart camera in a connected city that can alert the driver or safety system of oncoming traffic around a blind quarter, gotta be able to do that low latency. With low latency of wavelength and data sharing potential Confluent, we can unlock these types of real-time possibilities that were only dreams of the past. Industrial edge use cases include edge integration and processing in real-time, which are key for success in modern IOT architectures. Various use cases exist for industry 4.0 including predictive maintenance, quality insurance, process automation and cyber security. Building a digital twin with Confluent is one of the most frequent scenarios and a perfect fit for many use cases. The AWS edge suite with Confluent can help provide modern compute and data movement to industry. But I want to call out private mech from a moment. AWS can deliver it outpost to an industrial site. And in North America, Verizon could wire it for 4G, 5G connectivity, providing a private Wavelength zone. Layer on Confluent and you have a private mech infrastructure that can blanket your entire locale, help you modernize, replace legacy network equipment. This is by no means an exhaustive list of use cases. I had the pleasure of speaking with an edge session hosted by Tapia Networks a few months back where I had a chance to meet Chris Allen of Red5 Pro. His company is using Wavelength to provide viewers of live events, new, novel, real-time interactions. For example, imagine attending an air show and being able to watch from the inside of the cockpit in near real time using Red5 Pro, that's already happening today in Wavelength. So we've covered how edge services and Confluent technologies compliment each other to create a global data mesh. However, I wanted to take a moment to highlight how our partnerships have grown. Back in August of 2020, we only had a single batch. A little over a year later, here we are, and we'll be adding Lambda and RDS service ready to the collection in the near future. So what is my point here? Confluent, in my opinion, has the best platform in the world for data movement. AWS, in my opinion is the best cloud provider in the world. AWS is likely not going to dedicate the resources to build the technology we have. And Confluent is likely not gonna start building data centers anytime soon. We truly are better together, which enhances the outcome we could jointly provide to you. So let me tell you an origin story. I think we all like origin stories. We're now gonna dive into the Confluent Wavelength solution, which is the basis of our demonstration and something I am really proud of. This all began with a call from a solution architect from the Wavelength team at AWS. They learned of Confluent through our Outpost service ready designation and found a blog post from a fellow coworker of mine, Kai Waehner. Kai is one of our field CTOs and he works with customers on their data in motion use cases on a daily basis. This solution architect drew our attention to one particular diagram. This diagram shows Kafka collecting events at the edge, and then replicating the events running in a factory, then aggregating in the cloud. The question was, can we replace the edge in factory clusters with Wavelength? My answer was in the form of a quick diagram and a ton of enthusiasm to figure out if we can actually make this work. And this is what we came up with. Confluent running on EKS in Wavelength zone deployed using Confluent for Kubernetes. Our edge cluster is a cluster linked to an aggregation cluster in the AWS region. This particular diagram shows an industrial use case centered around predictive maintenance. Remember, we can run embedded ML models, excuse me, in Confluent and with the low-latency of wavelength, we can provide predictive failure notification in a timely manner. What about aggregation though? What does this potentially unlock? This is a story I love. So this is ultimately the big picture. We have multiple sites using clusters and embedded ML models at the edge with the full dataset across all locations being aggregated into Confluent Cloud using cluster linking. This would allow us to take our aggregate data set, sink in S3 using a fully managed connector, and then further train our ML model using Amazon SageMaker. As our model improves in its ability, we can then push down the updated model to the edge. We create this self-fulfilling loop of improvement while simultaneously removing operational burden from the actual factory site. Awesome. So now, we're gonna turn this on real quick. So now it's time for me to put my data where my mouth is. We have a powerhouse of logos on this slide. You turned it over a little too soon. Can you go back real quick? We have a powerhouse of logos on this slide, which all contributed to the demo today. Interestingly enough, Confluent, Hivecell, Verizon and AWS are all partners with each other as it pertains to the solution. So let's jump right into the demo. Afterwards, Justin will walk us through the data path of what you're seeing. All right, so what you see here is a quick visualization. I'm gonna play some music. (calming music) Happening in real time, I didn't fake this. So let me just stop real quick and Justin's gonna explain exactly what's happening. So can we give Justin just a quick round of applause 'cause one, he deserves it and two, it's part of the demo. (audience applauding) Oh, you switched it back. Don't switch it back. I messed it up, I'm sorry. It's okay. That was your clapping right there, by the way. Okay, go ahead. Right, so this is what we have. We have here on the stage, a Hivecell and the Hivecell is basically a portable Kubernetes cluster that in this case is connected to the 5G network, right? So we have effectively a 5G antenna connected from the Hivecell up to the Verizon Wavelength zone. We have a Wavelength zone where we are running Confluent platform using Confluent for Kubernetes. This is our fully managed or, sorry, this is our managed, this is our Confluent solution for running on edge, right? So what we have is we have the speaker, which is playing the music connected to a Raspberry PI with a sound sector. That is wired up to the five to the... Okay, so what's happening is the loudness sensor is detecting the music and generating MQTT events. Those MPTT events are hitting Confluent platform running in Wavelength zone. And we actually have a Wavelength zone here in Las Vegas, right here in Sin City. If you wanna pick it up there? Yeah, we have a Wavelength zone running in Las Vegas. We have Confluent platform running on the Wavelength zone, using automation that Joe and I built, and that is cluster linking up to Confluent Cloud. So we are able to collect data from the Raspberry PI, send it via an MQTT proxy running on the Hivecell, up to the Confluent platform instance running in Wavelength. And then we're cluster linking that data up to the Confluent Cloud. This allows us to have compute at the edge, right, where we're gathering all the information, gathering this telemetry data from various services and from various components. And then aggregate that up into the cloud. Once it's in the cloud, we then are able to sync it out to a Postgres database in this case, Amazon RDS. And from that we're displayin it and refining. So altogether, this allows us to put an end to end solution where we have data coming from remote sites, potentially in this case a stage, but maybe your factory, maybe your store, aggregate it altogether and analyze that in real time in the cloud. Perfect, thank you so much, Justin. And just to show everyone that again, just cause we caught it so quickly, we're not faking it. If you start playing music, it will visualize. And if I stop it, it'll stop, right? So you can see, this is a very novel example, but the reality is this is an MPTP proxy running here right now. So I could take this, we can plug it into any of your networks, start pointing your MQTT devices at it and start getting data in motion right away. You could also run full blown Confluent platform here. So if you had a scenario where you're like, I can not lose any data, you can have a full persistence layer here at the edge. And then once your connectivity is restored, cluster linking will pick up, move all that data right away. We actually have people running in the field of Raspberry PIs, running Confluent platform, pulling metrics from all their equipment. And then once they get back to home base, cluster linking helps bring all that data and then make it useful to the rest of the organizations. Let's switch back to our, see, fantastic. All right. So actually I just want to give a couple quick shout outs. So I want to call it Robbie Belson over, he's an edge evangelists at Verizon. Robbie and Justin right here helped me fully automate this so you can quickly run a POC for yourself. Also like to thank Hivecell for building the prototype verge, which is sitting right on top here for today's demonstration. So quick thank you. But also I think we have enough time if anyone has any questions. So any questions out there? I see hands over here. One quick note, the code for the demo, it lives us on GitHub, so you can actually do this today. You can go to github.com/horizon/5Gedgetutorials and provision a Wavelength cluster running in, or an EKS cluster running in Wavelength with Confluent platform running on top of it. So this is fully doable today. You can go home and set this up or test it. Fantastic. So the session doesn't officially end for another 10 minutes or so. So if you do think of any other questions, we're gonna stick around, but we thank you so much for your time. We really appreciate it. (audience applauding) Thank you. (audience applauding) Yeah, go ahead. (inaudible qustions from audience) Oh, that's a great question. So we're using what's called Squarespace cluster linking. So there are two flavors of cluster linking, destination based cluster linking where the destination cluster will monitor source cluster and pull data into it or source-based. We're using source-based in this scenario. So our CP cluster, oh, I'm sorry, real quick. The question was where's cluster linking running? Our CP cluster running in Wavelength zone is source-based cluster linked to Confluent Cloud, and it is pushing events up to the Confluent Cloud cluster. So when it detects any type of severance of connectivity, it just kicks up where it left off. It knows all its offsets and it just starts pushing data as soon as it's up and running again. Great question. The idea here is that you can run Confluent clusters wherever you want, where you can run them on Wavelength, you can run them on the Hivecell, although we're not doing that today, you can run it in your data center, you can run on outpost and then you can use cluster linking to aggregate all the data up into a Confluent Cloud cluster, a fully managed Confluent instance, and then do your processing there. That's great, we have another question over here. (inaudible qustions from audience) Absolutely. So the question was, is Kafka at the heart of it? And that's exactly what it is. So Confluent platform is Kafka in the core of things, but we layer on some technologies that make it more enterprise ready. And of course we can throw in all the support professional services and all the other things you want to do to build gigantic Kafka scale. Great question. Any other questions out here? (inaudible qustions from audience) Oh, that's interesting. Okay, so the question is, do we have validation if there were conflicts, if we had multiple things like cluster length, is that we're talking about two different? It's a great question. So it doesn't exist today, but by either the end of the year by Q1, we'll have a scenario. In that scenario what we would do is we would cluster link to different things and we would make sure that the topic names were different. So in the aggregation cluster, both topics would exist, but they would only exist on the edge via different ones. However, with cluster linking, we're gonna have two new features in the future. One is gonna allow you to have the same topic name in all your edge sites, but then add a prefix based on the cluster link name so that input topic is input topic at anywhere at the edge, but it is houston-inputtopic when it cluster links. And then the next step is to add a funnel type of scenario where we can take all the "input topics" regardless of where they're coming from, and then combine them into one aggregate cluster. That's gonna come out later next year. Great question. Any others? I could talk about Kafka all day. You know, we didn't really talk about the, we didn't really talk about the latency here. That's an excellent question. So the question was what is some of the latency here? So right there between, fortunately there's a Wavelength zone in Sin City which made this demo possible. If there wasn't one here, I wouldn't have done it. Between the verge Hivecell setup and Confluent platform Wavelength, we're talking about 20 to 30 milliseconds of latency, which is actually really impressive if you think about it. I'm a network engineer by heart. So if we had two devices on the same wavelength zone and they were peer to peer, you're talking about 20 to 40 milliseconds, like you could real game first person shot with that, right? But then from Confluent platform to Confluent Cloud, we're riding the Verizon to AWS backbone. That's about 40 to 50 milliseconds to get from Las Vegas over to US-West-2 in Oregon. At that point, Confluent class cluster, or sorry, the cluster linking very minimal overhead. You're talking about extra millisecond or two, really it's network path, that's most of your latency. And then sinking in RDS is almost instantaneous, less than a millisecond. And then Grafana reading from it is almost near real time. Actually, it probably takes us longer to pull Grafana from Oregon and get it back here than it does to actually get the data there. Great question. Yes, we've got a question right here. (inaudible qustions from audience) Oh, we actually have an official Terraform provider. Now, right? It's early access. It's early access, sorry about that. So yeah, you can absolutely do all of this with Terraform in the near future. Are you referring to by, so the question was, are there plans to extend the management of Confluent through Terraform? Quick clarification, are you referring to the managed Confluent Cloud solution or the self? Okay, yeah. The APIs for that are out now and the Terraform provider is early access. (inaudible qustions from audience) It was like a month ago, couple weeks ago. Yeah, it's in progress. We can chat after on that. Yeah, absolutely. Any others out there? We've got a question right here. (inaudible qustions from audience) Oh, absolutely. So the question was around the Raspberry PI and what we're doing here. So again, I wanted to come up with a novel example that would be easy to demo here in this space. So what we have is we have a little loudness sensor, it's a little IOT device. It's kind of hard to see, but it's right here above the speaker. And what it's doing is it's taking just a general relative giving us like an integer value from zero to 400 with the relative loudness. So the loudness will be 400, lowest is zero. You can hear a pin drop. And what I have is running just a very simple four loop running in Python, I'm not a developer. And every 150 milliseconds, I'm pulling the value from that sensor and I'm generating an MQTT event. The MQTT event is hitting the MQTT proxy that's running here on the Hivecells and that MQTT proxy is using that Confluent platform in Wavelength zone as its backend. So as soon as it receives a message, all it knows how to do is produce into some Kafka cluster and it's producing into a Confluent platform running the Wavelength. Very good question. But the idea though, is that it doesn't have to be a novel example, right? It could be full blown. You can have a full blown IOT shop and take this stack, get the IP configured, right? And then take your existing IP for your MQTT proxy or change your DNS and you could be using this right now. One of the stories we're looking at today is the idea of collecting telemetry data from airplanes as they fly through the air, right? And then once the airplane lands at an airport, we're gonna gather the telemetry data from the airplanes, feed that through either a Hivecell or an outpost or through a Wavelength Zone. And then analyze that to determine basically engine health or motor health, health of whether this airplane should be back in the air. Yeah, excellent point. Any other questions out there? (inaudible qustions from audience) Oh, that's actually a great question. So there is some work to build some automation out so that if you were traversing between Wavelength Zones. So let's say your truck is leaving New York City, right, and you're heading towards Atlanta. And I'm picking on those cause those are two Wavelength Zones. And as you start to approach Atlanta, you want to connect 'cause you want the lowest latency. There is a service discovery from Verizon out there that you can enable and put your clients on that will help you figure out to break up that pattern. So the service discovery, the client can reach out to service discovery say, "Hey, is this the closest Wavelength zone to me?" "No.", and I can then switch over to a new cluster. And because the cluster linking, it doesn't matter, what I'm producing to we can all send it back to the aggregation. There's even some automation, it's a little far out, that we could dynamically provision Confluent platform as you approach Atlanta to spin up clusters on demand. So you can make it really self-service to the point where you're not running Confluent platform and Wavelength Zone for no reason, you run it as needed. We've done some experimentation with that and we're really happy with at least our initial results. Any other questions out there? (inaudible qustions from audience) Absolutely, so the question is about encryption. Could we encrypt? So there are a couple of pieces to that. So there is a connect cluster that we put there. It actually isn't necessarily used in the form of this demo, but you could, if we were running a full blown MQTT server here, we have a source connector that can pull MQTT and would work just this way. Instead of pushing the data which we're doing now, we could pull it, but that doesn't really address your question about encryption. So absolutely Confluent Cloud and Confluent platform support TLS. They support encryption at rest. In fact, Confluent Cloud clusters, by default, they're encrypted. You can't have a non-encrypted data at rest Confluent Cloud cluster, it just doesn't exist. We even have a solution for encrypting before you produce messages. We have client libraries and we have some accelerators around the whole idea of encrypting the message, then producing it to Kafka and then consuming it and then decrypting it. So you could absolutely be sure there's nobody's reading that data but you. Great question. Any others out there? All right. I think we've exhausted the audience. I appreciate you guys. Thank you very much. (audience applauding) And let us know if you have any questions after this. We're at booth 220, Confluent data in motion. Check us out.

## Subtitles with Timestamps

[00:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=0s) All right.

[00:01](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1s) Hi, everyone.

[00:02](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2s) Welcome to Confluent at the edge on AWS.

[00:07](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=7s) So we're thrilled to have you in this session today.

[00:10](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=10s) I know there are many different ways

[00:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=11s) to spend your time at re:Invent

[00:13](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=13s) and I just wanted to acknowledge how grateful we are

[00:15](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=15s) to have you here with us.

[00:16](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=16s) I'm Joseph Morais, Staff Cloud Partner

[00:18](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=18s) and Solutions Architect at Confluent,

[00:20](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=20s) and joining me today is Justin Lee,

[00:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=22s) one of our outstanding Staff Solution Engineers.

[00:24](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=24s) How's it going?

[00:25](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=25s) Nice to meet everybody.

[00:26](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=26s) Good to be here.

[00:27](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=27s) We're gonna discuss data in motion at the edge.

[00:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=31s) There'll be some joy, plenty of insight,

[00:33](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=33s) and hopefully some fun.

[00:35](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=35s) So just a quick summary

[00:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=36s) of what we're gonna be diving into today.

[00:38](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=38s) First, we'll do a quick dive into what Apache Kafka is

[00:41](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=41s) and the rise of data in motion.

[00:43](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=43s) We'll then discuss who is Confluent

[00:44](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=44s) and how do we relate to Kafka.

[00:46](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=46s) What do we mean by edge and common challenges

[00:48](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=48s) in these architecture patterns?

[00:50](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=50s) Then we will explore AWS and Confluent technologies

[00:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=53s) that make working at the edge easier.

[00:56](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=56s) We'll close today with a discussion

[00:57](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=57s) of some common edge use cases,

[01:01](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=61s) a live demonstration of data in motion,

[01:03](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=63s) and if time permits some Q&A.

[01:04](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=64s) Buckle up.

[01:08](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=68s) So at its core, Apache Kafka is a scalable,

[01:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=71s) highly available, event streaming platform,

[01:13](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=73s) which you can think of as the central nervous system

[01:15](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=75s) of an enterprise.

[01:16](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=76s) Kafka also makes it easier to get more value

[01:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=79s) out of your existing systems and to make them real time,

[01:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=82s) so to speak.

[01:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=82s) And I say real time, so to speak,

[01:23](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=83s) because it depends on your definition of real time.

[01:25](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=85s) Kafka, we're talking 20 to 30 milliseconds.

[01:28](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=88s) Some people have those absolute zero millisecond use cases,

[01:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=91s) not exactly a Kafka fit.

[01:34](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=94s) We now like to focus on a new paradigm,

[01:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=96s) called data in motion,

[01:38](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=98s) which is centered around event streams

[01:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=99s) and streaming analytics and processing.

[01:42](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=102s) Here, data is not static and at rest,

[01:45](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=105s) but continuously evolving and continuously being processed

[01:47](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=107s) and analyzed in real time.

[01:49](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=109s) In today's world, the fundamental notion

[01:51](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=111s) is that data is moving, not sitting at rest.

[01:54](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=114s) We'll show an example of this in our demo later today.

[01:59](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=119s) Event streaming or data in motion was first developed

[02:02](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=122s) at LinkedIn by the founders of Confluent.

[02:05](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=125s) As we all can see the very best open source technologies

[02:08](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=128s) make their way from Silicon Valley into the enterprise.

[02:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=131s) And as of today,

[02:12](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=132s) over 70% of fortune 500 companies use Apache Kafka,

[02:16](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=136s) the majority of which are Confluent customers.

[02:21](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=141s) Let's quickly discuss what we see happening

[02:23](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=143s) around us every day,

[02:24](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=144s) which is that data is changing the world.

[02:27](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=147s) Whether through our interactions with mobile applications,

[02:30](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=150s) seeing real-time metrics from recent SpaceX launches,

[02:32](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=152s) seeing maintenance workers with tablets

[02:35](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=155s) or witnessing our doctors

[02:37](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=157s) working with our digital medical records,

[02:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=159s) our interactions with the world are immersed with data.

[02:43](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=163s) Data is helping the world build rich front-end

[02:46](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=166s) customer experiences.

[02:47](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=167s) And this is important because even if your business

[02:49](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=169s) has nothing in common with a company like Netflix,

[02:52](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=172s) this is the type of experience that your customers expect

[02:55](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=175s) in all aspects of their lives.

[02:59](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=179s) Data's helping companies move

[03:01](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=181s) towards realtime backend operations.

[03:04](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=184s) Amazon warehouses are a great example

[03:06](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=186s) of how they've driven efficiency and speed

[03:09](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=189s) through harnessing data.

[03:10](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=190s) Confluent has the technology, experience and support

[03:13](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=193s) to make these types of outcomes

[03:15](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=195s) possible for any organization, anywhere in the world.

[03:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=199s) Let's talk a bit more about Apache Kafka,

[03:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=202s) the open source project that Confluent is built on top off.

[03:25](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=205s) Outside of the code, Kafka is also about the community.

[03:28](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=208s) These numbers really speak for themselves.

[03:30](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=210s) The community loves Kafka and Kafka loves them right back.

[03:33](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=213s) For the non-Kafka nerds in the audience, us too,

[03:37](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=217s) a KIP is a Kafka improvement proposal,

[03:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=219s) which is used to submit propositions

[03:42](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=222s) for major changes to open-source Kafka.

[03:45](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=225s) The strength of Kafka is not only its completeness

[03:48](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=228s) as a streaming platform, but the ecosystem around it.

[03:51](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=231s) Kafka is not an island.

[03:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=233s) Fun fact, there are 1,000, that's right,

[03:56](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=236s) that's 1-0-0-0 more lines of code for integrations to Kafka

[04:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=240s) than lines of code for Kafka itself.

[04:02](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=242s) And Kafka is no small project.

[04:05](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=245s) So how does Confluent fit into all this?

[04:08](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=248s) As I mentioned earlier, the founders of Confluent,

[04:09](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=249s) are the original creators of Apache Kafka.

[04:12](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=252s) And the team here at Confluent has over one million hours

[04:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=254s) of contributing to the Kafka open source

[04:17](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=257s) code basic managing Kafka clusters at the largest scale.

[04:21](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=261s) At this time,

[04:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=262s) we have over 5,000 clusters running in Confluent Cloud.

[04:25](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=265s) Our platform extends Apache Kafka,

[04:27](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=267s) to be a secure enterprise-ready platform.

[04:30](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=270s) And we help enterprises all around the world successfully

[04:33](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=273s) to play Kafka at scale and accelerate their time to market.

[04:37](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=277s) Because of our success, our customers have achieved,

[04:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=279s) we've won several important awards,

[04:41](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=281s) including Forbes 100 Best Cloud Companies,

[04:43](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=283s) Morgan Stanley's CTO Innovation Award,

[04:47](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=287s) being inducted into JPMorgan Chase's Hall of Innovation

[04:50](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=290s) and Bank of America's Enterprise Innovation Award.

[04:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=293s) The largest, most innovative organizations in the world

[04:56](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=296s) are partnering with Confluent,

[04:58](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=298s) recognizing us as a key element of their success.

[05:03](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=303s) For those of you who are familiar with Apache Kafka,

[05:06](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=306s) I just wanted to quickly call out some differentiators.

[05:08](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=308s) We'll be discussing most of these in further in detail

[05:10](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=310s) later in the discussion,

[05:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=311s) but I just wanted to prime all of you.

[05:13](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=313s) We have a set of 130 plus prebuilt connectors

[05:16](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=316s) to help you easily connect

[05:17](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=317s) to our different data sources and sync.

[05:20](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=320s) We enable you to elastically scale

[05:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=322s) saving significant costs

[05:23](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=323s) by avoiding manual scaling and provision.

[05:26](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=326s) We offer an event streaming database, ksqlDB,

[05:30](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=330s) which is the easiest way to build stream

[05:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=331s) processing applications.

[05:33](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=333s) We have a set of security functionality

[05:35](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=335s) to ensure enterprise grade security.

[05:37](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=337s) And last, we have a set of functionality

[05:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=339s) that enables you to increase your operational efficiency

[05:42](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=342s) while keeping costs low.

[05:46](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=346s) Excuse me while I catch my breath.

[05:50](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=350s) So verbose.

[05:51](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=351s) Before we get into our discussion of the edge,

[05:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=353s) I would like to discuss another important differentiator

[05:56](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=356s) that deserves its own it's own slide,

[05:57](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=357s) and it's really kind of the basis of our demo today.

[06:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=360s) And it's that Confluent empowers you to run everywhere,

[06:02](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=362s) and I do mean everywhere,

[06:04](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=364s) from a Raspberry PI to a monster bare metal machine,

[06:07](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=367s) Confluent works.

[06:09](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=369s) Our customers can choose between a fully managed

[06:12](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=372s) cloud product in AWS and a software product

[06:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=374s) they can run themselves in their own data centers or VPCs.

[06:18](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=378s) And of course you can use both.

[06:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=379s) You can interconnect these into a global,

[06:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=382s) central nervous system for data in motion.

[06:26](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=386s) And this is becoming a critical component

[06:28](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=388s) of the cloud migration strategy

[06:30](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=390s) of many of our largest customers,

[06:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=391s) because it allows their new applications

[06:33](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=393s) to connect their input and output data

[06:35](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=395s) back into existing legacy systems

[06:38](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=398s) without requiring a big migration all at once.

[06:40](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=400s) Both Confluent Cloud and Confluent Platform

[06:42](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=402s) are subscription services where the spend scales with usage.

[06:45](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=405s) So you're only paying for what you use.

[06:47](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=407s) I think a lot of people think of a journey to the cloud

[06:49](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=409s) as lifting and shifting VMs or instances.

[06:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=413s) That just kind of takes your debt from your on-prem

[06:55](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=415s) into the cloud, your tech debt.

[06:57](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=417s) So by replicating your data from on-prem into the cloud,

[07:01](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=421s) you can build out brand new applications

[07:03](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=423s) with that replicated data set.

[07:05](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=425s) And then once you're satisfied with your new applications,

[07:07](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=427s) you can point your on-prem sources to the cloud.

[07:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=431s) I see customers do it all the time.

[07:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=434s) So what is the edge or edge computing?

[07:17](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=437s) Wikipedia says,

[07:18](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=438s) everyone starts a Wikipedia's definition, right,

[07:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=439s) Wikipedia says, "Edge computing

[07:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=442s) is a distributed computing paradigm

[07:23](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=443s) that brings computation and data storage

[07:27](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=447s) closer to the location where it is needed

[07:29](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=449s) to improve response times and save bandwidth."

[07:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=451s) From a practical perspective,

[07:32](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=452s) edge is really the closest you can get to your workload.

[07:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=456s) That might mean an end user interacting

[07:38](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=458s) with a mobile application or a weather measurement station

[07:41](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=461s) in a remote area with no network connectivity.

[07:46](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=466s) The edge might also be a combination of these use cases.

[07:49](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=469s) Consider a travel platform

[07:51](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=471s) which will have events for mobile devices,

[07:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=473s) events from the food inventory systems,

[07:55](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=475s) updates to travel information manifest and loyalty systems.

[08:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=480s) Even at the edge,

[08:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=480s) having all this data in a single place or system

[08:03](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=483s) has tremendous potential for enhanced customer experiences.

[08:08](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=488s) Let's discuss the first of three common edge patterns.

[08:12](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=492s) The first pattern is remote location,

[08:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=494s) which takes very different forms depending

[08:15](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=495s) on your type of business.

[08:17](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=497s) For a retail company,

[08:18](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=498s) this may include warehouses,

[08:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=499s) storefronts, kiosks, pop-up shops.

[08:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=502s) For a service oriented business,

[08:25](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=505s) this may include offices around the world, right,

[08:27](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=507s) your remote locations.

[08:29](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=509s) For logistics, it may include truck depots,

[08:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=511s) maintenance shops and regional offices.

[08:34](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=514s) The next pattern is partially disconnected edge.

[08:37](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=517s) This is a situation where the network connectivity

[08:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=519s) is limited or time bound.

[08:41](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=521s) Think of a train entering a tunnel

[08:43](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=523s) that relies on satellite communication.

[08:45](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=525s) And for the duration of that tunnel,

[08:47](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=527s) connectivity to the rest of the world is separate.

[08:49](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=529s) Often with these patterns,

[08:51](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=531s) we see mechanisms in place to synchronize data

[08:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=533s) once network connectivity is restored.

[08:57](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=537s) The final pattern we'll be focusing on

[08:59](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=539s) will be the focus of our demonstration later today,

[09:01](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=541s) it's a new type of edge battery.

[09:03](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=543s) MEC or multi-access edge computing

[09:06](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=546s) allows you to provide computational resources

[09:09](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=549s) over telco or carrier networks,

[09:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=551s) allowing you to serve as many devices

[09:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=554s) using the same infrastructure securely and with low latency.

[09:18](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=558s) There are also private mix scenarios.

[09:20](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=560s) We saw that announced yesterday,

[09:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=562s) where 4G, 5G connectivity and edge computing resources

[09:25](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=565s) can be provided to a specific customer and location

[09:28](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=568s) where cell phone towers may not even exist today.

[09:32](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=572s) So the edge is really cool.

[09:34](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=574s) It allows you to unlock new experiences for customers,

[09:37](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=577s) gain insight from data points never previously available,

[09:40](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=580s) or at least not in a timely fashion

[09:42](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=582s) or aggregate data from across the globe.

[09:46](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=586s) The problem is that edge is difficult.

[09:48](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=588s) The first thing maybe the most important challenge

[09:50](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=590s) is that of limited resources at the edge.

[09:52](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=592s) Likely the first thing that jumps to mind is budget,

[09:55](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=595s) which is certainly part of the issue,

[09:56](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=596s) but not the only limiting factor.

[09:59](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=599s) At the edge, we often have little

[10:01](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=601s) or no technical hands on staff.

[10:03](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=603s) In a retail scenario,

[10:04](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=604s) this often means asking a retail associate

[10:07](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=607s) to physically access equipment.

[10:09](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=609s) I've been there before.

[10:10](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=610s) At a remote monitoring station,

[10:12](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=612s) there may be no one on site for days, weeks,

[10:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=614s) or even months at a time.

[10:17](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=617s) Change operations at the edge can feel perilous

[10:21](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=621s) due to the aforementioned limited budgets

[10:23](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=623s) and lack of handling support,

[10:24](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=624s) often roll-outs upgrades or changes at the edge

[10:27](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=627s) can be overwhelming.

[10:29](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=629s) Outages in any form in today's world,

[10:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=631s) generally result in a loss of confidence

[10:33](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=633s) to end users of those systems,

[10:34](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=634s) whether they're internal or external to the organization.

[10:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=639s) Our second challenge is with device integration.

[10:42](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=642s) Consider just a single department in a hospital.

[10:45](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=645s) There are devices which with different connectivity types,

[10:48](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=648s) operating systems, manufacturers, et cetera,

[10:51](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=651s) getting these device voices to communicate

[10:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=653s) with a single messaging backbone can be very difficult.

[10:56](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=656s) In this example, we're only looking at one department.

[10:59](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=659s) Imagine the number of data points

[11:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=660s) across the entire hospital,

[11:02](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=662s) a network of hospitals, et cetera,

[11:05](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=665s) Amazon AWS has this concept of well-architected framework,

[11:08](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=668s) which distills what Amazon and AWS have learned

[11:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=671s) over years of building robust, scalable systems.

[11:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=674s) One of the tenets of well architected

[11:17](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=677s) is to loosely couple your applications,

[11:20](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=680s) which means not having one thing talk to another directly

[11:24](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=684s) because that is brittle and does not scale well.

[11:26](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=686s) Instead, have something in the middle

[11:27](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=687s) that scales really well and is highly available.

[11:30](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=690s) Later in the presentation,

[11:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=691s) we'll go over some of the technologies

[11:33](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=693s) that Confluent has layered on top of edge Kafka

[11:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=696s) which by design is highly available and scalable.

[11:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=699s) Think about how these features can help you build

[11:41](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=701s) a global network of loosely coupled data consumers

[11:44](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=704s) and producers.

[11:46](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=706s) With our client libraries and connectors,

[11:48](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=708s) we significantly reduced the burden of this design.

[11:51](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=711s) And remember that we can run this anywhere,

[11:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=713s) giving you a standard pattern that you can use globally.

[11:57](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=717s) Finally, processing it at the edge is no joke.

[12:02](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=722s) You can certainly get connectivity

[12:04](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=724s) between locations around the world,

[12:05](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=725s) however trying to process all this data in the cloud

[12:08](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=728s) or a primary data center can drive up transfer costs

[12:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=731s) and potentially delay insights

[12:12](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=732s) just due to the sheer volume of data.

[12:15](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=735s) By having systems at the edge

[12:16](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=736s) that can provide some type of processing,

[12:18](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=738s) think of aggregating or merging data,

[12:21](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=741s) filtering events or serving an embedded

[12:23](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=743s) machine learning model,

[12:25](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=745s) having a processing system at the edge is nontrivial,

[12:28](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=748s) but extremely beneficial.

[12:30](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=750s) Also, if you are looking at this diagram

[12:32](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=752s) and when you say to yourself,

[12:33](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=753s) I've never heard of Core or Near-edge, that's okay,

[12:35](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=755s) I'm pretty sure I made that up.

[12:37](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=757s) Because when we're doing the demo today

[12:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=759s) I'll explain what I meant.

[12:40](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=760s) There are things that sit near the edge,

[12:42](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=762s) but there's also things that set even further to the edge.

[12:43](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=763s) And I think it's a good way to disambiguate them.

[12:47](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=767s) So for the affirmation difficulties,

[12:49](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=769s) especially limited resources,

[12:51](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=771s) we can look to the suite of AWS edge services.

[12:54](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=774s) AWS can help deliver compute options

[12:56](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=776s) that address all the different edge types

[12:58](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=778s) we discussed previously.

[13:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=780s) Let's go through each at a bit more detail.

[13:03](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=783s) AWS outposts is a fully managed service

[13:05](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=785s) that offers the same AWS infrastructure,

[13:07](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=787s) AWS services, APIs,

[13:10](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=790s) and tools to virtually any data center,

[13:12](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=792s) colo or on-premise facility

[13:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=794s) for a truly consistent hybrid experience.

[13:16](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=796s) AWS Outpost is ideal for workloads

[13:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=799s) that require low latency access to on-prem systems,

[13:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=802s) local data processing, data residency

[13:25](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=805s) and migration of applications

[13:27](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=807s) with local system interdependencies.

[13:29](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=809s) Outpost is available as a 42U rack

[13:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=811s) that could scale from one to 96 racks

[13:34](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=814s) to create a pool of compute and storage capacity,

[13:37](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=817s) coming soon, if not already,

[13:38](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=818s) Outposts will be available in two smaller form factors,

[13:41](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=821s) in 1U and 2U rack mountable servers for locations

[13:44](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=824s) with limited space or capacity requirements.

[13:47](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=827s) So think about those remote locations

[13:49](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=829s) we discussed previously.

[13:50](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=830s) These small form factor outposts would be extremely helpful.

[13:55](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=835s) AWS Local Zones are a type of AWS infrastructure

[13:59](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=839s) deployed at places, AWS Compute,

[14:01](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=841s) Storage, Database and other select services,

[14:04](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=844s) close to a large population industry or IT centers.

[14:08](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=848s) With AWS Local Zones, you can easily run applications

[14:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=851s) that need single digit millisecond latency

[14:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=854s) closer to end users in a specific geography.

[14:18](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=858s) AWS Local Zones are ideal for use cases

[14:20](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=860s) such as media and entertainment content creation,

[14:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=862s) real-time gaming, live video streaming

[14:25](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=865s) and machine learning interface.

[14:28](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=868s) This is also another service

[14:29](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=869s) when thinking about remote locations,

[14:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=871s) especially if your use case

[14:32](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=872s) permits data moving over to the internet,

[14:35](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=875s) albeit with much less hops.

[14:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=879s) AWS Snowball, which is part of the AWS Snow Family

[14:42](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=882s) is an edge computing data migration and edge storage device

[14:45](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=885s) that comes in two different options.

[14:48](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=888s) Snowball edge storage optimized devices

[14:50](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=890s) provide both block storage and Amazon S3

[14:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=893s) compatible object storage and 40 vCPUs.

[14:57](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=897s) They are well-suited for local storage

[14:59](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=899s) and large scale data transfer.

[15:02](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=902s) Snowball edge compute optimized devices

[15:04](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=904s) provide 52 vCPUs, blocks in object storage and an optional,

[15:10](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=910s) excuse me, an optional GPU for use cases

[15:12](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=912s) like advanced machine learning

[15:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=914s) and full motion video analysis in disconnected environments.

[15:17](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=917s) You can use these devices for data collection,

[15:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=919s) machine learning and processing and storage in environments

[15:24](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=924s) with intermittent connectivity like manufacturing,

[15:28](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=928s) industrial and transportation

[15:30](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=930s) or in extremely remote locations,

[15:32](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=932s) think military or maritime operations.

[15:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=936s) Before shipping them back to AWS,

[15:38](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=938s) these devices may also be rack mounted

[15:40](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=940s) and clustered together

[15:41](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=941s) to build larger temporary installations.

[15:44](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=944s) I actually had a Snowball edge at my house

[15:46](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=946s) to ensure that we could run Confluent on it,

[15:49](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=949s) which proved to be true.

[15:51](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=951s) But let me tell you that when you power that thing on,

[15:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=953s) you might as well call it an AWS avalanche

[15:55](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=955s) for the first 15 seconds when it just was spinning up,

[15:58](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=958s) my primal fear definitely kicked in.

[16:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=960s) It's quiet after that though.

[16:02](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=962s) The Snow Family could help us

[16:03](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=963s) address those partially disconnected

[16:05](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=965s) or even fully disconnected edge scenarios.

[16:08](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=968s) The final edge service we will cover is AWS Wavelength,

[16:12](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=972s) which is an AWS infrastructure offering optimized

[16:15](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=975s) for mobile edge computing applications, remember that MEC.

[16:20](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=980s) Wavelength zones are AWS infrastructure deployed

[16:23](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=983s) that embeds AWS compute and storage services

[16:26](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=986s) within communication service providers,

[16:27](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=987s) data centers at the edge of the 5G network.

[16:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=991s) So application traffic from 5G and 4G devices

[16:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=996s) can reach application servers running a Wavelength zone

[16:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=999s) without leaving the telecommunication network.

[16:42](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1002s) This avoids the latency that would often result

[16:44](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1004s) from the application and traffic

[16:45](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1005s) having to traverse multiple hops across the internet

[16:48](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1008s) to reach their destination, enabling customers,

[16:51](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1011s) to take full advantage of latency

[16:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1013s) and bandwidth benefits offered by modern 5G networks.

[16:57](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1017s) AWS WAvelength is available in multiple cities

[16:59](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1019s) across the US or on Verizon's 5G network

[17:02](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1022s) in Tokyo and Osaka, Japan and on the KDDI 5G network,

[17:07](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1027s) in Daejeon, South Korea on SK telecom's 5G network

[17:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1031s) and in London Vodafone's 5G network.

[17:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1034s) So combining the power of AWS EC2,

[17:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1039s) robust carrier networks for cutting edge,

[17:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1042s) pun-intended use cases.

[17:25](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1045s) So AWS helps us get compute and storage

[17:28](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1048s) pretty much anywhere you need it

[17:30](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1050s) when you combine all the services we just went through.

[17:32](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1052s) What is missing though,

[17:33](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1053s) is a common platform that can easily be deployed

[17:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1056s) across these services that can scale to match your current

[17:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1059s) and future workloads and finally has mechanisms

[17:41](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1061s) to connect the edge to the rest of your network.

[17:44](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1064s) Of course, I'm talking about Confluent.

[17:48](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1068s) By combining AWS services with our technology,

[17:51](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1071s) we unlock the outcomes highlighted here.

[17:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1073s) Migrations, global data meshes, universal data sharing,

[17:57](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1077s) increased availability, or providing DR,

[18:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1080s) bridging your on-premise resources to the cloud.

[18:03](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1083s) And of course the most apt this presentation,

[18:05](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1085s) aggregating data from the edge.

[18:08](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1088s) So I mentioned our technology that makes all this easier.

[18:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1091s) So we're now gonna dive deeper into what Confluent

[18:13](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1093s) brings to the table.

[18:16](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1096s) The first technology I'm really proud to discuss

[18:18](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1098s) is Confluent for Kubernetes.

[18:20](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1100s) Our engineers designed the truly Kube-native way

[18:23](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1103s) to deploy Confluent and coupled with AWS EKS,

[18:26](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1106s) we have an ideal architecture to deliver Confluent

[18:29](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1109s) in a scalable, highly available manner,

[18:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1111s) supported by both AWS and Confluent.

[18:34](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1114s) Also an important note,

[18:35](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1115s) Local Zones, Wavelength and Outpost all support EKS.

[18:40](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1120s) Confluent for Kubernetes introduces a declarative API

[18:43](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1123s) to deploy and manage Confluent

[18:45](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1125s) in a variety of infrastructures.

[18:47](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1127s) This means you can manage topics and securities

[18:49](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1129s) through infrastructure as code rather than manual processes.

[18:52](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1132s) It also enables you to integrate with ecosystem toolings

[18:55](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1135s) to get you cloud native security, reliability,

[18:58](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1138s) and DevOps automation.

[19:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1140s) Let's expand on some of the benefits of Confluent

[19:03](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1143s) for Kubernetes across three key differentiators.

[19:08](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1148s) The first is cloud native.

[19:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1151s) Confluent for Kubernetes

[19:12](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1152s) allows you to quickly scale to changing business demands

[19:15](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1155s) with a single command elastic scaling

[19:17](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1157s) rather than more manual and time-intensive processes

[19:20](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1160s) that you would typically need to use.

[19:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1162s) It also helps accelerate time to value

[19:24](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1164s) by simplifying the deployment and management of the platform

[19:28](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1168s) through infrastructure's code approach

[19:30](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1170s) that pre-configures everything.

[19:32](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1172s) This means it provides an enterprise ready platform

[19:34](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1174s) that takes the guesswork out of deployment and management.

[19:38](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1178s) In terms of how it's complete,

[19:40](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1180s) it helps you implement use cases end to end

[19:44](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1184s) with all of our Confluent platform components

[19:47](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1187s) ready to use out of box.

[19:48](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1188s) It is also secure by default and integrates

[19:51](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1191s) with cloud native Kubernetes ecosystem tooling

[19:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1193s) like HashiCorp Vault or AWS Secrets Manager

[19:56](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1196s) for managing secrets.

[19:58](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1198s) Finally, it makes data in motion available everywhere

[20:01](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1201s) because it provides a consistent operational experience

[20:04](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1204s) across market leading Kubernetes distributions.

[20:07](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1207s) It also makes it easy to build hybrid

[20:09](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1209s) and multi-cloud architectures by simplifying the process

[20:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1211s) of connecting self-managed clusters to Confluent cloud.

[20:15](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1215s) This helps you get cloud ready

[20:16](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1216s) and allows them to seamlessly migrate workloads

[20:20](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1220s) to Confluent cloud when you're ready in the future.

[20:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1222s) Confluent for Kubernetes or C for K or CFK for short,

[20:26](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1226s) will give you a consistent templatable,

[20:28](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1228s) source control mechanism for deployment of Confluent

[20:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1231s) across the afforementioned suite for AWS edge services.

[20:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1236s) So Confluent for Kubernetes and AWS edge services

[20:38](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1238s) make it easy for us to get Confluent everywhere

[20:40](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1240s) and anywhere we need it.

[20:42](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1242s) Confluent cluster linking

[20:44](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1244s) will help us to put our data in motion

[20:46](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1246s) and allow us to connect all of our sites,

[20:47](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1247s) edge, regional, headquarters, et cetera,

[20:51](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1251s) together, to form a global data mesh.

[20:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1253s) Data is syndicated

[20:55](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1255s) and replicated between on-prem and on-prem,

[20:58](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1258s) cloud and cloud, on-prem and cloud,

[21:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1260s) edge and cloud and any mix that fits your outcomes.

[21:03](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1263s) All of this is achieved by leveraging

[21:05](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1265s) the internal replication mechanism of Kafka

[21:07](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1267s) and preserving all sense between source and mere topics.

[21:10](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1270s) Though, not necessarily required for edge use cases,

[21:13](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1273s) all set preservation is helpful

[21:15](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1275s) for some multi-region cluster or DR scenarios.

[21:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1279s) Okay, we've got Confluent deployed everywhere

[21:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1282s) and we linked it all together.

[21:24](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1284s) You're probably wondering how do we actually get data

[21:25](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1285s) in and out of the system, is pretty important question.

[21:28](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1288s) Let's first discuss our support of clients.

[21:30](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1290s) I'm sure that most of these listed up here

[21:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1291s) support your use cases.

[21:33](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1293s) However, I have no doubt that someone out there is laughing

[21:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1296s) about your remote site running a 4chan application

[21:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1299s) that was developed 20 years ago.

[21:41](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1301s) We do have an answer for that,

[21:43](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1303s) which we'll cover in the next couple of slides.

[21:45](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1305s) So in addition to this bevy of software clients,

[21:47](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1307s) we also have rest and MQTT proxies,

[21:50](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1310s) but now let's shift our focus over to Kafka Connect.

[21:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1313s) Connect allows us to source events from other systems

[21:56](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1316s) like relational databases or mainframes in the Kafka topics

[21:59](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1319s) and we call those source connectors.

[22:01](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1321s) We can also use sync connectors to take amends from topics

[22:04](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1324s) and send them into other data systems like elastic search

[22:07](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1327s) or S3.

[22:08](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1328s) Finally, the Kafka Connect framework is fall tolerant

[22:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1331s) and scalable.

[22:12](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1332s) There are a number of popular open source connectors

[22:15](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1335s) out there in the wild.

[22:16](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1336s) However, Confluent has expanded

[22:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1339s) on those open source Kafka connectors

[22:21](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1341s) to further increase the number of available data sources,

[22:26](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1346s) sorry about that,

[22:28](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1348s) data sources and sinks in order to move data

[22:29](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1349s) in and out of Kafka.

[22:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1351s) A developer working with open source Apache Kafka

[22:33](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1353s) will have two options,

[22:34](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1354s) develop their own connectors using

[22:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1356s) the Kafka connect framework or leverage the aforementioned

[22:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1359s) open-source connectors already built by the community.

[22:42](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1362s) The challenge with the first option

[22:43](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1363s) is the time and effort it takes.

[22:45](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1365s) In 2019, Confluent increased its connector portfolio

[22:48](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1368s) from around 10 to over 100 supportive connectors

[22:51](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1371s) whose experience we measured,

[22:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1373s) it takes an average of six weeks with a full-time engineer

[22:55](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1375s) to develop one connector.

[22:57](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1377s) And this is the time it took the world's Kafka experts.

[23:02](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1382s) The challenge with the second option is that all of these

[23:04](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1384s) open source connectors will be unsupported.

[23:06](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1386s) This would generate significant risk for an organization

[23:09](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1389s) deploying Kafka into production.

[23:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1391s) What would happen if something breaks?

[23:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1394s) Would the organization feel confident

[23:15](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1395s) about fixing these issues without help from the experts?

[23:18](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1398s) This is why Confluent offers a portfolio

[23:20](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1400s) of over 130 connectors around 100

[23:23](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1403s) of which were developed and supported directly by us.

[23:26](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1406s) Another, around 30, which were developed by our partners

[23:28](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1408s) and validated fully by Confluent.

[23:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1411s) You can run these connectors yourself anywhere,

[23:33](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1413s) including the edge, using Confluent platform

[23:35](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1415s) or fully managed on Confluent cloud.

[23:37](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1417s) Remember our client libraries in that 4chan application

[23:40](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1420s) I joked about,

[23:41](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1421s) if you do have a legacy system

[23:43](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1423s) that cannot easily integrate with Kafka or Confluent,

[23:47](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1427s) you can grab the events from the underlying database

[23:49](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1429s) mainframe or messaging system using these source connectors.

[23:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1433s) You can even scan log files on application hosts

[23:56](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1436s) and send those to Confluent using our connectors

[23:59](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1439s) between our client libraries, our rest and MQTT proxies,

[24:03](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1443s) and finally our connectors,

[24:04](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1444s) we can bridge almost any data from anywhere to anywhere.

[24:09](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1449s) Remember the challenge earlier

[24:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1451s) of lean processing at the edge?

[24:13](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1453s) Kafka streams allows us to build out applications

[24:16](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1456s) in either Java or Scala to do things with events

[24:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1459s) in real time.

[24:20](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1460s) You could, for example,

[24:21](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1461s) filter out specific events for one topic using a stream,

[24:24](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1464s) and then place the subset of events into another topic.

[24:27](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1467s) You could transform events from one topic,

[24:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1471s) say teams serialization or aggregating fields,

[24:34](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1474s) then place them into another topic.

[24:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1476s) You can even take events from multiple topics

[24:38](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1478s) and combine them.

[24:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1479s) Streams also supports embedded machine learning models.

[24:43](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1483s) The problem with Streams is that Java or Scala

[24:47](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1487s) can be difficult and limit how many of our engineers

[24:50](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1490s) would be able to develop Streams.

[24:52](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1492s) Fortunately, Confluent built ksqlDB

[24:55](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1495s) on top of Kafka Streams

[24:56](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1496s) to provide a lightweight sequel-like interface

[25:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1500s) so we can build the same streaming applications

[25:02](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1502s) without Java or Scala.

[25:03](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1503s) Like in the example above,

[25:05](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1505s) what we see here in this slide is the same task

[25:07](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1507s) being achieved using a Java application

[25:09](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1509s) that's consuming events from Kafka

[25:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1511s) and then coded in Java on Kafka Streams.

[25:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1514s) And finally, a single select statement ksqlDB.

[25:17](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1517s) I think most of you will agree

[25:18](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1518s) that this powerful abstraction leader

[25:20](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1520s) will make data and motion applications

[25:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1522s) much more accessible to your teams.

[25:24](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1524s) As a matter of fact, if you want to learn more about ksqlDB,

[25:27](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1527s) and our connectors, please check out

[25:28](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1528s) confluent.awsworkshop.io.

[25:33](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1533s) So once you and your teams have all these awesome

[25:37](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1537s) streaming applications running in ksqlDB,

[25:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1539s) we have some tools that will make managing

[25:41](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1541s) these applications even easier.

[25:42](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1542s) The first is our stream catalog,

[25:44](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1544s) which is a knowledge base for data in motion.

[25:46](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1546s) It's like the company's public library for event streams.

[25:49](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1549s) The key idea is to centralize

[25:51](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1551s) all of the Confluent-related metadata

[25:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1553s) from any of your clusters.

[25:55](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1555s) With all that real-time processing we're gonna do,

[25:57](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1557s) it's important to determine where did this data come from?

[26:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1560s) Where is it going and where or when

[26:02](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1562s) or how was it transformed?

[26:04](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1564s) This is what stream lineage does,

[26:05](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1565s) providing a gooey to give us the answers

[26:09](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1569s) to those exact questions.

[26:10](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1570s) Finally, stream quality via our schema registry

[26:13](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1573s) ensures that events have proper fields and field type

[26:17](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1577s) providing a mechanism for scheme evolution

[26:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1579s) without interruption.

[26:20](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1580s) And in the near future,

[26:21](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1581s) we'll provide validation built based on business rules.

[26:26](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1586s) We have covered many of the tools

[26:28](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1588s) that make it easier to get Confluent and data motion

[26:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1591s) running at the edge.

[26:32](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1592s) However, the edge sort of implies

[26:34](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1594s) that there's something in the middle, right?

[26:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1596s) So sourcing and connecting all this data globally

[26:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1599s) is one part of the picture,

[26:40](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1600s) but eventually you're gonna want to aggregate all this

[26:42](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1602s) and you might need a pretty significantly sized cluster

[26:45](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1605s) to hold all that data.

[26:46](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1606s) Kafka at that scale can be daunting.

[26:48](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1608s) This is where Confluent Cloud comes in,

[26:52](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1612s) which is our fully managed service in AWS.

[26:55](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1615s) Let us at Confluent worry about all the operational burden

[26:58](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1618s) so you can focus on building things instead of running them.

[27:01](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1621s) A few Confluent Cloud features

[27:04](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1624s) provision the cluster instantly,

[27:06](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1626s) no waiting for a cluster to spin up

[27:07](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1627s) or concern for large operation teams,

[27:09](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1629s) large operational teams for large scale workloads.

[27:13](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1633s) Usage based billing,

[27:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1634s) no need to spend a penny more than you have to.

[27:17](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1637s) You will always be on the latest version of Kafka.

[27:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1639s) Did we just upgrade your cluster with no downtime

[27:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1642s) interruption or performance degradation?

[27:25](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1645s) Yup, we did.

[27:28](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1648s) With this massive global data mesh,

[27:30](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1650s) you're gonna want industry leading support.

[27:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1651s) Confluent can support clusters running anywhere

[27:34](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1654s) at the largest scale.

[27:35](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1655s) We also have some exciting new support features

[27:37](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1657s) like Health+, which can provide you intelligent alerts

[27:41](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1661s) that you can get in front of potential issues

[27:44](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1664s) before they become problematic.

[27:46](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1666s) We also offer proactive support,

[27:48](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1668s) which allows our support teams to send out notifications

[27:50](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1670s) of any probable trouble

[27:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1673s) based on telemetry from your clusters.

[27:57](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1677s) So we discussed all of the AWS and Confluent services,

[28:01](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1681s) features and technologies that make the edge easier,

[28:04](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1684s) but to further cement the concept,

[28:06](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1686s) let's discuss some use cases.

[28:08](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1688s) In retail, digital transformation

[28:10](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1690s) enables many new innovative use cases,

[28:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1694s) including customer 360 degree experiences,

[28:16](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1696s) cross selling and collaboration with partner vendors.

[28:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1699s) This is relevant for any kind of retailer.

[28:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1702s) No matter if you think about retail stores like Walmart,

[28:24](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1704s) coffee shops like Starbucks or cutting-edge shops

[28:27](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1707s) like Amazon Go Store.

[28:29](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1709s) National or global retailers can have hundreds or thousands

[28:32](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1712s) of brick and mortar stores,

[28:34](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1714s) which can generally have some type

[28:35](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1715s) of on-premise computer storage.

[28:38](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1718s) Current infrastructure could be displaced by Outposts,

[28:41](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1721s) Local Zones or Wavelength running Confluent,

[28:43](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1723s) which allows customers to aggregate, to compute

[28:46](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1726s) and potentially share data across locations.

[28:49](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1729s) Less overhead, more possibilities.

[28:52](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1732s) Consider logistics and edge use cases.

[28:55](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1735s) Correlation of data in real time is a game changer

[28:58](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1738s) for any logistics scenario,

[29:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1740s) track and trace end-to-end for package delivery,

[29:03](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1743s) communication between delivery drones

[29:05](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1745s) or humans using cars

[29:07](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1747s) and the local service collection booths,

[29:10](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1750s) accelerated processing in the logistics center,

[29:13](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1753s) coordination of planning of car sharing/ride sharing,

[29:16](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1756s) traffic-like management in a smart city or so on.

[29:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1759s) Think about a smart tractor trailer,

[29:21](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1761s) communicating with a smart camera in a connected city

[29:24](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1764s) that can alert the driver or safety system

[29:28](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1768s) of oncoming traffic around a blind quarter,

[29:30](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1770s) gotta be able to do that low latency.

[29:33](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1773s) With low latency of wavelength and data sharing

[29:35](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1775s) potential Confluent,

[29:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1776s) we can unlock these types of real-time possibilities

[29:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1779s) that were only dreams of the past.

[29:41](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1781s) Industrial edge use cases include edge integration

[29:45](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1785s) and processing in real-time,

[29:47](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1787s) which are key for success in modern IOT architectures.

[29:50](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1790s) Various use cases exist for industry 4.0

[29:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1793s) including predictive maintenance,

[29:54](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1794s) quality insurance, process automation and cyber security.

[29:59](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1799s) Building a digital twin with Confluent

[30:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1800s) is one of the most frequent scenarios and a perfect fit

[30:04](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1804s) for many use cases.

[30:05](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1805s) The AWS edge suite with Confluent can help provide

[30:09](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1809s) modern compute and data movement to industry.

[30:13](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1813s) But I want to call out private mech from a moment.

[30:15](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1815s) AWS can deliver it outpost to an industrial site.

[30:18](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1818s) And in North America,

[30:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1819s) Verizon could wire it for 4G, 5G connectivity,

[30:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1822s) providing a private Wavelength zone.

[30:25](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1825s) Layer on Confluent and you have a private mech

[30:27](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1827s) infrastructure that can blanket your entire locale,

[30:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1831s) help you modernize, replace legacy network equipment.

[30:34](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1834s) This is by no means an exhaustive list of use cases.

[30:37](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1837s) I had the pleasure of speaking with an edge session

[30:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1839s) hosted by Tapia Networks a few months back

[30:42](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1842s) where I had a chance to meet Chris Allen of Red5 Pro.

[30:44](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1844s) His company is using Wavelength to provide viewers

[30:47](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1847s) of live events, new, novel, real-time interactions.

[30:50](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1850s) For example, imagine attending an air show

[30:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1853s) and being able to watch from the inside of the cockpit

[30:55](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1855s) in near real time using Red5 Pro,

[30:57](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1857s) that's already happening today in Wavelength.

[31:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1860s) So we've covered how edge services

[31:03](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1863s) and Confluent technologies compliment each other

[31:05](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1865s) to create a global data mesh.

[31:07](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1867s) However, I wanted to take a moment to highlight

[31:09](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1869s) how our partnerships have grown.

[31:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1871s) Back in August of 2020, we only had a single batch.

[31:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1874s) A little over a year later, here we are,

[31:16](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1876s) and we'll be adding Lambda and RDS service ready

[31:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1879s) to the collection in the near future.

[31:21](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1881s) So what is my point here?

[31:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1882s) Confluent, in my opinion,

[31:24](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1884s) has the best platform in the world for data movement.

[31:26](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1886s) AWS, in my opinion is the best cloud provider in the world.

[31:30](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1890s) AWS is likely not going to dedicate the resources

[31:33](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1893s) to build the technology we have.

[31:34](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1894s) And Confluent is likely not gonna start building

[31:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1896s) data centers anytime soon.

[31:38](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1898s) We truly are better together,

[31:40](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1900s) which enhances the outcome we could jointly provide to you.

[31:45](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1905s) So let me tell you an origin story.

[31:46](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1906s) I think we all like origin stories.

[31:48](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1908s) We're now gonna dive into the Confluent Wavelength solution,

[31:51](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1911s) which is the basis of our demonstration

[31:52](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1912s) and something I am really proud of.

[31:55](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1915s) This all began with a call from a solution architect

[31:57](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1917s) from the Wavelength team at AWS.

[32:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1920s) They learned of Confluent

[32:01](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1921s) through our Outpost service ready designation

[32:03](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1923s) and found a blog post from a fellow coworker of mine,

[32:06](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1926s) Kai Waehner.

[32:07](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1927s) Kai is one of our field CTOs and he works with customers

[32:10](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1930s) on their data in motion use cases on a daily basis.

[32:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1934s) This solution architect drew our attention

[32:15](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1935s) to one particular diagram.

[32:17](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1937s) This diagram shows Kafka collecting events at the edge,

[32:20](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1940s) and then replicating the events running in a factory,

[32:23](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1943s) then aggregating in the cloud.

[32:24](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1944s) The question was, can we replace the edge

[32:26](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1946s) in factory clusters with Wavelength?

[32:29](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1949s) My answer was in the form of a quick diagram

[32:32](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1952s) and a ton of enthusiasm to figure out

[32:34](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1954s) if we can actually make this work.

[32:37](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1957s) And this is what we came up with.

[32:38](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1958s) Confluent running on EKS in Wavelength zone

[32:41](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1961s) deployed using Confluent for Kubernetes.

[32:44](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1964s) Our edge cluster is a cluster linked

[32:46](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1966s) to an aggregation cluster in the AWS region.

[32:49](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1969s) This particular diagram shows an industrial use case

[32:51](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1971s) centered around predictive maintenance.

[32:54](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1974s) Remember, we can run embedded ML models, excuse me,

[32:58](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1978s) in Confluent and with the low-latency of wavelength,

[33:01](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1981s) we can provide predictive failure notification

[33:03](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1983s) in a timely manner.

[33:04](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1984s) What about aggregation though?

[33:06](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1986s) What does this potentially unlock?

[33:08](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1988s) This is a story I love.

[33:10](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1990s) So this is ultimately the big picture.

[33:12](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1992s) We have multiple sites using clusters

[33:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1994s) and embedded ML models at the edge

[33:16](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1996s) with the full dataset across all locations

[33:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=1999s) being aggregated into Confluent Cloud using cluster linking.

[33:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2002s) This would allow us to take our aggregate data set,

[33:24](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2004s) sink in S3 using a fully managed connector,

[33:27](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2007s) and then further train our ML model using Amazon SageMaker.

[33:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2011s) As our model improves in its ability,

[33:33](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2013s) we can then push down the updated model to the edge.

[33:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2016s) We create this self-fulfilling loop of improvement

[33:38](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2018s) while simultaneously removing operational burden

[33:41](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2021s) from the actual factory site.

[33:43](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2023s) Awesome.

[33:45](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2025s) So now, we're gonna turn this on real quick.

[33:47](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2027s) So now it's time for me to put my data where my mouth is.

[33:52](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2032s) We have a powerhouse of logos on this slide.

[33:54](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2034s) You turned it over a little too soon.

[33:55](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2035s) Can you go back real quick?

[33:57](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2037s) We have a powerhouse of logos on this slide,

[33:59](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2039s) which all contributed to the demo today.

[34:02](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2042s) Interestingly enough, Confluent, Hivecell,

[34:04](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2044s) Verizon and AWS are all partners with each other

[34:07](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2047s) as it pertains to the solution.

[34:09](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2049s) So let's jump right into the demo.

[34:10](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2050s) Afterwards, Justin will walk us through the data path

[34:12](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2052s) of what you're seeing.

[34:16](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2056s) All right, so what you see here is a quick visualization.

[34:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2059s) I'm gonna play some music.

[34:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2062s) (calming music)

[34:24](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2064s) Happening in real time, I didn't fake this.

[34:27](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2067s) So let me just stop real quick

[34:29](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2069s) and Justin's gonna explain exactly what's happening.

[34:32](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2072s) So can we give Justin just a quick round of applause

[34:34](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2074s) 'cause one, he deserves it and two, it's part of the demo.

[34:37](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2077s) (audience applauding)

[34:38](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2078s) Oh, you switched it back.

[34:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2079s) Don't switch it back.

[34:41](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2081s) I messed it up, I'm sorry.

[34:42](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2082s) It's okay.

[34:45](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2085s) That was your clapping right there, by the way.

[34:49](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2089s) Okay, go ahead.

[34:50](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2090s) Right, so this is what we have.

[34:52](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2092s) We have here on the stage, a Hivecell

[34:54](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2094s) and the Hivecell is basically a portable Kubernetes cluster

[34:59](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2099s) that in this case is connected to the 5G network, right?

[35:02](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2102s) So we have effectively a 5G antenna

[35:05](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2105s) connected from the Hivecell

[35:07](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2107s) up to the Verizon Wavelength zone.

[35:10](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2110s) We have a Wavelength zone where we are running

[35:12](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2112s) Confluent platform using Confluent for Kubernetes.

[35:16](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2116s) This is our fully managed or, sorry, this is our managed,

[35:23](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2123s) this is our Confluent solution for running on edge, right?

[35:27](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2127s) So what we have is we have the speaker,

[35:30](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2130s) which is playing the music

[35:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2131s) connected to a Raspberry PI with a sound sector.

[35:35](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2135s) That is wired up to the five to the...

[35:42](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2142s) Okay, so what's happening is the loudness sensor

[35:45](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2145s) is detecting the music and generating MQTT events.

[35:48](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2148s) Those MPTT events are hitting Confluent platform

[35:51](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2151s) running in Wavelength zone.

[35:52](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2152s) And we actually have a Wavelength zone here in Las Vegas,

[35:54](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2154s) right here in Sin City.

[35:56](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2156s) If you wanna pick it up there?

[35:57](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2157s) Yeah, we have a Wavelength zone

[35:58](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2158s) running in Las Vegas.

[36:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2160s) We have Confluent platform running on the Wavelength zone,

[36:03](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2163s) using automation that Joe and I built,

[36:05](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2165s) and that is cluster linking up to Confluent Cloud.

[36:08](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2168s) So we are able to collect data from the Raspberry PI,

[36:13](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2173s) send it via an MQTT proxy running on the Hivecell,

[36:16](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2176s) up to the Confluent platform instance running in Wavelength.

[36:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2179s) And then we're cluster linking that data

[36:20](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2180s) up to the Confluent Cloud.

[36:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2182s) This allows us to have compute at the edge, right,

[36:25](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2185s) where we're gathering all the information,

[36:27](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2187s) gathering this telemetry data from various services

[36:29](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2189s) and from various components.

[36:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2191s) And then aggregate that up into the cloud.

[36:33](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2193s) Once it's in the cloud,

[36:35](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2195s) we then are able to sync it out

[36:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2196s) to a Postgres database in this case, Amazon RDS.

[36:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2199s) And from that we're displayin it and refining.

[36:42](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2202s) So altogether, this allows us

[36:44](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2204s) to put an end to end solution where we have data

[36:46](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2206s) coming from remote sites,

[36:48](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2208s) potentially in this case a stage, but maybe your factory,

[36:52](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2212s) maybe your store, aggregate it altogether

[36:57](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2217s) and analyze that in real time in the cloud.

[37:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2220s) Perfect, thank you so much, Justin.

[37:02](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2222s) And just to show everyone that again,

[37:04](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2224s) just cause we caught it so quickly,

[37:06](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2226s) we're not faking it.

[37:07](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2227s) If you start playing music, it will visualize.

[37:09](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2229s) And if I stop it, it'll stop, right?

[37:12](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2232s) So you can see, this is a very novel example,

[37:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2234s) but the reality is this is an MPTP proxy

[37:16](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2236s) running here right now.

[37:17](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2237s) So I could take this,

[37:18](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2238s) we can plug it into any of your networks,

[37:20](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2240s) start pointing your MQTT devices at it

[37:23](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2243s) and start getting data in motion right away.

[37:25](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2245s) You could also run full blown Confluent platform here.

[37:28](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2248s) So if you had a scenario where you're like,

[37:29](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2249s) I can not lose any data,

[37:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2251s) you can have a full persistence layer here at the edge.

[37:34](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2254s) And then once your connectivity is restored,

[37:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2256s) cluster linking will pick up, move all that data right away.

[37:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2259s) We actually have people running in the field

[37:41](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2261s) of Raspberry PIs, running Confluent platform,

[37:44](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2264s) pulling metrics from all their equipment.

[37:47](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2267s) And then once they get back to home base,

[37:49](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2269s) cluster linking helps bring all that data

[37:51](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2271s) and then make it useful to the rest of the organizations.

[37:54](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2274s) Let's switch back to our, see, fantastic.

[37:59](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2279s) All right.

[38:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2280s) So actually I just want to give a couple quick shout outs.

[38:03](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2283s) So I want to call it Robbie Belson over,

[38:06](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2286s) he's an edge evangelists at Verizon.

[38:08](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2288s) Robbie and Justin right here

[38:09](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2289s) helped me fully automate this

[38:10](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2290s) so you can quickly run a POC for yourself.

[38:12](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2292s) Also like to thank Hivecell for building

[38:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2294s) the prototype verge,

[38:16](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2296s) which is sitting right on top here

[38:17](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2297s) for today's demonstration.

[38:20](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2300s) So quick thank you.

[38:23](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2303s) But also I think we have enough time

[38:24](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2304s) if anyone has any questions.

[38:26](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2306s) So any questions out there?

[38:30](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2310s) I see hands over here.

[38:32](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2312s) One quick note, the code for the demo,

[38:35](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2315s) it lives us on GitHub, so you can actually do this today.

[38:37](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2317s) You can go to github.com/horizon/5Gedgetutorials

[38:43](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2323s) and provision a Wavelength cluster running in,

[38:47](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2327s) or an EKS cluster running in Wavelength

[38:49](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2329s) with Confluent platform running on top of it.

[38:51](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2331s) So this is fully doable today.

[38:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2333s) You can go home and set this up or test it.

[38:56](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2336s) Fantastic.

[38:57](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2337s) So the session doesn't officially end

[39:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2340s) for another 10 minutes or so.

[39:02](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2342s) So if you do think of any other questions,

[39:04](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2344s) we're gonna stick around,

[39:05](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2345s) but we thank you so much for your time.

[39:06](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2346s) We really appreciate it.

[39:08](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2348s) (audience applauding)

[39:10](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2350s) Thank you.

[39:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2351s) (audience applauding)

[39:15](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2355s) Yeah, go ahead.

[39:17](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2357s) (inaudible qustions from audience)

[39:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2359s) Oh, that's a great question.

[39:20](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2360s) So we're using what's called Squarespace cluster linking.

[39:23](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2363s) So there are two flavors of cluster linking,

[39:25](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2365s) destination based cluster linking

[39:27](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2367s) where the destination cluster will monitor source cluster

[39:30](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2370s) and pull data into it or source-based.

[39:32](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2372s) We're using source-based in this scenario.

[39:33](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2373s) So our CP cluster, oh, I'm sorry, real quick.

[39:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2376s) The question was where's cluster linking running?

[39:38](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2378s) Our CP cluster running in Wavelength zone

[39:40](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2380s) is source-based cluster linked to Confluent Cloud,

[39:43](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2383s) and it is pushing events up to the Confluent Cloud cluster.

[39:47](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2387s) So when it detects any type of severance of connectivity,

[39:50](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2390s) it just kicks up where it left off.

[39:52](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2392s) It knows all its offsets and it just starts pushing data

[39:54](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2394s) as soon as it's up and running again.

[39:56](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2396s) Great question.

[39:57](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2397s) The idea here is that you can run

[39:59](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2399s) Confluent clusters wherever you want,

[40:01](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2401s) where you can run them on Wavelength,

[40:02](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2402s) you can run them on the Hivecell,

[40:04](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2404s) although we're not doing that today,

[40:05](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2405s) you can run it in your data center,

[40:06](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2406s) you can run on outpost and then you can use cluster linking

[40:09](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2409s) to aggregate all the data up into a Confluent Cloud cluster,

[40:12](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2412s) a fully managed Confluent instance,

[40:13](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2413s) and then do your processing there.

[40:15](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2415s) That's great, we have another question over here.

[40:17](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2417s) (inaudible qustions from audience)

[40:21](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2421s) Absolutely.

[40:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2422s) So the question was, is Kafka at the heart of it?

[40:23](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2423s) And that's exactly what it is.

[40:24](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2424s) So Confluent platform is Kafka in the core of things,

[40:29](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2429s) but we layer on some technologies

[40:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2431s) that make it more enterprise ready.

[40:32](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2432s) And of course we can throw in

[40:33](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2433s) all the support professional services

[40:35](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2435s) and all the other things you want to do

[40:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2436s) to build gigantic Kafka scale.

[40:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2439s) Great question.

[40:41](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2441s) Any other questions out here?

[40:45](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2445s) (inaudible qustions from audience)

[41:05](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2465s) Oh, that's interesting.

[41:06](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2466s) Okay, so the question is,

[41:07](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2467s) do we have validation if there were conflicts,

[41:08](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2468s) if we had multiple things like cluster length,

[41:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2471s) is that we're talking about two different?

[41:12](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2472s) It's a great question.

[41:13](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2473s) So it doesn't exist today,

[41:15](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2475s) but by either the end of the year by Q1,

[41:18](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2478s) we'll have a scenario.

[41:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2479s) In that scenario what we would do

[41:21](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2481s) is we would cluster link to different things

[41:23](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2483s) and we would make sure that the topic names were different.

[41:25](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2485s) So in the aggregation cluster, both topics would exist,

[41:28](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2488s) but they would only exist on the edge via different ones.

[41:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2491s) However, with cluster linking,

[41:33](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2493s) we're gonna have two new features in the future.

[41:34](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2494s) One is gonna allow you to have the same topic name

[41:37](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2497s) in all your edge sites, but then add a prefix based on

[41:41](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2501s) the cluster link name so that input topic

[41:45](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2505s) is input topic at anywhere at the edge,

[41:47](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2507s) but it is houston-inputtopic when it cluster links.

[41:51](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2511s) And then the next step is to add a funnel type of scenario

[41:55](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2515s) where we can take all the "input topics"

[41:58](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2518s) regardless of where they're coming from,

[41:59](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2519s) and then combine them into one aggregate cluster.

[42:01](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2521s) That's gonna come out later next year.

[42:03](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2523s) Great question.

[42:05](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2525s) Any others?

[42:06](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2526s) I could talk about Kafka all day.

[42:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2531s) You know, we didn't really talk about the,

[42:13](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2533s) we didn't really talk about the latency here.

[42:15](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2535s) That's an excellent question.

[42:16](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2536s) So the question was what is some of the latency here?

[42:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2539s) So right there between,

[42:21](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2541s) fortunately there's a Wavelength zone in Sin City

[42:23](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2543s) which made this demo possible.

[42:25](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2545s) If there wasn't one here, I wouldn't have done it.

[42:27](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2547s) Between the verge Hivecell setup

[42:30](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2550s) and Confluent platform Wavelength,

[42:32](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2552s) we're talking about 20 to 30 milliseconds of latency,

[42:34](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2554s) which is actually really impressive if you think about it.

[42:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2556s) I'm a network engineer by heart.

[42:38](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2558s) So if we had two devices on the same wavelength zone

[42:40](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2560s) and they were peer to peer,

[42:42](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2562s) you're talking about 20 to 40 milliseconds,

[42:43](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2563s) like you could real game

[42:45](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2565s) first person shot with that, right?

[42:46](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2566s) But then from Confluent platform to Confluent Cloud,

[42:50](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2570s) we're riding the Verizon to AWS backbone.

[42:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2573s) That's about 40 to 50 milliseconds to get from Las Vegas

[42:56](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2576s) over to US-West-2 in Oregon.

[42:58](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2578s) At that point, Confluent class cluster, or sorry,

[43:01](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2581s) the cluster linking very minimal overhead.

[43:03](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2583s) You're talking about extra millisecond or two,

[43:05](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2585s) really it's network path, that's most of your latency.

[43:10](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2590s) And then sinking in RDS is almost instantaneous,

[43:12](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2592s) less than a millisecond.

[43:13](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2593s) And then Grafana reading from it is almost near real time.

[43:17](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2597s) Actually, it probably takes us longer

[43:18](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2598s) to pull Grafana from Oregon and get it back here

[43:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2602s) than it does to actually get the data there.

[43:24](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2604s) Great question.

[43:27](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2607s) Yes, we've got a question right here.

[43:29](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2609s) (inaudible qustions from audience)

[43:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2619s) Oh, we actually have an official Terraform provider.

[43:42](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2622s) Now, right?

[43:43](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2623s) It's early access.

[43:44](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2624s) It's early access, sorry about that.

[43:45](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2625s) So yeah, you can absolutely do all of this with Terraform

[43:48](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2628s) in the near future.

[43:49](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2629s) Are you referring to by, so the question was,

[43:51](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2631s) are there plans to extend the management of Confluent

[43:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2633s) through Terraform?

[43:54](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2634s) Quick clarification, are you referring

[43:56](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2636s) to the managed Confluent Cloud solution or the self?

[43:59](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2639s) Okay, yeah.

[44:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2640s) The APIs for that are out now

[44:02](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2642s) and the Terraform provider is early access.

[44:06](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2646s) (inaudible qustions from audience)

[44:09](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2649s) It was like a month ago, couple weeks ago.

[44:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2651s) Yeah, it's in progress.

[44:13](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2653s) We can chat after on that.

[44:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2654s) Yeah, absolutely.

[44:18](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2658s) Any others out there?

[44:24](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2664s) We've got a question right here.

[44:26](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2666s) (inaudible qustions from audience)

[44:32](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2672s) Oh, absolutely.

[44:33](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2673s) So the question was around the Raspberry PI

[44:35](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2675s) and what we're doing here.

[44:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2676s) So again, I wanted to come up with a novel example

[44:38](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2678s) that would be easy to demo here in this space.

[44:41](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2681s) So what we have is we have a little loudness sensor,

[44:43](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2683s) it's a little IOT device.

[44:45](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2685s) It's kind of hard to see,

[44:46](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2686s) but it's right here above the speaker.

[44:47](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2687s) And what it's doing is it's taking

[44:49](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2689s) just a general relative giving us like

[44:52](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2692s) an integer value from zero to 400

[44:54](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2694s) with the relative loudness.

[44:55](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2695s) So the loudness will be 400, lowest is zero.

[44:59](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2699s) You can hear a pin drop.

[45:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2700s) And what I have is running just a very simple four loop

[45:03](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2703s) running in Python, I'm not a developer.

[45:05](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2705s) And every 150 milliseconds,

[45:07](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2707s) I'm pulling the value from that sensor

[45:09](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2709s) and I'm generating an MQTT event.

[45:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2711s) The MQTT event is hitting the MQTT proxy

[45:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2714s) that's running here on the Hivecells

[45:16](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2716s) and that MQTT proxy is using that Confluent platform

[45:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2719s) in Wavelength zone as its backend.

[45:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2722s) So as soon as it receives a message,

[45:23](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2723s) all it knows how to do is produce

[45:25](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2725s) into some Kafka cluster and it's producing

[45:28](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2728s) into a Confluent platform running the Wavelength.

[45:30](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2730s) Very good question.

[45:32](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2732s) But the idea though,

[45:34](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2734s) is that it doesn't have to be a novel example, right?

[45:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2736s) It could be full blown.

[45:37](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2737s) You can have a full blown IOT shop and take this stack,

[45:39](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2739s) get the IP configured, right?

[45:41](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2741s) And then take your existing IP for your MQTT proxy

[45:44](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2744s) or change your DNS and you could be using this right now.

[45:48](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2748s) One of the stories we're looking at today

[45:50](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2750s) is the idea of collecting telemetry data from airplanes

[45:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2753s) as they fly through the air, right?

[45:55](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2755s) And then once the airplane lands at an airport,

[45:59](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2759s) we're gonna gather the telemetry data from the airplanes,

[46:01](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2761s) feed that through either a Hivecell or an outpost

[46:04](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2764s) or through a Wavelength Zone.

[46:06](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2766s) And then analyze that to determine basically

[46:08](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2768s) engine health or motor health,

[46:10](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2770s) health of whether this airplane should be back in the air.

[46:13](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2773s) Yeah, excellent point.

[46:16](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2776s) Any other questions out there?

[46:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2779s) (inaudible qustions from audience)

[46:30](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2790s) Oh, that's actually a great question.

[46:32](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2792s) So there is some work to build some automation out

[46:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2796s) so that if you were traversing between Wavelength Zones.

[46:38](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2798s) So let's say your truck is leaving New York City, right,

[46:42](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2802s) and you're heading towards Atlanta.

[46:43](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2803s) And I'm picking on those

[46:43](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2803s) cause those are two Wavelength Zones.

[46:45](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2805s) And as you start to approach Atlanta,

[46:47](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2807s) you want to connect 'cause you want the lowest latency.

[46:50](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2810s) There is a service discovery from Verizon out there

[46:53](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2813s) that you can enable and put your clients on

[46:56](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2816s) that will help you figure out to break up that pattern.

[46:59](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2819s) So the service discovery,

[47:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2820s) the client can reach out to service discovery say,

[47:02](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2822s) "Hey, is this the closest Wavelength zone to me?"

[47:04](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2824s) "No.", and I can then switch over to a new cluster.

[47:08](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2828s) And because the cluster linking, it doesn't matter,

[47:09](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2829s) what I'm producing to

[47:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2831s) we can all send it back to the aggregation.

[47:13](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2833s) There's even some automation, it's a little far out,

[47:15](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2835s) that we could dynamically provision Confluent platform

[47:19](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2839s) as you approach Atlanta to spin up clusters on demand.

[47:22](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2842s) So you can make it really self-service

[47:24](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2844s) to the point where you're not running Confluent platform

[47:26](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2846s) and Wavelength Zone for no reason, you run it as needed.

[47:29](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2849s) We've done some experimentation with that

[47:31](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2851s) and we're really happy with at least our initial results.

[47:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2856s) Any other questions out there?

[47:38](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2858s) (inaudible qustions from audience)

[47:54](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2874s) Absolutely, so the question is about encryption.

[47:56](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2876s) Could we encrypt?

[47:57](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2877s) So there are a couple of pieces to that.

[47:58](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2878s) So there is a connect cluster that we put there.

[48:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2880s) It actually isn't necessarily used in the form of this demo,

[48:03](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2883s) but you could,

[48:04](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2884s) if we were running a full blown MQTT server here,

[48:08](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2888s) we have a source connector that can pull MQTT

[48:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2891s) and would work just this way.

[48:12](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2892s) Instead of pushing the data which we're doing now,

[48:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2894s) we could pull it,

[48:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2894s) but that doesn't really address your question

[48:17](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2897s) about encryption.

[48:17](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2897s) So absolutely Confluent Cloud

[48:20](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2900s) and Confluent platform support TLS.

[48:23](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2903s) They support encryption at rest.

[48:25](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2905s) In fact, Confluent Cloud clusters, by default,

[48:27](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2907s) they're encrypted.

[48:28](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2908s) You can't have a non-encrypted data at rest

[48:30](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2910s) Confluent Cloud cluster, it just doesn't exist.

[48:33](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2913s) We even have a solution for encrypting

[48:36](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2916s) before you produce messages.

[48:38](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2918s) We have client libraries and we have some accelerators

[48:40](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2920s) around the whole idea of encrypting the message,

[48:42](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2922s) then producing it to Kafka and then consuming it

[48:46](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2926s) and then decrypting it.

[48:47](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2927s) So you could absolutely be sure

[48:49](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2929s) there's nobody's reading that data but you.

[48:52](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2932s) Great question.

[48:54](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2934s) Any others out there?

[49:00](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2940s) All right.

[49:01](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2941s) I think we've exhausted the audience.

[49:03](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2943s) I appreciate you guys.

[49:06](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2946s) Thank you very much.

[49:07](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2947s) (audience applauding)

[49:09](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2949s) And let us know if you have any questions after this.

[49:11](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2951s) We're at booth 220, Confluent data in motion.

[49:14](https://www.youtube.com/watch?v=l7fH9FWvz_8&t=2954s) Check us out.

