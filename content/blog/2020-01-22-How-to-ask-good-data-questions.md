---
title: "How to Ask Good Data Questions"
date: 2020-01-22
tags: [workflow]
categories: [workflow]
summary: "A collection of responses from Caitlin Hudon's twitter thread on 'how to ask a good data question.' (Updated 2020-03-15)"
---
Have you ever spent weeks of your life building a great data product, only to find that you solved the wrong problem? Or you built a cadillac, when all they needed was a bike? 

Enter a secret from project management - you gotta nail the requirements, or the 'problem to be solved'. The analyst needs to ask the right questions to elicit the true requirements from the stakeholder, who often doesn't understand your domain or might be [obscuring the true nature of their problem](https://en.wikipedia.org/wiki/XY_problem).

[Caitlin Hudon](http://caitlinhudon.com/) is an awesome person and crowdsourced some responses in her [twitter thread on this topic](https://twitter.com/beeonaposy/status/1214973414345195520):

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Writing an internal &quot;how to ask a good data question&quot; guide for both technical and non-technical stakeholders. <br><br>What would yours include?</p>&mdash; Caitlin Hudon 👩🏼‍💻 (@beeonaposy) <a href="https://twitter.com/beeonaposy/status/1214973414345195520?ref_src=twsrc%5Etfw">January 8, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## Where a new analyst should begin

Here's a great framework from Laura Ellis (@LittleMissData) to start with:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">I wrote something along this lines showing ppl how to break down a business problem into a tangible data problem if it helps! I teach ppl this way at work. <a href="https://t.co/sOZZmXKzi6">https://t.co/sOZZmXKzi6</a></p>&mdash; Laura Ellis (@LittleMissData) <a href="https://twitter.com/LittleMissData/status/1215078949824475137?ref_src=twsrc%5Etfw">January 9, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## Mini checklist

Here are a few one-liners that I loved that you can use as a checklist at the start of a data project. I wish I asked these at the start of a few projects where I missed the mark.

1. If you had the answer, what action would you take?
    * or: If you get a perfect 100% confidence answer back, what would you do with that information?
    * Who will take action using this data? What will they do?
2. Who else may find this useful?
3. What are you doing today? What are you trying to do that you can't today?
4. Can you make a decision with imperfect data?
    * If I can give you an 80% confidence answer in a day, vs a 95% confidence answer in two weeks, which would you prefer?
5. How do you want to receive the results?

## Other responses that are worth some additional reading

Jeremy Howard's [Project Checklist](https://www.fast.ai/2020/01/07/data-questionnaire/) blog post. Pretty big questionnaire that he used over decades of consulting work. Key takeaway here is that you need to head off problems like initial constraints and resource limitations and to understand how this is going to benefit the company.

Do you have metrics about your data? Introducing [Data Meta-Metrics](https://caitlinhudon.com/2017/11/14/data-meta-metrics/). 

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">1000% agreed. I&#39;ve done some projects like this where the data wasn&#39;t great, and relied on data meta-metrics to help communicate availability and quality back up to stakeholders. (Like this: <a href="https://t.co/GVND4QFbXz">https://t.co/GVND4QFbXz</a>)</p>&mdash; Caitlin Hudon 👩🏼‍💻 (@beeonaposy) <a href="https://twitter.com/beeonaposy/status/1215003789876514816?ref_src=twsrc%5Etfw">January 8, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Caitlin added scores for Relevance, Trustworthiness, and Reliability to describe the quality of the data or the analysis. I liked how she defined the scales - once you see it it's hard to imagine seeing data without meta-metrics.

Someone recommended a book called ["Optimizing Data-to-Learning-to-Action"](https://www.amazon.com/dp/1484235304/ref=cm_sw_r_cp_api_i_IqJfEbMJ7R24D): Looks like a promising book that advocates for the use of data to drive decisions/actions. Aspirational to be sure, but reading through the preview pages is a waste of time as it's all advocacy and no clear suggestions yet. Likely to just be another consulting framework that is too vague to be useful. But yeah, you should work backward from the decisions to data, estimate the flow of value along the chain, and identify potential issues. I love [OODA](https://en.wikipedia.org/wiki/OODA_loop) and agree that you should build things that help you make decisions, looking for more books that have case studies.

Julia Evans wrote a blog post covering this exact issue in her [How to ask good questions blog post](https://jvns.ca/blog/good-questions/). This seems to be more geared towards asking for help or advice rather than scoping a data project, but I'm including it here because it's good general advice.