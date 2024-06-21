import tkinter  # Import the tkinter module for GUI
from tkinter import messagebox  # Import the messagebox from tkinter for error messages
from tkinter import *  # Import everything from tkinter
import requests  # Import requests module to handle HTTP requests

# Create the main window
root = tkinter.Tk()
root.title("Weather App")  # Set the window title
root.geometry("500x500")  # Set the window size

# Define a function to get the weather information for a given city
def get_weather(city):
    api_key = 'ENTER YOUR API KEY HERE'  # Replace with your WeatherAPI key
    base_url = "http://api.weatherapi.com/v1/current.json?"  # Base URL for the API
    complete_url = base_url + "key=" + api_key + "&q=" + city + "&aqi=no"  # Complete API request URL

    try:
        # Send a request to the API
        response = requests.get(complete_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()  # Parse the response as JSON

        # Check if there's no error in the response data
        if "error" not in data:
            location = data["location"]  # Get the location data
            current = data["current"]  # Get the current weather data
            temperature = current["temp_c"]  # Extract the temperature
            humidity = current["humidity"]  # Extract the humidity
            description = current["condition"]["text"]  # Extract the weather description
            region = location["region"]  # Extract the region
            country = location["country"]  # Extract the country

            # Format the weather information
            weather_info = (
                f"Location: {city}, {region}, {country}\n"
                f"Temperature: {temperature}°C\n"
                f"Humidity: {humidity}%\n"
                f"Description: {description}"
            )
        else:
            weather_info = "City Not Found!"  # If the city is not found
    except requests.exceptions.RequestException as e:
        weather_info = f"Error: {e}"  # Handle any request exceptions

    return weather_info

# Define a function to display the weather information
def show_weather():
    city = city_entry.get()  # Get the city name from the entry widget
    if city:
        weather_info = get_weather(city)  # Get the weather information
        weather_label.config(text=weather_info)  # Update the label with the weather information
    else:
        messagebox.showerror("Input Error", "Please enter a city name")  # Show an error if the entry is empty

# Create and place the widgets in the window
city_label = Label(root, text="Enter City Name :")
city_label.pack(pady=10)  # Add padding to the label

city_entry = Entry(root)
city_entry.pack(pady=5)  # Add padding to the entry

get_weather_button = Button(root, text="Search", command=show_weather)
get_weather_button.pack(pady=10)  # Add padding to the button

weather_label = Label(root, text="", font=("Helvetica", 12))
weather_label.pack(pady=20)  # Add padding to the weather information label

# Run the application
root.mainloop()
