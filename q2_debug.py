import asyncio
import logging

# Need to include os to use it in SLEEP_DURATION line
import os
# Need to include datetime to use timer
from datetime import datetime

logger = logging.getLogger(__name__)
SLEEP_DURATION = os.getenv("SLEEP_DURATION")

class Pipeline:
    async def __init__(*args, **kwargs): 
        default_sleep_duration = kwargs["default_sleep_duration"]

    async def sleep_for(coro, sleep_duration, *args, **kwargs): 
        asyncio.sleep(sleep_duration)
        # Fix indentation
        logger.info("Slept for %s seconds", sleep_duration)        

        start = datetime.now()
        # kwargs was passed in, not kwarg
        await coro(*args, **kwargs) 
        end = datetime.now()

        # To get time slept, subtract end from start
        time_elapsed = (end - start).total_seconds()
        logger.debug(f"Executed the coroutine for {time_elapsed} seconds")

