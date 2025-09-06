import argparse
import json
parser = argparse.ArgumentParser(description="Process extra vars")
parser.add_argument("--ipaddress", type=str, help="ipaddress")
parser.add_argument("--machine_name", type=str, help="machine_name")
parser.add_argument("--instance_type", type=str, help="instance_type")
parser.add_argument("--env", type=str, help="env")

args = parser.parse_args()
output={"ipaddress":args.ipaddress,"machine_name":args.machine_name,"cpu":"FINAL_TEST_CPU","memory":"FINAL_TEST_MEMORY","disk":"131072MB","instance_type":args.instance_type,"env":args.env,"status":"ON"}
print(json.dumps({"output":output}))


#python3 test.py --ipaddress=10.25.10.20 --machine_name=YOSH
