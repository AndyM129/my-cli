import rich_click as click


# 命令别名：https://click.palletsprojects.com/en/stable/extending-click/#command-aliases
# 自定义组：https://click.palletsprojects.com/en/stable/extending-click/#custom-groups
class AliasedGroup(click.RichGroup):
    """
    自定义 click 命令组，以支持命令别名

    参考文档: https://www.bookstack.cn/read/click-docs-zh-cn/10.md#%E5%91%BD%E4%BB%A4%E5%88%AB%E5%90%8D
    """

    def get_command(self, ctx, cmd_name):
        rv = click.Group.get_command(self, ctx, cmd_name)
        if rv is not None:
            return rv

        matches = [
            x for x in self.list_commands(ctx)
            if x.startswith(cmd_name)
        ]

        if not matches:
            return None

        if len(matches) == 1:
            return click.Group.get_command(self, ctx, matches[0])

        ctx.fail('Too many matches: %s' % ', '.join(sorted(matches)))
