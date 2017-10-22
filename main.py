# -*- coding: utf-8 -*-
import click
import twitter_client


@click.group()
def run():
    pass


@run.command()
def authorize():
    twitter_client.authorize()


@run.command()
@click.argument('message')
def update(message):
    if not message:
        return
    client = twitter_client.get_client()
    client.update_status(message)
    click.echo('Tweet "%s"' % message)


if __name__ == "__main__":
  run()
