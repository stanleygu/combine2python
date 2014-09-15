import click
import ipythonify
import os


@click.command()
@click.option('--input-str',
              help='Encoded combine archive string to decode.')
@click.option('--output-path', default='/home/user/workspaces',
              help='Path where combine archive will be unzipped.')
@click.option('--project-name',
              help='Name for unzipped archive.')
@click.option('--encoding', default='base64',
              help='Encoding of combine archive string.')
def combine2python(input_str, output_path, project_name, encoding):
    """Extracts encoded string containing combine archive
    and generates Python scripts."""
    ipythonify.str2py(input_str, output_path, project_name, encoding)
    notebook = ipythonify.jsonify(output_path, project_name)
    dstloc = os.path.join(os.path.join(output_path, project_name), project_name + '.ipynb')
    with open(dstloc, "w") as notebook_file:
        notebook_file.write(notebook)

if __name__ == '__main__':
    combine2python()
