import argparse

parser = argparse.ArgumentParser(description="Process extra vars")
parser.add_argument("--name", type=str, help="User's name")
parser.add_argument("--age", type=int, help="User's age")
parser.add_argument("--location", type=str, help="User's location")

args = parser.parse_args()

print("Received parameters Demo:")
print(f"Name: {args.name}")
print(f"Age: {args.age}")
print(f"Location: {args.location}")
