
Save New Duplicate & Edit Just Text 1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
import discord
from discord.ext import commands
import os
import sys
import inspect
import io
import textwrap
import traceback
from contextlib import redirect_stdout

bot = commands.Bot(command_prefix=commands.when_mentioned_or('_'))
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Logged in as " + str(bot.user))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.guild is None:
        await bot.process_commands(message)

@bot.command(name='eval')
async def _eval(ctx, *, body):
    env = {'__builtins__': {}}
    body = cleanup_code(body)
    stdout = io.StringIO()
    err = out = None

    to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

    try:
        exec(to_compile, env)
    except Exception as e:
        err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
        return

    func = env['func']
    try:
        with redirect_stdout(stdout):
            ret = await func()
    except Exception as e:
        value = stdout.getvalue()
        err = await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
    else:
        value = stdout.getvalue()
        if ret is None:
            if value:
                out = await ctx.send(f'```py\n{value}\n```')
        else:
            bot._last_result = ret
            out = await ctx.send(f'```py\n{value}{ret}\n```')

def cleanup_code(content):
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])

    return content.strip('` \n')

def get_syntax_error(e):
    if e.text is None:
        return f'```py\n{e.__class__.__name__}: {e}\n```'
    return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'

bot.run("token", reconnect=True)
