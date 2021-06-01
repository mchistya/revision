import requests
from requests.models import Response

def handle_duplicates(dataset):
    dataset=dataset.drop_duplicates()
    return dataset

def handle_na(dataset):
    # drop a column if 95% is missing values
    for i in dataset.columns:
        if dataset[i].isnan().sum()/len(dataset)<= 0.5:
            dataset.drop(columns=i,inplace=True)
    return dataset

def get_weather_forecast(city_name):
    b_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'
    params = {
        'city_name': city_name,
        'API_key': '92ef1adc05f178ab9358dfd5ce936260'
    }
    response = requests.get(b_url, params=params).json()

    temp = round((response['main']['temp']-32)/1.8,1)
    print(b_url)
    return temp, response['weather'][0]['main']
