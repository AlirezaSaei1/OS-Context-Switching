process_states = ["READY", "RUNNING", "BLOCKED"]


class Process:
    def __init__(self, processId, instructions):
        self.processID = processId
        self.instructions = instructions
        self.state = process_states[0]
        self.registers = {"temp": None, "acc": None, "ir": None}
        self.pc = 0
