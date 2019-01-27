from os import path, listdir


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
