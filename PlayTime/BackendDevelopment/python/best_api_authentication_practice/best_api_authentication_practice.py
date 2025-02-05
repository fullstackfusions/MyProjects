import logging
from typing import Callable, Any
from functools import wraps

logger = logging.getLogger(__name__)


def TokenDecorator(function: Callable) -> Callable:
    @wraps(function)
    def _inner(self, *args, **kwargs) -> Any:
        response = None
        with self._authenticate_lock:
            try:
                self._authenticate_token()
                try:
                    response = function(self, *args, **kwargs)
                except:
                    logger.exception("error executing decorated function")
            except:
                logger.exception("error authenticating to device")
            finally:
                try:
                    self._de_authenticate_token()
                except:
                    logger.exception("error de authenticating from device")
        return response

    return _inner


class SomeClass:
    def __init__(self):
        pass

    def _authenticate_token(self):
        pass

    def _authenticate_token(self):
        pass

    def _de_authenticate_token(self):
        pass
