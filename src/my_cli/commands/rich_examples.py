import os
import time
import rich
import rich_click as click
from click.core import Context
# from rich import print


from my_cli.utils.aliased_group import AliasedGroup
from my_cli.utils.click_settings import CONTEXT_SETTINGS
from my_cli.utils.rich_ext import *


@click.group(context_settings=CONTEXT_SETTINGS, cls=AliasedGroup, epilog='更多说明，见：https://rich.readthedocs.io/en/stable/introduction.html')
@click.pass_context
def rich_examples(ctx: Context):
    """
    rich 的各种示例，以便演示、测试、验证等

    \b\n
    示例：
    ```sh
    $ my-cli rich-examples -h  # 使用说明
    ```
    """
    click.echo_debug_ctx(ctx)


@rich_examples.command('print')
@click.argument('message', required=False, nargs=-1)
@click.pass_context
def print_(ctx: Context, message: str):
    """
    rich.print 的示例

    \b\n
    示例：
    ```sh
    $ my-cli rich-examples print -h  # 使用说明
    $ my-cli rich-examples print  # 输出默认内容
    $ my-cli rich-examples print hello world  # 输出自定义内容
    ```
    """
    rich.print('hello world')
    rich.print(f"[bold red]{' '.join(message) if message else 'This is red text!'}[/bold red]")
    rich.print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:")
    rich.print(locals())


# @rich_examples.command()
# @click.argument('message', required=False, nargs=1)
# @click.pass_context
def echo(ctx: Context, message: str):
    """
    各种调试输出

    \b\n
    执行示例：
    ```sh
    $ my-cli rich-examples echo -h  # 使用说明
    $ my-cli rich-examples echo  # 输出默认信息
    $ my-cli rich-examples echo 你好  # 输出指定信息
    ```
    """
    click.echo_debug_ctx(ctx)

    click.echo_debug(message if message else '调试信息')
    click.echo_verbose(message if message else '详细信息')
    click.echo_info(message if message else '普通信息')
    click.echo_warning(message if message else '警告信息')
    click.echo_error(message if message else '错误信息')
    click.echo_success(message if message else '成功信息')
    click.echo_fatal(message if message else '致命错误')
    click.echo_noset(message if message else '无样式信息')


@rich_examples.command('console')
@click.pass_context
def console_(ctx: Context):
    console.rule()
    console.print('hello world')

    console.rule()
    console.print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", ['aa', 'bb', 'cc'], {'p1': '1', 'p2': '2'})

    console.rule()
    console.print(f"[bold red]'This is red text!'[/bold red]")

    console.rule()
    console.print(locals())

    console.rule()
    console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")

    console.rule()
    console.print('[false, true, null, "foo"]', markup=False)

    console.rule()
    from rich.json import JSON
    console.print(JSON('["foo", "bar"]'))

    console.rule()
    console.print_json('[false, true, null, "foo"]')


@rich_examples.command()
@click.pass_context
def console_print_ext(ctx: Context):
    end = '\n' + '-'*120 + '\n'
    console.print('console.print')
    console.print_noset('console.print_noset', '[red]hello[/]', '\nnew line', end=end)
    console.print_debug('console.print_debug', '[red]hello[/]', '\nnew line', end=end)
    console.print_verbose('console.print_verbose', '[red]hello[/]', '\nnew line', end=end)
    console.print_info('console.print_info', '[red]hello[/]', '\nnew line', end=end)
    console.print_warning('console.print_warning', '[red]hello[/]', '\nnew line', end=end)
    console.print_success('console.print_success', '[red]hello[/]', '\nnew line', end=end)
    console.print_error('console.print_error', '[red]hello[/]', '\nnew line', end=end)
    console.print_fatal('console.print_fatal', '[red]hello[/]', '\nnew line', end=end)


@rich_examples.command('inspect')
@click.pass_context
def inspect_(ctx: Context):
    rich.inspect(inspect_, methods=True)


@rich_examples.command()
@click.argument('message', required=False, nargs=-1)
@click.pass_context
def console_print(ctx: Context, message: str):
    """
    rich.console.Console.print 的示例

    Rich 会通过其 ( \__str__ ) 方法将任何对象转换为字符串，并进行简单的语法高亮。它还会对任何容器（如字典和列表）进行美化打印。如果你打印一个字符串，它将渲染 Console Markup。

    \b\n
    示例：
    ```sh
    $ my-cli rich-examples console-print -h  # 使用说明
    $ my-cli rich-examples console-print  # 输出默认内容
    $ my-cli rich-examples console-print hello world  # 输出自定义内容
    ```
    """
    print(' 原生实现 '.center(120, '-'))
    print([1, 2, 3])
    print("[blue underline]Looks like a link")
    print(locals())
    print('\n\n')

    print(' rich.console.Console.print 实现 '.center(120, '-'))
    console = rich.console.Console()
    console.print([1, 2, 3])
    console.print("[blue underline]Looks like a link")
    console.print(locals())
    console.print("FOO", style="white on blue")


@rich_examples.command()
@click.argument('message', required=False, nargs=-1)
@click.pass_context
def console_log(ctx: Context, message: str):
    """
    log() 方法提供了与 print 相同的功能，但增加了对正在运行的应用程序进行调试有用的特性。日志记录在左侧的列中写入当前时间，在右侧的列中写入方法被调用的文件和行。

    \b\n
    示例：
    ```sh
    $ my-cli rich-examples console-log -h  # 使用说明
    $ my-cli rich-examples console-log  # 输出默认内容
    $ my-cli rich-examples console-log hello world  # 输出自定义内容
    ```
    """

    test_data = [
        {"jsonrpc": "2.0", "method": "sum", "params": [None, 1, 2, 4, False, True], "id": "1", },
        {"jsonrpc": "2.0", "method": "notify_hello", "params": [7]},
        {"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": "2"},
    ]
    movies = ["Deadpool", "Rise of the Skywalker"]

    console = rich.console.Console()
    console.log("Hello from", console, "!")
    console.log('test_data = ', test_data, log_locals=False)
    console.log('movies = ', movies)
    console.log(log_locals=True)


@rich_examples.command()
@click.pass_context
def console_print_json(ctx: Context):
    """
    print_json() 方法将格式化并美化（格式和样式）包含 JSON 的字符串。

    \b\n
    示例：
    ```sh
    $ my-cli rich-examples console-print-json -h  # 使用说明
    ```
    """
    console = rich.console.Console()
    console.print_json('[false, true, null, "foo"]')


@rich_examples.command()
@click.pass_context
def console_out(ctx: Context):
    """
    一种更低级别的终端写入方式。out()方法会将所有位置参数转换为字符串，不会进行美化打印、自动换行或应用标记，但可以应用基本样式，并且可以选择性地进行高亮显示。

    \b\n
    示例：
    ```sh
    $ my-cli rich-examples console-out -h  # 使用说明
    ```
    """
    console = rich.console.Console()
    console.out("Locals", locals())


@rich_examples.command()
@click.pass_context
def console_rule(ctx: Context):
    """
    rule() 方法将绘制一条水平线，并可选添加标题，这是将终端输出划分为不同部分的好方法。

    \b\n
    示例：
    ```sh
    $ my-cli rich-examples console-rule -h  # 使用说明
    ```
    """
    console = rich.console.Console()
    console.rule("[bold red]Chapter 2")


@rich_examples.command()
@click.pass_context
def console_status(ctx: Context):
    """
    Rich 可以显示带有“旋转器”动画的状态消息，而不会干扰常规控制台输出。

    \b\n
    示例：
    ```sh
    $ my-cli rich-examples console-status -h  # 使用说明
    ```

    运行以下命令以演示此功能：
    ```sh
    $ python -m rich.status
    ```

    运行以下命令以查看 spinner 的可用选项：
    ```sh
    $ python -m rich.spinner
    ```
    """

    console.rule("[bold red]示例")
    with console.status("Working..."):
        for i in range(5):
            time.sleep(0.3)  # 模拟耗时操作
            console.log(f"已完成第 {i + 1} 步处理...")  # 在状态栏下方输出日志

    console.rule("[bold red]示例")
    with console.status("Monkeying around...", spinner="monkey"):
        for i in range(5):
            time.sleep(0.3)  # 模拟耗时操作
            console.log(f"已完成第 {i + 1} 步处理...")  # 在状态栏下方输出日志

    console.rule("[bold red]示例")
    with console.status("[bold green]正在处理数据，请稍候...[/bold green]") as status:
        # 模拟一个耗时任务，比如数据处理
        for i in range(5):
            time.sleep(0.3)  # 模拟耗时操作
            console.log(f"已完成第 {i + 1} 步处理...")  # 在状态栏下方输出日志
    console.print("[bold green]✅ 数据处理完成！[/bold green]")


@rich_examples.command()
@click.pass_context
def console_print_justify(ctx: Context):
    """
    justify 参数用于指定文本的对齐方式。

    \b\n
    示例：
    ```sh
    $ my-cli rich-examples console-print-justify -h  # 使用说明
    ```
    """

    style = "bold blue"
    console = rich.console.Console()
    console.print("default", style=style, justify='default')
    console.print("left", style=style, justify="left")
    console.print("center", style=style, justify="center")
    console.print("right", style=style, justify="right")


@rich_examples.command()
@click.pass_context
def console_style(ctx: Context):
    from rich.console import Console
    blue_console = Console(style="white on blue")
    blue_console.print("I'm blue. Da ba dee da ba di.")


@rich_examples.command()
@click.pass_context
def console_record(ctx: Context):
    save_dir = 'outputs'
    os.makedirs(save_dir, exist_ok=True)

    console = rich.console.Console(record=True)

    console.log(log_locals=True)
    console.save_svg(f'{save_dir}/examples_rich_console_record.gitignore.svg')

    console.log(log_locals=True)
    console.save_text(f'{save_dir}/examples_rich_console_record.gitignore.txt')

    console.log(log_locals=True)
    console.save_html(f'{save_dir}/examples_rich_console_record.gitignore.html')
