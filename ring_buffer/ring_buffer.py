class RingBuffer:
    def __init__(self, capacity):
        self.index = 0
        self.storage = [None] * capacity
        self.capacity = capacity


    def append(self, item):
        self.storage[self.index] = item
        self.index = (self.index + 1) % len(self.storage)
        print(self.index)

    def get(self):
        return [item for item in self.storage if item is not None]
