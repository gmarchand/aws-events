# AWS re:Invent 2021 - Remote workforce cloud migration patterns

[Video Link](https://www.youtube.com/watch?v=9G84a9IjpXk)

## Description

Productive remote work is more critical to businesses than ever before. In this session, learn about remote workforce cloud migration patterns, such as virtual desktop, collaboration tooling, and cloud contact centers, following considerations and best practices from the AWS Well-Architected Framework. For each remote workforce pattern, consider the migration path, deployment approach, and application of the AWS Well-Architected Framework and review how these factors contributed to cost-effective, secure, and reliable systems on AWS. Also, hear about customer migration case studies using AWS for remote workforce solutions.

Learn more about re:Invent 2021 at https://bit.ly/3IvOLtK
 
Subscribe: 
More AWS videos http://bit.ly/2O3zS75 
More AWS events videos http://bit.ly/316g9t4

ABOUT AWS
Amazon Web Services (AWS) hosts events, both online and in-person, bringing the cloud computing community together to connect, collaborate, and learn from AWS experts.

AWS is the world’s most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally. Millions of customers—including the fastest-growing startups, largest enterprises, and leading government agencies—are using AWS to lower costs, become more agile, and innovate faster.

#AWS #AmazonWebServices #CloudComputing

## Transcript

(smooth rhythmic music) Welcome everyone to session ARC 205 on remote workforce cloud migration patterns. I'm Jennifer Ihejimba, the solutions architect at AWS. With me on this session is John Walker, also a solutions architect at AWS. We're excited to be joining you today from our home offices to talk to you about major solutions for your remote workforce and how to migrate these solutions to AWS. We know that you probably joined today's session to learn about remote workforce cloud migration patterns and we promise you won't be disappointed. John and I are both part of a small and medium business segment in AWS. More than 50% of our work deals with migrating workloads and very often, we're talkin' to different customers about migrating their remote workforce solutions from on-premises to AWS. So let's get started. So if you think about how many organizations have had to switch to workin' remotely in the past year or two, many fall into that category. The workforce has been changin' for a while and recent events have only accelerated those changes. For example before the pandemic, one in five jobs in the US was held by contractors and 70% of users globally were already workin' remotely at least one day a week. Deloitte's annual activity report at global mergers and acquisitions also show that 79% of organizations expect to increase M&A in 2020. So if you take a look at these long-term trends, it's more important than ever to start planning your workforce transformation, to deliver solutions for your remote staff and to ensure that you enable agility, continuity and security for your remote workforce. So in essence, what we see is that this could create some challenges for your entire organization, whether that means you have call center agents that can no longer go into the physical contact center but still need to support customers remotely or maybe you have employees that need to remotely communicate and collaborate your chat or messagin' solutions with each other to remain productive and feel connected. Your employees may also need to use virtual desktops or streamin' applications without the need for PCs or laptops. With all of these in mind, we thought we'd share with you today four major remote workforce solutions under key migration architecture patents, whether that's your call center agents, employees or students and educators. Here are the key takeaways from this session. We'll cover four main remote workforce solutions. And for each remote workforce pattern, we'll explore deployment paths and migration approach usin' the AWS well-architected principles. So keep in mind that this session is a 200-level talk today in a sense that we're not going to dive deep into the solution architectures, but we are going to see some really cool stuff about migration methodology and architecture best patterns. We'll also cover customer examples and share additional resources as we explore each remote workforce solution. AWS offers several services to enable remote work and learnin' and these are full solutions we'll be talkin' about today. We'll talk about Amazon Connect which enables businesses to have a fully-operational contact center that can be operated virtually anywhere. With Amazon Connect, you can have your agents, your supervisors, your managers and administrators work from home and still be able to perform all their normal contact center activities. We also have Amazon Chime, a collaboration tool that can enable your employees to meet, to chat and place business calls with a single secure application from anywhere. So they're able to collaborate and instantly go from chat to a call, they can share their screen and invite more people to join their meetin' all within the same application with Amazon Chime SDKs. There's also Amazon WorkSpaces, a managed secure desktop as a service solution that helps mobile and remote employees access applications they need by deliverin' a cloud desktop that's accessible anywhere with an internet connection usin' any supported device. And lastly, Amazon AppStream 2.0 which is a fully-managed application streaming service. With Amazon AppStream 2.0, your remote workers or students can access desktop applications they need at anytime. We'll get a chance to discuss all four services durin' this session. So let's kick off with the first AWS remote work solution with Amazon Connect for virtual contact centers. CEOs state overwhelmingly that more than any other element of your business customer experience is the most effective method for creatin' a competitive advantage. But one area where many costs companies continue to struggle to deliver similarly delightful customer experiences is within their contact center. Here, we see some common contact center challenges which are also migration triggers. What you see here answers the question why customers are migratin'. So why are customers migratin'? Last year, we commissioned Forrester Research to perform an independent study of customers who migrated to Amazon Connect across all sizes and segments. The study revealed this set of common challenges customers were facin' with your previous contact center systems makin' it impossible for them to deliver innovative contact center experiences to their customers. One of the challenges they had was havin' expensive legacy solutions. They had complex pricin' and very large upfront costs. Challengin' vendor relationships was another challenge with lack of trust, misleading fees and overall slow development cycles with an inability to scale up or down easily, but sometimes just being difficult to do that. There were also painful frequent outages that cause lapses in service, lost revenue, wasted agent labor and excessive troubleshooting. They were also unable to access powerful AI technologies which were just expensive and most times had very difficult bolt-on integrations. It was complex and expensive to integrate to systems of records are not possible at all within their legacy contact centers. In addition to all of these challenges for legacy or gen one contact centers, think about all the operational costs companies need to purchase or integrate systems from multiple vendors with all of these governed by licenses, hardware, telephony trunks makin' it difficult and costly to implement and maintain. And now I'm eager to share with you the origin story of how Amazon came to market with a simple-to-use omnichannel cloud contact center offering called Amazon Connect. If you've ever had to contact Amazon customer support before, you see how this gets interestin'. At Amazon, we strive to be the Earth's most customer-centric company and the success of our future as a company was built on customer satisfaction. About 12 years ago, our Amazon retail business started to see enormous growth and we were frustrated by all the challenges of legacy contact centers we just talked about. To do this, we needed the right tools to enable exceptional customer experience of skill. But every product we valued, it had fell short. So essentially, we built a tool ourselves to use internally. And in March of 2017 which was about three years ago, we brought that internal tool to market so that all the businesses within Amazon could break free of the same challenges they experience with contact centers. Amazon Connect is a simple-to-use cloud-based contact center we brought to market to deliver exceptional omnichannel customer experiences that are natural, dynamic and personalized. And the secret sauce of Amazon Connect is allowing you to integrate with a breadth of AWS services to accelerate the creation of personalized and dynamic experiences with Amazon Connect. It includes all the standard functionality contact center operations teams have come to expect. Amazon Connect comes with skills-based routin' which maximizes the efficiency of agents and the satisfaction of end customers and it also ensures that you connect the right customer to the right agents at the right time. Voice and chat interactions are recorded makin' it easy to monitor and improve agent quality. All the common reports analytics you would expect are available and easy to use including agent performance, service level and handle time. Our customers often tell us how much they love the audio quality for calls with Amazon Connect. And all you need to get started with Amazon Connect is a standard broadband internet connection and the only hardware you need is a USB headset. Your agent can be located virtually anywhere empowering businesses to offer increased flexibility for work-from-home agents. So now let's take a look at some of the architectural deployment models that we see for contact centers. Here, we have an on-premises-based deployment and these represent the majority of existin' contact center infrastructure we see today. You notice in the diagram how complex these typically are. And in the picture, all of the blocks represented on the screen are actually physical devices. In most circumstances, on-prem contact centers typically stitch together solutions from various vendors and they require numerous integrations and frequently involve extensive and ongoing services. In this setup sadly, customers are locked into complex and expensive licensing and maintenance contracts and they're also further bound by the upfront expenditure of cost and hardware. This makes it very difficult to adapt if your contact center requirements are always changin'. It also poses a challenge to spin up or spin down resources should you choose to innovate or experiment on customer experience in your contact center. Here, we see the hybrid deployment model and you notice in the picture here that the core section is a cloud service with additional onsite themes for localization. The hybrid contact centers most frequently use the cloud for storage, interactive voice response or telephony distribution. They commonly have a lot of one-off integrations that need to be done based on your contact center requirements. One of the challenges with the hybrid deployments is that it increases the anxiety with some contact center companies that are security focused because it increases the complexity of your security posture. Additionally, it doesn't usually address the physical footprint, the licensin', the infrastructure costs. And at best, it just provides a band-aid solution for scalability by usin' a network interactive voice response. There are also more opportunities for support difficulties in mixed environments because there's no clear ownership of a technical issue. For example, the issue could be cloud team versus the on-prem networking teams. Here we see the cloud deployment model with Amazon Connect and this model drastically reduces the complexity that we saw with the on-prem and the hybrid models. Everything you see in the diagram here is an AWS service that's hosted in the cloud, except for the agents and your desktops. This deployment model typically provides the lowest upfront costs, the quickest deployment time and the smallest footprint for your contact center. Amazon Connect is the only cloud contact center today that scales from tens of agents to tens of thousands of agents. So it's a great choice for some of the smallest customers all the way to the largest enterprise customers. Amazon Connect is built from the ground to be 100% cloud-based. There are no adapters, there are no applets or applications or browser extensions to install 'cause every part of Amazon Connect is available purely in the browser. Amazon Connect can be set up in minutes and agents can take calls after just a few simple steps. In fact, you can log in to the AWS console right now, you can answer a short few questions, claim a telephone number and be taking calls before I finish this slide. So lookin' at the diagram here, you see how Amazon Connect integrates with other AWS services that you may be familiar with. I mentioned earlier that the secret sauce of Amazon Connect is allowing you to accelerate the creation of dynamic, natural and personalized experiences with Amazon Connect by integrating with other services on AWS and here we can see the power of those services being utilized. Your call center agents use the Contact Control Panel or CCP for Amazon Connect which is provided out of the box and this is customizable. The Contact Control Panel allows your agents to connect to Amazon Connect usin' a browser-based cellphone over the secure public internet link. You can also integrate your existing CRM systems and your customer data lake with all of your customer information, all usin' AWS Lambda which is a serverless compute offering to connect all of that to your AWS backend systems. For example using Lambda, you can enable your agent to look up the caller ID in your CRM system and be able to return the caller's name and account number and use that account number to satisfy customer requests during the phone call. When a call comes into your organization, the caller ID is automatically passed and captured by Amazon Connect. You can configure identity and access management for your agents and supervisors usin' the AWS identity and management services. You can also store your call recordings and your chat transcripts in Amazon S3 which is our simple storage service and have access to archive these assets over time. You have access to a wide array of AI/ML analytics tool. For example, you have access to an AI/ML tool called Amazon Lex which is the very same agent that powers the popular Alexa device. You can use these AI/ML tools to create better customer experiences like chat bots to monitor and understand your customer sentiments to effectively train your agents. There's another AI/ML tool called Contact Lens for Amazon Connect and this allows supervisors and QA managers to better understand the sentiment, the trends and the compliance risks of customer interactions so they can effectively train agents and replicate success and identify crucial company and product feedback. But overall, you see the reduced complexity in this architecture and there's a lot of innovation you get out of the box with this deployment model with Amazon Connect. So now that we've seen the different deployment models for contact centers, let's talk about the migration path for your legacy or traditional contact centers to Amazon Connect. So how do you get started? The key to a good contact center migration is a good discovery and planning process to allow your teams work in an agile manner and you need to first define your goals. So to do that, we think big and start small and go fast. For example, one of the common use cases that we see with most of our customers is that they will often start with migrating internal lines of businesses like a help desk or kickstart a new contact center project. You want to determine the minimum lovable product. You notice how I said minimum lovable and not minimum viable. Because at AWS, we're always lookin' to delight our customers and not just do the bare viable minimum, so you look for those places to quickly add that value. In this discovery phase, you work backwards with the discovery exercise for all the requirements from all your major stakeholders to ensure that no voice is left out. And this is a good phase to do a proof of concept or pilot to learn and explore Amazon Connect. As a customer, you have access to your AWS account teams and Connect specialized sellers that can also guide you through this phase. Once you develop a plan to have your ideal experience for your call center, the next migration phase is the technology foundation phase and this is one of the most important phases that customers should implement. Because there's no infrastructure to manage with Amazon Connect, you can focus on buildin' a foundational framework to iterate on right away. And this lack of infrastructure build might be what makes an Amazon Connect migration the most unique because there's no waitin' around for someone to stand up servers or install software. So you might then start with an initial call center flow or a chat bot experience to make for really great first demos and to get all of your stakeholders excited and engaged. As a final note here as you go through this phase, don't forget to create a playbook for the next stage of migration. You wanna keep those lessons learned. The process is to create designs, any notes on obstacles you overcame or any other valuable information to allow you to accelerate the migration of the next group onto Amazon Connect. Finally after a successful first discovery and tech foundation phase, you have the launch phase and the innovation phase. With the launch phase, you're ready to move on to even more groups or bigger feature sets. Now you have those lessons learned from the previous phase and a playbook to get started, you're ready to tackle more migrations. It's great at this spot, for example, to train your IT team on how to migrate and successfully onboard your Amazon Connect users. If you're working with an IT operations team, you have them come alongside and use the playbook to begin to migrate all the groups in parallel. In the innovate phase, agile delivery becomes a foundation for ongoing contact center innovation to better service your customers. With Amazon Connect, you get a neverending cycle of opportunities to not just migrate new groups but also continuously improve those that have already migrated as they decide to add new features or add new capabilities that come online in Amazon Connect. So this is an Amazon Connect customer migration story with Priceline. If you're not familiar with Priceline, Priceline.com is an online travel agency for findin' discount rates for travel-related purchases such as airline tickets and hotel stays. Priceline director of contact center technology, Jennifer Featherling stated that they moved over 1,000 call center agents from office to work-from-home with Amazon Connect to be able to cope with the pandemic. With Amazon Connect, Priceline was better prepared to provide superior customer service and quickly make adjustments when needed. These are additional training resources for Amazon Connect that are available online. We talked about one group of your remote work users which are virtual contact centers for your remote call center agents. Now let's take a look at collaboration toolin' for your remote workers which is enabled with Amazon Chime. You can embed audio and video into your application as a collaboration tool using the Amazon Chime SDK. In fact, much of the same audio and video technology available in the SDK is used in the Amazon Chime meetings app. And this is the same app that you probably used for meetings with AWS teams, leaders and technologists throughout re:Invent. Before we dive deeper into how the SDK works, it's worth spendin' just a couple of minutes on why we built the Amazon Chime SDK. The reality is that audio and video technology can be pretty complex. It relies on multiple integrated standards and technologies. And as builders, you have to plan for communications that can traverse all network conditions while still offering an excellent end-user experience. You have to provide applications for your users that can be used from a laptop, a mobile device or sometimes even a regular phone. All of these requirements mean that there's development overhead, operational complexity and the extensibility of application may be limited when you're building from the ground up. So why use the Amazon Chime SDK to build real-time communications to your applications? By usin' the Chime SDK, you can build faster letting your teams focus on deployment of web RTC technology while you focus on buildin' out your remote end-user experiences. You can take advantage of the Amazon Chime global network with communication services for audio callin', video callin' or screen sharin' features, all available in 18 AWS regions without any additional infrastructure investment. This allows you to just focus on your application and your users. The Amazon Chime SDK can scale up or down with no additional work and it's available across desktop and mobile clients with Android and iOS clients. By using Amazon Chime SDK, you're buildin' on a solid AWS foundation with the ability to extend your apps with capabilities from AWS AI/ML services like Transcribe and Comprehend. So when Amazon Chime SDK was launched, it was essentially made up of three parts: the JavaScript client SDK, the AWS SDK and the media services. At a high level, here is how Amazon Chime SDK works to integrate audio and video capabilities into your application. You start out by use of the AWS SDK with Lambda in your server-side application to create media resources in one of the supported AWS regions. In response, you receive a media resource and a set of media URLs that represent the Amazon Chime media services that are used to host the meetin'. Your server-side application can then authenticate and authorize each user joining the meetin' session and create a corresponding attending resource by using a unique identifier from your identity system. Each attendee of the meetin' is assigned a unique joint token that your server application will securely send back to the client application. The client application uses a combination of secure web sockets and DTLS through web RTC peer connections to send and receive media to and from other attendees usin' the media services. So the Amazon Chime SDK tech takes the guesswork out of addin' real-time communication components to your applications. Now let's take a look at Amazon Chime SDK for messagin'. Amazon Chime SDK also supports highly-scalable persistent messagin' in the Amazon Chime SDK to build chat and other real-time messagin' features. There are several Chime APIs for messagin' and these APIs are combined with the Amazon Chime SDKs we just saw in the previous slide so developers don't have to worry about buildin' and scalin' your own infrastructure for messagin'. The messagin' features can be used alongside with existin' audio, video and content sharing capabilities of the Amazon Chime SDK. And messaging can also be used separately if you choose not to integrate it with video and audio. You can use it in delivery applications of broadcasts because you can allow up to 100,000 members per channel. Here's a quick overview of how the Amazon Chime SDK messagin' works. One user on a client side application is connected to a web socket provided by Amazon Chime. This user is member of a channel along with up to 100,000 other users who are also connected to an active web socket on your client. When the sender sends the message, the client sends a sent channel message API in the AWS SDK and this message and its metadata are persisted by the Amazon Chime SDK and then fanned out to the recipients. If the recipient does not have a channel open, they can be notified that new messages are available in the channel. And if they're not connected, their client will retrieve the message from history the next time the user connects and loads the messages. Developers can enable sendin' of attachments usin' Amazon S3 or their choice of file storage and attach a link to the file in the message metadata. Developers also have the option of turnin' on streaming export of chat messages through Amazon Kinesis. And this export feature can be used to integrate with services like Amazon Kendra for search or services like Amazon Comprehend to detect sensitive data or profanity which they can be redacted or archived. Amazon Chime SDK messagin' is designed to be highly flexible so that you can achieve the exact experience that you need. I'd like to share with you an Amazon Chime customer migration story with Cerner Corporation. So Cerner is a healthcare IT company that specializes in electronic medical records. The company used the Amazon Chime SDK to rapidly deploy and scale telehealth solutions durin' the COVID-19 global health crisis and this solution helped them bring doctors and patients together in the midst of a global health crisis. With Amazon Chime SDK, they leverage and manage service with Amazon Chime that can support their clients dynamic usage patterns. Here are some additional resources for you to learn more about the Amazon Chime SDK. Now I'll hand it over to my co-presenter John Walker to talk about additional remote workforce solutions, professional desktops, application streaming and will architect with best practices. Thank you, Jennifer, so much for leading us through some of those remote workforce solutions for migration. Next, we're going to talk about Amazon WorkSpaces. Amazon WorkSpaces is a managed and secure desktop as a service solution. It helps mobile and remote employees access the applications they need from anywhere by delivering a full cloud desktop solution. So what are some of the challenges that we see for remote workers? The modern approach to work really presents challenges for IT. They need to support many different device types, maintain legacy applications while also building next-generation capabilities and all of this while providing an easy experience for their employees and ensuring corporate applications and data are secure, then they also need to drive down cost. Unfortunately, the traditional approaches to supporting end users are falling short. First, many customers are telling us that they've tried traditional VDI and other on-prem infrastructure solutions. With traditional VDI solutions the IT administrators tell us, they're forced to guess at annual demand and to buy hardware for peak needs and this typically results in overbuying. It can take weeks or months to complete the ongoing maintenance and infrastructure and onboarding of those new devices and this can be a real and hard problem. And IT organizations are often caught by surprise when new projects or new groups need to be onboarded and come online. That results in the need to purchase or upgrade hardware and can delay those users coming online. Second, customers tell us that their users are asking for BYOD or bring your own device type solutions with Macs and Chromebooks. It makes it challenging to securely manage and deliver applications across multiple hardware, operating system and software configurations. While many customers have moved their data to the cloud, their desktop applications remain on-premises on user devices. This increases latency and it makes users less productive as they move data to and from the cloud and to and from their applications. Today, customers also use GPU or graphics processing units-enabled laptops in order to run CAD applications like AutoCAD and Siemens NX. So on average, these devices can cost more than $5,000 US and we had received feedback from customers that they would like to deliver these applications on commodity hardware or reduce their hardware cost and let the workers work from any device. And customers are increasingly trying to support global workforces. It's challenging to distribute those solutions and to estimate demand for solutions across many different physical locations and operating physical device VDI deployments in multiple data centers. Customers also tell that security is the key requirement and a top priority for them. So as organizations become more agile, how do we protect those corporate assets without choking off employee productivity or reducing business agility? It's the reason that AWS and Amazon have created Amazon WorkSpaces. Really this is about simplifying the desktop delivery. Amazon WorkSpaces helps you to eliminate many administrative tasks associated with managing your desktop lifecycle including provisioning, deploying, maintaining and recycling desktops. There's less hardware inventory to manage and no need for complex virtual desktop infrastructure deployments that don't scale. So we also wanna keep that data secure. Amazon WorkSpaces is deployed within your Amazon Virtual Private Cloud or VPC to provide each user with access to persistent encrypted storage volumes in the AWS cloud and integrate with AWS Key Management Service or KMS in order to provide the secure storage of those cryptography keys. No user data's stored on the local device and it helps improve the security of your data and reduces your overall risk surface area. In addition, this is centrally managed and scales your global desktop deployment as your needs dictate. Amazon WorkSpaces is available in 13 different AWS regions and provides access to high-performance cloud desktops wherever your teams get work done. You can manage a global deployment of many thousands of WorkSpaces from the AWS console and you get to rapidly provision and deprovision those desktops as the needs of your workforce change. All of this while reducing cost, WorkSpaces eliminates the need for overbuy of desktop and laptop resources by providing on-demand access to cloud desktops that include a range of compute, memory, storage and graphics resources needs to meet your users' performance needs. Okay, so we've spoken about what WorkSpaces is and what user problems this solves for our customers. Next, let's take a look at Amazon WorkSpaces target architecture. So have a look at the design here. This is a fully-managed solution, but you control the networking with your private subnets. The WorkSpaces are going to deploy elastic network interfaces or ENIs and you get to control what data comes in to and goes out of those WorkSpaces. So we have a fully-managed solution. The data isolation and protection is there for your security. And then with scalability, you're able to turn on multiple WorkSpaces in minutes and deploy them to your subnets. And with cost controls using an option of the AlwaysOn or AutoStop, you're able to really control and dial in how many WorkSpaces resources you need to be able to allocate for your users. All right, so we talked about a target architecture. We talked about which problems we're trying to solve. Now let's talk about the migration. So migrating your desktop to WorkSpaces really consists of the build out phase, the migration phase and operations. So during build out, what we want to make sure that we do is to decide what your identity solution is going to be. If you're standing up brand-new sets of users, you can use a simple AD in order to implement your identity provider. So AD stands for Active Directory. You can use AWS' managed Active Directory or you can use an AD connector in order to connect back to a directory service that exists on-premises, in a data center or in another cloud. You also want to decide your networking solutions. So with networking, you want to lay out your network access. If you have AD Connector, it's going to need AD access so make sure that you got the open ports back to that active directory and probably set in place a virtual private network or VPN connection there. Inside of that security group for your subnet, make sure that you open up the ports to the services that your users need to access. So if that's databases or if it's accessing special TCP ports, make sure you open those up so your users can access exactly the services that they need. All right, now that we've set up the networking, we've set up the identity and we're able to bring over your users' identities in order to authenticate into WorkSpaces, now it's time for you to do the image creation. So during image creation, you'll first launch a workspace and configure it. So use our images in order to create your bundle for your workspace. You can start with a Value image all the way up to PowerPro images and choose one of these images per high-level use case for your users. So consider your different user personas and which users you want to deploy this to. Once you create your image, go ahead and minimize the number of images by using WorkSpaces Application Manager, WAM which is going to be able to package additional applications to deploy whenever a user logs into their workspace. All right, so other distribution package types also work the way that you're already used to distributing applications onto your desktop solutions. Create that image from the workspace and bundle the image with a correct hardware type. You can also use BYOL or bring your own license with Windows 10 desktop licenses. Okay, then you're gonna launch your WorkSpaces. Whenever you've launched your WorkSpaces, next you wanna figure out which users you're going to bring to bear here. So the user selection is going to be proof of concept users or opt-in groups. Often this is consultants or I find users are looking at outsourced work or contingent work that's seasonal and go ahead and turn those on as your first-use cases, then move into other user groups as your needs see fit. Then you want to use correct WorkSpaces sizing. So evaluate memory optimize, CPU optimize, GPU optimize sizing bundles in order to correctly size your WorkSpaces and correctly size your spend. Next whenever you're migrating that information, you want to make sure that you can access the data that you already have. So what you can do is use Windows shares and/or your WorkDocs Drive in order to make sure that that data is there whenever a user logs into their workspace. Next, let's talk about operations. It's very important during operations to enable those users, so make sure that you're going to train the users and of the support desk in order to operate in a slightly new way with operating these remote WorkSpaces in the cloud. With fleet management, make sure that you're evaluating constantly and upgrading to larger bundles or downgrading to smaller bundles as your users' needs see fit and shift between that AlwaysOn and AutoStop in order to save a little bit of money. Terminate those unused WorkSpaces and you're increasing the value that you're getting out of WorkSpaces. Monitor those alarms and check on your best practices with health checks on network links and on Active Directory using Amazon CloudWatch and make sure that you're patching, updating and maintaining those WorkSpaces just as you would desktop solutions. All right. Next, let's talk a little bit about a customer's story. Amazon.com is an AWS customer. And at Amazon, we were able to burst scale our Amazon WorkSpaces environment in 1 1/2 weeks going from 25,000 running instances to near 300,000 running instances across eight different regions. So look at that timeline just 1 1/2 weeks. And whenever you look at the scale going from 25,000 to 300,000 running instances, that's phenomenal agility that you have at your fingertips. Okay, for a few resources here, you can go over to aws.amazon.com/workspaces and aws.training in order to get access to more WorkSpaces information and in order to get access to some training for Amazon WorkSpaces. And we heard a little bit about Amazon WorkSpaces which is a persistent desktop solution in the cloud. And now I'm going to talk to you about Amazon AppStream 2.0 which is a fully-managed non-persistent desktop and application service for remotely accessing your work. So what are some of the challenges that we see for IT to meet end user needs that Amazon AppStream 2.0 fills? So this is a modern approach to work that presents some challenges to IT. First, we need to make sure that we improve the user experiences of applications all while being able to deliver applications that have become increasingly complicated for application delivery. So whenever you think about being able to deliver an application to a Mac, to a Chromebook, to a Windows computer and being able to do that on assets that may not be inside of a corporate computer deployment. Instead, it may be taken home to someone's home office or to be sitting on someone's kitchen table. Being able to deliver those applications to those users has become increasingly complex as users choose remote working styles. In addition, we still need to have that at the primary forefront of IT users' needs to improve the security of applications while letting those users work remotely. In addition, IT are telling us that they are needing to scale their workforce globally. So being able to provide those same solutions with a consistent application experience, being able to improve the efficiency with which we're delivering the applications, improve the security and be able to scale globally is a real and hard problem. So this is what Amazon AppStream 2.0 is created for. AWS apps and desktop as a service delivers persistent and non-persistent virtualized Windows apps and desktops as fully managed cloud services at scale. And Amazon AppStream 2.0 is a fully-managed application streaming service that allows your remote workers or students to access the applications they need on any computer whether they're in the classroom, the library, a cafe or at home. And so what we see is real improvement of the end-user experience by being able to stream non-persistent desktops and apps. And the architecture here contrasted with WorkSpaces is a non-persistent by-design architecture. This is going to be able to integrate with existing IT storage and identity management solutions. And the approach is really to be able to deliver a fully-managed service and be able to deploy this at scale globally with pay-as-you-go pricing. All right. Next, let's take a look at the target architecture. So the target architecture for this is really going to solve for those same problem sets that we saw IT and users are needing to solve. So for communications, those communications between applications and the data that exists in the cloud are now going to be brought together. So your data will be delivered inside of the AWS cloud, inside of the region that you've chosen, in your availability zones and your VPCs. Similar to WorkSpaces, Amazon AppStream is going to be able to deploy your AppStream 2.0 elastic network interfaces or ENIs inside of your private subnets in your VPC. And then on top of that, you'll be able to get automatic provisioning with application auto-scaling. This is going to be able to automatically scale your applications as user needs increase and scale them back in importantly whenever your users' needs decrease. Then for operations, we have AppStream 2.0 fleet images and this is going to be able to optimize what your operations and IT team needs to do. So if you need to say update an AppStream 2.0 image because a new patch came in for the application or a new patch came in for the underlying operating system, all you have to do is update one image and then it's available to all users of that fleet as you deploy that for usage. It's a phenomenally streamlined ability to update your fleet and get those updates rolled out to everyone all at once. As your users log in to their AppStream 2.0 streaming applications, they're going to be able to save their data and have it available to them whenever they log back in, whenever they use that application for the next time by taking advantage of user home folders. That can be deployed in Amazon S3. In addition, you can bring your own cloud drive if you so wish and configure this to connect into your Amazon AppStream 2.0. In addition, whenever you change settings and set them up for your baseline fleet image, everyone's going to get the same default application settings. But if a user's able to change those application settings, likewise those are going to be stored in an Amazon S3 bucket so that application login over login the users get a consistent usability for the applications they're using. All right, so we talked about what the target architecture looks like. Let's talk about migrating your applications to AppStream 2.0. And really first, I wanna give you an idea of what some of these are, some of the example applications that I see users have success with or for using a security bastion host. Maybe you got a remote desktop solution that you're logging in to to perform secure actions in your cloud. A security bastion host, it's also called a jumpbox. You can have these set up in a way that is non-persistent so that as the user needs it, that AppStream service is available to log in to the device, do the security work, be able to log off and have that go away so it's no longer an IP address that's deployed in your VPC and it's no longer a target, right? Because it has those security tools on it, it's only there as you need it as you need to use it. We also see this for 3D engineering: SOLIDWORKS, AutoCAD, Siemens NX and more, being able to use graphics-intensive processes and being able to get access to that hardware in the cloud without the need to provision that heavy GPU-intensive application hardware on users' devices themselves. So there's an easy app import through the AWS Management Console. Just launch an image builder, connect and install your applications, configure them for the default settings that you need and then set those Windows settings you want your users to have. Then you're going to launch this and optimize it to make sure that your performance is great, exactly what your users need and test out the application experience and save it. Once you save that image, you can use it for your fleets. Assign it to your fleets according to those user personas that we spoke about before. And with AppStream 2.0, that agent software that is on those remote systems can be managed for you. There's no need for you to manage that yourself. So that's an easy way to migrate to the Amazon AppStream 2.0. Let's talk about a customer story. This is Samsung Engineering and they had construction sites and partners that are located all over the world including North and Central America, Asia, the Middle East and Europe. And Jeong Hoon Lee, the senior engineer at Samsung engineering said that they were able to save 20% of the cost of purchasing and maintaining on-premises design infrastructure and they were able to actually improve the efficiency of their personnel to where only one person needs to manage the system. And they had additional benefits. So in addition to saving 20%, they were able to speed up their deployment from months to days and reduce the support staff from four to one and enable greater customer collaboration. So as they were able to bring on users in different regions, deploying them in each region where they operated once required them to source, deploy, manage complex and costly on-premises infrastructure for each project. In addition, there were issues with latency that made it difficult for them to be able to bring partners and customers in the project workflow. So for those reasons, Samsung Engineering decided to move its design suite into Amazon AppStream 2.0. And using AppStream 2.0, they were able to virtualize their solutions while providing a fluid, low-latency experience accessible via web browser and be able to bring in new users independent of where they were located. For some additional AppStream 2.0 resources, take a look at aws.amazon.com/appstream2 to learn more about AppStream. And for training on AppStream 2.0, go over to aws.training. All right, so we looked a little bit at four different solutions and four different migration patterns for remote workforce. Now let's do some consideration of the Well-Architected Framework. With the AWS Well-Architected Framework, it helps cloud architects build secure, high-performing, resilient and efficient infrastructure for the applications and workloads. Based on five pillars: operational excellence, security, reliability, performance efficiency and cost optimization, the AWS Well-Architected Framework provides a consistent approach for customers and partners to evaluate these architectures and implement designs that can scale over time. So first, let's have a consideration of reliability. With reliability, one thing I wanna focus in on and we're just gonna do one per pillar here is make sure that you're going to manage your quotas. So each AWS service does have a quota. There are soft quotas and hard quotas that exist for each service. As you near quotas, make sure that you're paying attention to the needs of your users and you can go ahead and provision new quota increases with the service quota tool inside of the AWS console or you can open a support ticket using the support resource in the AWS console in the upper right corner. So with Connect, you can pay attention to Connect instances per account. With AppStream 2.0, pay attention to the number of your fleet instances. And with WorkSpaces, take a look at the number of workspace image types and bundles that you're actually utilizing and keep track of those with CloudWatch alerts. Next, let's take a look at security. And what you wanna do with security is to plan in advance the different personas or user types and how they're going to identify to the system. So pay attention to your identity management system and the credentials they'll use with your onboarding and offboarding and decide in advance what your identity provider will be and use AWS documentation for setup and best practices in order to identify those users and further access control. Next, let's talk about performance efficiency. And again, there's a bit of a focus on users. For users and agents. make sure to pay attention to their enablement. Train your users, your contact center agents and your support personnel how to use these services in order to optimize the value that you and your teams get from migrating to end-user computing on AWS. Next, we'll talk about operational excellence. For operational excellence, pay attention to change management. For incremental changes that you're going to enforce, try to put in place good governance with change management. For updating or configuring contact flows with Connect, for instance, make sure you're keeping track of and using change management. Follow annd update and rollback process to make sure that you're streamlining clean change management procedures. With AppStream, for instance, create new images and test them with updates and new applications before rolling them out to your fleets and also to optimize the amount of performance that your users are going to get out of 'em. So there's kind of a two-fer there with performance efficiency and operational excellence by employing change management here. Next for cost optimization, make sure and take a look at the self-service options for each of the services that we've discussed today evolving beyond the on-premise model of over-provisioning and overpaying. Instead, you can take a look at on-demand service technology capabilities in order to enable access to the resources users need at the time that they need them. For instance, being able to provision a workspace by user, changing that over to an on-demand as opposed to an upfront provisioning system. This can save you and your users significant cost and time. All right, we've talked about the Well-Architected Framework and a key consideration for each. And in summary, we've spoken about Amazon Connect before being able to enable businesses to have a fully-operational contact center. We've spoken about Amazon Chime that lets you meet, chat and place business phone calls with a single secure application from anywhere. We've spoken about Amazon WorkSpaces as a managed secure desktop as a service solution in the cloud and Amazon AppStream 2.0 as a fully-managed application streaming service. And as you migrate to these, I wish you the best of success. Thank you all so much for listening to Jennifer and me to describe these four different solutions that Amazon and AWS are providing for remote workforce solutions and the design for remote workforce solution migration patterns. We wish you the best of luck implementing them and have a wonderful day. (smooth rhythmic music)

## Subtitles with Timestamps

[00:00](https://www.youtube.com/watch?v=9G84a9IjpXk&t=0s) (smooth rhythmic music)

[00:10](https://www.youtube.com/watch?v=9G84a9IjpXk&t=10s) Welcome everyone to session ARC 205

[00:14](https://www.youtube.com/watch?v=9G84a9IjpXk&t=14s) on remote workforce cloud migration patterns.

[00:17](https://www.youtube.com/watch?v=9G84a9IjpXk&t=17s) I'm Jennifer Ihejimba, the solutions architect at AWS.

[00:20](https://www.youtube.com/watch?v=9G84a9IjpXk&t=20s) With me on this session is John Walker,

[00:23](https://www.youtube.com/watch?v=9G84a9IjpXk&t=23s) also a solutions architect at AWS.

[00:25](https://www.youtube.com/watch?v=9G84a9IjpXk&t=25s) We're excited to be joining you today from our home offices

[00:28](https://www.youtube.com/watch?v=9G84a9IjpXk&t=28s) to talk to you about major solutions

[00:31](https://www.youtube.com/watch?v=9G84a9IjpXk&t=31s) for your remote workforce

[00:32](https://www.youtube.com/watch?v=9G84a9IjpXk&t=32s) and how to migrate these solutions to AWS.

[00:35](https://www.youtube.com/watch?v=9G84a9IjpXk&t=35s) We know that you probably joined today's session

[00:38](https://www.youtube.com/watch?v=9G84a9IjpXk&t=38s) to learn about remote workforce cloud migration patterns

[00:41](https://www.youtube.com/watch?v=9G84a9IjpXk&t=41s) and we promise you won't be disappointed.

[00:44](https://www.youtube.com/watch?v=9G84a9IjpXk&t=44s) John and I are both part

[00:45](https://www.youtube.com/watch?v=9G84a9IjpXk&t=45s) of a small and medium business segment in AWS.

[00:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=48s) More than 50% of our work deals with migrating workloads

[00:52](https://www.youtube.com/watch?v=9G84a9IjpXk&t=52s) and very often, we're talkin' to different customers

[00:54](https://www.youtube.com/watch?v=9G84a9IjpXk&t=54s) about migrating their remote workforce solutions

[00:58](https://www.youtube.com/watch?v=9G84a9IjpXk&t=58s) from on-premises to AWS.

[01:01](https://www.youtube.com/watch?v=9G84a9IjpXk&t=61s) So let's get started.

[01:05](https://www.youtube.com/watch?v=9G84a9IjpXk&t=65s) So if you think about how many organizations

[01:08](https://www.youtube.com/watch?v=9G84a9IjpXk&t=68s) have had to switch to workin' remotely

[01:10](https://www.youtube.com/watch?v=9G84a9IjpXk&t=70s) in the past year or two, many fall into that category.

[01:15](https://www.youtube.com/watch?v=9G84a9IjpXk&t=75s) The workforce has been changin' for a while

[01:17](https://www.youtube.com/watch?v=9G84a9IjpXk&t=77s) and recent events have only accelerated those changes.

[01:20](https://www.youtube.com/watch?v=9G84a9IjpXk&t=80s) For example before the pandemic,

[01:24](https://www.youtube.com/watch?v=9G84a9IjpXk&t=84s) one in five jobs in the US was held by contractors

[01:28](https://www.youtube.com/watch?v=9G84a9IjpXk&t=88s) and 70% of users globally

[01:30](https://www.youtube.com/watch?v=9G84a9IjpXk&t=90s) were already workin' remotely at least one day a week.

[01:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=94s) Deloitte's annual activity report

[01:36](https://www.youtube.com/watch?v=9G84a9IjpXk&t=96s) at global mergers and acquisitions also show

[01:39](https://www.youtube.com/watch?v=9G84a9IjpXk&t=99s) that 79% of organizations expect to increase M&A in 2020.

[01:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=106s) So if you take a look at these long-term trends,

[01:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=108s) it's more important than ever

[01:50](https://www.youtube.com/watch?v=9G84a9IjpXk&t=110s) to start planning your workforce transformation,

[01:53](https://www.youtube.com/watch?v=9G84a9IjpXk&t=113s) to deliver solutions for your remote staff

[01:55](https://www.youtube.com/watch?v=9G84a9IjpXk&t=115s) and to ensure that you enable agility,

[01:58](https://www.youtube.com/watch?v=9G84a9IjpXk&t=118s) continuity and security for your remote workforce.

[02:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=122s) So in essence, what we see

[02:04](https://www.youtube.com/watch?v=9G84a9IjpXk&t=124s) is that this could create some challenges

[02:06](https://www.youtube.com/watch?v=9G84a9IjpXk&t=126s) for your entire organization,

[02:07](https://www.youtube.com/watch?v=9G84a9IjpXk&t=127s) whether that means you have call center agents

[02:10](https://www.youtube.com/watch?v=9G84a9IjpXk&t=130s) that can no longer go into the physical contact center

[02:13](https://www.youtube.com/watch?v=9G84a9IjpXk&t=133s) but still need to support customers remotely

[02:16](https://www.youtube.com/watch?v=9G84a9IjpXk&t=136s) or maybe you have employees

[02:18](https://www.youtube.com/watch?v=9G84a9IjpXk&t=138s) that need to remotely communicate

[02:20](https://www.youtube.com/watch?v=9G84a9IjpXk&t=140s) and collaborate your chat or messagin' solutions

[02:23](https://www.youtube.com/watch?v=9G84a9IjpXk&t=143s) with each other to remain productive and feel connected.

[02:27](https://www.youtube.com/watch?v=9G84a9IjpXk&t=147s) Your employees may also need to use

[02:29](https://www.youtube.com/watch?v=9G84a9IjpXk&t=149s) virtual desktops or streamin' applications

[02:31](https://www.youtube.com/watch?v=9G84a9IjpXk&t=151s) without the need for PCs or laptops.

[02:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=154s) With all of these in mind,

[02:36](https://www.youtube.com/watch?v=9G84a9IjpXk&t=156s) we thought we'd share with you today

[02:38](https://www.youtube.com/watch?v=9G84a9IjpXk&t=158s) four major remote workforce solutions

[02:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=160s) under key migration architecture patents,

[02:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=163s) whether that's your call center agents,

[02:45](https://www.youtube.com/watch?v=9G84a9IjpXk&t=165s) employees or students and educators.

[02:50](https://www.youtube.com/watch?v=9G84a9IjpXk&t=170s) Here are the key takeaways from this session.

[02:53](https://www.youtube.com/watch?v=9G84a9IjpXk&t=173s) We'll cover four main remote workforce solutions.

[02:56](https://www.youtube.com/watch?v=9G84a9IjpXk&t=176s) And for each remote workforce pattern,

[02:58](https://www.youtube.com/watch?v=9G84a9IjpXk&t=178s) we'll explore deployment paths and migration approach

[03:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=182s) usin' the AWS well-architected principles.

[03:05](https://www.youtube.com/watch?v=9G84a9IjpXk&t=185s) So keep in mind that this session is a 200-level talk today

[03:07](https://www.youtube.com/watch?v=9G84a9IjpXk&t=187s) in a sense that we're not going to dive deep

[03:10](https://www.youtube.com/watch?v=9G84a9IjpXk&t=190s) into the solution architectures,

[03:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=192s) but we are going to see some really cool stuff

[03:14](https://www.youtube.com/watch?v=9G84a9IjpXk&t=194s) about migration methodology and architecture best patterns.

[03:18](https://www.youtube.com/watch?v=9G84a9IjpXk&t=198s) We'll also cover customer examples

[03:21](https://www.youtube.com/watch?v=9G84a9IjpXk&t=201s) and share additional resources

[03:22](https://www.youtube.com/watch?v=9G84a9IjpXk&t=202s) as we explore each remote workforce solution.

[03:27](https://www.youtube.com/watch?v=9G84a9IjpXk&t=207s) AWS offers several services

[03:30](https://www.youtube.com/watch?v=9G84a9IjpXk&t=210s) to enable remote work and learnin'

[03:32](https://www.youtube.com/watch?v=9G84a9IjpXk&t=212s) and these are full solutions we'll be talkin' about today.

[03:35](https://www.youtube.com/watch?v=9G84a9IjpXk&t=215s) We'll talk about Amazon Connect which enables businesses

[03:38](https://www.youtube.com/watch?v=9G84a9IjpXk&t=218s) to have a fully-operational contact center

[03:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=220s) that can be operated virtually anywhere.

[03:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=223s) With Amazon Connect, you can have your agents,

[03:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=226s) your supervisors, your managers and administrators

[03:49](https://www.youtube.com/watch?v=9G84a9IjpXk&t=229s) work from home and still be able to perform

[03:52](https://www.youtube.com/watch?v=9G84a9IjpXk&t=232s) all their normal contact center activities.

[03:55](https://www.youtube.com/watch?v=9G84a9IjpXk&t=235s) We also have Amazon Chime,

[03:57](https://www.youtube.com/watch?v=9G84a9IjpXk&t=237s) a collaboration tool that can enable your employees

[04:00](https://www.youtube.com/watch?v=9G84a9IjpXk&t=240s) to meet, to chat and place business calls

[04:03](https://www.youtube.com/watch?v=9G84a9IjpXk&t=243s) with a single secure application from anywhere.

[04:06](https://www.youtube.com/watch?v=9G84a9IjpXk&t=246s) So they're able to collaborate

[04:07](https://www.youtube.com/watch?v=9G84a9IjpXk&t=247s) and instantly go from chat to a call,

[04:10](https://www.youtube.com/watch?v=9G84a9IjpXk&t=250s) they can share their screen

[04:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=252s) and invite more people to join their meetin'

[04:14](https://www.youtube.com/watch?v=9G84a9IjpXk&t=254s) all within the same application with Amazon Chime SDKs.

[04:18](https://www.youtube.com/watch?v=9G84a9IjpXk&t=258s) There's also Amazon WorkSpaces,

[04:20](https://www.youtube.com/watch?v=9G84a9IjpXk&t=260s) a managed secure desktop as a service solution

[04:23](https://www.youtube.com/watch?v=9G84a9IjpXk&t=263s) that helps mobile and remote employees

[04:25](https://www.youtube.com/watch?v=9G84a9IjpXk&t=265s) access applications they need

[04:27](https://www.youtube.com/watch?v=9G84a9IjpXk&t=267s) by deliverin' a cloud desktop that's accessible anywhere

[04:31](https://www.youtube.com/watch?v=9G84a9IjpXk&t=271s) with an internet connection usin' any supported device.

[04:35](https://www.youtube.com/watch?v=9G84a9IjpXk&t=275s) And lastly, Amazon AppStream 2.0

[04:38](https://www.youtube.com/watch?v=9G84a9IjpXk&t=278s) which is a fully-managed application streaming service.

[04:41](https://www.youtube.com/watch?v=9G84a9IjpXk&t=281s) With Amazon AppStream 2.0, your remote workers or students

[04:45](https://www.youtube.com/watch?v=9G84a9IjpXk&t=285s) can access desktop applications they need at anytime.

[04:49](https://www.youtube.com/watch?v=9G84a9IjpXk&t=289s) We'll get a chance to discuss

[04:51](https://www.youtube.com/watch?v=9G84a9IjpXk&t=291s) all four services durin' this session.

[04:56](https://www.youtube.com/watch?v=9G84a9IjpXk&t=296s) So let's kick off with the first AWS remote work solution

[04:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=299s) with Amazon Connect for virtual contact centers.

[05:05](https://www.youtube.com/watch?v=9G84a9IjpXk&t=305s) CEOs state overwhelmingly

[05:07](https://www.youtube.com/watch?v=9G84a9IjpXk&t=307s) that more than any other element of your business

[05:10](https://www.youtube.com/watch?v=9G84a9IjpXk&t=310s) customer experience is the most effective method

[05:13](https://www.youtube.com/watch?v=9G84a9IjpXk&t=313s) for creatin' a competitive advantage.

[05:16](https://www.youtube.com/watch?v=9G84a9IjpXk&t=316s) But one area where many costs companies continue to struggle

[05:21](https://www.youtube.com/watch?v=9G84a9IjpXk&t=321s) to deliver similarly delightful customer experiences

[05:25](https://www.youtube.com/watch?v=9G84a9IjpXk&t=325s) is within their contact center.

[05:27](https://www.youtube.com/watch?v=9G84a9IjpXk&t=327s) Here, we see some common contact center challenges

[05:30](https://www.youtube.com/watch?v=9G84a9IjpXk&t=330s) which are also migration triggers.

[05:33](https://www.youtube.com/watch?v=9G84a9IjpXk&t=333s) What you see here answers the question

[05:35](https://www.youtube.com/watch?v=9G84a9IjpXk&t=335s) why customers are migratin'.

[05:38](https://www.youtube.com/watch?v=9G84a9IjpXk&t=338s) So why are customers migratin'?

[05:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=340s) Last year, we commissioned Forrester Research

[05:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=343s) to perform an independent study of customers

[05:45](https://www.youtube.com/watch?v=9G84a9IjpXk&t=345s) who migrated to Amazon Connect

[05:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=348s) across all sizes and segments.

[05:50](https://www.youtube.com/watch?v=9G84a9IjpXk&t=350s) The study revealed this set of common challenges

[05:53](https://www.youtube.com/watch?v=9G84a9IjpXk&t=353s) customers were facin'

[05:55](https://www.youtube.com/watch?v=9G84a9IjpXk&t=355s) with your previous contact center systems

[05:57](https://www.youtube.com/watch?v=9G84a9IjpXk&t=357s) makin' it impossible for them

[05:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=359s) to deliver innovative contact center experiences

[06:01](https://www.youtube.com/watch?v=9G84a9IjpXk&t=361s) to their customers.

[06:03](https://www.youtube.com/watch?v=9G84a9IjpXk&t=363s) One of the challenges they had was

[06:05](https://www.youtube.com/watch?v=9G84a9IjpXk&t=365s) havin' expensive legacy solutions.

[06:08](https://www.youtube.com/watch?v=9G84a9IjpXk&t=368s) They had complex pricin' and very large upfront costs.

[06:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=372s) Challengin' vendor relationships was another challenge

[06:15](https://www.youtube.com/watch?v=9G84a9IjpXk&t=375s) with lack of trust, misleading fees

[06:18](https://www.youtube.com/watch?v=9G84a9IjpXk&t=378s) and overall slow development cycles

[06:21](https://www.youtube.com/watch?v=9G84a9IjpXk&t=381s) with an inability to scale up or down easily,

[06:25](https://www.youtube.com/watch?v=9G84a9IjpXk&t=385s) but sometimes just being difficult to do that.

[06:27](https://www.youtube.com/watch?v=9G84a9IjpXk&t=387s) There were also painful frequent outages

[06:30](https://www.youtube.com/watch?v=9G84a9IjpXk&t=390s) that cause lapses in service, lost revenue,

[06:33](https://www.youtube.com/watch?v=9G84a9IjpXk&t=393s) wasted agent labor and excessive troubleshooting.

[06:37](https://www.youtube.com/watch?v=9G84a9IjpXk&t=397s) They were also unable to access powerful AI technologies

[06:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=400s) which were just expensive and most times

[06:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=403s) had very difficult bolt-on integrations.

[06:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=406s) It was complex and expensive

[06:49](https://www.youtube.com/watch?v=9G84a9IjpXk&t=409s) to integrate to systems of records

[06:51](https://www.youtube.com/watch?v=9G84a9IjpXk&t=411s) are not possible at all within their legacy contact centers.

[06:56](https://www.youtube.com/watch?v=9G84a9IjpXk&t=416s) In addition to all of these challenges

[06:58](https://www.youtube.com/watch?v=9G84a9IjpXk&t=418s) for legacy or gen one contact centers,

[07:00](https://www.youtube.com/watch?v=9G84a9IjpXk&t=420s) think about all the operational costs

[07:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=422s) companies need to purchase or integrate systems

[07:05](https://www.youtube.com/watch?v=9G84a9IjpXk&t=425s) from multiple vendors with all of these governed

[07:08](https://www.youtube.com/watch?v=9G84a9IjpXk&t=428s) by licenses, hardware, telephony trunks

[07:11](https://www.youtube.com/watch?v=9G84a9IjpXk&t=431s) makin' it difficult and costly to implement and maintain.

[07:17](https://www.youtube.com/watch?v=9G84a9IjpXk&t=437s) And now I'm eager to share with you the origin story

[07:21](https://www.youtube.com/watch?v=9G84a9IjpXk&t=441s) of how Amazon came to market

[07:23](https://www.youtube.com/watch?v=9G84a9IjpXk&t=443s) with a simple-to-use omnichannel cloud

[07:25](https://www.youtube.com/watch?v=9G84a9IjpXk&t=445s) contact center offering called Amazon Connect.

[07:28](https://www.youtube.com/watch?v=9G84a9IjpXk&t=448s) If you've ever had to contact

[07:30](https://www.youtube.com/watch?v=9G84a9IjpXk&t=450s) Amazon customer support before,

[07:32](https://www.youtube.com/watch?v=9G84a9IjpXk&t=452s) you see how this gets interestin'.

[07:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=454s) At Amazon, we strive to be the Earth's

[07:37](https://www.youtube.com/watch?v=9G84a9IjpXk&t=457s) most customer-centric company

[07:39](https://www.youtube.com/watch?v=9G84a9IjpXk&t=459s) and the success of our future as a company

[07:41](https://www.youtube.com/watch?v=9G84a9IjpXk&t=461s) was built on customer satisfaction.

[07:44](https://www.youtube.com/watch?v=9G84a9IjpXk&t=464s) About 12 years ago, our Amazon retail business

[07:47](https://www.youtube.com/watch?v=9G84a9IjpXk&t=467s) started to see enormous growth

[07:49](https://www.youtube.com/watch?v=9G84a9IjpXk&t=469s) and we were frustrated by all the challenges

[07:51](https://www.youtube.com/watch?v=9G84a9IjpXk&t=471s) of legacy contact centers we just talked about.

[07:54](https://www.youtube.com/watch?v=9G84a9IjpXk&t=474s) To do this, we needed the right tools

[07:56](https://www.youtube.com/watch?v=9G84a9IjpXk&t=476s) to enable exceptional customer experience of skill.

[07:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=479s) But every product we valued, it had fell short.

[08:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=482s) So essentially, we built a tool ourselves to use internally.

[08:06](https://www.youtube.com/watch?v=9G84a9IjpXk&t=486s) And in March of 2017 which was about three years ago,

[08:10](https://www.youtube.com/watch?v=9G84a9IjpXk&t=490s) we brought that internal tool to market

[08:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=492s) so that all the businesses within Amazon

[08:15](https://www.youtube.com/watch?v=9G84a9IjpXk&t=495s) could break free of the same challenges

[08:17](https://www.youtube.com/watch?v=9G84a9IjpXk&t=497s) they experience with contact centers.

[08:19](https://www.youtube.com/watch?v=9G84a9IjpXk&t=499s) Amazon Connect is a simple-to-use

[08:21](https://www.youtube.com/watch?v=9G84a9IjpXk&t=501s) cloud-based contact center we brought to market

[08:24](https://www.youtube.com/watch?v=9G84a9IjpXk&t=504s) to deliver exceptional omnichannel customer experiences

[08:28](https://www.youtube.com/watch?v=9G84a9IjpXk&t=508s) that are natural, dynamic and personalized.

[08:31](https://www.youtube.com/watch?v=9G84a9IjpXk&t=511s) And the secret sauce of Amazon Connect

[08:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=514s) is allowing you to integrate with a breadth of AWS services

[08:37](https://www.youtube.com/watch?v=9G84a9IjpXk&t=517s) to accelerate the creation

[08:38](https://www.youtube.com/watch?v=9G84a9IjpXk&t=518s) of personalized and dynamic experiences with Amazon Connect.

[08:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=523s) It includes all the standard functionality

[08:45](https://www.youtube.com/watch?v=9G84a9IjpXk&t=525s) contact center operations teams have come to expect.

[08:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=528s) Amazon Connect comes with skills-based routin'

[08:51](https://www.youtube.com/watch?v=9G84a9IjpXk&t=531s) which maximizes the efficiency of agents

[08:54](https://www.youtube.com/watch?v=9G84a9IjpXk&t=534s) and the satisfaction of end customers

[08:57](https://www.youtube.com/watch?v=9G84a9IjpXk&t=537s) and it also ensures that you connect the right customer

[08:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=539s) to the right agents at the right time.

[09:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=542s) Voice and chat interactions are recorded

[09:05](https://www.youtube.com/watch?v=9G84a9IjpXk&t=545s) makin' it easy to monitor and improve agent quality.

[09:10](https://www.youtube.com/watch?v=9G84a9IjpXk&t=550s) All the common reports analytics you would expect

[09:13](https://www.youtube.com/watch?v=9G84a9IjpXk&t=553s) are available and easy to use

[09:15](https://www.youtube.com/watch?v=9G84a9IjpXk&t=555s) including agent performance, service level and handle time.

[09:20](https://www.youtube.com/watch?v=9G84a9IjpXk&t=560s) Our customers often tell us

[09:21](https://www.youtube.com/watch?v=9G84a9IjpXk&t=561s) how much they love the audio quality for calls

[09:23](https://www.youtube.com/watch?v=9G84a9IjpXk&t=563s) with Amazon Connect.

[09:25](https://www.youtube.com/watch?v=9G84a9IjpXk&t=565s) And all you need to get started with Amazon Connect

[09:27](https://www.youtube.com/watch?v=9G84a9IjpXk&t=567s) is a standard broadband internet connection

[09:30](https://www.youtube.com/watch?v=9G84a9IjpXk&t=570s) and the only hardware you need is a USB headset.

[09:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=574s) Your agent can be located virtually anywhere

[09:36](https://www.youtube.com/watch?v=9G84a9IjpXk&t=576s) empowering businesses to offer increased flexibility

[09:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=580s) for work-from-home agents.

[09:44](https://www.youtube.com/watch?v=9G84a9IjpXk&t=584s) So now let's take a look at

[09:45](https://www.youtube.com/watch?v=9G84a9IjpXk&t=585s) some of the architectural deployment models

[09:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=588s) that we see for contact centers.

[09:51](https://www.youtube.com/watch?v=9G84a9IjpXk&t=591s) Here, we have an on-premises-based deployment

[09:53](https://www.youtube.com/watch?v=9G84a9IjpXk&t=593s) and these represent the majority

[09:56](https://www.youtube.com/watch?v=9G84a9IjpXk&t=596s) of existin' contact center infrastructure we see today.

[09:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=599s) You notice in the diagram how complex these typically are.

[10:03](https://www.youtube.com/watch?v=9G84a9IjpXk&t=603s) And in the picture,

[10:04](https://www.youtube.com/watch?v=9G84a9IjpXk&t=604s) all of the blocks represented on the screen

[10:06](https://www.youtube.com/watch?v=9G84a9IjpXk&t=606s) are actually physical devices.

[10:09](https://www.youtube.com/watch?v=9G84a9IjpXk&t=609s) In most circumstances, on-prem contact centers

[10:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=612s) typically stitch together solutions from various vendors

[10:15](https://www.youtube.com/watch?v=9G84a9IjpXk&t=615s) and they require numerous integrations

[10:18](https://www.youtube.com/watch?v=9G84a9IjpXk&t=618s) and frequently involve extensive and ongoing services.

[10:22](https://www.youtube.com/watch?v=9G84a9IjpXk&t=622s) In this setup sadly,

[10:23](https://www.youtube.com/watch?v=9G84a9IjpXk&t=623s) customers are locked into complex and expensive licensing

[10:26](https://www.youtube.com/watch?v=9G84a9IjpXk&t=626s) and maintenance contracts and they're also further bound

[10:30](https://www.youtube.com/watch?v=9G84a9IjpXk&t=630s) by the upfront expenditure of cost and hardware.

[10:33](https://www.youtube.com/watch?v=9G84a9IjpXk&t=633s) This makes it very difficult to adapt

[10:35](https://www.youtube.com/watch?v=9G84a9IjpXk&t=635s) if your contact center requirements are always changin'.

[10:38](https://www.youtube.com/watch?v=9G84a9IjpXk&t=638s) It also poses a challenge to spin up or spin down resources

[10:42](https://www.youtube.com/watch?v=9G84a9IjpXk&t=642s) should you choose to innovate or experiment

[10:45](https://www.youtube.com/watch?v=9G84a9IjpXk&t=645s) on customer experience in your contact center.

[10:50](https://www.youtube.com/watch?v=9G84a9IjpXk&t=650s) Here, we see the hybrid deployment model

[10:53](https://www.youtube.com/watch?v=9G84a9IjpXk&t=653s) and you notice in the picture here

[10:54](https://www.youtube.com/watch?v=9G84a9IjpXk&t=654s) that the core section is a cloud service

[10:57](https://www.youtube.com/watch?v=9G84a9IjpXk&t=657s) with additional onsite themes for localization.

[11:01](https://www.youtube.com/watch?v=9G84a9IjpXk&t=661s) The hybrid contact centers

[11:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=662s) most frequently use the cloud for storage,

[11:05](https://www.youtube.com/watch?v=9G84a9IjpXk&t=665s) interactive voice response or telephony distribution.

[11:08](https://www.youtube.com/watch?v=9G84a9IjpXk&t=668s) They commonly have a lot of one-off integrations

[11:11](https://www.youtube.com/watch?v=9G84a9IjpXk&t=671s) that need to be done

[11:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=672s) based on your contact center requirements.

[11:14](https://www.youtube.com/watch?v=9G84a9IjpXk&t=674s) One of the challenges with the hybrid deployments

[11:16](https://www.youtube.com/watch?v=9G84a9IjpXk&t=676s) is that it increases the anxiety

[11:18](https://www.youtube.com/watch?v=9G84a9IjpXk&t=678s) with some contact center companies that are security focused

[11:21](https://www.youtube.com/watch?v=9G84a9IjpXk&t=681s) because it increases the complexity

[11:23](https://www.youtube.com/watch?v=9G84a9IjpXk&t=683s) of your security posture.

[11:25](https://www.youtube.com/watch?v=9G84a9IjpXk&t=685s) Additionally, it doesn't usually address

[11:27](https://www.youtube.com/watch?v=9G84a9IjpXk&t=687s) the physical footprint,

[11:29](https://www.youtube.com/watch?v=9G84a9IjpXk&t=689s) the licensin', the infrastructure costs.

[11:31](https://www.youtube.com/watch?v=9G84a9IjpXk&t=691s) And at best, it just provides

[11:33](https://www.youtube.com/watch?v=9G84a9IjpXk&t=693s) a band-aid solution for scalability

[11:35](https://www.youtube.com/watch?v=9G84a9IjpXk&t=695s) by usin' a network interactive voice response.

[11:39](https://www.youtube.com/watch?v=9G84a9IjpXk&t=699s) There are also more opportunities

[11:41](https://www.youtube.com/watch?v=9G84a9IjpXk&t=701s) for support difficulties in mixed environments

[11:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=703s) because there's no clear ownership of a technical issue.

[11:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=706s) For example, the issue could be cloud team

[11:50](https://www.youtube.com/watch?v=9G84a9IjpXk&t=710s) versus the on-prem networking teams.

[11:55](https://www.youtube.com/watch?v=9G84a9IjpXk&t=715s) Here we see the cloud deployment model with Amazon Connect

[11:58](https://www.youtube.com/watch?v=9G84a9IjpXk&t=718s) and this model drastically reduces the complexity

[12:01](https://www.youtube.com/watch?v=9G84a9IjpXk&t=721s) that we saw with the on-prem and the hybrid models.

[12:04](https://www.youtube.com/watch?v=9G84a9IjpXk&t=724s) Everything you see in the diagram here

[12:06](https://www.youtube.com/watch?v=9G84a9IjpXk&t=726s) is an AWS service that's hosted in the cloud,

[12:09](https://www.youtube.com/watch?v=9G84a9IjpXk&t=729s) except for the agents and your desktops.

[12:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=732s) This deployment model

[12:13](https://www.youtube.com/watch?v=9G84a9IjpXk&t=733s) typically provides the lowest upfront costs,

[12:16](https://www.youtube.com/watch?v=9G84a9IjpXk&t=736s) the quickest deployment time

[12:18](https://www.youtube.com/watch?v=9G84a9IjpXk&t=738s) and the smallest footprint for your contact center.

[12:21](https://www.youtube.com/watch?v=9G84a9IjpXk&t=741s) Amazon Connect is the only cloud contact center today

[12:24](https://www.youtube.com/watch?v=9G84a9IjpXk&t=744s) that scales from tens of agents

[12:26](https://www.youtube.com/watch?v=9G84a9IjpXk&t=746s) to tens of thousands of agents.

[12:28](https://www.youtube.com/watch?v=9G84a9IjpXk&t=748s) So it's a great choice for some of the smallest customers

[12:31](https://www.youtube.com/watch?v=9G84a9IjpXk&t=751s) all the way to the largest enterprise customers.

[12:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=754s) Amazon Connect is built from the ground

[12:37](https://www.youtube.com/watch?v=9G84a9IjpXk&t=757s) to be 100% cloud-based.

[12:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=760s) There are no adapters, there are no applets or applications

[12:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=763s) or browser extensions to install

[12:45](https://www.youtube.com/watch?v=9G84a9IjpXk&t=765s) 'cause every part of Amazon Connect

[12:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=766s) is available purely in the browser.

[12:49](https://www.youtube.com/watch?v=9G84a9IjpXk&t=769s) Amazon Connect can be set up in minutes

[12:52](https://www.youtube.com/watch?v=9G84a9IjpXk&t=772s) and agents can take calls after just a few simple steps.

[12:55](https://www.youtube.com/watch?v=9G84a9IjpXk&t=775s) In fact, you can log in to the AWS console right now,

[12:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=779s) you can answer a short few questions,

[13:01](https://www.youtube.com/watch?v=9G84a9IjpXk&t=781s) claim a telephone number

[13:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=782s) and be taking calls before I finish this slide.

[13:06](https://www.youtube.com/watch?v=9G84a9IjpXk&t=786s) So lookin' at the diagram here, you see how Amazon Connect

[13:09](https://www.youtube.com/watch?v=9G84a9IjpXk&t=789s) integrates with other AWS services

[13:11](https://www.youtube.com/watch?v=9G84a9IjpXk&t=791s) that you may be familiar with.

[13:13](https://www.youtube.com/watch?v=9G84a9IjpXk&t=793s) I mentioned earlier that the secret sauce of Amazon Connect

[13:16](https://www.youtube.com/watch?v=9G84a9IjpXk&t=796s) is allowing you to accelerate the creation of dynamic,

[13:19](https://www.youtube.com/watch?v=9G84a9IjpXk&t=799s) natural and personalized experiences with Amazon Connect

[13:23](https://www.youtube.com/watch?v=9G84a9IjpXk&t=803s) by integrating with other services on AWS

[13:25](https://www.youtube.com/watch?v=9G84a9IjpXk&t=805s) and here we can see

[13:26](https://www.youtube.com/watch?v=9G84a9IjpXk&t=806s) the power of those services being utilized.

[13:29](https://www.youtube.com/watch?v=9G84a9IjpXk&t=809s) Your call center agents use the Contact Control Panel or CCP

[13:35](https://www.youtube.com/watch?v=9G84a9IjpXk&t=815s) for Amazon Connect which is provided out of the box

[13:38](https://www.youtube.com/watch?v=9G84a9IjpXk&t=818s) and this is customizable.

[13:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=820s) The Contact Control Panel allows your agents

[13:42](https://www.youtube.com/watch?v=9G84a9IjpXk&t=822s) to connect to Amazon Connect usin' a browser-based cellphone

[13:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=826s) over the secure public internet link.

[13:49](https://www.youtube.com/watch?v=9G84a9IjpXk&t=829s) You can also integrate your existing CRM systems

[13:51](https://www.youtube.com/watch?v=9G84a9IjpXk&t=831s) and your customer data lake

[13:53](https://www.youtube.com/watch?v=9G84a9IjpXk&t=833s) with all of your customer information, all usin' AWS Lambda

[13:56](https://www.youtube.com/watch?v=9G84a9IjpXk&t=836s) which is a serverless compute offering

[13:58](https://www.youtube.com/watch?v=9G84a9IjpXk&t=838s) to connect all of that to your AWS backend systems.

[14:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=842s) For example using Lambda, you can enable your agent

[14:05](https://www.youtube.com/watch?v=9G84a9IjpXk&t=845s) to look up the caller ID in your CRM system

[14:08](https://www.youtube.com/watch?v=9G84a9IjpXk&t=848s) and be able to return the caller's name and account number

[14:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=852s) and use that account number to satisfy customer requests

[14:15](https://www.youtube.com/watch?v=9G84a9IjpXk&t=855s) during the phone call.

[14:17](https://www.youtube.com/watch?v=9G84a9IjpXk&t=857s) When a call comes into your organization,

[14:19](https://www.youtube.com/watch?v=9G84a9IjpXk&t=859s) the caller ID is automatically passed

[14:21](https://www.youtube.com/watch?v=9G84a9IjpXk&t=861s) and captured by Amazon Connect.

[14:24](https://www.youtube.com/watch?v=9G84a9IjpXk&t=864s) You can configure identity and access management

[14:26](https://www.youtube.com/watch?v=9G84a9IjpXk&t=866s) for your agents and supervisors

[14:28](https://www.youtube.com/watch?v=9G84a9IjpXk&t=868s) usin' the AWS identity and management services.

[14:31](https://www.youtube.com/watch?v=9G84a9IjpXk&t=871s) You can also store your call recordings

[14:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=874s) and your chat transcripts in Amazon S3

[14:37](https://www.youtube.com/watch?v=9G84a9IjpXk&t=877s) which is our simple storage service

[14:39](https://www.youtube.com/watch?v=9G84a9IjpXk&t=879s) and have access to archive these assets over time.

[14:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=883s) You have access to a wide array of AI/ML analytics tool.

[14:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=886s) For example, you have access

[14:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=888s) to an AI/ML tool called Amazon Lex

[14:50](https://www.youtube.com/watch?v=9G84a9IjpXk&t=890s) which is the very same agent

[14:52](https://www.youtube.com/watch?v=9G84a9IjpXk&t=892s) that powers the popular Alexa device.

[14:55](https://www.youtube.com/watch?v=9G84a9IjpXk&t=895s) You can use these AI/ML tools

[14:56](https://www.youtube.com/watch?v=9G84a9IjpXk&t=896s) to create better customer experiences like chat bots

[15:00](https://www.youtube.com/watch?v=9G84a9IjpXk&t=900s) to monitor and understand your customer sentiments

[15:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=902s) to effectively train your agents.

[15:05](https://www.youtube.com/watch?v=9G84a9IjpXk&t=905s) There's another AI/ML tool

[15:06](https://www.youtube.com/watch?v=9G84a9IjpXk&t=906s) called Contact Lens for Amazon Connect

[15:09](https://www.youtube.com/watch?v=9G84a9IjpXk&t=909s) and this allows supervisors and QA managers

[15:11](https://www.youtube.com/watch?v=9G84a9IjpXk&t=911s) to better understand the sentiment,

[15:13](https://www.youtube.com/watch?v=9G84a9IjpXk&t=913s) the trends and the compliance risks of customer interactions

[15:18](https://www.youtube.com/watch?v=9G84a9IjpXk&t=918s) so they can effectively train agents

[15:20](https://www.youtube.com/watch?v=9G84a9IjpXk&t=920s) and replicate success and identify crucial company

[15:23](https://www.youtube.com/watch?v=9G84a9IjpXk&t=923s) and product feedback.

[15:25](https://www.youtube.com/watch?v=9G84a9IjpXk&t=925s) But overall,

[15:26](https://www.youtube.com/watch?v=9G84a9IjpXk&t=926s) you see the reduced complexity in this architecture

[15:29](https://www.youtube.com/watch?v=9G84a9IjpXk&t=929s) and there's a lot of innovation you get out of the box

[15:32](https://www.youtube.com/watch?v=9G84a9IjpXk&t=932s) with this deployment model with Amazon Connect.

[15:37](https://www.youtube.com/watch?v=9G84a9IjpXk&t=937s) So now that we've seen the different deployment models

[15:39](https://www.youtube.com/watch?v=9G84a9IjpXk&t=939s) for contact centers,

[15:41](https://www.youtube.com/watch?v=9G84a9IjpXk&t=941s) let's talk about the migration path

[15:42](https://www.youtube.com/watch?v=9G84a9IjpXk&t=942s) for your legacy or traditional contact centers

[15:45](https://www.youtube.com/watch?v=9G84a9IjpXk&t=945s) to Amazon Connect.

[15:47](https://www.youtube.com/watch?v=9G84a9IjpXk&t=947s) So how do you get started?

[15:49](https://www.youtube.com/watch?v=9G84a9IjpXk&t=949s) The key to a good contact center migration

[15:51](https://www.youtube.com/watch?v=9G84a9IjpXk&t=951s) is a good discovery and planning process

[15:54](https://www.youtube.com/watch?v=9G84a9IjpXk&t=954s) to allow your teams work in an agile manner

[15:57](https://www.youtube.com/watch?v=9G84a9IjpXk&t=957s) and you need to first define your goals.

[15:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=959s) So to do that, we think big and start small and go fast.

[16:04](https://www.youtube.com/watch?v=9G84a9IjpXk&t=964s) For example, one of the common use cases

[16:07](https://www.youtube.com/watch?v=9G84a9IjpXk&t=967s) that we see with most of our customers

[16:08](https://www.youtube.com/watch?v=9G84a9IjpXk&t=968s) is that they will often start

[16:10](https://www.youtube.com/watch?v=9G84a9IjpXk&t=970s) with migrating internal lines of businesses

[16:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=972s) like a help desk or kickstart a new contact center project.

[16:18](https://www.youtube.com/watch?v=9G84a9IjpXk&t=978s) You want to determine the minimum lovable product.

[16:21](https://www.youtube.com/watch?v=9G84a9IjpXk&t=981s) You notice how I said

[16:22](https://www.youtube.com/watch?v=9G84a9IjpXk&t=982s) minimum lovable and not minimum viable.

[16:25](https://www.youtube.com/watch?v=9G84a9IjpXk&t=985s) Because at AWS,

[16:26](https://www.youtube.com/watch?v=9G84a9IjpXk&t=986s) we're always lookin' to delight our customers

[16:28](https://www.youtube.com/watch?v=9G84a9IjpXk&t=988s) and not just do the bare viable minimum,

[16:31](https://www.youtube.com/watch?v=9G84a9IjpXk&t=991s) so you look for those places to quickly add that value.

[16:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=994s) In this discovery phase, you work backwards

[16:36](https://www.youtube.com/watch?v=9G84a9IjpXk&t=996s) with the discovery exercise for all the requirements

[16:38](https://www.youtube.com/watch?v=9G84a9IjpXk&t=998s) from all your major stakeholders

[16:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1000s) to ensure that no voice is left out.

[16:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1003s) And this is a good phase to do a proof of concept or pilot

[16:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1006s) to learn and explore Amazon Connect.

[16:49](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1009s) As a customer, you have access to your AWS account teams

[16:52](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1012s) and Connect specialized sellers

[16:54](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1014s) that can also guide you through this phase.

[16:57](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1017s) Once you develop a plan to

[17:01](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1021s) have your ideal experience for your call center,

[17:04](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1024s) the next migration phase is the technology foundation phase

[17:07](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1027s) and this is one of the most important phases

[17:09](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1029s) that customers should implement.

[17:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1032s) Because there's no infrastructure to manage

[17:14](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1034s) with Amazon Connect,

[17:16](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1036s) you can focus on buildin' a foundational framework

[17:19](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1039s) to iterate on right away.

[17:21](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1041s) And this lack of infrastructure build

[17:23](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1043s) might be what makes an Amazon Connect migration

[17:25](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1045s) the most unique because there's no waitin' around

[17:28](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1048s) for someone to stand up servers or install software.

[17:33](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1053s) So you might then start with an initial call center flow

[17:36](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1056s) or a chat bot experience

[17:38](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1058s) to make for really great first demos

[17:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1060s) and to get all of your stakeholders excited and engaged.

[17:44](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1064s) As a final note here as you go through this phase,

[17:47](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1067s) don't forget to create a playbook

[17:49](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1069s) for the next stage of migration.

[17:51](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1071s) You wanna keep those lessons learned.

[17:52](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1072s) The process is to create designs,

[17:55](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1075s) any notes on obstacles you overcame

[17:57](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1077s) or any other valuable information

[17:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1079s) to allow you to accelerate the migration of the next group

[18:03](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1083s) onto Amazon Connect.

[18:05](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1085s) Finally after a successful first discovery

[18:08](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1088s) and tech foundation phase,

[18:09](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1089s) you have the launch phase and the innovation phase.

[18:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1092s) With the launch phase, you're ready to move on

[18:14](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1094s) to even more groups or bigger feature sets.

[18:17](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1097s) Now you have those lessons learned from the previous phase

[18:20](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1100s) and a playbook to get started,

[18:21](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1101s) you're ready to tackle more migrations.

[18:24](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1104s) It's great at this spot, for example,

[18:26](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1106s) to train your IT team on how to migrate

[18:29](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1109s) and successfully onboard your Amazon Connect users.

[18:33](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1113s) If you're working with an IT operations team,

[18:35](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1115s) you have them come alongside and use the playbook

[18:38](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1118s) to begin to migrate all the groups in parallel.

[18:42](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1122s) In the innovate phase,

[18:44](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1124s) agile delivery becomes a foundation

[18:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1126s) for ongoing contact center innovation

[18:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1128s) to better service your customers.

[18:50](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1130s) With Amazon Connect,

[18:51](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1131s) you get a neverending cycle of opportunities

[18:53](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1133s) to not just migrate new groups

[18:55](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1135s) but also continuously improve those

[18:58](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1138s) that have already migrated

[18:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1139s) as they decide to add new features

[19:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1142s) or add new capabilities that come online in Amazon Connect.

[19:08](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1148s) So this is an Amazon Connect

[19:09](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1149s) customer migration story with Priceline.

[19:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1152s) If you're not familiar with Priceline,

[19:13](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1153s) Priceline.com is an online travel agency

[19:17](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1157s) for findin' discount rates for travel-related purchases

[19:19](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1159s) such as airline tickets and hotel stays.

[19:23](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1163s) Priceline director of contact center technology,

[19:27](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1167s) Jennifer Featherling

[19:28](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1168s) stated that they moved over 1,000 call center agents

[19:31](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1171s) from office to work-from-home with Amazon Connect

[19:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1174s) to be able to cope with the pandemic.

[19:37](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1177s) With Amazon Connect, Priceline was better prepared

[19:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1180s) to provide superior customer service

[19:42](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1182s) and quickly make adjustments when needed.

[19:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1188s) These are additional training resources

[19:49](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1189s) for Amazon Connect that are available online.

[19:55](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1195s) We talked about one group of your remote work users

[19:58](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1198s) which are virtual contact centers

[20:00](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1200s) for your remote call center agents.

[20:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1202s) Now let's take a look at collaboration toolin'

[20:05](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1205s) for your remote workers which is enabled with Amazon Chime.

[20:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1212s) You can embed audio and video

[20:15](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1215s) into your application as a collaboration tool

[20:18](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1218s) using the Amazon Chime SDK.

[20:20](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1220s) In fact, much of the same audio and video technology

[20:24](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1224s) available in the SDK is used

[20:27](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1227s) in the Amazon Chime meetings app.

[20:29](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1229s) And this is the same app that you probably used

[20:31](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1231s) for meetings with AWS teams, leaders

[20:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1234s) and technologists throughout re:Invent.

[20:37](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1237s) Before we dive deeper into how the SDK works,

[20:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1240s) it's worth spendin' just a couple of minutes

[20:42](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1242s) on why we built the Amazon Chime SDK.

[20:45](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1245s) The reality is that audio and video technology

[20:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1248s) can be pretty complex.

[20:49](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1249s) It relies on multiple integrated standards and technologies.

[20:53](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1253s) And as builders, you have to plan

[20:55](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1255s) for communications that can traverse all network conditions

[20:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1259s) while still offering an excellent end-user experience.

[21:03](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1263s) You have to provide applications for your users

[21:05](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1265s) that can be used from a laptop, a mobile device

[21:07](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1267s) or sometimes even a regular phone.

[21:10](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1270s) All of these requirements mean

[21:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1272s) that there's development overhead, operational complexity

[21:16](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1276s) and the extensibility of application may be limited

[21:19](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1279s) when you're building from the ground up.

[21:23](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1283s) So why use the Amazon Chime SDK

[21:25](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1285s) to build real-time communications to your applications?

[21:29](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1289s) By usin' the Chime SDK, you can build faster

[21:32](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1292s) letting your teams focus on deployment

[21:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1294s) of web RTC technology while you focus on buildin' out

[21:37](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1297s) your remote end-user experiences.

[21:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1300s) You can take advantage of the Amazon Chime global network

[21:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1303s) with communication services for audio callin',

[21:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1306s) video callin' or screen sharin' features,

[21:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1308s) all available in 18 AWS regions

[21:51](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1311s) without any additional infrastructure investment.

[21:54](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1314s) This allows you to just focus on your application

[21:57](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1317s) and your users.

[21:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1319s) The Amazon Chime SDK can scale up or down

[22:01](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1321s) with no additional work

[22:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1322s) and it's available across desktop and mobile clients

[22:05](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1325s) with Android and iOS clients.

[22:08](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1328s) By using Amazon Chime SDK,

[22:09](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1329s) you're buildin' on a solid AWS foundation

[22:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1332s) with the ability to extend your apps

[22:14](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1334s) with capabilities from AWS AI/ML services

[22:17](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1337s) like Transcribe and Comprehend.

[22:24](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1344s) So when Amazon Chime SDK was launched,

[22:26](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1346s) it was essentially made up of three parts:

[22:29](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1349s) the JavaScript client SDK,

[22:30](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1350s) the AWS SDK and the media services.

[22:33](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1353s) At a high level, here is how Amazon Chime SDK works

[22:38](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1358s) to integrate audio and video capabilities

[22:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1360s) into your application.

[22:42](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1362s) You start out by use of the AWS SDK with Lambda

[22:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1366s) in your server-side application to create media resources

[22:49](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1369s) in one of the supported AWS regions.

[22:53](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1373s) In response, you receive a media resource

[22:55](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1375s) and a set of media URLs

[22:58](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1378s) that represent the Amazon Chime media services

[23:00](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1380s) that are used to host the meetin'.

[23:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1382s) Your server-side application

[23:03](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1383s) can then authenticate and authorize each user

[23:06](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1386s) joining the meetin' session

[23:08](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1388s) and create a corresponding attending resource

[23:10](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1390s) by using a unique identifier from your identity system.

[23:14](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1394s) Each attendee of the meetin'

[23:15](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1395s) is assigned a unique joint token

[23:18](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1398s) that your server application

[23:19](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1399s) will securely send back to the client application.

[23:22](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1402s) The client application

[23:23](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1403s) uses a combination of secure web sockets

[23:26](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1406s) and DTLS through web RTC peer connections

[23:29](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1409s) to send and receive media to and from other attendees

[23:32](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1412s) usin' the media services.

[23:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1414s) So the Amazon Chime SDK tech takes the guesswork out

[23:38](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1418s) of addin' real-time communication components

[23:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1420s) to your applications.

[23:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1423s) Now let's take a look at Amazon Chime SDK for messagin'.

[23:47](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1427s) Amazon Chime SDK also supports

[23:49](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1429s) highly-scalable persistent messagin' in the Amazon Chime SDK

[23:53](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1433s) to build chat and other real-time messagin' features.

[23:58](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1438s) There are several Chime APIs for messagin'

[24:00](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1440s) and these APIs are combined with the Amazon Chime SDKs

[24:03](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1443s) we just saw in the previous slide

[24:05](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1445s) so developers don't have to worry about buildin' and scalin'

[24:08](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1448s) your own infrastructure for messagin'.

[24:10](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1450s) The messagin' features can be used alongside

[24:13](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1453s) with existin' audio, video and content sharing capabilities

[24:17](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1457s) of the Amazon Chime SDK.

[24:19](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1459s) And messaging can also be used separately

[24:21](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1461s) if you choose not to integrate it with video and audio.

[24:24](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1464s) You can use it in delivery applications of broadcasts

[24:28](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1468s) because you can allow up to 100,000 members per channel.

[24:33](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1473s) Here's a quick overview

[24:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1474s) of how the Amazon Chime SDK messagin' works.

[24:37](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1477s) One user on a client side application

[24:39](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1479s) is connected to a web socket provided by Amazon Chime.

[24:42](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1482s) This user is member of a channel

[24:45](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1485s) along with up to 100,000 other users

[24:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1488s) who are also connected to an active web socket

[24:51](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1491s) on your client.

[24:52](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1492s) When the sender sends the message,

[24:54](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1494s) the client sends a sent channel message API in the AWS SDK

[24:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1499s) and this message and its metadata are persisted

[25:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1502s) by the Amazon Chime SDK

[25:03](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1503s) and then fanned out to the recipients.

[25:06](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1506s) If the recipient does not have a channel open,

[25:09](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1509s) they can be notified

[25:10](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1510s) that new messages are available in the channel.

[25:13](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1513s) And if they're not connected,

[25:14](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1514s) their client will retrieve the message from history

[25:17](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1517s) the next time the user connects and loads the messages.

[25:20](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1520s) Developers can enable sendin' of attachments usin' Amazon S3

[25:24](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1524s) or their choice of file storage

[25:26](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1526s) and attach a link to the file in the message metadata.

[25:30](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1530s) Developers also have the option

[25:31](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1531s) of turnin' on streaming export of chat messages

[25:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1534s) through Amazon Kinesis.

[25:36](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1536s) And this export feature can be used to integrate

[25:38](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1538s) with services like Amazon Kendra for search

[25:41](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1541s) or services like Amazon Comprehend

[25:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1543s) to detect sensitive data or profanity

[25:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1546s) which they can be redacted or archived.

[25:49](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1549s) Amazon Chime SDK messagin' is designed to be highly flexible

[25:53](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1553s) so that you can achieve the exact experience that you need.

[25:58](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1558s) I'd like to share with you

[25:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1559s) an Amazon Chime customer migration story

[26:01](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1561s) with Cerner Corporation.

[26:03](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1563s) So Cerner is a healthcare IT company

[26:06](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1566s) that specializes in electronic medical records.

[26:09](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1569s) The company used the Amazon Chime SDK

[26:11](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1571s) to rapidly deploy and scale telehealth solutions

[26:15](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1575s) durin' the COVID-19 global health crisis

[26:18](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1578s) and this solution helped them

[26:19](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1579s) bring doctors and patients together

[26:21](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1581s) in the midst of a global health crisis.

[26:24](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1584s) With Amazon Chime SDK,

[26:25](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1585s) they leverage and manage service with Amazon Chime

[26:27](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1587s) that can support their clients dynamic usage patterns.

[26:33](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1593s) Here are some additional resources

[26:35](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1595s) for you to learn more about the Amazon Chime SDK.

[26:39](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1599s) Now I'll hand it over to my co-presenter John Walker

[26:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1603s) to talk about additional remote workforce solutions,

[26:45](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1605s) professional desktops, application streaming

[26:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1608s) and will architect with best practices.

[26:52](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1612s) Thank you, Jennifer, so much

[26:53](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1613s) for leading us through some of those

[26:55](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1615s) remote workforce solutions for migration.

[26:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1619s) Next, we're going to talk about Amazon WorkSpaces.

[27:01](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1621s) Amazon WorkSpaces is a managed and secure desktop

[27:04](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1624s) as a service solution.

[27:05](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1625s) It helps mobile and remote employees

[27:07](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1627s) access the applications they need from anywhere

[27:10](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1630s) by delivering a full cloud desktop solution.

[27:15](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1635s) So what are some of the challenges

[27:17](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1637s) that we see for remote workers?

[27:19](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1639s) The modern approach to work

[27:20](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1640s) really presents challenges for IT.

[27:22](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1642s) They need to support many different device types,

[27:25](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1645s) maintain legacy applications

[27:27](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1647s) while also building next-generation capabilities

[27:30](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1650s) and all of this while providing

[27:31](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1651s) an easy experience for their employees

[27:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1654s) and ensuring corporate applications and data are secure,

[27:37](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1657s) then they also need to drive down cost.

[27:39](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1659s) Unfortunately, the traditional approaches

[27:41](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1661s) to supporting end users are falling short.

[27:44](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1664s) First, many customers are telling us

[27:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1666s) that they've tried traditional VDI

[27:49](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1669s) and other on-prem infrastructure solutions.

[27:51](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1671s) With traditional VDI solutions

[27:53](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1673s) the IT administrators tell us,

[27:55](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1675s) they're forced to guess at annual demand

[27:57](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1677s) and to buy hardware for peak needs

[27:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1679s) and this typically results in overbuying.

[28:01](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1681s) It can take weeks or months

[28:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1682s) to complete the ongoing maintenance and infrastructure

[28:06](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1686s) and onboarding of those new devices

[28:07](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1687s) and this can be a real and hard problem.

[28:10](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1690s) And IT organizations are often caught by surprise

[28:13](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1693s) when new projects or new groups

[28:15](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1695s) need to be onboarded and come online.

[28:18](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1698s) That results in the need to purchase or upgrade hardware

[28:20](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1700s) and can delay those users coming online.

[28:24](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1704s) Second, customers tell us that their users are asking

[28:27](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1707s) for BYOD or bring your own device type solutions

[28:29](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1709s) with Macs and Chromebooks.

[28:31](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1711s) It makes it challenging

[28:33](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1713s) to securely manage and deliver applications

[28:35](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1715s) across multiple hardware,

[28:37](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1717s) operating system and software configurations.

[28:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1720s) While many customers have moved their data to the cloud,

[28:42](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1722s) their desktop applications

[28:44](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1724s) remain on-premises on user devices.

[28:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1726s) This increases latency and it makes users less productive

[28:50](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1730s) as they move data to and from the cloud

[28:52](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1732s) and to and from their applications.

[28:55](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1735s) Today, customers also use GPU

[28:58](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1738s) or graphics processing units-enabled laptops

[29:01](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1741s) in order to run CAD applications

[29:04](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1744s) like AutoCAD and Siemens NX.

[29:06](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1746s) So on average,

[29:07](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1747s) these devices can cost more than $5,000 US

[29:11](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1751s) and we had received feedback from customers

[29:13](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1753s) that they would like to deliver these applications

[29:15](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1755s) on commodity hardware or reduce their hardware cost

[29:18](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1758s) and let the workers work from any device.

[29:21](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1761s) And customers are increasingly

[29:22](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1762s) trying to support global workforces.

[29:25](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1765s) It's challenging to distribute

[29:27](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1767s) those solutions and to estimate demand for solutions

[29:32](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1772s) across many different physical locations

[29:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1774s) and operating physical device

[29:35](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1775s) VDI deployments in multiple data centers.

[29:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1780s) Customers also tell that security is the key requirement

[29:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1783s) and a top priority for them.

[29:45](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1785s) So as organizations become more agile,

[29:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1788s) how do we protect those corporate assets

[29:49](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1789s) without choking off employee productivity

[29:52](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1792s) or reducing business agility?

[29:54](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1794s) It's the reason that AWS and Amazon

[29:57](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1797s) have created Amazon WorkSpaces.

[29:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1799s) Really this is about simplifying the desktop delivery.

[30:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1802s) Amazon WorkSpaces helps you

[30:03](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1803s) to eliminate many administrative tasks

[30:05](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1805s) associated with managing your desktop lifecycle

[30:08](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1808s) including provisioning, deploying,

[30:10](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1810s) maintaining and recycling desktops.

[30:13](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1813s) There's less hardware inventory to manage

[30:15](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1815s) and no need for complex virtual desktop

[30:18](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1818s) infrastructure deployments that don't scale.

[30:21](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1821s) So we also wanna keep that data secure.

[30:24](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1824s) Amazon WorkSpaces is deployed

[30:26](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1826s) within your Amazon Virtual Private Cloud or VPC

[30:30](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1830s) to provide each user with access to

[30:33](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1833s) persistent encrypted storage volumes in the AWS cloud

[30:36](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1836s) and integrate with AWS Key Management Service or KMS

[30:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1840s) in order to provide the secure storage

[30:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1843s) of those cryptography keys.

[30:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1846s) No user data's stored on the local device

[30:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1848s) and it helps improve the security of your data

[30:51](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1851s) and reduces your overall risk surface area.

[30:54](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1854s) In addition, this is centrally managed

[30:56](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1856s) and scales your global desktop deployment

[30:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1859s) as your needs dictate.

[31:01](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1861s) Amazon WorkSpaces is available in 13 different AWS regions

[31:04](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1864s) and provides access to high-performance cloud desktops

[31:07](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1867s) wherever your teams get work done.

[31:09](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1869s) You can manage a global deployment

[31:11](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1871s) of many thousands of WorkSpaces from the AWS console

[31:14](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1874s) and you get to rapidly provision

[31:16](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1876s) and deprovision those desktops

[31:18](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1878s) as the needs of your workforce change.

[31:20](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1880s) All of this while reducing cost,

[31:22](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1882s) WorkSpaces eliminates the need for overbuy

[31:25](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1885s) of desktop and laptop resources

[31:27](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1887s) by providing on-demand access to cloud desktops

[31:29](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1889s) that include a range of compute, memory,

[31:31](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1891s) storage and graphics resources needs

[31:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1894s) to meet your users' performance needs.

[31:37](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1897s) Okay, so we've spoken about what WorkSpaces is

[31:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1900s) and what user problems this solves for our customers.

[31:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1903s) Next, let's take a look at Amazon WorkSpaces

[31:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1906s) target architecture.

[31:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1908s) So have a look at the design here.

[31:49](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1909s) This is a fully-managed solution,

[31:51](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1911s) but you control the networking with your private subnets.

[31:56](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1916s) The WorkSpaces are going to deploy

[31:57](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1917s) elastic network interfaces or ENIs

[32:00](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1920s) and you get to control what data comes in to

[32:03](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1923s) and goes out of those WorkSpaces.

[32:06](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1926s) So we have a fully-managed solution.

[32:08](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1928s) The data isolation and protection

[32:09](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1929s) is there for your security.

[32:11](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1931s) And then with scalability,

[32:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1932s) you're able to turn on multiple WorkSpaces in minutes

[32:16](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1936s) and deploy them to your subnets.

[32:18](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1938s) And with cost controls

[32:19](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1939s) using an option of the AlwaysOn or AutoStop,

[32:23](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1943s) you're able to really control and dial in

[32:26](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1946s) how many WorkSpaces resources

[32:27](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1947s) you need to be able to allocate for your users.

[32:32](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1952s) All right, so we talked about a target architecture.

[32:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1954s) We talked about which problems we're trying to solve.

[32:37](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1957s) Now let's talk about the migration.

[32:39](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1959s) So migrating your desktop to WorkSpaces

[32:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1963s) really consists of the build out phase,

[32:45](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1965s) the migration phase and operations.

[32:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1968s) So during build out, what we want to make sure that we do

[32:51](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1971s) is to decide what your identity solution is going to be.

[32:56](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1976s) If you're standing up brand-new sets of users,

[32:58](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1978s) you can use a simple AD

[33:00](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1980s) in order to implement your identity provider.

[33:03](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1983s) So AD stands for Active Directory.

[33:06](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1986s) You can use AWS' managed Active Directory

[33:08](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1988s) or you can use an AD connector

[33:10](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1990s) in order to connect back to a directory service

[33:13](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1993s) that exists on-premises,

[33:15](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1995s) in a data center or in another cloud.

[33:18](https://www.youtube.com/watch?v=9G84a9IjpXk&t=1998s) You also want to decide your networking solutions.

[33:21](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2001s) So with networking, you want to lay out your network access.

[33:25](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2005s) If you have AD Connector, it's going to need AD access

[33:28](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2008s) so make sure that you got the open ports

[33:30](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2010s) back to that active directory

[33:32](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2012s) and probably set in place a virtual private network

[33:35](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2015s) or VPN connection there.

[33:37](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2017s) Inside of that security group for your subnet,

[33:41](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2021s) make sure that you open up the ports to the services

[33:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2023s) that your users need to access.

[33:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2026s) So if that's databases

[33:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2028s) or if it's accessing special TCP ports,

[33:50](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2030s) make sure you open those up so your users can access

[33:53](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2033s) exactly the services that they need.

[33:55](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2035s) All right, now that we've set up the networking,

[33:57](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2037s) we've set up the identity

[33:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2039s) and we're able to bring over your users' identities

[34:01](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2041s) in order to authenticate into WorkSpaces,

[34:03](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2043s) now it's time for you to do the image creation.

[34:06](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2046s) So during image creation,

[34:07](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2047s) you'll first launch a workspace and configure it.

[34:10](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2050s) So use our images

[34:13](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2053s) in order to create your bundle for your workspace.

[34:17](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2057s) You can start with a Value image

[34:20](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2060s) all the way up to PowerPro images

[34:22](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2062s) and choose one of these images

[34:24](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2064s) per high-level use case for your users.

[34:27](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2067s) So consider your different user personas

[34:29](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2069s) and which users you want to deploy this to.

[34:32](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2072s) Once you create your image,

[34:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2074s) go ahead and minimize the number of images

[34:37](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2077s) by using WorkSpaces Application Manager,

[34:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2080s) WAM which is going to be able

[34:42](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2082s) to package additional applications to deploy

[34:45](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2085s) whenever a user logs into their workspace.

[34:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2088s) All right, so other distribution package types

[34:51](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2091s) also work the way that you're already used to

[34:54](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2094s) distributing applications onto your desktop solutions.

[34:58](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2098s) Create that image from the workspace

[34:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2099s) and bundle the image with a correct hardware type.

[35:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2102s) You can also use BYOL or bring your own license

[35:04](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2104s) with Windows 10 desktop licenses.

[35:07](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2107s) Okay, then you're gonna launch your WorkSpaces.

[35:10](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2110s) Whenever you've launched your WorkSpaces,

[35:11](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2111s) next you wanna figure out which users

[35:14](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2114s) you're going to bring to bear here.

[35:16](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2116s) So the user selection

[35:17](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2117s) is going to be proof of concept users or opt-in groups.

[35:20](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2120s) Often this is consultants

[35:22](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2122s) or I find users are looking at outsourced work

[35:25](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2125s) or contingent work that's seasonal

[35:27](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2127s) and go ahead and turn those on as your first-use cases,

[35:31](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2131s) then move into other user groups as your needs see fit.

[35:35](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2135s) Then you want to use correct WorkSpaces sizing.

[35:38](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2138s) So evaluate memory optimize, CPU optimize,

[35:41](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2141s) GPU optimize sizing bundles

[35:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2143s) in order to correctly size your WorkSpaces

[35:47](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2147s) and correctly size your spend.

[35:49](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2149s) Next whenever you're migrating that information,

[35:51](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2151s) you want to make sure that you can access the data

[35:53](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2153s) that you already have.

[35:55](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2155s) So what you can do is use Windows shares

[35:58](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2158s) and/or your WorkDocs Drive

[36:00](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2160s) in order to make sure that that data is there

[36:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2162s) whenever a user logs into their workspace.

[36:05](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2165s) Next, let's talk about operations.

[36:08](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2168s) It's very important during operations to enable those users,

[36:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2172s) so make sure that you're going to train the users

[36:14](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2174s) and of the support desk

[36:15](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2175s) in order to operate in a slightly new way

[36:18](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2178s) with operating these remote WorkSpaces in the cloud.

[36:22](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2182s) With fleet management,

[36:23](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2183s) make sure that you're evaluating constantly

[36:25](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2185s) and upgrading to larger bundles

[36:27](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2187s) or downgrading to smaller bundles

[36:29](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2189s) as your users' needs see fit

[36:31](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2191s) and shift between that AlwaysOn and AutoStop

[36:33](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2193s) in order to save a little bit of money.

[36:36](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2196s) Terminate those unused WorkSpaces

[36:38](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2198s) and you're increasing the value

[36:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2200s) that you're getting out of WorkSpaces.

[36:42](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2202s) Monitor those alarms and check on your best practices

[36:44](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2204s) with health checks on network links

[36:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2206s) and on Active Directory using Amazon CloudWatch

[36:50](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2210s) and make sure that you're patching,

[36:52](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2212s) updating and maintaining those WorkSpaces

[36:54](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2214s) just as you would desktop solutions.

[36:57](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2217s) All right.

[36:58](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2218s) Next, let's talk a little bit about a customer's story.

[37:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2222s) Amazon.com is an AWS customer.

[37:05](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2225s) And at Amazon, we were able to burst scale

[37:08](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2228s) our Amazon WorkSpaces environment in 1 1/2 weeks

[37:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2232s) going from 25,000 running instances

[37:14](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2234s) to near 300,000 running instances

[37:17](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2237s) across eight different regions.

[37:19](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2239s) So look at that timeline just 1 1/2 weeks.

[37:22](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2242s) And whenever you look at the scale

[37:23](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2243s) going from 25,000 to 300,000 running instances,

[37:28](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2248s) that's phenomenal agility that you have at your fingertips.

[37:32](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2252s) Okay, for a few resources here,

[37:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2254s) you can go over to aws.amazon.com/workspaces

[37:39](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2259s) and aws.training in order to get access

[37:42](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2262s) to more WorkSpaces information

[37:44](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2264s) and in order to get access to some training

[37:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2266s) for Amazon WorkSpaces.

[37:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2268s) And we heard a little bit about Amazon WorkSpaces

[37:51](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2271s) which is a persistent desktop solution in the cloud.

[37:54](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2274s) And now I'm going to talk to you about Amazon AppStream 2.0

[37:57](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2277s) which is a fully-managed non-persistent desktop

[38:00](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2280s) and application service for remotely accessing your work.

[38:05](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2285s) So what are some of the challenges

[38:07](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2287s) that we see for IT to meet end user needs

[38:11](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2291s) that Amazon AppStream 2.0 fills?

[38:14](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2294s) So this is a modern approach to work

[38:17](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2297s) that presents some challenges to IT.

[38:18](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2298s) First, we need to make sure

[38:19](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2299s) that we improve the user experiences of applications

[38:23](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2303s) all while being able to deliver applications

[38:27](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2307s) that have become increasingly complicated

[38:29](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2309s) for application delivery.

[38:31](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2311s) So whenever you think about

[38:32](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2312s) being able to deliver an application to a Mac,

[38:35](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2315s) to a Chromebook, to a Windows computer

[38:37](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2317s) and being able to do that on assets

[38:39](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2319s) that may not be inside of a corporate computer deployment.

[38:44](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2324s) Instead, it may be taken home to someone's home office

[38:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2328s) or to be sitting on someone's kitchen table.

[38:51](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2331s) Being able to deliver those applications to those users

[38:54](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2334s) has become increasingly complex

[38:56](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2336s) as users choose remote working styles.

[39:00](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2340s) In addition, we still need to have that

[39:03](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2343s) at the primary forefront of IT users' needs

[39:06](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2346s) to improve the security of applications

[39:08](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2348s) while letting those users work remotely.

[39:11](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2351s) In addition, IT are telling us

[39:14](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2354s) that they are needing to scale their workforce globally.

[39:17](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2357s) So being able to provide those same solutions

[39:19](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2359s) with a consistent application experience,

[39:22](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2362s) being able to improve the efficiency

[39:24](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2364s) with which we're delivering the applications,

[39:25](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2365s) improve the security and be able to scale globally

[39:28](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2368s) is a real and hard problem.

[39:32](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2372s) So this is what Amazon AppStream 2.0 is created for.

[39:36](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2376s) AWS apps and desktop as a service

[39:38](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2378s) delivers persistent and non-persistent virtualized

[39:41](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2381s) Windows apps and desktops

[39:42](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2382s) as fully managed cloud services at scale.

[39:45](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2385s) And Amazon AppStream 2.0

[39:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2386s) is a fully-managed application streaming service

[39:50](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2390s) that allows your remote workers or students

[39:52](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2392s) to access the applications they need on any computer

[39:56](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2396s) whether they're in the classroom,

[39:57](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2397s) the library, a cafe or at home.

[40:00](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2400s) And so what we see is real improvement

[40:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2402s) of the end-user experience

[40:04](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2404s) by being able to stream non-persistent desktops and apps.

[40:07](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2407s) And the architecture here contrasted with WorkSpaces

[40:10](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2410s) is a non-persistent by-design architecture.

[40:15](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2415s) This is going to be able to integrate

[40:16](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2416s) with existing IT storage and identity management solutions.

[40:20](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2420s) And the approach is really to be able

[40:21](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2421s) to deliver a fully-managed service

[40:23](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2423s) and be able to deploy this at scale globally

[40:25](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2425s) with pay-as-you-go pricing.

[40:27](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2427s) All right. Next, let's take a look

[40:29](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2429s) at the target architecture.

[40:32](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2432s) So the target architecture for this

[40:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2434s) is really going to solve for those same problem sets

[40:37](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2437s) that we saw IT and users are needing to solve.

[40:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2440s) So for communications,

[40:42](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2442s) those communications between applications

[40:45](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2445s) and the data that exists in the cloud

[40:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2446s) are now going to be brought together.

[40:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2448s) So your data will be delivered inside of the AWS cloud,

[40:52](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2452s) inside of the region that you've chosen,

[40:54](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2454s) in your availability zones and your VPCs.

[40:57](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2457s) Similar to WorkSpaces,

[40:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2459s) Amazon AppStream is going to be able to deploy

[41:01](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2461s) your AppStream 2.0 elastic network interfaces or ENIs

[41:06](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2466s) inside of your private subnets in your VPC.

[41:10](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2470s) And then on top of that,

[41:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2472s) you'll be able to get automatic provisioning

[41:14](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2474s) with application auto-scaling.

[41:16](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2476s) This is going to be able

[41:17](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2477s) to automatically scale your applications

[41:20](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2480s) as user needs increase and scale them back in importantly

[41:24](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2484s) whenever your users' needs decrease.

[41:27](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2487s) Then for operations, we have AppStream 2.0 fleet images

[41:31](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2491s) and this is going to be able to optimize

[41:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2494s) what your operations and IT team needs to do.

[41:38](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2498s) So if you need to say update an AppStream 2.0 image

[41:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2503s) because a new patch came in for the application

[41:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2506s) or a new patch came in for the underlying operating system,

[41:49](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2509s) all you have to do is update one image

[41:52](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2512s) and then it's available to all users of that fleet

[41:56](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2516s) as you deploy that for usage.

[41:58](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2518s) It's a phenomenally streamlined ability

[42:00](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2520s) to update your fleet and get those updates

[42:03](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2523s) rolled out to everyone all at once.

[42:06](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2526s) As your users log in

[42:08](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2528s) to their AppStream 2.0 streaming applications,

[42:11](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2531s) they're going to be able to save their data

[42:14](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2534s) and have it available to them whenever they log back in,

[42:17](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2537s) whenever they use that application for the next time

[42:19](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2539s) by taking advantage of user home folders.

[42:22](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2542s) That can be deployed in Amazon S3.

[42:24](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2544s) In addition, you can bring your own cloud drive

[42:28](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2548s) if you so wish and configure this

[42:30](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2550s) to connect into your Amazon AppStream 2.0.

[42:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2554s) In addition, whenever you change settings

[42:36](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2556s) and set them up for your baseline fleet image,

[42:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2560s) everyone's going to get

[42:41](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2561s) the same default application settings.

[42:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2563s) But if a user's able to change those application settings,

[42:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2566s) likewise those are going to be stored

[42:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2568s) in an Amazon S3 bucket

[42:50](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2570s) so that application login over login

[42:52](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2572s) the users get a consistent usability

[42:55](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2575s) for the applications they're using.

[42:58](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2578s) All right, so we talked about

[42:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2579s) what the target architecture looks like.

[43:00](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2580s) Let's talk about migrating your applications

[43:03](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2583s) to AppStream 2.0.

[43:04](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2584s) And really first, I wanna give you an idea

[43:06](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2586s) of what some of these are, some of the example applications

[43:09](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2589s) that I see users have success with

[43:11](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2591s) or for using a security bastion host.

[43:14](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2594s) Maybe you got a remote desktop solution

[43:17](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2597s) that you're logging in to

[43:18](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2598s) to perform secure actions in your cloud.

[43:20](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2600s) A security bastion host, it's also called a jumpbox.

[43:23](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2603s) You can have these set up in a way that is non-persistent

[43:27](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2607s) so that as the user needs it,

[43:29](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2609s) that AppStream service is available to log in to the device,

[43:32](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2612s) do the security work,

[43:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2614s) be able to log off and have that go away

[43:36](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2616s) so it's no longer an IP address that's deployed in your VPC

[43:39](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2619s) and it's no longer a target, right?

[43:41](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2621s) Because it has those security tools on it,

[43:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2623s) it's only there as you need it as you need to use it.

[43:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2626s) We also see this for 3D engineering:

[43:49](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2629s) SOLIDWORKS, AutoCAD, Siemens NX and more,

[43:51](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2631s) being able to use graphics-intensive processes

[43:54](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2634s) and being able to get access to that hardware in the cloud

[43:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2639s) without the need to provision

[44:00](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2640s) that heavy GPU-intensive application hardware

[44:05](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2645s) on users' devices themselves.

[44:07](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2647s) So there's an easy app import

[44:09](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2649s) through the AWS Management Console.

[44:10](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2650s) Just launch an image builder,

[44:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2652s) connect and install your applications,

[44:14](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2654s) configure them for the default settings that you need

[44:16](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2656s) and then set those Windows settings

[44:19](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2659s) you want your users to have.

[44:20](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2660s) Then you're going to launch this and optimize it

[44:23](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2663s) to make sure that your performance is great,

[44:25](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2665s) exactly what your users need

[44:26](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2666s) and test out the application experience and save it.

[44:29](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2669s) Once you save that image, you can use it for your fleets.

[44:32](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2672s) Assign it to your fleets according to those user personas

[44:35](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2675s) that we spoke about before.

[44:37](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2677s) And with AppStream 2.0,

[44:39](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2679s) that agent software that is on those remote systems

[44:41](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2681s) can be managed for you.

[44:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2683s) There's no need for you to manage that yourself.

[44:47](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2687s) So that's an easy way to migrate

[44:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2688s) to the Amazon AppStream 2.0.

[44:51](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2691s) Let's talk about a customer story.

[44:53](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2693s) This is Samsung Engineering

[44:55](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2695s) and they had construction sites and partners

[44:57](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2697s) that are located all over the world

[44:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2699s) including North and Central America,

[45:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2702s) Asia, the Middle East and Europe.

[45:04](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2704s) And Jeong Hoon Lee, the senior engineer

[45:06](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2706s) at Samsung engineering said

[45:08](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2708s) that they were able to save 20% of the cost

[45:10](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2710s) of purchasing and maintaining

[45:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2712s) on-premises design infrastructure

[45:14](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2714s) and they were able to actually improve

[45:16](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2716s) the efficiency of their personnel

[45:18](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2718s) to where only one person needs to manage the system.

[45:21](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2721s) And they had additional benefits.

[45:23](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2723s) So in addition to saving 20%,

[45:25](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2725s) they were able to speed up their deployment

[45:27](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2727s) from months to days and reduce the support staff

[45:29](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2729s) from four to one and enable greater customer collaboration.

[45:33](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2733s) So as they were able to bring on users in different regions,

[45:37](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2737s) deploying them in each region where they operated

[45:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2740s) once required them to source, deploy, manage complex

[45:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2743s) and costly on-premises infrastructure for each project.

[45:46](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2746s) In addition, there were issues with latency

[45:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2748s) that made it difficult for them

[45:49](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2749s) to be able to bring partners and customers

[45:51](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2751s) in the project workflow.

[45:53](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2753s) So for those reasons, Samsung Engineering decided to move

[45:56](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2756s) its design suite into Amazon AppStream 2.0.

[45:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2759s) And using AppStream 2.0,

[46:01](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2761s) they were able to virtualize their solutions

[46:04](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2764s) while providing a fluid, low-latency experience

[46:07](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2767s) accessible via web browser and be able to bring in new users

[46:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2772s) independent of where they were located.

[46:16](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2776s) For some additional AppStream 2.0 resources,

[46:19](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2779s) take a look at aws.amazon.com/appstream2

[46:24](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2784s) to learn more about AppStream.

[46:26](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2786s) And for training on AppStream 2.0, go over to aws.training.

[46:32](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2792s) All right, so we looked a little bit

[46:33](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2793s) at four different solutions

[46:35](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2795s) and four different migration patterns for remote workforce.

[46:38](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2798s) Now let's do some consideration

[46:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2800s) of the Well-Architected Framework.

[46:44](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2804s) With the AWS Well-Architected Framework,

[46:47](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2807s) it helps cloud architects build secure,

[46:49](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2809s) high-performing, resilient and efficient infrastructure

[46:52](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2812s) for the applications and workloads.

[46:55](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2815s) Based on five pillars:

[46:57](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2817s) operational excellence, security, reliability,

[47:00](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2820s) performance efficiency and cost optimization,

[47:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2822s) the AWS Well-Architected Framework

[47:05](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2825s) provides a consistent approach for customers and partners

[47:08](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2828s) to evaluate these architectures

[47:09](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2829s) and implement designs that can scale over time.

[47:13](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2833s) So first, let's have a consideration of reliability.

[47:17](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2837s) With reliability, one thing I wanna focus in on

[47:19](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2839s) and we're just gonna do one per pillar here

[47:21](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2841s) is make sure that you're going to manage your quotas.

[47:24](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2844s) So each AWS service does have a quota.

[47:27](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2847s) There are soft quotas and hard quotas

[47:28](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2848s) that exist for each service.

[47:30](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2850s) As you near quotas, make sure that you're paying attention

[47:33](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2853s) to the needs of your users

[47:35](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2855s) and you can go ahead and provision new quota increases

[47:40](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2860s) with the service quota tool inside of the AWS console

[47:43](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2863s) or you can open a support ticket

[47:45](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2865s) using the support resource in the AWS console

[47:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2868s) in the upper right corner.

[47:50](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2870s) So with Connect, you can pay attention

[47:53](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2873s) to Connect instances per account.

[47:55](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2875s) With AppStream 2.0,

[47:56](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2876s) pay attention to the number of your fleet instances.

[47:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2879s) And with WorkSpaces,

[48:00](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2880s) take a look at the number of workspace

[48:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2882s) image types and bundles that you're actually utilizing

[48:04](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2884s) and keep track of those with CloudWatch alerts.

[48:08](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2888s) Next, let's take a look at security.

[48:11](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2891s) And what you wanna do with security

[48:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2892s) is to plan in advance the different personas or user types

[48:15](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2895s) and how they're going to identify to the system.

[48:19](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2899s) So pay attention to your identity management system

[48:21](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2901s) and the credentials they'll use

[48:22](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2902s) with your onboarding and offboarding and decide in advance

[48:26](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2906s) what your identity provider will be

[48:28](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2908s) and use AWS documentation for setup and best practices

[48:32](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2912s) in order to identify those users

[48:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2914s) and further access control.

[48:36](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2916s) Next, let's talk about performance efficiency.

[48:39](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2919s) And again, there's a bit of a focus on users.

[48:41](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2921s) For users and agents.

[48:42](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2922s) make sure to pay attention to their enablement.

[48:45](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2925s) Train your users, your contact center agents

[48:48](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2928s) and your support personnel how to use these services

[48:51](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2931s) in order to optimize the value that you and your teams get

[48:54](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2934s) from migrating to end-user computing on AWS.

[48:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2939s) Next, we'll talk about operational excellence.

[49:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2942s) For operational excellence,

[49:03](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2943s) pay attention to change management.

[49:05](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2945s) For incremental changes that you're going to enforce,

[49:08](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2948s) try to put in place good governance with change management.

[49:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2952s) For updating or configuring contact flows with Connect,

[49:15](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2955s) for instance, make sure you're keeping track of

[49:17](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2957s) and using change management.

[49:19](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2959s) Follow annd update and rollback process

[49:22](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2962s) to make sure that you're streamlining

[49:24](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2964s) clean change management procedures.

[49:26](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2966s) With AppStream, for instance,

[49:28](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2968s) create new images and test them

[49:30](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2970s) with updates and new applications

[49:31](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2971s) before rolling them out to your fleets

[49:33](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2973s) and also to optimize the amount of performance

[49:36](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2976s) that your users are going to get out of 'em.

[49:38](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2978s) So there's kind of a two-fer there

[49:39](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2979s) with performance efficiency and operational excellence

[49:42](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2982s) by employing change management here.

[49:45](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2985s) Next for cost optimization,

[49:47](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2987s) make sure and take a look at the self-service options

[49:50](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2990s) for each of the services that we've discussed today

[49:53](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2993s) evolving beyond the on-premise model

[49:55](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2995s) of over-provisioning and overpaying.

[49:57](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2997s) Instead, you can take a look at

[49:59](https://www.youtube.com/watch?v=9G84a9IjpXk&t=2999s) on-demand service technology capabilities

[50:02](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3002s) in order to enable access to the resources users need

[50:05](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3005s) at the time that they need them.

[50:06](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3006s) For instance, being able to provision a workspace by user,

[50:10](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3010s) changing that over to an on-demand

[50:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3012s) as opposed to an upfront provisioning system.

[50:15](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3015s) This can save you and your users significant cost and time.

[50:20](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3020s) All right, we've talked about the Well-Architected Framework

[50:24](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3024s) and a key consideration for each.

[50:26](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3026s) And in summary, we've spoken about Amazon Connect

[50:29](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3029s) before being able to enable businesses

[50:32](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3032s) to have a fully-operational contact center.

[50:34](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3034s) We've spoken about Amazon Chime

[50:36](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3036s) that lets you meet, chat and place business phone calls

[50:38](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3038s) with a single secure application from anywhere.

[50:42](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3042s) We've spoken about Amazon WorkSpaces

[50:44](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3044s) as a managed secure desktop

[50:45](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3045s) as a service solution in the cloud

[50:47](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3047s) and Amazon AppStream 2.0

[50:49](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3049s) as a fully-managed application streaming service.

[50:52](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3052s) And as you migrate to these, I wish you the best of success.

[50:55](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3055s) Thank you all so much for listening to Jennifer and me

[50:58](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3058s) to describe these four different solutions

[51:00](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3060s) that Amazon and AWS are providing

[51:03](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3063s) for remote workforce solutions

[51:05](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3065s) and the design for remote workforce

[51:08](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3068s) solution migration patterns.

[51:09](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3069s) We wish you the best of luck implementing them

[51:12](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3072s) and have a wonderful day.

[51:15](https://www.youtube.com/watch?v=9G84a9IjpXk&t=3075s) (smooth rhythmic music)

