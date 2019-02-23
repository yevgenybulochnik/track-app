from setuptools import setup, find_packages


setup(
    name='Flask-Base',
    packages=find_packages(),
    entry_points={
        'flask.commands': [
            'build=app.cli:build'
        ]
    }
)
