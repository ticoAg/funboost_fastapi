from fastapi import FastAPI

from async_tasks import async_task

app = FastAPI()


@app.post("/run_async_task")
async def run_async_task(x: int, y: int):
    # 推送队列任务
    async_task.push(x, y)
    return {"msg": "task pushed", "x": x, "y": y}
