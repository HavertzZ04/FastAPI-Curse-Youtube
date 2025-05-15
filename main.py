from fastapi import FastAPI
#video min 1:29:43

app = FastAPI()

@app.get("/")
async def root():
    return "Hello FastAPI!"

@app.get("/url")
async def url():
    return {"ulr_portfolio":"https://havertzz.netlify.app/"}