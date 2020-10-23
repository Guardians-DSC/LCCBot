import paramiko
import requests 
from bs4 import BeautifulSoup
from datetime import date
from ..services.testes import *


def scheduleService():
  LCC1 = []
  LCC2 = [ ]
  LCC3 = []
  return {"LCC1": LCC1, "LCC2": LCC2, "LCC3": LCC3}

site =  {"LCC1": "https://calendar.google.com/calendar/u/0/htmlembed?src=computacao.ufcg.edu.br_9u9fch5o55dbgrschdeduq348c@group.calendar.google.com&dates=" + SiteUrl(),
"LCC2": "https://calendar.google.com/calendar/u/0/htmlembed?src=computacao.ufcg.edu.br_80qc5chl59nmv2268aef8hp528@group.calendar.google.com&dates=" + SiteUrl(),
"LCC3": "https://calendar.google.com/calendar/u/0/htmlembed?src=computacao.ufcg.edu.br_noalttgqttm3c5pm94k3ttbj1k@group.calendar.google.com&dates=" + SiteUrl() }


events = get_events(site)
today = date.today()
curr_day = today.strftime('%d/%m/%Y')
new_event = SpecificEvent(events, curr_day)

LCC1 = new_event
LCC2 = new_event
LCC3 = new_event