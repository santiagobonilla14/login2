from flask import (
    Blueprint,flash, g, redirect,render_template,request,url_for
)
from werkzeug.exceptions import abort
from app.register import login_required
from app.db import get_db

bp = Blueprint('todo', __name__)

@bp.route('/')
@login_required
def index():
   db, c= get_db()
   c.execute(
        'select h.id, h.hecho,u.username,h.completed, h.created_at '
        'from hechos h JOIN usuario u on h.created_by = u.id where h.created_by = %s order by created_at desc',
        (g.user['id'],)
   )
   hechos = c.fetchall()
    
   return render_template('hechos/index.html', hechos=hechos)


@bp.route ('/crear', methods=['GET','POST'])
def crear():
   if request.method=='POST':
      hecho=request.form.get('hecho')
      estado=request.form.get('estado')
      estado=str(estado)
      error=None

      if not hecho:
            error='hecho es requerido'
        
      if error is not None:
            flash(error)
        
      else: 
         db, c =get_db()
         c.execute(
                'insert into hechos (hecho,estado,completed, created_by)'
                'values (%s,%s,%s,%s)',
                (hecho,estado, False, g.user['id'])
                 )
         db.commit()
         return redirect(url_for('todo.index'))


   return render_template('login/crear.html')

def get_hecho(id):
    db, c= get_db()
    c.execute(
        'select h.id, h.hecho, h.completed,h.created_by, h.created_at, u.username ' 
        'from hechos h JOIN usuario u on h.created_by = u.id where h.id = %s',
        (id,)
    )

    hecho = c.fetchone()

    if hecho is None:
        abort(404, 'el todo de id {0} no existe'.format(id))
    return hecho

@bp.route('/<int:id>/update' , methods=['GET','POST'])
@login_required
def update(id):
    hecho = get_hecho(id)
    if request.method=='POST':
        description = request.form['description']
        completed=True if request.form.get('completed') == 'on' else False
        error = None

        if not description:
            error= "la sescribcion es requerida."
        if error is not None:
                flash(error)
        else:
            db, c= get_db()
            c.execute(
                    'update hechos set hecho = %s, completed=%s '
                    'where id = %s and created_by= %s',
                    (description, completed, id, g.user['id'])
                     )
            db.commit()
            return redirect(url_for('todo.index'))

    return render_template('hechos/update.html', hechos=hecho) 


@bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    db, c=get_db()
    c.execute('delete from hechos where id =%s and created_by= %s',(id,g.user['id']))
    db.commit()
    return redirect(url_for('todo.index'))