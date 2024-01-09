from BTree import BTree
import random, string


class BTreeController:
    def __init__(self, t):
        self.btree = BTree(t)

    def insert(self, key):
        if not self.btree.is_exists(key):
            self.btree.insert(key)
            self.update_display()
            return True
        else:
            return False

    def search(self, key):
        self.btree.comparison_counter = 0
        value = self.btree.search(self.btree.root, key)
        return value, self.btree.comparison_counter

    def delete(self, key):
        if self.btree.search(self.btree.root, key):
            self.btree.delete(self.btree.root, (key,))
            self.update_display()
            return True
        return False

    def update(self, key, value):
        k = (key, value)
        if self.btree.is_exists(k):
            self.btree.update(key, value)
            self.update_display()
            return True
        return False

    def clear_data(self):
        self.btree.btree_data.clear()

    def get_current_data(self):
        return self.btree.btree_data

    def save_data(self):
        self.btree.save(self.btree.root)

    def update_display(self):
        self.btree.btree_data.clear()
        self.btree.save(self.btree.root)

    def save_data_to_file(self):
        self.btree.btree_data.clear()
        self.btree.save(self.btree.root)
        data_list = self.btree.btree_data
        data = ""
        for item in data_list:
            data += f"{item[0]} : {item[1]}\n"
        with open("data.txt", "w") as file:
            file.write(data)

    def generate_random_data(self):
        data = []
        exist_keys = set()
        for i in range(15000):
            key = random.randint(1, 20000)
            while key in exist_keys:
                key = random.randint(1, 20000)
            exist_keys.add(key)
            length = random.randint(2, 10)
            value = ''.join(random.choice(string.ascii_letters) for j in range(length))
            data.append((key, value))
        for item in data:
            self.btree.insert(item)

    def load_data_from_file(self, filename="data.txt"):
        with open(filename, "r") as file:
            lines = file.readlines()
        data_list = []
        for line in lines:
            if line.strip():
                key, value = map(str.strip, line.split(':'))
                data_list.append((int(key), value))
        self.btree.btree_data.clear()
        for item in data_list:
            self.btree.insert(item)
