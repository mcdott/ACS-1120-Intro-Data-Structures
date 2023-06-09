#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = []
        for i in range(init_size):
            self.buckets.append(LinkedList())

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = []
        for key, val in self.items():
            items.append('{!r}: {!r}'.format(key, val))
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n) because we need to loop through all the key-value pairs in all buckets."""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n) because we need to loop through all the key-value pairs in all buckets."""
        # Loop through all buckets
        all_values = []
        for bucket in self.buckets:
            # Collect all values in each bucket
            for _, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n) because we need to loop through all the key-value pairs in all buckets."""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(n) because we need to loop through all the key-value pairs in all buckets."""
        # Loop through all buckets
        num_items = 0
        for bucket in self.buckets:
            # Count number of key-value entries in each bucket
            num_items += bucket.length()
        return num_items

    # def contains(self, key):
    #     """Return True if this hash table contains the given key, or False.
    #     Running time: O(n/b) where n is the number of items and b is the number of buckets. This 
    #     is because we need to loop through all the key-value pairs in the bucket where the key belongs,
    #     and there is the worst case potential for all keys to hash to a single bucket."""
    #     # Find bucket where given key belongs
    #     bucket = self.buckets[self._bucket_index(key)]
    #     # Check if key-value entry exists in bucket
    #     if bucket.find(lambda item: item[0] == key) is not None:    
    #         return True
    #     else:
    #         return False

    # def get(self, key):
    #     """Return the value associated with the given key, or raise KeyError.
    #     Running time: O(n/b) where n is the number of items and b is the number of buckets. This 
    #     is because we need to loop through all the key-value pairs in the bucket where the key belongs 
    #     and there is the worst case potential for all keys to hash to a single bucket."""
    #     # Find bucket where given key belongs
    #     bucket = self.buckets[self._bucket_index(key)]
    #     # Check if key-value entry exists in bucket
    #     item = bucket.find(lambda item: item[0] == key)
    #     # If found, return value associated with given key
    #     if item is not None:
    #         return item[1]
    #     # Otherwise, raise error to tell user get failed
    #     else:
    #         raise KeyError('Key not found: {}'.format(key))

    # def set(self, key, value):
    #     """Insert or update the given key with its associated value.
    #     Running time: O(n/b) where n is the number of items and b is the number of buckets. This 
    #     is because we need to loop through all the key-value pairs in the bucket where the key belongs 
    #     and there is the worst case potential for all keys to hash to a single bucket."""
    #     # Find bucket where given key belongs
    #     bucket = self.buckets[self._bucket_index(key)]
    #     # Check if key-value entry exists in bucket
    #     item = bucket.find(lambda item: item[0] == key)
    #     # If found, update value associated with given key
    #     if item is not None:
    #         bucket.delete(item)
    #         bucket.append((key, value))
    #     # Otherwise, insert given key-value entry into bucket
    #     else:
    #         bucket.append((key, value))

    # def delete(self, key):
    #     """Delete the given key from this hash table, or raise KeyError.
    #     Running time: O(n/b) where n is the number of items and b is the number of buckets. This
    #     is because we need to loop through all the key-value pairs in the bucket where the key belongs 
    #     and there is the worst case potential for all keys to hash to a single bucket."""
    #     # Find bucket where given key belongs
    #     bucket = self.buckets[self._bucket_index(key)]
    #     # Check if key-value entry exists in bucket
    #     item = bucket.find(lambda item: item[0] == key)
    #     # If found, delete entry associated with given key
    #     if item is not None:
    #         bucket.delete(item)
    #     # Otherwise, raise error to tell user delete failed
    #     else:
    #         raise KeyError('Key not found: {}'.format(key))
        
    def contains(self, key):
        bucket = self.buckets[self._bucket_index(key)]
        for item in bucket.items():
            if item[0] == key:
                return True
        return False

    def get(self, key):
        bucket = self.buckets[self._bucket_index(key)]
        for item in bucket.items():
            if item[0] == key:
                return item[1]
        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        bucket = self.buckets[self._bucket_index(key)]
        for item in bucket.items():
            if item[0] == key:
                bucket.delete(item)
                bucket.append((key, value))
                return
        bucket.append((key, value))

    def delete(self, key):
        bucket = self.buckets[self._bucket_index(key)]
        for item in bucket.items():
            if item[0] == key:
                bucket.delete(item)
                return
        raise KeyError('Key not found: {}'.format(key))

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
