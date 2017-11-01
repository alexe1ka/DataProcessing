import serial
import binascii


def comparator(sourcebuffer, radiobuffer):
    count = 0
    all_packets_count = 0
    sourcebuffer_len = len(sourcebuffer)
    radiobuffer_len = len(radiobuffer)
    for i in range(sourcebuffer_len):
        all_packets_count += 1
        for j in range(radiobuffer_len):
            if sourcebuffer[i] == radiobuffer[j]:
                count += 1
    print(count)
    print(all_packets_count)
    return


# функция для чтения данных с порта
# параметры
# com_name - имя порта('COM1',"COM2",etc...)
# speed - скорость соединения
def read_data_from_terminal(com_name, speed):
    ser = serial.Serial(str(com_name), speed, timeout=1)
    print(ser.name)
    ser.write(b"TEST")
    term_data = []
    while True:
        for c in ser.read():
            term_data.append(c)
            print(c)
            if c == "\n":
                break
                # return term_data


def extract_data_from_file(current_file):
    global data_file
    try:
        data_file = open(current_file, 'r', encoding='utf8', errors='ignore')
    except IOError:
        print('Cannot open file', current_file)
    except Exception:
        print('где-то ошибка')
    read_data = []

    for line in data_file:
        # out_hex = ['{:02}'.format(b) for b in line]
        read_data.append(line)






        # line = str(line).split(" | ")
        # read_data.append(line[2])
        # line[1] -если понадобится - там хранится номер пакета
        # line[3] - уровень сигнала
    data_file.close()
    return read_data


def read_hex_file(filenam):
    hex_data = []
    i = 0
    with open(filenam, 'rb') as f:
        while 1:
            # while i < 1000:
            content = f.read(512)
            if content == b'':
                break
            splitted_cont = str(binascii.hexlify(content)).split("'")
            clear_data = splitted_cont[1]
            print(clear_data)
            if clear_data.startswith("A69CB493AD67EF5F"):
                clear_data.replace("AB", "QW")
            hex_data.append(clear_data)
            i -= 1
    return hex_data


def write_to_file(something_data, filename):
    writing_file = open(filename, 'w')
    writing_file.write(str(something_data))
    # for line in something_data:
    #     writing_file.write(line)
    writing_file.close()


def start():
    source_buffer = read_hex_file("source.bin")
    radio_buffer = read_hex_file("radio_buffer.hex")
    write_to_file(source_buffer, "readedsourcebuffer")
    write_to_file(radio_buffer, "readedradiobuffer")
    comparator(source_buffer, radio_buffer)

    # write_to_file(data_from_cc, "data_from_cc.txt")

    # read_data_from_terminal("COM3", 57600)

    return


start()
