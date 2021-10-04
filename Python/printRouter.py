"""
Program to print a pattern of a router (box)

     ◌                  ◌
    * *                * *
    * *                * *
    * *                * *
    * *                * *
    * *                * *
    * *                * *
-----^------------------^-----
|****************************|
|/\/○\/\/\/○\/\/\/○\/\/\/○\/\|
|****************************|
|****************************|
------------------------------
"""

def print_router():
    print("◌".center(11), end="")
    print(" " * 8, end="")
    print("◌".center(11))
    for i in range(6):
        print("* *".center(11), end="")
        print(" " * 8, end="")
        print("* *".center(11))
    print("-" * 5, end="")
    print("^", end="")
    print("-" * 18, end="")
    print("^", end="")
    print("-" * 5)
    for i in range(4):
        print("|", end="")
        if i == 1:
            for j in range(4):
                print("/\\/", end="")
                print("○", end="")
                print("\\/\\", end="")
        else:
            print("*" * 28, end="")
        print("|")
    print("-" * 30)

if __name__ == "__main__":
    print_router()
