# AWS re:Invent 2021 - Architecting for sustainability

[Video Link](https://www.youtube.com/watch?v=3-Zq2W1-odU)

## Description

AWS is focused on efficiency in every aspect of our infrastructure, and builders can accelerate the sustainability of their workloads through optimization and informed architecture patterns. This session dives deep into techniques recommended by the AWS Well-Architected Framework and provides direction on reducing the energy and carbon impact of AWS architectures. Learn about user patterns, software design, and AWS service considerations, which organizations of any size can apply to their workloads. As an example, discover how Starbucks optimized its Kubernetes cluster, increased spot usage, and focused on digital sustainability across the organization following an AWS sustainable architecture assessment.

Learn more about re:Invent 2021 at https://bit.ly/3IvOLtK

Subscribe: 
More AWS videos http://bit.ly/2O3zS75 
More AWS events videos http://bit.ly/316g9t4

ABOUT AWS
Amazon Web Services (AWS) hosts events, both online and in-person, bringing the cloud computing community together to connect, collaborate, and learn from AWS experts.

AWS is the world’s most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally. Millions of customers—including the fastest-growing startups, largest enterprises, and leading government agencies—are using AWS to lower costs, become more agile, and innovate faster.

#AWS #AmazonWebServices #CloudComputing

## Transcript

(gentle music) Okay, hi, everybody. Thank you for coming to ARC325 architecting for sustainability. I'm Adrian Cockcroft, VP Sustainability Architecture for Amazon. People ask me, "What does that mean?" It means this. This is actually kind of the title I have for talking about architecting for sustainability. I was previously with AWS working on open source, and things like that. Earlier this year, I switched to working for Amazon, but focused on helping AWS and AWS customers with their sustainability needs. We'll have Steffen up next, talking about the well-architected guide for sustainability, the pillar and Drew talking about how Starbucks has optimized their architecture for sustainability. I'll come back at the end just for a few words to wrap it up. So it's the overall of it. Starting off talking about sustainability transformation. What do we mean by that? How are we partnering on sustainability? Then Steffen will talk about how to architect. We'll get the Starbucks talking. I'll just talk a little bit about the end call to action next steps for builders. So sustainability transformation. What does this mean? Well, let's start talking about sustainability to start with. There's really four areas to sustainability. One is decarbonizing everything we do. The second one is water usage. How do we use water effectively make sure we're not polluting, and keep it clean? Then there's social responsibility. This is about knowing your supply chain, knowing that the labor practices are good, there's no false labor or child labor. And then circular economy. How do we make sure there's zero going to landfill, and there's a lot of recycling? Today, we focusing really on the carbon part of this problem. So sustainability is becoming an increasing trend across the business. We're seeing customer demand for this. We're seeing increased government regulations, driving all kinds of businesses to worry about sustainability they didn't use to. We're seeing a lot of employee demand, a lot of enthusiasm for people that want to do something, like I'm going to leave the world a better place for your children is a common sort of phrase that we hear. We're seeing investors that want to invest in things which are helping the planet rather than destroying the planet. And we're also seeing sustainability as competitive positioning across product lines. Everyone knows what that looks like in the grocery store, you see all of these brandings. But what we've been doing for the last decade or so, what I've been working on is digital transformation. And what that means to me is that we were able to connect to our customers and everything we made, and we were able to use that to transform our businesses, and build new kinds of services, and new kinds of capabilities. And speed everything up using Cloud. So that's digital transformation. You should all be pretty familiar with that by now. But what we have to do now is use those same techniques, but use them to decarbonize everything we do. Measure it, decarbonize it, and do it at speed. Do it quickly using the same techniques that we used for digital transformation. And it turns out that companies that figured out digital transformation and sustainability transformation are doing much better in the market. The combination together is a very powerful thing. But there's challenges. How do you identify what your carbon emission hotspots are? How do you reduce energy and water use in your operations? How can you innovate faster to achieve this transformation? And how do you collaborate with your supply chain and your value chain to reduce the carbon emissions across end to end? And then the other thing that's different, digital transformation happens in months or years you should know fast enough, but months to years. Sustainability, we're talking about decades. And we say, well, you may have heard of people saying, "Well, we have a pledge. We're going to be carbon neutral in 2050." How many people are still gonna be working at that company in 2050 that are making that commitment now? You can make all kinds of promises you don't have to deliver on for 30 years. So how can you deliver on a result that's decades away and know that you're speeding up the process of getting there? So I'm gonna talk a bit about how Amazon's approaching that, and then a bit more about how AWS is approaching that. About two years ago, we announced The Climate Pledge. This is to take the Paris Agreement, which is a 2050 net-zero goal, and bring it in 10 years earlier to 2040. And to have a number of companies around the world, join us in that pledge. Now, around Earth Day, which is April this year, we announced that we passed 100 signatories in the Climate Pledge. And at COP26, month or so ago, we announced we'd passed 200 companies in the Climate Pledge. So this is growing very quickly, and I'd encourage you, if your company has a goal to be sustainable, take a look at The Climate Pledge, reach out through your account team, reach out to me. We can help figure out what does it take to help you get to a 2040 commitment. Because the more people we can get to 2040, the more impact we can get on the overall goal of getting the carbon for 2050 down to the where it needs to be. There's gonna be plenty of people that miss the 2050, right? We need to have a lot of people that are early to balance the people that are gonna be late. So you need a path, oh. So we've committed to net-zero carbon, and then there's a path to 100% renewable energy by 2025 that Amazon as a whole is committed to as well. And we also have this $2 billion Climate Pledge fund, which has invested in a number of smaller startups plus a company called Rivian. And you may have seen the truck downstairs, which is done very well recently. So, The Climate Pledge has three principles. Regular reporting, carbon elimination, and credible offsets. And across many industries, many countries, and many large brands from around the world. So what do you get out of signing this? So it's collaboration, we're sharing ideas. We're trying to find a puff to look to carbon neutrality. But these are the companies who are the leaders and innovators in their markets that have figured out how to get to an earlier commitment and then there are other companies going well. I'd like to get there, but I don't see how to get there. So what we want to do is use these leaders and innovators, document how they did it. Discuss how they did it. Collaboratively work together to help get there quickly and then bring the next wave of people into The Climate Pledge. So that's what we're doing. But also if you're a Climate Pledge signatory, and the investors are looking at you, there were these ESG funds, environmental, social, and governance funds, which are looking for investing in companies which have a good sustainability record. So it helps your branding in that sense. And then there's always opportunities to lead by sharing technologies, and this is really to accelerate the progress. If you look at how we've got there, last three years, we've published our annual report. You can find it on the website. Incredible detail on what we're doing, and across all of Amazons. This is not just AWS. We publish the entire company of Amazon, and AWS is just a piece of that. We've ordered these 100,000 Rivian electric delivery vehicles. We've reduced the weight of outbound packaging, saved a million tons of cardboard and things like that. And we're also the largest buyer of renewable energy in the world. And we recently announced, just a few days ago, that we're now up to 12 gigawatts of energy under contract. We're building new headquarters, and that's got LEED platinum, it's sustainable. These new buildings have no gas supply to the building. They're fully electric. And they're built out of low-carbon concrete, low-carbon steel. So building is one of the areas that every company has buildings, everyone needs to decarbonize how they build their buildings, and how they operate their buildings. One of the big areas we're working on. And then if you have an echo or a fire device, we're actually working to offset the energy you use in your house to run those devices. We know which ones are turned on. We know how much power they use. We add that up, and we we're basically offsetting the energy of the footprint of our devices. If we look at AWS, we've done a lot of work on water around data center cooling, and evaporative cooling, and recycling the water. So there's a very advanced set of processes there around water management. We've also optimized the energy that comes into the data center from the edge, and it gets supplied to the building. There's a lot of conversion losses before it actually gets to the CPU that's going to run your workloads. We reduce those energy losses by 35%. And part of that was by going to a distributed UPS that's actually lets you optimize everything deeply in the system rather than having a UPS for the entire building. Obviously, we've been using the renewable energy that Amazon as a whole has been buying up to provide low-carbon energy for data centers. We've got a low-carbon concrete data center design. You've heard a lot about Graviton this week, Graviton3 and Graviton2. Very good performance per watt. So you can reduce your carbon footprint by just moving to Graviton. And I'll talk a bit more about the Amazon Sustainability Data Initiative. This launched in 2018, and it's an Open Data Program. Just going back to that carbon neutral data centre, there's a European organization, the Climate Neutral Data Centre Pact. We've joined that, and we're building this commitment to proactively lead the transition to climate-neutral economy. But data is central to addressing the climate crisis. It's growing exponentially from new sources. You heard in the keynote, certainly about satellites. There were more and more satellites, downloading more and more high resolution data, as well as all the instrumentation we're getting from the Internet of Things, and all the metering we're doing to figure out where our carbon footprint goes. It's very diverse data. There's lots of different people using it, and lots of different applications for it. So we have a few programs that can help here. And we have an Open Data Program that in general, if you have a data set, you own a dataset, and you'd like to share it with the world. Maybe it's petabytes in size. That's fairly expensive to share it with the world. But if you enter our Open Data Program, we will zero out the cost of that S3 bucket to you. You still own the data, it's your bucket, but you share that to the world. We zero out the cost, and we cover all the transfer and usage costs. So, it's free for you and it's free to use. So we're taking that approach, and we have a very large number of data sets in this program. A subset of that is Amazon Sustainability Data Initiative, which is more focused on climate data. And then we have a marketplace, AWS Data Exchange. So ASDI is there to reduce the cost, time, and technical barriers with dealing with these very large data sets. Lots of different data sources here, Digital Globe, NASA, the Met Office, UK Met Office. Climate data, we have models. Climate data, air quality, historical weather records forecasts, all kinds of indicators. So if you're trying to do something that's more sort of global, trying to figure out what's going on in your region, you can actually aggregate all these data sets together. We have a hackathon, the Code Green hackathon on Monday, where we had teams come in work on combining some of these data sets to build some new capabilities. We've also recently announced the first climate model, the full climate models. These are the things that are predicting what's gonna happen that we brought to the Cloud with NCAR. And SilverLining is the nonprofit that's doing, sort of working with NCAR to make this happen. Then Data Exchange provides data sources as a marketplace. So that's AWS as your sustainability partner. But what problems you're trying to solve? What are your biggest challenges related to sustainability? How are you solving these issues? We want to identify the cases, move to AWS, and optimize those workloads. Lots of different use cases. Our professional services team has been working across all these different areas, and work through your account teams, if you're working on one of these, and we can bring in some experienced teams that have built this for other organizations already. One of those case studies is carrier with the cold chain, keeping refrigeration working end-to-end through the entire chain of activities. Another one is using machine learning to optimize the energy and water usage for Coca-Cola. So lots of different ways. We can migrate workloads to AWS. And we even decode developed products with our customers through the industry products group. And one example there is Vector, who had building metering system that can track the energy usage of that customers. So that's what I've got. And we should look now optimizing Cloud workloads. And I'm gonna bring up Steffen now to talk about that. Yeah, thank you.
There you go. Thank you, Adrian. Yeah, I would like to talk about how you architect for sustainability, and reduce your environmental impact. When we talk about the environmental impact, one important factor for the climate change and for the global warming is the emission of pollution and emission by greenhouse gases. One way to categorize and quantify these emissions is the Greenhouse Gas Protocol, which divides the emissions into three scopes. It's measured in carbon dioxide equivalents to also factor in other gases that support global warming. Scope one is direct emissions. Fuel, wood, anything which burns, or emits greenhouse gases. To reduce that, you would electrify everything. For example, by switching to electric vehicles, or moving from gas ranges to induction ranges. Scope two is emissions through purchased electricity. If you electrify anything, still the energy is having a carbon intensity, because it's usually sourced, for example, from a mix of wind, and solar, and coal. And the emissions contribute to scope two. To reduce that, you would use as much renewable power as possible, and use the renewable energies, for example, in batteries. So it is there when you need it. Scope three is indirect emissions, all the way up and down your supply chain. Scope three is depending a lot on your production depth, the products and services you're delivering, and how you deliver them. Let's transfer these three scopes to data centers. Looking at a typical data center, you see the energy is coming from the grid. It's usually a mix of renewables and fossil fuels. And the carbon in the energy contributes to scope two. Then you have a diesel generator for backup if the grid is not available, and its direct emissions contribute to scope one. And then there are things which needs to be built and delivered to the facilities like the building itself, and also equipment like racks and servers. And the carbon emitted for this contributes to scope three. Zooming in close on the data center, you see that the energy is distributed in the facilities for the cooling to the service, and to charge the uninterruptible power supplies. The servers are doing a lot, but if you just look from outside at these boxes, using the energy, they trust electricity and emit it as heat. And this heat needs to be dissipated by cooling. And on an abstract level, every data center looks like this. Cloud or on-premise. But let's look at how the Cloud helps to increase the resource efficiency, and reduce the carbon footprint. First, let's go back to something you're already likely familiar with, the shared responsibility model of security, which you share with AWS. It says, AWS is responsible for the security of the Cloud, like physical data centers, managed services, and customers are responsible for the security in the Cloud using these managed services to, for example, configure a firewall in the VPC, or encrypt data. And we can apply the same concept of shared responsibility to sustainability. AWS designs things, builds things, like data centers, data halls, REX servers, and takes care of the material from the construction to the recycling. AWS, as you have seen in Adrian's part purchases the energy, and then ensures that the energy is used efficiently, and also other resources like water for cooling is used efficiently. And lastly, AWS service teams manage services, and take care to optimize them for sustainability. And customers responsibility on top of that is making architectural decisions. Selecting the services, using the services, and determined which code is running on these, and how efficient that is. How does the sustainability of the Cloud look like and how does it compare to on-premises operations? A typical data center is a mix of technology often under utilized, and with a lot of wasted energy and older equipment. For most organizations running data centers and IT equipment is not their core competency, and as such, they have less experience, relatively less experience, and investments into end-to-end efficiency improvements of their operations. In contrast to that, if you look at an AWS datacenter, the optimization begins with the purchase of energy, as you have seen in Adrian's part. Amazon is the largest corporate purchaser of renewable energies, and is far from being done here, as you saw in the recent announcements this week. But we are also investing in innovating to increase the energy efficiency. For example, the decentralized uninterruptible power supplies, and we also minimize the energy we use for cooling by using direct evaporative cooling or cooling with outside air. We manage centralized services, for example, for network and storage. And each service has a dedicated service team, which is managing the capacity according to the demand of the customers. And each team works on optimizing and reducing the cost of operating the services, and ultimately the energy and carbon footprint of the systems used to run AWS. Take the EC2 teams. They manage the fleet of instances used by customers, but if they are not used by customers, the service are still there. Of course, the service teams cannot dial down the infrastructure to the exact demand. There must be spare capacities, so it is there when you need it. That's why they incentivize the use of spare EC2 capacity within discount of up to 90% on demand pricing with EC2 spot instances. And this increases the overall utilization, and resource efficiency of the data centers. I'll take a higher level service like AWS Lambda. When Lambda was launched at re:Invent seven years ago, it was running with dedicated EC2 instances per customer. So it meets the desired level of isolation and security. Four years later already, it was running on all new services. Bare metal instances controlled by EC2 and Nitro with the virtualization technology called firecracker, which allows the launch of a new secure microVM in a fraction of a second. And this of course reduces the overhead also of the whole service. And this is just one example of how AWS service teams can optimize under the hood. You can find more information on how AWS helps to reduce the carbon emissions in these public reports from 451 Research for US, APAC, and Europe. One important factor of course, for the reduction is the growing share of renewable energies. But it's also very important how this energy is used. In the report for Europe, which has just been released last month, you can see, and this is highlighting how the energy use can be reduced by almost 80% by moving from on-premise data centers to the Cloud through more efficient facilities, more efficient servers, and the overall higher utilization of the Cloud. But what can customers do in their part of the responsibility? Over the last years, we've published five pillars in the AWS Well-Architected Framework, and they capture best practices for operational excellence, security, reliability, performance, and cost. And these all have to support business needs for fast time to value for features, and the delivery of products. However, today we have new problems, and we noticed that the ocean is rising. There's a climate crisis affecting our businesses, and we need to think about sustainability. Essentially, we need to optimize for the delivery of sustainable products. So that's why today we announced sustainability as the sixth pillar for the AWS Well-Architected Framework to meet this need. The sustainability pillar enhances the framework to provide a way for you to consistently measure architectures against best practices, and identify areas for improvement. And over time, it helps us to do our bit towards mitigating the climate crisis. The practice of sustainability when building Cloud workloads is to understand and quantify the impacts, and apply best practices to reduce these impacts. And the term sustainability is a broad field like covering social, and economic, and environmental aspects. And as this talk, that the pillar focuses on the environmental impacts, and especially resource efficiency, energy consumption, resource efficiency, as this is an important lever, architects have to improve and reduce the resource usage. How can you improve? Basically the improvement process that is outlined in the well-architected pillar is an iterative process. It's similar how we already optimizing for cost and performance for decades. First, you need to be aware of your KPIs, and the performance against these KPIs. And you also need a goal for improvements. You identify targets like looking at all your applications in your application landscape, and then you prioritize them by impact and by usage type, for example. Then you evaluate specific improvements. You make hypothesis like implementing auto-scaling, doing right-sizing, making an architectural change. Then you experiment, you deploy to production, and then you measure the results. Depending on the success, you either roll back unacceptable outcomes, or you spread the word. You look at ways to replicate the success to other workloads. And as long as you provide application teams with metrics, they can optimize against that. Which metrics make sense? I need metrics that can be measured frequently, that are delivered in a timely manner, and which I can break down to application teams so that application teams can say, yeah, this release we did last Monday had a bad or good impact on our metrics. And metrics need to align with resource usage, so that they are tangible for application teams. These metrics here are metrics I can draw from AWS services. I can look at resources such as compute, network, and storage and it is important to not look only at one metric, since they often compete with each other. For example, I can store my data in just one region, but then to serve my customers globally, I will have more data transfer. Or I can reduce my compute resources by storing more data, caching more data. And in the same way, the metrics compete with each other, also they compete with traditional non-functional requirements. Essentially, your sustainability KPIs are yet another nonfunctional requirement. And as such, you consider trade offs like adjusting costs. Moving processing work from your end user devices into your application backend, may increase the cost of your application, but it will also lower the demands to your end user devices. And maybe your application will not be responsible that this iPhone from last year need to be upgraded. And you can also make a trade off regarding the quality of the results. Sometimes it's okay to say there are hundreds of results instead of giving an exact figure. And we should avoid the pitfall to just look at the resources. When your usage is the same, but at the same time, your user base is decreasing, that's a cost for alarm. That's why you should factor in the business metrics to measure efficiency in resources, by unit of work, such as vCPU hours per connected vehicle mile, or megabyte of storage per customer. And this, by the way, you normalize KPIs to compare the performance over time. You need to get this tablet dashboards for the KPIs at the team level so that each team can own their goals and can optimize independently. This year is just one way to do this. Most of you are already familiar with the AWS cost and user tree parts for the sake of cost show backs, but as the name implies, it is a source for usage as well. And you can combine that with Amazon CloudWatch metrics and your business metrics and create that with Amazon Athena. Start by establishing a few KPIs, for example, in an Amazon QuickSight and start with KPIs where you have a large influence in the shared responsibility model, for example, EC2 Compute and experiment based on the feedback by your application teams. We look now at the process and the KPIs you need to establish, or you're suggesting to established in the sustainability pillar and these help us to identify workloads where you should invest with further deep dives and reviews. And the pillar also highlights best practices you should apply from these five areas. User behavior, software, and architecture, the hardware, the data management and the development and deployment process. And I would like to go over these best practice areas in detail. First, user behavior, best practices. They describe how you can align your workload to your customers usage to meet your sustainability goals. It's a lot of suggestions here, but in short look at when, where and how your customers are using your workload and what they don't use, is of course, potential for optimization and you can get rid of unused resources. And revisit the service levels you promise to your external, but also internal customers. I want to show an example of the impact of the architectural decisions and SLAs on the resource efficiency. Consider the SLA of your application requires an immediate fail over, and your service is already running into availability zones for high availability. For implementing the immediate fail over, you will have to have the capacity running of one AZ and being available in the other AZ so that when you have a fail over the other AZ can take over the additional workload. But as you saw to be able to successfully accomplish that, you have to have over 50% of the capacity, just waiting for the rare case of a fail over, which translates to 50% utilization. Now, if you run across three availability zones, you will have to have less capacity in the other two availability zones to handle the workload. In this case here, you have at least two thirds of the capacity available for your resources. So when a fail-over happens, your reserve capacity in the other two availability zones can take over. So as you see, you can run with higher utilization rates, across three availability zones to have enough capacity. If you want to optimize resiliency for sustainability, revisit the SLA, does it need to have an immediate fail over capability? If not, you can use cold capacity for failover. The trade off, you will have to consider is it takes a longer time to spin up the resources and your users may have to wait until their request is fulfilled. However, the upside is utilization. You don't have to have all that extra capacity waiting for the rare case of a fail over. One recommendation is to review the SLAs and negotiate impact-friendly SLAs. Yes, they might be negative effects like slower response times, but the upside is a higher resource efficiency. And for those stakeholders who can be convinced by US dollars, yes, less resources means less cost. The next area for best practices is reducing your impact by making changes to the software and architecture. And to sum up the previous slide, it is work less, store less, do work more efficiently, drive up the utilization by reducing idling resources, use sustainable scheduling strategies, steer work to more sustainable regions. To make it more concrete, let's pick the example of logging in your application. Review the details and the lock level and the detention. Use efficient formats and compression that matches the structure and the type of your logging. Use as in Kronos lock free logging. So your logging does not become the bottleneck. And when you don't care, when your lock analytics need to run, distribute your logs over time. You can imagine that many customers are running their analytics workloads at night at the full hour. And as regions have a different carbon intensity select regions near Amazon renewable energy projects or pick regions where the grid has published carbon intensity that is lower than in other regions. This curve here shows the resources used by an application. You see an average use and also peaks when the work load is all done at the same time. However, the resources and the energy use is not indicated by this curve, but it's indicated by the provision capacity line. And that provision capacity is needed to handle the peaks. Now let's consider that we can drive down these peaks by distributing your workloads over time, or by implementing a queue to smoothen the workload. We achieve a better ratio from the peaks to the average use and can dial down the provision capacity. This results in less resources and also less energy consumed. Next area for best practices from the pillar is minimize the amount of hardware that is needed to provision and deploy. In general, select the most efficient hardware for your individual workload. A general recommendation is do right-sizing not only select the right ratio from compute to memory and the size of the instance, and also features like GPU's and instance storage also, the processor type. One example is Graviton, already mentioned by Adrian. The Graviton2 processor has been launched already in 2019, Graviton3 this week and it remains the most power efficient processor AWS offers. The adoption can be as easy as switching a managed service like Amazon relational database or open search service to the corresponding Graviton type. And you can also move your code to Graviton with EC2 and also with Lambda. Next in the pillar are best practices around data management and storage and processing practices. For our data, we should think strategically about the type of storage that we use. Some data needs to be accessed fast and often, some data is never read once written. And if you decide for storage or service features with a relaxed durability, availability or response time, AWS can use this information to make trade offs and improve the resource efficiency and energy efficiency. The example here of Amazon S3, S3 One Zone-Infrequent access allows AWS to not send all objects over the wire to another availability zone. And in the same way, the extended retrieval times of glacier allow tradeoffs to use less energy and less infrastructure for operations. The general recommendation is look for opportunities to move your data to cold storage tiers, and also take a look at the announcements. This week, we also did two interesting announcements about EBS networks and in S3 for further storage tiers that you can leverage. Let me point out the case from an internal service AWS users for Lock archival to S3, to highlight the relevance of compression. The service teams looked for opportunities to reduce the resource use and experimented with different compression algorithms. Of course, the results will vary by the trade offs you're willing to make between speed and ratio and the types of data you compress but the compression in this example here, improved significantly coming from LZ4 and gzip to Z standard, and as many small things at Op, this reduced the required storage by overall one exabyte. And finally one area for the best practices by the pillar, look at your software life cycle to support improvements for resource efficiency. That includes of course, switching off test and dev environments when you do not use them, but also make it safe and easy to introduce and validate improvements off your own applications for resource efficiency and third party libraries. One example I would like to pick here is the AWS SDK for JavaScript. It's used almost always when a browser or node js application is using an AWS service. And as the many copies of these libraries at app, the team wanted to decrease the size of the libraries. With version three, they implemented a modular approach so that you can cherry pick the clients that are needed for your application, which resulted in a potential reduction of the size by 75%. And in further iterations, they trimmed the unnecessary code and build artifacts to reduce the packaged and install size by another 50%. Now we had a quick rundown of the process and the best practices from the well-architected pillar document to get more practical. Let's hear from Drew Engelson, Director of Engineering at Starbucks Technology, how he and his team implemented sustainability as a non-functional requirement. Thank you.
Thank you. Thank you, Steffen, thank you, Adrian. And welcome everybody. To inspire and nurture the human spirit, one person, one cup, one neighborhood at a time. This is the Starbucks mission statement. It serves as a guiding light a guidepost and a directional opportunity for us to understand and make decisions hopefully for the betterment of our customer experience and the planet. You'll see, there's no mention of coffee there. It's about people, it's about humanity. Yes, we sell coffee, but we really sell moments of joy. So Starbucks was founded in 1971. So for those who are really quick at math, that makes this our 50th anniversary. And over that time, we have made many investments in sustainability. I'll highlight just a few. So in 1985, we were one of the first retailers to offer a 10 cent discount for bringing in a reusable cup. And that was just one year into Starbucks selling coffee and cups. Prior to that, we were selling bulk coffee and tea. In 2008, LED Build, if you remember, had got a cold feeling, they weren't warming cozy like they are today. So we work with general electric to help develop the right feel for LED bulbs and put them in all of our stores. And in 2019, we updated our cold drink lids to eliminate the need for straws, reducing the overall plastic by about 9% and increasing the recyclability. And this past September Starbucks was recognized by the environmental protection agency as a green power leader for having 100% renewable energy in our company owned stores. And our CEO, Kevin Johnson routinely highlights the importance to our business of being planet positive. So trying to set the context that Starbucks itself really believes in sustainability and being green. Let's take a shift and look at what my team does. So I find it best to start here and help. This is familiar to some of you, the Starbucks app. It's a very popular app for ordering your Starbucks coffee for getting rewarded with stars and spending stars. I'll remind you what I remind my mother all the time, I don't build the app. This app is powered by several domains of APIs or engines, as I call them. So the first is the loyalty engine or Starbucks rewards and allows customers to, earn stars as they drink coffee and eventually it can earn enough to spend them on other caffeinated beverages. Second is the commerce engine. When you go and place that order with your phone, all those call requests are coming through our platform. We handle approximately two and a half million mobile orders on a daily basis in north America alone. Now these systems were built in the last two or three or four years. It was an amazing Greenfield opportunity to start from scratch, to build custom software Cloud native, using the best of breed technologies that helped us deliver on these capabilities. I'll give a quick overview of what some of that looks like. Lees run on AWS. We use an event driven microservice architecture. So in general requests are coming in. They can hand it off to Kafka then they're processed asynchronously wherever possible. Now the engineering team are building services or microservice is the smallest unit of the application that can be built and these services get deployed into Kubernetes pods, and we run just enough pods to be able to deliver our services to our customers. You see a lot of these things on this diagram were part of our optimization efforts and we'll talk about some of that in just a minute. So Starbucks has a great green mission. It's a mission that it resonates very much with me very well and gets me very excited to go to work in the morning. I still felt a bit of a gap in my day-to-day life. We're off building the rewards program. We're building the commerce engine. Starbucks is saying, and setting audacious green goals but I felt there was a gap between, making the link from what we do to helping participate in those broader statements. So I asked myself, what is the environmental impact of our systems? Could, and should we be doing better? What is our carbon footprint and what metrics should we be looking at as we think about reducing our impact? So I started out by reaching out to our global sustainability team. Those are the folks who are responsible for calculating and reporting the overall carbon footprint for Starbucks. I learned some very interesting things. One, they use a very course spend based model for estimating annual carbon emissions. I also learned that over 20% of our carbon footprint is attributed to dairy and less than 1% is attributed to Starbucks technology. So one of my key takeaways, well, I'm definitely putting oat milk in my macho lattes from now on technology has very low impact compared to other parts of the business. While that 1% seems low, we are a very large business. So 1% of a lot is still quite a big number. And we have opportunities to improve that as well. Another interesting takeaway is that because technology tends to be efficient by nature, we can leverage technology to actually offset and build projects, to reduce our carbon footprint outside of technology. I also learned that these annual spend model isn't granular enough or timely enough for me to make architectural decisions, to be able to make a change test and see how it impacted our carbon footprint. So ahead of mine, this dashboard, what if we can get near real-time metrics, if we can, perform a change and test and see whether or not we actually had positive or negative impact on our actual carbon footprint or our customer experience. So we did this during hack week. I partnered with our sustainability team analyzing AWS usage data Now I had no way to get any access to our actual carbon emissions. So we were left with figuring what are the right proxy metrics to look at to get a good understanding of our impact? Well, some easy ones are costs, cost is directly related to how much you're consuming in the Cloud. So we can get costs down. We probably having a lower impact on the planet. And similar to that, we look at CPU hours normalized based on the size of an instance. So making many assumptions and educated guesses, we built a dashboard that kind of gave us some numbers and some directional ideas about how well we're doing. Knowing the numbers, the absolute numbers were completely garbage, but relative from one month to the next to the next, we can figure out what direction we were going. And directional is really what we're looking for. Now, maybe perhaps more interesting than the actual carbon footprint, which I was really still going after is what opportunities do we have for being even more efficient. So we built in, everything we can think of that would, we could do to potentially reduce consumption, be greener. Some of these are very obvious and there's so many other areas what are quite nuanced. I mean, created this green score to show us what the gap is for what other opportunities we have to be greener. At that point, we were entirely on our own and just making stuff up and doing the best we can. We rent then reached out to AWS's sustainability team who was extremely helpful to help us validate some of our assumptions to make sense and provide a lot of recommendations and some data for us to help make better decisions. The one thing we did, we went through a very early version of the sustainability pillar, the well-architected review. We had been through many traditional well-architected reviews in the past and knew that we were pretty tightly optimized just from a performance and cost perspective. My intuition told me that we were also having a pretty good a lower impact on the environment as a result of those optimizations we already done. We also got an early version of some of the carbon footprint tool data sent to us and learnt that from 2019 to 2020, our actual carbon footprint was reduced by about 32%. Now, throughout this entire time, our business was growing like crazy. We had several record breaking mobile order days in 2020. And we went from 50 stores with our commerce engine to every store in north America, by the end of that year. So I shared this with our leadership, our CTO, and our chief sustainability officer that, Hey, look there and we reduced our footprint. And by the way, we saved money and our business has grown like crazy. And his response was, this is a big challenge. And technology actually offers some really interesting opportunities here where we can divorce the carbon reduction from business growth. Business grows, carbon goes down in these particular cases, the more we optimized. That's a legitimate win-win situation right there. So looking back a little bit, now, some of this, again, with hindsight, when we sort of just did the analysis and how do we pull some of that off? So first of all, it was extremely important to have great observability, great service level objectives. We couldn't really know if we were improving or not if we didn't know where our targets were, where we were headed. So we depend heavily on Datadog in our case, but whatever tool that does the job we'll do it, but it's important to have good observability and have an understanding of what your customers expect from their experience and what your SLAs are. We also knew that we were quite efficient by design. Cloud Native was cleaner, reportedly up to 88% cleaner than a traditional data center. We rely heavily on Kubernetes, which allows us to densely pack our services onto the infrastructure beneath it, really getting us very high utilization. We use binary protocols, GRPC is super efficient for communicating between our services. Many of our services are written in very efficient Scala. And we also with cost in mind are constantly optimizing. So I like to just say right-size everything all the time, make sure that if we are not utilizing resource, but we're paying for it, let's get rid of it. We don't need that. Rightsize instance types that we learned a lot about making sure that we can match an EC2 instance type two with a workload and there's so many EC2s there's one, that's perfect for the job. And it made things along those lines. You can see some examples here of where we do some auto-scaling tuning. We found that some of our services were asking for too much compute than what they actually needed. So based on the data, we were able to turn that down a little bit and have the auto scaling curve much more closely and more smoothly matched the actual demand curve. Some less obvious learnings. It's a little bit nuanced areas. And we're already hinted at actually by my predecessors here. Some regions are greener than others lower carbon regions. So if we can get access and understand where those are, all other things being equal, we might as well run these workloads in those lower carbon regions. We've heard a lot about Gravitas, this week. We switched some of our incidents types to arm. And I think the cost was about the same performance was the same. We did it for no other reason than it was more energy efficient. Spot is an interesting one as well. From a customer perspective, we're still using as much compute as we were, whether we use spot or not. It's an obvious target for optimizing by costs, but we believe it's the right thing to do in addition to the cost savings, it allows the Cloud provider as we saw earlier, to get much higher utilization of their infrastructure, it's already running, let's just use it. And another one we learned, which was also something you don't normally think about is, we have backup jobs running on a regular basis. And by default, it might run at the top of each hour, very predictably. But again, if every single customer of Amazon web services did that, and they do, I think have a crazy amount of peak. So we went and added kind of randomization to the time that some of these jobs run. Now, we talk mostly about Cloud but we're not unique here. We are a part of a much larger ecosystem. Data centers, Data transfer, Vendors, Cloud, End-user devices, each one of these areas, no matter what part of the business you're in, if you're making decisions about how to configure data center, how are you gonna build an application, how are you going to write a contract with the vendor, there is something you can do to help improve the sustainability of your workloads. So, as we already said, moving the data to the Cloud is much more efficient. You can favor vendors that have strong sustainability statements put out there in public. Data transfer is interesting because we have to move data back and forth, but let's make fewer calls. Let's make smaller calls. Let's shorten those calls and reduce our impact overall. I find end-user devices would be one of the most interesting areas here, because whatever it is, you're building a website, you're building a mobile app. It lands on your end user screen. And there's so many different ways to interpret and understand how interview's consumed on that screen. So for example, I like dark mode. Screens consume energy and sometimes the brighter they are, the more drain on the battery it is. Some colors require, on some screens require more energy. So dark mode is one way to potentially reduce the energy need for displaying a simple application or whatever it is. Blocking bots, bots, hitting your website are just complete wasted bots you don't want to have, to say, and even good bots. You can tell them don't come back for another week and don't every day. Lazy loading, reducing CPU, reducing page weight, these are all opportunities we have for improving. Looking at a website, for example, there's all sorts of tools out there for helping to understand, how green a website is. And you look at some of these safari tools at the bottom, you can see the CPU profiles spike. It might be interesting to look at that what's causing that spike? When sometimes when you hear your laptop fan worrying and worrying and worrying, it might be your laptop saying help, I can't do this anymore. Let's let's help them out, right? Let's not send up useless JavaScript. Let's reduce the size of images. Let's not auto play a video that is off the screen below the fold anyway. So there's a lot of things to think about. Some of these might seem like small negligible tweaks, but at a large scale with lots of volume, it can have a major impact overall. Plus you probably get a snap, your user experience. So real quick, I think we're low on time here. Overall, I believe that we should factor in carbon as just a cost and part of our total cost of ownership as I like to call it, and please, I beg for forgiveness already. TCO2. If we were to consider carbon as the thing we're optimizing for, and that's what it costs, we're making trade-offs. If carbon was the thing, what would we do? Would we have make different choices? in the Cloud, it's easy 'cause we tend to also align very closely with costs, but that's not always the case in different parts of the stack. So what do we do? I think it's very important to get the word out just in your company, start having conversations, get people excited about this. I find people are already excited about this when I bring it up. We recently started a greener technology Gilda at Starbucks, across the organization to help bring ideas together and see how we can start measuring and really have an impact overall. Make sure you include green goals in your projects as a non-functional requirement. Target low-hanging fruits, accelerate migration to the Cloud. There's lots of things we can do. And when you have your technology in order, you can use technology outside of technology to have a better impact. And here's just an example of one of the reasonable cup programs. Kiosks, you can drop a cup in, it gets washed automatically, and you can get a couple stars as a reward for that. And lastly, a couple great people I met along the way. ClimateAction.tech is a great slack community. And through that group, I learned about Tom Greenwood, "Sustainable Web Design" book. It's a great book and I greatly enjoyed it. So I'm going to hand it back to Adrian to wrap us up. Thanks very much. Thanks Drew, and really appreciate all the effort you put in to come here and present for us and the wonderful work that you've been doing. So just sort of divide this as a summary. If you're on the development site, you can optimize code, choose faster languages, fishing algorithms, do a bunch of things to just speed up your code, peat up the way you've building it. Then the operations side, you can configure systems to have the right instance types, get high utilization, automation, things like auto-scaling. Worry about these over specified requirements, archive and delete data sooner you duplicate, be very careful about times and locations. So all of these different things, but make sure you're doing this at scale. And you don't want to spend a lot of time optimizing something that is actually so small that you're spending more carbon thinking about it, then you're actually saving. So this really makes a huge difference at scale, but don't worry about the small things. Just want to mention this was announced yesterday, AWS Customer Carbon Footprint Tool it's gonna come soon. It includes the full cost that we'll show you how your sustainability investments go down over time. And we've talked a little bit about sort of choosing regions. So just very, very broad sort of things that you'll see here. Europe is pretty low carbon already. Like there's really not a lot you can do there to reduce the carbon because it's worth saving the energy, but it's largely a low carbon environment. The US, we're buying lots of energy. Carbon is going down really quickly. So yeah, it's on a good path. Asia is more problematic. There's a lot of very high carbon sources and it's very hard to buy renewable power there. And this is all very well known in the industry, but just to think about, if you're going to optimize a workload first deploy that optimization in Asia, if you have a nation workload that will make more difference than deploying it in Europe. Just think about it in those terms. And when you get access to the tool, you'll be able to see the actual behavior and where your competence is going. So that's pretty much it, just a call to action. One of the things you can do when you go back to your companies is just us asking questions when you're doing planning discussions. When you set goals for 2022, what are you doing about sustainability? Find areas where there's the biggest opportunity, to make a difference, really focus on where this is going to be a big thing. And then collect, share your sustainability optimization learnings, come back reinvent next year and tell us the same stories that we've heard from Starbucks from Drew. What have you done and how have you done it and what techniques have you learnt? So thank you very much. There are some other sessions you can go look up from re:Invent and we had a hackathon and a few other special screenings of videos that you can go find as well. So thank you very much. (audience applauding)

## Subtitles with Timestamps

[00:00](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=0s) (gentle music)

[00:01](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1s) Okay, hi, everybody.

[00:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3s) Thank you for coming to ARC325

[00:06](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=6s) architecting for sustainability.

[00:08](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=8s) I'm Adrian Cockcroft,

[00:10](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=10s) VP Sustainability Architecture for Amazon.

[00:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=14s) People ask me, "What does that mean?"

[00:16](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=16s) It means this.

[00:17](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=17s) This is actually kind of the title I have

[00:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=21s) for talking about architecting for sustainability.

[00:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=25s) I was previously with AWS working on open source,

[00:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=29s) and things like that.

[00:30](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=30s) Earlier this year, I switched to working for Amazon,

[00:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=34s) but focused on helping AWS and AWS customers

[00:38](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=38s) with their sustainability needs.

[00:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=41s) We'll have Steffen up next,

[00:42](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=42s) talking about the well-architected

[00:44](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=44s) guide for sustainability, the pillar

[00:46](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=46s) and Drew talking about how Starbucks

[00:49](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=49s) has optimized their architecture for sustainability.

[00:52](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=52s) I'll come back at the end

[00:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=53s) just for a few words to wrap it up.

[00:57](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=57s) So it's the overall of it.

[01:00](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=60s) Starting off talking about sustainability transformation.

[01:02](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=62s) What do we mean by that?

[01:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=63s) How are we partnering on sustainability?

[01:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=67s) Then Steffen will talk about how to architect.

[01:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=71s) We'll get the Starbucks talking.

[01:12](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=72s) I'll just talk a little bit about the end call to action

[01:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=74s) next steps for builders.

[01:17](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=77s) So sustainability transformation.

[01:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=80s) What does this mean?

[01:22](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=82s) Well, let's start talking about sustainability

[01:24](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=84s) to start with.

[01:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=85s) There's really four areas to sustainability.

[01:27](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=87s) One is decarbonizing everything we do.

[01:30](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=90s) The second one is water usage.

[01:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=92s) How do we use water effectively

[01:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=94s) make sure we're not polluting, and keep it clean?

[01:37](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=97s) Then there's social responsibility.

[01:38](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=98s) This is about knowing your supply chain,

[01:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=101s) knowing that the labor practices are good,

[01:43](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=103s) there's no false labor or child labor.

[01:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=105s) And then circular economy.

[01:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=107s) How do we make sure there's zero going to landfill,

[01:51](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=111s) and there's a lot of recycling?

[01:52](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=112s) Today, we focusing really

[01:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=113s) on the carbon part of this problem.

[01:59](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=119s) So sustainability is becoming an increasing trend

[02:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=123s) across the business.

[02:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=125s) We're seeing customer demand for this.

[02:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=127s) We're seeing increased government regulations,

[02:09](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=129s) driving all kinds of businesses

[02:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=131s) to worry about sustainability they didn't use to.

[02:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=134s) We're seeing a lot of employee demand,

[02:16](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=136s) a lot of enthusiasm for people that want to do something,

[02:19](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=139s) like I'm going to leave the world a better place

[02:22](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=142s) for your children is a common sort of phrase that we hear.

[02:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=145s) We're seeing investors that want to invest

[02:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=149s) in things which are helping the planet

[02:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=152s) rather than destroying the planet.

[02:33](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=153s) And we're also seeing sustainability

[02:36](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=156s) as competitive positioning across product lines.

[02:39](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=159s) Everyone knows what that looks like in the grocery store,

[02:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=161s) you see all of these brandings.

[02:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=165s) But what we've been doing for the last decade or so,

[02:48](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=168s) what I've been working on is digital transformation.

[02:51](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=171s) And what that means to me is that we were able to connect

[02:55](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=175s) to our customers and everything we made,

[02:58](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=178s) and we were able to use that to transform our businesses,

[03:01](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=181s) and build new kinds of services,

[03:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=183s) and new kinds of capabilities.

[03:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=185s) And speed everything up using Cloud.

[03:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=187s) So that's digital transformation.

[03:09](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=189s) You should all be pretty familiar with that by now.

[03:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=191s) But what we have to do now is use those same techniques,

[03:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=194s) but use them to decarbonize everything we do.

[03:17](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=197s) Measure it, decarbonize it, and do it at speed.

[03:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=201s) Do it quickly using the same techniques

[03:23](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=203s) that we used for digital transformation.

[03:27](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=207s) And it turns out that companies that figured out

[03:30](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=210s) digital transformation and sustainability transformation

[03:33](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=213s) are doing much better in the market.

[03:35](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=215s) The combination together is a very powerful thing.

[03:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=221s) But there's challenges.

[03:42](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=222s) How do you identify what your carbon emission hotspots are?

[03:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=227s) How do you reduce energy and water use in your operations?

[03:51](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=231s) How can you innovate faster to achieve this transformation?

[03:54](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=234s) And how do you collaborate with your supply chain

[03:57](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=237s) and your value chain to reduce the carbon emissions

[04:00](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=240s) across end to end?

[04:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=245s) And then the other thing that's different,

[04:06](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=246s) digital transformation happens in months or years

[04:09](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=249s) you should know fast enough, but months to years.

[04:12](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=252s) Sustainability, we're talking about decades.

[04:15](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=255s) And we say, well, you may have heard of people saying,

[04:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=260s) "Well, we have a pledge.

[04:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=261s) We're going to be carbon neutral in 2050."

[04:24](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=264s) How many people are still gonna be working

[04:26](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=266s) at that company in 2050

[04:27](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=267s) that are making that commitment now?

[04:31](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=271s) You can make all kinds of promises

[04:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=272s) you don't have to deliver on for 30 years.

[04:35](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=275s) So how can you deliver on a result that's decades away

[04:37](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=277s) and know that you're speeding up the process

[04:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=280s) of getting there?

[04:42](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=282s) So I'm gonna talk a bit about how Amazon's approaching that,

[04:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=285s) and then a bit more about how AWS is approaching that.

[04:51](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=291s) About two years ago, we announced The Climate Pledge.

[04:55](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=295s) This is to take the Paris Agreement,

[04:58](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=298s) which is a 2050 net-zero goal,

[05:00](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=300s) and bring it in 10 years earlier to 2040.

[05:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=303s) And to have a number of companies around the world,

[05:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=307s) join us in that pledge.

[05:09](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=309s) Now, around Earth Day, which is April this year,

[05:12](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=312s) we announced that we passed 100 signatories

[05:16](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=316s) in the Climate Pledge.

[05:17](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=317s) And at COP26, month or so ago,

[05:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=320s) we announced we'd passed 200 companies

[05:23](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=323s) in the Climate Pledge.

[05:24](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=324s) So this is growing very quickly, and I'd encourage you,

[05:27](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=327s) if your company has a goal to be sustainable,

[05:30](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=330s) take a look at The Climate Pledge,

[05:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=332s) reach out through your account team, reach out to me.

[05:35](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=335s) We can help figure out what does it take to help you get

[05:39](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=339s) to a 2040 commitment.

[05:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=341s) Because the more people we can get to 2040,

[05:44](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=344s) the more impact we can get

[05:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=345s) on the overall goal of getting the carbon for 2050 down

[05:51](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=351s) to the where it needs to be.

[05:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=353s) There's gonna be plenty of people that miss the 2050, right?

[05:56](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=356s) We need to have a lot of people that are early

[05:58](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=358s) to balance the people that are gonna be late.

[06:01](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=361s) So you need a path, oh.

[06:06](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=366s) So we've committed to net-zero carbon,

[06:08](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=368s) and then there's a path to 100% renewable energy by 2025

[06:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=371s) that Amazon as a whole is committed to as well.

[06:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=374s) And we also have this $2 billion Climate Pledge fund,

[06:17](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=377s) which has invested in a number of smaller startups

[06:19](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=379s) plus a company called Rivian.

[06:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=381s) And you may have seen the truck downstairs,

[06:23](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=383s) which is done very well recently.

[06:26](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=386s) So, The Climate Pledge has three principles.

[06:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=389s) Regular reporting, carbon elimination, and credible offsets.

[06:33](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=393s) And across many industries, many countries,

[06:36](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=396s) and many large brands from around the world.

[06:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=401s) So what do you get out of signing this?

[06:43](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=403s) So it's collaboration, we're sharing ideas.

[06:46](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=406s) We're trying to find a puff to look to carbon neutrality.

[06:51](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=411s) But these are the companies

[06:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=413s) who are the leaders and innovators in their markets

[06:55](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=415s) that have figured out how to get to an earlier commitment

[06:58](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=418s) and then there are other companies going well.

[07:01](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=421s) I'd like to get there, but I don't see how to get there.

[07:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=425s) So what we want to do is use these leaders

[07:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=427s) and innovators, document how they did it.

[07:10](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=430s) Discuss how they did it.

[07:12](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=432s) Collaboratively work together to help get there quickly

[07:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=434s) and then bring the next wave of people

[07:18](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=438s) into The Climate Pledge.

[07:19](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=439s) So that's what we're doing.

[07:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=441s) But also if you're a Climate Pledge signatory,

[07:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=445s) and the investors are looking at you,

[07:27](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=447s) there were these ESG funds,

[07:28](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=448s) environmental, social, and governance funds,

[07:31](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=451s) which are looking for investing in companies

[07:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=454s) which have a good sustainability record.

[07:36](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=456s) So it helps your branding in that sense.

[07:39](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=459s) And then there's always opportunities to lead

[07:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=461s) by sharing technologies,

[07:43](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=463s) and this is really to accelerate the progress.

[07:48](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=468s) If you look at how we've got there,

[07:50](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=470s) last three years, we've published our annual report.

[07:55](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=475s) You can find it on the website.

[07:56](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=476s) Incredible detail on what we're doing,

[07:59](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=479s) and across all of Amazons.

[08:01](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=481s) This is not just AWS.

[08:02](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=482s) We publish the entire company of Amazon,

[08:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=485s) and AWS is just a piece of that.

[08:08](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=488s) We've ordered these

[08:09](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=489s) 100,000 Rivian electric delivery vehicles.

[08:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=491s) We've reduced the weight of outbound packaging,

[08:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=494s) saved a million tons of cardboard and things like that.

[08:16](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=496s) And we're also the largest buyer

[08:19](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=499s) of renewable energy in the world.

[08:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=501s) And we recently announced, just a few days ago,

[08:24](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=504s) that we're now up to 12 gigawatts of energy under contract.

[08:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=509s) We're building new headquarters,

[08:30](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=510s) and that's got LEED platinum, it's sustainable.

[08:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=514s) These new buildings have no gas supply to the building.

[08:36](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=516s) They're fully electric.

[08:37](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=517s) And they're built out of low-carbon concrete,

[08:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=520s) low-carbon steel.

[08:42](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=522s) So building is one of the areas

[08:43](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=523s) that every company has buildings,

[08:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=525s) everyone needs to decarbonize

[08:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=527s) how they build their buildings,

[08:48](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=528s) and how they operate their buildings.

[08:50](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=530s) One of the big areas we're working on.

[08:52](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=532s) And then if you have an echo or a fire device,

[08:55](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=535s) we're actually working to offset the energy you use

[08:58](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=538s) in your house to run those devices.

[09:00](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=540s) We know which ones are turned on.

[09:02](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=542s) We know how much power they use.

[09:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=543s) We add that up, and we we're basically offsetting the energy

[09:06](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=546s) of the footprint of our devices.

[09:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=551s) If we look at AWS, we've done a lot of work on water

[09:17](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=557s) around data center cooling, and evaporative cooling,

[09:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=560s) and recycling the water.

[09:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=561s) So there's a very advanced set of processes there

[09:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=565s) around water management.

[09:27](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=567s) We've also optimized the energy

[09:30](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=570s) that comes into the data center from the edge,

[09:33](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=573s) and it gets supplied to the building.

[09:35](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=575s) There's a lot of conversion losses

[09:37](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=577s) before it actually gets to the CPU

[09:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=580s) that's going to run your workloads.

[09:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=581s) We reduce those energy losses by 35%.

[09:44](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=584s) And part of that was by going to a distributed UPS

[09:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=587s) that's actually lets you optimize

[09:50](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=590s) everything deeply in the system

[09:52](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=592s) rather than having a UPS for the entire building.

[09:56](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=596s) Obviously, we've been using the renewable energy

[09:58](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=598s) that Amazon as a whole has been buying

[10:00](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=600s) up to provide low-carbon energy for data centers.

[10:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=605s) We've got a low-carbon concrete data center design.

[10:08](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=608s) You've heard a lot about Graviton this week,

[10:10](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=610s) Graviton3 and Graviton2.

[10:12](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=612s) Very good performance per watt.

[10:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=614s) So you can reduce your carbon footprint

[10:17](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=617s) by just moving to Graviton.

[10:18](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=618s) And I'll talk a bit more about

[10:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=620s) the Amazon Sustainability Data Initiative.

[10:22](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=622s) This launched in 2018, and it's an Open Data Program.

[10:28](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=628s) Just going back to that carbon neutral data centre,

[10:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=632s) there's a European organization,

[10:33](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=633s) the Climate Neutral Data Centre Pact.

[10:35](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=635s) We've joined that, and we're building this commitment

[10:39](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=639s) to proactively lead the transition

[10:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=640s) to climate-neutral economy.

[10:44](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=644s) But data is central to addressing the climate crisis.

[10:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=647s) It's growing exponentially from new sources.

[10:50](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=650s) You heard in the keynote, certainly about satellites.

[10:54](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=654s) There were more and more satellites,

[10:56](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=656s) downloading more and more high resolution data,

[10:58](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=658s) as well as all the instrumentation we're getting

[11:00](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=660s) from the Internet of Things,

[11:02](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=662s) and all the metering we're doing

[11:04](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=664s) to figure out where our carbon footprint goes.

[11:06](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=666s) It's very diverse data.

[11:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=667s) There's lots of different people using it,

[11:10](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=670s) and lots of different applications for it.

[11:13](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=673s) So we have a few programs that can help here.

[11:17](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=677s) And we have an Open Data Program that in general,

[11:19](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=679s) if you have a data set, you own a dataset,

[11:22](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=682s) and you'd like to share it with the world.

[11:24](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=684s) Maybe it's petabytes in size.

[11:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=685s) That's fairly expensive to share it with the world.

[11:28](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=688s) But if you enter our Open Data Program,

[11:31](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=691s) we will zero out the cost of that S3 bucket to you.

[11:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=694s) You still own the data, it's your bucket,

[11:36](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=696s) but you share that to the world.

[11:38](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=698s) We zero out the cost,

[11:39](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=699s) and we cover all the transfer and usage costs.

[11:42](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=702s) So, it's free for you and it's free to use.

[11:44](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=704s) So we're taking that approach,

[11:46](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=706s) and we have a very large number of data sets

[11:48](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=708s) in this program.

[11:49](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=709s) A subset of that is Amazon Sustainability Data Initiative,

[11:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=713s) which is more focused on climate data.

[11:56](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=716s) And then we have a marketplace, AWS Data Exchange.

[12:01](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=721s) So ASDI is there to reduce the cost, time,

[12:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=725s) and technical barriers with dealing with these

[12:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=727s) very large data sets.

[12:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=731s) Lots of different data sources here,

[12:12](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=732s) Digital Globe, NASA, the Met Office, UK Met Office.

[12:17](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=737s) Climate data, we have models.

[12:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=740s) Climate data, air quality,

[12:22](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=742s) historical weather records forecasts,

[12:24](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=744s) all kinds of indicators.

[12:26](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=746s) So if you're trying to do something

[12:28](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=748s) that's more sort of global,

[12:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=749s) trying to figure out what's going on in your region,

[12:31](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=751s) you can actually aggregate all these data sets together.

[12:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=754s) We have a hackathon, the Code Green hackathon on Monday,

[12:38](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=758s) where we had teams come in work

[12:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=760s) on combining some of these data sets

[12:42](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=762s) to build some new capabilities.

[12:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=767s) We've also recently announced the first climate model,

[12:51](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=771s) the full climate models.

[12:52](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=772s) These are the things that are predicting

[12:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=773s) what's gonna happen

[12:55](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=775s) that we brought to the Cloud with NCAR.

[12:58](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=778s) And SilverLining is the nonprofit that's doing,

[13:00](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=780s) sort of working with NCAR to make this happen.

[13:06](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=786s) Then Data Exchange provides data sources as a marketplace.

[13:13](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=793s) So that's AWS as your sustainability partner.

[13:15](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=795s) But what problems you're trying to solve?

[13:18](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=798s) What are your biggest challenges related to sustainability?

[13:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=800s) How are you solving these issues?

[13:24](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=804s) We want to identify the cases, move to AWS,

[13:28](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=808s) and optimize those workloads.

[13:30](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=810s) Lots of different use cases.

[13:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=812s) Our professional services team has been working

[13:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=814s) across all these different areas,

[13:35](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=815s) and work through your account teams,

[13:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=820s) if you're working on one of these,

[13:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=821s) and we can bring in some experienced teams

[13:44](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=824s) that have built this for other organizations already.

[13:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=827s) One of those case studies is carrier with the cold chain,

[13:50](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=830s) keeping refrigeration working end-to-end

[13:52](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=832s) through the entire chain of activities.

[13:55](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=835s) Another one is using machine learning

[13:57](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=837s) to optimize the energy and water usage for Coca-Cola.

[14:04](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=844s) So lots of different ways.

[14:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=845s) We can migrate workloads to AWS.

[14:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=847s) And we even decode developed products with our customers

[14:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=851s) through the industry products group.

[14:13](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=853s) And one example there is Vector,

[14:16](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=856s) who had building metering system that can track

[14:19](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=859s) the energy usage of that customers.

[14:23](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=863s) So that's what I've got.

[14:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=865s) And we should look now optimizing Cloud workloads.

[14:30](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=870s) And I'm gonna bring up Steffen now to talk about that.

[14:36](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=876s) Yeah, thank you.
There you go.

[14:37](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=877s) Thank you, Adrian.

[14:39](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=879s) Yeah, I would like to talk about

[14:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=880s) how you architect for sustainability,

[14:43](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=883s) and reduce your environmental impact.

[14:48](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=888s) When we talk about the environmental impact,

[14:50](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=890s) one important factor for the climate change

[14:52](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=892s) and for the global warming is the emission of pollution

[14:55](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=895s) and emission by greenhouse gases.

[14:58](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=898s) One way to categorize and quantify these emissions

[15:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=903s) is the Greenhouse Gas Protocol,

[15:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=905s) which divides the emissions into three scopes.

[15:09](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=909s) It's measured in carbon dioxide equivalents

[15:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=911s) to also factor in other gases that support global warming.

[15:18](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=918s) Scope one is direct emissions.

[15:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=920s) Fuel, wood, anything which burns, or emits greenhouse gases.

[15:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=925s) To reduce that, you would electrify everything.

[15:28](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=928s) For example, by switching to electric vehicles,

[15:31](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=931s) or moving from gas ranges to induction ranges.

[15:36](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=936s) Scope two is emissions through purchased electricity.

[15:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=940s) If you electrify anything,

[15:42](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=942s) still the energy is having a carbon intensity,

[15:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=945s) because it's usually sourced,

[15:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=947s) for example, from a mix of wind, and solar, and coal.

[15:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=953s) And the emissions contribute to scope two.

[15:57](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=957s) To reduce that, you would use as much

[15:59](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=959s) renewable power as possible, and use the renewable energies,

[16:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=965s) for example, in batteries.

[16:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=967s) So it is there when you need it.

[16:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=971s) Scope three is indirect emissions,

[16:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=974s) all the way up and down your supply chain.

[16:17](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=977s) Scope three is depending a lot on your production depth,

[16:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=980s) the products and services you're delivering,

[16:22](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=982s) and how you deliver them.

[16:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=985s) Let's transfer these three scopes to data centers.

[16:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=989s) Looking at a typical data center,

[16:31](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=991s) you see the energy is coming from the grid.

[16:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=994s) It's usually a mix of renewables and fossil fuels.

[16:38](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=998s) And the carbon in the energy contributes to scope two.

[16:43](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1003s) Then you have a diesel generator for backup

[16:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1005s) if the grid is not available,

[16:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1007s) and its direct emissions contribute to scope one.

[16:50](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1010s) And then there are things which needs to be built

[16:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1013s) and delivered to the facilities like the building itself,

[16:57](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1017s) and also equipment like racks and servers.

[16:59](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1019s) And the carbon emitted for this contributes to scope three.

[17:06](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1026s) Zooming in close on the data center,

[17:09](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1029s) you see that the energy is distributed in the facilities

[17:12](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1032s) for the cooling to the service,

[17:15](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1035s) and to charge the uninterruptible power supplies.

[17:19](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1039s) The servers are doing a lot,

[17:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1041s) but if you just look from outside at these boxes,

[17:27](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1047s) using the energy,

[17:28](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1048s) they trust electricity and emit it as heat.

[17:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1052s) And this heat needs to be dissipated by cooling.

[17:35](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1055s) And on an abstract level, every data center looks like this.

[17:39](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1059s) Cloud or on-premise.

[17:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1061s) But let's look at how the Cloud helps

[17:43](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1063s) to increase the resource efficiency,

[17:46](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1066s) and reduce the carbon footprint.

[17:50](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1070s) First, let's go back to something

[17:52](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1072s) you're already likely familiar with,

[17:54](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1074s) the shared responsibility model of security,

[17:57](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1077s) which you share with AWS.

[18:00](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1080s) It says, AWS is responsible for the security of the Cloud,

[18:04](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1084s) like physical data centers, managed services,

[18:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1087s) and customers are responsible for the security in the Cloud

[18:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1091s) using these managed services to, for example,

[18:15](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1095s) configure a firewall in the VPC, or encrypt data.

[18:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1101s) And we can apply the same concept

[18:24](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1104s) of shared responsibility to sustainability.

[18:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1109s) AWS designs things, builds things,

[18:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1112s) like data centers, data halls, REX servers,

[18:37](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1117s) and takes care of the material from the construction

[18:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1120s) to the recycling.

[18:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1121s) AWS, as you have seen in Adrian's part

[18:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1125s) purchases the energy, and then ensures that the energy

[18:48](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1128s) is used efficiently, and also other resources

[18:52](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1132s) like water for cooling is used efficiently.

[18:55](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1135s) And lastly, AWS service teams manage services,

[19:00](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1140s) and take care to optimize them for sustainability.

[19:04](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1144s) And customers responsibility on top of that

[19:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1147s) is making architectural decisions.

[19:09](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1149s) Selecting the services, using the services,

[19:12](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1152s) and determined which code is running on these,

[19:15](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1155s) and how efficient that is.

[19:19](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1159s) How does the sustainability of the Cloud look like

[19:22](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1162s) and how does it compare to on-premises operations?

[19:26](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1166s) A typical data center is a mix of technology

[19:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1169s) often under utilized,

[19:31](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1171s) and with a lot of wasted energy and older equipment.

[19:37](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1177s) For most organizations running data centers and IT equipment

[19:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1181s) is not their core competency,

[19:43](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1183s) and as such, they have less experience,

[19:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1185s) relatively less experience,

[19:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1187s) and investments into end-to-end efficiency improvements

[19:50](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1190s) of their operations.

[19:54](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1194s) In contrast to that, if you look at an AWS datacenter,

[19:59](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1199s) the optimization begins with the purchase of energy,

[20:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1203s) as you have seen in Adrian's part.

[20:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1207s) Amazon is the largest corporate purchaser

[20:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1211s) of renewable energies, and is far from being done here,

[20:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1214s) as you saw in the recent announcements this week.

[20:18](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1218s) But we are also investing in innovating

[20:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1220s) to increase the energy efficiency.

[20:22](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1222s) For example, the decentralized

[20:24](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1224s) uninterruptible power supplies,

[20:26](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1226s) and we also minimize the energy we use for cooling

[20:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1232s) by using direct evaporative cooling

[20:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1234s) or cooling with outside air.

[20:39](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1239s) We manage centralized services,

[20:42](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1242s) for example, for network and storage.

[20:44](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1244s) And each service has a dedicated service team,

[20:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1247s) which is managing the capacity

[20:50](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1250s) according to the demand of the customers.

[20:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1253s) And each team works on optimizing and reducing the cost

[20:58](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1258s) of operating the services,

[21:01](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1261s) and ultimately the energy and carbon footprint

[21:04](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1264s) of the systems used to run AWS.

[21:09](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1269s) Take the EC2 teams.

[21:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1271s) They manage the fleet of instances used by customers,

[21:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1274s) but if they are not used by customers,

[21:16](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1276s) the service are still there.

[21:18](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1278s) Of course, the service teams cannot dial down

[21:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1281s) the infrastructure to the exact demand.

[21:24](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1284s) There must be spare capacities,

[21:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1285s) so it is there when you need it.

[21:28](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1288s) That's why they incentivize the use of spare EC2 capacity

[21:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1292s) within discount of up to 90% on demand pricing

[21:37](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1297s) with EC2 spot instances.

[21:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1300s) And this increases the overall utilization,

[21:42](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1302s) and resource efficiency of the data centers.

[21:48](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1308s) I'll take a higher level service like AWS Lambda.

[21:51](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1311s) When Lambda was launched at re:Invent seven years ago,

[21:55](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1315s) it was running with dedicated EC2 instances per customer.

[21:59](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1319s) So it meets the desired level of isolation and security.

[22:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1323s) Four years later already,

[22:04](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1324s) it was running on all new services.

[22:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1327s) Bare metal instances controlled by EC2 and Nitro

[22:10](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1330s) with the virtualization technology called firecracker,

[22:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1334s) which allows the launch of a new secure microVM

[22:17](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1337s) in a fraction of a second.

[22:19](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1339s) And this of course reduces the overhead

[22:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1341s) also of the whole service.

[22:24](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1344s) And this is just one example of how AWS service teams

[22:27](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1347s) can optimize under the hood.

[22:31](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1351s) You can find more information on how AWS helps to reduce

[22:35](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1355s) the carbon emissions in these public reports

[22:39](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1359s) from 451 Research for US, APAC, and Europe.

[22:44](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1364s) One important factor of course, for the reduction

[22:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1367s) is the growing share of renewable energies.

[22:50](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1370s) But it's also very important how this energy is used.

[22:55](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1375s) In the report for Europe,

[22:56](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1376s) which has just been released last month, you can see,

[22:59](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1379s) and this is highlighting how the energy use

[23:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1383s) can be reduced by almost 80%

[23:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1387s) by moving from on-premise data centers to the Cloud

[23:12](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1392s) through more efficient facilities, more efficient servers,

[23:16](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1396s) and the overall higher utilization of the Cloud.

[23:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1400s) But what can customers do

[23:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1401s) in their part of the responsibility?

[23:26](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1406s) Over the last years, we've published five pillars

[23:30](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1410s) in the AWS Well-Architected Framework,

[23:33](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1413s) and they capture best practices for operational excellence,

[23:36](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1416s) security, reliability, performance, and cost.

[23:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1420s) And these all have to support business needs

[23:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1425s) for fast time to value for features,

[23:48](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1428s) and the delivery of products.

[23:51](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1431s) However, today we have new problems,

[23:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1433s) and we noticed that the ocean is rising.

[23:57](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1437s) There's a climate crisis affecting our businesses,

[24:00](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1440s) and we need to think about sustainability.

[24:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1443s) Essentially, we need to optimize for the delivery

[24:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1447s) of sustainable products.

[24:10](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1450s) So that's why today we announced sustainability

[24:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1454s) as the sixth pillar for the AWS Well-Architected Framework

[24:19](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1459s) to meet this need.

[24:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1461s) The sustainability pillar enhances the framework

[24:24](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1464s) to provide a way for you to consistently measure

[24:27](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1467s) architectures against best practices,

[24:30](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1470s) and identify areas for improvement.

[24:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1472s) And over time, it helps us to do our bit towards

[24:37](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1477s) mitigating the climate crisis.

[24:42](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1482s) The practice of sustainability when building Cloud workloads

[24:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1485s) is to understand and quantify the impacts,

[24:48](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1488s) and apply best practices to reduce these impacts.

[24:52](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1492s) And the term sustainability is a broad field

[24:56](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1496s) like covering social, and economic,

[24:59](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1499s) and environmental aspects.

[25:01](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1501s) And as this talk,

[25:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1503s) that the pillar focuses on the environmental impacts,

[25:06](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1506s) and especially resource efficiency, energy consumption,

[25:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1511s) resource efficiency, as this is an important lever,

[25:15](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1515s) architects have to improve and reduce the resource usage.

[25:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1521s) How can you improve?

[25:24](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1524s) Basically the improvement process that is outlined

[25:28](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1528s) in the well-architected pillar is an iterative process.

[25:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1532s) It's similar how we already optimizing for cost

[25:35](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1535s) and performance for decades.

[25:38](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1538s) First, you need to be aware of your KPIs,

[25:42](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1542s) and the performance against these KPIs.

[25:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1545s) And you also need a goal for improvements.

[25:49](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1549s) You identify targets like looking at all your applications

[25:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1553s) in your application landscape,

[25:54](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1554s) and then you prioritize them by impact

[25:56](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1556s) and by usage type, for example.

[26:00](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1560s) Then you evaluate specific improvements.

[26:02](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1562s) You make hypothesis like implementing auto-scaling,

[26:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1567s) doing right-sizing, making an architectural change.

[26:10](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1570s) Then you experiment, you deploy to production,

[26:13](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1573s) and then you measure the results.

[26:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1574s) Depending on the success,

[26:16](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1576s) you either roll back unacceptable outcomes,

[26:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1580s) or you spread the word.

[26:22](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1582s) You look at ways to replicate the success

[26:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1585s) to other workloads.

[26:27](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1587s) And as long as you provide application teams with metrics,

[26:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1592s) they can optimize against that.

[26:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1594s) Which metrics make sense?

[26:36](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1596s) I need metrics that can be measured frequently,

[26:39](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1599s) that are delivered in a timely manner,

[26:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1601s) and which I can break down to application teams

[26:44](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1604s) so that application teams can say,

[26:46](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1606s) yeah, this release we did last Monday

[26:49](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1609s) had a bad or good impact on our metrics.

[26:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1613s) And metrics need to align with resource usage,

[26:57](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1617s) so that they are tangible for application teams.

[27:02](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1622s) These metrics here are metrics I can draw from AWS services.

[27:06](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1626s) I can look at resources

[27:08](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1628s) such as compute, network, and storage

[27:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1631s) and it is important to not look only at one metric,

[27:15](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1635s) since they often compete with each other.

[27:18](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1638s) For example, I can store my data in just one region,

[27:23](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1643s) but then to serve my customers globally,

[27:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1645s) I will have more data transfer.

[27:28](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1648s) Or I can reduce my compute resources by storing more data,

[27:33](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1653s) caching more data.

[27:37](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1657s) And in the same way, the metrics compete with each other,

[27:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1660s) also they compete with traditional

[27:44](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1664s) non-functional requirements.

[27:46](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1666s) Essentially, your sustainability KPIs

[27:49](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1669s) are yet another nonfunctional requirement.

[27:52](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1672s) And as such, you consider trade offs like adjusting costs.

[27:55](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1675s) Moving processing work from your end user devices

[27:59](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1679s) into your application backend,

[28:01](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1681s) may increase the cost of your application,

[28:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1685s) but it will also lower the demands to your end user devices.

[28:09](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1689s) And maybe your application will not be responsible

[28:12](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1692s) that this iPhone from last year need to be upgraded.

[28:17](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1697s) And you can also make a trade off

[28:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1700s) regarding the quality of the results.

[28:23](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1703s) Sometimes it's okay to say there are hundreds of results

[28:26](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1706s) instead of giving an exact figure.

[28:30](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1710s) And we should avoid the pitfall

[28:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1712s) to just look at the resources.

[28:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1714s) When your usage is the same, but at the same time,

[28:38](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1718s) your user base is decreasing, that's a cost for alarm.

[28:42](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1722s) That's why you should factor in the business metrics

[28:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1725s) to measure efficiency in resources, by unit of work,

[28:49](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1729s) such as vCPU hours per connected vehicle mile,

[28:54](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1734s) or megabyte of storage per customer.

[28:57](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1737s) And this, by the way,

[28:58](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1738s) you normalize KPIs to compare the performance over time.

[29:04](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1744s) You need to get this tablet dashboards for the KPIs

[29:08](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1748s) at the team level so that each team can own

[29:10](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1750s) their goals and can optimize independently.

[29:16](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1756s) This year is just one way to do this.

[29:18](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1758s) Most of you are already familiar with the AWS cost

[29:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1761s) and user tree parts for the sake of cost show backs,

[29:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1765s) but as the name implies, it is a source for usage as well.

[29:28](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1768s) And you can combine that with Amazon CloudWatch metrics

[29:33](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1773s) and your business metrics

[29:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1774s) and create that with Amazon Athena.

[29:37](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1777s) Start by establishing a few KPIs,

[29:39](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1779s) for example, in an Amazon QuickSight

[29:42](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1782s) and start with KPIs where you have a large influence

[29:46](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1786s) in the shared responsibility model,

[29:48](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1788s) for example, EC2 Compute

[29:50](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1790s) and experiment based on the feedback

[29:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1793s) by your application teams.

[29:56](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1796s) We look now at the process and the KPIs

[29:59](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1799s) you need to establish,

[30:01](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1801s) or you're suggesting to established

[30:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1803s) in the sustainability pillar

[30:04](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1804s) and these help us to identify workloads

[30:09](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1809s) where you should invest with further deep dives and reviews.

[30:15](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1815s) And the pillar also highlights best practices

[30:17](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1817s) you should apply from these five areas.

[30:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1820s) User behavior, software, and architecture,

[30:23](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1823s) the hardware, the data management

[30:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1825s) and the development and deployment process.

[30:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1829s) And I would like to go

[30:30](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1830s) over these best practice areas in detail.

[30:36](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1836s) First, user behavior, best practices.

[30:39](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1839s) They describe how you can align your workload

[30:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1841s) to your customers usage

[30:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1845s) to meet your sustainability goals.

[30:48](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1848s) It's a lot of suggestions here,

[30:51](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1851s) but in short look at when, where

[30:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1853s) and how your customers are using your workload

[30:56](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1856s) and what they don't use, is of course,

[30:59](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1859s) potential for optimization

[31:02](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1862s) and you can get rid of unused resources.

[31:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1865s) And revisit the service levels

[31:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1867s) you promise to your external,

[31:10](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1870s) but also internal customers.

[31:13](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1873s) I want to show an example of the impact

[31:16](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1876s) of the architectural decisions and SLAs

[31:19](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1879s) on the resource efficiency.

[31:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1881s) Consider the SLA of your application requires

[31:24](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1884s) an immediate fail over,

[31:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1885s) and your service is already running into availability zones

[31:28](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1888s) for high availability.

[31:33](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1893s) For implementing the immediate fail over,

[31:36](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1896s) you will have to have the capacity running of one AZ

[31:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1901s) and being available in the other AZ

[31:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1905s) so that when you have a fail over

[31:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1907s) the other AZ can take over the additional workload.

[31:51](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1911s) But as you saw to be able to successfully accomplish that,

[31:55](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1915s) you have to have over 50% of the capacity, just waiting

[31:59](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1919s) for the rare case of a fail over,

[32:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1923s) which translates to 50% utilization.

[32:06](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1926s) Now, if you run across three availability zones,

[32:10](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1930s) you will have to have less capacity

[32:13](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1933s) in the other two availability zones

[32:18](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1938s) to handle the workload.

[32:19](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1939s) In this case here, you have at least two thirds

[32:23](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1943s) of the capacity available for your resources.

[32:27](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1947s) So when a fail-over happens,

[32:28](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1948s) your reserve capacity in the other two availability zones

[32:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1952s) can take over.

[32:35](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1955s) So as you see, you can run with higher utilization rates,

[32:39](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1959s) across three availability zones to have enough capacity.

[32:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1965s) If you want to optimize resiliency for sustainability,

[32:48](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1968s) revisit the SLA,

[32:51](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1971s) does it need to have an immediate fail over capability?

[32:54](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1974s) If not, you can use cold capacity for failover.

[32:58](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1978s) The trade off, you will have to consider

[33:00](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1980s) is it takes a longer time to spin up the resources

[33:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1983s) and your users may have to wait

[33:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1985s) until their request is fulfilled.

[33:08](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1988s) However, the upside is utilization.

[33:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1991s) You don't have to have all that extra capacity

[33:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=1994s) waiting for the rare case of a fail over.

[33:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2001s) One recommendation is to review the SLAs

[33:23](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2003s) and negotiate impact-friendly SLAs.

[33:26](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2006s) Yes, they might be negative effects

[33:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2009s) like slower response times,

[33:31](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2011s) but the upside is a higher resource efficiency.

[33:38](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2018s) And for those stakeholders

[33:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2020s) who can be convinced by US dollars,

[33:42](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2022s) yes, less resources means less cost.

[33:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2027s) The next area for best practices is reducing your impact

[33:51](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2031s) by making changes to the software and architecture.

[33:54](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2034s) And to sum up the previous slide,

[33:57](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2037s) it is work less, store less, do work more efficiently,

[34:02](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2042s) drive up the utilization by reducing idling resources,

[34:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2047s) use sustainable scheduling strategies,

[34:09](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2049s) steer work to more sustainable regions.

[34:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2054s) To make it more concrete,

[34:15](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2055s) let's pick the example of logging in your application.

[34:18](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2058s) Review the details and the lock level and the detention.

[34:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2061s) Use efficient formats and compression

[34:24](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2064s) that matches the structure and the type of your logging.

[34:28](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2068s) Use as in Kronos lock free logging.

[34:30](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2070s) So your logging does not become the bottleneck.

[34:33](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2073s) And when you don't care,

[34:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2074s) when your lock analytics need to run,

[34:38](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2078s) distribute your logs over time.

[34:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2080s) You can imagine that many customers

[34:42](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2082s) are running their analytics workloads

[34:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2085s) at night at the full hour.

[34:48](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2088s) And as regions have a different carbon intensity

[34:52](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2092s) select regions near Amazon renewable energy projects

[34:55](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2095s) or pick regions where the grid

[34:59](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2099s) has published carbon intensity

[35:01](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2101s) that is lower than in other regions.

[35:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2105s) This curve here shows the resources used by an application.

[35:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2111s) You see an average use

[35:13](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2113s) and also peaks when the work load

[35:16](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2116s) is all done at the same time.

[35:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2120s) However, the resources and the energy use

[35:23](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2123s) is not indicated by this curve,

[35:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2125s) but it's indicated by the provision capacity line.

[35:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2129s) And that provision capacity is needed to handle the peaks.

[35:33](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2133s) Now let's consider that we can drive down these peaks

[35:37](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2137s) by distributing your workloads over time,

[35:39](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2139s) or by implementing a queue to smoothen the workload.

[35:43](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2143s) We achieve a better ratio from the peaks

[35:46](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2146s) to the average use and can dial down the provision capacity.

[35:51](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2151s) This results in less resources

[35:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2153s) and also less energy consumed.

[35:57](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2157s) Next area for best practices from the pillar

[36:02](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2162s) is minimize the amount of hardware

[36:04](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2164s) that is needed to provision and deploy.

[36:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2167s) In general, select the most efficient hardware

[36:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2171s) for your individual workload.

[36:13](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2173s) A general recommendation is do right-sizing

[36:16](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2176s) not only select the right ratio

[36:19](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2179s) from compute to memory and the size of the instance,

[36:23](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2183s) and also features like GPU's and instance storage

[36:26](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2186s) also, the processor type.

[36:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2189s) One example is Graviton, already mentioned by Adrian.

[36:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2194s) The Graviton2 processor has been launched already in 2019,

[36:38](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2198s) Graviton3 this week

[36:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2200s) and it remains the most power efficient

[36:42](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2202s) processor AWS offers.

[36:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2205s) The adoption can be as easy

[36:46](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2206s) as switching a managed service

[36:48](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2208s) like Amazon relational database

[36:49](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2209s) or open search service to the corresponding Graviton type.

[36:55](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2215s) And you can also move your code to Graviton with EC2

[36:58](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2218s) and also with Lambda.

[37:02](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2222s) Next in the pillar are best practices

[37:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2225s) around data management and storage

[37:08](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2228s) and processing practices.

[37:10](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2230s) For our data, we should think strategically

[37:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2234s) about the type of storage that we use.

[37:18](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2238s) Some data needs to be accessed fast and often,

[37:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2241s) some data is never read once written.

[37:24](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2244s) And if you decide for storage or service features

[37:27](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2247s) with a relaxed durability, availability or response time,

[37:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2252s) AWS can use this information

[37:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2254s) to make trade offs and improve the resource efficiency

[37:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2260s) and energy efficiency.

[37:43](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2263s) The example here of Amazon S3,

[37:46](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2266s) S3 One Zone-Infrequent access allows AWS

[37:49](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2269s) to not send all objects over the wire

[37:52](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2272s) to another availability zone.

[37:54](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2274s) And in the same way,

[37:55](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2275s) the extended retrieval times of glacier allow tradeoffs

[38:00](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2280s) to use less energy and less infrastructure for operations.

[38:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2285s) The general recommendation is look for opportunities

[38:09](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2289s) to move your data to cold storage tiers,

[38:12](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2292s) and also take a look at the announcements.

[38:16](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2296s) This week, we also did two interesting announcements

[38:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2300s) about EBS networks and in S3

[38:24](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2304s) for further storage tiers that you can leverage.

[38:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2309s) Let me point out the case

[38:30](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2310s) from an internal service AWS users

[38:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2312s) for Lock archival to S3,

[38:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2314s) to highlight the relevance of compression.

[38:38](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2318s) The service teams looked for opportunities

[38:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2320s) to reduce the resource use

[38:42](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2322s) and experimented with different compression algorithms.

[38:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2327s) Of course, the results will vary by the trade offs

[38:50](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2330s) you're willing to make between speed and ratio

[38:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2333s) and the types of data you compress

[38:55](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2335s) but the compression in this example here,

[38:58](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2338s) improved significantly coming from LZ4 and gzip

[39:02](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2342s) to Z standard, and as many small things

[39:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2345s) at Op, this reduced the required storage

[39:09](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2349s) by overall one exabyte.

[39:12](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2352s) And finally one area for the best practices by the pillar,

[39:16](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2356s) look at your software life cycle

[39:18](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2358s) to support improvements for resource efficiency.

[39:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2361s) That includes of course,

[39:23](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2363s) switching off test and dev environments

[39:26](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2366s) when you do not use them,

[39:28](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2368s) but also make it safe and easy to introduce and validate

[39:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2372s) improvements off your own applications

[39:35](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2375s) for resource efficiency and third party libraries.

[39:39](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2379s) One example I would like to pick here

[39:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2381s) is the AWS SDK for JavaScript.

[39:44](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2384s) It's used almost always when a browser

[39:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2387s) or node js application is using an AWS service.

[39:51](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2391s) And as the many copies of these libraries at app,

[39:54](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2394s) the team wanted to decrease the size of the libraries.

[39:57](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2397s) With version three, they implemented

[39:59](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2399s) a modular approach so that you can cherry pick

[40:02](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2402s) the clients that are needed for your application,

[40:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2405s) which resulted in a potential reduction of the size by 75%.

[40:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2411s) And in further iterations,

[40:12](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2412s) they trimmed the unnecessary code and build artifacts

[40:16](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2416s) to reduce the packaged and install size by another 50%.

[40:23](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2423s) Now we had a quick rundown of the process

[40:26](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2426s) and the best practices

[40:27](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2427s) from the well-architected pillar document

[40:30](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2430s) to get more practical.

[40:31](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2431s) Let's hear from Drew Engelson,

[40:33](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2433s) Director of Engineering at Starbucks Technology,

[40:36](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2436s) how he and his team implemented sustainability

[40:39](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2439s) as a non-functional requirement.

[40:43](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2443s) Thank you.
Thank you.

[40:46](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2446s) Thank you, Steffen, thank you, Adrian.

[40:49](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2449s) And welcome everybody.

[40:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2453s) To inspire and nurture the human spirit,

[40:56](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2456s) one person, one cup, one neighborhood at a time.

[41:00](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2460s) This is the Starbucks mission statement.

[41:02](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2462s) It serves as a guiding light

[41:04](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2464s) a guidepost and a directional opportunity

[41:09](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2469s) for us to understand and make decisions

[41:10](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2470s) hopefully for the betterment

[41:13](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2473s) of our customer experience and the planet.

[41:17](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2477s) You'll see, there's no mention of coffee there.

[41:19](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2479s) It's about people, it's about humanity.

[41:22](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2482s) Yes, we sell coffee, but we really sell moments of joy.

[41:31](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2491s) So Starbucks was founded in 1971.

[41:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2494s) So for those who are really quick at math,

[41:35](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2495s) that makes this our 50th anniversary.

[41:38](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2498s) And over that time,

[41:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2500s) we have made many investments in sustainability.

[41:43](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2503s) I'll highlight just a few.

[41:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2505s) So in 1985, we were one of the first retailers

[41:48](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2508s) to offer a 10 cent discount for bringing in a reusable cup.

[41:52](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2512s) And that was just one year into Starbucks

[41:55](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2515s) selling coffee and cups.

[41:57](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2517s) Prior to that, we were selling bulk coffee and tea.

[42:00](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2520s) In 2008, LED Build, if you remember,

[42:06](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2526s) had got a cold feeling,

[42:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2527s) they weren't warming cozy like they are today.

[42:10](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2530s) So we work with general electric

[42:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2531s) to help develop the right feel for LED bulbs

[42:16](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2536s) and put them in all of our stores.

[42:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2540s) And in 2019, we updated our cold drink lids

[42:24](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2544s) to eliminate the need for straws,

[42:26](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2546s) reducing the overall plastic by about 9%

[42:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2549s) and increasing the recyclability.

[42:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2552s) And this past September Starbucks was recognized

[42:35](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2555s) by the environmental protection agency

[42:37](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2557s) as a green power leader for having 100% renewable energy

[42:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2561s) in our company owned stores.

[42:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2565s) And our CEO, Kevin Johnson routinely highlights

[42:49](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2569s) the importance to our business of being planet positive.

[42:52](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2572s) So trying to set the context

[42:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2573s) that Starbucks itself really believes in sustainability

[42:58](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2578s) and being green.

[42:59](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2579s) Let's take a shift and look at what my team does.

[43:02](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2582s) So I find it best to start here and help.

[43:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2585s) This is familiar to some of you, the Starbucks app.

[43:10](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2590s) It's a very popular app for ordering your Starbucks coffee

[43:13](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2593s) for getting rewarded with stars and spending stars.

[43:18](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2598s) I'll remind you what I remind my mother all the time,

[43:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2601s) I don't build the app.

[43:23](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2603s) This app is powered by several domains of APIs

[43:27](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2607s) or engines, as I call them.

[43:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2609s) So the first is the loyalty engine or Starbucks rewards

[43:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2612s) and allows customers to, earn stars as they drink coffee

[43:36](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2616s) and eventually it can earn enough

[43:38](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2618s) to spend them on other caffeinated beverages.

[43:43](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2623s) Second is the commerce engine.

[43:44](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2624s) When you go and place that order with your phone,

[43:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2627s) all those call requests are coming through our platform.

[43:50](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2630s) We handle approximately two and a half million

[43:54](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2634s) mobile orders on a daily basis in north America alone.

[43:59](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2639s) Now these systems were built

[44:00](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2640s) in the last two or three or four years.

[44:04](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2644s) It was an amazing Greenfield opportunity

[44:06](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2646s) to start from scratch,

[44:08](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2648s) to build custom software Cloud native,

[44:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2651s) using the best of breed technologies

[44:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2654s) that helped us deliver on these capabilities.

[44:17](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2657s) I'll give a quick overview of what some of that looks like.

[44:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2660s) Lees run on AWS.

[44:22](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2662s) We use an event driven microservice architecture.

[44:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2665s) So in general requests are coming in.

[44:27](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2667s) They can hand it off to Kafka

[44:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2669s) then they're processed asynchronously wherever possible.

[44:33](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2673s) Now the engineering team are building services

[44:37](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2677s) or microservice is the smallest unit of the application

[44:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2681s) that can be built

[44:43](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2683s) and these services get deployed into Kubernetes pods,

[44:46](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2686s) and we run just enough pods

[44:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2687s) to be able to deliver our services to our customers.

[44:52](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2692s) You see a lot of these things on this diagram

[44:54](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2694s) were part of our optimization efforts

[44:57](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2697s) and we'll talk about some of that in just a minute.

[45:00](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2700s) So Starbucks has a great green mission.

[45:04](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2704s) It's a mission that it resonates very much with me very well

[45:08](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2708s) and gets me very excited to go to work in the morning.

[45:12](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2712s) I still felt a bit of a gap in my day-to-day life.

[45:15](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2715s) We're off building the rewards program.

[45:17](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2717s) We're building the commerce engine.

[45:19](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2719s) Starbucks is saying, and setting audacious green goals

[45:23](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2723s) but I felt there was a gap between,

[45:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2725s) making the link from what we do to helping participate

[45:30](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2730s) in those broader statements.

[45:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2732s) So I asked myself,

[45:33](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2733s) what is the environmental impact of our systems?

[45:36](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2736s) Could, and should we be doing better?

[45:39](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2739s) What is our carbon footprint

[45:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2740s) and what metrics should we be looking at

[45:42](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2742s) as we think about reducing our impact?

[45:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2747s) So I started out by reaching out

[45:48](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2748s) to our global sustainability team.

[45:50](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2750s) Those are the folks who are responsible

[45:52](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2752s) for calculating and reporting

[45:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2753s) the overall carbon footprint for Starbucks.

[45:57](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2757s) I learned some very interesting things.

[45:59](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2759s) One, they use a very course spend based model

[46:02](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2762s) for estimating annual carbon emissions.

[46:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2765s) I also learned that over 20% of our carbon footprint

[46:08](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2768s) is attributed to dairy

[46:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2771s) and less than 1% is attributed to Starbucks technology.

[46:16](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2776s) So one of my key takeaways,

[46:17](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2777s) well, I'm definitely putting oat milk

[46:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2780s) in my macho lattes from now on

[46:23](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2783s) technology has very low impact

[46:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2785s) compared to other parts of the business.

[46:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2789s) While that 1% seems low, we are a very large business.

[46:33](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2793s) So 1% of a lot is still quite a big number.

[46:37](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2797s) And we have opportunities to improve that as well.

[46:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2801s) Another interesting takeaway

[46:42](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2802s) is that because technology tends to be efficient by nature,

[46:46](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2806s) we can leverage technology to actually offset

[46:49](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2809s) and build projects, to reduce our carbon footprint

[46:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2813s) outside of technology.

[46:56](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2816s) I also learned that these annual spend model

[46:58](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2818s) isn't granular enough or timely enough

[47:01](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2821s) for me to make architectural decisions,

[47:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2823s) to be able to make a change test

[47:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2825s) and see how it impacted our carbon footprint.

[47:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2831s) So ahead of mine, this dashboard,

[47:12](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2832s) what if we can get near real-time metrics,

[47:16](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2836s) if we can, perform a change and test

[47:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2840s) and see whether or not we actually had positive

[47:23](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2843s) or negative impact on our actual carbon footprint

[47:27](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2847s) or our customer experience.

[47:30](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2850s) So we did this during hack week.

[47:31](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2851s) I partnered with our sustainability team

[47:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2854s) analyzing AWS usage data

[47:37](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2857s) Now I had no way to get any access

[47:39](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2859s) to our actual carbon emissions.

[47:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2861s) So we were left with figuring

[47:42](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2862s) what are the right proxy metrics to look at

[47:44](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2864s) to get a good understanding of our impact?

[47:49](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2869s) Well, some easy ones are costs,

[47:50](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2870s) cost is directly related

[47:52](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2872s) to how much you're consuming in the Cloud.

[47:55](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2875s) So we can get costs down.

[47:56](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2876s) We probably having a lower impact on the planet.

[47:59](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2879s) And similar to that, we look at CPU hours normalized

[48:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2883s) based on the size of an instance.

[48:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2885s) So making many assumptions and educated guesses,

[48:09](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2889s) we built a dashboard that kind of gave us

[48:12](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2892s) some numbers and some directional ideas

[48:15](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2895s) about how well we're doing.

[48:17](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2897s) Knowing the numbers, the absolute numbers

[48:19](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2899s) were completely garbage,

[48:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2900s) but relative from one month to the next to the next,

[48:24](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2904s) we can figure out what direction we were going.

[48:26](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2906s) And directional is really what we're looking for.

[48:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2909s) Now, maybe perhaps more interesting

[48:31](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2911s) than the actual carbon footprint,

[48:33](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2913s) which I was really still going after

[48:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2914s) is what opportunities do we have

[48:36](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2916s) for being even more efficient.

[48:38](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2918s) So we built in, everything we can think of that would,

[48:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2921s) we could do to potentially reduce consumption, be greener.

[48:46](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2926s) Some of these are very obvious

[48:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2927s) and there's so many other areas what are quite nuanced.

[48:50](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2930s) I mean, created this green score

[48:51](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2931s) to show us what the gap is

[48:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2933s) for what other opportunities we have to be greener.

[48:59](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2939s) At that point, we were entirely on our own

[49:01](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2941s) and just making stuff up and doing the best we can.

[49:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2943s) We rent then reached out to AWS's sustainability team

[49:06](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2946s) who was extremely helpful to help us validate

[49:09](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2949s) some of our assumptions to make sense

[49:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2951s) and provide a lot of recommendations

[49:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2954s) and some data for us to help make better decisions.

[49:18](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2958s) The one thing we did,

[49:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2961s) we went through a very early version

[49:23](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2963s) of the sustainability pillar, the well-architected review.

[49:26](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2966s) We had been through many

[49:27](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2967s) traditional well-architected reviews in the past

[49:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2969s) and knew that we were pretty tightly optimized

[49:33](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2973s) just from a performance and cost perspective.

[49:35](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2975s) My intuition told me that we were also having

[49:37](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2977s) a pretty good a lower impact on the environment

[49:42](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2982s) as a result of those optimizations we already done.

[49:46](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2986s) We also got an early version

[49:49](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2989s) of some of the carbon footprint tool data sent to us

[49:52](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2992s) and learnt that from 2019 to 2020,

[49:56](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=2996s) our actual carbon footprint was reduced by about 32%.

[50:01](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3001s) Now, throughout this entire time,

[50:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3003s) our business was growing like crazy.

[50:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3005s) We had several record breaking mobile order days in 2020.

[50:10](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3010s) And we went from 50 stores with our commerce engine

[50:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3014s) to every store in north America, by the end of that year.

[50:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3021s) So I shared this with our leadership, our CTO,

[50:24](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3024s) and our chief sustainability officer

[50:26](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3026s) that, Hey, look there and we reduced our footprint.

[50:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3029s) And by the way, we saved money and our business

[50:31](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3031s) has grown like crazy.

[50:33](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3033s) And his response was, this is a big challenge.

[50:37](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3037s) And technology actually offers

[50:38](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3038s) some really interesting opportunities here

[50:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3040s) where we can divorce the carbon reduction

[50:44](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3044s) from business growth.

[50:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3047s) Business grows, carbon goes down in these particular cases,

[50:50](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3050s) the more we optimized.

[50:52](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3052s) That's a legitimate win-win situation right there.

[50:56](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3056s) So looking back a little bit,

[50:58](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3058s) now, some of this, again, with hindsight,

[51:00](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3060s) when we sort of just did the analysis

[51:01](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3061s) and how do we pull some of that off?

[51:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3065s) So first of all, it was extremely important

[51:06](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3066s) to have great observability,

[51:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3067s) great service level objectives.

[51:10](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3070s) We couldn't really know if we were improving or not

[51:13](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3073s) if we didn't know where our targets were,

[51:17](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3077s) where we were headed.

[51:19](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3079s) So we depend heavily on Datadog in our case,

[51:22](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3082s) but whatever tool that does the job we'll do it,

[51:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3085s) but it's important to have good observability

[51:28](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3088s) and have an understanding of what your customers expect

[51:31](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3091s) from their experience and what your SLAs are.

[51:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3094s) We also knew that we were quite efficient by design.

[51:37](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3097s) Cloud Native was cleaner,

[51:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3100s) reportedly up to 88% cleaner than a traditional data center.

[51:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3105s) We rely heavily on Kubernetes,

[51:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3107s) which allows us to densely pack our services

[51:50](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3110s) onto the infrastructure beneath it,

[51:51](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3111s) really getting us very high utilization.

[51:55](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3115s) We use binary protocols,

[51:57](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3117s) GRPC is super efficient for communicating

[52:01](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3121s) between our services.

[52:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3123s) Many of our services are written in very efficient Scala.

[52:09](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3129s) And we also with cost in mind are constantly optimizing.

[52:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3134s) So I like to just say right-size everything all the time,

[52:17](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3137s) make sure that if we are not utilizing resource,

[52:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3140s) but we're paying for it, let's get rid of it.

[52:22](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3142s) We don't need that.

[52:23](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3143s) Rightsize instance types

[52:26](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3146s) that we learned a lot about making sure

[52:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3149s) that we can match an EC2 instance type two

[52:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3152s) with a workload

[52:33](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3153s) and there's so many EC2s

[52:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3154s) there's one, that's perfect for the job.

[52:38](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3158s) And it made things along those lines.

[52:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3160s) You can see some examples here

[52:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3161s) of where we do some auto-scaling tuning.

[52:44](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3164s) We found that some of our services were asking

[52:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3167s) for too much compute than what they actually needed.

[52:50](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3170s) So based on the data, we were able

[52:51](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3171s) to turn that down a little bit

[52:52](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3172s) and have the auto scaling curve much more closely

[52:55](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3175s) and more smoothly matched the actual demand curve.

[53:00](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3180s) Some less obvious learnings.

[53:01](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3181s) It's a little bit nuanced areas.

[53:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3183s) And we're already hinted at actually

[53:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3185s) by my predecessors here.

[53:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3187s) Some regions are greener than others

[53:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3191s) lower carbon regions.

[53:12](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3192s) So if we can get access and understand where those are,

[53:15](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3195s) all other things being equal,

[53:16](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3196s) we might as well run these workloads

[53:18](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3198s) in those lower carbon regions.

[53:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3201s) We've heard a lot about Gravitas, this week.

[53:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3205s) We switched some of our incidents types to arm.

[53:28](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3208s) And I think the cost was about the same

[53:30](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3210s) performance was the same.

[53:31](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3211s) We did it for no other reason

[53:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3212s) than it was more energy efficient.

[53:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3214s) Spot is an interesting one as well.

[53:38](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3218s) From a customer perspective,

[53:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3220s) we're still using as much compute as we were,

[53:43](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3223s) whether we use spot or not.

[53:44](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3224s) It's an obvious target for optimizing by costs,

[53:48](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3228s) but we believe it's the right thing to do

[53:49](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3229s) in addition to the cost savings,

[53:51](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3231s) it allows the Cloud provider

[53:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3233s) as we saw earlier, to get much higher utilization

[53:56](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3236s) of their infrastructure,

[53:57](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3237s) it's already running, let's just use it.

[53:59](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3239s) And another one we learned,

[54:01](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3241s) which was also something you don't normally think about

[54:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3243s) is, we have backup jobs running on a regular basis.

[54:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3247s) And by default, it might run

[54:10](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3250s) at the top of each hour, very predictably.

[54:12](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3252s) But again, if every single customer of Amazon web services

[54:16](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3256s) did that, and they do,

[54:18](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3258s) I think have a crazy amount of peak.

[54:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3261s) So we went and added kind of randomization

[54:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3265s) to the time that some of these jobs run.

[54:30](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3270s) Now, we talk mostly about Cloud

[54:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3272s) but we're not unique here.

[54:33](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3273s) We are a part of a much larger ecosystem.

[54:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3274s) Data centers, Data transfer, Vendors,

[54:38](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3278s) Cloud, End-user devices,

[54:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3280s) each one of these areas,

[54:42](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3282s) no matter what part of the business you're in,

[54:44](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3284s) if you're making decisions

[54:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3285s) about how to configure data center,

[54:49](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3289s) how are you gonna build an application,

[54:51](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3291s) how are you going to write a contract with the vendor,

[54:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3293s) there is something you can do

[54:55](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3295s) to help improve the sustainability of your workloads.

[55:00](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3300s) So, as we already said, moving the data to the Cloud

[55:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3303s) is much more efficient.

[55:06](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3306s) You can favor vendors

[55:08](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3308s) that have strong sustainability statements

[55:10](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3310s) put out there in public.

[55:12](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3312s) Data transfer is interesting

[55:13](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3313s) because we have to move data back and forth,

[55:15](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3315s) but let's make fewer calls.

[55:17](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3317s) Let's make smaller calls.

[55:18](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3318s) Let's shorten those calls

[55:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3320s) and reduce our impact overall.

[55:23](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3323s) I find end-user devices

[55:24](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3324s) would be one of the most interesting areas here,

[55:26](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3326s) because whatever it is, you're building a website,

[55:27](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3327s) you're building a mobile app.

[55:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3329s) It lands on your end user screen.

[55:31](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3331s) And there's so many different ways to interpret

[55:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3334s) and understand how interview's consumed on that screen.

[55:37](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3337s) So for example, I like dark mode.

[55:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3340s) Screens consume energy

[55:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3341s) and sometimes the brighter they are,

[55:43](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3343s) the more drain on the battery it is.

[55:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3345s) Some colors require, on some screens require more energy.

[55:50](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3350s) So dark mode is one way to potentially reduce

[55:52](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3352s) the energy need for displaying

[55:54](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3354s) a simple application or whatever it is.

[55:56](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3356s) Blocking bots, bots, hitting your website

[55:58](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3358s) are just complete wasted bots

[56:00](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3360s) you don't want to have, to say,

[56:02](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3362s) and even good bots.

[56:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3363s) You can tell them don't come back for another week

[56:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3365s) and don't every day.

[56:08](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3368s) Lazy loading, reducing CPU, reducing page weight,

[56:10](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3370s) these are all opportunities we have for improving.

[56:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3374s) Looking at a website, for example,

[56:16](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3376s) there's all sorts of tools out there

[56:18](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3378s) for helping to understand, how green a website is.

[56:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3381s) And you look at some of these safari tools at the bottom,

[56:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3385s) you can see the CPU profiles spike.

[56:27](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3387s) It might be interesting to look at that

[56:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3389s) what's causing that spike?

[56:31](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3391s) When sometimes when you hear your laptop fan

[56:33](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3393s) worrying and worrying and worrying,

[56:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3394s) it might be your laptop saying help,

[56:36](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3396s) I can't do this anymore.

[56:39](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3399s) Let's let's help them out, right?

[56:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3401s) Let's not send up useless JavaScript.

[56:43](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3403s) Let's reduce the size of images.

[56:44](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3404s) Let's not auto play a video

[56:46](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3406s) that is off the screen below the fold anyway.

[56:50](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3410s) So there's a lot of things to think about.

[56:52](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3412s) Some of these might seem like small negligible tweaks,

[56:55](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3415s) but at a large scale with lots of volume,

[56:58](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3418s) it can have a major impact overall.

[57:00](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3420s) Plus you probably get a snap, your user experience.

[57:04](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3424s) So real quick, I think we're low on time here.

[57:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3427s) Overall, I believe that we should factor in carbon

[57:10](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3430s) as just a cost and part of our total cost of ownership

[57:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3434s) as I like to call it,

[57:15](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3435s) and please, I beg for forgiveness already.

[57:18](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3438s) TCO2.

[57:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3441s) If we were to consider carbon

[57:24](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3444s) as the thing we're optimizing for,

[57:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3445s) and that's what it costs,

[57:26](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3446s) we're making trade-offs.

[57:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3449s) If carbon was the thing, what would we do?

[57:31](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3451s) Would we have make different choices?

[57:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3452s) in the Cloud, it's easy

[57:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3454s) 'cause we tend to also align very closely with costs,

[57:37](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3457s) but that's not always the case

[57:38](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3458s) in different parts of the stack.

[57:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3461s) So what do we do?

[57:42](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3462s) I think it's very important to get the word out

[57:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3465s) just in your company, start having conversations,

[57:48](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3468s) get people excited about this.

[57:49](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3469s) I find people are already excited about this

[57:51](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3471s) when I bring it up.

[57:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3473s) We recently started a greener technology Gilda at Starbucks,

[57:56](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3476s) across the organization to help bring ideas together

[57:59](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3479s) and see how we can start measuring

[58:01](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3481s) and really have an impact overall.

[58:04](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3484s) Make sure you include green goals in your projects

[58:06](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3486s) as a non-functional requirement.

[58:08](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3488s) Target low-hanging fruits,

[58:10](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3490s) accelerate migration to the Cloud.

[58:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3491s) There's lots of things we can do.

[58:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3494s) And when you have your technology in order,

[58:17](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3497s) you can use technology outside of technology

[58:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3500s) to have a better impact.

[58:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3501s) And here's just an example

[58:21](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3501s) of one of the reasonable cup programs.

[58:24](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3504s) Kiosks, you can drop a cup in,

[58:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3505s) it gets washed automatically,

[58:27](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3507s) and you can get a couple stars as a reward for that.

[58:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3512s) And lastly, a couple great people I met along the way.

[58:35](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3515s) ClimateAction.tech is a great slack community.

[58:38](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3518s) And through that group,

[58:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3520s) I learned about Tom Greenwood,

[58:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3521s) "Sustainable Web Design" book.

[58:43](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3523s) It's a great book and I greatly enjoyed it.

[58:48](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3528s) So I'm going to hand it back to Adrian to wrap us up.

[58:55](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3535s) Thanks very much.

[58:56](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3536s) Thanks Drew, and really appreciate

[58:59](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3539s) all the effort you put in to come here

[59:01](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3541s) and present for us and the wonderful work

[59:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3543s) that you've been doing.

[59:06](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3546s) So just sort of divide this as a summary.

[59:09](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3549s) If you're on the development site,

[59:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3551s) you can optimize code, choose faster languages,

[59:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3554s) fishing algorithms, do a bunch of things

[59:16](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3556s) to just speed up your code,

[59:18](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3558s) peat up the way you've building it.

[59:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3560s) Then the operations side, you can configure systems

[59:22](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3562s) to have the right instance types,

[59:24](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3564s) get high utilization, automation,

[59:28](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3568s) things like auto-scaling.

[59:31](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3571s) Worry about these over specified requirements,

[59:33](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3573s) archive and delete data sooner

[59:34](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3574s) you duplicate, be very careful about times and locations.

[59:38](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3578s) So all of these different things,

[59:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3580s) but make sure you're doing this at scale.

[59:42](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3582s) And you don't want to spend a lot of time

[59:44](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3584s) optimizing something that is actually so small

[59:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3587s) that you're spending more carbon thinking about it,

[59:49](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3589s) then you're actually saving.

[59:50](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3590s) So this really makes a huge difference at scale,

[59:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3593s) but don't worry about the small things.

[59:58](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3598s) Just want to mention this was announced yesterday,

[01:00:01](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3601s) AWS Customer Carbon Footprint Tool

[01:00:04](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3604s) it's gonna come soon.

[01:00:06](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3606s) It includes the full cost

[01:00:07](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3607s) that we'll show you how your sustainability investments

[01:00:10](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3610s) go down over time.

[01:00:11](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3611s) And we've talked a little bit about

[01:00:13](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3613s) sort of choosing regions.

[01:00:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3614s) So just very, very broad sort of things

[01:00:16](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3616s) that you'll see here.

[01:00:18](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3618s) Europe is pretty low carbon already.

[01:00:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3620s) Like there's really not a lot you can do there

[01:00:22](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3622s) to reduce the carbon because it's worth saving the energy,

[01:00:26](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3626s) but it's largely a low carbon environment.

[01:00:30](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3630s) The US, we're buying lots of energy.

[01:00:32](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3632s) Carbon is going down really quickly.

[01:00:35](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3635s) So yeah, it's on a good path.

[01:00:39](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3639s) Asia is more problematic.

[01:00:40](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3640s) There's a lot of very high carbon sources

[01:00:43](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3643s) and it's very hard to buy renewable power there.

[01:00:47](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3647s) And this is all very well known in the industry,

[01:00:51](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3651s) but just to think about,

[01:00:52](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3652s) if you're going to optimize a workload first

[01:00:54](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3654s) deploy that optimization in Asia,

[01:00:56](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3656s) if you have a nation workload

[01:00:58](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3658s) that will make more difference

[01:00:59](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3659s) than deploying it in Europe.

[01:01:01](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3661s) Just think about it in those terms.

[01:01:02](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3662s) And when you get access to the tool,

[01:01:03](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3663s) you'll be able to see the actual behavior

[01:01:05](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3665s) and where your competence is going.

[01:01:08](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3668s) So that's pretty much it, just a call to action.

[01:01:12](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3672s) One of the things you can do when you go back

[01:01:14](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3674s) to your companies is just us asking questions

[01:01:16](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3676s) when you're doing planning discussions.

[01:01:18](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3678s) When you set goals for 2022,

[01:01:20](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3680s) what are you doing about sustainability?

[01:01:23](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3683s) Find areas where there's the biggest opportunity,

[01:01:25](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3685s) to make a difference,

[01:01:26](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3686s) really focus on where this is going to be a big thing.

[01:01:29](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3689s) And then collect, share

[01:01:31](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3691s) your sustainability optimization learnings,

[01:01:33](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3693s) come back reinvent next year

[01:01:35](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3695s) and tell us the same stories

[01:01:37](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3697s) that we've heard from Starbucks from Drew.

[01:01:39](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3699s) What have you done and how have you done it

[01:01:41](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3701s) and what techniques have you learnt?

[01:01:44](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3704s) So thank you very much.

[01:01:45](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3705s) There are some other sessions you can go look up

[01:01:48](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3708s) from re:Invent and we had a hackathon

[01:01:51](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3711s) and a few other special screenings of videos

[01:01:53](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3713s) that you can go find as well.

[01:01:56](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3716s) So thank you very much.

[01:01:57](https://www.youtube.com/watch?v=3-Zq2W1-odU&t=3717s) (audience applauding)

