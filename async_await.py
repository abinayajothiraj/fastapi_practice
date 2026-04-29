from fastapi import FastAPI
import time
import asyncio

app = FastAPI()

# Normal :  (blocking)

@app.get("/")
def sync_api():
    time.sleep(5)             #blocks everything
    return {"message" : "Sync Done"}

# Async (non-blocking)

@app.get("/async")
async def async_api():
    await asyncio.sleep(5)     #does not block
    return {"message" : "Async Done"}

