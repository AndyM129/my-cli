import rich_click as click

###################################################################################################
# rich-click configurations
#
# - 注释掉 则表示取默认配置
# - 完整配置，详见 https://ewels.github.io/rich-click/documentation/configuration/#configuration-options
# - 样式的实时编辑器，见 https://ewels.github.io/rich-click/editor
###################################################################################################
# click.rich_click.STYLE_OPTION = "bold cyan"
# click.rich_click.STYLE_ARGUMENT = "bold cyan"
# click.rich_click.STYLE_COMMAND = "bold cyan"
# click.rich_click.STYLE_SWITCH = "bold green"
# click.rich_click.STYLE_METAVAR = "bold yellow"
# click.rich_click.STYLE_METAVAR_APPEND = "dim yellow"
# click.rich_click.STYLE_METAVAR_SEPARATOR = "dim"
# click.rich_click.STYLE_HEADER_TEXT = ""
# click.rich_click.STYLE_EPILOG_TEXT = ""
# click.rich_click.STYLE_FOOTER_TEXT = ""
# click.rich_click.STYLE_USAGE = "yellow"
# click.rich_click.STYLE_USAGE_COMMAND = "bold"
# click.rich_click.STYLE_DEPRECATED = "red"
# click.rich_click.STYLE_HELPTEXT_FIRST_LINE = ""
# click.rich_click.STYLE_HELPTEXT = "dim"
# click.rich_click.STYLE_OPTION_HELP = ""
# click.rich_click.STYLE_OPTION_DEFAULT = "dim"
# click.rich_click.STYLE_OPTION_ENVVAR = "dim yellow"
# click.rich_click.STYLE_REQUIRED_SHORT = "red"
# click.rich_click.STYLE_REQUIRED_LONG = "dim red"
# click.rich_click.STYLE_OPTIONS_PANEL_BORDER = "dim"
# click.rich_click.STYLE_OPTIONS_PANEL_BOX = "ROUNDED"
# click.rich_click.ALIGN_OPTIONS_PANEL = "left"
# click.rich_click.STYLE_OPTIONS_TABLE_SHOW_LINES = False
# click.rich_click.STYLE_OPTIONS_TABLE_LEADING = 0
# click.rich_click.STYLE_OPTIONS_TABLE_PAD_EDGE = False
# click.rich_click.STYLE_OPTIONS_TABLE_PADDING = (0, 1)
click.rich_click.STYLE_OPTIONS_TABLE_BOX = "SIMPLE"
# click.rich_click.STYLE_OPTIONS_TABLE_ROW_STYLES = None
# click.rich_click.STYLE_OPTIONS_TABLE_BORDER_STYLE = None
# click.rich_click.STYLE_COMMANDS_PANEL_BORDER = "dim"
# click.rich_click.STYLE_COMMANDS_PANEL_BOX = "ROUNDED"
# click.rich_click.ALIGN_COMMANDS_PANEL = "left"
# click.rich_click.STYLE_COMMANDS_TABLE_SHOW_LINES = False
# click.rich_click.STYLE_COMMANDS_TABLE_LEADING = 0
click.rich_click.STYLE_COMMANDS_TABLE_PAD_EDGE = True
click.rich_click.STYLE_COMMANDS_TABLE_PADDING = (0, 1)
# click.rich_click.STYLE_COMMANDS_TABLE_BOX = ""
# click.rich_click.STYLE_COMMANDS_TABLE_ROW_STYLES = None
# click.rich_click.STYLE_COMMANDS_TABLE_BORDER_STYLE = None
# click.rich_click.STYLE_COMMANDS_TABLE_COLUMN_WIDTH_RATIO = (None, None)
# click.rich_click.STYLE_ERRORS_PANEL_BORDER = "red"
# click.rich_click.STYLE_ERRORS_PANEL_BOX = "ROUNDED"
# click.rich_click.ALIGN_ERRORS_PANEL = "left"
# click.rich_click.STYLE_ERRORS_SUGGESTION = "dim"
# click.rich_click.STYLE_ERRORS_SUGGESTION_COMMAND = "blue"
# click.rich_click.STYLE_ABORTED = "red"
# click.rich_click.WIDTH = int(getenv("TERMINAL_WIDTH")) if getenv("TERMINAL_WIDTH") else None
# click.rich_click.MAX_WIDTH = int(getenv("TERMINAL_WIDTH")) if getenv("TERMINAL_WIDTH") else WIDTH
# click.rich_click.COLOR_SYSTEM = "auto"  # Set to None to disable colors
# click.rich_click.FORCE_TERMINAL = True if getenv("GITHUB_ACTIONS") or getenv("FORCE_COLOR") or getenv("PY_COLORS") else None

# Fixed strings
# click.rich_click.HEADER_TEXT = None
# click.rich_click.FOOTER_TEXT = None
# click.rich_click.DEPRECATED_STRING = "(Deprecated) "
# click.rich_click.DEFAULT_STRING = "[default: {}]"
# click.rich_click.ENVVAR_STRING = "[env var: {}]"
# click.rich_click.REQUIRED_SHORT_STRING = "*"
# click.rich_click.REQUIRED_LONG_STRING = "[required]"
# click.rich_click.RANGE_STRING = " [{}]"
# click.rich_click.APPEND_METAVARS_HELP_STRING = "({})"
# click.rich_click.ARGUMENTS_PANEL_TITLE = "Arguments"
# click.rich_click.OPTIONS_PANEL_TITLE = "Options"
# click.rich_click.COMMANDS_PANEL_TITLE = "Commands"
# click.rich_click.ERRORS_PANEL_TITLE = "Error"
click.rich_click.ERRORS_SUGGESTION = "Tip: 可在当前命令后面追加 '--help' 以查看使用说明\n"
click.rich_click.ERRORS_EPILOGUE = "如需了解更多信息，请访问 [link=https://xxx.yyy.zz]https://xxx.yyy.zz[/link]"
# click.rich_click.ABORTED_TEXT = "Aborted."

# Behaviours
click.rich_click.SHOW_ARGUMENTS = True  # Show positional arguments
# click.rich_click.SHOW_METAVARS_COLUMN = True  # Show a column with the option metavar (eg. INTEGER)
# click.rich_click.APPEND_METAVARS_HELP = False  # Append metavar (eg. [TEXT]) after the help text
# click.rich_click.GROUP_ARGUMENTS_OPTIONS = False  # Show arguments with options instead of in own panel
# click.rich_click.OPTION_ENVVAR_FIRST = False  # Show env vars before option help text instead of avert
# click.rich_click.TEXT_MARKUP = "ansi"  # One of: "rich", "markdown", "ansi", None.
click.rich_click.USE_RICH_MARKUP = True
click.rich_click.USE_MARKDOWN = True
# click.rich_click.USE_MARKDOWN_EMOJI = True  # Parse emoji codes in markdown :smile:
# click.rich_click.COMMAND_GROUPS = {}  # Define sorted groups of panels to display subcommands
# click.rich_click.OPTION_GROUPS = {}  # Define sorted groups of panels to display options and arguments
# click.rich_click.USE_CLICK_SHORT_HELP = False  # Use click's default function to truncate help text


# click 命令行上下文设置
CONTEXT_SETTINGS = dict(
    help_option_names=['-h', '--help'],
    ignore_unknown_options=True,
    token_normalize_func=lambda x: x.lower(),  # 将命令行中输入的选项名 转换为小写，详见 https://click.palletsprojects.com/en/stable/advanced/#token-normalization
)
