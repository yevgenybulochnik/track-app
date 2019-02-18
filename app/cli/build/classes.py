import os
import json
import subprocess


class Asset:
    def __init__(self, abs_path):
        self.path = abs_path
        self.name = os.path.basename(self.path)

    @property
    def entry(self):
        package_json = os.path.join(self.path, 'package.json')
        try:
            with open(package_json) as f:
                data = json.loads(f.read())
            return data['main']
        except IOError:
            raise IOError(f'Asset {self.path} does not have a package.json')


class BPAssets:
    def __init__(self, abs_path):
        self.path = abs_path
        self.name = os.path.basename(abs_path)
        self.assets_path = os.path.join(self.path, 'assets')

    @property
    def assets(self):
        asset_dirs = [
            os.path.join(self.assets_path, dir)
            for dir in os.listdir(self.assets_path)
        ]
        return [
            Asset(asset_path)
            for asset_path in asset_dirs
            if os.path.isdir(asset_path)
        ]

    @property
    def entry_points(self):
        entries = dict()
        for asset in self.assets:
            entries.update(self.generate_entry(asset))
        return entries

    def generate_entry(self, asset):
        return {
            f'{self.name}/{asset.name}/{asset.name}':
            f'{asset.path}/{asset.entry}'
        }


class AssetBuilder:
    def __init__(self, app, cwd):
        self.app = app
        self.app_root = app.root_path
        self.cwd = cwd
        self.project_root = os.path.dirname(self.app_root)
        self.wp_config = os.path.join(self.project_root, 'wp_config')
        self.webpack_config = os.path.join(self.wp_config, 'webpack.config.js')
        self.wp_bin = os.path.join(
            self.wp_config,
            'node_modules', '.bin', 'webpack'
        )
        self.wp_dev_server_bin = os.path.join(
            self.wp_config,
            'node_modules', '.bin', 'webpack-dev-server'
        )
        self.proxy_context = ''

    @property
    def blueprints(self):
        bp_assets = []
        for bp in self.app.blueprints:
            bp_path = self.app.blueprints[bp].root_path
            bp_assets_path = os.path.join(bp_path, 'assets')
            if os.path.isdir(bp_assets_path):
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
            'port': os.environ.get('WEBPACK_PORT'),
            'public_url': os.environ.get('WEBPACK_PUBLIC_URL') or '',
            'host': os.environ.get('WEBPACK_HOST') or 'localhost',
            'target': 'http://localhost:5000',
            'proxy_context': self.proxy_context
        }
        return json.dumps(config)

    def generate_entry(self):
        entries = {}
        for bp in self.blueprints:
            for asset in bp.assets:
                if self.cwd == asset.path:
                    self.proxy_context = f'!(/static/{bp.name}/{asset.name}/**)'
                    return bp.generate_entry(asset)
            if self.cwd == bp.assets_path:
                self.proxy_context = f'!(/static/{bp.name}/**)'
                return bp.entry_points
            entries.update(bp.entry_points)
        self.proxy_context = f'!(/static/**)'
        return entries

    def list_assets(self):
        for bp in self.blueprints:
            print(bp.name)
            for asset in bp.assets:
                print('  ', asset.name)
