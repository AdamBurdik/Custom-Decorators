# Just Example File

from CustomDecorators import get_time

def finished():
    print("Finished")

@get_time(name=True, round_to=2, function=finished)
def main():
    for i in range(100_000_000):
        pass

if __name__ == "__main__":
    main()
