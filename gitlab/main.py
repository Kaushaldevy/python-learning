import requests

response = requests.get("https://gitlab.com/api/v4/users/Kaushaldevy/projects")
print(response.json())
print(type(response.json()))

for item in response.json():
    print(f"Name of the project is {item['name']} and the URL is {item['web_url']}")

