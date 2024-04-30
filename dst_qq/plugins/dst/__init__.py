from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters import Message
from nonebot.params import CommandArg
import httpx

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="dst",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)

dst = on_command("dst", rule=to_me(), aliases={"饥荒"}, priority=10, block=True)


@dst.handle()
async def handle_function(args: Message = CommandArg()):
    location = args.extract_plain_text()
    if not location:
        await dst.finish("请输入指令")
    elif location == "status":
        res = httpx.get("http://xxx.xxx.xx/api/dontstarve/status")
        await dst.finish(res.text)

