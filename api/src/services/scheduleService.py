import requests
from bs4 import BeautifulSoup
from datetime import date


def date_decode(date):
    day = "%s/%s/%s" % (date[6:8], date[4:6], date[0:4])
    hour = "%02d:%s" % (int(date[9:11]) - 3, date[11:13])
    return [day, hour]


def get_events(site):
    page = requests.get(site)
    soup = BeautifulSoup(page.content, "lxml")

    events = []
    courses = soup.find_all("a", attrs={"class": "event-link"})

    for name in courses:
        getcourseurl = (
            lambda name: "https://calendar.google.com/calendar/" + name["href"]
        )
        page = BeautifulSoup(requests.get(getcourseurl(name)).content, "lxml")
        event = {"course": page.title.text}

        for time in page.find_all("time"):
            event[time.attrs["itemprop"]] = date_decode(time["datetime"])

        events.append(event)
    return events


def SpecificEvent(events, day):
    new_event = [event for event in events if event["startDate"][0] == day]
    return new_event


def SiteUrl():
    curr_year = date.today().year
    curr_month = date.today().month

    startdate = "%d%02d01" % (curr_year, curr_month)
    enddate = "%d%02d01" % (curr_year, curr_month + 1)

    if curr_month == 12:
        enddate = str(curr_year) + "01" + "01"
    return "%s/%s" % (startdate, enddate)


def scheduleService():
    sites = {
        "LCC1": "https://calendar.google.com/calendar/u/0/htmlembed?src=computacao.ufcg.edu.br_9u9fch5o55dbgrschdeduq348c@group.calendar.google.com&dates="
        + SiteUrl(),
        "LCC2": "https://calendar.google.com/calendar/u/0/htmlembed?src=computacao.ufcg.edu.br_80qc5chl59nmv2268aef8hp528@group.calendar.google.com&dates="
        + SiteUrl(),
        "LCC3": "https://calendar.google.com/calendar/u/0/htmlembed?src=computacao.ufcg.edu.br_noalttgqttm3c5pm94k3ttbj1k@group.calendar.google.com&dates="
        + SiteUrl(),
    }

    dicEvents = {}
    for lcc in sites:
        site = sites[lcc]

        events = get_events(site)
        today = date.today()
        curr_day = today.strftime("%d/%m/%Y")
        new_event = SpecificEvent(events, curr_day)
        dicEvents[lcc] = new_event

    dicEvents2 = {}
    for lcc in dicEvents:
        listaDeAulas = dicEvents[lcc]
        novaListaDeAulas = []
        for aula in listaDeAulas:
            aulaNova = {
                "course": aula["course"],
                "startTime": aula["startDate"][1],
                "endTime": aula["endDate"][1],
            }
            novaListaDeAulas.append(aulaNova)
        dicEvents2[lcc] = novaListaDeAulas

    return dicEvents2
