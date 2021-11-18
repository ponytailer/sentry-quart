# sentry-quart
The sentry middleware for quart

Sentry-asgi can't not collect the information like Flask

## How to install

```
pip install sentry-quart

```

## How to use

```
from quart import Quart
from sentry_quart import QuartMiddleware

app = Quart(__name__)
host = "https://xxxx.com/v1"
app.asgi_app = QuartMiddleware(app, host)._run_asgi3
sentry_sdk.init(traces_sample_rate=1)
```
