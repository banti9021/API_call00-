import requests

def create_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "My First API Post",
        "body": "This is the body content",
        "userId": 101
    }

    try:
        response = requests.post(url, json=payload, timeout=5)
        response.raise_for_status()

        data = response.json()

        # Correct output
        print("ID:", data.get("id"))
        print("Title:", data.get("title"))
        print("Body:", data.get("body"))
        print("UserID:", data.get("userId"))

    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)

    except requests.exceptions.Timeout:
        print("Request timed out")

    except Exception as e:
        print("Error:", e)

create_post()
