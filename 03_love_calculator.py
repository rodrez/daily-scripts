import requests

url = "https://love-calculator.p.rapidapi.com/getPercentage"

person_one = input("Enter a person name: \n")
person_two = input("Enter another person name: \n")


querystring = {"fname":person_one,"sname": person_two}

headers = {
    'x-rapidapi-host': "love-calculator.p.rapidapi.com",
    'x-rapidapi-key': "c81713750fmshbdd6ac998e05c82p1632a1jsn682bb95b4777"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

