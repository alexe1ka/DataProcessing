import serial
import binascii
import time


# pyinstaller --onefile base_station_control.py
# ser = serial.Serial


# функция для чтения данных с порта
# параметры
# com_name - имя порта('COM1',"COM2"6,etc...)
# speed - скорость соединения

def write_request_to_terminal(com_name, speed, request, isSetDtr):
    global ser
    try:
        ser = serial.Serial(str(com_name), speed, timeout=1)
        # print(ser.name)
        ser.write(request)  # тестовая посылка в терминал
        ser.close()
    except ValueError:
        print("Cannot configure this port")
    finally:
        pass


def is_correct_serial_port(port):
    try:
        serial.Serial(port)
        # print("Port correct")
        return True
    except serial.SerialException:
        # print("Couldn't open port")
        return False


def read_packet_from_serial(port_name, port_baudrate):
    # port_baudrate = 256000
    # port_name = 'COM6'  # set the correct port before run it
    bs_serial_port = serial.Serial(port=port_name, baudrate=port_baudrate)
    bs_serial_port.timeout = 100  # set read timeout
    # print(bs_serial_port.isOpen())  # True если порт открыт
    packet = []
    count = 0
    start_time = time.clock()
    # print(start_time)
    if bs_serial_port.isOpen():
        while True:
            size = bs_serial_port.inWaiting()  # сколько в порту есть - столько и читаем
            if time.clock() - start_time > 0.2:
                # print(time.clock())
                break
            if size:
                data = bs_serial_port.read(size)
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
    bs_serial_port.close()


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
        arr_request.append(int(set_addr))
    elif command == "5":
        arr_request.append(5)
        arr_request.append(int(set_addr))
    elif command == "6":
        arr_request.append(6)
    elif command == "7":
        arr_request.append(7)

    elif command == "8":
        arr_request.append(8)

    for i in range(63):
        arr_request.append(0)
    # request = ''.join(arr_request)
    # print(arr_request)
    print("size of packet : " + str(len(arr_request)))
    return arr_request


# read_data_from_terminal("COM3", 57600)
def menu():
    print(30 * "-", "MENU", 30 * "-")
    print("1. Program reset (MRDI)")
    print("2. Set r/w address to start (MRDI)")
    print("3. Set read address to start (MRDI)")
    print("4. Set control point (MRDI)")
    print("5. Select address (MRDI)")
    print("6. Requests descriptors (MRDI)")
    print("7. Requests address and status (MRDI)")
    print("8. Data request (BMO)")
    print("9. Read flash (BMO)")
    print("10. Write flash (BMO)")
    print("11. Exit")
    print(67 * "-")


def start():
    app_start = True
    while app_start:
        loop = True
        port_number = input("Insert port name: ")
        port_name = 'COM' + port_number

        # print(is_correct_serial_port(port_name))
        if is_correct_serial_port(port_name):
            # print("all ok")
            while loop:
                menu()
                choice = input("Enter your choice [1-8]: ")

                if "1" == choice:
                    write_request_to_terminal(port_name, 256000, generate_request_body(choice, 0))
                elif choice == "2":
                    write_request_to_terminal(port_name, 256000, generate_request_body(choice, 0))
                elif choice == "3":
                    write_request_to_terminal(port_name, 256000, generate_request_body(choice, 0))
                elif choice == "4":
                    # TODO адрес пока десятичный
                    control_point = input("Control point addr: ")
                    write_request_to_terminal(port_name, 256000, generate_request_body(choice, control_point))
                elif choice == "5":
                    sel_addr = input("Select address: ")
                    write_request_to_terminal(port_name, 256000, generate_request_body(choice, sel_addr))
                elif choice == "6":
                    write_request_to_terminal(port_name, 256000, generate_request_body(choice, 0))
                    read_packet_from_serial(port_name, 256000)
                elif choice == "7":
                    write_request_to_terminal(port_name, 256000, generate_request_body(choice, 0))
                elif choice == "8":
                    # TODO Data request
                    pass
                elif choice == "9":
                    # TODO Data request
                    pass
                elif choice == "10":
                    # TODO Data request
                    pass
                elif choice == "11":
                    loop = False
                    app_start = False
                else:
                    input("Wrong option selection. Enter any key to try again..")
        else:
            print("Wrong port number!!!")
            continue


if __name__ == "__main__":
    start()
