import rich_click as click

from my_cli.utils.aliased_group import AliasedGroup
from my_cli.utils.click_ext import *
from my_cli.utils.click_ctx_obj import ClickCtxObj
from my_cli.utils.click_settings import *
from my_cli.commands.hello import hello


@click.group(invoke_without_command=True, context_settings=CONTEXT_SETTINGS, cls=AliasedGroup, epilog='详见：[http://xxx.yy.zz](http://xxx.yy.zz)')
@click.option('-d', '--debug', is_flag=True,  default=False, help='是否开启调试模式，以打印调试信息')  # 代码级、调试用、适合开发阶段
@click.option('-v', '--verbose', is_flag=True,  default=False, help='是否开启详细模式，以打印运行的详细过程信息')  # 过程级、记录用、适合运行阶段
@click.version_option(message="%(version)s")
@click.pass_context
def cli(ctx, debug, verbose):
    """
    MyCLI 工具（模板）
    """

    ctx.ensure_object(ClickCtxObj)
    ctx.obj.debug = debug
    ctx.obj.verbose = verbose
    click.echo_debug_ctx(ctx)

    if ctx.invoked_subcommand is None:
        # click.echo_debug('I was invoked without subcommand')
        cli.main(args=['--help'], standalone_mode=False)
    else:
        # click.echo_debug(f'I am about to invoke {ctx.invoked_subcommand}')
        pass


# 注册子命令
cli.add_command(hello)


if __name__ == '__main__':
    # 自动环境变量前缀，详见 https://click.palletsprojects.com/en/stable/commands-and-groups/#auto-envvar-prefix
    cli(auto_envvar_prefix='MY_CLI')
