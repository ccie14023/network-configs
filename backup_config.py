from netmiko import ConnectHandler
from datetime import datetime

device = {
    'device_type': 'cisco_ios',
    'host': '10.195.180.73',
    'username': 'admin',      # Replace with your username
    'password': 'cisco123'
}

try:
    print("Connecting to switch...")
    connection = ConnectHandler(**device)
    
    print("Getting running configuration...")
    config = connection.send_command('show running-config')
    
    # Create filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'switch_backup_{timestamp}.txt'
    
    # Save to file
    with open(filename, 'w') as f:
        f.write(config)
    
    print(f"Configuration saved to {filename}")
    connection.disconnect()
    
except Exception as e:
    print(f"Backup failed: {e}")
