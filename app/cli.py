import subprocess
import click
import json
from os import path, listdir, walk
from flask.cli import with_appcontext


class Asset:
    def __init__(self, abs_path):
        self.path = abs_path
        self.name = path.basename(self.path)


class BPAssets:
    def __init__(self, abs_path):
        self.path = abs_path
        self.name = path.basename(abs_path)
        self.assets_path = path.join(self.path, 'assets')

    @property
    def assets(self):
        asset_dirs = [
            path.join(self.assets_path, dir)
            for dir in listdir(self.assets_path)
        ]
        return [
            Asset(asset_path)
            for asset_path in asset_dirs
            if path.isdir(asset_path)
        ]


class AssetBuilder:
    def __init__(self, app):
        self.app = app
        self.app_root = app.root_path
        self.project_root = path.dirname(self.app_root)
        self.wp_config = path.join(self.project_root, 'wp_config')
        self.webpack_config = path.join(self.wp_config, 'webpack.config.js')
        self.wp_bin = path.join(self.wp_config, 'node_modules', 'webpack')
        self.wp_dev_server_bin = path.join(
            self.wp_config,
            'node_modlues', 'webpack-dev-server'
        )

    @property
    def blueprints(self):
        bp_assets = []
        for bp in self.app.blueprints:
            bp_path = self.app.blueprints[bp].root_path
            bp_assets_path = path.join(bp_path, 'assets')
            if path.isdir(bp_assets_path):
                bp_assets.append(
                    BPAssets(self.app.blueprints[bp].root_path)
                )
        return bp_assets

    def list_assets(self):
        for bp in self.blueprints:
            print(bp.name)
            for asset in bp.assets:
                print('  ', asset.name)


def register(app):

    @app.cli.command()
    @click.option('--list-assets', '-a', is_flag=True)
    def build(list_assets):
        wab = AssetBuilder(app)
        if list_assets:
            wab.list_assets()

    @app.cli.command()
    def build_old():
        """
        Build application assets
        """
        """
        Should refactor to use file globing in the future.
        Also refactor root package.json for globing
        """
        application_root = app.root_path
        project_root = path.dirname(application_root)
        workspace_file = path.join(project_root, "package.json")
        with open(workspace_file) as f:
            data = json.loads(f.read())
        if data['workspaces']:
            for workspace in data['workspaces']:
                if workspace == 'wp_config':
                    continue
                package_name = path.basename(workspace)
                package_path = path.abspath(workspace)
                package_build_path = path.join(package_path, 'build')
                static_path = path.abspath(
                    path.join(package_path, '..', '..', 'static')
                )
                static_builds_path = path.join(static_path, 'package_builds')
                subprocess.run(
                    ['./node_modules/.bin/webpack'],
                    cwd=package_path
                )
                if not path.exists(static_path):
                    subprocess.run(
                        ['mkdir', 'static'],
                        cwd=path.dirname(static_path)
                    )
                if not path.exists(static_builds_path):
                    subprocess.run(
                        ['mkdir', static_builds_path],
                        cwd=static_path
                    )
                if not path.exists(path.join(static_builds_path, package_name)):
                    subprocess.run(
                       ['mkdir', package_name],
                       cwd=static_builds_path
                       )
                for file in listdir(package_build_path):
                    subprocess.run(
                        [
                            'ln', '-snf',
                            path.join(package_build_path, file),
                            path.join(static_builds_path, package_name)
                        ]
                    )
        else:
            print("You have no packages registered")
