import serial
import binascii

ser = serial.Serial


# функция для чтения данных с порта
# параметры
# com_name - имя порта('COM1',"COM2",etc...)
# speed - скорость соединения
def write_request_to_terminal(com_name, speed, request):
    global ser
    ser = serial.Serial(str(com_name), speed, timeout=1)
    print(ser.name)
    ser.write(request)  # тестовая посылка в терминал
    return


def read_packet_from_serial(port_name, port_baudrate):
    # port_baudrate = 256000
    # port_name = 'COM6'  # set the correct port before run it
    z1serial = serial.Serial(port=port_name, baudrate=port_baudrate)
    z1serial.timeout = 0  # set read timeout
    print(z1serial.isOpen())  # True если порт открыт
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


def generate_request_body(command, set_addr):
    arr_request = bytearray([])
    # arr_request.append("b")
    if command == "1":
        arr_request.append(1)
    elif command == "2":
        arr_request.append(2)
    elif command == "3":
        arr_request.append(3)
    elif command == "4":
        arr_request.append(4)
        arr_request.append(set_addr)
    elif command == "5":
        arr_request.append(5)
        arr_request.append(set_addr)
    elif command == "6":
        arr_request.append(6)
    elif command == "7":
        arr_request.append(7)

    for i in range(62):
        arr_request.append(0)
    # request = ''.join(arr_request)
    print(arr_request)
    print("size of packet : " + str(len(arr_request)))
    return arr_request


# read_data_from_terminal("COM3", 57600)
def menu():
    print(30 * "-", "MENU", 30 * "-")
    print("1. Program reset 1")
    print("2. Set r/w address to start 2")
    print("3. Set read address to start 3")
    print("4. Set control point 4")
    print("5. Select address 5")
    print("6. Requests descriptors 6")
    print("7. Requests address and status 7")
    print("8. Exit")
    print(67 * "-")


def start():
    loop = True
    while loop:
        menu()
        choice = input("Enter your choice [1-5]: ")
        if choice == "1":
            write_request_to_terminal('COM3', 256000, generate_request_body(choice, 0))
        elif choice == "2":

            print("2")
        elif choice == "3":
            print("3")
        elif choice == "4":
            control_point = input("Control point addr")

            print("4")
        elif choice == "5":
            print("5")
        elif choice == "6":
            print("6")
        elif choice == "7":
            print("7")
            # loop = False  # This will make the while loop to end as not value of loop is set to False
        elif choice == "8":
            loop = False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            input("Wrong option selection. Enter any key to try again..")

start()
# request_command_and_send("COM6", 256000)
