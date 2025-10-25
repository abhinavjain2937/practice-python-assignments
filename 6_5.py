class DLinkedNode:
    """A node in a doubly linked list."""
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Hash map: key -> DLinkedNode
        
        # Initialize dummy head and tail for easier node manipulation
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node: DLinkedNode):
        """Removes a node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: DLinkedNode):
        """Adds a node right after the dummy head (making it the MRU)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Move accessed node to the head (most recently used)
            self._remove_node(node)
            self._add_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If key exists, update its value and move it to the head
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_to_head(node)
        else:
            # If key is new, create a new node
            new_node = DLinkedNode(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            
            # If capacity is exceeded, evict the least recently used item
            if len(self.cache) > self.capacity:
                # The LRU node is the one right before the dummy tail
                lru_node = self.tail.prev
                self._remove_node(lru_node)
                del self.cache[lru_node.key]

# --- Running the Example ---

# Input from the problem description
commands = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
output = []

# Initialize a variable to hold the LRUCache instance
lRUCache = None

# Process each command
for i in range(len(commands)):
    command = commands[i]
    arg = args[i]
    
    if command == "LRUCache":
        lRUCache = LRUCache(arg[0])
        output.append(None)
    elif command == "put":
        lRUCache.put(arg[0], arg[1])
        output.append(None)
    elif command == "get":
        result = lRUCache.get(arg[0])
        output.append(result)

# Print the results
print(f"Input Commands: {commands}")
print(f"Input Arguments: {args}")
print(f"Output: {output}")

# Expected output from the problem description for comparison
expected_output = [None, None, None, 1, None, -1, None, -1, 3, 4]
print(f"Expected Output: {expected_output}")
print(f"Matches Expected: {output == expected_output}")