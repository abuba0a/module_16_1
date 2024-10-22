from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def welcome():
    return f'Главная страница'


@app.get('/user/admin')
async def welcome():
    return f'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def id_paginator(user_id: int):
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user')
async def id_paginator(username: str, age: int):
    return f'Информация о пользователе. Имя: {username}, Возраст : {age}'
