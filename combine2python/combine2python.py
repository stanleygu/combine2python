import click
import ipythonify


@click.command()
@click.option('--input',
              help='Encoded combine archive string to decode.')
@click.option('--output-path', default='/home/user/workspaces',
              help='Path where combine archive will be unzipped.')
@click.option('--folder-name',
              help='Name for unzipped archive.')
@click.option('--encoding', default='base64',
              help='Encoding of combine archive string.')
def combine2python(inputstr, dirpth, fname, encoding):
    """Simple program that greets NAME for a total of COUNT times."""
    ipythonify.str2py(inputstr, dirpth, fname, encoding)

if __name__ == '__main__':
    combine2python()
