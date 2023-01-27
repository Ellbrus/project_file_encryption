import pyAesCrypt
import os


def decryption(file, password):
    buffer_size = 512 * 1024
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )
    print("[Файл '" + str(os.path.splitext(file)[0]) + "' дешифрован]")

    os.remove(file)


def walking_by_dir(dir, password):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dir(path, password)


password = input('Введите пароль для дешифрования: ')
walking_by_dir('', password)  # указать путь для дешифрования файлов
