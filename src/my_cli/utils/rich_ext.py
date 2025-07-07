from my_cli.utils.rich_console_ext import *


# def print_debug(*objects, sep=' ', end='\n', file=None, flush=False, style='dim', prefix='[DEBUG]'):
#     """
#     自定义的调试打印方法，基于 rich.print 实现，带有特定样式和前缀。

#     参数:
#         *objects: 要打印的对象
#         sep: 分隔符，默认是空格
#         end: 结束符，默认是换行符
#         file: 输出文件对象，默认为 None（即标准输出）
#         flush: 是否立即刷新输出流，默认为 False
#         style: 文本样式，默认是 'dim'（暗淡）
#         prefix: 调试信息前缀，默认是 '[DEBUG]'
#     """
#     # 获取调用者的文件名和行号（可选，用于更详细的调试信息）
#     frame = inspect.currentframe().f_back
#     filename = frame.f_code.co_filename.split('/')[-1]  # 只取文件名部分
#     lineno = frame.f_lineno

#     # 创建 Rich 的 Console 对象
#     console = Console(file=file)

#     # 构造带前缀和调用位置的调试信息
#     debug_prefix = Text()
#     debug_prefix.append(f"{prefix} {filename}:{lineno} ", style=style)

#     # 将用户传入的对象转换为字符串并组合
#     message = sep.join(str(obj) for obj in objects)

#     # 将前缀和消息合并为一个 Text 对象（可选，如果希望统一样式）
#     full_text = Text()
#     full_text.append(debug_prefix)
#     full_text.append(message, style=style)  # 你也可以给 message 单独设置样式

#     # 使用 rich.print 打印
#     print(full_text, end=end, flush=flush)

#     # 释放 frame 引用，避免引用循环
#     del frame
