import requests

url = "https://www.toontownrewritten.com/api/population"
header = {"Content-Type":"application/json",
        "Accept-Encoding":"deflate",
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0"}

response = requests.get(url, headers = header)
data = response.json()
print(data)

for district in data["populationByDistrict"]:
    print(data["populationByDistrict"][district])
    print(data["statusByDistrict"][district])