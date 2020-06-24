from pyModbusTCP.client import ModbusClient


hsl = ModbusClient(host="191.33.231.154", port=502, auto_open=True, debug=True, unit_id=1)  # HSL
encore = ModbusClient(host="189.39.19.162", port=502, auto_open=True, debug=True, unit_id=1)  # ENCORE
# c = ModbusClient(host="192.168.1.100", port=502, auto_open=True, debug=True, unit_id=41) # local


r_hsl = hsl.read_input_registers(1, 66)
r_encore = encore.read_input_registers(1, 66)

"""
if regs:
    print(regs)
else:
    print("read error")
"""
