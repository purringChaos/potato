import psutil
import discord
from discord.ext import commands
from dateutil.relativedelta import relativedelta as rd
import time
import uptime
FMT = '{0.days} days {0.hours} hours {0.minutes} minutes {0.seconds} seconds'


def get_system_uptime():
    return FMT.format(rd(seconds=round(uptime.uptime())))


def get_bot_uptime(boot_time):
    return FMT.format(rd(seconds=round(int(time.time()) - int(boot_time))))


class Stats:
    def __init__(self, potato):
        self.potato = potato

    @commands.command()
    async def stats(self, ctx):
        user_name = self.potato.user.name
        avatar_url = 'https://cdn.discordapp.com/avatars/{0}/{1}.jpg'.format(
            self.potato.user.id,
            self.potato.user.avatar
        )

        memory = psutil.virtual_memory()
        used_gib = round(memory.used / 1024 / 1024 / 1024, 2)
        available_gib = round(memory.available / 1024 / 1024 / 1024, 2)
        total_gib = round(memory.total / 1024 / 1024 / 1024, 2)
        memory_pretty = '**In use:** {0} GiB\n**Available:** {1} GiB\n**Total:** {2} GiB'.format(used_gib,
                                                                                                 available_gib,
                                                                                                 total_gib)

        cpu_cores = psutil.cpu_count()
        cpu_load = psutil.cpu_percent()
        cpu_pretty = '**Cores:** {0}\n**Load:** {1}%'.format(cpu_cores, cpu_load)

        embed = discord.Embed()
        embed.set_author(name=user_name, icon_url=avatar_url)
        embed.description = "Hi, I am a bot owned by " + self.potato.owner.name
        embed.add_field(name='**CPU**', value=cpu_pretty)
        embed.add_field(name='**Memory**', value=memory_pretty)
        embed.add_field(name="**System Uptime**", value=get_system_uptime())
        embed.add_field(name="**Bot Uptime**", value=get_bot_uptime(self.potato.boot_time))

        try:
            embed.add_field(name="**Battery**", value="{}%".format(round(psutil.sensors_battery().percent)))
        except:
            pass

        await ctx.send(embed=embed)


def setup(potato):
    potato.setup_module(Stats(potato))