import sys
from sayhi import backend

def main():
    backend.say(" ".join(sys.argv[2:]), animal = sys.argv[1])

if __name__ == "__main__":
    main()