from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymongo import MongoClient
import time

# create modbus client
client = ModbusClient(method='rtu', port='COM1', baudrate=9600, timeout=1)

# connect to mongodb
mongo_client = MongoClient()
db = mongo_client.mydb
modbus_data = db.modbus_data

# get device id, register address, and register name from user input
device_id = input("Enter device id: ")
register_address = input("Enter register address: ")
register_name = input("Enter register name: ")

# open connection
client.connect()

while True:
    # read holding register
    result = client.read_holding_registers(register_address, 1, unit=1)

    # insert data to mongodb
    modbus_data.insert_one({'device_id': device_id, 'register_address': register_address, 'register_name': register_name,'value': result.registers[0], 'timestamp': time.time()})

    # sleep for 5 seconds
    time.sleep(5)

# close connection
client.close()
