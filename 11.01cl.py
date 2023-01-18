import requests
params = {'latlng': '49.589938,34.550938', 'key': ''}
response = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=params)

print(response)
print(response.json())
