# services/users/manage.py


from flask.cli import FlaskGroup

from project import app, db     # nuevo


cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()