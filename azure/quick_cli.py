import sys

from azure.cli.core import get_default_cli


def invoke_default_cli():
    """Simply invokes the default CLI program."""
    az_cli = get_default_cli()
    exit_code = az_cli.invoke(sys.argv[1:])
    sys.exit(exit_code)
