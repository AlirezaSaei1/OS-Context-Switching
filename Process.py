process_states = ["READY", "RUNNING", "BLOCKED"]


class Process:
    def __init__(self, processId, instructions):
        self.processID = processId
        self.instructions = instructions
        self.state = process_states[0]
        self.registers = {"temp": None, "acc": None, "ir": None}
        self.pc = 0

    def show_context(self):
        print(f"Process ID: {self.processID}")
        print(f"Instruction Register: {self.registers['ir']}")
        print(
            f"Accumulator: {self.registers['acc']}\t\tTemp: {self.registers['temp']}")
        print(f"Program Counter: {self.pc}\t\tState: {self.state}")

    def run(self):
        self.pc = self.pc + 1
        op, num = self.instructions[self.pc - 1].split()
        self.registers["ir"] = f"{op} {num}"
        self.registers["temp"] = num
        self.state = process_states[1]

        num = int(num)
        if op == "load":
            self.registers["acc"] = num
        elif op == "sub":
            self.registers["acc"] = self.registers["acc"] - num
        elif op == "add":
            self.registers["acc"] = self.registers["acc"] + num
        elif op == "mul":
            self.registers["acc"] = self.registers["acc"] * num
        else:
            raise Exception("Invalid Operation")
