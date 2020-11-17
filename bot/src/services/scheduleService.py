import requests
import discord


def horarios(mensagem, args):
    instrucao = "!horarios"

    req_schedule = requests.get("https://lcc-bot-mvp.herokuapp.com/schedule")
    dic = req_schedule.json()

    embed = discord.Embed(title="LCC Bot", descripition="Aulas do dia:")
    shouldCheckLcc = lambda lcc: lcc.lower() in args or len(args) == 0

    for lcc in dic:
        if shouldCheckLcc(lcc):
            aulas = _getAulasByLcc(lcc, dic)
            embed.add_field(name=lcc.upper(), value=(aulas), inline=False)

    embed.set_footer(text="Guardians-DSC")
    return embed


def _getAulasByLcc(lcc, dic):
    aulas = ""
    if len(dic[lcc]) == 0:
        aulas += " - Hoje não haverá aula"
    else:
        aulas = ""
        for aula in dic[lcc]:
            aulas += " - Hoje tem aula de %s ás %s horas.\n\n" % (
                aula["course"],
                aula["startTime"],
            )
    return aulas