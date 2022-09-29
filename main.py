import requests
import json





class WeatherSlupsk:
    def __init__(self): 
        API_key = "### YOUR_API_KEY ### get it for free from -> https://home.openweathermap.org"
        #Coordinates of your city
        lat = "54.46"
        lon = "17.03"
        self.url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&lang=pl&appid={API_key}"

    def get_data(self):
        #gets the forecast data from the API 
        response = requests.get(self.url)
        data = response.json()
        return data 
    
    def conclusion(self):
        #takes the weather forecast data out of the json file
        data = self.get_data()
        for weather in data['list']:
            weatherDate = weather['dt_txt']
            weatherValue = weather['weather'][0]['main']
            if weatherValue == "Rain":
                print(f"{weatherValue} {weatherDate} 🌧️")
            elif weatherValue == "Clouds":
                print(f"{weatherValue} {weatherDate} ☁️")
            elif weatherValue == "Clear" or "Sun":
                print(f"{weatherValue} {weatherDate} ☀️")
            else:
                print(f"{weatherValue} {weatherDate} 💩")


def main():
    WeatherSlupsk().conclusion()



if __name__ == "__main__":
    main()
