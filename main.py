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
        await client.send_message(message.channel,"https://github.com/Keyditor/Monster-Bot/raw/master/imagens/garuga.jpg")
        await client.send_message(message.channel,monsters.char.yiangaruga)
    if message.content.lower().startswith(pref + monster + ' gypceros'):
        await client.send_message(message.channel,"**Analise de Monstro...**")
        await client.send_message(message.channel,"https://github.com/Keyditor/Monster-Bot/raw/master/imagens/gypceros.jpg")
        await client.send_message(message.channel,monsters.char.gypceros)
    if message.content.lower().startswith(pref + monster + ' purple gypceros'):
        await client.send_message(message.channel,"**Analise de Monstro...**")
        await client.send_message(message.channel,"https://github.com/Keyditor/Monster-Bot/raw/master/imagens/purplegypceros.jpg")
        await client.send_message(message.channel,monsters.char.purplegypceros)
    if message.content.lower().startswith(pref + monster + ' hypnocatrice'):
        await client.send_message(message.channel,"**Analise de Monstro...**")
        await client.send_message(message.channel,"https://github.com/Keyditor/Monster-Bot/raw/master/imagens/hypnocatrice.jpg")
        await client.send_message(message.channel,monsters.char.hypnocatrice)
    if message.content.lower().startswith(pref + monster + ' rathian'):
        await client.send_message(message.channel,"**Analise de Monstro...**")
        await client.send_message(message.channel,"https://github.com/Keyditor/Monster-Bot/raw/master/imagens/rathian.jpg")
        await client.send_message(message.channel,monsters.char.rathian)
    if message.content.lower().startswith(pref + monster + ' pink rathian'):
        await client.send_message(message.channel,"**Analise de Monstro...**")
        await client.send_message(message.channel,"https://github.com/Keyditor/Monster-Bot/raw/master/imagens/pinkrathian.jpg")
        await client.send_message(message.channel,monsters.char.pinkrathian)
    if message.content.lower().startswith(pref + monster + ' gold rathian'):
        await client.send_message(message.channel,"**Analise de Monstro...**")
        await client.send_message(message.channel,"https://github.com/Keyditor/Monster-Bot/raw/master/imagens/goldrathian.jpg")
        await client.send_message(message.channel,monsters.char.goldrathian)




#client.run(BOTCODE)
client.run('NDEzNzk0ODU0NzAzOTg4NzM3.DWeAAw.9UAZRNxAZgHgP5gDM-wBnlXlA4c')
