import requests
import csv
from datetime import datetime,tzinfo,timezone,timedelta

def get_cur_time():
    cur_time=datetime.utcnow().replace(tzinfo=timezone.utc)
    tw=timezone(timedelta(hours=8))
    cur_time=cur_time.astimezone(tw)
    cur_time = datetime.strftime(cur_time,"%Y-%m-%d-%H:%M")
    return cur_time

def wirte_csv(data):
    with open("out/popular_leaders.csv",'a') as f:
        ranks={**{"date":get_cur_time()},**{ ele['count']:ele['id'] for ele in data['popularLeaders']}}
        csv_writer=csv.DictWriter(f, ranks.keys())
        csv_writer.writerow(ranks)
        
response = requests.get('https://website-api.tosgame.com/api/checkup/popularLeaders')
wirte_csv(eval(response.text))
