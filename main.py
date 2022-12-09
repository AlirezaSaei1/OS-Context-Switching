from Process import Process
from pprint import pprint


def create_process(path, id):
    instructions = [line.rstrip() for line in open(path)]
    return Process(id, instructions)


def main():
    processes = {}
    while True:
        print(processes)
        try:
            signal = input().split()
            if signal[0] == "create_process":
                processes[signal[1]] = create_process(signal[2], signal[1])
            elif signal[0] == "run_process":
                pass
            elif signal[0] == "block_process":
                pass
            elif signal[0] == "unblock_process":
                pass
            elif signal[0] == "kill_process":
                processes.pop(signal[1])
            elif signal[0] == "show_context":
                processes[signal[1]].show_context()
            else:
                raise Exception("Invalid Command")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
