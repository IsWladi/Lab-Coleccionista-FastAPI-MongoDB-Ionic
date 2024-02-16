from pydantic import BaseModel
import datetime
from .collections import Libro, Figura, Arma, Carta, Videojuego
from typing import List


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
    username: str
    password: str
    email: str
    coleccion: ColeccionUsuario = ColeccionUsuario(
        videojuegos=[], cartas=[], armas=[], figuras=[], libros=[])
    fecha_registro: datetime.datetime = datetime.datetime.now(
        tz=datetime.timezone.utc)
