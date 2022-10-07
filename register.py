from flask import(Blueprint, render_template, request, flash, redirect, url_for, current_app)
from app.db import get_db

##a donde quiero que me dirija la ruta inicial.
bp = Blueprint('inicial', __name__, url_prefix="/")
@bp.route ('/', methods=['GET'])
def inicial():
   return render_template('login/inicio.html')


@bp.route ('/login', methods=['GET'])
def login():
   return render_template('login/login.html')

@bp.route ('/registro', methods=['GET'])
def registro():
   return render_template('login/registro.html')