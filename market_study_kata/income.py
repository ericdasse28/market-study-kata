import requests

def f(a):
    r=requests.get("https://api.insee.fr/data/"+a)
    j=r.json()
    x=j["results"][0]["values"]["income"]
    y=j["results"][0]["values"]["population"]
    if y==0:
        return None
    else:
        z=x/y
        if z>20000:
            return "rich"
        elif z>12000:
            return "middle"
        else:
            return "poor"
if __name__ == "main":
    for d in ["75", "13", "59"]:
        print(d,f(d))