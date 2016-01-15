# Blog dev

Code in development of rules debugging and trace blog

## api-latency-app

Python flask application that can be made to perform poorly via some RPC. This is the
application that will be monitored and remediated.

## app_remediation

StackStorm pack to remediate response times of api-latency-app.

### Requires

https://github.com/StackStorm/st2contrib/tree/master/packs/sensu
