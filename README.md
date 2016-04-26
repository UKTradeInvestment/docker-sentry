# sentry container
Starts pre-configured with `default` organisation, project, team
- username: admin
- email: admin@localhost
- password: admin

Works with AWS ELB.

You can obtain api keys from the web frontend or from console output (docker logs):
```
PROJECT={} SENTRY_DSN={}
```
