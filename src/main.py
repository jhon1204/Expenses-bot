from fastapi import FastAPI, Request, BackgroundTasks
from bot.bot import bot
from model.models import create_db_and_tables

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    # create_db_and_tables()
    bot.run_webhook()

@app.post("/webhook")
async def webhook(update: dict, background_tasks: BackgroundTasks):
    bot.process_update(update)
    return "ok"

@app.get("/")
async def read_root():
    return {"message": "Hello, this is the FastAPI Chatbot server."}