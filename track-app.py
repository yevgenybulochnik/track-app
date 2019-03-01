from app import create_app
from app.database import db
from app.main.models import User, Role
from app.climbing.models import Session, Route

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Role': Role,
        'Session': Session,
        'Route': Route
    }
