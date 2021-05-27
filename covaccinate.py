import time
import json
from sys import exit
import requests

with open('config.json') as data:
    filter_data = json.load(data)
today = time.strftime("%d/%m/%Y")
url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={filter_data['pincode']}&date={today}"

while True:
    with requests.session() as session:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
        print('Executing script !!!')
        response = session.get(url, headers=headers)
        MESSAGE = ""
        if response.ok:
            response = response.json()
            for center in response['centers']:
                for session in center['sessions']:

                    if (session['min_age_limit'] == filter_data['min_age_limit'] and session['available_capacity'] > filter_data['available_capacity'] and session['vaccine'] == filter_data['vaccine']):
                        MESSAGE += f"<b>{today}- VACCINE AVAILABLE FOR {filter_data['pincode']} of {session['min_age_limit']} age group!!</b> \nAvailable- {session['available_capacity']} slots \nCenter- {center['name']},{center['block_name']}\nDate- {session['date']}\nAge- {session['min_age_limit']} + \nVaccine:<strong>{session['vaccine']}</strong>  \nDose 1: {session['available_capacity_dose1']}Dose 2: {session['available_capacity_dose2']}  \n <a href='https://selfregistration.cowin.gov.in/'>Book on CoWin</a>\n\n"
            if MESSAGE != "":
                url = f"https://api.telegram.org/{filter_data['my_token']}/sendMessage?chat_id={filter_data['chat_id']}&text={MESSAGE}&parse_mode=HTML"
                requests.post(url)
                exit()
        time.sleep(filter_data['poll_interval'])
        # poll time in seconds
