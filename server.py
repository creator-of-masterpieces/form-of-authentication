from fastapi import FastAPI
from fastapi.responses import Response

#Для запуска сервера введите в консоль команду uvicorn server:app --reload

#Создаём экземляр приложения
app = FastAPI()

@app.get("/")
def index_page():
    """При запросе к адресу / Вернёт страницу с текстом 'Привет!'"""
    with open('templates/login.html', 'r') as f:
        login_page = f.read()
        return Response(login_page, media_type="text/html")
