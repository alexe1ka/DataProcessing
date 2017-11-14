import serial

ser = serial.Serial


# функция для чтения данных с порта
# параметры
# com_name - имя порта('COM1',"COM2",etc...)
# speed - скорость соединения
def read_data_from_terminal(com_name, speed):
    global ser  # один открытый порт
    ser = serial.Serial(str(com_name), speed, timeout=1)
    print(ser.name)
    ser.write(b"Terminal is open \n")  # тестовая посылка в терминал
    term_data = []
    
    # while True:
    #     for c in ser.read(512):
    #         term_data.append(c)
    #         print(c)
    #         if c == "\n":
    #             break
    return term_data


def request_command_and_send():
    command = input("enter command: ")
    byte_command = command.encode('ascii')  # convert to byte array
    ser = serial.Serial('COM3', 57600, timeout=None)
    ser.write(byte_command)  # send command
    i = 0
    packet_from_mrdi = []
    bytesToRead = ser.inWaiting()
    print(ser.read(bytesToRead))

    # while i < 9:
    #     if i == 8:  # последний пакет 32 байта
    #         c = ser.read(36)
    #         ser.read(28)
    #         packet_from_mrdi.append(c)
    #     else:
    #         for c in ser.read(64):
    #             packet_from_mrdi.append(c)

    # print(packet_from_mrdi)
    return True


# read_data_from_terminal("COM3", 57600)


request_command_and_send()
