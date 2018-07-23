import bs4

class af_item():
    def __init__(self, title, content, timestamp):
        self.title = title
        self.content = content
        self.timestamp = timestamp

def gettimedifference(basehour, acthour, baseminute , actminute):
    diffacthour = basehour - acthour
    diffactminute = baseminute - actminute
    if diffactminute < 0:
        diffacthour = diffacthour - 1
        diffactminute = diffactminute + 60
    outtime = '{0}:{1}'.format(diffacthour, diffactminute)
    return outtime

def ack_units(timeagg):
    temphour = 0
    tempminute = 0
    for time_measure in timeagg:
        unit = time_measure[-1]
        if unit == 'm':
            tempminute = int(time_measure[:-1])
        if unit == 'h':
            temphour = temphour + int(time_measure[:-1])
        if unit == 'd':
            temphour = temphour + (24 * int(time_measure[:-1]))
        if unit == 'w':
            temphour = temphour + (144 * int(time_measure[:-1]))
    return temphour, tempminute

fff = open(r"D:\zaf\CloudShell - Full Activity Feed.html")
abc = bs4.BeautifulSoup(fff, "html.parser")
qqq = abc.find_all('div', {"class": "cell"})
activity = []
output = 'Title, Content, time for action, time from start \n'
for item in qqq:
    plp = item.find_all('span')
    title = plp[1].find("span")['data-full-text']
    if "live status" not in title:
        title = str(title).replace("\n", "").replace(",", "")
        content = plp[2]['data-full-text']
        content = str(content).replace("\n", "").replace(",", "")
        timestamp = plp[3].contents[0].split()[0]
        activity.append(af_item(title, content, timestamp))
activity.reverse()
tempbasetime = activity[0].timestamp.split(':')
basehour, baseminute = ack_units(tempbasetime)
firsthour, firstminute = ack_units(tempbasetime)
for ac in activity:
    tempbasetime = ac.timestamp.split(':')
    acthour, actminute = ack_units(tempbasetime)
    difftimer = gettimedifference(basehour, acthour, baseminute , actminute)
    firstdifftimer = gettimedifference(firsthour, acthour, firstminute, actminute)
    output += '{0},{1},{2},{3}\n'.format(ac.title, ac.content, difftimer, firstdifftimer)
    basehour = acthour
    baseminute = actminute
file_ = open('activityfeed.csv', 'w')
file_.write(output)
file_.close()
pass

