import discord
import asyncio
import monsters
from pathlib import Path

client = discord.Client()
pref = '?'
monster = 'monster '
#print('Starting MonsterBot!')
#print('enter bot Token: ')
#BOTCODE = input()
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
    await client.change_presence(game=discord.Game(name='Informações aos Caçadores!'))
    if message.content.lower().startswith(pref+'teste'):
        await client.send_message(message.channel, "AEEEEEE POOORRAAAAAAAAAA! DEU BOM CARAIO! BORA FAZER ESSE BOT JDASLDJASLDJASLDLASDJALSKD")
    if message.content.lower().startswith(pref+'game'):
        await client.change_presence(game=discord.Game(name='Informações aos Caçadores!'))
    if message.content.lower().startswith(pref + monster):
        msg = message.content.lower()
        monstername = msg.replace('?monster ','')
        testfile = Path("monsters/"+monstername+".txt")
        print ("/monsters/"+monstername+".txt")
        if testfile.is_file():
            monsterfile = open('monsters/'+monstername+'.txt','r',encoding='utf8', errors='ignore')
            monsterinfo = monsterfile.read()
            print ("informação requerida sobre: "+monstername)
            await client.send_message(message.channel,"**Analise de Monstro...**")
            await client.send_message(message.channel,"https://github.com/Keyditor/Monster-Bot/raw/master/imagens/"+monstername+".jpg")
            await client.send_message(message.channel,monsterinfo)
            monsterfile.close()
        else:
            print ('error!!')
            await client.send_message(message.channel,"ERROR 404 Monstro não encontrado")
            await client.send_message(message.channel,"Verifique se digitou corretamente o nome do monstro!")

### Old code for send monster's info
"""   if message.content.lower().startswith(pref + monster + ' velocidrome'):
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
        await client.send_message(message.channel,"https://github.com/Keyditor/Monster-Bot/raw/master/imagens/yian kutku.jpg")
        await client.send_message(message.channel,monsters.char.yiankutku)
    if message.content.lower().startswith(pref + monster + ' blue yian kut-ku'):
        await client.send_message(message.channel,"**Analise de Monstro...**")
        await client.send_message(message.channel,"https://github.com/Keyditor/Monster-Bot/raw/master/imagens/blue yian kut-ku.jpg")
        await client.send_message(message.channel,monsters.char.blueyiankutku)
    if message.content.lower().startswith(pref + monster + ' yian garuga'):
        await client.send_message(message.channel,"**Analise de Monstro...**")
        await client.send_message(message.channel,"https://github.com/Keyditor/Monster-Bot/raw/master/imagens/yian garuga.jpg")
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
        await client.send_message(message.channel,"https://github.com/Keyditor/Monster-Bot/raw/master/imagens/pink rathian.jpg")
        await client.send_message(message.channel,monsters.char.pinkrathian)
    if message.content.lower().startswith(pref + monster + ' gold rathian'):
        await client.send_message(message.channel,"**Analise de Monstro...**")
        await client.send_message(message.channel,"https://github.com/Keyditor/Monster-Bot/raw/master/imagens/gold rathian.jpg")
        await client.send_message(message.channel,monsters.char.goldrathian)
"""



with open('Bot-Token.txt', 'r') as BotTokenTxt:
    BotToken= BotTokenTxt.read()
client.run(BotToken)

