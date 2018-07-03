from multiprocessing import Pool

key = 1
threads = 4

def encrypt_line(line):
    res = ""
    for char in line:
        char = chr(ord(char) + key)
        res+=char
    return res
def decrypt_line(line):
    res = ""
    for char in line:
        char = chr(ord(char) - key)
        res+=char
    return res


if __name__ == "__main__":
    pool = Pool(4)
    # читаем из исходного файла
    with open('file.txt') as source_file:
        # chunk the work into batches of 4 lines at a time
        results = pool.map(encrypt_line, source_file, threads)
        # пишем зашифрованное в новый файл
        with (open('ecrypted_file.txt', "w")) as source_file_2:
            source_file_2.writelines(results)

    print(1)
    with open('ecrypted_file.txt') as source_file_2:
        results = pool.map(decrypt_line, source_file_2, threads)
        print(results)
