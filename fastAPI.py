from fastapi import FastAPI

app=FastAPI()
@app.get('/')

def he():
    return {'name:ekua'}

