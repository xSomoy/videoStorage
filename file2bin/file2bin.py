import os


def convert_file_to_binary(input_file_path, output_file_path):
    """Converts a file to binary data.

    Args:
      input_file_path: The path to the input file.
      output_file_path: The path to the output file.
    """

    with open(input_file_path, "rb") as input_file:
        with open(output_file_path, "wb") as output_file:
            while True:
                data = input_file.read(1)
                if not data:
                    break
                output_file.write(data)


if __name__ == "__main__":
    input_file_path = "E:\Active Work Project\\file2mp4\input"
    output_file_path = "./output.bin"

    convert_file_to_binary(input_file_path, output_file_path)
