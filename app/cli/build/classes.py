from os import path, listdir
import json
import subprocess


class Asset:
    def __init__(self, abs_path):
        self.path = abs_path
        self.name = path.basename(self.path)

    @property
    def entry(self):
        package_json = path.join(self.path, 'package.json')
        try:
            with open(package_json) as f:
                data = json.loads(f.read())
            return data['main']
        except IOError:
            raise IOError(f'Asset {self.path} does not have a package.json')


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

    @property
    def entry_points(self):
        entries = dict()
        for asset in self.assets:
            entries[f'{self.name}/{asset.name}/{asset.name}'] = f'{asset.path}/{asset.entry}'
        return entries


class AssetBuilder:
    def __init__(self, app, cwd):
        self.app = app
        self.app_root = app.root_path
        self.cwd = cwd
        self.project_root = path.dirname(self.app_root)
        self.wp_config = path.join(self.project_root, 'wp_config')
        self.webpack_config = path.join(self.wp_config, 'webpack.config.js')
        self.wp_bin = path.join(
            self.wp_config,
            'node_modules', '.bin', 'webpack'
        )
        self.wp_dev_server_bin = path.join(
            self.wp_config,
            'node_modules', '.bin', 'webpack-dev-server'
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

    def execute(self):
        subprocess.run(
            [
                self.wp_bin,
                '--config', self.webpack_config,
                '--env', self.generate_env()
            ],
            cwd=self.cwd
        )

    def execute_dev_server(self):
        subprocess.run(
            [
                self.wp_dev_server_bin,
                '--config', self.webpack_config,
                '--env', self.generate_env()
            ],
            cwd=self.cwd
        )

    def generate_env(self):
        config = {
            'entry': self.generate_entry(),
        }
        return json.dumps(config)

    def generate_entry(self):
        entries = {}
        for bp in self.blueprints:
            for entry, entry_path in bp.entry_points.items():
                if self.cwd == path.dirname(entry_path):
                    return {entry: entry_path}
            if self.cwd == bp.path:
                return bp.entry_points
            entries.update(bp.entry_points)
        return entries

    def list_assets(self):
        for bp in self.blueprints:
            print(bp.name)
            for asset in bp.assets:
                print('  ', asset.name)
