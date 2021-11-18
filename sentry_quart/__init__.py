import logging

from sentry_sdk.integrations.asgi import SentryAsgiMiddleware


logger = logging.getLogger(__name__)


class QuartMiddleware(SentryAsgiMiddleware):
    """support sentry"""

    def __init__(self, app, host, unsafe_context_data=False):
        super().__init__(app.asgi_app, unsafe_context_data)
        self.raw_app = app
        self.host = host
        self._urls = None

    @property
    def urls(self):
        if not self._urls:
            mapper = self.raw_app.url_map
            self._urls = mapper.bind(self.host)
        return self._urls

    def event_processor(self, event, hint, asgi_scope):
        message = super().event_processor(event, hint, asgi_scope)
        request_info = message.get("request", {})
        if not request_info.get("method"):
            request_info["method"] = asgi_scope.get("method")

        path = asgi_scope.get("path", "")
        try:
            view_name, _ = self.urls.match(
                path, asgi_scope["method"].upper())
        except BaseException as exc:
            logger.error(exc)
            return message
        message["transaction"] = view_name
        return message
