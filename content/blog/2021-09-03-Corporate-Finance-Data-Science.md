---
title: "How Data Science Can Be Applied to Corporate Finance"
date: 2021-09-03
tags: [applied data science]
categories: [projects]
summary: "In which I meander through the work of finance data scientists and how data science can be applied to corporate finance."
---

There's been plenty of hype around data science over the last decade, and [plenty](https://www2.deloitte.com/ca/en/pages/finance-transformation/articles/finance-2020.html) of consultancies have proclaimed that future of finance will involve data science somehow. But in teaching new analysts about these techniques, it's clear to me that the finance community in general is *interested* in data science but at a loss as to *how* to do it and *what* a solution would look like. 

I get asked this all the time because I'm working on applying these skills to support the finance function and working to upskill analysts. So here I will attempt to meander my way around the question of "what does data science in corporate finance look like?" 

## Financial Analysts Are Data Analysts

Financial analysts have long been the keepers of financial data, responsible for reporting on the business results and analyzing it to understand the impacts of business decisions. Compared to other parts of the business, financial data is 'clean' thanks to strict regulatory requirements, auditors, and the profession of accounting which exists to correctly count things ([which is super hard, as Vicki Boykis skillfully articulates](https://vicki.substack.com/p/all-numbers-are-made-up-some-are)). 

What surprises me is that most finance analysts don't realize they're data analysts...[their data happens to be structured financial data](https://youtu.be/GbL-42kv5LI?t=151). They already go to extreme lengths to engineer reports, codify complex business logic, and warehouse data using their tool of choice (spreadsheets). In other words, [these folks are building and running business-critical software with in Excel](https://multithreaded.stitchfix.com/blog/2017/07/06/why-internal-software/).

### What's In It For Finance?

Excel offers tremendous flexibility for financial analysts and it's wicked fast for ad-hoc analysis. And despite its [known shortcomings](https://floatapp.com/blog/5-greatest-spreadsheet-errors-of-all-time/), finance will never stop using it. 

And that's where people get stuck - the status quo sucks but learning DS is tough, too. I get plenty of analysts and managers who tell me they're interested in data science/analytics/AI/ML - largely thanks to years of marketing hype and concern for their careers - but struggle with the motivation to become students again. What they're really asking is: *if I learn data science, what's in it for me?* 

[Here's a great analogy from 'Causal Inference for the Brave and True':](https://matheusfacure.github.io/python-causality-handbook/01-Introduction-To-Causality.html)

> To use a Jim Collins analogy, think about pouring yourself an ice cold cup of your favorite beer. If you do this the right way, most of the cup will be beer but there will be a 1 finger thick layer of foam at the top. This cup is just like Data Science.
>
> * It’s the beer. The statistical foundations, the scientific curiosity, the passion for difficult problems. All of this was proven very valuable throughout hundreds of years.
> * It’s the foam. The fluffy stuff built on unrealistic expectations that will eventually go away.
>
> This foam might come down crashing faster than you think. 

So to sell the idea of DS in finance and to secretly get them to learn math, stats, and programming to be useful, I think it helps to offer some examples of where these techniques have been applied within corporate finance to automate work and improve planning.

## Automating Repetitive Work

Automating work for finance analysts means less manual effort for routine analysis, like comparing actual business metrics against forecasts and presenting results in a pretty chart for stakeholders, or applying business rules to predict future performance. I assure you, across every company in the Fortune 500 there are teams of analysts that are manually do all of this by passing around Excel files back and forth and it takes more time than you would think.

[Microsoft's finance department](https://www.microsoft.com/cms/api/am/binary/RE2IIQU) offers an example of a large-scale automated prediction that incorporated thousands of features to automate their revenue forecasts. While this [might be pure marketing for their products and their vision of Modern Finance](https://www.microsoft.com/en-us/modernfinance/), there's plenty of quick wins to be had in automation. For many analysts, even [simpler methods](https://otexts.com/fpp2/expsmooth.html) can be applied with a few lines of code to generate more accurate and automated forecasts based on historical trends. And there's plenty of work that can be automated with python scripts - no machine learning required.

## Improving Planning

While process automation is great, a more accurate prediction isn't enough for the business. Business folks have a deterministic view of the world: if I sell more widgets, revenue goes up, and if I lay off headcount, my personnel costs go down, right? People don't just want to know *what* the number is going to be, they want to know *why* and *how* things could happen.

And when it comes to planning, executives often have a number in their head and the analyst's job is to model the scenario that magically results in that number. Traditional Excel-based financial modeling is more than capable of obliging this view as long as people can convince themselves that point estimates are the way to go. 

Instead, Data Science (and even basic applied stats) can augment our decision making with new types of models on data sets that would be too large or troublesome for Excel. And thanks to advancements in computing and research, people are rediscovering new superpowers in decision support like Bayesian methods and Causal Inference [(i.e. Stitch Fix)](https://multithreaded.stitchfix.com/blog/2019/12/19/good-marketing-decisions/). But this path is *much* harder and it requires deep business acumen along with the technical skills (and soft skills!) to deliver on a solution. This is where a 'Finance Data Scientist' could come in.

Taken to the extreme, I look at [Uber's data scientists who are attached to finance teams]((https://eng.uber.com/financial-planning-for-data-scientist/)) for inspiration into what an integrated scenario planning platform can offer. [Their planning platform allows for the integration of their data scientists' work with financial analysts]((https://eng.uber.com/transforming-financial-forecasting-machine-learning/)) - a revolutionary way to do financial planning, but one that can't magically transform an unprofitable business.

## A Plan for Solo Finance Data Scientists

So let's say you're a brand new Finance Data Scientist, the first of your kind. Congrats! How do you get started?

Here's the approach that I'm taking: We need to examine the business, create a prioritized project pipeline to tackle it, and get free help.

### Model the Business

**First** - we want to build out a model of the business, sort of a 'beta' version of our integrated [directed graph](https://en.wikipedia.org/wiki/Directed_graph) in the Uber vein. By modeling the business this way, you get a shared vision of the end product with the business and leverage the collective intelligence of the analysts closest to these problems. Chances are, they've already built out some of the connections in excel already and have stakeholder buy-in. The analysts get the benefit of recognition for their work and in helping create the solution, and the business gets a better model. Where there are gaps, you can target them with additional exploratory project work to build those models.

Once those gaps are filled, you can look to improve existing models and driving accuracy or increased information. Furthermore, by creating the map of the business, you can then start calculating the benefit of filling in the gaps by tying it to cost savings, capital improvements, or even just convenience by making the data more readily available.

For a great worked example, see [The Analytics Edge](https://ocw.mit.edu/courses/sloan-school-of-management/15-071-the-analytics-edge-spring-2017/) on MIT's open courseware site. [The series on Linear Regression](https://ocw.mit.edu/courses/sloan-school-of-management/15-071-the-analytics-edge-spring-2017/linear-regression/) is the perfect introduction to teach analysts how to recognize an opportunity and break a business problem down into parts using the story from [Moneyball](https://www.amazon.com/Moneyball-Art-Winning-Unfair-Game/dp/0393324818) as inspiration.

### Map Out Needs

**Second** - after modeling the business and identifying the existing gaps in the model, map out the available data and how you might solve the business problem. Do you have enough data to solve the problem? Do you have the knowhow and talent to model it correctly and know what 'done' looks like? How difficult is the problem to solve - can an analyst do it or do you need a different skillset? Then, we need a method to capture ROI or 'importance to management' so you can rack and stack. An example here could be a combination of 'technical feasibility' and 'perceived impact' that people could vote on or score.

### Enlist Help By Upskilling Analysts

**Finally** - how are we going to do all of this work? We'll need to enlist the help of analysts in finance. There are already a number of people with the acumen and interest to learn python, and from there they can learn additional methods in analysis. In exchange for upskilling them and breaking down problems into bite-sized projects, they get mentorship and a cool thing on their resume.

## Will There Be More Finance Data Scientists?

Finance has a few great things going for it:

* A workforce with business acumen and a tradition of critical thinking
* 'Clean' structured historical data with an entire profession devoted to ensuring accuracy
* A seat at the table when it comes to making business decisions

I'm incredibly fortunate to have a role where I can experiment with applied data science in finance. At my company, Finance is close to the results and is responsible for measuring the impacts of decisions on business performance, and is a key player in strategy and planning. With a healthy set of clean, structured financial data and squads of highly-trained analysts, there's no better seat to help the business make the best possible decisions in the face of uncertainty. It's obvious that there are plenty of opportunities, and organizations are (as of 2021) still early in creating room for these specialties to grow. 

Of course, success is not assured. I've left out a lot of details and completely ignored the need for executive sponsorship, infrastructure resourcing, the right org structure, soft skills, and so on. It's still early days in this discipline, but I'm confident that I won't be the last Finance Data Scientist at my company. More to follow as I learn more!