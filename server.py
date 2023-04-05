from fastapi import FastAPI
from fastapi.responses import Response

#Создаём экземляр приложения
app = FastAPI()

#При запросе к адресу / Вернёт страницу с текстом "Привет!"
@app.get("/")
def index_page():
    return Response("Привет!", media_type="text/html")
