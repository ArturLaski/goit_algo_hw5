class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            # Update value if key already exists
            for i, kv in enumerate(self.table[index]):
                if kv[0] == key:
                    self.table[index][i] = (key, value)
                    return
            self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            return None
        for kv in self.table[index]:
            if kv[0] == key:
                return kv[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            return False
        for i, kv in enumerate(self.table[index]):
            if kv[0] == key:
                del self.table[index][i]
                return True
        return False
# Create a hash table
hash_table = HashTable(10)

# Insert some key-value pairs
hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
hash_table.insert("cherry", 30)

# Search for values
print(hash_table.search("apple"))  # Output: 10
print(hash_table.search("banana"))  # Output: 20

# Delete a key-value pair
hash_table.delete("banana")

# Try searching for the deleted key
print(hash_table.search("banana"))  # Output: None
