import json
import requests
import datetime
"""
Finished at 2017-4-19 20:31:57
By:yuxuliu@cisco.com
Version:1.1
"""
def checkweekend(mydate):
    y = int(mydate.split('-')[0])
    m = int(mydate.split('-')[1])
    d = int(mydate.split('-')[2])
    return datetime.datetime(y, m, d).weekday()+1

def checkholi(mydate,country):

    if country.upper() == "ZH":
        year = int(mydate.split('-')[0])
        payload = {'query':str(year), "resource_id": "6018", "format": "json"}
        r = requests.get('https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?', payload)
        data_json = json.dumps(r.json())
        data = json.loads(data_json)
        for i in data['data'][0]['holiday']:
            for item in i['list']:
                if mydate in item['date']:
                    if item['status']=='1':
                        return (1)
                    elif item['status']=='2':
                        return (2)
        return (0)

    if country.upper() == "JP":
        year = mydate.split('-')[0]
        r = requests.get(
            'https://clients6.google.com/calendar/v3/calendars/en.japanese%23holiday@group.v.calendar.google.com/events?calendarId=en.japanese%23holiday%40group.v.calendar.google.com&singleEvents=true&timeZone=Asia%2FShanghai&maxAttendees=1&maxResults=250&sanitizeHtml=true&timeMin=' + year + '-01-01T00%3A00%3A00-05%3A00&timeMax=' + year + '-12-31T00%3A00%3A00-05%3A00&key=AIzaSyBNlYH01_9Hc5S1J9vuFmu2nUqBZJNAXxs')
        data_json = json.dumps(r.json())
        data = json.loads(data_json)
        JPlist=[]
        for i in data['items']:
            JPlist.append(i['start']['date'])
        # print(JPlist)
        # print(mydate)
        formatedmydate=[]
        formatedmydate.append((mydate.split('-'))[0])
        if (mydate.split('-'))[1].__len__()==1:
            formatedmydate.append('0'+(mydate.split('-'))[1])
        else:
            formatedmydate.append((mydate.split('-'))[1])
        if (mydate.split('-'))[2].__len__() == 1:
            formatedmydate.append('0' + (mydate.split('-'))[2])
        else:
            formatedmydate.append((mydate.split('-'))[2])
        formatedmydate='-'.join(formatedmydate)
        # print(formatedmydate)
        # print(JPlist)
        if formatedmydate in JPlist:
          return 1
        else:
            return 0
    if country.upper() == "KR":
        year = mydate.split('-')[0]
        r = requests.get(
            'https://clients6.google.com/calendar/v3/calendars/en.south_korea%23holiday@group.v.calendar.google.com/events?calendarId=en.south_korea%23holiday%40group.v.calendar.google.com&singleEvents=true&timeZone=America%2FMexico_City&maxAttendees=1&maxResults=250&sanitizeHtml=true&timeMin='+year+'-01-01T00%3A00%3A00-05%3A00&timeMax='+year+'-12-31T00%3A00%3A00-05%3A00&key=AIzaSyBNlYH01_9Hc5S1J9vuFmu2nUqBZJNAXxs')
        data_json = json.dumps(r.json())
        data = json.loads(data_json)
        KRlist=[]
        for i in data['items']:
            KRlist.append(i['start']['date'])
        # print(JPlist)
        # print(mydate)
        formatedmydate=[]
        formatedmydate.append((mydate.split('-'))[0])
        if (mydate.split('-'))[1].__len__()==1:
            formatedmydate.append('0'+(mydate.split('-'))[1])
        else:
            formatedmydate.append((mydate.split('-'))[1])
        if (mydate.split('-'))[2].__len__() == 1:
            formatedmydate.append('0' + (mydate.split('-'))[2])
        else:
            formatedmydate.append((mydate.split('-'))[2])
        formatedmydate='-'.join(formatedmydate)
        # print(formatedmydate)
        # print(KRlist)
        if formatedmydate in KRlist:
            return 1
        else:
            return 0