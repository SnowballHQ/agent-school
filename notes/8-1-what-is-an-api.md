---
slug: what-is-an-api
cluster: 8
cluster_title: "APIs, data pipelines and system integration"
order: 1
title: "What is an API, really?"
teaser: "Every useful AI system spends most of its life asking other programs questions. The rules for asking are older and simpler than you think."
access: free
minutes: 10
mission: "Warm-up"
---

An API is a way for one program to ask another program for something, in a
form both sides agreed on beforehand. The letters stand for application
programming interface, which is a mouthful for a plain idea: a published
list of what you may ask, how to phrase it, and what you'll get back.

A few words come with it. The question you send is a request. The answer
is a response. The place you send the request is an endpoint, which is
just a web address that answers questions instead of showing you a page.
The answer usually comes back as JSON, a plain-text format for organised
data that looks like `{"title": "Data Analyst", "remote": true}`: labels
on the left, values on the right. And every response carries a status
code, a number that says how it went. 200 means fine. 404 means that
thing doesn't exist. 429 means you're asking too fast and should slow
down.

Here's the analogy. Think of a restaurant with a menu and a kitchen
window. The menu is the documentation. You can order what's on it, in the
way the restaurant takes orders, and what comes out looks like the
picture. You never see the kitchen and you never need to. The restaurant
can change its cooks, its stove, its suppliers, and as long as the dish
matches the menu, you're none the wiser. Order something that isn't on the
menu and you get a polite no, which is a lot better than a surprise.

The word to remember is contract. An API is a promise, written down, that
the answer will have a certain shape. Nothing magic happens. Your program
trusts the promise, and the other program keeps it.

## This happened to us

This is how our own job board stays fresh. Every night, a crawler (a
program that visits many sites in a row and collects what it finds) asks
about 3,000 company job boards the same question: which jobs do you have
open right now?

Nobody at most of those companies knows we exist. We haven't phoned them,
we haven't signed anything, and none of them will be awake at the hour we
ask. It works anyway, because the boards publish their answers in a
predictable shape, and we ask only for what the menu offers. The crawler
reads the fields it expects, such as the title and the location, and files
them into our database.

That predictability is the entire asset. One program can ask 3,000
questions a night because the answers all arrive in a form it can read
without a human squinting at each one. Take the contract away and the same
job takes people, not a program.

It also tells you where to look when something goes wrong. A crawler that
runs perfectly can still hand you bad data if one of those boards keeps
its promise about the shape and breaks it about the meaning. The next note
is about exactly that.

## See it yourself (2 minutes)

You can play both sides of an API in any AI chat. Paste this:

> Pretend you are the API for a small library. Reply ONLY in JSON and
> always include a status code. The menu is: search books by title, get
> one book by id. Nothing else. I'll send requests now. First: search for
> "garden". Then: get book 7. Then: delete book 7. Then: tell me a joke.

Watch the last two. A well-behaved API answers a request that's off the
menu with a clear refusal and a status code, rather than improvising. If
your pretend library tells you a joke, you've found out what a program
without a contract does: it answers anyway, and you can't predict the
shape.

Now send one more request that is on the menu, but spelled badly: `get
book seven`. See whether the library accepts it. Real APIs are strict
about this, and the strictness is a feature.

## What this means when you build

In the warm-up mission you'll build an agent that watches our live job
board and tells you when something relevant appears. The tool it uses to
read the board is an API call: your agent sends a request, gets JSON back,
and reasons about what it finds. A model is also reached through an API,
so every time your agent "thinks", that's a request and a response too.

Before you wire anything up, do what professionals do and read the menu.
Find the endpoint, the fields it promises, and the status codes it can
return. Then write down one thing the menu does not promise, because that
gap is where your first surprise will come from.
