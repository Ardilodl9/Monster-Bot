import discord
import asyncio
import monsters

client = discord.Client()
pref = '?'
monster = 'monster'
print('Starting MonsterBot!')
print('enter bot Token: ')
BOTCODE = input()
print('Now wait i am connecting...')
@client.event
async def on_ready():
    print ('BOT ONLINE - I AM READY!')
    print (client.user.name)
    print (client.user.id)
    print ('-------Created by: JOGANDO-------')
    print ('-------   is.gd/JOGANDO   -------')

@client.event
async def on_message(message):
    if message.content.lower().startswith(pref+'teste'):
        await client.send_message(message.channel, "AEEEEEE POOORRAAAAAAAAAA! DEU BOM CARAIO! BORA FAZER ESSE BOT JDASLDJASLDJASLDLASDJALSKD")
    if message.content.lower().startswith(pref+'game'):
        await client.change_status(game='Informações no chat')
    if message.content.lower().startswith(pref + monster + ' giadrome'):
        await client.send_message(message.channel,"**Analise de Monstro...**")
        await client.send_message(message.channel,"https://github.com/Keyditor/Monster-Bot/raw/master/imagens/giadrome.jpg")
        await client.send_message(message.channel,monsters.char.giadrome)
    if message.content.lower().startswith(pref + monster + ' velocidrome'):
        await client.send_message(message.channel,"**Analise de Monstro...**")
        await client.send_message(message.channel,"https://github.com/Keyditor/Monster-Bot/raw/master/imagens/velocidrome.jpg")
        await client.send_message(message.channel,monsters.char.velocidrome)
    if message.content.lower().startswith(pref + monster + ' iodrome'):
        await client.send_message(message.channel,"**Analise de Monstro...**")
        await client.send_message(message.channel,"https://github.com/Keyditor/Monster-Bot/raw/master/imagens/iodrome.jpg")
        await client.send_message(message.channel,monsters.char.iodrome)
    if message.content.lower().startswith(pref + monster + ' gendrome'):
        await client.send_message(message.channel,"**Analise de Monstro...**")
        await client.send_message(message.channel,"https://github.com/Keyditor/Monster-Bot/raw/master/imagens/gendrome.jpg")
        await client.send_message(message.channel,monsters.char.gendrome)
    if message.content.lower().startswith(pref + monster + ' yian kut-ku'):
        await client.send_message(message.channel,"**Analise de Monstro...**")
        await client.send_message(message.channel,"https://github.com/Keyditor/Monster-Bot/raw/master/imagens/yiankutku.jpg")
        await client.send_message(message.channel,monsters.char.yiankutku)
    if message.content.lower().startswith(pref + monster + ' blue yian kut-ku'):
        await client.send_message(message.channel,"**Analise de Monstro...**")
        await client.send_message(message.channel,"https://github.com/Keyditor/Monster-Bot/raw/master/imagens/bluekutku.jpg")
        await client.send_message(message.channel,monsters.char.blueyiankutku)
    if message.content.lower().startswith(pref + monster + ' yian garuga'):
        await client.send_message(message.channel,"**Analise de Monstro...**")
        await client.send_message(message.channel,"https://vignette.wikia.nocookie.net/monsterhunter/images/c/c5/MHRoC-Yian_Garuga_Card_001.jpg")
        await client.send_message(message.channel,monsters.char.yiangaruga)




client.run(BOTCODE)
#client.run('NDEzNzk0ODU0NzAzOTg4NzM3.DWeAAw.9UAZRNxAZgHgP5gDM-wBnlXlA4c')
