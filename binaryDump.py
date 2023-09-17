def dump_binary_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            while True:
                byte = file.read(1)
                if not byte:
                    break
                print(format(ord(byte), '02x'), end=' ')
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")
    dump_binary_file(file_path)
