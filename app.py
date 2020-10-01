from app import create_app as application
from app import db
from app.dbmodels import User

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}

if __name__ == '__main__':
    app.run(debug=True)
else:
    application = app