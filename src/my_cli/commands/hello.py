import os
import rich_click as click
from click.core import Context


@click.command()
@click.argument('name', required=False, nargs=1)
@click.pass_context
def hello(ctx: Context, name: str):
    """
    示例命令：打招呼
    """

    click.echo_debug_ctx(ctx)

    name = name if name else os.environ.get("USER", "you")
    click.echo_info(f'Hello {name} ~')
