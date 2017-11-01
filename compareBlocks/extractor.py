import re
import os


def file_maker():
    filename_of_created_file = 'Final_radio_config'  # задание имя создаваемого файла
    path = './radio_settings'
    try:
        catalog_of_files = os.listdir(path)  # файл в каталоге скрипта
        # print(catalog_of_files)
        if not catalog_of_files:  # пустота листа в питоне проверяется логическим выражением
            print("В каталоге нет файлов для обработки")
            exit_nah()
            raise SystemExit(1)
    except FileNotFoundError:
        print("В каталоге скрипта нет папки RadioSettings")
        raise SystemExit(1)  # выход из программы,если папки нет в каталоге скрипта

    final_file = open('./' + filename_of_created_file + '.h', 'w')
    final_file.write("#ifndef " + filename_of_created_file.upper() + "_H_\n")
    final_file.write("#define " + filename_of_created_file.upper() + "_H_\n\n\n")
    final_file.write("#include \"stdint.h\" \n\n\n")

    full_config_array = []

    for file in catalog_of_files:
        # final_file.write("#define " + (file.split('.'))[0] + " { \ \n")
        config_array_elem = (file.split('.'))[0].replace('-', '_')
        full_config_array.append(config_array_elem)
        final_file.write("uint8_t " + config_array_elem + "[] = " + " { \n")
        filepath = path + '/' + file
        param_list = parser(filepath)  # парсинг заданного файла
        for param_line in param_list:
            if param_line != len(param_list):
                final_file.write(str(param_line) + ',' + '\n')
            else:
                final_file.write(str(param_line) + '\n')
        final_file.write("0x00")
        final_file.write(" } \n\n")

    final_file.write("uint8_t* config_array[]= {\n")
    for line in full_config_array:
        final_file.write('\t\t\t\t'+line + ', \n')
    final_file.write('0x0 \n')
    final_file.write('}\n')

    final_file.write('#endif /*FINAL_FILE_H*/\n')

    print("Файл создан!")
    final_file.close()
    exit_nah()


def parser(current_filepath):
    global file
    try:
        file = open(current_filepath, 'r')
    except IOError:
        print('Cannot open file', current_filepath)
    except Exception:
        print('где-то ошибка')

    matches_arrays = re.compile('^#define\sRF.*')  # шаблон для поиска строки,начинающейся с #define RF
    out_data = []
    for line in file:
        search_data = matches_arrays.findall(line)
        for data in search_data:
            data = data.split("#define ")  # split
            clean_data = (data[1].split(' ', 1))[1]
            correct_data = clean_data.split(', ')
            out_data.append(hex(len(correct_data)) + ', ' + clean_data)
    file.close()
    return out_data


def exit_nah():
    input("\nНажмите Enter,чтобы выйти")


file_maker()  # здесь собственно и происходит запуск
