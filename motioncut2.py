import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the weather website you want to scrape
url = "https://www.exampleweatherwebsite.com"

# Send an HTTP GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the weather data you're interested in (e.g., temperature and humidity)
    temperature = soup.find("span", class_="temperature").text
    humidity = soup.find("span", class_="humidity").text

    # Create a list to store the data
    weather_data = [temperature, humidity]

    # Define the name of the CSV file where you want to save the data
    csv_file = "weather_data.csv"

    # Write the data to a CSV file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(["Temperature", "Humidity"])
        # Write the weather data
        writer.writerow(weather_data)

    print("Weather data has been scraped and saved to", csv_file)
else:
    print("Failed to retrieve data from the website. Status code:", response.status_code)