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
        return(hash(key))
    
    def _hash_modulus(self, key)
        """
        We use the _ in the function declaration to indicate to us that it should never be used outside of blank
        We use this when we need a value for indexing 
        we are going to pass the _hashifier the key, we take _hashifier's return and (modulus %) capacity to return an integer that we can use for indexing
        """
        return(self._hashifier(key) % self.capacity)
    
    def insert():
        pass
    
    def resize():
        pass


