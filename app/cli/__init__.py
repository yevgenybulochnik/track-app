import click
from app.cli.build import AssetBuilder


def register(app):
    @app.cli.command()
    @click.option('--list-assets', '-a', is_flag=True)
    def build(list_assets):
        wab = AssetBuilder(app)
        if list_assets:
            wab.list_assets()
