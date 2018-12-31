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
            """
            needs to be refactored to test if package_builds already present
            """
            for package_dir in data['workspaces']:
                package_full_path = path.join(project_root, package_dir)
                package_dist_path = path.join(package_dir, 'dist')
                static_dir_path = path.abspath(path.join(package_full_path, '..', '..', 'static'))
                static_package_builds_path = path.join(static_dir_path, 'package_builds')
                subprocess.run(
                    ['./node_modules/.bin/webpack'],
                    cwd=package_full_path
                )
                subprocess.run(
                    ['mkdir',  'package_builds'],
                    cwd=static_dir_path
                )
                for file in listdir(package_dist_path):
                    subprocess.run(
                        ['ln', '-snf', path.abspath(path.join(package_dist_path, file)), static_package_builds_path]
                    )
        else:
            print("You have no packages registered")
