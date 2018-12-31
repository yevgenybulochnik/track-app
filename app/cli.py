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
