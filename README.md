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
# the sentry dsn in $env
sentry_sdk.init(traces_sample_rate=1)
```


## Photo

before:

![image](https://user-images.githubusercontent.com/6038418/142375407-c7a5e810-e8c6-4c35-9ffc-0abd0035a85c.png)


after(like flask to show the view_func.name):
![image](https://user-images.githubusercontent.com/6038418/142375499-73ae8777-6f7e-40f0-9aa8-d14ad88e41c7.png)

