import configparser
import json
import math
import os
import random
import time
import rich_click as click
from click.core import Context

from rich.console import Console
from rich.table import Table
from rich.box import SIMPLE

from my_cli.utils.aliased_group import AliasedGroup
from my_cli.utils.click_settings import CONTEXT_SETTINGS


# 另有一些特性，详见如下文档：
# 命令链：https://click.palletsprojects.com/en/stable/commands/#command-chaining
# 命令管道：https://click.palletsprojects.com/en/stable/commands/#command-pipelines
# 上下文默认值：https://click.palletsprojects.com/en/stable/commands/#context-defaults
# 管理资源：https://click.palletsprojects.com/en/stable/advanced/#managing-resources
@click.group(context_settings=CONTEXT_SETTINGS, cls=AliasedGroup, epilog='更多示例见：https://click.palletsprojects.com/en/stable/quickstart/#examples')
@click.pass_context
def click_examples(ctx: Context):
    """
    click 的各种示例，以便演示、测试、验证等

    \b\n
    示例：
    ```sh
    $ my-cli click-examples -h  # 使用说明
    ```

    \f
    如果您不想包含文档字符串的一部分，请添加 \f 转义标记，让 Click 在标记后截断帮助文本。
    """
    click.echo_debug_ctx(ctx)


@click_examples.command()
@click.pass_context
def basic(ctx: Context):
    """
    一个没有任何参数的 基本命令

    \b\n
    示例：
    ```sh
    $ my-cli click-examples basic -h  # 使用说明
    $ my-cli click-examples basic  # 直接执行默认逻辑
    ```
    """
    click.echo_debug_ctx_dict(ctx)
    click.echo_info('this is a basic command')


@click_examples.command()
@click.argument('message', required=False, nargs=1)
@click.pass_context
def echo(ctx: Context, message: str):
    """
    各种调试输出

    \b\n
    执行示例：
    ```sh
    $ my-cli click-examples echo -h  # 使用说明
    $ my-cli click-examples echo  # 输出默认信息
    $ my-cli click-examples echo 你好  # 输出指定信息
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


@click_examples.command()
@click.option('-i', '--int', type=int, required=True, default=None, show_default=True, help='整数参数')
@click.pass_context
def int_option(ctx: Context, int: int):
    """
    整数类型的选项参数

    \b\n
    示例：
    ```sh
    $ my-cli click-examples int-option -h  # 使用说明
    $ my-cli click-examples int-option  # 错误提示：请输入整数
    $ my-cli click-examples int-option --int 123  # 正确传入参数
    ```
    """
    click.echo_info(f'int = {int}')


@click_examples.command()
@click.option("--password", prompt='请输入密码', hide_input=True, confirmation_prompt='请再次输入以确认', help='密码参数')
@click.pass_context
def password_option(ctx: Context, password: str):
    """
    密码类型的选项参数

    \b\n
    示例：
    ```sh
    $ my-cli click-examples password-option -h  # 使用说明
    $ my-cli click-examples password-option  # 提示输入密码
    $ my-cli click-examples password-option --password 123456  # 直接传入密码，无需输入
    ```
    """
    click.echo_info(f'password = {password}')


@click_examples.command()
@click.option('--yes', is_flag=True, expose_value=True, prompt='确认?', help='是否确认')
@click.pass_context
def confirmation_option(ctx: Context, yes: bool):
    """
    确认类型的选项参数

    \b\n
    示例：
    ```sh
    $ my-cli click-examples confirmation-option -h  # 使用说明
    $ my-cli click-examples confirmation-option  # 请求确认，并输出结果
    $ my-cli click-examples confirmation-option --yes  # 直接确认
    ```
    """
    click.echo_info(f'yes = {yes}')
    # if not yes: ctx.abort()


@click_examples.command()
@click.confirmation_option(prompt='确认?')
def confirmation_option_2():
    """
    确认类型的选项参数，仅当确认后才执行

    \b\n
    示例：
    ```sh
    $ my-cli click-examples confirmation-option-2  # 请求确认，并输出结果
    $ my-cli click-examples confirmation-option-2 --yes  # 直接确认
    ```
    """
    click.echo_info(f'已确认')


@click_examples.command()
@click.argument('message', required=False, nargs=-1)  # nargs = -1 则表示可以传入任意个数参数；>=1 则表示传入指定个数的参数
@click.pass_context
def multiple_arguments(ctx: Context, message: tuple[str, ...]):
    """
    多个参数

    \b\n
    示例：
    ```sh
    $ my-cli click-examples multiple-arguments -h  # 使用说明
    $ my-cli click-examples multiple-arguments aaa bbb ccc # 传入多个参数
    ```
    """
    click.echo_info(f'message = {message}')


@click_examples.command(deprecated=True)
@click.pass_context
def deprecating_commands(ctx: Context):
    """
    标记为废弃的命令

    \b\n
    示例：
    ```sh
    $ my-cli click-examples deprecating-commands -h  # 使用说明
    $ my-cli click-examples deprecating-commands  # 执行命令
    ```
    """
    click.echo_info(f'hello {click.get_current_context().info_name}')


# @click_examples.command()
# @click.option('-u', '--username', type=str, required=False, default=None, help='用户名')
# @click.pass_context
# def auto_envvar_prefix(ctx: Context, username: str):
#     """
#     自动环境变量前缀
#     详见文档：https://click.palletsprojects.com/en/stable/commands-and-groups/#auto-envvar-prefix
#
#     \b
#     执行示例：
#     $ my-cli click-examples auto-envvar-prefix -h  # 使用说明
#     $ my-cli click-examples auto-envvar-prefix --username myname  # 手动输入参数值
#     $ export MY_CLI_EXAMPLES_AUTO_ENVVAR_PREFIX_USERNAME=Andy && my-cli click-examples auto-envvar-prefix  # 自动识别环境变量
#     """
#     click.echo_info(f'username = {username}')


@click_examples.command()
@click.option('-n', '--name', prompt='请输入姓名', default=lambda: os.environ.get("USER", ""), show_default="$USER")
@click.pass_context
def option_prompts(ctx: Context, name: str):
    """
    选项提示

    \b\n
    示例：
    ```sh
    $ my-cli click-examples option-prompts -h  # 使用说明
    $ my-cli click-examples option-prompts  # 提示输入参数值
    $ my-cli click-examples option-prompts --name 张三  # 直接传入参数值
    ```

    \b
    另见：https://click.palletsprojects.com/en/stable/prompts/#optional-prompts
    """
    click.echo_info(f'name = {name}')


@click_examples.command()
@click.pass_context
def input_prompts(ctx: Context):
    """
    手动请求用户输入

    \b\n
    示例：
    ```sh
    $ my-cli click-examples input-prompts -h  # 使用说明
    $ my-cli click-examples input-prompts  # 执行该示例
    ```
    """
    click.echo_info(f'你好！')
    name = click.prompt('请输入姓名', type=str, default=f'{os.environ.get("USER", "you")}', show_default=True)
    click.echo_info(f'name = {name}')


@click_examples.command()
@click.pass_context
def confirmation_prompts(ctx: Context):
    """
    手动请求用户确认

    \b\n
    示例：
    ```sh
    $ my-cli click-examples confirmation-prompts -h  # 使用说明
    $ my-cli click-examples confirmation-prompts  # 执行该示例
    ```
    """
    click.echo_info(f'你好！')
    if click.confirm('要继续么?'):
        click.echo_info(f'继续执行')
    else:
        click.echo_info(f'退出执行')
        ctx.abort()

    # 或者，可以选择让函数在未返回 True 时自动中止程序执行
    # if click.confirm('Do you want to continue?'):
    #     click.echo('Well done!')


@click_examples.command()
@click.option('-n', '--name', prompt='请输入姓名', default=lambda: os.environ.get("USER", ""), show_default="$USER")
@click.pass_context
def invoking_other_commands(ctx: Context, name: str):
    """
    调用其他命令

    \b\n
    示例：
    ```sh
    $ my-cli click-examples invoking-other-commands -h  # 使用说明
    $ my-cli click-examples invoking-other-commands  # 执行该示例
    ```
    """
    ctx.forward(option_prompts)  # 用当前命令的参数进行填充
    ctx.invoke(option_prompts, name='invoking_other_commands !!')  # 只是用调用者提供的参数调用另一个命令


@click_examples.command()
@click.pass_context
def pager_support(ctx: Context):
    """
    分页支持

    \b\n
    示例：
    ```sh
    $ my-cli click-examples pager-support -h # 显示使用说明
    $ my-cli click-examples pager-support  # 执行该示例
    ```
    """
    click.echo_via_pager("\n".join(f"Line {idx}" for idx in range(200)))


@click_examples.command()
@click.pass_context
def pager_support_2(ctx: Context):
    """
    分页支持：配合生成器函数使用

    如果您想使用分页器显示大量文本，特别是如果预先生成所有内容需要大量时间，您可以传递一个生成器（或生成器函数）而不是字符串：

    \b\n
    示例：
    ```sh
    $ my-cli click-examples pager-support-2 -h # 显示使用说明
    $ my-cli click-examples pager-support-2  # 执行该示例
    ```
    """

    def _generate_output():
        for idx in range(50000):
            yield f"Line {idx}\n"

    click.echo_via_pager(_generate_output())


@click_examples.command()
@click.option('--prompt', is_flag=True, prompt='切到要清除终端屏幕?')
@click.pass_context
def clear(ctx: Context, prompt: bool):
    """
    清除终端屏幕

    \b\n
    示例：
    ```sh
    $ my-cli click-examples clear -h # 显示使用说明
    $ my-cli click-examples clear  # 执行该示例
    ```
    """
    if prompt:
        click.clear()


@click_examples.command()
@click.pass_context
def getchar(ctx: Context):
    """
    从终端获取字符

    \b\n
    示例：
    ```sh
    $ my-cli click-examples tests-2 -h  # 执行该示例
    $ my-cli click-examples tests-2  # 执行该示例
    ```
    """
    click.echo_info(f'你好！')
    click.echo_info('要继续么? [yn] ', nl=False)

    c = click.getchar()
    click.echo()
    if c == 'y':
        click.echo('已继续')
    elif c == 'n':
        click.echo('已终止')
    else:
        click.echo('无效输入 :(')


@click_examples.command()
@click.pass_context
def pause(ctx: Context):
    """
    等待用户按键

    \b\n
    示例：
    ```sh
    $ my-cli click-examples waiting-for-key-press -h  # 显示使用说明
    $ my-cli click-examples waiting-for-key-press  # 执行该示例
    ```
    """
    click.echo_info(f'你好！')
    click.pause(info='按任意键继续...')  # 默认会输出 Press any key to continue...


@click_examples.command()
@click.pass_context
def editor(ctx: Context):
    """
    启动编辑器

    \b\n
    示例：
    ```sh
    $ my-cli click-examples editor -h  # 显示使用说明
    $ my-cli click-examples editor  # 执行该示例
    ```
    """
    MARKER = '# Everything below is ignored\n'
    content = click.edit('\n\n' + MARKER)
    click.echo_debug(f'content = ```\n{content}\n```')
    # if message is not None:
    #     msg = message.split(MARKER, 1)[0].rstrip("\n")
    #     if not msg:
    #         click.echo("Empty message!")
    #     else:
    #         click.echo(f"Message:\n{msg}")
    # else:
    #     click.echo("You did not enter anything!")

    message = content.split(MARKER, 1)[0].rstrip('\n') if content is not None else None
    click.echo_debug(f'message = ```\n{message}\n```')

    TIMESTAMP = int(time.time())  # 当前时间戳，eg. 1617351251
    DATE_STAMP = time.strftime('%Y%m%d%H%M%S', time.localtime(TIMESTAMP))  # 当前时间戳，eg. 20210402161411

    filename = f'../outputs/examples_editor_output_{DATE_STAMP}.gitignore.txt'
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with click.open_file(filename, 'w') as f:
        f.write(message if message else '')


@click_examples.command()
@click.pass_context
def launching_applications(ctx: Context):
    """
    启动应用程序

    \b\n
    示例：
    ```sh
    $ my-cli click-examples launching-applications -h  # 显示使用说明
    $ my-cli click-examples launching-applications  # 执行该示例
    ```
    """
    url = 'https://click.palletsprojects.com/'
    click.echo_info(f'准备打开: {url}')
    click.pause(info='按任意键继续...')  # 默认会输出 Press any key to continue...
    click.launch("https://click.palletsprojects.com/")

    # 除此之外，它还可以启动文件管理器并自动选择提供的文件。
    # click.launch("/my/downloaded/file.txt", locate=True)


@click_examples.command()
@click.pass_context
def format_filename(ctx: Context):
    """
    将文件名格式化为字符串以供显示

    由于文件名可能不是 Unicode，格式化它们可能有点棘手。
    在 click 中，这种方式是通过 format_filename() 函数实现的。它会尽力将文件名转换为 Unicode，并且永远不会失败。这使得可以在完整的 Unicode 字符串上下文中使用这些文件名。

    \b\n
    示例：
    ```sh
    $ my-cli click-examples format-filename -h  # 显示使用说明
    $ my-cli click-examples format-filename  # 执行该示例
    ```
    """
    filename = 'xx/yy/zz/foo.txt'
    click.echo_info(f"filename: {filename}")
    click.echo_info(f">> {click.format_filename(filename)}\t\t# format_filename")
    click.echo_info(f">> {click.format_filename(filename, shorten=True)}\t\t\t# format_filename shorten=True")


@click_examples.command()
@click.pass_context
def open_file(ctx: Context):
    """
    打开文件

    \b\n
    示例：
    ```sh
    $ my-cli click-examples open-file -h  # 显示使用说明
    $ my-cli click-examples open-file  # 执行该示例
    ```
    """
    filename = f'../outputs/examples_open_file_output.gitignore.txt'
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # 'a' 表示追加内容
    # ’w‘ 是覆盖写入
    with click.open_file(filename, 'a') as f:
        TIMESTAMP = int(time.time())  # 当前时间戳，eg. 1617351251
        DATE = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(TIMESTAMP))  # 当前时间，eg. 2021-04-02 16:14:11
        f.write(f'[{DATE}] Hello World!\n')

    click.echo_info(f'已将内容追加至文件：{filename}')


@click_examples.command()
@click.pass_context
def get_app_dir(ctx: Context):
    """
    获取应用程序目录

    \b\n
    示例：
    ```sh
    $ my-cli click-examples get-app-dir -h  # 显示使用说明
    $ my-cli click-examples get-app-dir  # 执行该示例
    ```
    """
    APP_NAME = 'My CLI'
    app_dir = click.get_app_dir(APP_NAME)
    click.echo_info(f"app_dir = {app_dir}")


@click_examples.command()
@click.pass_context
def read_config(ctx: Context):
    """
    读取配置文件

    \b\n
    示例：
    ```sh
    $ my-cli click-examples read-config -h  # 显示使用说明
    $ my-cli click-examples read-config  # 执行该示例
    ```
    """
    APP_NAME = 'My CLI'
    app_dir = click.get_app_dir(APP_NAME)
    click.echo_info(f"app_dir = {app_dir}")

    app_dir = 'tests/data'
    click.echo_warning(f"为了方便测试，暂将 app_dir mock 为 {app_dir}")
    cfg = os.path.join(app_dir, 'config.ini')
    parser = configparser.RawConfigParser()
    parser.read([cfg])
    rv = {}
    for section in parser.sections():
        for key, value in parser.items(section):
            rv[f"{section}.{key}"] = value

    click.echo_info(f'读取配置文件 {cfg} 内容：{json.dumps(rv, indent=4, ensure_ascii=False)}')


# @click_examples.command()
# @click.pass_context
# def appdirs(ctx: Context):
    # click.echo_info('调试中... :(')
    # print(appdirs.__version__)
    #
    # 定义你的应用名称和作者（通常与项目名称一致）
    # app_name = "my-cli"
    # app_author = "Andy Meng"  # 可选，某些系统会用到
    #
    # app_name = "my-cli"
    # app_author = "your_name_or_organization"  # 可选，某些系统会用到
    #
    # 创建 AppDirs 实例
    # dirs = AppDirs(app_name, app_author)
    #
    #
    # # 获取不同用途的目录路径
    # # 注意：某些目录可能需要手动创建（如果不存在的话）
    #
    # # 用户数据文件（持久化数据，如配置、生成的文件等）
    # user_data_dir = dirs.user_data_dir
    # click.echo_info(f"User Data Directory: {user_data_dir}")
    #
    # # 用户缓存目录（临时缓存文件，可被系统清理）
    # user_cache_dir = dirs.user_cache_dir
    # click.echo_info(f"User Cache Directory: {user_cache_dir}")
    #
    # # 用户日志目录（日志文件）
    # user_log_dir = dirs.user_log_dir
    # click.echo_info(f"User Log Directory: {user_log_dir}")


@click_examples.command()
@click.pass_context
def progressbar(ctx: Context):
    """
    进度条

    \b\n
    示例：
    ```sh
    $ my-cli click-examples progressbar -h  # 显示使用说明
    $ my-cli click-examples progressbar  # 执行该示例
    ```
    """

    # 在每次循环迭代后更新条形图
    with click.progressbar(range(10), label='示例1') as bar:
        for x in bar:
            time.sleep(0.05)

    # 直接指定长度
    with click.progressbar(length=100, label='示例2', hidden=False, item_show_func=lambda update_index: f'<<- 当前为第 {update_index} 次更新') as bar:
        for update_index in bar:
            time.sleep(0.05)
            bar.update(random.randint(0, 10))
            if bar.pos >= 100:
                break

    # 指定样式
    with click.progressbar(
        length=100, label='示例3',
        fill_char=click.style(">", fg="green"),
        empty_char=click.style("-", fg="bright_black"),
        hidden=False,
        item_show_func=lambda update_index: f'<<- 当前为第 {update_index} 次更新',
    ) as bar:
        for update_index in bar:
            time.sleep(0.05)
            bar.update(random.randint(0, 10))
            if bar.pos >= 100:
                break

    # 指定样式
    with click.progressbar(
        length=100,
        label='示例4',
        bar_template="%(label)s  %(bar)s | %(info)s",
        fill_char=click.style("█", fg="cyan"),
        empty_char=" ",
        hidden=False,
        item_show_func=lambda update_index: f'<<- 当前为第 {update_index} 次更新',
    ) as bar:
        for update_index in bar:
            time.sleep(0.05)
            bar.update(random.randint(0, 10))
            if bar.pos >= 100:
                break

    # 更多官方示例：
    count = 8000
    items = range(count)

    def process_slowly(item):
        time.sleep(0.002 * random.random())

    def filter(items):
        for item in items:
            if random.random() > 0.3:
                yield item

    with click.progressbar(
        items, label="Processing accounts", fill_char=click.style("#", fg="green")
    ) as bar:
        for item in bar:
            process_slowly(item)

    def show_item(item):
        if item is not None:
            return f"Item #{item}"

    with click.progressbar(
        filter(items),
        label="Committing transaction",
        fill_char=click.style("#", fg="yellow"),
        item_show_func=show_item,
    ) as bar:
        for item in bar:
            process_slowly(item)

    with click.progressbar(
        length=count,
        label="Counting",
        bar_template="%(label)s  %(bar)s | %(info)s",
        fill_char=click.style("█", fg="cyan"),
        empty_char=" ",
    ) as bar:
        for item in bar:
            process_slowly(item)

    with click.progressbar(
        length=count,
        width=0,
        show_percent=False,
        show_eta=False,
        fill_char=click.style("#", fg="magenta"),
    ) as bar:
        for item in bar:
            process_slowly(item)

    # 'Non-linear progress bar'
    steps = [math.exp(x * 1.0 / 20) - 1 for x in range(20)]
    count = int(sum(steps))
    with click.progressbar(
        length=count,
        show_percent=False,
        label="Slowing progress bar",
        fill_char=click.style("█", fg="green"),
    ) as bar:
        for item in steps:
            time.sleep(item)
            bar.update(item)


@click_examples.command()
@click.pass_context
def fail(ctx: Context):
    """
    中止程序并显示特定的错误信息

    \b\n
    示例：
    ```sh
    $ my-cli click-examples fail -h  # 显示使用说明
    $ my-cli click-examples fail  # 执行该示例
    ```
    """
    message = click.prompt('请输入要模拟的 错误信息', type=str, default=f'默认信息', show_default=True)
    ctx.fail(message)


@click_examples.command()
@click.pass_context
def abort(ctx: Context):
    """
    终止脚本

    \b\n
    示例：
    ```sh
    $ my-cli click-examples abort -h  # 显示使用说明
    $ my-cli click-examples abort  # 执行该示例
    ```
    """
    if click.confirm('要终止执行么?'):
        click.echo_info(f'已终止执行')
        ctx.abort()

    click.echo_info(f'继续执行')


@click_examples.command()
@click.pass_context
def exit(ctx: Context):
    """
    退出应用程序并使用指定的退出代码，可在执行后通过 `echo $?` 查看

    \b\n
    示例：
    ```sh
    $ my-cli click-examples exit -h  # 显示使用说明
    $ my-cli click-examples exit  # 执行该示例
    ```
    """
    code = click.prompt('请输入要模拟的 退出代码', type=int, default=f'0', show_default=True)
    ctx.exit(code)


@click_examples.command()
@click.pass_context
def get_usage(ctx: Context):
    """
    获取命令的使用说明

    \b\n
    示例：
    ```sh
    $ my-cli click-examples get-usage -h  # 显示使用说明
    $ my-cli click-examples get-usage  # 执行该示例
    ```
    """
    click.echo_info(f'{ctx.get_usage()}')


@click_examples.command()
@click.pass_context
def get_help(ctx: Context):
    """
    获取命令的帮助信息

    \b\n
    示例：
    ```sh
    $ my-cli click-examples get-help -h  # 显示使用说明
    $ my-cli click-examples get-help  # 执行该示例
    ```
    """
    click.echo_info(f'{ctx.get_help()}')


@click_examples.command()
@click.pass_context
def colors(ctx: Context):
    """
    输出所有颜色的示例文本

    \b\n
    示例：
    ```sh
    $ my-cli click-examples all-colors -h  # 显示使用说明
    $ my-cli click-examples all-colors  # 执行该示例
    ```
    """
    all_colors = (
        "black",
        "red",
        "green",
        "yellow",
        "blue",
        "magenta",
        "cyan",
        "white",
        "bright_black",
        "bright_red",
        "bright_green",
        "bright_yellow",
        "bright_blue",
        "bright_magenta",
        "bright_cyan",
        "bright_white",
    )
    for color in all_colors:
        click.echo(click.style(f"I am style text —— fg={color}", fg=color))

    click.echo('-' * 120)
    for color in all_colors:
        click.echo(click.style(f"I am style text —— fg={color}, bold=True", fg=color, bold=True))

    click.echo('-' * 120)
    for color in all_colors:
        click.echo(click.style(f"I am style text —— fg={color}, reverse=True", fg=color, reverse=True))

    click.echo('-' * 120)
    click.echo(click.style("I am style text —— blink=True", blink=True))
    click.echo(click.style("I am style text —— underline=True", underline=True))


@click_examples.command()
@click.pass_context
def colors_table(ctx: Context):
    """
    输出所有颜色的表格

    \b\n
    示例：
    ```sh
    $ my-cli click-examples colors-table -h  # 显示使用说明
    $ my-cli click-examples colors-table  # 执行该示例
    ```
    """
    console = Console(color_system="truecolor")

    table = Table(title="ANSI Colors", box=SIMPLE)
    colors = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    table.add_column("Color", style="bold")

    for variant in ["Normal", "Dim", "Bright", "Dim +\nBright"]:
        table.add_column(variant, style="bold")

    for color in colors:
        table.add_row(
            color,
            *[
                f"[{style}{color}]██████[/{style}{color}]"
                for style in ["", "dim ", "bright_", "dim bright_"]
            ]
        )

    console.print(table)


# @click_examples.command()
# @click.argument("input", type=click.File("rb"), nargs=-1)
# @click.argument("output", type=click.File("wb"))
# def inout(input, output):
#     """
#     输入&输出
#
#     This example works similar to the Unix `cat` command but it writes
#     into a specific file (which could be the standard output as denoted by
#     the ``-`` sign).
#
#     \b
#     Copy stdin to stdout:
#         inout - -
#
#     \b
#     Copy foo.txt and bar.txt to stdout:
#         inout foo.txt bar.txt -
#
#     \b
#     Write stdin into the file foo.txt
#         inout - foo.txt
#     """
#     for f in input:
#         while True:
#             chunk = f.read(1024)
#             if not chunk:
#                 break
#             output.write(chunk)
#             output.flush()
