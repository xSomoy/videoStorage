from keystone import *


def assemble_x86(assembly_code):
    try:
        # Initialize the Keystone assembler for x86 architecture
        ks = Ks(KS_ARCH_X86, KS_MODE_32)

        # Assemble the assembly code into machine code
        machine_code, _ = ks.asm(assembly_code)

        return bytes(machine_code)
    except KsError as e:
        print(f"Assembly error: {e}")
        return None


if __name__ == "__main__":
    assembly_code = input("Enter x86 assembly code: ")
    machine_code = assemble_x86(assembly_code)

    if machine_code is not None:
        print("Machine code:")
        print(machine_code.hex())
