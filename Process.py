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
