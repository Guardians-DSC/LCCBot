import requests 
from bs4 import BeautifulSoup
from datetime import date

def date_decode(date):
    day = "%s/%s/%s" % (date[6:8], date[4:6], date[0:4])
    hour = "%02d:%s" % (int(date[9:11]) - 3, date[11:13])
    return [day, hour]

def get_events(site):
    page = requests.get(site)
    soup = BeautifulSoup(page.content, 'lxml')

    events = []
    courses = soup.find_all('a', attrs={'class': 'event-link'})

    for name in courses:
        print(name)
        getcourseurl = lambda name: "https://calendar.google.com/calendar/" + name['href']
        page = BeautifulSoup(requests.get(getcourseurl(name)).content, 'lxml')
        event = { 'course': page.title.text }

        for time in page.find_all('time'):
            event[time.attrs['itemprop']] = date_decode(time['datetime'])

        events.append(event)
    return events 

def SpecificEvent(events, day):
    new_event = [event for event in events if event['startDate'][0] == day]
    return new_event

def SiteUrl():
    curr_year = date.today().year
    curr_month = date.today().month

    startdate = str(curr_year) + str(curr_month) + '01'
    enddate = str(curr_year) + str(1 + curr_month) + '01'

    if curr_month == 12:
        enddate = str(curr_year) + '01' + '01'    
    return '%s/%s'%(startdate,enddate)



