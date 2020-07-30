import requests

url = "https://indeed-indeed.p.rapidapi.com/apigetjobs"

querystring = {"v":"2","format":"json"}

headers = {
    'x-rapidapi-host': "indeed-indeed.p.rapidapi.com",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)