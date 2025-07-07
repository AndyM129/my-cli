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
    click.echo_debug(f'Hello {name} ~\t\t << 调试信息')
    click.echo_verbose(f'Hello {name} ~\t\t << 详细信息')
    click.echo_info(f'Hello {name} ~\t\t << 普通信息')
    click.echo_warning(f'Hello {name} ~\t\t << 警告信息')
    click.echo_error(f'Hello {name} ~\t\t << 错误信息')
    click.echo_success(f'Hello {name} ~\t\t << 成功信息')
    click.echo_fatal(f'Hello {name} ~\t\t << 致命错误')
    click.echo_noset(f'Hello {name} ~\t\t << 无样式信息')
    print('\n'*10)
