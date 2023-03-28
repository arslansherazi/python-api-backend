if __name__ == '__main__':
    files_dict = {'123.jpg': '/uploads/home'}
    file = {'files': files_dict}

    for f in file:
        for key, value in file[f].items():
            print(key)
            print(value)