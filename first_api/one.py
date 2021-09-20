from fastapi import FastAPI
new=FastAPI()

@new.get("/")
async def root():
    return {"message":"Hello World from fastAPI"}

@new.get("/newpage")
async def root():
    return {"message":"New page created !"}