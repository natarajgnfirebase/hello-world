import requests
import urllib3
import json

NETBOX_URL = "https://10.25.52.203/api/"
API_TOKEN = "2269dd604649fc8afc5d4b65e40be307722df617"
VLAN_ID = 1000

HEADERS = {
    "Authorization": f"Token {API_TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_vlan_by_id(vlan_id):
    url = f"{NETBOX_URL}ipam/vlans/?vid={vlan_id}"
    response = requests.get(url, headers=HEADERS, verify=False)
    response.raise_for_status()
    results = response.json().get("results")
    if not results:
        raise ValueError(f"No VLAN found with ID {vlan_id}")
    return results[0]

def get_prefixes_for_vlan(vlan_id):
    url = f"{NETBOX_URL}ipam/prefixes/?vlan_id={vlan_id}"
    response = requests.get(url, headers=HEADERS, verify=False)
    response.raise_for_status()
    results = response.json().get("results")
    if not results:
        raise ValueError(f"No prefixes found for VLAN ID {vlan_id}")
    return results

def get_next_available_ip(prefix_id):
    url = f"{NETBOX_URL}ipam/prefixes/{prefix_id}/available-ips/"
    response = requests.post(url, headers=HEADERS, verify=False)
    response.raise_for_status()
    ip_data = response.json()
    return ip_data["address"]

if __name__ == "__main__":
    try:
        vlan = get_vlan_by_id(VLAN_ID)
        vlan_id = vlan["id"]
        vlan_name = vlan["name"]
        print(f" VLAN: {vlan_name} (ID: {VLAN_ID})")

        prefixes = get_prefixes_for_vlan(vlan_id)
        print(f" Found {len(prefixes)} prefix(es) for VLAN")

        prefix = prefixes[0]
        prefix_id = prefix["id"]
        prefix_str = prefix["prefix"]
        print(f" Using Prefix: {prefix_str} (ID: {prefix_id})")

        ip = get_next_available_ip(prefix_id)
        print(f" Next available IP: {ip}")
        output=json.dumps({"output": {"ipaddress":ip}})
        print(output)

    except Exception as e:
        print(f" Error: {e}")
