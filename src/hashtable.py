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

        If the index (bucket) isnt empty
            while the index (bucket) is not empty & some boolen is not False
                if the index is the same as the key
                    set the value
                    boolen to true so loop ends
                check to see if the next bucket is empty
                    set the value
                    boolen to true so loop ends
                else ( meaning that none of the two index's we checked are free for a bucket entry)
                    set the current index to the next one so the loop repeats
        else ( if the index is empty )
            we need to start a new linked list

                
        else (if the bucket is empty)
            We add the key/value pair to the bucket since we found an open place to store information
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

        If the index we are looking at isn't None
            while the index is not None  (meaning we arent at the end of the linked list)
                and the keys match
                    we can return the value from the key/value pair (aka bucket)
                if they dont match
                    set the current index (bucket) to the next one and loop again
        else:
            tell the user that we checked the entire linked list and could not find it.
        """
        # Step 1: We need to hash & then mod the key to get an integer so we know what index to retrieve information from, we also need to keep track of the index we are at
        index = self._hash_modulus(key)
        current_pair = self.storage[index]
        loop_count = 0

        # Step 2: If the current pair we are looking at doesnt have anything in it we can go look for the value, else return none
        if current_pair is not None:
            # Step 3: While the current_pair we are looking at is NOT None (meaning something is there) we do something
            while current_pair is not None:
                print(f"    retrieve --- \n        the current_pair we are looking at has some information in it, lets see the keys match || loop iteration : {loop_count}")

                # Step 3.1: If the key we are looking at is the key that the user is looking for we can return the value
                if current_pair.key is key:
                    print(f"            current_pair key: \"{current_pair.key}\" matches the one we were looking for:\"{key}\", now we can return the value {current_pair.value}")
                    return current_pair.value

                # Step 3.2: If the key's dont match, we need to set the current_pair to the next pair until we find it
                else:
                    print(f"            current_pair key: \"{current_pair.key}\" does not match the one we were looking for \"{key}\", lets look at the next one")
                    loop_count += 1
                    current_pair = current_pair.next

        else:
            print(f"    retrieve --- \n        key doesnt exist but if it did it would be key:{hash(key)}")
            # Step 4: if were here that means that the index we were looking at is none, we do this to save computational time
            print(f"\n! Retrieve WARNING::\n    key:{index} is 'None' in the Array, that value must not exist")
            return None
             
    def remove(self, key):
        """
        We use this function when we want to remove an key/value (bucket) from an index
        We will need to Hash the key the user provides
        
        if the index is None, we tell the user theres no data to remove because nothing is there

        loop over the array until we find the index
            If the index isnt none
                check to see if the keys match
                    remove the bucket
                else
                    set the current index to the next one and loop again
        If the key isn't found we need to print a warning
        """

        # Step 1: We hash & mod the key to get an integer, so we know what index we should look at
        index = self._hash_modulus(key)
        print(f"    remove --- \n       Looking for {key} aka {index}, so we can remove it.")

        # Step 2: If the index is already None, theres nothing there and we cant delete anything
        if self.storage[index] is None:
            # Step 2.1: Inform the user theres nothing to delete and end the function
            print(f"        Key: {index} ({key}), was not found")
            return

        # Step : While searching is True do something, also set index to current pair to keep track of what we are looking at & a loop count so we know how many times we had to loop over it
        searching = True
        current_pair = self.storage[index]
        loop_count = 0
        while current_pair is not None and searching is True:
            print(f"        we are still searching for {key} || loop iteration : {loop_count}")

            # Step 2.1: if the current pairs key matches the key the user passed in, we can set the index to None (since thats how each bucket starts at)
            if current_pair.key is key:
                print(f"            key: \"{key}\" found, its value is \"{current_pair.value}\". We are now setting the bucket to None")
                self.storage[index] = None
                searching = False
            # Step 3.1: If they key does not match, we need to set the current index to the next one to start the loop again
            else:
                loop_count += 1
                current_pair = current_pair.next

    def resize(self):
        """
        This gets used when the hash table is full, we resize so we can have more room to add keys

        set the current capacity to itself * 2
        create a new storage with all of its values set to None * the size of the current capacity
        create a shallow copy of the old storage
        set the old storage to the new storage

        (since the shallow copy of the old storage is intact, we can copy all of those key & value pairs over into the new storage)

        loop over every entry in the shallow copy
            if what we are looking at is not empty
                and while it stays not empty (not at the end of the list)
                    we can insert the key & value into the new storage
                    we also want to update the bucket we are looking at to the next one to start the loop again
        """

        # Step 1: Set the capacity to double the size, make a new storage with all values set to None with the size of the new capacity
        self.capacity *=2
        new_storage = [None] * self.capacity
        storage_shallow_copy = self.storage
        self.storage = new_storage

        # Step 2: Loop over each index in the shallow copy.
        for pair in storage_shallow_copy:

            # Step 2.1: If the pair has something in it do something, if its empty we dont need to do anything
            if pair is not None:

                # Step 2.2: Set the list we are looking at to a shallow copy so we can iterate over it while there are buckets
                the_current_bucket = pair
                while the_current_bucket is not None:

                    # Use the insert function to add the key and value to the new storage ( that is now double the size of the previous one )
                    # We also want to set the current bucket to the next one to continue the loop
                    self.insert(the_current_bucket.key, the_current_bucket.value)
                    the_current_bucket = the_current_bucket.next
        

"""
Code for testing
"""
# Code for testing
if __name__ == "__main__":
    ht = HashTable(3)
    print("-------- STARTING INSERT OF DATA --------")
    ht.insert("Action", "Chuck Norris")
    ht.insert("Action", "Jackie Chan")
    # ht.insert("Action", "Arnold Schwarzenegger")
    ht.insert("Sci-fi", "Bren Spinner")
    # ht.insert("Dystopian", "Ray Bradbury")
    # ht.insert("Drama", "Quentin Tarantio")
    print("-------- FINISHED INSERTING DATA --------")

    # Test storing beyond capacity
    print("-------- STARTING RETRIEVAL OF DATA --------")
    print(ht.retrieve("Action"))
    # print(ht.retrieve("Sci-fi"))
    # print(ht.retrieve("Dystopian"))
    # print(ht.retrieve("Drama"))
    # print("-------- FINISHED RETRIEVING DATA --------")

    # # Test resizing
    print(f"****** STARTING HASH TABLE RESIZE ******")
    old_storage = len(ht.storage)
    ht.resize()
    new_storage = len(ht.storage)
    print(f"\n****** Resized from {old_storage} to {new_storage}. ******\n")
    print(f"****** FINISHED HASH TABLE RESIZE ******")

    # # Test if data intact after resizing
    print("-------- TESTING IF DATA IS STILL THE SAME --------")
    print(ht.retrieve("Action"))
    print(ht.retrieve("Sci-fi"))
    print(ht.retrieve("Dystopian"))
    print(ht.retrieve("Drama"))
    print("-------- FINISHED TESTING IF DATA IS STILL THE SAME --------")