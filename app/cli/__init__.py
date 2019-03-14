import os
import click
from flask.cli import with_appcontext
from flask import current_app
from app.cli.build import AssetBuilder


@click.command()
@with_appcontext
@click.option('--list-assets', '-a', is_flag=True)
@click.option('--dev-server', '-d', is_flag=True)
@click.argument('cwd', envvar='PWD')
def build(list_assets, dev_server, cwd):
    app = current_app
    if not os.path.exists(cwd):
        print('This command does not accept arguments')
        return
    wab = AssetBuilder(app, cwd)
    if list_assets:
        wab.list_assets()
    elif dev_server:
        wab.execute_dev_server()
    else:
        wab.execute()


@click.command()
@with_appcontext
def ipython():
    from app.database import db
    from app.main.models import User, Role
    from app.climbing.models import Session, Route
    from IPython import embed
    from traitlets.config import get_config
    c = get_config()
    c.InteractiveShellEmbed.colors = 'Linux'
    embed(user_ns={
        'db': db,
        'User': User,
        'Role': Role,
        'Session': Session,
        'Route': Route
    }, config=c)
