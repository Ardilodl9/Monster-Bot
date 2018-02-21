import discord
import asyncio
import monsters

client = discord.Client()
pref = '?'
monster = 'monster'
@client.event
async def on_ready():
    print ('BOT ONLINE - Olá Mundo!')
    print (client.user.name)
    print (client.user.id)
    print ('-------Key-------')

@client.event
async def on_message(message):
    if message.content.lower().startswith(pref+'teste'):
        await client.send_message(message.channel, "AEEEEEE POOORRAAAAAAAAAA! DEU BOM CARAIO! BORA FAZER ESSE BOT JDASLDJASLDJASLDLASDJALSKD")
    if message.content.lower().startswith(pref+'game'):
        await client.change_status(game='Informações no chat')
    if message.content.lower().startswith(pref + monster + ' giadrome'):
        await client.send_message(message.channel,"**Analise de Monstro...**")
        await client.send_message(message.channel,"https://vignette.wikia.nocookie.net/monsterhunter/images/3/31/MHRoC-Giadrome_Card_001.jpg")
        await client.send_message(message.channel,"**```"
                                                  "---------------------------------------------"
                                                  "\n```**"
                                                  "\n**Nome:** Giadrome | Em japonês: ド ス ギ ア ノ ス (Dosugianosu)."
                                                  "\n**Espécie:** Bird Wyvern"
                                                  "\n**Elemento:** :snowflake: Gelo."
                                                  "\n**Status:** :snowman: Boneco de Neve."
                                                  "\n**Fraqueza:** :fire: Fogo."
                                                  "\n**Movimentação:** Move-se andando normalmente, dá saltos para frente, atrás, esqueda e direita."
                                                  "\n**Ataques:** Sempre frontais, Usando as garras, Saltando ou cuspindo gelo."
                                                  "\n**Dicas:** Sempre rolar e atacar lateralmente."
                                                  "\n**Bagagem necessaria:** Nenhuma, apenas as que a missão lhe proporciona."
                                                  "\n"
                                                  "\n**Drops:** Nenhum."
                                                  "\n"
                                                  "\n**Carves:** "
                                                  "\n**--- Corpo ---**"
                                                  "\nGiadrome Claw	53%"
                                                  "\nGiadrome Hide	30%"
                                                  "\nGiaprey Scale	15%"
                                                  "\nGiadrome Skull	2%"
                                                  "\n**-------------**"
                                                  "\n"
                                                  "\n**Recompença de Captura:**"
                                                  "\nGiadrome Hide	56%"
                                                  "\nScreamer x2	39%"
                                                  "\nGiadrome Skull	 5%"
                                                  "\n"
                                                  "\n**```"
                                                  "---------------------------------------------"
                                                  "\n```**"
        )
    if message.content.lower().startswith(pref + monster + ' velocidrome'):
        await client.send_message(message.channel,"**Analise de Monstro...**")
        await client.send_message(message.channel,"https://vignette.wikia.nocookie.net/monsterhunter/images/a/ad/MHRoC-Velocidrome_Card_001.jpg")
        await client.send_message(message.channel,"**```"
                                                  "---------------------------------------------"
                                                  "\n```**"
                                                  "\n**Nome:** Velocidrome | Em japonês: ドスランポス (Dosuranposu)."
                                                  "\n**Espécie:** Bird Wyvern"
                                                  "\n**Elemento:** Nenhum"
                                                  "\n**Status:** Nenhum."
                                                  "\n**Fraqueza:** :zap:  Raio e :snowflake: Gelo."
                                                  "\n**Movimentação:** Move-se andando normalmente, dá saltos para frente, atrás, esqueda e direita."
                                                  "\n**Ataques:** Sempre frontais, Usando as garras ou saltando."
                                                  "\n**Dicas:** Sempre rolar e atacar lateralmente."
                                                  "\n**Bagagem necessaria:** Nenhuma, apenas as que a missão lhe proporciona."
                                                  "\n"
                                                  "\n**Drops:** Nenhum."
                                                  "\n"
                                                  "\n**Carves:** "
                                                  "\n**--- Corpo ---**"
                                                  "\nVelocidrome Claw	53%"
                                                  "\nVelocidrome Hide	30%"
                                                  "\nVelociprey Scale	15%"
                                                  "\nVelocidrome Skull	2%"
                                                  "\n**-------------**"
                                                  "\n"
                                                  "\n**Recompença de Captura:**"
                                                  "\nVelocidrome Hide	56%"
                                                  "\nScreamer x2	    39%"
                                                  "\nVelocidrome Skull	 5%"
                                                  "\n"
                                                  "\n**```"
                                                  "---------------------------------------------"
                                                  "\n```**"
        )
    if message.content.lower().startswith(pref + monster + ' iodrome'):
        await client.send_message(message.channel,"**Analise de Monstro...**")
        await client.send_message(message.channel,"https://vignette.wikia.nocookie.net/monsterhunter/images/0/08/MHRoC-Iodrome_Card_001.jpg")
        await client.send_message(message.channel,"**```"
                                                  "---------------------------------------------"
                                                  "\n```**"
                                                  "\n**Nome:** Iodrome | Em japonês: ドスイーオス (Dosuiosu)."
                                                  "\n**Espécie:** Bird Wyvern"
                                                  "\n**Elemento:** Nenhum."
                                                  "\n**Status:** :snake: Envenenamento."
                                                  "\n**Fraqueza:** :zap:  Raio e :droplet: Água."
                                                  "\n**Movimentação:** Move-se andando normalmente, dá saltos para frente, atrás, esqueda e direita."
                                                  "\n**Ataques:** Sempre frontais, Usando as garras, Saltando ou cuspindo Veneno."
                                                  "\n**Dicas:** Sempre rolar e atacar lateralmente."
                                                  "\n**Bagagem necessaria:** Nenhuma, apenas as que a missão lhe proporciona."
                                                  "\n"
                                                  "\n**Drops:** Nenhum."
                                                  "\n"
                                                  "\n**Carves:** "
                                                  "\n**--- Corpo ---**"
                                                  "\nIodrome Hide	48%"
                                                  "\nPoison Sac 	35%"
                                                  "\nIoprey Scale	15%"
                                                  "\nIodrome Skull	2%"
                                                  "\n**-------------**"
                                                  "\n"
                                                  "\n**Recompença de Captura:**"
                                                  "\nIodrome Hide	56%"
                                                  "\nPoison Sac x2  39%"
                                                  "\nIodrome Skull	 5%"
                                                  "\n"
                                                  "\n**```"
                                                  "---------------------------------------------"
                                                  "\n```**"
        )
    if message.content.lower().startswith(pref + monster + ' gendrome'):
        await client.send_message(message.channel,"**Analise de Monstro...**")
        await client.send_message(message.channel,"https://vignette.wikia.nocookie.net/monsterhunter/images/3/3d/MHRoC-Gendrome_Card_001.jpg")
        await client.send_message(message.channel,"**```"
                                                  "---------------------------------------------"
                                                  "\n```**"
                                                  "\n**Nome:** Gendrome | Em japonês: ドスゲネポス (Dosugeneposu)."
                                                  "\n**Espécie:** Bird Wyvern"
                                                  "\n**Elemento:** Nenhum"
                                                  "\n**Status:** :part_alternation_mark: Paralisia."
                                                  "\n**Fraqueza:** :droplet: Água e :snowflake: Gelo."
                                                  "\n**Movimentação:** Move-se andando normalmente, dá saltos para frente, atrás, esqueda e direita."
                                                  "\n**Ataques:** Sempre frontais, Usando as garras ou saltando ( o salto pode causar o Status )."
                                                  "\n**Dicas:** Sempre rolar e atacar lateralmente."
                                                  "\n**Bagagem necessaria:** Nenhuma, apenas as que a missão lhe proporciona."
                                                  "\n"
                                                  "\n**Drops:** Nenhum."
                                                  "\n"
                                                  "\n**Carves:** "
                                                  "\n**--- Corpo ---**"
                                                  "\nGendrome Hide	48%"
                                                  "\nParalysis Sac	35%"
                                                  "\nGenprey Scale	15%"
                                                  "\nGendrome Skull	 2%"
                                                  "\n**-------------**"
                                                  "\n"
                                                  "\n**Recompença de Captura:**"
                                                  "\nGendrome Hide	    56%"
                                                  "\nParalysis Sac x2	39%"
                                                  "\nGendrome Skull	     5%"
                                                  "\n"
                                                  "\n**```"
                                                  "---------------------------------------------"
                                                  "\n```**"
        )
    if message.content.lower().startswith(pref + monster + ' yian kut-ku'):
        await client.send_message(message.channel,"**Analise de Monstro...**")
        await client.send_message(message.channel,"https://vignette.wikia.nocookie.net/monsterhunter/images/e/e2/MHRoC-Yian_Kut-Ku_Card_001.jpg")
        await client.send_message(message.channel,"**```"
                                                  "---------------------------------------------"
                                                  "\n```**"
                                                  "\n**Nome:** Yian Kut-Ku | Em japonês: イャンクック (Iyankukku)."
                                                  "\n**Espécie:** Bird Wyvern."
                                                  "\n**Elemento:** :fire: Fogo."
                                                  "\n**Status:** :fire: Queimadura."
                                                  "\n**Fraqueza:** :droplet: Água (Nas Asas) e :snowflake: Gelo (Na Cabeça)."
                                                  "\n**Movimentação:** Move-se andando normalmente ou Voando."
                                                  "\n**Ataques:** Frontais bicando, correndo ou jogando bolas de fogo. Laterais bicando e dando rabadas. Algumas vezes decolando e dando rasantes"
                                                  "\n**Dicas:** Quebre as orelhas com uma Greatsword ou similar, em baixo do pescoço é um ponto cego! Abuse disso para dar o maior dano possivel, mas tome cuidado com ataques giratorios."
                                                  "\n**Bagagem necessaria:** Nenhuma, Nem mesmo as que a missão lhe proporciona! Afinal é só um Kut-ku: :Leo: ."
                                                  "\n"
                                                  "\n**Drops:** (Usando Sonic Bomb na sua frente)"
                                                  "\nWyvern Tears	74%"
                                                  "\nKut-Ku Scale	16%"
                                                  "\nKut-Ku Ear	    10%"
                                                  "\n"
                                                  "\n**Carves:** "
                                                  "\n**--- Corpo ---**"
                                                  "\nKut-Ku Shell	40%"
                                                  "\nKut-Ku Webbing	37%"
                                                  "\nKut-Ku Scale	20%"
                                                  "\nGiant Beak	     3%"
                                                  "\n**-------------**"
                                                  "\n"
                                                  "\n**Recompença de Captura:**"
                                                  "\nKut-Ku Shell	33%"
                                                  "\nScreamer	24%"
                                                  "\nMed Monster Bone x2	20%"
                                                  "\nFlame Sac	20%"
                                                  "\nGiant Beak	3%"
                                                  "\n"
                                                  "\n**Recompensas de Feridas:**"
                                                  "\nOrelhas: "
                                                  "\n        Kut-Ku Ear	        50%"
                                                  "\n        Kut-Ku Scale x3	42%"
                                                  "\n"
                                                  "\n**```"
                                                  "---------------------------------------------"
                                                  "\n```**"
        )
    if message.content.lower().startswith(pref + monster + ' blue yian kut-ku'):
        await client.send_message(message.channel,"**Analise de Monstro...**")
        await client.send_message(message.channel,"https://orig00.deviantart.net/6fb6/f/2018/046/4/1/pink_fatalis_scan_41_by_keyditor-dc39f2d.jpg")
        await client.send_message(message.channel,monsters.char.blueyiankutku)
    if message.content.lower().startswith(pref + monster + ' yian garuga'):
        await client.send_message(message.channel,"**Analise de Monstro...**")
        await client.send_message(message.channel,"https://vignette.wikia.nocookie.net/monsterhunter/images/c/c5/MHRoC-Yian_Garuga_Card_001.jpg")
        await client.send_message(message.channel,monsters.char.yiangaruga)





client.run('NDEzNzk0ODU0NzAzOTg4NzM3.DWeAAw.9UAZRNxAZgHgP5gDM-wBnlXlA4c')
