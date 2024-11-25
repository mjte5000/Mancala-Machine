from board import *

def main():
    """
    Starts the program.
    """

    print("\nWelcome to Mancala Machine!")
    Board.view_nodes()
    print("\nEnter the current number of each pieces in each node.")
    

    pieces = {}
    pieces["A6"] = int(input("A6: "))
    pieces["A5"] = int(input("A5: "))
    pieces["A4"] = int(input("A4: "))
    pieces["A3"] = int(input("A3: "))
    pieces["A2"] = int(input("A2: "))
    pieces["A1"] = int(input("A1: "))
    pieces["AS"] = int(input("AS: "))
    pieces["B6"] = int(input("B6: "))
    pieces["B5"] = int(input("B5: "))
    pieces["B4"] = int(input("B4: "))
    pieces["B3"] = int(input("B3: "))
    pieces["B2"] = int(input("B2: "))
    pieces["B1"] = int(input("B1: "))
    pieces["BS"] = int(input("BS: "))

    board = Board(pieces)

if __name__ == "__main__":
    main()