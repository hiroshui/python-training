"""
Refactor the program below (use a "with" statement).
"""
import time

class Timer:
    def __init__(self,name):
        self.name = name
        print(f"timer {name} initialized")

    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self,ty,val,tb):
        end = time.perf_counter()
        print(f"{self.name} : {end-self.start:.10f} seconds")
        return False

def main():
    text = "Explicit is better than implicit."
    with Timer("timerdemo") as timer:
        print(text)

def write_to_file(text):
    with open("exercise.txt", "w") as file:
        file.write(text)

if __name__ == "__main__":
    main()