import requests

# For now using local host, will change once Heroku is online!
resp = requests.post('https://webvqa.herokuapp.com/predict', files={'image': open('rain.jpg', 'rb'), 'question': "What is the weather like?", 'URL': 'https://images.hindustantimes.com/img/2021/12/30/1600x900/INDIA-WEATHER-RAIN-4_1640872723354_1640872733554.jpg'})

print("This is the output", resp.text)

