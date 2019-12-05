class LinkedPair:
    """
    We use a linked pair to help handle collisions
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None # This is used so theres always an extra spot to add values to on the linked list (Linked Pair) which is just a key/value pair

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity # Number of buckets in the table, each bucket contains an linked list (Linked Pair) which is just a key/value pair
        self.storage = [None] * capacity

    def _hashifier(self, key):
        """
        We use the _ in the function declaration to indicate to us that it should never be used outside of this class because it is "protected"
        All this does is take in a key, and return the hashed version of it using pythons built in hash function (but this can be replaced with dj2b, sha etc...)
        """
        print(f"    hashifier --- \n        key: {key} is now {hash(key)}")
        return hash(key)
    
    def _hash_modulus(self, key):
        """
        We use the _ in the function declaration to indicate to us that it should never be used outside of this class because it is "protected"
        We use this when we need a value for indexing 
        we are going to pass the _hashifier the key, we take _hashifier's return and (modulus %) capacity to return an integer that we can use for indexing
        """
        print(f"\n\nhash_modulus --- \nunhashed key: {key} will get modded by capacity: {self.capacity}")
        print(f"    Now sending information to the hashifier.")
        print(f"        we should get a key of {hash(key)} & modding that by {self.capacity} should be :{hash(key) % self.capacity}")
        return self._hashifier(key) % self.capacity
    
    def insert(self, key, value):
        """
        We use this when we want to add data to the hash table
        Sometimes we will create an entirely new index & bucket (which is just a key/value pair) to contain the data
        Other times we will add to an existing index and growing the linked list
        """
        # Step 1: We need to hash & then mod the key to get an integer so we know what index we need to put the data into
        index = self._hash_modulus(key)
        print(f"    inserting ---\n        \"{key}\" : \"{value}\" At index {index}")
        
        # Step 2: We need to check to see if the index has anything in its bucket (which is just a key/value pair chained together to form alinked list)
        if self.storage[index] is not None:
            # Step 3: keep track of a boolen & the linked list's current key/value pair so we know when inserting the new value and linking it up is completed
            current_pair = self.storage[index]
            finished_linking = False

            loop_count = 0
            while current_pair is not None and not finished_linking:
                print(f"            Looping over linked list (at index : {index}) to find room to insert \"{key}\" : \"{value}\" || Loop iteration : {loop_count}")
                # Step 3.1: if the current pair's key (first one in the linked list) is the same one as the one that was passed in we can set the value
                if current_pair.key is key:
                    current_pair.value = value
                    finished_linking = True
                    print(f"            Current_pair.key is key")
                    print(f"                Inserting \"{current_pair.key}\" : \"{current_pair.value} into the linked list {index}")

                # Step 3.2: if pair.next ( the next index from the one we were just looking at ) is None, we can insert a new key value pair 
                elif current_pair.next is None:
                    print(f"            Current pair is none, this means we can insert here")
                    print(f"                Inserting \"{current_pair.key}\" : \"{current_pair.value}\" into the linked list at index:{index}")
                    current_pair.next = LinkedPair(key, value)
                    finished_linking = True

                # Step 3.3: since we cant find a spot to insert, we should look at the next index in the linked list & start the loop again
                else:
                    print(f"        Setting current.pair to the next index to see if theres room.")
                    loop_count += 1
                    current_pair = current_pair.next

        # Step 4: If self.storage[index] is None, that means theres room to insert
        else:
            print(f"            Found room to insert a bucket in the linked list")
            print(f"            Inserting \"{key}\" : \"{value}\" at {self.storage[index]}")
            self.storage[index] = LinkedPair(key, value)
                


    def retrieve(self, key):
        """
        We would use this if we wanted to get data out of the hash table for use anywhere else.
        All we need is the CORRECT key to get the right value, since we are using a linked list we have to me sure to return the proper value. 
        We also want to return None if they key is not found
        """
        # Step 1: We need to hash & then mod the key to get an integer so we know what index to retrieve information from
        index = self._hash_modulus(key)

        # Step 2: If the index we are looking at doesnt have anything in it we can go look for the value, else return none
        if self.storage[index] is not None:
            # Step 3: double check that the keywe found is the one that was passed in so we know its the one we are looking for
            if self.storage[index].key == key:
                print(f"    retrieve --- \n       value: {self.storage[index].value}")
                # Step 4: Return the data stored in the Linked List (linked pair), And If the key is not found it will automatically return None since we set it to None by default
                return self.storage[index].value # This is .value because we have the key we want and we just want the value associated with it
            else:
                # Step 5: print a warning & return None
                print(f"\n! Retrieve WARNING::\n    passed in key:{key} does not match hashed_key:{index}")
                return None 
        else:
            print(f"    retrieve --- \n       key doesnt exist but if it did it would be key:{hash(key)}")
            # Step 6: if were here that means that the index we were looking at is none, we do this to save computational time
            print(f"\n! Retrieve WARNING::\n    key:{index} is 'None' in the Array, that value must not exist")
            return None
            
    def remove(self):
        """
        We use this function when we want to remove an key/value (bucket) from an index
        If the key isn't found we need to print a warning
        """
        print(f"remove: index: {index}")

        # Step 1: We need to hash & then mod the key to get an integer so we know what index we should be looking at
        index = self._hash_modulus(key)

        # Step 2: We will print a warning if they key wasnt found in the array
        if self.storage[index] is None:
            print(f"\n! Remove WARNING::\n    key: {self.storage[index]} Not Found")
            return # Return to end the function & avoid step 3 since we dont need to assign None to something that is already None

        # Step 3: The way we delete from a Hash Table is to re-assign the index's entire linked list to None since this is the way it started out
        self.storage[index] = None

    def resize(self):
        """
        This gets used when the hash table is full
        We will take the current size of the hash table, multiply it by 2 & create a new hashtable with that value
        Then we will loop over each index and copy the values over into the new hash table
        We also have to re-hash the new index since the current _hash_modulus is based on the capacity but the capacity is going to double in size
        Once complete we will set the new hash table to the old hash table (overwriting) the data
        """

        # Step 1: Double the size of storage, make a new array with all values set to none
        self.capacity *= 2
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
# Code for testing
if __name__ == "__main__":
    ht = HashTable(2)
    print("-------- STARTING INSERT OF DATA --------")
    ht.insert("Action", "Chuck Norris")
    ht.insert("Action", "Jaskie Chan")
    ht.insert("Action", "Arnold Schwarzenegger")
    ht.insert("Sci-fi", "Bren Spinner")
    ht.insert("Dystopian", "Ray Bradbury")
    ht.insert("Drama", "Quentin Tarantio")
    print("-------- FINISHED INSERTING DATA --------")

    # # Test storing beyond capacity
    # print("-------- STARTING RETRIEVAL OF DATA --------")
    # print(ht.retrieve("Action"))
    # print(ht.retrieve("Sci-fi"))
    # print(ht.retrieve("Dystopian"))
    # print(ht.retrieve("Drama"))
    # print("-------- FINISHED RETRIEVING DATA --------")

    # # Test resizing
    # print(f"****** STARTING HASH TABLE RESIZE ******")
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)
    # print(f"\n****** Resized from {old_capacity} to {new_capacity}. ******\n")
    # print(f"****** FINISHED HASH TABLE RESIZE ******")

    # # Test if data intact after resizing
    # print("-------- TESTING IF DATA IS STILL THE SAME --------")
    # print(ht.retrieve("Action"))
    # print(ht.retrieve("Sci-fi"))
    # print(ht.retrieve("Dystopian"))
    # print(ht.retrieve("Drama"))
    # print("-------- FINISHED TESTING IF DATA IS STILL THE SAME --------")