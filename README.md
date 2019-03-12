This is a simple HTML scraping script, which takes a URL as a command line argument, gets it via an HTTP requests, 
parses the HTML using the Beatiful Soup library and prints any web links and images found in the webpage.

To use, one should first install Beatiful Soup via executing: pip install beautifulsoup4
and then run the script by providing a URL string as an argument, 
e.g.: python scraper.py https://zakynthos-lazaros.com
