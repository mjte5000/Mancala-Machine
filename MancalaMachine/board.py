from abc import ABC, abstractmethod

class Board():

    def __init__(self, pieces:dict):
        """
        Initializes a mancala board from the given number of pieces in each
        node.

        Params:
            pieces (dict): a dictionary containing the number of pieces for
                each node. The dictionary expects keys of A6-A1, AS, B6-B1,
                and BS
        """

        self.A6 = Hole('A', pieces["A6"])
        self.A5 = Hole('A', pieces["A5"])
        self.A6.next = self.A5
        self.A4 = Hole('A', pieces["A4"])
        self.A5.next = self.A4
        self.A3 = Hole('A', pieces["A3"])
        self.A4.next = self.A3
        self.A2 = Hole('A', pieces["A2"])
        self.A3.next = self.A2
        self.A1 = Hole('A', pieces["A1"])
        self.A2.next = self.A1
        self.AS = Sink('A', pieces["AS"])
        self.A1.next = self.AS
        self.B6 = Hole('B', pieces["B6"])
        self.AS.next = self.B6
        self.B5 = Hole('B', pieces["B5"])
        self.B6.next = self.B5
        self.B4 = Hole('B', pieces["B4"])
        self.B5.next = self.B4
        self.B3 = Hole('B', pieces["B3"])
        self.B4.next = self.B3
        self.B2 = Hole('B', pieces["B2"])
        self.B3.next = self.B2
        self.B1 = Hole('B', pieces["B1"])
        self.B2.next = self.B1
        self.BS = Sink('B', pieces["BS"])
        self.B1.next = self.BS
        self.BS.next = self.A6
        
    @staticmethod
    def view_nodes():
        """
        Prints a representation of the mancala board with the node names.
        """
        print("---------------------------")
        print("|    B1 B2 B3 B4 B5 B6    |")
        print("| BS                   AS |")
        print("|    A6 A5 A4 A3 A2 A1    |")
        print("---------------------------")

class Node(ABC):

    def __init__(self, player:str, pieces:int, next:'Node'=None):
        """
        Creates a node on the mancala board. There are two types of nodes:
        holes and sinks.

        Params:
            player (str): player 'A' or 'B'
            pieces (int): the number of pieces in this node on the board
            next (Node): the next node on the board
        """

        self.pieces = pieces
        self.next = next
        assert player == 'A' or player == 'B', "Player must be defined as 'A' or 'B'"
        self.player = player

class Hole(Node):

    def __init__(self, player:str, pieces:int, next:'Node'=None):
        """
        Creates a hole on the mancala board, defined as a node where pieces
        can be picked up.

        Params:
            player (str): player 'A' or 'B'
            pieces (int): the number of pieces in this node on the board
            next (Node): the next node on the board
        """

        super().__init__(player, pieces, next)

    def run():
        """
        Generates a run starting with picking up the pieces from this hole.
        """
        pass

class Sink(Node):

    def __init__(self, player:str, pieces:int, next:'Node'=None):
        """
        Creates a sink on the mancala board, defined as a node where pieces
        cannot be picked up (where the player's score is kept).

        Params:
            player (str): player 'A' or 'B'
            pieces (int): the number of pieces in this node on the board
            next (Node): the next node on the board
        """

        super().__init__(player, pieces, next)