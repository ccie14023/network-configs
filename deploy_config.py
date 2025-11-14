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
    
    print("Reading configuration file...")
    with open('vlan_config.txt', 'r') as f:
        config_commands = f.read().splitlines()
    
    print("Applying configuration...")
    output = connection.send_config_set(config_commands)
    print(output)
    
    print("Saving configuration...")
    connection.save_config()
    
    print("Configuration deployed successfully!")
    connection.disconnect()
    
except Exception as e:
    print(f"Deployment failed: {e}")
    sys.exit(1)
