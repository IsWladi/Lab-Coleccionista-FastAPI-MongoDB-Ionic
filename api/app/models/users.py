from pydantic import BaseModel, Field
import datetime
from .collections import Libro, Figura, Arma, Carta, Videojuego
from typing import List
from app.settings import ModelConstraintsSettings


class ColeccionUsuario(BaseModel):
    videojuegos: List[Videojuego]
    cartas: List[Carta]
    armas: List[Arma]
    figuras: List[Figura]
    libros: List[Libro]


class Usuario(BaseModel):
    username: str
    hashed_password: str
    email: str
    fecha_registro: str
    coleccion: ColeccionUsuario


class UserRegistration(BaseModel):
    username: str = Field(..., min_length=ModelConstraintsSettings.min_length_username.value,
                          max_length=ModelConstraintsSettings.max_length_username.value,
                          pattern=ModelConstraintsSettings.username_regex.value)

    password: str = Field(..., min_length=ModelConstraintsSettings.min_length_password.value,
                          max_length=ModelConstraintsSettings.max_length_password.value,
                          pattern=ModelConstraintsSettings.password_regex.value)
    email: str
    coleccion: ColeccionUsuario = ColeccionUsuario(
        videojuegos=[], cartas=[], armas=[], figuras=[], libros=[])
    fecha_registro: datetime.datetime = datetime.datetime.now(
        tz=datetime.timezone.utc)
