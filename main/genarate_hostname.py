import json
import argparse

g_vmaas_vm_name_prefix = "gcc"
g_vmaas_provider_prefix = {
    "VMware": "exs",
    "OLVM": "kvm",
    "Nutanix": "nut",
    "Hyper-V": "hyp",
    "AzureHCI": "azh",
    "OpenStack": "ops"
}

g_vmaas_os_destros = {
    "Rocky Linux": {
        "os_type": "Linux",
        "9 x64": {
            "Development": {"vm_template": "rocky-91-1c1r20s-net59"},
            "Project": {"vm_template": "rocky-91-1c1r20s-net59"},
            "Production": {"vm_template": "rocky-91-1c1r20s-net59"}
        }
    },
    "Ubuntu": {
        "os_type": "Linux",
        "22.04 LTS x64": {
            "Development": {"vm_template": "ubuntu-2204-2c2r40s"},
            "Project": {"vm_template": "ubuntu-2204-2c2r40s"},
            "Production": {"vm_template": "ubuntu-2204-2c2r40s"}
        }
    },
    "Windows": {
        "os_type": "Windows",
        "2019": {
            "Development": {"vm_template": "windows_2019_2c2r40s_shubh"},
            "Project": {"vm_template": "windows_2019_2c2r40s_shubh"},
            "Production": {"vm_template": "windows_2019_2c2r40s_shubh"}
        }
    }
}


def generate_hostname(prefix, env, provider, ostype, count=1):
    """
    Simple hostname generator — format: prefix-env-provider-ostype-### (3 digit number)
    """
    number = f"{count:03d}"
    return f"{prefix}-{env.lower()}-{provider}-{ostype.lower()}-{number}"


def main():
    

    parser = argparse.ArgumentParser(description="Process extra vars")
    parser.add_argument("--pb_vmaas_env", type=str, help="pb_vmaas_env")
    parser.add_argument("--pb_vmaas_provider", type=str, help="pb_vmaas_provider")
    parser.add_argument("--pb_vmaas_zone", type=str, help="pb_vmaas_zone")
    parser.add_argument("--pb_vmaas_image", type=str, help="pb_vmaas_image")
    parser.add_argument("--pb_vmaas_os_version", type=str, help="pb_vmaas_os_version")
    parser.add_argument("--pb_vmaas_vmcount", type=str, help="pb_vmaas_vmcount")
    # pb_vmaas_env = inputs.get("pb_vmaas_env")
    # pb_vmaas_provider = inputs.get("pb_vmaas_provider")
    # pb_vmaas_zone = inputs.get("pb_vmaas_zone")
    # pb_vmaas_image = inputs.get("pb_vmaas_image")
    # pb_vmaas_os_version = inputs.get("pb_vmaas_os_version")
    # pb_vmaas_vmcount = inputs.get("pb_vmaas_vmcount", 1)
    args = parser.parse_args()
    pb_vmaas_env = args.pb_vmaas_env
    pb_vmaas_provider = args.pb_vmaas_provider
    pb_vmaas_zone = args.pb_vmaas_zone
    pb_vmaas_image = args.pb_vmaas_image
    pb_vmaas_os_version = args.pb_vmaas_os_version
    pb_vmaas_vmcount = int(args.pb_vmaas_vmcount)
    # pb_vmaas_env = inputs.get("pb_vmaas_env")
    # pb_vmaas_provider = inputs.get("pb_vmaas_provider")
    # pb_vmaas_zone = inputs.get("pb_vmaas_zone")
    # pb_vmaas_image = inputs.get("pb_vmaas_image")
    # pb_vmaas_os_version = inputs.get("pb_vmaas_os_version")
    # pb_vmaas_vmcount = inputs.get("pb_vmaas_vmcount", 1)
    

    provider_prefix = g_vmaas_provider_prefix.get(pb_vmaas_provider, "unknown")

    os_type = g_vmaas_os_destros.get(pb_vmaas_image, {}).get("os_type", "linux")

    hostname = generate_hostname(
        prefix=g_vmaas_vm_name_prefix,
        env=pb_vmaas_env,
        provider=provider_prefix,
        ostype=os_type,
        count=pb_vmaas_vmcount
    )
    output=json.dumps({"output": {"hostname":hostname}})
    print(output)
    print(f"Generated hostname: {hostname}")


if __name__ == "__main__":
    main()
