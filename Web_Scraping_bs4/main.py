import requests

def fetch_n_save(url, filename):
    response = requests.get(url)
    with open(filename, "w") as f:
        f.write(response.text)
        
        
url = "https://www.indiatoday.in/"

fetch_n_save(url, "data/webpage.html")  # Fetch and save the webpage content to a file named webpage.html in the data directory
