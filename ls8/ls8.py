#!/usr/bin/env python3

"""Main."""


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 25  # x is a list of 25 zeroes
        self.pc = 0

    def ram_write(self, address, value):
        self.ram[address] = value

    def ram_read(self, address):
        return self.ram[address]

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010,  # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111,  # PRN R0
            0b00000000,
            0b00000001,  # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        halted = False
        HALT = 1
        LDI = 130  # Save a value in a register
        PRINT = 71

        registers = [0, 0, 0, 0, 0, 0, 0, 0]

        while not halted:
            instruction = self.ram[self.pc]

            if instruction == HALT:
                halted = True
            elif instruction == LDI:
                reg_num = self.ram[self.pc + 1]
                value = self.ram[self.pc + 2]
                registers[reg_num] = value
                self.pc += 3
            elif instruction == PRINT:
                reg_num = self.ram[self.pc + 1]
                print(registers[reg_num])
                self.pc += 2
            else:
                print('unknown instruction')


cpu = CPU()

cpu.load()
cpu.run()
