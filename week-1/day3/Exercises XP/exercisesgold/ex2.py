import random

class MyList:
    def __init__(self, letters):
        self.list = letters
    
    def reverse_list(self):
        return self.list[::-1]
    
    def sort_list(self):
        return sorted(self.list)
    
    def random_list(self):
        return [random.randint(1, 100) for _ in range(len(self.list))]

if __name__ == "__main__":
    my_list = MyList(['a', 'b', 'c', 'd', 'e'])

    print(f"Liste originale: {my_list.list}")
    print(f"Liste inversée: {my_list.reverse_list()}")
    print(f"Liste triée: {my_list.sort_list()}")
    print(f"Liste aléatoire de même longueur: {my_list.random_list()}")