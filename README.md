# Take Home Exercise: Software Engineering, Data

## 🎯 Goal

This take home exercise is meant as an opportunity for you to showcase your software engineering
skills. We think about software engineering in its broadest sense - ie not just design and 
code but also all the best practices around the software.


## 🔥 Problem

Pave offers to its clients a minimal HTTP API endpoint developed to normalize merchant names
from credit card transactions. For example, a client can send a transaction to the API,
and the API runs a heuristic, ie a set of rules, to link that transaction to a given
merchant. When the heuristic matches a merchant, the API returns the merchant name. You 
will find a mock  implementation of that application and heuristic in the `app.py` file in this folder.

The problem is the following: the Pave heuristic is good, but takes a lot of time to run.
For example, it may take up to 30s to produce a match. For this reason, it becomes
impractical for our clients to hit the Pave API synchronously - ie sending the request
and waiting for it to complete to get the response. For example, timeout errors can happen
on both client and server sides.


## 💪 Exercise

Assuming the match heuristic cannot be further optimized, we would like to change the way
our clients interact with the Pave API. Instead of them interacting synchronously with the API,
we would like them to be able to use it ***asynchronously***.

The goal of the exercise is to build a system that enables Pave's clients to asynchronously
consume the merchant normalization function provided by the API. It could involve, for example,
but not limited to, technologies like queues, caches, or webhooks.


## 🧭 Constraints

Language: Pave's production code base is 100% Python, so we would love to see you working with Python.

Runnable: we would really like to be able to run your solution - please make it easy!
Tools that can help here include Docker and/or Docker Compose.


## ❌ What is out of scope

We value your time, so we don't expect you to spend time on:
* CI/CD: this is a critical component of the software engineering process, but it can be
very heavy to setup, so we don't expect anything on this front.
* The heuristic itself: the exercise is not about optimizing or developing the heuristic.
We provide a mock heuristic, which is intentionally slow.

## ▶️ How to run

We provide a starter API endpoint leveraging Python, Docker and FastAPI. Please use this
as a starting point - but feel free to go and modify the code and the API to accomodate
your solution.

The steps below show how to build and run the minimal API:

### Step 1: build image

```bash
docker build -t pave-api .
```

### Step 2: run

```bash
docker run --rm -p 9898:9898 pave-api
```

### Step 3: test

```bash
curl localhost:9898/normalize_merchant \
  --request POST \
  --data-raw '{"date": "2021-04-01", "description": "Payment Netflix APRIL***", "amount": 12.99}'
```