from pymodbus.client import ModbusTcpClient

# 1. Define the PLC connection (Targeting localhost for simulation)
# Standard Modbus TCP port is 502, but simulators often use 5020
client = ModbusTcpClient('127.0.0.1', port=5020)

print("Attempting to connect to simulated PLC...")
connection = client.connect()

if connection:
    print("Connected successfully!")

    # 2. Attempt to read from "Holding Registers" (Memory slots in the PLC)
    # address=0 (Start at slot 0), count=5 (Read 5 slots), slave=1 (Target device ID)
    result = client.read_holding_registers(address=0, count=5, device_id=1)

    if not result.isError():
        print("Data read from PLC:", result.registers)
    else:
        print("Failed to read data. The simulated server might be empty.")

    # 3. Clean up the connection
    client.close()
else:
    print("Connection failed. Is the simulated PLC server actually running?")
