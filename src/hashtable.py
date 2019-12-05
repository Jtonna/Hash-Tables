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
        We use the _ in the function declaration to indicate to us that it should never be used outside of this class because it is "protected"
        All this does is take in a key, and return the hashed version of it using pythons built in hash function (but this can be replaced with dj2b, sha etc...)
        """
        print(f"hashifier --- \n    key: {key} is now {hash(key)}")
        return(hash(key))
    
    def _hash_modulus(self, key):
        """
        We use the _ in the function declaration to indicate to us that it should never be used outside of this class because it is "protected"
        We use this when we need a value for indexing 
        we are going to pass the _hashifier the key, we take _hashifier's return and (modulus %) capacity to return an integer that we can use for indexing
        """
        print(f"hash_modulus --- \n    key: {key} gets modded by capacity: {self.capacity}")
        return(self._hashifier(key) % self.capacity)
    
    def insert(self, key, value):
        """
        We use this when we want to add data to the hash table
        Sometimes we will create an entirely new index & bucket to contain the data
        Other times we will add to an existing bucket (LinkedPair)
        """

        # Step 1: We need to hash & then mod the key to get an integer so we know what index we need to put the data into
        index = self._hash_modulus(key)

        # Step 2: We need to check to see if the index has anything in its bucket (linked list)
        if self.storage[index] is not None:
            # Step 3:
            print(f"WARNING:: Overwriting data at {index}")

        # the index is now our value
        self.storage[index] = value

    def retrieve(self, key):
        """
        """
        # Step 1: We need to hash & then mod the key to get an integer so we know what index's bucket to retrieve information from
        index = self._hash_modulus(key)

        # Step 2: return the data stored at that index
        return self.storage[index]

    def remove(self):
        """
        """
        pass

    def resize(self):
        """
        This gets used when the __ blank is full
        We will take the current size of the hash table, multiply it by 2 & create a new hashtable with that value
        Then we will loop over each index and copy the values over into the new hash table
        Once complete we will set the new hash table to the old hash table (overwriting) the data
        """
        pass

"""
Code for testing
"""
if __name__ == "__main__":
    ht = HashTable(2)
    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    print("")
    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)
    print(f"\nResized from {old_capacity} to {new_capacity}.\n")
    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    print("")