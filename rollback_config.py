from netmiko import ConnectHandler
import sys

device = {
    'device_type': 'cisco_ios',
    'host': '10.195.180.73',
    'username': 'admin',      # Replace with your username
    'password': 'cisco123'
}

try:
    print("Connecting to switch...")
    connection = ConnectHandler(**device)
    
    # Read the VLAN to remove from config file
    with open('vlan_config.txt', 'r') as f:
        for line in f:
            if 'vlan' in line:
                vlan_id = line.split()[1]
                break
    
    print(f"Removing VLAN {vlan_id}...")
    output = connection.send_config_set([f'no vlan {vlan_id}'])
    print(output)
    
    print("Saving configuration...")
    connection.save_config()
    
    print(f"VLAN {vlan_id} removed successfully!")
    connection.disconnect()
    
except Exception as e:
    print(f"Rollback failed: {e}")
    sys.exit(1)
