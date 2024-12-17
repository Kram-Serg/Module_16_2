from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()


@app.get('/')
async def main_page():
    return 'Главная страница'


@app.get('/user/admin')
async def admin_page():
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def user(user_id: Annotated[int, Path(ge=1,
                                            le=100,
                                            description='Enter User ID',
                                            example='10')]):
    return f'Вы вошли как пользователь №{user_id}'


@app.get('/user/{user_name}/{user_age}')
async def info_user(user_name: Annotated[str, Path(ge=5,
                                                   le=20,
                                                   description='Enter Username',
                                                   example='Sergei')],
                    user_age: Annotated[int, Path(ge=18,
                                                  le=120,
                                                  description='Enter age',
                                                  example='24')]):
    return f'Информация о пользователе. Имя: {user_name}, возраст: {user_age}'
