import requests

API_KEY = "b6907d289e10d714a6e88b30761fae22"
BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly"

def get_weather_data(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

def get_temperature(weather_data, date):
    for entry in weather_data["list"]:
        api_date = entry["dt_txt"].split()[0]  # Extract date part from API response
        if api_date == date:
            return entry["main"]["temp"]
    return None

def get_wind_speed(weather_data, date):
    for entry in weather_data["list"]:
        api_date = entry["dt_txt"].split()[0]  # Extract date part from API response
        if api_date == date:
            return entry["wind"]["speed"]
    return None

def get_pressure(weather_data, date):
    for entry in weather_data["list"]:
        api_date = entry["dt_txt"].split()[0]  # Extract date part from API response
        if api_date == date:
            return entry["main"]["pressure"]
    return None

def main():
    city = "London"
    weather_data = get_weather_data(city)

    while True:
        print("\nWeather Information Options :")
        print("1. Get Temperature ")
        print("2. Get Wind Speed")
        print("3. Get Air Pressure")
        print("0. Exit")
        option = int(input("Enter your choice: "))

        if option == 1:
            date = input("Enter the date (YYYY-MM-DD): ")
            temperature = get_temperature(weather_data, date)
            if temperature is not None:
                print(f"Temperature on {date} is : {temperature}K")
            else:
                print("Data not available for the specified date.")
        elif option == 2:
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed(weather_data, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date} is : {wind_speed} km/h")
            else:
                print("Data not available for the specified date.")
        elif option == 3:
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure(weather_data, date)
            if pressure is not None:
                print(f"Air Pressure on {date} is : {pressure} hPa")
            else:
                print("Data not available for the specified date.")
        elif option == 0:
            print("....................Program is Terminated ...............................")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
