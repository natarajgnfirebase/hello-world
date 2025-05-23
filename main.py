import argparse
import requests
parser = argparse.ArgumentParser(description="Process extra vars")
parser.add_argument("--name", type=str, help="User's name")
parser.add_argument("--age", type=int, help="User's age")
parser.add_argument("--location", type=str, help="User's location")

args = parser.parse_args()

print("Received parameters Demo:")
print(f"Name: {args.name}")
print(f"Age: {args.age}")
print(f"Location: {args.location}")
url = "https://api.ipify.org?format=json"
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for HTTP errors
    data = response.json()
    print({"output": {"ip": data["ip"]}})
except requests.RequestException as e:
    print("An error occurred:", e)
