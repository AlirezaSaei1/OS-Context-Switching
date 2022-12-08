from Process import Process
from pprint import pprint


def create_process(path, id):
    instructions = [line.rstrip() for line in open(path)]
    p = Process(id, instructions)
    pprint(vars(p))


def main():
    while True:
        try:
            signal = input().split()
            if signal[0] == "create_process":
                create_process(signal[2], signal[1])

            elif signal[0] == "run_process":
                pass
            elif signal[0] == "block_process":
                pass
            elif signal[0] == "unblock_process":
                pass
            elif signal[0] == "kill_process":
                pass
            elif signal[0] == "show_context":
                pass
            else:
                raise Exception("Invalid Command")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
