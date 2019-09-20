class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            self.storage[self.current] = item
        if self.current < self.capacity - 1:
            self.current += 1
        else:
            self.current = 0

    def get(self):
        print(f"current: {self.current}")
        print(f"item at: {self.storage[self.current - 1]}")
        print(f"full list: {self.storage}")
        pass


rb = RingBuffer(5)
rb.append("first")
rb.get()
rb.append("second")
rb.get()
rb.append("third")
rb.get()
rb.append("fourth")
rb.get()
rb.append("fifth")
rb.get()
rb.append("sixth")
rb.get()
rb.append("seventh")
rb.get()
rb.append("eighth")
rb.get()
rb.append("nineth")
rb.get()
