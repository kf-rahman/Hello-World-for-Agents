---
id: 00-02
title: Watch the Loop
xp: 100
skippable: true
demo: false
---

## Briefing
Tell the player there's a small project in `playground/`: the Tavern Ledger,
an inventory tool for a fantasy tavern. They'll use it for the rest of the course.

Their first job is to give the agent a real task and watch how it works. Ask
them to type a request in their own words, something like:

> "Look at the playground folder and tell me what this project does and how to run it."

**GM instructions:** when they send it, handle it as a normal task, but
**narrate your loop** as you go. Before each tool call, say in one line what
you're about to do and why (for example: "Reading `tavern.py` to see what
commands exist"). At the end, sum up how many steps you took.

## Tasks
1. Player asks the agent to explain the playground project.
2. Player answers the GM's follow-up question: *"How many separate actions did I
   take, and which one surprised you?"*

## Win condition
The player has seen at least two tool calls (for example a file read and a
command run) and answered the follow-up question in their own words.

## Hints
1. You don't need special syntax. Just ask in plain English.
2. Try: "What does the code in playground/ do? Run it to show me."

## Debrief
You just watched the **agent loop**: read → decide → act → observe → repeat.
A chatbot would have guessed from your description. The agent went and
*looked*. This is why agents are more useful, and also why you need to watch
what they do.
