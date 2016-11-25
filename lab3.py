import requests, json
from datetime import datetime as dt
from datetime import timedelta as delta
res = requests.get('https://api.meetup.com/2/open_events?and_text=False&country=us&offset=0&city=Boston&format=json&lon=-71.0&limited_events=False&topic=technology&state=ma&photo-host=public&page=20&radius=25.0&lat=42.0&desc=False&status=upcoming&sig_id=216657279&sig=ccb1a0f4db5045c31835161ebda65eb33db5a7e9')
data = json.loads(res.text)
now = dt.now()
start = now.replace(hour=0, minute=0, second=0, microsecond=0)
cur = start+delta(days=1)
page = open("page.html", "w")
for day in range(0,7,1):
	page.write("<h3>"+(now+delta(days=day)).strftime('%A')+", "+(now+delta(days=day)).strftime('%Y-%m-%d')+"</h3>")
	for event in data["results"]:
		event_time = int(str(event["time"])[0:10])
		if (event_time > cur.timestamp() and event_time < (cur+delta(days=1)).timestamp()):
			try:
				page.write("<div><b>Name:</b> "+event["name"]+"</div>")
			except KeyError:pass
			try:
				page.write("<div><b>Address:</b> "+(event["venue"])["address_1"]+"</div>")
			except KeyError:pass
			try:
				page.write("<div><b>Time:</b> "+str((dt.fromtimestamp(event_time)).strftime('%H:%M'))+"</div>")
			except KeyError:pass
			try:
				page.write("<details><summary><b>Description</b></summary><p>"+event["description"]+"</p></details>")
			except KeyError:pass
	cur += delta(days=1)

page.close()