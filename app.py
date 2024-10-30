from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import re

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
        image_div = event.find('div', class_='img-top')
        image = extract_image_url(image_div)
        name = event.find('h5').text.strip()
        place = event.find(class_='upcoming-events-place').text.strip()
        date = event.find('span').text.strip()
        concerts.append({"image": image, "name": name, "place": place, "date": date})
    return concerts

def grabo(region):
    city = translate_city(region).lower().replace(" ", "-")
    url = f"https://grabo.bg/events/{city}/popular#s"
    response = requests.get(url)
    concerts = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        events = soup.find_all('div', class_='e_deal')

        for event in events:
            image_div = event.find('div', class_='ed_image')
            title_div = event.find('div', class_='ed_event_title')
            place_div = event.find('div', class_='ed_venue')
            date_div  = event.find('div', class_='ed_date')
            
            if title_div:  
                image = extract_image_url(image_div)
                title = title_div.text.strip()
                place = place_div.text.strip() if place_div else ""
                date = date_div.text.strip() if date_div else ""
                concerts.append({"image": image, "name": title, "place" : place, "date" : date})
    return concerts

def translate_city(city_name):
    # Translate the city name from Bulgarian to English
    translated = GoogleTranslator(source='bg', target='en').translate(city_name)
    return translated

def extract_image_url(image_div):
    if image_div and 'style' in image_div.attrs:
        style = image_div['style']
        url_match = re.search(r'url\([\'"]?(.+?)[\'"]?\)', style)
        if url_match:
            return url_match.group(1)
    return ""

if __name__ == '__main__':
    app.run(debug=True)
