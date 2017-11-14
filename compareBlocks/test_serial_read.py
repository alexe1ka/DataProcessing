import serial
import time

z1baudrate = 115200
z1port = 'COM3'  # set the correct port before run it

z1serial = serial.Serial(port=z1port, baudrate=z1baudrate)
z1serial.timeout = 2  # set read timeout
# print z1serial  # debug serial.
print(z1serial.isOpen())  # True for opened


packet = []
count = 0
if z1serial.isOpen():
    while True:
        size = z1serial.inWaiting()  # сколько в порту есть - столько и читаем
        if size:
            if count == 9:
                break
            else:
                data = z1serial.read(size)
                packet.append(data)
                print(data)
                count += 1
        time.sleep(1)
else:
    print('z1serial not open')
