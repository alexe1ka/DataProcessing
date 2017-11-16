import binascii
import serial


def write_to_file(something_data, filename):
    writing_file = open(filename, 'w')
    writing_file.write(str(something_data))
    # for line in something_data:
    #     writing_file.write(line)
    writing_file.close()


z1baudrate = 256000
z1port = 'COM6'  # set the correct port before run it

z1serial = serial.Serial(port=z1port, baudrate=z1baudrate)
z1serial.timeout = 0  # set read timeout
# print z1serial  # debug serial.
print(z1serial.isOpen())  # True for opened

packet = []
count = 0
if z1serial.isOpen():
    while True:
        size = z1serial.inWaiting()  # сколько в порту есть - столько и читаем
        if size:
            data = z1serial.read(size)
            data_decode = binascii.hexlify(data)  # преобразуем к нормальному виду
            packet.append(data_decode)
            print(data_decode)
            count += 1
            # time.sleep(1)
            # if count > 8:
            if count > 8:
                break
else:
    print('z1serial not open')

z1serial.close()
write_to_file(packet, "receive_data_from_bs")
