import click
from findreplace.core import findreplace

@click.group()
def cli():
    """findreplace
    """
    if sys.version_info[0] == 2:
        print("Current environment is Python 2.")
        print("Please use a Python 3 virtualenv")
        raise SystemExit


@cli.command('replace')
@click.argument('find_val', required=True)
@click.argument('replace_val', required=True)
@click.option('--perm', is_flag=True)
def replace(find_val, replace_val, perm):
    findreplace(find_val, replace_val)


def main():
    cli()


if __name__ == '__main__':
    main()
