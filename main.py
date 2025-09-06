from fastapi import fastapi

app = fastapi()

@app.get("/")
async def roof():
    return "Hello World"