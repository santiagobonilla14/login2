from flask import(Blueprint, render_template, request, flash, redirect, url_for,session,g)
from app.db import get_db
from werkzeug.security import check_password_hash, generate_password_hash


##a donde quiero que me dirija la ruta inicial.
bp = Blueprint('inicial', __name__, url_prefix="/")
@bp.route ('/', methods=['GET'])
def inicial():
      db,c= get_db()
      c.execute("SELECT * FROM hecho")
      hechos=c.fetchall()

      return render_template('login/inicio.html', hechos=hechos)

@bp.route ('/registro', methods=['GET','POST'])
def registro():
   if request.method == 'POST':
         usuario = request.form['usuario']
         password = request.form['password']
         db, c= get_db()
         error=None
         c.execute(
            'select id from usuario where user = %s', (usuario,)
         )
         if not usuario:
            error='username es requerido'
         if not password:
            error='Password es requerido'
         elif c.fetchone()is not None:
            error='usuario {} se enncuentra registado.'.format(usuario)
         if error is None:
            c.execute(
                'insert into usuario (user, password) values (%s, %s)',
                (usuario, generate_password_hash(password))
            )
            db.commit()

            return redirect(url_for('inicial.login'))
         flash(error)

   return render_template('login/registro.html')


@bp.route ('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        db, c= get_db()
        error = None
        c.execute(
            'select * from usuario where user = %s',(usuario,) 
        )
        usuario = c.fetchone()

        if usuario is None:
            error='usuario y contraseña invalida'
        elif not check_password_hash(usuario['password'],password):
            error='usuario y/o contraseña incorrecta'
        
        if error is None:
            session.clear()
            session['user_id'] = usuario['id']
            return redirect(url_for('inicial.sesion'))

        flash(error)
   
    return render_template('login/login.html')

@bp.route ('/sesion', methods=['GET','POST'])
def sesion():
   db,c= get_db()
   c.execute("SELECT * FROM hecho")
   hechos=c.fetchall()
   return render_template ('login/sesion.html', hechos=hechos)


# @bp.before_app_request
# def load_logged_in_user():
#     user_id = session.get('user_id')

#     if user_id is None:
#         g.user = None
#     else:
#         db,c=get_db()
#         c.execute(
#             'select * from usuario where id= %s', (user_id,)
#         )
#         g.user = c.fetchone()


@bp.route ('/crear', methods=['GET','POST'])
def crear():
   if request.method=='POST':
      hecho=request.form.get('hecho')
      estado=request.form.get('estado')
      estado=str(estado)
      errors = []

      if not hecho:
         errors.append('hecho es obligatorio')

      if len(errors) == 0:
         db, c = get_db()
         c.execute("INSERT INTO hecho (hecho,estado) VALUES (%s,%s)", (hecho,estado))
         db.commit()
         return redirect(url_for('inicial.crear'))


         
      else:
         for error in errors:
          flash(error)

   return render_template('login/crear.html')
