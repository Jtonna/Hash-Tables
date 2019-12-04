class LinkedPair:
    """
    We use a linked pair to help handle collisions
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None # This is used so theres always an extra spot to add values to on the linked list (Linked Pair)

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity # Number of buckets in the table, each bucket contains an linked list (Linked Pair)
        self.storage = [None] * capacity

    def _hashifier(self, key):
        """
        We use the _ in the function declaration to indicate to us that it should never be used outside of blank
        All this does is take in a key, and return the hashed version of it
        """
        print(f"_hashifier||| key: {key} is now {hash(key)}")
        return(hash(key))
    
    def _hash_modulus(self, key)
        """
        We use the _ in the function declaration to indicate to us that it should never be used outside of blank
        We use this when we need a value for indexing 
        we are going to pass the _hashifier the key, we take _hashifier's return and (modulus %) capacity to return an integer that we can use for indexing
        """
        print(f"_hash_modulus||| key: {key} gets modded by capacity: {self.capacity}")
        return(self._hashifier(key) % self.capacity)
    
    def insert(self, key, value):
        """
        We use this when we want to add data to the hash table
        Sometimes we will create an entirely new index & bucket to contain the data
        Other times we will add to an existing bucket (LinkedPair)
        """

        # if the key
        pass

    def remove(self):
        """
        """
        pass

    def retrieve(self, key):
        """
        """
        pass

    def resize(self):
        """
        """
        pass

