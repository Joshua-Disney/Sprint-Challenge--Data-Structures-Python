class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.current] = item
        if self.current < self.capacity - 1:
            self.current += 1
        else:
            self.current = 0

    def get(self):
        # non_none = []
        # for i in self.storage:
        #     if i is not None:
        #         non_none.append(i)
        # return non_none
        return [i for i in self.storage if i is not None]


# rb = RingBuffer(5)
# rb.append("first")
# rb.get()
# rb.append("second")
# rb.get()
# rb.append("third")
# rb.get()
# rb.append("fourth")
# rb.get()
# rb.append("fifth")
# rb.get()
# rb.append("sixth")
# rb.get()
# rb.append("seventh")
# rb.get()
# rb.append("eighth")
# rb.get()
# rb.append("nineth")
# rb.get()
# rb.append("tenth")
# rb.get()
# rb.append("eleventh")
# rb.get()
