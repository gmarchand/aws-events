# AWS re:Invent 2021 - Sustainability in AWS global infrastructure

[Video Link](https://www.youtube.com/watch?v=Dmz45WhXENs)

## Description

The global cloud infrastructure helps customers build reliable, available, secure, scalable, and fault-tolerant applications. AWS is also committed to innovating in sustainability as the organization works toward Amazon’s goal of achieving net-zero carbon by 2040. In this session, learn how AWS continues to increase efficiency across their operations and review progress toward the goal of powering operations with 100% renewable energy. Also, hear an update on water stewardship programs at AWS and explore how AWS InCommunities is making a positive impact in the regions where AWS global infrastructure is built and operated.

Learn more about re:Invent 2021 at https://bit.ly/3IvOLtK

Subscribe: 
More AWS videos http://bit.ly/2O3zS75 
More AWS events videos http://bit.ly/316g9t4

ABOUT AWS
Amazon Web Services (AWS) hosts events, both online and in-person, bringing the cloud computing community together to connect, collaborate, and learn from AWS experts.

AWS is the world’s most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services from data centers globally. Millions of customers—including the fastest-growing startups, largest enterprises, and leading government agencies—are using AWS to lower costs, become more agile, and innovate faster.

#AWS #AmazonWebServices #CloudComputing

## Transcript

Good afternoon. My name is Nat Sahlstrom. I work for Amazon Web Services, within the AWS Infrastructure Group. And I'm really, really happy to be here. I gotta share something with you all, though. I'm a little bit nervous. Probably because like a lot of you, this is my first time doing a presentation in about two years. And, these type of presentations are a little different than Zoom ones, aren't they? But my nervousness is a assuaged by the fact that I'm so energized to be with colleagues and customers, and partners. And I hope you guys are feeling the same thing. This week I've probably been hugged more warmly, had my hand shaken more vigorously, and smiled at by my colleagues in ways that I probably have never had in my over 10 years at Amazon. So I hope you guys are experiencing the same thing, and hopefully you guys can carry that energy through to the rest of the week. And through our conversation today. But, I think that's gonna be easy to do. Because I'm really excited about the message that we're gonna share today. And that's around sustainability with an AWS Cloud. We've made a lot of progress in this space, and I'm excited to share some of the highlights of that journey today with you. What we're gonna be talking about, because this is such a broad topic, is to start with, what is the AWS global infrastructure footprint look like? I'm gonna talk to you guys about The Climate Pledge, and how AWS intersects with that. I'm gonna talk about our progress in renewable energy. I'm gonna share some of the stories around how we're implementing energy efficiency in carbon reduction, within our footprint. I'm gonna talk about water stewardship. And finally, I'm gonna talk about community engagement. Which is, how do we impact the communities where the cloud lives? Where we operate? Where our customer's workloads live virtually, and we have a physical presence? As I mentioned, I've been at Amazon over 10 years, and it's just been an incredible journey. And when I first started, we had four regions. Today, AWS has the largest global cloud infrastructure footprint in the world. With over 25 regions, 81 availability zones, and over 300 cloud front locations. And what's interesting about this footprint, is that it's massive. And just last year, there's a really, really cool tie-in around leadership principles, and our footprint. And that is our new leadership principle of with great size and scale, comes responsibility. And a really good example of that, is The Amazon Climate Pledge. We announced the Amazon Climate Pledge in 2019. In partnership with Global Optimism. And The Climate Pledge committed Amazon, and other signatories to commit to being net zero by 2040. Which is 10 years faster than the Paris Agreement. Why this is important, is because there are scientific consensus that if we want to really dramatically impact and reduce the worse parts of global warming, we need to limit global warming to 1.5 degrees Celsius. And The Climate Pledge allows companies to think collaboratively about how they can implement technologies and business solutions to go drive out carbon from their businesses. Signatories commit to being to net zero by 2040. And when Amazon signed The Climate Pledge and founded this, we committed to be 100% renewable energy by 2030. But we since stepped on the gas, and I'm gonna talk about that, and pull that target in five years, to 2025. Another instrument that we put to work in The Climate Pledge is funding The Climate Pledge Fund. Which is a $2 billion fund dedicated to funding companies and technologies who's products and solutions are gonna be integral to transitioning to a low carbon economy. We've made a lot of progress to Climate Pledge, and we're really excited about this. At this time last year, The Climate Pledge had roughly 31 signatories. We're now over 200 companies a year from that period, and continue to grow. If you are interested in participating in The Climate Pledge there's the three fundamental principles that participants agree to when they sign The Climate Pledge. One, is regular reporting. We all acknowledge that transparency measuring, mapping, are critical to reducing our carbon footprint. The second is carbon elimination. So, signatories will commit to de-carbonization strategies across their business. And this involves the host of programs, such as energy efficiency, implementing renewable energy programs, and de-carbonize their business by looking at the materials in which they operate in the physical realm. And finally, since we do operate in the physical realm, we know that it's very, very challenging to reduce all carbon from our business. And signatories then agree that they'll find real, credible offsets to negate the rest of their missions. As I mentioned, renewable energy is a big part of The Climate Pledge, and we've made a lot of progress in this space. We're well on-track to getting there by 2025. And it's worth talking about this a little bit. I mentioned that I've been at Amazon 10 years. I'm in front of you guys today with a bit of my dream job. When I first started at Amazon, I was tasked with the kind of ambiguous charter of, we're spending a lot of money on energy, can you go figure this out? That was my job at that point in time. Really exciting, and a great opportunity. If you go look at the progress we've made in this space, something we're really, really proud of what we delivered on behalf of our customers. And what's interesting, is the path of acceleration. Pre-2020, we had under 6500 megawatts of load. In 2020, we signed up a lot more. In 2021, already, we did 3.6 gigawatts of new utility-scale wind and solar projects. And just yesterday, we announced 18 new projects, bringing another two gigawatts of capacity around, across Europe, and the Americas. We now have over 12 gigawatts of load. This is a tremendous amount of renewable energy capacity. And often times, we use these figures and these units, like gigawatts, I hear a lot of "Back to the Future" jokes. We use megawatt hours, and it's tough to quantify that. So just for a little bit of perspective, often times when we think about really large utility companies, they hold eight, nine gigawatts. Amazon's renewable energy holdings right now, rival, or are larger than most of, many of the U.S. large investor-run utilities. Well, what does this mean for the world? Well, what does it mean that Amazon has over 274 renewable projects across the world? What we're focused on, is avoiding carbon emissions. So we can reduce the carbon environmental impact of our cloud services. And we believe this is happening in a big way through our renewable energy projects. When all the projects that we signed to date come online, it will reduce 13.7 million metric tons of carbon emissions that will be avoided. I don't know if you guys are really sharp on your Emerald Isles geography, but that outline is the country of Ireland. Imagine the country of Ireland completely composed of woods. That's how much carbon emissions would be avoided by our projects. And doing this is not as simple as, simply taking out your credit card, and saying, "Hey, every renewable energy developer in the world, "I want power, just go get me these projects." It's actually a complex undertaking. And what's really challenging about this, is that many parts of the world, you simply can't go and do a standard procurement model to go buy renewable projects. And, one of the things that we've been doing over the last couple of years, is innovating in the commercial space, the regulatory space, and the policy space, to go deliver renewable projects, where previously, corporate companies weren't able to do that. Examples of that include Japan and Singapore. The projects we announced, and the projects we just announced in South Africa, is the first corporate project where utility-scale renewable energy is brought on behalf of a corporate customer. And this seems a little bit esoteric, you might say, "What's the big deal?" But it's actually very challenging, and impossible until the efforts that we put in place actually go do this type of work. And why this is important, is it's not just about how we can de-carbonize, how we can bring more renewable energy under the grid, but how we can create commercial structures that other companies, and other people can replicate, as they implement decarbonization strategies. Similar example you might think about, well, this is a massive 20 gigawatt solar project. It's out in the middle of the dessert in South Africa. Well, we did a 20 gigawatt project in Japan. If you've had the privilege of going to Tokyo before, it's a fascinating city. A really fun place to visit. But can you imagine a place where you would put this many solar panels in Tokyo? We had to think of innovative approaches. So we worked with developers, and find ways where we can bring impactful, large projects to scale and online. And in Tokyo, we've put panels across 440 locations, across the city, to bring big impact renewable projects to bear. And we also know that it's not just about doing lots of projects. It's about innovating, and looking towards the challenges in the future. And one of these is the intermittency problem. You may have heard that term before. But simply stated is, what do you do when the sun's not shining, or the wind's not blowing? You need storage. And we recognize that, as well. And accordingly, we've done our first two large solar and storage projects this year. And these projects are our first bridging solutions towards our eventual goal of 24/7 renewable power. Powering our operations 100% across all of Amazon. In addition to these storage and solar integration projects, we also know that we need to go big. And a great way to go big, is with off-shore wind. We've already announced two large off-shore wind projects to date. And the really cool thing about these off-shore wind projects is simply a matter of physics. When you go look at the size of the turbines and the sails that are incorporated in these off-shore projects, and you combine that with the consistent high wind speed that you get out at sea, you get much higher yields. Today, off-shore wind currently only produces a small amount of the wind energy that goes into power's grids. But we know that if we go look at what that untapped potential is, wind technology companies and energy economists predict that off-shore wind could generate over 18 times the power load that the world consumes today. So it is truly a massive and untapped resource that we're looking at very closely. We also know that it's not just about putting lots of projects and storage and size, it's about being smart about how we use these assets, how we integrate them. And to that impact, we're a lot like you. We use the AWS Cloud, and tools and services, to find ways to optimize the performance of our renewable energy assets. And a great way we do that, is with the team that we have called, the Renewable Energy Optimization Team. So I'm excited to share a short little video with you guys about how we use AWS Services to efficiently optimize our renewable energy projects. With our renewable goal, we're developing solar projects, wind projects, including this wind farm here in California. And were developing software built on AWS to optimize our renewable portfolio at scale. So here we're looking at live metrics from Turbine Five. And we have a total of 200 metrics from each turbine at this facility. My name is Athanasios Caramanolis, and I lead the Renewable Energy Optimization Team at AWS. With AWS IoT and machine learning services, we stream and analyze millions of data points in real time from projects across the world. At AWS, we're looking at how to decarbonize our entire business. This year Amazon announced it's first two solar-plus storage projects. This software will let us optimization how we deliver clean electricity onto the gird. Decarbonizing our energy system is an enormous challenge. We're using the AWS Cloud to build automated mechanisms at scale. Ensuring our renewable fleet delivers as much clean electricity as possible. Thank you. By 2025, we expect that the production we have, they'll be increased by using AWS Services to optimize performance of our renewable assets. We'll bring on the size of 200 megawatt wind farm. That's a big deal. That's $100 million investment that we're not having to make because we're increasing the renewable energy performance, the assets we have using the AWS Cloud. And we're gonna continue to optimize renewable energy performance using AWS Cloud. And with the progress that we've made to date, I'm very excited that I can tell you that Amazon is still the world's largest corporate buyer of renewable energy. I wanna shift gears here for a second. And this may sound a little bit strange. But, fancy videos and big, sweeping vistas of wind turbines, off-shore wind projects, I would argue can sometimes be a distraction. That may seem like a paradox, that may seem strange. And you're like, "Well, why are you telling us "so much about that?" Well, it is very important. That is the supply side of the stack. But what gets lost often times is efficiency. We know that the greenest electron is the one that you do not use. And often times, that's the less sexy work. It's the less optical work. But is really, really critical if we're gonna be serious about combating climate change, and reducing carbon. And I'm very pleased to tell you that increasing efficiency and reducing carbon emissions is integral to how AWS operates its infrastructure, and it's data centers, and it's cloud platform. So I'm gonna spend a little bit of time today diving into the dirt, diving into some of the details on the margin about how we actually do this to reduce the carbon of our business. The first side is simply about how do we operate, engineer, and build our data centers? This may seem like well, of course, don't you guys just do a good job? Well yes, we have the highest levels of reliability and security, but we're also very, very keyed in on how we use energy within our data centers. And this comes down to places that you might not even think about. And that includes cooling technology. Cooling is one of the biggest energy consumers in the data center next to IT load. So constantly thinking about how do we increase the efficiency of our cooling. And this is where engineering dive deep really matters. Because we go all the way to the margins on things to find out how we can squeeze out energy efficiency gains in our business. Now a great example of this is the evaporative cooling media that we use to cool our data centers. Now this may seem like a really weird esoteric detail, but it's actually really important. The evaporative media that we use to cool our data centers has a big impact to the efficiency of our operations. So our engineering teams go work with vendors who actually go work on these media that we use in our data centers. And find ways to experiment and engineer about making that more efficient. And one of the things that we've recently done, is change out that evaporative media by working with partners. And the result, we're increasing the efficiency of our cooling equipment by 20%. That has big energy gain impacts. And it's not just about the energy infrastructure, the energy consuming assets within the data center floor, it's also about utilization and how compute works efficiency within the data center. And if you had any of the chances to be familiarized with Graviton, last year we shared information about Graviton, about how it's our most power-efficiency processor, and how that produces better performance per watt than previous EC2 generation processors. And that can be very exciting because there's cost-savings, there's efficiency gains there. But one of the things gets lost is energy efficiency, sustainability, and carbon-reduction gains. Graviton is our most power-efficient general purpose processor. And the exciting thing about that is it's more efficient for 60% of workloads. We estimate a reduction of 300,000 metric tons of carbon in 2022, purely from running Graviton-based instances, rather than EC2 instances. This is a big deal. This is roughly equivalent to 54,000 U.S. homes in carbon reduction. And these carbon emissions are going to continue to reduce, as more customers move to Graviton. So when you add these pieces of the puzzle up, we have supply side, which is bringing more renewable energy into our infrastructure, into our data centers. You have the demand side, which is how we use power in our data centers. How we utilize compute load efficiently on processors, on server racks. And we have long suspected that we do this really well. So what we did is look at, well, how does the rest of the cloud industry compare on this? So a study by 451 Research was done recently, and it found that AWS at 3.6 times more energy efficient, than the median of surveyed U.S. enterprise data centers. We're like, wow, 3.6 times more energy efficient? That's really compelling. That's exciting. We translated that into carbon reduction. And we looked at that. And recently, we did the same study and looked at Europe. So we looked at enterprise data centers in places like France, Spain, and Germany. And we found a similar pattern. Except this time, it was even higher. Five times more energy efficient. And what that means to a customer, is that when you move load from an enterprise data center, to AWS Cloud, you're seeing up to an 80% reduction in energy load. And when you combine that will all the exciting, big renewable energy stories, you see a really big potential for carbon reduction. Up to 95% when all these renewable projects are online, combined with the efficiency of our data centers and compute load. And we're not done in the space. And when I say we're not, is because we're really focused on some of the next big challenges. From conversations with customers and other people in the industry, we know that one of the big hurdles is on Scope 3. Scope 3 is the embodied carbon that goes into our businesses. And one of the ones that's a real big challenge for us, that we're excited to be working on, is reducing the carbon that goes into the physical infrastructure of how we build our cloud. When we started looking at this problem, we started looking at where are the biggest concentrations of carbon that we can start driving out immediately? And it turns out that concrete, simple plain old concrete is one of those areas where we have a lot of carbon, and have actionable tools in our tool chest to go reduce this right now. So one of the things that we started doing is looking at low cure carbon when we go build our data centers. And when we found it, we implement this into our basis of design for data centers that we build, we can have a 20% reduction in the carbon of that. The next piece that we looked at was steel. And steel is a great example of how we use our size and scale to go drive out carbon. Because Amazon is a large buyer of steel. Not just for AWS, but if you look at our fulfillment center network, the racking and shelving, all of the steel that goes into the Amazon business, we have an opportunity to work with the vendors to implement technologies and manufacturing processes that drive out carbon and Scope 3 that goes into all of our business. And I'm learning stuff all the time about this, so I'm gonna give you guys a little bit of a manufacturing lesson that I learned recently. Thanks to some of the people on the team. Steel is traditionally made through a process called 'Basic oxygen furnaces'. And I recently learned about this. And what this means is, we're burning and melting down steel, iron ore, to make steel. And that burning combustion process comes from burning coal, or natural gas. An alternative technology that vendors can use is EAF, Electric Ark Furnaces. And what's compelling about this, is two-fold. One is, since you're running a current to melt down the steel, that current is generated by electricity rather than the combustion of natural gas, or thermal based resources like coal. So what you can do is have that EAF be coming from renewable energy resources. The second piece is EAF, since it's melting down recycled steel, you can take scrap steel and other parts of this. And what that means is that you have much less carbon intensity through the production of ore by using recycled steel components. And you have the same levels of rigor that you need to actually have steel that will meet your building standards. And that can have a really big impact on your carbon reduction. EAF steel can be up to five times less carbon intensive than BOF produced steel. And we've used this type of steel process in six of our data centers, and we're gonna be using it in more of our data centers as we build forward. Now it seems like a really prosaic deep in the weeds topic, but it matters, because Scope 3 is so challenging. It's built into so many parts of our businesses that you have to be thinking on the margin about how you can go drive out these parts of our business. And we're very, are serious about that. And just yesterday we announced the AWS Customer Carbon Footprint Tool. This is a service that shows our dedication to reducing carbon across our business. Customers of AWS now will be able to see the carbon intensity of their workloads that their running on AWS. They'll also have a forward-looking view that's going to show them the carbon reduction impact of our renewable energy investments. We're really excited about this work. And to exemplify what we're doing in this case, I'd like to share a short video with you guys with one of the customers that works on this type of technology with us, and that's Patrick Flynn, who's the V.P. From Global Head of Sustainability with Salesforce. So let's hear from him about how they're working with AWS to achieve their sustainability goals. Hello, my name is Patrick Flynn, Vice-President and Global Head of Sustainability at Salesforce. At Salesforce, we believe that business is the greatest platform for change. And we work to serve the interests of all stakeholders, employees, customers, partners, communities, and the planet. In 2021, we announced that Salesforce has reached net zero carbon across our full value chain, and 100% renewable energy for our global operations. Salesforce and AWS have been collaborating for a long time. And we have shared climate values. Together, we're also working to expand renewable energy procurement in partnership with the Clean Energy Buyer's Alliance. Salesforce also joins The Climate Pledge, co-founded by Amazon and Global Optimism. And both Amazon and Salesforce are founding members of the LEAF Coalition, which aims to protect tropical forests around the world. We're excited that AWS is providing us with the carbon footprint associated with our use of AWS Services. As this data is essential to our net zero commitment. We start by optimizing our use of AWS's services, so that we can reduce the carbon intensity of our applications. AWS provides technical guidance to help Salesforce architect sustainably on AWS. The data that AWS provides lets us understand our climate impact, and develop plans to avoid, reduce, or compensate for those emissions. Salesforce and AWS are on a mission to help our suppliers, help our customers, and help our communities take climate action for the future that we all share. Thank you to Patrick; and thank you, Salesforce. I'm really excited about that shared vision. On top of energy and carbon, another pressing concern that we all have as global citizens is water stewardship. In addition to our efforts on efficiency and renewable energy, we have multiple initiatives in place around water stewardship and conservation that I wanna share with you guys today. Our water program is really built around four principals. One is, what is the source of water that goes into our data centers to cool? The second is, how do we use that water most efficiently? The third is, what do we do with the water when we're done using it to cool our data centers? And the fourth is, how do we restore water levels in the communities where we operate? I wanna walk through a little bit of those four steps with you quickly. The first one is around sustainable sourcing of water. So whether it's in Spain, Chile, Northern Virginia, Eastern Oregon, we're always looking about how we can use the most sustainable sources of water. And one of the ways that we can do that, is through using recycled water. Now that may seem like a strange thing, but why that's important is because we all have to drink water. Drinking water is sometimes called potable water. So one of our first principles is, how can we use water that's non-potable to cool our data centers? Because arguably, the most critical use of water is for the preservation of life on earth, which is drinking water, right? So when we go into many parts of the world, we say what the non-potable water sources that we can employ to cool our infrastructure? And this is a lot like the South African example I gave to you guys earlier about renewable projects, which is often times, when you go to utilities, they say, "Well, I guess we have a small pilot program somewhere, "but we haven't really done anything at the scale "that you wanna do." And we have a team of water professionals and public policy folks who had a lot of success going out and working with utilities and local governments to go drive the acceleration of recycled water integration into our data centers. A great example of this is in Northern Virginia, where we were the first large industrial user to bring in recycled water to cool our data centers. And we're not done with Northern Virginia, or parts of the Bay Area, or Singapore, or other parts of the world we've implemented this. We're using the same principles that we brought to bear with our renewable energy commercial innovation towards recycled water. Which is, finding paths to do this at scale. Not just for AWS, for other industrial users of water who wanna replicate that playbook. We also make sure that the water that we do use within our data centers is efficiently used as possible. So we do this through evaporative cooling technology, which basically means that we don't use water to cool our data centers when we can bring in free cold air from the outside ambient environment. Instead, we carefully use metrics and operational best practices to calibrate bulb set points. And understand what the weather forecast is gonna be, how we can operate our infrastructure reliably, and then, when we get to set points when we need to cool, we use water diligently and efficiently. And the other piece that we use, is we innovate and build technologies for onsite water treatment. Now that may seem a little bit strange too, but, any of you guys who may have had one of those old-school air conditioners, with the tank that you had to go empty, that was sitting in your living room, or basement? Similar to that. You can recall those air-conditioners that would get the kind of funk in the water? That little bit of scaling? That happens when you're cycling water through an evaporative cooling technology. So what we've developed is modular onsite treatment. So we can reduce that type of scaling that happens through hard water usage, to make sure that we can continue to use that water. But eventually, we do have to get rid of that water from our data centers. So what are the ways we do this? One of the things that we like to do is go look at what is the water that comes out of our data centers? In many cases, because of the onsite water treatment that we use, and how we efficiently use that water, that water is often times cleaner than when it came into our data centers. And this has created some really unique opportunities that we didn't really think about until we got closely integrated with our communities. A great example of this is, Eastern Oregon, and our Western Region, where we have what we call PDX. What we do there is, take the water that we've used in our data centers and a strange function of irrigation and the use of chemicals to go treat crops in parts of this world, is that the water table sometimes has high nitrate levels in it. But the water when we go treat it in our data centers, is actually cleaner than often times what the water table is. So what we've done is go work with utility, and go discharge that water directly into irrigation channels, where it can be used right for agricultural purposes. The water company doesn't have to treat it, farmers and the local community can use this right off the bat. And it's a win-win for us, too. Because we do not have to go build the discharge infrastructure that we might have to put this water back to a waste water treatment plant. And finally, we look about how we can restore water within the communities where we operate. This is an example of a watershed restoration project in South Africa, where we partnered up with local groups. In this case, the Nature Conservancy in Cape Town to go reduce evasive species that are water hogs, while on the water table. We're also doing water restoration projects in parts of the world like India, and Indonesia. Through partnerships with water.org What we do here is connect water.org with micro projects where we've done over, connected AWS projects to over 160,000 people to clean up public water systems. In India, with wateraid.org we've done over 5,000 projects for water filtration, rain water capture, and ground water recharge projects. Projects we've done to date to restore water will bring over 250 million gallons of water per year to the communities where we operate. Speaking of the communities where we operate, it's not just about energy efficiency and water, it's also about what is our social impact. What is our equity impact in the communities where we operate? To make a positive impact in the communities where we have physical infrastructure, where the cloud lives in the real world, we formed a team called AWS InCommunities. And InCommunities is one of the things that I've been most excited about in the last couple years. We all know that being engaged with your work, having a sense of higher purposes is a really, really important part for employee engagement. So AWS InCommunities has tapped into that desire for something bigger, for that sense of meaning, in a couple of different ways. AWS InCommunities is built around four pillars. The first one is STEAM Education, Access, and Equity. We all know what STEM means: science, technology, engineering and mathematics. The A is is not for the end, though. It's for arts. Because we truly believe that creative thinking comes through a focus on the arts. So AWS InCommunities focuses of STEAM. Science, technology, engineering, arts and mathematics. We also believe that we need to think big about the cloud, careers and technology. And what that's going to mean for the future. So, we've developed this pipeline mechanism pillar, which is local tech upskilling. Which is to work in the communities to find ways to bring the next generation of technologists to learn about opportunities in the space, develop those tool sets, and to think unbounded around what careers mean in technology. InCommunities focuses on environmental stewardship on a micro level in the communities where we operate. Those big off-shore wind projects can also translate into an environmental projects in the communities where we operate. And finally, InCommunities focuses on AWS employee engagement. How do people who work for AWS get involved in the communities that they work in? I wanna share four of our global signature programs. The first is AWS Tech Week, where we get involved in local schools in communities to go share careers in technology. Talk about machine learning, IoT, things that may be strange to some of the communities where we operate. Or may not even be a possibility to many children. I can tell you guys personally that this has probably been one of the most exciting things that I've been involved in with my time at Amazon. And it was one of those things where like you're, "How can I find the time to go make myself do this?" But I found myself sitting in front of a sixth grade class in rural Minnesota, in a town with 2,000 people. And it was eerily similar to the community where I grew up in rural South Dakota. This is a sixth grade class with about 30 people in it. And these types of communities are a lot like the ones that I grew up in. Small, rural, where the jobs that are in front of many of the people who live in this community are truck driver, nurse, teacher, construction worker. All great professions, but these kids have never even heard of the idea of what is a developer? What is machine learning? And it was just such an empowering opportunity to go talk to these kids and say, "Well, you know what else is out there? "All of this stuff." And to see the imagination and gears spinning in these kid's minds. And we talked about this type of program, across the world through this tech week, is truly, truly fulfilling. We also get engaged with under-represented communities through things like Girls' Tech Day. Where we focus on STEAM-based education and curriculum for girls and young women. We also recognize that it takes a full community to make these types of programs successful. So the third signature program is Family Tech Day. Where we get the entire learning environment working together to go work on these types of programs. And finally, we have Think Big Spaces. Which in essence, un-tap the creativity of these young minds and families, and communities, to go, to work on Think Big projects about leveraging the AWS Cloud, IoT, Edge, or ML, and let people's imaginations run unbounded. This is an example of Girls In Tech in Virginia. And one of our Think Big spaces in India. The InCommunities team has just done an incredible job in the short order of time building a program around the globe that impacts the communities where we operate. From Ireland to Virginia, to Cape Town, to parts of Europe, Middle East and Africa, InCommunities is doing programs around the world. We have a Stepping Stones program in Ireland, where we're focusing on diversity impacts, putting things down from new beehives to increase pollination rates. To doing Soil for Life projects in Cape Town. And finally we recognize that the problems that I have been talking about today and opportunities, sustainability, climate change, renewable energy, carbon reduction, those truly are bigger than any one company. Than any one individual, than any one government. It's gonna require a forward-looking mindset. And as a result, InCommunities is focusing on a greener future. So it won't just be people like myself and people like you working on these challenges, but having the next generation pick up the mantle for how we're gonna work on these type of problems. And to that, I'm excited to announce that we're doing the AWS Greener Future Competition in 2022. Which is a global sustainability competition that InCommunities is working on to go develop technologies and solutions that come from the next generation of thinkers, the school and communities we work on for sustainability ideas. I wanna say thank you so much for coming to this conversation this afternoon. There's so much stuff happening across Amazon and AWS within sustainability. These are some other sessions, that if you're interested in learning more about this, or wanna check into a recorded session, you're certainly welcomed to do so. I'd also like to say thank you so much. You guys have really just made this an enjoyable experience for myself, first time back on the stage. And I wanna say thank you guys so much for coming and listening today. (audience applauding)

## Subtitles with Timestamps

[00:01](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1s) Good afternoon.

[00:03](https://www.youtube.com/watch?v=Dmz45WhXENs&t=3s) My name is Nat Sahlstrom.

[00:05](https://www.youtube.com/watch?v=Dmz45WhXENs&t=5s) I work for Amazon Web Services,

[00:07](https://www.youtube.com/watch?v=Dmz45WhXENs&t=7s) within the AWS Infrastructure Group.

[00:10](https://www.youtube.com/watch?v=Dmz45WhXENs&t=10s) And I'm really, really happy to be here.

[00:12](https://www.youtube.com/watch?v=Dmz45WhXENs&t=12s) I gotta share something with you all, though.

[00:15](https://www.youtube.com/watch?v=Dmz45WhXENs&t=15s) I'm a little bit nervous.

[00:17](https://www.youtube.com/watch?v=Dmz45WhXENs&t=17s) Probably because like a lot of you,

[00:19](https://www.youtube.com/watch?v=Dmz45WhXENs&t=19s) this is my first time doing a presentation

[00:20](https://www.youtube.com/watch?v=Dmz45WhXENs&t=20s) in about two years.

[00:23](https://www.youtube.com/watch?v=Dmz45WhXENs&t=23s) And, these type of presentations are a little different

[00:26](https://www.youtube.com/watch?v=Dmz45WhXENs&t=26s) than Zoom ones, aren't they?

[00:29](https://www.youtube.com/watch?v=Dmz45WhXENs&t=29s) But my nervousness is a assuaged

[00:31](https://www.youtube.com/watch?v=Dmz45WhXENs&t=31s) by the fact that I'm so energized

[00:33](https://www.youtube.com/watch?v=Dmz45WhXENs&t=33s) to be with colleagues and customers, and partners.

[00:37](https://www.youtube.com/watch?v=Dmz45WhXENs&t=37s) And I hope you guys are feeling the same thing.

[00:39](https://www.youtube.com/watch?v=Dmz45WhXENs&t=39s) This week I've probably been hugged more warmly,

[00:42](https://www.youtube.com/watch?v=Dmz45WhXENs&t=42s) had my hand shaken more vigorously,

[00:45](https://www.youtube.com/watch?v=Dmz45WhXENs&t=45s) and smiled at by my colleagues

[00:47](https://www.youtube.com/watch?v=Dmz45WhXENs&t=47s) in ways that I probably have never had

[00:48](https://www.youtube.com/watch?v=Dmz45WhXENs&t=48s) in my over 10 years at Amazon.

[00:50](https://www.youtube.com/watch?v=Dmz45WhXENs&t=50s) So I hope you guys are experiencing the same thing,

[00:52](https://www.youtube.com/watch?v=Dmz45WhXENs&t=52s) and hopefully you guys can carry that energy

[00:53](https://www.youtube.com/watch?v=Dmz45WhXENs&t=53s) through to the rest of the week.

[00:55](https://www.youtube.com/watch?v=Dmz45WhXENs&t=55s) And through our conversation today.

[00:57](https://www.youtube.com/watch?v=Dmz45WhXENs&t=57s) But, I think that's gonna be easy to do.

[00:59](https://www.youtube.com/watch?v=Dmz45WhXENs&t=59s) Because I'm really excited about the message

[01:01](https://www.youtube.com/watch?v=Dmz45WhXENs&t=61s) that we're gonna share today.

[01:02](https://www.youtube.com/watch?v=Dmz45WhXENs&t=62s) And that's around sustainability with an AWS Cloud.

[01:06](https://www.youtube.com/watch?v=Dmz45WhXENs&t=66s) We've made a lot of progress in this space,

[01:07](https://www.youtube.com/watch?v=Dmz45WhXENs&t=67s) and I'm excited to share some of the highlights

[01:09](https://www.youtube.com/watch?v=Dmz45WhXENs&t=69s) of that journey today with you.

[01:12](https://www.youtube.com/watch?v=Dmz45WhXENs&t=72s) What we're gonna be talking about,

[01:13](https://www.youtube.com/watch?v=Dmz45WhXENs&t=73s) because this is such a broad topic,

[01:15](https://www.youtube.com/watch?v=Dmz45WhXENs&t=75s) is to start with,

[01:17](https://www.youtube.com/watch?v=Dmz45WhXENs&t=77s) what is the AWS global infrastructure footprint look like?

[01:21](https://www.youtube.com/watch?v=Dmz45WhXENs&t=81s) I'm gonna talk to you guys about The Climate Pledge,

[01:23](https://www.youtube.com/watch?v=Dmz45WhXENs&t=83s) and how AWS intersects with that.

[01:26](https://www.youtube.com/watch?v=Dmz45WhXENs&t=86s) I'm gonna talk about our progress in renewable energy.

[01:29](https://www.youtube.com/watch?v=Dmz45WhXENs&t=89s) I'm gonna share some of the stories

[01:30](https://www.youtube.com/watch?v=Dmz45WhXENs&t=90s) around how we're implementing energy efficiency

[01:33](https://www.youtube.com/watch?v=Dmz45WhXENs&t=93s) in carbon reduction, within our footprint.

[01:37](https://www.youtube.com/watch?v=Dmz45WhXENs&t=97s) I'm gonna talk about water stewardship.

[01:39](https://www.youtube.com/watch?v=Dmz45WhXENs&t=99s) And finally, I'm gonna talk about community engagement.

[01:41](https://www.youtube.com/watch?v=Dmz45WhXENs&t=101s) Which is,

[01:42](https://www.youtube.com/watch?v=Dmz45WhXENs&t=102s) how do we impact the communities where the cloud lives?

[01:45](https://www.youtube.com/watch?v=Dmz45WhXENs&t=105s) Where we operate?

[01:47](https://www.youtube.com/watch?v=Dmz45WhXENs&t=107s) Where our customer's workloads live virtually,

[01:50](https://www.youtube.com/watch?v=Dmz45WhXENs&t=110s) and we have a physical presence?

[01:55](https://www.youtube.com/watch?v=Dmz45WhXENs&t=115s) As I mentioned, I've been at Amazon over 10 years,

[01:57](https://www.youtube.com/watch?v=Dmz45WhXENs&t=117s) and it's just been an incredible journey.

[02:00](https://www.youtube.com/watch?v=Dmz45WhXENs&t=120s) And when I first started,

[02:02](https://www.youtube.com/watch?v=Dmz45WhXENs&t=122s) we had four regions.

[02:05](https://www.youtube.com/watch?v=Dmz45WhXENs&t=125s) Today, AWS has the largest global cloud infrastructure

[02:09](https://www.youtube.com/watch?v=Dmz45WhXENs&t=129s) footprint in the world.

[02:10](https://www.youtube.com/watch?v=Dmz45WhXENs&t=130s) With over 25 regions,

[02:13](https://www.youtube.com/watch?v=Dmz45WhXENs&t=133s) 81 availability zones,

[02:15](https://www.youtube.com/watch?v=Dmz45WhXENs&t=135s) and over 300 cloud front locations.

[02:18](https://www.youtube.com/watch?v=Dmz45WhXENs&t=138s) And what's interesting about this footprint,

[02:20](https://www.youtube.com/watch?v=Dmz45WhXENs&t=140s) is that it's massive.

[02:22](https://www.youtube.com/watch?v=Dmz45WhXENs&t=142s) And just last year,

[02:24](https://www.youtube.com/watch?v=Dmz45WhXENs&t=144s) there's a really, really cool tie-in

[02:27](https://www.youtube.com/watch?v=Dmz45WhXENs&t=147s) around leadership principles,

[02:29](https://www.youtube.com/watch?v=Dmz45WhXENs&t=149s) and our footprint.

[02:30](https://www.youtube.com/watch?v=Dmz45WhXENs&t=150s) And that is our new leadership principle of

[02:33](https://www.youtube.com/watch?v=Dmz45WhXENs&t=153s) with great size and scale, comes responsibility.

[02:38](https://www.youtube.com/watch?v=Dmz45WhXENs&t=158s) And a really good example of that,

[02:40](https://www.youtube.com/watch?v=Dmz45WhXENs&t=160s) is The Amazon Climate Pledge.

[02:42](https://www.youtube.com/watch?v=Dmz45WhXENs&t=162s) We announced the Amazon Climate Pledge in 2019.

[02:47](https://www.youtube.com/watch?v=Dmz45WhXENs&t=167s) In partnership with Global Optimism.

[02:49](https://www.youtube.com/watch?v=Dmz45WhXENs&t=169s) And The Climate Pledge committed Amazon,

[02:52](https://www.youtube.com/watch?v=Dmz45WhXENs&t=172s) and other signatories to commit to being net zero by 2040.

[02:57](https://www.youtube.com/watch?v=Dmz45WhXENs&t=177s) Which is 10 years faster than the Paris Agreement.

[03:00](https://www.youtube.com/watch?v=Dmz45WhXENs&t=180s) Why this is important,

[03:01](https://www.youtube.com/watch?v=Dmz45WhXENs&t=181s) is because there are scientific consensus

[03:03](https://www.youtube.com/watch?v=Dmz45WhXENs&t=183s) that if we want to really dramatically impact

[03:05](https://www.youtube.com/watch?v=Dmz45WhXENs&t=185s) and reduce the worse parts of global warming,

[03:08](https://www.youtube.com/watch?v=Dmz45WhXENs&t=188s) we need to limit global warming to 1.5 degrees Celsius.

[03:12](https://www.youtube.com/watch?v=Dmz45WhXENs&t=192s) And The Climate Pledge allows companies

[03:14](https://www.youtube.com/watch?v=Dmz45WhXENs&t=194s) to think collaboratively

[03:15](https://www.youtube.com/watch?v=Dmz45WhXENs&t=195s) about how they can implement technologies

[03:17](https://www.youtube.com/watch?v=Dmz45WhXENs&t=197s) and business solutions to go drive out

[03:19](https://www.youtube.com/watch?v=Dmz45WhXENs&t=199s) carbon from their businesses.

[03:22](https://www.youtube.com/watch?v=Dmz45WhXENs&t=202s) Signatories commit to being to net zero by 2040.

[03:26](https://www.youtube.com/watch?v=Dmz45WhXENs&t=206s) And when Amazon signed The Climate Pledge and founded this,

[03:29](https://www.youtube.com/watch?v=Dmz45WhXENs&t=209s) we committed to be 100% renewable energy by 2030.

[03:34](https://www.youtube.com/watch?v=Dmz45WhXENs&t=214s) But we since stepped on the gas,

[03:36](https://www.youtube.com/watch?v=Dmz45WhXENs&t=216s) and I'm gonna talk about that,

[03:37](https://www.youtube.com/watch?v=Dmz45WhXENs&t=217s) and pull that target in five years, to 2025.

[03:41](https://www.youtube.com/watch?v=Dmz45WhXENs&t=221s) Another instrument that we put to work in The Climate Pledge

[03:45](https://www.youtube.com/watch?v=Dmz45WhXENs&t=225s) is funding The Climate Pledge Fund.

[03:47](https://www.youtube.com/watch?v=Dmz45WhXENs&t=227s) Which is a $2 billion fund

[03:49](https://www.youtube.com/watch?v=Dmz45WhXENs&t=229s) dedicated to funding companies and technologies

[03:52](https://www.youtube.com/watch?v=Dmz45WhXENs&t=232s) who's products and solutions are gonna be integral

[03:55](https://www.youtube.com/watch?v=Dmz45WhXENs&t=235s) to transitioning to a low carbon economy.

[04:00](https://www.youtube.com/watch?v=Dmz45WhXENs&t=240s) We've made a lot of progress to Climate Pledge,

[04:02](https://www.youtube.com/watch?v=Dmz45WhXENs&t=242s) and we're really excited about this.

[04:03](https://www.youtube.com/watch?v=Dmz45WhXENs&t=243s) At this time last year,

[04:05](https://www.youtube.com/watch?v=Dmz45WhXENs&t=245s) The Climate Pledge had roughly 31 signatories.

[04:08](https://www.youtube.com/watch?v=Dmz45WhXENs&t=248s) We're now over 200 companies a year from that period,

[04:11](https://www.youtube.com/watch?v=Dmz45WhXENs&t=251s) and continue to grow.

[04:13](https://www.youtube.com/watch?v=Dmz45WhXENs&t=253s) If you are interested in participating in The Climate Pledge

[04:17](https://www.youtube.com/watch?v=Dmz45WhXENs&t=257s) there's the three fundamental principles

[04:19](https://www.youtube.com/watch?v=Dmz45WhXENs&t=259s) that participants agree to

[04:20](https://www.youtube.com/watch?v=Dmz45WhXENs&t=260s) when they sign The Climate Pledge.

[04:23](https://www.youtube.com/watch?v=Dmz45WhXENs&t=263s) One, is regular reporting.

[04:26](https://www.youtube.com/watch?v=Dmz45WhXENs&t=266s) We all acknowledge that transparency measuring, mapping,

[04:30](https://www.youtube.com/watch?v=Dmz45WhXENs&t=270s) are critical to reducing our carbon footprint.

[04:33](https://www.youtube.com/watch?v=Dmz45WhXENs&t=273s) The second is carbon elimination.

[04:37](https://www.youtube.com/watch?v=Dmz45WhXENs&t=277s) So, signatories will commit to de-carbonization strategies

[04:39](https://www.youtube.com/watch?v=Dmz45WhXENs&t=279s) across their business.

[04:41](https://www.youtube.com/watch?v=Dmz45WhXENs&t=281s) And this involves the host of programs,

[04:44](https://www.youtube.com/watch?v=Dmz45WhXENs&t=284s) such as energy efficiency,

[04:45](https://www.youtube.com/watch?v=Dmz45WhXENs&t=285s) implementing renewable energy programs,

[04:48](https://www.youtube.com/watch?v=Dmz45WhXENs&t=288s) and de-carbonize their business

[04:50](https://www.youtube.com/watch?v=Dmz45WhXENs&t=290s) by looking at the materials in which they operate

[04:51](https://www.youtube.com/watch?v=Dmz45WhXENs&t=291s) in the physical realm.

[04:54](https://www.youtube.com/watch?v=Dmz45WhXENs&t=294s) And finally, since we do operate in the physical realm,

[04:56](https://www.youtube.com/watch?v=Dmz45WhXENs&t=296s) we know that it's very, very challenging

[04:58](https://www.youtube.com/watch?v=Dmz45WhXENs&t=298s) to reduce all carbon from our business.

[05:01](https://www.youtube.com/watch?v=Dmz45WhXENs&t=301s) And signatories then agree that they'll find

[05:03](https://www.youtube.com/watch?v=Dmz45WhXENs&t=303s) real, credible offsets to negate the rest of their missions.

[05:10](https://www.youtube.com/watch?v=Dmz45WhXENs&t=310s) As I mentioned, renewable energy is a big part

[05:13](https://www.youtube.com/watch?v=Dmz45WhXENs&t=313s) of The Climate Pledge,

[05:15](https://www.youtube.com/watch?v=Dmz45WhXENs&t=315s) and we've made a lot of progress in this space.

[05:17](https://www.youtube.com/watch?v=Dmz45WhXENs&t=317s) We're well on-track to getting there by 2025.

[05:20](https://www.youtube.com/watch?v=Dmz45WhXENs&t=320s) And it's worth talking about this a little bit.

[05:23](https://www.youtube.com/watch?v=Dmz45WhXENs&t=323s) I mentioned that I've been at Amazon 10 years.

[05:26](https://www.youtube.com/watch?v=Dmz45WhXENs&t=326s) I'm in front of you guys today

[05:27](https://www.youtube.com/watch?v=Dmz45WhXENs&t=327s) with a bit of my dream job.

[05:29](https://www.youtube.com/watch?v=Dmz45WhXENs&t=329s) When I first started at Amazon,

[05:31](https://www.youtube.com/watch?v=Dmz45WhXENs&t=331s) I was tasked with the kind of ambiguous charter of,

[05:34](https://www.youtube.com/watch?v=Dmz45WhXENs&t=334s) we're spending a lot of money on energy,

[05:36](https://www.youtube.com/watch?v=Dmz45WhXENs&t=336s) can you go figure this out?

[05:38](https://www.youtube.com/watch?v=Dmz45WhXENs&t=338s) That was my job at that point in time.

[05:40](https://www.youtube.com/watch?v=Dmz45WhXENs&t=340s) Really exciting, and a great opportunity.

[05:42](https://www.youtube.com/watch?v=Dmz45WhXENs&t=342s) If you go look at the progress we've made in this space,

[05:45](https://www.youtube.com/watch?v=Dmz45WhXENs&t=345s) something we're really, really proud of

[05:47](https://www.youtube.com/watch?v=Dmz45WhXENs&t=347s) what we delivered on behalf of our customers.

[05:49](https://www.youtube.com/watch?v=Dmz45WhXENs&t=349s) And what's interesting, is the path of acceleration.

[05:52](https://www.youtube.com/watch?v=Dmz45WhXENs&t=352s) Pre-2020, we had under 6500 megawatts of load.

[05:57](https://www.youtube.com/watch?v=Dmz45WhXENs&t=357s) In 2020, we signed up a lot more.

[06:02](https://www.youtube.com/watch?v=Dmz45WhXENs&t=362s) In 2021, already, we did 3.6 gigawatts

[06:05](https://www.youtube.com/watch?v=Dmz45WhXENs&t=365s) of new utility-scale wind and solar projects.

[06:09](https://www.youtube.com/watch?v=Dmz45WhXENs&t=369s) And just yesterday, we announced 18 new projects,

[06:12](https://www.youtube.com/watch?v=Dmz45WhXENs&t=372s) bringing another two gigawatts of capacity around,

[06:14](https://www.youtube.com/watch?v=Dmz45WhXENs&t=374s) across Europe, and the Americas.

[06:18](https://www.youtube.com/watch?v=Dmz45WhXENs&t=378s) We now have over 12 gigawatts of load.

[06:20](https://www.youtube.com/watch?v=Dmz45WhXENs&t=380s) This is a tremendous amount of renewable energy capacity.

[06:23](https://www.youtube.com/watch?v=Dmz45WhXENs&t=383s) And often times, we use these figures and these units,

[06:26](https://www.youtube.com/watch?v=Dmz45WhXENs&t=386s) like gigawatts,

[06:27](https://www.youtube.com/watch?v=Dmz45WhXENs&t=387s) I hear a lot of "Back to the Future" jokes.

[06:29](https://www.youtube.com/watch?v=Dmz45WhXENs&t=389s) We use megawatt hours, and it's tough to quantify that.

[06:33](https://www.youtube.com/watch?v=Dmz45WhXENs&t=393s) So just for a little bit of perspective,

[06:34](https://www.youtube.com/watch?v=Dmz45WhXENs&t=394s) often times when we think about

[06:36](https://www.youtube.com/watch?v=Dmz45WhXENs&t=396s) really large utility companies,

[06:38](https://www.youtube.com/watch?v=Dmz45WhXENs&t=398s) they hold eight, nine gigawatts.

[06:40](https://www.youtube.com/watch?v=Dmz45WhXENs&t=400s) Amazon's renewable energy holdings right now,

[06:43](https://www.youtube.com/watch?v=Dmz45WhXENs&t=403s) rival, or are larger than most of,

[06:45](https://www.youtube.com/watch?v=Dmz45WhXENs&t=405s) many of the U.S. large investor-run utilities.

[06:49](https://www.youtube.com/watch?v=Dmz45WhXENs&t=409s) Well, what does this mean for the world?

[06:51](https://www.youtube.com/watch?v=Dmz45WhXENs&t=411s) Well, what does it mean that Amazon

[06:53](https://www.youtube.com/watch?v=Dmz45WhXENs&t=413s) has over 274 renewable projects across the world?

[06:56](https://www.youtube.com/watch?v=Dmz45WhXENs&t=416s) What we're focused on,

[06:58](https://www.youtube.com/watch?v=Dmz45WhXENs&t=418s) is avoiding carbon emissions.

[06:59](https://www.youtube.com/watch?v=Dmz45WhXENs&t=419s) So we can reduce the carbon environmental impact

[07:02](https://www.youtube.com/watch?v=Dmz45WhXENs&t=422s) of our cloud services.

[07:04](https://www.youtube.com/watch?v=Dmz45WhXENs&t=424s) And we believe this is happening in a big way

[07:06](https://www.youtube.com/watch?v=Dmz45WhXENs&t=426s) through our renewable energy projects.

[07:08](https://www.youtube.com/watch?v=Dmz45WhXENs&t=428s) When all the projects that we signed to date come online,

[07:12](https://www.youtube.com/watch?v=Dmz45WhXENs&t=432s) it will reduce 13.7 million metric tons

[07:15](https://www.youtube.com/watch?v=Dmz45WhXENs&t=435s) of carbon emissions that will be avoided.

[07:18](https://www.youtube.com/watch?v=Dmz45WhXENs&t=438s) I don't know if you guys are really sharp

[07:20](https://www.youtube.com/watch?v=Dmz45WhXENs&t=440s) on your Emerald Isles geography,

[07:22](https://www.youtube.com/watch?v=Dmz45WhXENs&t=442s) but that outline is the country of Ireland.

[07:25](https://www.youtube.com/watch?v=Dmz45WhXENs&t=445s) Imagine the country of Ireland completely composed of woods.

[07:30](https://www.youtube.com/watch?v=Dmz45WhXENs&t=450s) That's how much carbon emissions

[07:31](https://www.youtube.com/watch?v=Dmz45WhXENs&t=451s) would be avoided by our projects.

[07:36](https://www.youtube.com/watch?v=Dmz45WhXENs&t=456s) And doing this is not as simple as,

[07:38](https://www.youtube.com/watch?v=Dmz45WhXENs&t=458s) simply taking out your credit card, and saying,

[07:40](https://www.youtube.com/watch?v=Dmz45WhXENs&t=460s) "Hey, every renewable energy developer in the world,

[07:43](https://www.youtube.com/watch?v=Dmz45WhXENs&t=463s) "I want power, just go get me these projects."

[07:46](https://www.youtube.com/watch?v=Dmz45WhXENs&t=466s) It's actually a complex undertaking.

[07:48](https://www.youtube.com/watch?v=Dmz45WhXENs&t=468s) And what's really challenging about this,

[07:50](https://www.youtube.com/watch?v=Dmz45WhXENs&t=470s) is that many parts of the world,

[07:51](https://www.youtube.com/watch?v=Dmz45WhXENs&t=471s) you simply can't go and do a standard procurement model

[07:54](https://www.youtube.com/watch?v=Dmz45WhXENs&t=474s) to go buy renewable projects.

[07:56](https://www.youtube.com/watch?v=Dmz45WhXENs&t=476s) And, one of the things that we've been doing

[07:58](https://www.youtube.com/watch?v=Dmz45WhXENs&t=478s) over the last couple of years,

[07:59](https://www.youtube.com/watch?v=Dmz45WhXENs&t=479s) is innovating in the commercial space,

[08:01](https://www.youtube.com/watch?v=Dmz45WhXENs&t=481s) the regulatory space, and the policy space,

[08:04](https://www.youtube.com/watch?v=Dmz45WhXENs&t=484s) to go deliver renewable projects,

[08:06](https://www.youtube.com/watch?v=Dmz45WhXENs&t=486s) where previously, corporate companies

[08:08](https://www.youtube.com/watch?v=Dmz45WhXENs&t=488s) weren't able to do that.

[08:10](https://www.youtube.com/watch?v=Dmz45WhXENs&t=490s) Examples of that include Japan and Singapore.

[08:13](https://www.youtube.com/watch?v=Dmz45WhXENs&t=493s) The projects we announced,

[08:15](https://www.youtube.com/watch?v=Dmz45WhXENs&t=495s) and the projects we just announced in South Africa,

[08:17](https://www.youtube.com/watch?v=Dmz45WhXENs&t=497s) is the first corporate project

[08:19](https://www.youtube.com/watch?v=Dmz45WhXENs&t=499s) where utility-scale renewable energy

[08:21](https://www.youtube.com/watch?v=Dmz45WhXENs&t=501s) is brought on behalf of a corporate customer.

[08:23](https://www.youtube.com/watch?v=Dmz45WhXENs&t=503s) And this seems a little bit esoteric,

[08:25](https://www.youtube.com/watch?v=Dmz45WhXENs&t=505s) you might say, "What's the big deal?"

[08:28](https://www.youtube.com/watch?v=Dmz45WhXENs&t=508s) But it's actually very challenging,

[08:30](https://www.youtube.com/watch?v=Dmz45WhXENs&t=510s) and impossible until the efforts that we put in place

[08:34](https://www.youtube.com/watch?v=Dmz45WhXENs&t=514s) actually go do this type of work.

[08:35](https://www.youtube.com/watch?v=Dmz45WhXENs&t=515s) And why this is important,

[08:37](https://www.youtube.com/watch?v=Dmz45WhXENs&t=517s) is it's not just about how we can de-carbonize,

[08:39](https://www.youtube.com/watch?v=Dmz45WhXENs&t=519s) how we can bring more renewable energy under the grid,

[08:42](https://www.youtube.com/watch?v=Dmz45WhXENs&t=522s) but how we can create commercial structures

[08:44](https://www.youtube.com/watch?v=Dmz45WhXENs&t=524s) that other companies, and other people can replicate,

[08:47](https://www.youtube.com/watch?v=Dmz45WhXENs&t=527s) as they implement decarbonization strategies.

[08:50](https://www.youtube.com/watch?v=Dmz45WhXENs&t=530s) Similar example you might think about,

[08:52](https://www.youtube.com/watch?v=Dmz45WhXENs&t=532s) well, this is a massive 20 gigawatt solar project.

[08:54](https://www.youtube.com/watch?v=Dmz45WhXENs&t=534s) It's out in the middle of the dessert in South Africa.

[08:57](https://www.youtube.com/watch?v=Dmz45WhXENs&t=537s) Well, we did a 20 gigawatt project in Japan.

[09:00](https://www.youtube.com/watch?v=Dmz45WhXENs&t=540s) If you've had the privilege of going to Tokyo before,

[09:03](https://www.youtube.com/watch?v=Dmz45WhXENs&t=543s) it's a fascinating city.

[09:04](https://www.youtube.com/watch?v=Dmz45WhXENs&t=544s) A really fun place to visit.

[09:06](https://www.youtube.com/watch?v=Dmz45WhXENs&t=546s) But can you imagine a place

[09:07](https://www.youtube.com/watch?v=Dmz45WhXENs&t=547s) where you would put this many solar panels in Tokyo?

[09:10](https://www.youtube.com/watch?v=Dmz45WhXENs&t=550s) We had to think of innovative approaches.

[09:12](https://www.youtube.com/watch?v=Dmz45WhXENs&t=552s) So we worked with developers,

[09:14](https://www.youtube.com/watch?v=Dmz45WhXENs&t=554s) and find ways where we can bring impactful, large projects

[09:18](https://www.youtube.com/watch?v=Dmz45WhXENs&t=558s) to scale and online.

[09:19](https://www.youtube.com/watch?v=Dmz45WhXENs&t=559s) And in Tokyo, we've put panels across 440 locations,

[09:23](https://www.youtube.com/watch?v=Dmz45WhXENs&t=563s) across the city, to bring big impact

[09:26](https://www.youtube.com/watch?v=Dmz45WhXENs&t=566s) renewable projects to bear.

[09:29](https://www.youtube.com/watch?v=Dmz45WhXENs&t=569s) And we also know that it's not just about

[09:31](https://www.youtube.com/watch?v=Dmz45WhXENs&t=571s) doing lots of projects.

[09:32](https://www.youtube.com/watch?v=Dmz45WhXENs&t=572s) It's about innovating,

[09:33](https://www.youtube.com/watch?v=Dmz45WhXENs&t=573s) and looking towards the challenges in the future.

[09:36](https://www.youtube.com/watch?v=Dmz45WhXENs&t=576s) And one of these is the intermittency problem.

[09:39](https://www.youtube.com/watch?v=Dmz45WhXENs&t=579s) You may have heard that term before.

[09:41](https://www.youtube.com/watch?v=Dmz45WhXENs&t=581s) But simply stated is,

[09:42](https://www.youtube.com/watch?v=Dmz45WhXENs&t=582s) what do you do when the sun's not shining,

[09:44](https://www.youtube.com/watch?v=Dmz45WhXENs&t=584s) or the wind's not blowing?

[09:46](https://www.youtube.com/watch?v=Dmz45WhXENs&t=586s) You need storage.

[09:48](https://www.youtube.com/watch?v=Dmz45WhXENs&t=588s) And we recognize that, as well.

[09:50](https://www.youtube.com/watch?v=Dmz45WhXENs&t=590s) And accordingly, we've done our first two large

[09:53](https://www.youtube.com/watch?v=Dmz45WhXENs&t=593s) solar and storage projects this year.

[09:56](https://www.youtube.com/watch?v=Dmz45WhXENs&t=596s) And these projects are our first bridging solutions

[09:58](https://www.youtube.com/watch?v=Dmz45WhXENs&t=598s) towards our eventual goal of 24/7 renewable power.

[10:02](https://www.youtube.com/watch?v=Dmz45WhXENs&t=602s) Powering our operations 100% across all of Amazon.

[10:08](https://www.youtube.com/watch?v=Dmz45WhXENs&t=608s) In addition to these storage and solar integration projects,

[10:12](https://www.youtube.com/watch?v=Dmz45WhXENs&t=612s) we also know that we need to go big.

[10:14](https://www.youtube.com/watch?v=Dmz45WhXENs&t=614s) And a great way to go big, is with off-shore wind.

[10:18](https://www.youtube.com/watch?v=Dmz45WhXENs&t=618s) We've already announced

[10:19](https://www.youtube.com/watch?v=Dmz45WhXENs&t=619s) two large off-shore wind projects to date.

[10:23](https://www.youtube.com/watch?v=Dmz45WhXENs&t=623s) And the really cool thing

[10:23](https://www.youtube.com/watch?v=Dmz45WhXENs&t=623s) about these off-shore wind projects

[10:25](https://www.youtube.com/watch?v=Dmz45WhXENs&t=625s) is simply a matter of physics.

[10:27](https://www.youtube.com/watch?v=Dmz45WhXENs&t=627s) When you go look at the size of the turbines

[10:29](https://www.youtube.com/watch?v=Dmz45WhXENs&t=629s) and the sails that are incorporated

[10:31](https://www.youtube.com/watch?v=Dmz45WhXENs&t=631s) in these off-shore projects,

[10:33](https://www.youtube.com/watch?v=Dmz45WhXENs&t=633s) and you combine that with the consistent high wind speed

[10:36](https://www.youtube.com/watch?v=Dmz45WhXENs&t=636s) that you get out at sea,

[10:38](https://www.youtube.com/watch?v=Dmz45WhXENs&t=638s) you get much higher yields.

[10:40](https://www.youtube.com/watch?v=Dmz45WhXENs&t=640s) Today, off-shore wind currently only produces

[10:43](https://www.youtube.com/watch?v=Dmz45WhXENs&t=643s) a small amount of the wind energy

[10:45](https://www.youtube.com/watch?v=Dmz45WhXENs&t=645s) that goes into power's grids.

[10:47](https://www.youtube.com/watch?v=Dmz45WhXENs&t=647s) But we know that if we go look at

[10:49](https://www.youtube.com/watch?v=Dmz45WhXENs&t=649s) what that untapped potential is,

[10:51](https://www.youtube.com/watch?v=Dmz45WhXENs&t=651s) wind technology companies and energy economists

[10:55](https://www.youtube.com/watch?v=Dmz45WhXENs&t=655s) predict that off-shore wind could generate

[10:58](https://www.youtube.com/watch?v=Dmz45WhXENs&t=658s) over 18 times the power load that the world consumes today.

[11:02](https://www.youtube.com/watch?v=Dmz45WhXENs&t=662s) So it is truly a massive and untapped resource

[11:04](https://www.youtube.com/watch?v=Dmz45WhXENs&t=664s) that we're looking at very closely.

[11:07](https://www.youtube.com/watch?v=Dmz45WhXENs&t=667s) We also know that it's not just about

[11:10](https://www.youtube.com/watch?v=Dmz45WhXENs&t=670s) putting lots of projects and storage and size,

[11:12](https://www.youtube.com/watch?v=Dmz45WhXENs&t=672s) it's about being smart about how we use these assets,

[11:15](https://www.youtube.com/watch?v=Dmz45WhXENs&t=675s) how we integrate them.

[11:17](https://www.youtube.com/watch?v=Dmz45WhXENs&t=677s) And to that impact, we're a lot like you.

[11:20](https://www.youtube.com/watch?v=Dmz45WhXENs&t=680s) We use the AWS Cloud, and tools and services,

[11:23](https://www.youtube.com/watch?v=Dmz45WhXENs&t=683s) to find ways to optimize the performance

[11:25](https://www.youtube.com/watch?v=Dmz45WhXENs&t=685s) of our renewable energy assets.

[11:27](https://www.youtube.com/watch?v=Dmz45WhXENs&t=687s) And a great way we do that,

[11:29](https://www.youtube.com/watch?v=Dmz45WhXENs&t=689s) is with the team that we have called,

[11:31](https://www.youtube.com/watch?v=Dmz45WhXENs&t=691s) the Renewable Energy Optimization Team.

[11:33](https://www.youtube.com/watch?v=Dmz45WhXENs&t=693s) So I'm excited to share a short little video with you guys

[11:36](https://www.youtube.com/watch?v=Dmz45WhXENs&t=696s) about how we use AWS Services to efficiently optimize

[11:42](https://www.youtube.com/watch?v=Dmz45WhXENs&t=702s) our renewable energy projects.

[11:59](https://www.youtube.com/watch?v=Dmz45WhXENs&t=719s) With our renewable goal,

[12:00](https://www.youtube.com/watch?v=Dmz45WhXENs&t=720s) we're developing solar projects, wind projects,

[12:02](https://www.youtube.com/watch?v=Dmz45WhXENs&t=722s) including this wind farm here in California.

[12:04](https://www.youtube.com/watch?v=Dmz45WhXENs&t=724s) And were developing software built on AWS

[12:07](https://www.youtube.com/watch?v=Dmz45WhXENs&t=727s) to optimize our renewable portfolio at scale.

[12:10](https://www.youtube.com/watch?v=Dmz45WhXENs&t=730s) So here we're looking at live metrics from Turbine Five.

[12:14](https://www.youtube.com/watch?v=Dmz45WhXENs&t=734s) And we have a total of 200 metrics

[12:16](https://www.youtube.com/watch?v=Dmz45WhXENs&t=736s) from each turbine at this facility.

[12:19](https://www.youtube.com/watch?v=Dmz45WhXENs&t=739s) My name is Athanasios Caramanolis,

[12:21](https://www.youtube.com/watch?v=Dmz45WhXENs&t=741s) and I lead the Renewable Energy Optimization Team at AWS.

[12:25](https://www.youtube.com/watch?v=Dmz45WhXENs&t=745s) With AWS IoT and machine learning services,

[12:28](https://www.youtube.com/watch?v=Dmz45WhXENs&t=748s) we stream and analyze millions of data points in real time

[12:32](https://www.youtube.com/watch?v=Dmz45WhXENs&t=752s) from projects across the world.

[12:35](https://www.youtube.com/watch?v=Dmz45WhXENs&t=755s) At AWS, we're looking at how to decarbonize

[12:36](https://www.youtube.com/watch?v=Dmz45WhXENs&t=756s) our entire business.

[12:38](https://www.youtube.com/watch?v=Dmz45WhXENs&t=758s) This year Amazon announced it's first two

[12:40](https://www.youtube.com/watch?v=Dmz45WhXENs&t=760s) solar-plus storage projects.

[12:41](https://www.youtube.com/watch?v=Dmz45WhXENs&t=761s) This software will let us optimization

[12:43](https://www.youtube.com/watch?v=Dmz45WhXENs&t=763s) how we deliver clean electricity onto the gird.

[12:46](https://www.youtube.com/watch?v=Dmz45WhXENs&t=766s) Decarbonizing our energy system is an enormous challenge.

[12:49](https://www.youtube.com/watch?v=Dmz45WhXENs&t=769s) We're using the AWS Cloud

[12:51](https://www.youtube.com/watch?v=Dmz45WhXENs&t=771s) to build automated mechanisms at scale.

[12:53](https://www.youtube.com/watch?v=Dmz45WhXENs&t=773s) Ensuring our renewable fleet delivers

[12:55](https://www.youtube.com/watch?v=Dmz45WhXENs&t=775s) as much clean electricity as possible.

[13:04](https://www.youtube.com/watch?v=Dmz45WhXENs&t=784s) Thank you.

[13:07](https://www.youtube.com/watch?v=Dmz45WhXENs&t=787s) By 2025, we expect that the production we have,

[13:10](https://www.youtube.com/watch?v=Dmz45WhXENs&t=790s) they'll be increased by using AWS Services

[13:13](https://www.youtube.com/watch?v=Dmz45WhXENs&t=793s) to optimize performance of our renewable assets.

[13:16](https://www.youtube.com/watch?v=Dmz45WhXENs&t=796s) We'll bring on the size of 200 megawatt wind farm.

[13:21](https://www.youtube.com/watch?v=Dmz45WhXENs&t=801s) That's a big deal.

[13:22](https://www.youtube.com/watch?v=Dmz45WhXENs&t=802s) That's $100 million investment

[13:24](https://www.youtube.com/watch?v=Dmz45WhXENs&t=804s) that we're not having to make

[13:25](https://www.youtube.com/watch?v=Dmz45WhXENs&t=805s) because we're increasing the renewable energy performance,

[13:27](https://www.youtube.com/watch?v=Dmz45WhXENs&t=807s) the assets we have using the AWS Cloud.

[13:31](https://www.youtube.com/watch?v=Dmz45WhXENs&t=811s) And we're gonna continue to optimize

[13:32](https://www.youtube.com/watch?v=Dmz45WhXENs&t=812s) renewable energy performance using AWS Cloud.

[13:35](https://www.youtube.com/watch?v=Dmz45WhXENs&t=815s) And with the progress that we've made to date,

[13:37](https://www.youtube.com/watch?v=Dmz45WhXENs&t=817s) I'm very excited that I can tell you that

[13:38](https://www.youtube.com/watch?v=Dmz45WhXENs&t=818s) Amazon is still the world's largest corporate buyer

[13:41](https://www.youtube.com/watch?v=Dmz45WhXENs&t=821s) of renewable energy.

[13:44](https://www.youtube.com/watch?v=Dmz45WhXENs&t=824s) I wanna shift gears here for a second.

[13:46](https://www.youtube.com/watch?v=Dmz45WhXENs&t=826s) And this may sound a little bit strange.

[13:50](https://www.youtube.com/watch?v=Dmz45WhXENs&t=830s) But, fancy videos and big, sweeping vistas

[13:54](https://www.youtube.com/watch?v=Dmz45WhXENs&t=834s) of wind turbines, off-shore wind projects,

[13:58](https://www.youtube.com/watch?v=Dmz45WhXENs&t=838s) I would argue can sometimes be a distraction.

[14:02](https://www.youtube.com/watch?v=Dmz45WhXENs&t=842s) That may seem like a paradox, that may seem strange.

[14:05](https://www.youtube.com/watch?v=Dmz45WhXENs&t=845s) And you're like, "Well, why are you telling us

[14:06](https://www.youtube.com/watch?v=Dmz45WhXENs&t=846s) "so much about that?"

[14:08](https://www.youtube.com/watch?v=Dmz45WhXENs&t=848s) Well, it is very important.

[14:09](https://www.youtube.com/watch?v=Dmz45WhXENs&t=849s) That is the supply side of the stack.

[14:12](https://www.youtube.com/watch?v=Dmz45WhXENs&t=852s) But what gets lost often times is efficiency.

[14:16](https://www.youtube.com/watch?v=Dmz45WhXENs&t=856s) We know that the greenest electron

[14:18](https://www.youtube.com/watch?v=Dmz45WhXENs&t=858s) is the one that you do not use.

[14:20](https://www.youtube.com/watch?v=Dmz45WhXENs&t=860s) And often times, that's the less sexy work.

[14:23](https://www.youtube.com/watch?v=Dmz45WhXENs&t=863s) It's the less optical work.

[14:25](https://www.youtube.com/watch?v=Dmz45WhXENs&t=865s) But is really, really critical

[14:26](https://www.youtube.com/watch?v=Dmz45WhXENs&t=866s) if we're gonna be serious about

[14:27](https://www.youtube.com/watch?v=Dmz45WhXENs&t=867s) combating climate change, and reducing carbon.

[14:31](https://www.youtube.com/watch?v=Dmz45WhXENs&t=871s) And I'm very pleased to tell you that

[14:32](https://www.youtube.com/watch?v=Dmz45WhXENs&t=872s) increasing efficiency and reducing carbon emissions

[14:35](https://www.youtube.com/watch?v=Dmz45WhXENs&t=875s) is integral to how AWS operates its infrastructure,

[14:39](https://www.youtube.com/watch?v=Dmz45WhXENs&t=879s) and it's data centers, and it's cloud platform.

[14:41](https://www.youtube.com/watch?v=Dmz45WhXENs&t=881s) So I'm gonna spend a little bit of time today

[14:43](https://www.youtube.com/watch?v=Dmz45WhXENs&t=883s) diving into the dirt,

[14:45](https://www.youtube.com/watch?v=Dmz45WhXENs&t=885s) diving into some of the details on the margin

[14:48](https://www.youtube.com/watch?v=Dmz45WhXENs&t=888s) about how we actually do this to reduce

[14:50](https://www.youtube.com/watch?v=Dmz45WhXENs&t=890s) the carbon of our business.

[14:54](https://www.youtube.com/watch?v=Dmz45WhXENs&t=894s) The first side is simply about how do we operate,

[14:56](https://www.youtube.com/watch?v=Dmz45WhXENs&t=896s) engineer, and build our data centers?

[14:59](https://www.youtube.com/watch?v=Dmz45WhXENs&t=899s) This may seem like well, of course,

[15:03](https://www.youtube.com/watch?v=Dmz45WhXENs&t=903s) don't you guys just do a good job?

[15:04](https://www.youtube.com/watch?v=Dmz45WhXENs&t=904s) Well yes, we have the highest levels of reliability

[15:06](https://www.youtube.com/watch?v=Dmz45WhXENs&t=906s) and security,

[15:07](https://www.youtube.com/watch?v=Dmz45WhXENs&t=907s) but we're also very, very keyed in

[15:09](https://www.youtube.com/watch?v=Dmz45WhXENs&t=909s) on how we use energy within our data centers.

[15:12](https://www.youtube.com/watch?v=Dmz45WhXENs&t=912s) And this comes down to places

[15:13](https://www.youtube.com/watch?v=Dmz45WhXENs&t=913s) that you might not even think about.

[15:15](https://www.youtube.com/watch?v=Dmz45WhXENs&t=915s) And that includes cooling technology.

[15:19](https://www.youtube.com/watch?v=Dmz45WhXENs&t=919s) Cooling is one of the biggest energy consumers

[15:22](https://www.youtube.com/watch?v=Dmz45WhXENs&t=922s) in the data center next to IT load.

[15:24](https://www.youtube.com/watch?v=Dmz45WhXENs&t=924s) So constantly thinking about

[15:26](https://www.youtube.com/watch?v=Dmz45WhXENs&t=926s) how do we increase the efficiency of our cooling.

[15:28](https://www.youtube.com/watch?v=Dmz45WhXENs&t=928s) And this is where engineering dive deep really matters.

[15:31](https://www.youtube.com/watch?v=Dmz45WhXENs&t=931s) Because we go all the way to the margins on things

[15:34](https://www.youtube.com/watch?v=Dmz45WhXENs&t=934s) to find out how we can squeeze out

[15:35](https://www.youtube.com/watch?v=Dmz45WhXENs&t=935s) energy efficiency gains in our business.

[15:39](https://www.youtube.com/watch?v=Dmz45WhXENs&t=939s) Now a great example of this is the evaporative cooling media

[15:43](https://www.youtube.com/watch?v=Dmz45WhXENs&t=943s) that we use to cool our data centers.

[15:46](https://www.youtube.com/watch?v=Dmz45WhXENs&t=946s) Now this may seem like a really weird esoteric detail,

[15:49](https://www.youtube.com/watch?v=Dmz45WhXENs&t=949s) but it's actually really important.

[15:51](https://www.youtube.com/watch?v=Dmz45WhXENs&t=951s) The evaporative media that we use

[15:53](https://www.youtube.com/watch?v=Dmz45WhXENs&t=953s) to cool our data centers has a big impact

[15:55](https://www.youtube.com/watch?v=Dmz45WhXENs&t=955s) to the efficiency of our operations.

[15:58](https://www.youtube.com/watch?v=Dmz45WhXENs&t=958s) So our engineering teams go work with vendors

[16:00](https://www.youtube.com/watch?v=Dmz45WhXENs&t=960s) who actually go work on these media

[16:01](https://www.youtube.com/watch?v=Dmz45WhXENs&t=961s) that we use in our data centers.

[16:03](https://www.youtube.com/watch?v=Dmz45WhXENs&t=963s) And find ways to experiment and engineer

[16:05](https://www.youtube.com/watch?v=Dmz45WhXENs&t=965s) about making that more efficient.

[16:07](https://www.youtube.com/watch?v=Dmz45WhXENs&t=967s) And one of the things that we've recently done,

[16:09](https://www.youtube.com/watch?v=Dmz45WhXENs&t=969s) is change out that evaporative media

[16:10](https://www.youtube.com/watch?v=Dmz45WhXENs&t=970s) by working with partners.

[16:12](https://www.youtube.com/watch?v=Dmz45WhXENs&t=972s) And the result, we're increasing the efficiency

[16:15](https://www.youtube.com/watch?v=Dmz45WhXENs&t=975s) of our cooling equipment by 20%.

[16:18](https://www.youtube.com/watch?v=Dmz45WhXENs&t=978s) That has big energy gain impacts.

[16:21](https://www.youtube.com/watch?v=Dmz45WhXENs&t=981s) And it's not just about the energy infrastructure,

[16:25](https://www.youtube.com/watch?v=Dmz45WhXENs&t=985s) the energy consuming assets within the data center floor,

[16:28](https://www.youtube.com/watch?v=Dmz45WhXENs&t=988s) it's also about utilization

[16:30](https://www.youtube.com/watch?v=Dmz45WhXENs&t=990s) and how compute works efficiency within the data center.

[16:33](https://www.youtube.com/watch?v=Dmz45WhXENs&t=993s) And if you had any of the chances

[16:34](https://www.youtube.com/watch?v=Dmz45WhXENs&t=994s) to be familiarized with Graviton,

[16:36](https://www.youtube.com/watch?v=Dmz45WhXENs&t=996s) last year we shared information about Graviton,

[16:39](https://www.youtube.com/watch?v=Dmz45WhXENs&t=999s) about how it's our most power-efficiency processor,

[16:42](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1002s) and how that produces better performance per watt

[16:45](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1005s) than previous EC2 generation processors.

[16:48](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1008s) And that can be very exciting because there's cost-savings,

[16:51](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1011s) there's efficiency gains there.

[16:53](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1013s) But one of the things gets lost

[16:54](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1014s) is energy efficiency,

[16:56](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1016s) sustainability, and carbon-reduction gains.

[17:00](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1020s) Graviton is our most power-efficient

[17:03](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1023s) general purpose processor.

[17:05](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1025s) And the exciting thing about that is

[17:06](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1026s) it's more efficient for 60% of workloads.

[17:10](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1030s) We estimate a reduction of 300,000 metric tons

[17:13](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1033s) of carbon in 2022,

[17:15](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1035s) purely from running Graviton-based instances,

[17:17](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1037s) rather than EC2 instances.

[17:20](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1040s) This is a big deal.

[17:21](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1041s) This is roughly equivalent to 54,000 U.S. homes

[17:24](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1044s) in carbon reduction.

[17:26](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1046s) And these carbon emissions are going to continue

[17:28](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1048s) to reduce, as more customers move to Graviton.

[17:35](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1055s) So when you add these pieces of the puzzle up,

[17:37](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1057s) we have supply side,

[17:38](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1058s) which is bringing more renewable energy

[17:41](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1061s) into our infrastructure, into our data centers.

[17:44](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1064s) You have the demand side,

[17:45](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1065s) which is how we use power in our data centers.

[17:48](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1068s) How we utilize compute load efficiently on processors,

[17:51](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1071s) on server racks.

[17:54](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1074s) And we have long suspected that we do this really well.

[17:58](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1078s) So what we did is look at,

[17:59](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1079s) well, how does the rest

[18:01](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1081s) of the cloud industry compare on this?

[18:04](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1084s) So a study by 451 Research was done recently,

[18:08](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1088s) and it found that AWS at 3.6 times more energy efficient,

[18:13](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1093s) than the median of surveyed U.S. enterprise data centers.

[18:17](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1097s) We're like, wow, 3.6 times more energy efficient?

[18:20](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1100s) That's really compelling.

[18:21](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1101s) That's exciting.

[18:23](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1103s) We translated that into carbon reduction.

[18:24](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1104s) And we looked at that.

[18:25](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1105s) And recently, we did the same study

[18:28](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1108s) and looked at Europe.

[18:30](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1110s) So we looked at enterprise data centers

[18:31](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1111s) in places like France,

[18:34](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1114s) Spain, and Germany.

[18:36](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1116s) And we found a similar pattern.

[18:38](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1118s) Except this time, it was even higher.

[18:40](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1120s) Five times more energy efficient.

[18:43](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1123s) And what that means to a customer,

[18:46](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1126s) is that when you move load from an enterprise data center,

[18:49](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1129s) to AWS Cloud, you're seeing up to

[18:51](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1131s) an 80% reduction in energy load.

[18:54](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1134s) And when you combine that will all the exciting,

[18:57](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1137s) big renewable energy stories,

[18:59](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1139s) you see a really big potential for carbon reduction.

[19:04](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1144s) Up to 95% when all these renewable projects are online,

[19:07](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1147s) combined with the efficiency of our data centers

[19:09](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1149s) and compute load.

[19:11](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1151s) And we're not done in the space.

[19:15](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1155s) And when I say we're not,

[19:16](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1156s) is because we're really focused on

[19:18](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1158s) some of the next big challenges.

[19:19](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1159s) From conversations with customers

[19:21](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1161s) and other people in the industry,

[19:23](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1163s) we know that one of the big hurdles is on Scope 3.

[19:26](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1166s) Scope 3 is the embodied carbon

[19:29](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1169s) that goes into our businesses.

[19:31](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1171s) And one of the ones that's a real big challenge for us,

[19:33](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1173s) that we're excited to be working on,

[19:35](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1175s) is reducing the carbon

[19:36](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1176s) that goes into the physical infrastructure

[19:38](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1178s) of how we build our cloud.

[19:41](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1181s) When we started looking at this problem,

[19:43](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1183s) we started looking at where are the biggest

[19:45](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1185s) concentrations of carbon

[19:47](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1187s) that we can start driving out immediately?

[19:49](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1189s) And it turns out that concrete,

[19:53](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1193s) simple plain old concrete

[19:55](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1195s) is one of those areas where we have a lot of carbon,

[19:57](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1197s) and have actionable tools in our tool chest

[19:59](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1199s) to go reduce this right now.

[20:02](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1202s) So one of the things that we started doing

[20:03](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1203s) is looking at low cure carbon

[20:05](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1205s) when we go build our data centers.

[20:07](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1207s) And when we found it, we implement this

[20:09](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1209s) into our basis of design for data centers

[20:11](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1211s) that we build,

[20:12](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1212s) we can have a 20% reduction in the carbon of that.

[20:15](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1215s) The next piece that we looked at was steel.

[20:18](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1218s) And steel is a great example

[20:19](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1219s) of how we use our size and scale to go drive out carbon.

[20:23](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1223s) Because Amazon is a large buyer of steel.

[20:26](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1226s) Not just for AWS,

[20:27](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1227s) but if you look at our fulfillment center network,

[20:29](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1229s) the racking and shelving,

[20:30](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1230s) all of the steel that goes into the Amazon business,

[20:33](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1233s) we have an opportunity to work with the vendors

[20:35](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1235s) to implement technologies and manufacturing processes

[20:39](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1239s) that drive out carbon and Scope 3

[20:40](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1240s) that goes into all of our business.

[20:44](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1244s) And I'm learning stuff all the time about this,

[20:46](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1246s) so I'm gonna give you guys a little bit

[20:47](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1247s) of a manufacturing lesson that I learned recently.

[20:49](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1249s) Thanks to some of the people on the team.

[20:51](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1251s) Steel is traditionally made through a process

[20:56](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1256s) called 'Basic oxygen furnaces'.

[20:59](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1259s) And I recently learned about this.

[21:00](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1260s) And what this means is,

[21:01](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1261s) we're burning and melting down steel, iron ore,

[21:06](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1266s) to make steel.

[21:07](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1267s) And that burning combustion process comes from

[21:09](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1269s) burning coal, or natural gas.

[21:12](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1272s) An alternative technology that vendors can use is EAF,

[21:17](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1277s) Electric Ark Furnaces.

[21:19](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1279s) And what's compelling about this, is two-fold.

[21:21](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1281s) One is, since you're running a current

[21:24](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1284s) to melt down the steel,

[21:25](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1285s) that current is generated by electricity

[21:28](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1288s) rather than the combustion of natural gas,

[21:30](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1290s) or thermal based resources like coal.

[21:32](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1292s) So what you can do is have that EAF

[21:34](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1294s) be coming from renewable energy resources.

[21:37](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1297s) The second piece is EAF,

[21:39](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1299s) since it's melting down recycled steel,

[21:42](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1302s) you can take scrap steel and other parts of this.

[21:44](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1304s) And what that means is that you have much less

[21:46](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1306s) carbon intensity through the production of ore

[21:49](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1309s) by using recycled steel components.

[21:51](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1311s) And you have the same levels of rigor

[21:54](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1314s) that you need to actually have steel

[21:55](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1315s) that will meet your building standards.

[21:57](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1317s) And that can have a really big impact

[21:59](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1319s) on your carbon reduction.

[22:01](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1321s) EAF steel can be up to five times less carbon intensive

[22:05](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1325s) than BOF produced steel.

[22:07](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1327s) And we've used this type of steel process

[22:09](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1329s) in six of our data centers,

[22:10](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1330s) and we're gonna be using it in more

[22:11](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1331s) of our data centers as we build forward.

[22:14](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1334s) Now it seems like a really prosaic deep in the weeds topic,

[22:18](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1338s) but it matters, because Scope 3 is so challenging.

[22:21](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1341s) It's built into so many parts of our businesses

[22:23](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1343s) that you have to be thinking on the margin

[22:25](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1345s) about how you can go drive out these parts of our business.

[22:28](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1348s) And we're very, are serious about that.

[22:33](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1353s) And just yesterday we announced

[22:35](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1355s) the AWS Customer Carbon Footprint Tool.

[22:38](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1358s) This is a service that shows our dedication

[22:40](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1360s) to reducing carbon across our business.

[22:42](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1362s) Customers of AWS now will be able to see

[22:45](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1365s) the carbon intensity of their workloads

[22:47](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1367s) that their running on AWS.

[22:49](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1369s) They'll also have a forward-looking view

[22:51](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1371s) that's going to show them the carbon reduction impact

[22:55](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1375s) of our renewable energy investments.

[22:57](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1377s) We're really excited about this work.

[23:00](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1380s) And to exemplify what we're doing in this case,

[23:01](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1381s) I'd like to share a short video with you guys

[23:04](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1384s) with one of the customers that works

[23:06](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1386s) on this type of technology with us,

[23:08](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1388s) and that's Patrick Flynn, who's the V.P.

[23:10](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1390s) From Global Head of Sustainability with Salesforce.

[23:13](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1393s) So let's hear from him about how they're working

[23:15](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1395s) with AWS to achieve their sustainability goals.

[23:21](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1401s) Hello, my name is Patrick Flynn,

[23:23](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1403s) Vice-President and Global Head

[23:25](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1405s) of Sustainability at Salesforce.

[23:27](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1407s) At Salesforce, we believe that business

[23:29](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1409s) is the greatest platform for change.

[23:32](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1412s) And we work to serve the interests of all stakeholders,

[23:35](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1415s) employees, customers, partners,

[23:37](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1417s) communities, and the planet.

[23:39](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1419s) In 2021, we announced that Salesforce has reached

[23:43](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1423s) net zero carbon across our full value chain,

[23:46](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1426s) and 100% renewable energy for our global operations.

[23:50](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1430s) Salesforce and AWS have been collaborating for a long time.

[23:56](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1436s) And we have shared climate values.

[23:58](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1438s) Together, we're also working to expand

[24:01](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1441s) renewable energy procurement in partnership

[24:04](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1444s) with the Clean Energy Buyer's Alliance.

[24:06](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1446s) Salesforce also joins The Climate Pledge,

[24:09](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1449s) co-founded by Amazon and Global Optimism.

[24:12](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1452s) And both Amazon and Salesforce

[24:15](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1455s) are founding members of the LEAF Coalition,

[24:17](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1457s) which aims to protect tropical forests around the world.

[24:21](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1461s) We're excited that AWS is providing us

[24:24](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1464s) with the carbon footprint associated

[24:27](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1467s) with our use of AWS Services.

[24:29](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1469s) As this data is essential to our net zero commitment.

[24:34](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1474s) We start by optimizing our use of AWS's services,

[24:38](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1478s) so that we can reduce the carbon intensity

[24:41](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1481s) of our applications.

[24:43](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1483s) AWS provides technical guidance to help Salesforce

[24:46](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1486s) architect sustainably on AWS.

[24:50](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1490s) The data that AWS provides lets us understand

[24:53](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1493s) our climate impact,

[24:55](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1495s) and develop plans to avoid, reduce,

[24:58](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1498s) or compensate for those emissions.

[25:01](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1501s) Salesforce and AWS are on a mission

[25:04](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1504s) to help our suppliers, help our customers,

[25:08](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1508s) and help our communities take climate action

[25:11](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1511s) for the future that we all share.

[25:18](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1518s) Thank you to Patrick; and thank you, Salesforce.

[25:21](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1521s) I'm really excited about that shared vision.

[25:25](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1525s) On top of energy and carbon,

[25:27](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1527s) another pressing concern that we all have

[25:29](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1529s) as global citizens is water stewardship.

[25:33](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1533s) In addition to our efforts on efficiency

[25:35](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1535s) and renewable energy,

[25:36](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1536s) we have multiple initiatives in place

[25:38](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1538s) around water stewardship and conservation

[25:40](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1540s) that I wanna share with you guys today.

[25:44](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1544s) Our water program is really built around four principals.

[25:48](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1548s) One is, what is the source of water

[25:51](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1551s) that goes into our data centers to cool?

[25:54](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1554s) The second is, how do we use that water most efficiently?

[25:58](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1558s) The third is, what do we do with the water

[26:00](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1560s) when we're done using it to cool our data centers?

[26:02](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1562s) And the fourth is,

[26:03](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1563s) how do we restore water levels

[26:06](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1566s) in the communities where we operate?

[26:08](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1568s) I wanna walk through a little bit of those four steps

[26:10](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1570s) with you quickly.

[26:12](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1572s) The first one is around sustainable sourcing of water.

[26:15](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1575s) So whether it's in Spain,

[26:17](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1577s) Chile,

[26:19](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1579s) Northern Virginia,

[26:21](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1581s) Eastern Oregon,

[26:22](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1582s) we're always looking about how we can use

[26:24](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1584s) the most sustainable sources of water.

[26:27](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1587s) And one of the ways that we can do that,

[26:28](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1588s) is through using recycled water.

[26:31](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1591s) Now that may seem like a strange thing,

[26:33](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1593s) but why that's important is because

[26:35](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1595s) we all have to drink water.

[26:37](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1597s) Drinking water is sometimes called potable water.

[26:40](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1600s) So one of our first principles is,

[26:42](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1602s) how can we use water that's non-potable

[26:44](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1604s) to cool our data centers?

[26:45](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1605s) Because arguably, the most critical use of water

[26:47](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1607s) is for the preservation of life on earth,

[26:50](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1610s) which is drinking water, right?

[26:52](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1612s) So when we go into many parts of the world,

[26:53](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1613s) we say what the non-potable water sources

[26:56](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1616s) that we can employ to cool our infrastructure?

[26:59](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1619s) And this is a lot like the South African example

[27:02](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1622s) I gave to you guys earlier about renewable projects,

[27:04](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1624s) which is often times, when you go to utilities,

[27:07](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1627s) they say,

[27:08](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1628s) "Well, I guess we have a small pilot program somewhere,

[27:10](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1630s) "but we haven't really done anything at the scale

[27:12](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1632s) "that you wanna do."

[27:14](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1634s) And we have a team of water professionals

[27:15](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1635s) and public policy folks who had a lot of success

[27:19](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1639s) going out and working with utilities

[27:21](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1641s) and local governments to go drive the acceleration

[27:24](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1644s) of recycled water integration into our data centers.

[27:28](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1648s) A great example of this is in Northern Virginia,

[27:30](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1650s) where we were the first large industrial user

[27:33](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1653s) to bring in recycled water to cool our data centers.

[27:36](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1656s) And we're not done with Northern Virginia,

[27:38](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1658s) or parts of the Bay Area, or Singapore,

[27:40](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1660s) or other parts of the world we've implemented this.

[27:42](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1662s) We're using the same principles that we brought to bear

[27:45](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1665s) with our renewable energy commercial innovation

[27:48](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1668s) towards recycled water.

[27:50](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1670s) Which is, finding paths to do this at scale.

[27:52](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1672s) Not just for AWS, for other industrial users of water

[27:56](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1676s) who wanna replicate that playbook.

[28:00](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1680s) We also make sure that the water that we do use

[28:02](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1682s) within our data centers is efficiently used as possible.

[28:06](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1686s) So we do this through evaporative cooling technology,

[28:08](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1688s) which basically means that we don't use water

[28:11](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1691s) to cool our data centers

[28:13](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1693s) when we can bring in free cold air

[28:14](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1694s) from the outside ambient environment.

[28:17](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1697s) Instead, we carefully use metrics

[28:19](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1699s) and operational best practices to calibrate

[28:22](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1702s) bulb set points.

[28:23](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1703s) And understand what the weather forecast is gonna be,

[28:25](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1705s) how we can operate our infrastructure reliably,

[28:28](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1708s) and then, when we get to set points when we need to cool,

[28:30](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1710s) we use water diligently and efficiently.

[28:33](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1713s) And the other piece that we use,

[28:34](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1714s) is we innovate and build technologies

[28:38](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1718s) for onsite water treatment.

[28:40](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1720s) Now that may seem a little bit strange too,

[28:42](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1722s) but, any of you guys who may have had

[28:44](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1724s) one of those old-school air conditioners,

[28:47](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1727s) with the tank that you had to go empty,

[28:48](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1728s) that was sitting in your living room, or basement?

[28:51](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1731s) Similar to that.

[28:51](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1731s) You can recall those air-conditioners

[28:53](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1733s) that would get the kind of funk in the water?

[28:55](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1735s) That little bit of scaling?

[28:56](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1736s) That happens when you're cycling water

[28:58](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1738s) through an evaporative cooling technology.

[29:00](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1740s) So what we've developed is modular onsite treatment.

[29:03](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1743s) So we can reduce that type of scaling

[29:04](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1744s) that happens through hard water usage,

[29:06](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1746s) to make sure that we can continue to use that water.

[29:11](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1751s) But eventually, we do have to get rid of that water

[29:13](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1753s) from our data centers.

[29:14](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1754s) So what are the ways we do this?

[29:16](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1756s) One of the things that we like to do

[29:17](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1757s) is go look at what is the water

[29:19](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1759s) that comes out of our data centers?

[29:21](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1761s) In many cases,

[29:21](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1761s) because of the onsite water treatment that we use,

[29:24](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1764s) and how we efficiently use that water,

[29:26](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1766s) that water is often times cleaner

[29:28](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1768s) than when it came into our data centers.

[29:30](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1770s) And this has created some really unique opportunities

[29:33](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1773s) that we didn't really think about

[29:34](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1774s) until we got closely integrated with our communities.

[29:37](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1777s) A great example of this is, Eastern Oregon,

[29:40](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1780s) and our Western Region, where we have what we call PDX.

[29:44](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1784s) What we do there is,

[29:45](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1785s) take the water that we've used in our data centers

[29:48](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1788s) and a strange function of irrigation

[29:52](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1792s) and the use of chemicals to go treat crops

[29:58](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1798s) in parts of this world,

[29:59](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1799s) is that the water table sometimes has

[30:00](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1800s) high nitrate levels in it.

[30:02](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1802s) But the water when we go treat it in our data centers,

[30:04](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1804s) is actually cleaner than often times

[30:06](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1806s) what the water table is.

[30:07](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1807s) So what we've done is go work with utility,

[30:09](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1809s) and go discharge that water

[30:11](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1811s) directly into irrigation channels,

[30:13](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1813s) where it can be used right for agricultural purposes.

[30:17](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1817s) The water company doesn't have to treat it,

[30:19](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1819s) farmers and the local community

[30:20](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1820s) can use this right off the bat.

[30:21](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1821s) And it's a win-win for us, too.

[30:23](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1823s) Because we do not have to go build

[30:24](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1824s) the discharge infrastructure that we might have

[30:27](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1827s) to put this water back to a waste water treatment plant.

[30:32](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1832s) And finally, we look about how we can restore water

[30:34](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1834s) within the communities where we operate.

[30:37](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1837s) This is an example of a watershed restoration project

[30:40](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1840s) in South Africa,

[30:41](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1841s) where we partnered up with local groups.

[30:44](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1844s) In this case, the Nature Conservancy in Cape Town

[30:47](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1847s) to go reduce evasive species

[30:50](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1850s) that are water hogs, while on the water table.

[30:53](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1853s) We're also doing water restoration projects

[30:56](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1856s) in parts of the world like India, and Indonesia.

[31:00](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1860s) Through partnerships with water.org

[31:02](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1862s) What we do here is connect water.org with micro projects

[31:06](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1866s) where we've done over,

[31:08](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1868s) connected AWS projects to over 160,000 people

[31:13](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1873s) to clean up public water systems.

[31:16](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1876s) In India, with wateraid.org

[31:18](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1878s) we've done over 5,000 projects for water filtration,

[31:21](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1881s) rain water capture,

[31:22](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1882s) and ground water recharge projects.

[31:25](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1885s) Projects we've done to date to restore water

[31:29](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1889s) will bring over 250 million gallons of water

[31:31](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1891s) per year to the communities where we operate.

[31:36](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1896s) Speaking of the communities where we operate,

[31:38](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1898s) it's not just about energy efficiency and water,

[31:41](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1901s) it's also about what is our social impact.

[31:44](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1904s) What is our equity impact

[31:46](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1906s) in the communities where we operate?

[31:48](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1908s) To make a positive impact in the communities

[31:50](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1910s) where we have physical infrastructure,

[31:52](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1912s) where the cloud lives in the real world,

[31:54](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1914s) we formed a team called AWS InCommunities.

[31:58](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1918s) And InCommunities is one of the things

[31:59](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1919s) that I've been most excited about in the last couple years.

[32:02](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1922s) We all know that being engaged with your work,

[32:05](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1925s) having a sense of higher purposes

[32:07](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1927s) is a really, really important part for employee engagement.

[32:10](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1930s) So AWS InCommunities has tapped into that desire

[32:14](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1934s) for something bigger, for that sense of meaning,

[32:17](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1937s) in a couple of different ways.

[32:19](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1939s) AWS InCommunities is built around four pillars.

[32:22](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1942s) The first one is STEAM Education, Access, and Equity.

[32:26](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1946s) We all know what STEM means:

[32:28](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1948s) science, technology, engineering and mathematics.

[32:31](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1951s) The A is is not for the end, though.

[32:33](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1953s) It's for arts.

[32:34](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1954s) Because we truly believe that creative thinking

[32:37](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1957s) comes through a focus on the arts.

[32:38](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1958s) So AWS InCommunities focuses of STEAM.

[32:42](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1962s) Science, technology, engineering, arts and mathematics.

[32:47](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1967s) We also believe that we need to think big

[32:50](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1970s) about the cloud, careers and technology.

[32:53](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1973s) And what that's going to mean for the future.

[32:56](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1976s) So, we've developed this pipeline mechanism pillar,

[32:58](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1978s) which is local tech upskilling.

[33:01](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1981s) Which is to work in the communities

[33:03](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1983s) to find ways to bring the next generation

[33:05](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1985s) of technologists to learn about opportunities in the space,

[33:08](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1988s) develop those tool sets,

[33:09](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1989s) and to think unbounded around

[33:11](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1991s) what careers mean in technology.

[33:14](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1994s) InCommunities focuses on environmental stewardship

[33:16](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1996s) on a micro level in the communities where we operate.

[33:19](https://www.youtube.com/watch?v=Dmz45WhXENs&t=1999s) Those big off-shore wind projects

[33:20](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2000s) can also translate into an environmental projects

[33:23](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2003s) in the communities where we operate.

[33:26](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2006s) And finally, InCommunities focuses on

[33:28](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2008s) AWS employee engagement.

[33:30](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2010s) How do people who work for AWS get involved

[33:32](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2012s) in the communities that they work in?

[33:35](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2015s) I wanna share four of our global signature programs.

[33:39](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2019s) The first is AWS Tech Week,

[33:41](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2021s) where we get involved in local schools

[33:43](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2023s) in communities to go share careers in technology.

[33:47](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2027s) Talk about machine learning, IoT,

[33:50](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2030s) things that may be strange

[33:51](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2031s) to some of the communities where we operate.

[33:53](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2033s) Or may not even be a possibility to many children.

[33:56](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2036s) I can tell you guys personally

[33:57](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2037s) that this has probably been one of the most exciting things

[33:59](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2039s) that I've been involved in with my time at Amazon.

[34:02](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2042s) And it was one of those things where like you're,

[34:03](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2043s) "How can I find the time to go make myself do this?"

[34:06](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2046s) But I found myself sitting in front of a sixth grade class

[34:09](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2049s) in rural Minnesota, in a town with 2,000 people.

[34:13](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2053s) And it was eerily similar to the community

[34:15](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2055s) where I grew up in rural South Dakota.

[34:17](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2057s) This is a sixth grade class with about 30 people in it.

[34:20](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2060s) And these types of communities

[34:21](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2061s) are a lot like the ones that I grew up in.

[34:23](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2063s) Small, rural, where the jobs

[34:26](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2066s) that are in front of many of the people

[34:27](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2067s) who live in this community

[34:28](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2068s) are truck driver,

[34:30](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2070s) nurse,

[34:31](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2071s) teacher,

[34:32](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2072s) construction worker.

[34:34](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2074s) All great professions,

[34:37](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2077s) but these kids have never even heard of the idea

[34:38](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2078s) of what is a developer?

[34:40](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2080s) What is machine learning?

[34:42](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2082s) And it was just such an empowering opportunity

[34:44](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2084s) to go talk to these kids and say,

[34:46](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2086s) "Well, you know what else is out there?

[34:47](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2087s) "All of this stuff."

[34:48](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2088s) And to see the imagination and gears spinning

[34:51](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2091s) in these kid's minds.

[34:52](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2092s) And we talked about this type of program,

[34:54](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2094s) across the world through this tech week,

[34:56](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2096s) is truly, truly fulfilling.

[34:59](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2099s) We also get engaged with under-represented communities

[35:01](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2101s) through things like Girls' Tech Day.

[35:03](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2103s) Where we focus on STEAM-based education and curriculum

[35:07](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2107s) for girls and young women.

[35:10](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2110s) We also recognize that it takes a full community

[35:12](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2112s) to make these types of programs successful.

[35:14](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2114s) So the third signature program is Family Tech Day.

[35:17](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2117s) Where we get the entire learning environment

[35:19](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2119s) working together to go work on these types of programs.

[35:23](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2123s) And finally, we have Think Big Spaces.

[35:25](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2125s) Which in essence, un-tap the creativity

[35:27](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2127s) of these young minds and families, and communities,

[35:29](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2129s) to go, to work on Think Big projects

[35:31](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2131s) about leveraging the AWS Cloud, IoT,

[35:34](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2134s) Edge, or ML,

[35:36](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2136s) and let people's imaginations run unbounded.

[35:40](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2140s) This is an example of Girls In Tech in Virginia.

[35:43](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2143s) And one of our Think Big spaces in India.

[35:45](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2145s) The InCommunities team has just done an incredible job

[35:48](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2148s) in the short order of time

[35:49](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2149s) building a program around the globe

[35:51](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2151s) that impacts the communities where we operate.

[35:56](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2156s) From Ireland to Virginia,

[35:58](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2158s) to Cape Town,

[36:00](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2160s) to parts of Europe, Middle East and Africa,

[36:02](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2162s) InCommunities is doing programs around the world.

[36:05](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2165s) We have a Stepping Stones program in Ireland,

[36:07](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2167s) where we're focusing on diversity impacts,

[36:11](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2171s) putting things down from new beehives

[36:14](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2174s) to increase pollination rates.

[36:15](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2175s) To doing Soil for Life projects in Cape Town.

[36:21](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2181s) And finally we recognize that the problems

[36:22](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2182s) that I have been talking about today and opportunities,

[36:25](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2185s) sustainability, climate change,

[36:28](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2188s) renewable energy,

[36:29](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2189s) carbon reduction,

[36:31](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2191s) those truly are bigger than any one company.

[36:34](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2194s) Than any one individual,

[36:36](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2196s) than any one government.

[36:38](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2198s) It's gonna require a forward-looking mindset.

[36:41](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2201s) And as a result,

[36:42](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2202s) InCommunities is focusing on a greener future.

[36:45](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2205s) So it won't just be people like myself

[36:47](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2207s) and people like you working on these challenges,

[36:49](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2209s) but having the next generation pick up the mantle

[36:51](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2211s) for how we're gonna work on these type of problems.

[36:54](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2214s) And to that, I'm excited to announce

[36:55](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2215s) that we're doing the AWS Greener Future Competition in 2022.

[36:59](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2219s) Which is a global sustainability competition

[37:01](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2221s) that InCommunities is working on

[37:03](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2223s) to go develop technologies and solutions

[37:06](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2226s) that come from the next generation of thinkers,

[37:08](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2228s) the school and communities we work on

[37:10](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2230s) for sustainability ideas.

[37:14](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2234s) I wanna say thank you so much for coming

[37:16](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2236s) to this conversation this afternoon.

[37:18](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2238s) There's so much stuff happening across Amazon and AWS

[37:22](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2242s) within sustainability.

[37:23](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2243s) These are some other sessions,

[37:24](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2244s) that if you're interested in learning more about this,

[37:26](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2246s) or wanna check into a recorded session,

[37:28](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2248s) you're certainly welcomed to do so.

[37:31](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2251s) I'd also like to say thank you so much.

[37:33](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2253s) You guys have really just made this

[37:35](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2255s) an enjoyable experience for myself,

[37:37](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2257s) first time back on the stage.

[37:38](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2258s) And I wanna say thank you guys so much for coming

[37:40](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2260s) and listening today.

[37:42](https://www.youtube.com/watch?v=Dmz45WhXENs&t=2262s) (audience applauding)

