import click
from example_blog.config import settings
from example_blog.server import Server

"""
使用@click.group装饰器创建一个命令组，invoke_without_command=True表示如果没有指定子命令，则调用main函数
使用@click.pass_context装饰器将上下文传递给main函数
使用@click.option装饰器定义一个--version选项，用于显示版本信息
main函数根据是否指定了--version选项来打印版本信息或打印帮助信息
"""
@click.group(invoke_without_command=True)
@click.pass_context
@click.option('-V', '--version', is_flag=True, help='Show version and exit.')
def main(ctx, version):
    if version:
        click.echo(__version__)
    elif ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())

"""
使用@click.group装饰器创建一个命令组，invoke_without_command=True表示如果没有指定子命令，则调用main函数
使用@click.pass_context装饰器将上下文传递给main函数
使用@click.option装饰器定义一个--version选项，用于显示版本信息
main函数根据是否指定了--version选项来打印版本信息或打印帮助信息
"""
@main.command()
@click.option('-h', '--host', show_default=True, help=f'Host IP. Default: {settings.HOST}')
@click.option('-p', '--port', show_default=True, type=int, help=f'Port. Default: {settings.PORT}')
@click.option('--level', help='Log level')
def server(host, port, level):
    """Start server."""
    kwargs = {
        'LOGLEVEL': level,
        'HOST': host,
        'PORT': port,
    }
    for name, value in kwargs.items():
        if value:
            settings.set(name, value)

    Server().run()