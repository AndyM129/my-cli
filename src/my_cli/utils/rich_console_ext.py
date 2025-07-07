import datetime
import inspect
import json
import os
import rich_click as click
import sys
from rich.console import Console

from my_cli.utils.click_ext import _LOG_LEVELS


console = Console(
    # 启用导出功能，以便将写入它的任何内容导出为文本、svg 或 html 格式
    # 详见 https://rich.readthedocs.io/en/stable/console.html#exporting
    # record=True,
)


def _make_print_x(level_name):
    """
    动态创建 print_* 方法
    """
    def _print_x(*objects, **kwargs) -> None:
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
            prefix += ": "

        if 'fg' not in kwargs and level_conf['fg']:
            kwargs.setdefault("style", level_conf['fg'])

        if len(prefix):
            console.print(prefix, *objects, **kwargs)
        else:
            console.print(*objects, **kwargs)

    return _print_x


# 动态创建 print_* 方法
for _level in _LOG_LEVELS:
    setattr(console, f'print_{_level}', _make_print_x(_level))
