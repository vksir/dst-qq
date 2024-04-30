import nonebot
from nonebot.adapters.console import Adapter as ConsoleAdapter
from nonebot.adapters.onebot.v11 import Adapter as OnebotV11Adapter

nonebot.init()

driver = nonebot.get_driver()
driver.register_adapter(ConsoleAdapter)
driver.register_adapter(OnebotV11Adapter)

nonebot.load_builtin_plugins("echo")
nonebot.load_plugins("dst_qq/plugins")

if __name__ == "__main__":
    nonebot.run()
