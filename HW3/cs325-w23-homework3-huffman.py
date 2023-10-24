import heapq # Hint: use Python's priority queue class, heapq.

class Node:
    def __init__(self, count, children):
        self.count    = count
        self.children = children
        
    def is_leaf(self):
        return False
        
    def __lt__(self, other):
        return self.count < other.count

    def __eq__(self, other):
        return self.count == other.count
        
class LeafNode(Node):
    def __init__(self, symbol, count):
        super().__init__(count, [])
        self.symbol = symbol
        
    def is_leaf(self):
        return True

class HuffmanCode:
    def __init__(self, F):
        self.C = dict()
        self.T = None 
        self.cost = 0
        self.average_cost = 0
        # TODO: Construct the Huffman Code and set C, T, cost, and average_cost properly!
        heap = []
        
        for symbol, count in F.items():
            heap.append(LeafNode(symbol, count))
            
        heapq.heapify(heap)
        while len(heap) > 1:
            node1 = heapq.heappop(heap)
            node2 = heapq.heappop(heap)
            new_node = Node(node1.count + node2.count, [node1, node2])
            heapq.heappush(heap, new_node)
        
        self.T = heapq.heappop(heap)

        def build_code(node, code):
            if node.is_leaf():
                self.C[node.symbol] = code
                self.cost = self.cost + node.count * len(code)
            else:
                build_code(node.children[0], code + "0")
                build_code(node.children[1], code + "1")
        
        build_code(self.T, "")
        self.average_cost = self.cost / len(F)

    def encode(self, data):
        encoded_data = ""
        for symbol in data:
            encoded_data = encoded_data + self.C[symbol]
        return encoded_data
    
    def decode(self, encoded_data):
        decoded_data = ""
        node = self.T
        for bit in encoded_data:
            if bit == "0":
                node = node.children[0]
            else:
                node = node.children[1]
            if node.is_leaf():
                decoded_data = decoded_data + node.symbol
                node = self.T
        return decoded_data
    
    def get_cost(self):
        """
        Returns the cost of the Huffman code as defined in CLRS Equation 16.4.
        
        Returns:
            Returns the cost of the Huffman code.
        """ 
                
        return self.cost
        
    def get_average_cost(self):
        """
        Returns the average cost of the Huffman code.
        
        Returns:
            Returns the average cost of the Huffman code.
        """ 
        return self.average_cost
        
def get_frequencies(s):
    """
    Computes a frequency table for the input string "s".
    
    Parameters:
        s: A string.
        
    Returns:
        A frequency table F such that F[c] = (# of occurrences of c in s).
    """

    F = dict()
    
    for char in s:
        if not(char in F):
            F[char] = 1
        else:
            F[char] += 1
            
    return F
    
def get_frequencies_from_file(file_name):
    """
    Computes a frequency table from the text in file_name.
    
    Parameters:
        file_name: The name of a text file.
        
    Returns:
        A frequency table F such that F[c] = (# of occurrences of c in the contents of <file_name>).
    """
    f = open(file_name, "r")
    s = f.read()
    f.close()

    return get_frequencies(s)
