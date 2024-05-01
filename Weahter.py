'''
About Programm : A weather forecast program. It will take a required argument: 
the city name. It will
show all the weather information for that city. The program can also take another
argument, either temperature or density or other (based on the options that provide the
API). The user should be able to see the list of those options.

Version : 1.0
Author : Artash
'''
import requests

def get_weather(city, option=None):
    """
    Get weather information for a given city.
    
    Args:
    city (str): The name of the city.
    option (str): Optional. The specific weather information to fetch (e.g., temperature, humidity, etc.).
    
    Returns:
    dict: Weather information as a dictionary.
    """
    api_key = "24222b74845561948f135c0fc143682e"  # Replace "YOUR_API_KEY" with your actual API key from OpenWeatherMap
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Make API call to fetch weather data
    try:
        # Make API call to fetch weather data
        params = {"q": city, "appid": api_key, "units": "metric"}
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            if option:
                if option in data['main']:
                    return {option.capitalize(): data['main'][option]}
                else:
                    return f"Option '{option}' is not available for this city."
            else:
                return data
        else:
            return f"Error: Unable to fetch weather data. Status code: {response.status_code}"
    except Exception as e:
        return f"Error: {str(e)}"

def get_available_options():
    """
    Get available weather options provided by the API.
    
    Returns:
    list: Available weather options.
    """
    return ['temp', 'humidity', 'pressure', 'temp_min', 'temp_max']

if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    options = get_available_options()
    print("Available options:", options)
    selected_option = input("Enter the option you want to see (or leave blank for all): ").lower()

    weather_info = get_weather(city_name, selected_option)
    print("\nWeather Information:")
    if isinstance(weather_info, dict):
        for key, value in weather_info.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("Error 404",weather_info)

# def get_display_smile(data):
#     """
#     Displaying currency smile
    
#     Returns:
#     list: Available weather options.
#     """
#     code_to_smile = {
#         "Clear": "Clear \U00002600",
#         "Clouds": "Cloudy \U00002601",
#         "Rain": "rain \U00002614",
#         "Drizzle": "rain2 \U00002614",
#         "Thunderstorm": "Storm \U000026A1",
#         "Snow": "snow \U0001F328",
#         "Mist": "Fog \U0001F32B"
#     }
#     weather_description = data["weather"][0]["main"]
#     if weather_description in code_to_smile:
#         smile = code_to_smile[weather_description]
#     else:
#         smile = "I dont Know what the wheather is it!?"
#     return smile