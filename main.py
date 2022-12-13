from Process import Process, process_states


def create_process(path, id):
    instructions = [line.rstrip() for line in open(path)]
    return Process(id, instructions)


def main():
    processes = {}
    loop = 0
    while True:
        try:
            signal = input()
            print(f"Loop: {loop}")
            print(signal)
            signal = signal.split()
            if signal[0] == "create_process":
                processes[signal[1]] = create_process(signal[2], signal[1])

            elif signal[0] == "run_process":
                # make process ready after running is complete
                if processes[signal[1]].state != process_states[2]:
                    processes[signal[1]].run()
                else:
                    raise Exception("Process is Blocked")

            elif signal[0] == "block_process":
                processes[signal[1]].state = process_states[2]

            elif signal[0] == "unblock_process":
                processes[signal[1]].state = process_states[0]

            elif signal[0] == "kill_process":
                processes.pop(signal[1])

            elif signal[0] == "show_context":
                processes[signal[1]].show_context()

            else:
                raise Exception("Invalid Command")
            loop += 1
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
