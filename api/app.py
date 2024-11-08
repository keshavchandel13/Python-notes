from fastapi import FastAPI
app = FastAPI()
@app.get("/getMessage")
async def getMessage(name:str):
     return {f"Hello {name} this is api data"}