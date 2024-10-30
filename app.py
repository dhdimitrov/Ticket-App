from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/concerts/<region>')
def scrape_concerts(region):
    concerts = []
    if region == 'София' or region == "София област":
        concerts = biletbg()
        concerts += grabo(region)
    else:
        concerts = grabo(region)
    
    return render_template('concerts.html', concerts=concerts, region=region)

def biletbg():
    url = f"https://bilet.bg/bg/calendar"
    response = requests.get(url)
    response.raise_for_status() 

    soup = BeautifulSoup(response.text, 'html.parser')
                
    concerts = []    
    for event in soup.find_all('div', class_='upcoming-events-box'):
        name = event.find('h5').text.strip()
            # date = event.find('span', class_='date').text.strip()
        concerts.append({"name": name})
    return concerts

def grabo(region):
    city = translate_city(region)
    url = f"https://grabo.bg/events/{city.lower()}/popular#s"
    response = requests.get(url)
    concerts = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        events = soup.find_all('div', class_='e_deal')

        for event in events:
            title_div = event.find('div', class_='ed_event_title')
            
            if title_div:  
                title = title_div.text.strip()
                concerts.append({"name": title})
    return concerts

def translate_city(city_name):
    # Translate the city name from Bulgarian to English
    translated = GoogleTranslator(source='bg', target='en').translate(city_name)
    return translated

if __name__ == '__main__':
    app.run(debug=True)
