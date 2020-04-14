import click

from commands import test_results
from neoload_cli_lib import running_tools, user_data, tools


@click.command()
@click.argument("name_or_id", type=str)
def cli(name_or_id):
    """Wait the end of test"""
    if not name_or_id or name_or_id == "cur":
        name_or_id = user_data.get_meta(test_results.meta_key)

    id_ = tools.get_id(name_or_id, test_results.__resolver)

    running_tools.wait(id_)