import datetime
import inspect
import json
import os
import rich_click as click
import sys


###################################################################################################


# 日志级别配置
_LOG_LEVELS = {
    'noset':    {'prefix': '',        'fg': None},
    'debug':    {'prefix': 'DEBUG',   'fg': 'bright_black'},
    'verbose':  {'prefix': 'VERBOSE', 'fg': 'blue'},
    'info':     {'prefix': 'INFO',    'fg': 'cyan'},
    'warning':  {'prefix': 'WARNING', 'fg': 'yellow'},
    'success':  {'prefix': 'SUCCESS', 'fg': 'bright_green'},
    'error':    {'prefix': 'ERROR',   'fg': 'red'},
    'fatal':    {'prefix': 'FATAL',   'fg': 'bright_red'},
}


def _make_echo(level_name):
    """
    动态创建 echo_* 方法
    """
    def _echo(message, **kwargs):
        ctx = click.get_current_context(silent=True)
        if ctx is None:
            return
        obj = ctx.obj
        debug_enabled = getattr(obj, 'debug', False)
        verbose_enabled = getattr(obj, 'verbose', False)

        if level_name == 'debug' and not debug_enabled:
            return
        if level_name == 'verbose' and not (verbose_enabled or debug_enabled):
            return

        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        stack = inspect.stack()
        if len(stack) > 1:
            caller = stack[1]
            abs_path = caller.filename
            try:
                rel_path = os.path.relpath(abs_path, os.getcwd())
            except ValueError:
                rel_path = os.path.basename(abs_path)
            rel_path = rel_path.replace(os.sep, '/')
            lineno = caller.lineno
            funcname = caller.function
        else:
            rel_path = 'unknown'
            lineno = 0
            funcname = 'unknown'

        level_conf = _LOG_LEVELS[level_name]
        level_prefix = level_conf['prefix']
        prefix = ''
        if debug_enabled:
            prefix += f"[{now}] {rel_path} {funcname}() #L{lineno}"
            # if level_prefix:
            #     prefix += f" {level_prefix}"
            prefix += ": "

        full_message = prefix + str(message)

        if 'fg' not in kwargs and level_conf['fg']:
            kwargs['fg'] = level_conf['fg']

        click.secho(full_message, **kwargs)

    return _echo


# 动态创建 echo_* 方法
for _level in _LOG_LEVELS:
    setattr(click, f'echo_{_level}', _make_echo(_level))


###################################################################################################


def echo_debug_ctx(ctx):
    if click.get_current_context(silent=True).obj.debug:
        print('')
        print('')

    click.echo_debug(f' {ctx.command_path} '.center(120, '='))
    click.echo_debug(f' current ctx info '.center(120, '-'))
    click.echo_debug(f'ctx.command = {ctx.command}')
    click.echo_debug(f'ctx.command_path = {ctx.command_path}')
    click.echo_debug(f'ctx.invoked_subcommand = {ctx.invoked_subcommand}')
    click.echo_debug(f'ctx.args = {ctx.args}')
    click.echo_debug(f'ctx.default_map = {ctx.default_map}')
    for key, value in ctx.params.items():
        click.echo_debug(f'ctx.params.get("{key}") = {value}')

    click.echo_debug(f' current func params info '.center(120, '-'))
    for key, value in {key: value for key, value in locals().items() if key not in ['key', 'value']}.items():
        click.echo_debug(f'{key} = {value}')

    click.echo_debug(f' global ctx.obj info '.center(120, '-'))
    for k, v in ctx.obj.__dict__.items():
        click.echo_debug(f'ctx.obj.{k} = {v}')

    click.echo_debug(f''.center(120, '-'))


# 动态挂载
click.echo_debug_ctx = echo_debug_ctx


###################################################################################################


def echo_debug_ctx_dict(ctx):
    if click.get_current_context(silent=True).obj.debug:
        print('')
        print('')

    click.echo_debug(f' current ctx info dict '.center(120, '-'))
    ctx_info_dict = ctx.to_info_dict()
    json_str = json.dumps(ctx_info_dict, indent=4, ensure_ascii=False)
    click.echo_debug(json_str)

    click.echo_debug(f''.center(120, '-'))


# 动态挂载
click.echo_debug_ctx_dict = echo_debug_ctx_dict


###################################################################################################
