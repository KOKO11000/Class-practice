class Counter:
    def __init__(self, count = 0):
        self.count = count

    def increase(self):
        self.count += 1
        return self.count

    def decrease(self):
        self.count -= 1
        return self.count

    def reset(self):
        self.count = 0
        return self.count

    def get_value(self):
        return self.count
        
cou = Counter(25)

        