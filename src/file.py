def read_data_from_file(filename):
    try:
        with open(filename, "r") as file:
            data = file.read()
        return data
    except FileNotFoundError as e:
        raise e
