import asyncio
from random import random
import functools
from aiohttp_retry.retry_options import ExponentialRetry

from .exceptions import ApiException
from .api import AuthenticationApi


# logger = logging.getLogger('sm_content_api')
retry_opts = ExponentialRetry(statuses={401, 403}, start_timeout=1)


def refresh_expired_token(retry_options: ExponentialRetry = retry_opts):
    """
    Decorator for API methods.
    Refreshes the expired token when the request returns HTTP status code 401.
    :param retry_options: options for the retry function, e.g. ExponentialRetry
    :return: decorated method
    """
    def _decorator(func):
        @functools.wraps(func)
        async def wrapper(self, *args, **kwargs):
            max_retries = retry_options.attempts
            config = self.api_client.configuration
            old_token = config.access_token
            logger = config.logger["sm_content_api"]
            # main idea how to avoid using recursions was proudly stolen from aiohttp_retry.client
            current_attempt = 0

            while True:
                logger.info(f"Attempt {current_attempt + 1} out of {max_retries}. Host: {config.host}")

                current_attempt += 1
                try:
                    res = await func(self, *args, **kwargs)
                    logger.debug(f"Response {res}")

                    # some responses does not contain  data property and may be empty (None)
                    if hasattr(res, 'data') or res is None:
                        return res

                    if current_attempt == max_retries:
                        raise ApiException(f"Max retries ({max_retries}) exceeded")
                    else:
                        retry_wait = retry_options.get_timeout(current_attempt)

                except ApiException as e:

                    if current_attempt >= max_retries:
                        raise e

                    if e.status in retry_options.statuses:

                        if old_token == config.access_token:
                            # wait random time and check if other coroutines already refreshed token
                            _wait = random() * 2
                            logger.debug(f'Waiting random time before refreshing token (t={_wait})')
                            await asyncio.sleep(_wait)

                        if old_token == config.access_token:
                            logger.info(f"Refreshing expired token.  "
                                        f"Old was {old_token[:8] if old_token and len(old_token) > 8 else 'None'}")
                            auth_api = AuthenticationApi(self.api_client)
                            resp = await auth_api.get_token(config.client_id,
                                                            config.client_secret,
                                                            config.grant_type)
                            if resp.token_type == 'Bearer':
                                config.access_token = resp.access_token
                        else:
                            logger.info(f"Token seems to be already refreshed. Skipping refresh.")

                    elif e.status >= 500:
                        raise e

                    retry_wait = retry_options.get_timeout(current_attempt)

                await asyncio.sleep(retry_wait)
        return wrapper
    return _decorator
