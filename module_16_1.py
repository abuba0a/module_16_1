from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def welcome():
    return f'Главная страница'


@app.get('/user/admin')
async def admin():
    return f'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def userId(user_id: int):
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user')
async def userName(username: str, age: int):
    return f'Информация о пользователе. Имя: {username}, Возраст : {age}'
