class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self):
        # TO BE COMPLETED
        # make vairables for the current and next nodes
        if self.head is None:
            return None
        else:
            # current_list = [self.head.value]
            constant = self.head
            next_in_line = constant.next_node
            # print(f"starting head: {self.head.value}")
            # print(f"starting constant: {constant.value}")
            # while there is a next node to look at
            while next_in_line:
                constant.next_node = next_in_line.next_node
                next_in_line.next_node = self.head
                self.head = next_in_line
                # current_list.insert(0, self.head.value)
                next_in_line = constant.next_node
                # if self.head:
                #     print(f"new head: {self.head.value}")
                #     print(f"second in line: {self.head.next_node.value}")
                # if constant:
                #     print(f"new constant: {constant.value}")
                # if next_in_line:
                #     print(f"new next: {next_in_line.value}")
                # if len(current_list) > 0:
                #     print(f"constant list: {current_list}")
            return
