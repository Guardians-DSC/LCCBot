import discord
import requests 

client = discord.Client()

@client.event
async def on_ready():
    print("Efetuamos o login como {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Hello'):
        await message.channel.send('Hello!')
    if message.content.lower().startswith('!horarios'):
        mensagem = message.content
        instrução = '!horarios'
        args = mensagem[len(instrução) + 1:].split(' ')


        req_ping = requests.get('http://127.0.0.1:5000/ping')
        req_schedule = requests.get('http://127.0.0.1:5000/schedule')
        dic= req_schedule.json()

        embed= discord.Embed(title="LCC Bot", descripition="Aulas do dia:")

        for lcc in dic.keys():
            if lcc.lower() in args or len(args):
                if len(dic[lcc]) == 0:
                    embed.add_field(name = lcc.upper(), value="Hoje não haverá aula", inline= False)
                for aula in dic[lcc]:
                    embed.add_field(name = lcc.upper(), value=("Hoje tem aula de %s ás %s horas.\n" %(aula['course'], aula['startTime'])), inline= False)

        embed.set_footer(text="Guardians-DSC")

        await message.channel.send(embed=embed)

client.run("NzU0ODQ3ODI4Mjk5NDgxMDg4.X16s0g.5BBgr0DusyZ0CxLL4O_rsuvwoj4")