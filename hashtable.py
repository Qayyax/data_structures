# Hash table data structure
class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        if [key, value] in self.data_map[index]:
            return False
        self.data_map[index].append([key, value])
        return True

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for ke, value in self.data_map[index]:
                if ke == key:
                    return value
        return None

    def keys(self):
        key_list = []
        for data in self.data_map:
            if data is not None:
                for item in data:
                    key_list.append(item[0])
        return key_list

    def __repr__(self):
        word = []
        for i, val in enumerate(self.data_map):
            output = f"{i}: {val}"
            word.append(output)
        return ', '.join(word)


my_hash_table = HashTable()
my_hash_table.set_item('blue', 1000)
my_hash_table.set_item('green', 2300)
my_hash_table.set_item('red', 5500)
print(my_hash_table)
print(my_hash_table.keys())
