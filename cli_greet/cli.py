import click


@click.command()
@click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@click.argument('name', default='world', required=False, metavar='<name>')
def main(name, as_cowboy):
    """
    CLI Greet  greets <name>, optionally as a cowboy.
    """
    greet = 'Howdy' if as_cowboy else 'Hello'
    click.echo('{0}, {1}.'.format(greet, name))
