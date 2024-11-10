from fastapi import FastAPI, Request, BackgroundTasks
from dotenv import load_dotenv
from bot.bot import bot
import os

# from model.models import create_db_and_tables
load_dotenv()
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    # print("start")
    # create_db_and_tables()
    await bot.bot.set_webhook(WEBHOOK_URL)

@app.post("/webhook")
async def webhook(update: dict, background_tasks: BackgroundTasks):
    await bot.process_update(update)
    return "ok"

@app.get("/")
async def read_root():
    return {"message": "Hello, this is the FastAPI Chatbot server."}