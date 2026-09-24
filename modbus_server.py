import asyncio
from pymodbus.server import StartAsyncTcpServer
from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusServerContext,
    ModbusDeviceContext,
)

# 1. Create the memory block (Holding Registers) starting at address 1
datablock = ModbusSequentialDataBlock(1, [42] * 10)

# 2. Assign the block to a Device Context (formerly "Slave Context")
device = ModbusDeviceContext(hr=datablock)

# 3. Assign the device to the Server Context using ID 1 (formerly "slaves=")
context = ModbusServerContext(devices={1: device})

async def run_server():
    print("Starting Simulated PLC Server on 127.0.0.1:5020...")
    print("Waiting for client connections...")
    await StartAsyncTcpServer(
        context=context,
        address=("127.0.0.1", 5020)
    )

if __name__ == "__main__":
    asyncio.run(run_server())
