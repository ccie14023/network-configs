from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'host': '10.195.180.73',
    'username': 'admin',      # Replace with your username
    'password': 'cisco123'
}

try:
    print("Connecting to switch for pre-check...")
    connection = ConnectHandler(**device)
    
    print("\nCurrent VLANs on switch:")
    output = connection.send_command('show vlan brief')
    print(output)
    
    connection.disconnect()
    
except Exception as e:
    print(f"Pre-check failed: {e}")
