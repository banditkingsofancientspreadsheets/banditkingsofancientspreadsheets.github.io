---
title: "What I'm Pondering: Screen Graphics and Why My Dashboards Suck"
date: 2019-12-28
tags: [dataviz, UX]
excerpt: "Today I learned that there are design studios who specialize in 'Screen Graphics' - the cool visual effects that shows up on computer screens in movies like The Martian and Blade Runner 2049. And then I wonder why our corporate finance dashboards seem to miss the mark."
---

# "Screen Graphics" and Future Data Interfaces

Today I learned that there are design studios who specialize in 'Screen Graphics' - visual effects that show up on computer screens in movies.

I learned this from listening to [Data Stories ep 151: Future Data Interfaces with David Sheldon-Hicks](https://datastori.es/151-future-data-interfaces-with-david-sheldon-hicks/). They talk about Territory Studios, the creative studio behind the screen graphics in movies like Blade Runner 2049 and The Martian. I liked the piece about how they had to interview people from NASA and the military on how the data is used and the context around their usage. For NASA, their primary concern is the validity of the data, they don't need fancy visualizations, just data that they can trust. This jives with my own experience in space launch, where the UI was pretty nonexistent except for a few dozen real-time numbers on a screen. They talked about drawing from research (which in turn draws from film) and joke about how everything in the future had blue screens.

I love these futuristic data interfaces. They're entirely aspirational (like concept cars) but they provide valuable examples of UI/UX design. And I think every analyst (or executive sponsor of a data project) secretly wishes they could be manipulating data like this, and new tools like PowerBI and Tableau are making dashboard creation more accessible than ever.

## Dashboards: Too Little and Too Much Information

PowerBI and Tableau are great tools. They empower your average business user to build their own custom dashboards, and they can scale so that your power users can build 'standard' reports to be used across the organization or function. The value prop for your corporate finance team is clear: less reliance on excel and powerpoint reporting, more time for more value-added analysis. But the reality is that you get a proliferation of bespoke dashboards that are hyperspecific to a single analyst or standardized corporate dashboards designed for everyone and no one. It's how dashboards can have both too little and too much information at the same time.

If it's true that dashboards often have too much and too little information, why don't we take inspiration from real world 'dashboards'? You know, the dashboard in your car? The gauges and indicators that you have are particularly suited for the exact task that you're doing at the time. One downside with standardized corporate dashboards are that they aren't tailored with a specific user or context in mind, and end up with crowded dashboards with dozens of filters and buttons to click through. There are great books and resources for basic visualization principles that go into making the design aesthetically pleasing and information rich, but the often unanswered question is: what is the point of having the dashboard in the first place? Does the BI developer know the problem that the end user is trying to solve? Do they understand the business problem?

This is a recipe for disillusioned BI developers and frustrated end users. Developers feel that they don't have any impact because nobody uses their product, and end users get frustrated because they asked for information but instead got a pretty dashboard that doesn't help them solve their problem. The podcast touches on this briefly when the designer talks about the importance of getting the initial brief right. A dashboard should help the user accomplish a specific task or solve a specific problem, and present the most relevant information for the user. Going back to the analogy of driving a car: imagine if your car dashboard showed you your speed in yards per second (the wrong information) instead of mph or km/h, or if your dashboard showed a data table with 40 rows and 1000 columns of telemetry (too much information).

## Good Dashboards Should Solve a Specific Problem in a Specific Context

How do you help provide more business context and design better dashboards? Developers must have an understanding of the KPIs and the context in which those measures are important. Are they leading or lagging indicators? Who is the audience, and what decisions will be made from this data? To answer these questions, start with your organizational structure.

In my company's corporate finance team, our dashboard developers are mostly finance analysts who upskilled into Business Intelligence (BI) work. Almost all of them sit in a center of excellence (COE), which is about as far away as you can get from an end user. The clear benefit of having a COE is that data professionals can learn and grow alongside each other, and they can work on cross-functional and cross-org issues. This also has has clear advantages when working under a tight budget or when talent is scarce. The downside of a COE model is that you create a brain drain in the lines of business, and you can create the perception of preferential treatment...which inevitably leads to resentment from organizations outside of the COE. To combat this, organizations like AirBnB adopted a 'hybrid' or matrixed approach, where their data professionals are dotted line to the product teams but also report to a functional manager. Another alternative is to have 'Product Owner' or 'Analytics Managers' to act as the voice of the users and serve as a bridge between the data professionals and business units.

## Further Research

[UX Collective](https://uxdesign.cc): UX Design related blog posts on Medium

[Storytelling with Data](https://www.amazon.com/Storytelling-Data-Visualization-Business-Professionals/dp/1119002257): Great book on visualization design that covers the basic do's and don'ts, very comprehensive and approachable (all of its' graphics were created in Excel)

[Territory Studios](https://territorystudio.com): Inspiration from screen graphics from major films

[Data Stories](https://datastori.es): Podcast on data visualization, Episode 151 inspired this writing
