import binascii


# сравнивает исходные данные с полученными
# sourcebuffer - list  с исходными данными
# radiobuffer - list с данными с радиоканала
# def comparator(sourcebuffer, radiobuffer):
#     count = 0
#     all_packets_count = 0
#     sourcebuffer_len = len(sourcebuffer)
#     radiobuffer_len = len(radiobuffer)
#     for i in range(sourcebuffer_len):
#         all_packets_count += 1
#         for j in range(radiobuffer_len):
#             if sourcebuffer[i] == radiobuffer[j]:
#                 count += 1
#     print(count)
#     print(all_packets_count)
#     return

# проверяет наличие исходного пакета в заданном файле
# source file - путь до файла источника
# radio_buffer - массив со считанными пакетами
def comparator(source_file, radio_buffer):
    with open(source_file, "rb") as source_file:
        source_data = source_file.read()
        clear_source_data = str(binascii.hexlify(source_data))
    correct_packet_count = 0
    for i in radio_buffer:
        if clear_source_data.__contains__(i):
            correct_packet_count += 1
        # else:
        #     print(i)
    print("Receive packet count : " + str(correct_packet_count))
    return True


# данная функция не используется. раньше обрабатывала txt file
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
        line = str(line).split(" | ")
        read_data.append(line[2])
        # line[1] -если понадобится - там хранится номер пакета
        # line[3] - уровень сигнала
    data_file.close()
    return read_data


# просто читает по 512 байт
def read_hex_file(filename):
    hex_data = []
    with open(filename, 'rb') as f:
        while 1:
            content = f.read(512)
            if content == b'':
                break
            splitted_cont = str(binascii.hexlify(content)).split("'")
            clear_data = splitted_cont[1]
            print(clear_data)
            if clear_data.startswith("A69CB493AD67EF5F"):
                # проверяется неполность блока и происходит выкидывание добавочных символов
                clear_data.replace("AB", "")
            hex_data.append(clear_data)
    return hex_data


# Парсинг и очистка пакетов
def read_hex_file_and_parse_packet(filename):
    hex_data = []
    packet_count = 0
    with open(filename, 'rb') as f:
        while 1:
            read_adr = f.read(4)
            read_zan = f.read(4)
            read_data_length = f.read(2)  # длинна полезной нагрузки
            if read_data_length == b'':
                read_data_length = 0  # надо явно указать,что длина может быть 0
            else:
                num_data_len = int(binascii.hexlify(read_data_length), 16)
            content = f.read(num_data_len)  # чтение ПОЛЕЗНОЙ нагрузки
            trash = f.read(512 - num_data_len)
            # print("data length: =" + str(num_data_len))
            if content == b'':
                break
            splitted_cont = str(binascii.hexlify(content)).split("'")
            clear_data = splitted_cont[1]
            # print(clear_data)
            if clear_data.startswith(
                    "A69CB493AD67EF5F"):  # проверяется неполность блока и происходит выкидывание добавочных символов
                clear_data.replace("AB", "")
            hex_data.append(clear_data)
            packet_count += 1
    print("Packet count : " + str(packet_count))
    return hex_data


def write_to_file(something_data, filename):
    writing_file = open(filename, 'w')
    writing_file.write(str(something_data))
    # for line in something_data:
    #     writing_file.write(line)
    writing_file.close()


def start():
    buffer_data = read_hex_file_and_parse_packet("source_file/d3.bin")
    write_to_file(buffer_data, "clear_d3")
    comparator("source_file/source.bin", buffer_data)

    return


start()  # точка запуска
