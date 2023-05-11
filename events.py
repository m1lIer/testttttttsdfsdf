from PIL import Image, ImageDraw, ImageFont
import os
from disnake.ext import commands
import disnake
import datetime
class Events(commands.Cog):
    def __init__(self, bot):
            self.bot = bot  
    @commands.Cog.listener()
    async def on_ready(self):
        print("\033[35m\nEVENTS LOADED\033[0m")
    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = {
                "description": "**Зачем дверь на сервере выбил? Я же пошутил про залёт с двух ног (...**\n\n**Активность на сервере появляется к 22:00 по МСК 💨**\n\n **Основные:**\n``/report`` — Жалоба на человека\n``/help`` — Помощь умственно отсталым\n``/server`` — Информация о сервере\n\n**Чат команды:**\nДоступны только в <#856962982948503562>\n``/ударить`` — Ударить человека\n``/обнять`` — Обнять человека\n``/поцеловать`` — Поцеловать человека\n``/укусить`` — Укусить человека\n``/заплакать`` — Заплакать\n``/убить`` — Убить человека\n``/улыбнуться`` — Улыбнуться\n``/пощечина`` — Дать пощечину человеку\n``/тыкнуть`` — Тыкнуть человека\n``/погладить`` — Погладить человека\n``/приветствие`` — Поздороваться с человеком\n``/подмигнуть`` — Подмигнуть человеку\n``/накормить`` — Накормить человека\n\n**Музыкальные команды:**\nДоступны только в <#953731239112736818>\n``/play`` — Воспроизвести трек\n``/skip`` — Остановить проигрывание трека\n``/volume`` — Изменить громкость бота(Доступ от Модератора и выше)\n``/leave`` — Выгнать бота из голосового канала\n``/pause`` — Поставить бота на паузу\n``/resume`` — Продолжить проигрывание трека\n",
                "color": 11862271,
                "author": {
                "name": "Доступные команды",
                "url": "https://нахуйтынажал.ru"
                        },
                 
                "components": [
                {
                    "type": 1,
                    "components": [
                        {
                            "type": 2,
                            "style": 5,
                            "url": "https://t.me/sbcommunityds",
                            "label": "Telegram чат сервера"
                        }
                    ]
                }
                ]
        }
                
        buttons = disnake.ui.View()
        buttons.add_item(disnake.ui.Button(style=disnake.ButtonStyle.secondary, url = "https://t.me/sbcommunityds", label = "Telegram чат сервера"))        
        #user = await self.bot.fetch_user(inter.author.id)
        #await user.send(embed = disnake.Embed.from_dict(embed))
        #await inter.response.send_message("Посмотри в лс!)", ephemeral = True)
        await member.send(embed = disnake.Embed.from_dict(embed), view=buttons)


        print("LEAVE")
        image = Image.open("./commands/banner.jpg")
        font = ImageFont.truetype("./commands/AirAmerica.otf", 300)
        drawer = ImageDraw.Draw(image)
        member_coun = member.guild.member_count
        drawer.text((1324, 698), str(member_coun), font=font, fill='#aaf6ff')
        image.save('./commands/ban.jpg')
        file = "./commands/ban.jpg"
        with open(file, 'rb') as image:
            await member.guild.edit(banner=image.read())
        os.remove("./commands/ban.jpg") 
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        
        image = Image.open("./commands/banner.jpg")
        font = ImageFont.truetype("./commands/AirAmerica.otf", 300)
        drawer = ImageDraw.Draw(image)
        member_coun = member.guild.member_count
        drawer.text((1324, 698), str(member_coun), font=font, fill='#aaf6ff')
        image.save('./commands/ban.jpg')
        file = "./commands/ban.jpg"
        with open(file, 'rb') as image:
            await member.guild.edit(banner=image.read())
        os.remove("./commands/ban.jpg")
        embed = {
            "title": "Я тебя спас и в благородство играть не буду: выполнишь                                                      для меня пару заданий — и мы в расчете.",
            "image": {
                "url": "https://cdn.discordapp.com/attachments/1087471217939857470/1104840862778802297/anime-kissin-5.gif"
            },
            "description": "",
            "color": 7254271,
            "content": "https://discord.gg/vV8D5wzWqu"
        }
        print("LEAVE")
        await member.send(embed = disnake.Embed.from_dict(embed)) 
    @commands.Cog.listener()
    async def on_message(self, message):
        f = open('log.txt', 'a')
        today = datetime.datetime.today()
        str = f"\n\033[33m{message.author.name}#{message.author.discriminator} написал(a)\033[0m ({today.strftime('%Y-%m-%d-%H.%M.%S')}): \033[32m{message.content}\033[0m\n"
        f.write(f"\n {message.author.name}#{message.author.discriminator} написал(a) ({today.strftime('%Y-%m-%d-%H.%M.%S')}): {message.content} \n")
        print(str)
def setup(bot):
    bot.add_cog(Events(bot))  