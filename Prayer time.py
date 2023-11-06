import requests
from datetime import datetime


def convert_to_12_hour_format(time_24_hour):
    time_24_hour = time_24_hour.split()[0]
    time_object = datetime.strptime(time_24_hour, '%H:%M')
    time_12_hour = time_object.strftime('%I:%M %p')
    return time_12_hour

current_date = datetime.now().strftime("%d-%m-%Y")
while True:
    city_name = input("\nEnter the city name: ")
    country_name = input("\nEnter Country name: ")
    if country_name== "" or city_name == "":
        city_name = "Dubai"
        country_name = "United Arab Emirates"
        
    api_url = f"http://api.aladhan.com/v1/calendarByCity/{current_date.split('-')[2]}/{current_date.split('-')[1]}?city={city_name}&country={country_name}&method=2"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        if "data" in data and len(data["data"]) > 0:
            # Get the prayer times for the current date
            today_prayer_times = data["data"][0]["timings"]

            print(f"Prayer Times for {city_name}, {country_name} on {current_date}:")
            for prayer, time in today_prayer_times.items():
                # Convert the time to 12-hour format before printing
                time_12_hour = convert_to_12_hour_format(time)
                print(f"{prayer}: {time_12_hour}")
        else:
            print("No data available for the specified city and date.")
    else:
        print(f"API request failed with status code {response.status_code}")
