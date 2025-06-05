import asyncio

from funboost import BoosterParams, BrokerEnum, boost


@boost(BoosterParams(queue_name="async_queue", broker_kind=BrokerEnum.REDIS, qps=1000, concurrent_mode="async"))
async def async_task(x, y):
    await asyncio.sleep(1)
    # print(f"async done: {x} + {y} = {x + y}")
    return x + y
