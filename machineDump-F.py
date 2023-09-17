import argparse
from capstone import Cs, CS_ARCH_X86, CS_MODE_64

file_path = input("File Path:")


def dump_machine_code(file_path):
    try:
        with open(file_path, 'rb') as file:
            binary_data = file.read()

            # Initialize the Capstone disassembler for x86_64 architecture
            md = Cs(CS_ARCH_X86, CS_MODE_64)

            # Disassemble and print the machine code
            for instr in md.disasm(binary_data, 0):
                print(f'0x{instr.address:x}: {instr.mnemonic} {instr.op_str}')
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Dump machine code from a binary file.")
    parser.add_argument("file_path", help="Path to the binary file")
    args = parser.parse_args()

    dump_machine_code(args.file_path)
