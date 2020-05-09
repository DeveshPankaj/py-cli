import click
import os
import json

# from pyfiglet import Figlet
# f = Figlet(font='big')
# print(f.renderText('Android JS'))

import time
import sys


CWD = os.getcwd()

@click.group()
def cli():
    pass

@cli.command()
@click.option('--app-name', prompt='App Name ? ', help='New App Name')
@click.option('--force', is_flag=True, default=False, help='Force to reload resources.')
@click.option('--debug', is_flag=True, default=False, help='Enable debug logs.')
def init(app_name, force, debug):
    click.echo('Creating new project: ' + app_name)
    click.echo(CWD)


@cli.command()
@click.option('--force', is_flag=True, default=False, help='Force to reload resources.')
@click.option('--debug', is_flag=True, default=False, help='Enable debug logs.')
@click.option('--release', is_flag=True, default=False, help='Build Apk in release mode.')
def build(force, debug, release):
	click.echo('Building project')
	if os.path.exists(os.path.join(CWD, 'test-data.json')):
		package = {}
		with open('./test-data.json') as pkg:
			package = json.load(pkg)
		print(package)
	else:
		print("package.json not found")




@cli.command()
@click.option('--force', is_flag=True, default=False, help='Force to reload resources.')
@click.option('--debug', is_flag=True, default=False, help='Enable debug logs.')
def update(force, debug):
    click.echo('Update sdk')


if __name__ == "__main__":
    cli()