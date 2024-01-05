import pprint

import click
from flask.cli import with_appcontext
import cv


@click.command('export-cv')
@click.argument('section')
def export_cv_cmd(section):
    if hasattr(cv, section):
        pprint.pprint(getattr(cv, section))
    else:
        click.echo("Please provide a valid section name")


def register_commands(app):
    app.cli.add_command(export_cv_cmd)
