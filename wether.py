import requests

def api_fetch():
    url = "https://api.zippopotam.us/in/110001"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        print("Post Code:", data.get("post code"))
        print("Country:", data.get("country"))

        # "places" ek list hoti hai
        place = data.get("places")[0]

        print("Place Name:", place.get("place name"))
        print("State:", place.get("state"))
        print("Latitude:", place.get("latitude"))
        print("Longitude:", place.get("longitude"))

    except requests.exceptions.HTTPError as e:
        print("HTTP error:", e)
    except requests.exceptions.Timeout:
        print("Request timed out")
    except Exception as e:
        print("Error:", e)


api_fetch()
