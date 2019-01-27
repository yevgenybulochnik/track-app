import os
import click
from app.cli.build import AssetBuilder


def register(app):
    @app.cli.command()
    @click.option('--list-assets', '-a', is_flag=True)
    @click.option('--dev-server', '-d', is_flag=True)
    @click.argument('cwd', envvar='PWD')
    def build(list_assets, dev_server, cwd):
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
