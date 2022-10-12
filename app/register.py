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

@bp.route ('/registro', methods=['GET','POST'])
def registro():
   if request.method == 'POST':
         usuario = request.form.get('usuario')
         password = request.form.get('password')
         errors =[]

         if not usuario:
            errors.append('digitar usuario')
         if not password :
             errors.append('contraseña obligatoria')

         if len(errors) == 0:
            db, c = get_db()
            c.execute("INSERT INTO usuario (user,password) VALUES (%s,%s)",(usuario,password))
            db.commit()
            return redirect(url_for('inicial.login'))
         
         else:
            for error in errors:
               flash(error) 

   return render_template('login/registro.html')

@bp.route ('/crear', methods=['GET','POST'])
def crear():
   if request.method=='POST':
      hecho=request.form.get('hecho')
      estado=request.form.get('estado')
      errors = []

      if not hecho:
         errors.append('hecho es obligatorio')

      if len(errors) == 0:
         db, c = get_db()
         c.execute("INSERT INTO hecho (hecho,estado) VALUES (%s,%s)", (hecho,estado))
         db.commit()
         return redirect(url_for('inicial.login'))


         
      else:
         for error in errors:
          flash(error)

   return render_template('login/crear.html')
