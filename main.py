# -*- coding: utf-8 -*-
import click

@click.group()
def run():
    pass

@run.command()
@click.argument('message')
def update(message):
    if not message:
        return
    client = get_client()
    client.update_status(message)
    click.echo('Tweet "%s"' % message)

if __name__ == "__main__":
  run()
