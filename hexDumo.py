import binascii


def hex_dump(file_path, bytes_per_line=16):
    try:
        with open(file_path, 'rb') as file:
            offset = 0
            while True:
                data = file.read(bytes_per_line)
                if not data:
                    break
                hex_data = binascii.hexlify(data).decode('utf-8')
                printable_data = ''.join(
                    [chr(byte) if 32 <= byte < 127 else '.' for byte in data])
                print(
                    f"{offset:08X}: {hex_data[:bytes_per_line*2]}   {printable_data}")
                offset += bytes_per_line

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")
    hex_dump(file_path)
