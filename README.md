# OT Modbus Scripting

This repository contains the assignment for OT Network and Modbus Scripting. The project demonstrates how to simulate an Industrial Control System (ICS) Programmable Logic Controller (PLC) and read its memory registers over a local TCP network using Python.

## Project Files

* **`modbus_server.py`**: An asynchronous Modbus TCP server that acts as a simulated PLC. It hosts a local datastore (Holding Registers) starting at address 1, with 10 memory slots initialized to the value `42`.
* **`modbus_client.py`**: A Modbus TCP client that establishes a connection to the simulated PLC on localhost (port 5020) and successfully requests/reads 5 holding registers using the `pymodbus` library.

## Prerequisites
* Python 3.x
* `pymodbus` (v3.15.0 or later)

## How to Run

1. **Start the Server (Simulated PLC):**
   Open a terminal and run the server script. It will begin listening on `127.0.0.1:5020`.
   ```bash
   python modbus_server.py
