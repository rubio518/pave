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

## Solution

The proposed solution for this problem is to utilize the advantages of webhooks, since webhooks are automatic messages sent by some app when something happens, this is a case where the utilization of webhooks is advised.

For the utilization of webhooks we need the clients to provide us with a url they have set up for receiving requests from pave. We also need the clients to send the client_id which we will use to get the appropriate webhook for each client.

To accomplish this i have used the BackgroundTasks module from FastAPI, this module allows us to respond to the request almost instantly while executing the heuristic in the background, the endpoint responds with a request_id which can be used by the client to track the response in their webhook. 

the webhooks are stored in `postgres` as a persistent storage, but also cached in `redis` to improve performance.

this is a rough diagram showing how the solution is arranged
![diagram](https://s3.amazonaws.com/rubiomejia.com/pave/pave.png)


To add a new client or modify the existing webhook I have created the endpoint 

```
POST /create_webhook
{
	"url":"http://example.com",
	"client_id":"1234"
}
```
this url is used in the app to send the response of the heuristic for this specific client.

the endpoint `normalize_merchant` still receives the same request but now it requires a `client-id` header with the id of the client also the response is different it now returns a request_id:
```
{
    "request_id": "105f149e-02b6-4d22-9a42-3a8979c979a6"
}
```

the information received by the webhook is the merchant and the request id previously returned by the normalize_merchant endpoint:
```
{
  "merchant": {"name": "Netflix"}, 
  "request_id": "105f149e-02b6-4d22-9a42-3a8979c979a6"}
```


to execute the application you need to run
```bash
docker-compose up --build
```

this will create a postgres instance as well as a redis instance, the first time it will also create the webhooks table as well as a sample webhook for the fake client `1234` this will point to a public endpoint `https://webhook.site/728342da-1f00-4fb6-99ed-7552845e1103`

the app is exposed on `localhost:9898`

you can check the requests by going to: [this link](https://webhook.site/#!/728342da-1f00-4fb6-99ed-7552845e1103/2a5e84b7-387a-438a-a876-dc517a7972df/1)

I have created a postman collection to this api: [postman](https://www.getpostman.com/collections/8611dd5477c28578fe23)