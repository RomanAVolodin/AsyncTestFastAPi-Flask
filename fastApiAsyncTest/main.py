import asyncio
from time import sleep

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/long")
async def say_hello():
    # await asyncio.sleep(5)
    sleep(5)
    return {"message": f"Hello from long endpoint"}

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        reload=True,
    )