import subprocess
import click
import json
from os import path, listdir
from flask.cli import with_appcontext


def register(app):
    @app.cli.command()
    @with_appcontext
    def build():
        """
        Build application assets
        """
        application_root = app.root_path
        project_root = path.dirname(application_root)
        workspace_file = path.join(project_root, "package.json")
        with open(workspace_file) as f:
            data = json.loads(f.read())
        if data['workspaces']:
            for package in data['workspaces']:
                package_path = path.abspath(package)
                package_dist_path = path.join(package_path, 'dist')
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
                        ['mkdir', 'package_builds'],
                        cwd=static_path
                    )
                for file in listdir(package_dist_path):
                    subprocess.run(
                        [
                            'ln', '-snf',
                            path.join(package_dist_path, file),
                            static_builds_path
                        ]
                    )
        else:
            print("You have no packages registered")
