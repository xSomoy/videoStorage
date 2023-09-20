def file_to_binary(file_path):
    try:
        with open(file_path, "rb") as file:
            binary_data = file.read()
        return binary_data
    except FileNotFoundError:
        return None


if __name__ == "__main__":
    file_path = input(
        "Enter the path to the file you want to convert to binary data: ")
    binary_data = file_to_binary(file_path)

    if binary_data is not None:
        print("Binary data:")
        print(binary_data)
    else:
        print("File not found.")
