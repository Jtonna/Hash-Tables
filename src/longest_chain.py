import random

def longest_linked_list_chain(keys, buckets, loops=10):
    '''
    Rolls 'keys' 
    '''

    for i in range(loops):
        key_counts = {}

        for i in range(buckets):
            key_counts[i] = 0
        
        for i in range(keys):
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            key_counts[hash_index] += 1
        
        # Tally up and find the largest linked list chain {index where we had the most collision}

        largest_num = 0
        for key in key_counts:
            if key_counts[key] > largest_num:
                largest_num = key_counts[key]
            
        print(f"Longest linked list chaining for {keys} keys in {buckets} buckets (Load factor: {keys/buckets:.2f} : {largest_num})")

longest_linked_list_chain(6, 5, 10)
longest_linked_list_chain(60, 50, 10)
longest_linked_list_chain(600, 500, 10)
longest_linked_list_chain(6000, 5000, 10)
longest_linked_list_chain(600000, 500000, 10)
longest_linked_list_chain(9000000, 1000000, 10)
