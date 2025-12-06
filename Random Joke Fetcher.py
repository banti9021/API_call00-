import requests

def fetch_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        joke = response.json()
        print("\nSetup:", joke.get("setup"))
        print("Punchline:", joke.get("punchline"))
    except requests.exceptions.HTTPError as e:
        print("HTTP error:", e)
    except requests.exceptions.Timeout:
        print("Request timed out")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    print("=== Welcome to Random Joke Generator ===")
    while True:
        fetch_joke()
        again = input("\nDo you want another joke? (y/n): ").strip().lower()
        if again != 'y':
            print("\nThanks for laughing! 😄")
            break
