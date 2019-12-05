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
        print(f"    hashifier --- \n        key: {key} is now {hash(key)}")
        return(hash(key))
    
    def _hash_modulus(self, key):
        """
        We use the _ in the function declaration to indicate to us that it should never be used outside of this class because it is "protected"
        We use this when we need a value for indexing 
        we are going to pass the _hashifier the key, we take _hashifier's return and (modulus %) capacity to return an integer that we can use for indexing
        """
        print(f"\n\nhash_modulus --- \nunhashed key: {key} gets modded by capacity: {self.capacity}")
        print(f"    Now sending information to the hashifier.")
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
            # Step 3: Print a warning that data is being over written
            print(f"\n! Insert WARNING::\n    Overwriting data at {index} with {key}\n")

        # Step 4: The index will become the Linked List & contain Key:value pairs. 
        self.storage[index] = LinkedPair(key, value)

    def retrieve(self, key):
        """
        We would use this if we wanted to get data out of the hash table for use anywhere else.
        All we need is the CORRECT key to get the right value, since we are using a linked list we have to me sure to return the proper value. 
        We also want to return None if they key is not found
        """
        # Step 1: We need to hash & then mod the key to get an integer so we know what index's bucket to retrieve information from
        index = self._hash_modulus(key)
        print(f"    retrieve --- \n       key:{self.storage[index].value}")

        # Step 2: Make sure we are looking at the right key, by comparing the passed in key to the hashed version
        if self.storage[index].key == key:
            # Step 3: Return the data stored in the Linked List (linked pair), And If the key is not found it will automatically return None since we set it to None by default
            return self.storage[index].value # This is .value because we have the key we want and we just want the value associated with it
        else:
            # Step 4: print a warning & return None
            print(f"\n! Retrieve WARNING::\n    key:{key} does not match hashed_key:{index}")
            return None 
            
    def remove(self):
        """
        We use this function when we want to remove a value a bucket from the hash table compeletely
        If the key isn't found we need to print a warning
        """
        print(f"remove: index: {index}")

        # Step 1: We need to hash & then mod the key to get an integer so we know what index's bucket to retrieve information from
        index = self._hash_modulus(key)

        # Step 2: We will print a warning if they key wasnt found
        if self.storage[index] is None:
            print(f"\n! Remove WARNING::\n    key: {self.storage[index]} Not Found")
            return # Return to end the function & avoid step 3 since we dont need to assign None to something that is already None

        # Step 3: The way we delete from a Hash Table is to re-assign the index to None since this is the way it started out
        self.storage[index] = None

    def resize(self):
        """
        This gets used when the hash table is full
        We will take the current size of the hash table, multiply it by 2 & create a new hashtable with that value
        Then we will loop over each index and copy the values over into the new hash table
        We also have to re-hash the new index since the current _hash_modulus is based on the capacity but the capacity is going to double in size
        Once complete we will set the new hash table to the old hash table (overwriting) the data
        """
        return

        # Step 1: Double the size of storage, make a new array with all values set to none
        self.storage *= 2
        new_storage = [None] * self.capacity
        
        # Step 2: Loop over the old storage & for every item do something
        for bucket_item in self.storage:
            # Step 3: If the item has something in it we need to copy it, if not its already set to None
            if bucket_item is not None:
                # Step 4: Create a new index to keep track of where what key we are looking at & create a new storage
                new_index = self._hash_modulus(bucket_item.key)
                # Step 5: set the new storage to have all of the key value pairs as the old one
                new_storage[new_index] = LinkedPair(bucket_item.key, bucket_item.value)
        
        # Step 6: Set the new storage to the old storage.
        self.storage = new_storage

        

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