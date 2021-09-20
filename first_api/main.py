from fastapi import FastAPI
app=FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World from fastAPI"}

@app.get("/newpage")
async def root():
    return {"message":"New page created !"}