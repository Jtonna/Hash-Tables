class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None # This is used so theres always an extra spot to add to

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity # Number of buckets in the table, each bucket contains an linked list (linked pair)
        self.storage = [None] * capacity

    def _hashifier(self, key):
        """
        We use the _ in the function declaration to indicate to us that it should never be used outside of blank
        All this does is take in a key, and return the hashed version of it
        """
        return hash(key)
    
    def _hash_modulus(self, key)
        """
        We use the _ in the function declaration to indicate to us that it should never be used outside of blank
        We use this when 
        All this does is return a value used for indexing, we take the key (modulus %) capacity to return an integer
        """
        pass
    
    def insert():
        pass
    
    def resize():
        pass


