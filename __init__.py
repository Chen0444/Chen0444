from hoshino import Service
from .gacha import gacha_10 , gacha_info

sv = Service('原神抽卡')


@sv.on_prefix(["相遇之缘"], only_to_me=True)
async def gacha_(bot, ev):
    await bot.send(ev, gacha_10() , at_sender=True)

@sv.on_prefix(["原神卡池","原神up","原神UP"], only_to_me=True)
async def gacha_(bot, ev):
    await bot.send(ev, gacha_info() , at_sender=True)
