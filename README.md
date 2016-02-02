# Blog dev

Code in development of rules debugging and trace blog

## api-latency-app

Python flask application that can be made to perform poorly via some RPC. This is the
application that will be monitored and remediated.

In this sample application it is possible to purposefully and only
for demonstration purposes only cause it to degrade API response latency as well as restore the performance.

There are 3 APIs that this application exposes -
* `http://app-server:9999/sqaure/<number>`
* `http://app-server:9999/bad/<latency-time-sec>`
* `http://app-server:9999/good`

## app_remediation

StackStorm pack to remediate response times of api-latency-app.

### Requires

https://github.com/StackStorm/st2contrib/tree/master/packs/sensu
