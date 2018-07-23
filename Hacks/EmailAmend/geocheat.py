import requests
import re
from bs4 import BeautifulSoup
import html

TEKEN = 9.25

class entry():
    def __init__(self, date, starttime='', endtime='', tottime='', usdata=[]):
        self.date = date
        self.usdata = usdata
        self.tottime = ''

    def calc_days(self):
        if len(self.usdata) > 3:
            self.tottime = self.usdata[3]


headers = {
    'Origin': 'https://www.tlushim.co.il',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8,he;q=0.6',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.0.10802 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Referer': 'https://www.tlushim.co.il/',
    'Connection': 'keep-alive',
    }
data = 'id_num=066377466&password=ofueky&connect='
r = requests.post('https://www.tlushim.co.il/login.php', headers=headers, data=data)
sitedata = r.content
soup = BeautifulSoup(sitedata, 'html.parser')
agg = soup.findAll('td', attrs={'class': 'atnd'})
nagg = []
for ag in agg:
    if ag.text not in [' ', '']:
        nagg.append(ag.text)
entry_data = []
entries = []
entry_date = ''
for nag in nagg:
    if re.findall('\d{2}\/\d{2}\/\d{2}', nag):
        if entry_date and entry_data:
            new_entry = entry(entry_date, usdata=entry_data)
            entries.append(new_entry)
            entry_date = ''
            entry_data = []
        entry_date = nag
    else:
        entry_data.append(nag)
tot_done = float()
tot_need = float()
for entri in entries:
    entri.calc_days()
    if entri.tottime:
        tot_done += float(entri.tottime)
        tot_need += TEKEN
days = int(tot_need/TEKEN)
differe = tot_done-tot_need
pass