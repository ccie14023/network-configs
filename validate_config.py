import re
import sys

print("Validating configuration file...")

# Read the config file
with open('vlan_config.txt', 'r') as f:
    config = f.read()

errors = []

# Check for VLAN ID in valid range (1-4094)
vlan_match = re.search(r'vlan (\d+)', config)
if vlan_match:
    vlan_id = int(vlan_match.group(1))
    if vlan_id < 1 or vlan_id > 4094:
        errors.append(f"Invalid VLAN ID: {vlan_id} (must be 1-4094)")
    else:
        print(f"✓ VLAN {vlan_id} is valid")

# Check for VLAN name
if 'name' in config:
    print("✓ VLAN name is configured")
else:
    print("⚠ Warning: No VLAN name configured")

# Check for exit statement
if 'exit' not in config:
    errors.append("Missing 'exit' statement")
else:
    print("✓ Exit statement present")

if errors:
    print("\n❌ Validation FAILED:")
    for error in errors:
        print(f"  - {error}")
    sys.exit(1)
else:
    print("\n✅ Validation PASSED")
