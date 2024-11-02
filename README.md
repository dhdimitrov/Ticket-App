# Ticket-App

## Overview
Ticket-App is a web application that scrapes ticket websites to provide information about upcoming events in different regions of Bulgaria. The application uses Flask as its web framework and incorporates web scraping techniques to gather event data from various sources.

## Project Structure
- app.py: The main Flask application file containing route definitions and scraping logic.
- templates/: Directory containing HTML templates for rendering pages.
  - index.html: The main page with a map of Bulgaria.
  - concerts.html: Page displaying event information for a specific region.
- static/: Directory for static files.
  - css/styles.css: CSS file for styling the web pages.
  - js/map.js: JavaScript file for rendering the interactive map.
  - data/bulgaria-regions.json: GeoJSON file containing Bulgaria's region data for the map.

## Features
1. Interactive map of Bulgaria on the homepage.
2. Event information scraping from multiple sources (bilet.bg and grabo.bg).
3. Region-specific event listings.
4. Responsive design for various screen sizes.
5. Bilingual support (Bulgarian and English) for city names.

## Dependencies
- Flask: Web framework for Python
- requests: For making HTTP requests
- BeautifulSoup: For parsing HTML content
- deep_translator: For translating city names
- D3.js: For rendering the interactive map (loaded via CDN)

## How to Run
1. Install the required Python packages:
   
pip install flask requests beautifulsoup4 deep_translator
2. Navigate to the project directory and run:
   
python app.py
3. Open a web browser and go to http://localhost:5000 to access the application.

## Usage
- Click on a region in the map or use the navigation menu to view events for a specific area.
- The application will scrape and display relevant event information including event name, location, date, and an image (if available).
- Use the navigation menu to switch between different regions quickly.

## Main Components
1. app.py:
   - Contains Flask routes and main application logic.
   - Implements web scraping functions for bilet.bg and grabo.bg.
   - Handles requests for different regions and renders appropriate templates.
   - Key routes:
     - /: Renders the homepage with the interactive map.
     - /concerts/<region>: Scrapes and displays events for the specified region.

2. index.html:
   - Displays the interactive map of Bulgaria.
   - Provides navigation menu for quick access to different regions.

3. concerts.html:
   - Displays scraped event information in a tabular format.
   - Shows event details including image, name, location, and date.

4. map.js:
   - Renders the interactive map of Bulgaria using D3.js.
   - Allows users to click on regions to view events.

## Scraping Logic
- biletbg() function: 
  - Scrapes events from bilet.bg for Sofia and Sofia region.
  - Extracts event details including image, name, place, and date.
- grabo(region) function: 
  - Scrapes events from grabo.bg for all regions.
  - Translates the region name to English for the API request.
  - Extracts event details including image, name, place, and date.
- translate_city(city_name) function: 
  - Translates city names from Bulgarian to English for API requests using GoogleTranslator.
- extract_image_url(image_div) function: 
  - Extracts image URLs from the scraped HTML using regular expressions.

## Scraping Sources
- bilet.bg: Used for events in Sofia and Sofia region.
- grabo.bg: Used for events in all regions.

## Note
This application is designed for educational purposes and should be used responsibly. Always respect the terms of service of the websites being scraped.

## Future Improvements
1. Add more event sources to increase coverage and provide a more comprehensive event listing.
2. Implement caching to reduce load on scraped websites and improve performance.
3. Add user authentication and personalized event recommendations based on user preferences.
4. Implement error handling and logging for better debugging and maintenance.
5. Create an API endpoint for other applications to access the scraped data.
6. Implement pagination for event listings to handle a large number of events efficiently.
7. Add filters for event types, dates, and price ranges to enhance user experience.
8. Implement a search functionality to allow users to find specific events quickly.

## Contributing
Contributions to improve Ticket-App are welcome. Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License
This project is open-source and available under the MIT License.
