import argparse
import json
def generate_vm_name(ipaddress, hostname):
    # Customize your VM name convention here
    # Example: hostname-ipaddress (with IP dots replaced by underscores)
    safe_ip = ipaddress.replace('.', '_')
    return f"{hostname}-{safe_ip}"

def main():
    parser = argparse.ArgumentParser(description="Generate VM name from IP address and hostname")
    parser.add_argument("--ipaddress", type=str, required=True, help="IP address of the VM")
    parser.add_argument("--hostname", type=str, required=True, help="Hostname of the VM")

    args = parser.parse_args()
    vm_name = generate_vm_name(args.ipaddress, args.hostname)
    output = json.dumps({"output": {"vm_name": vm_name}})
    print(output)

if __name__ == "__main__":
    main()
