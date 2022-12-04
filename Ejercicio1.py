class PNode(object):
    def __init__(self, val=None, priority=0):
        self.val = val
        self.priority = priority

class Priority_Queue(object):
    def __init__(self):
        self.priority_list = [PNode(0)]

    def insert(self, val):
        self.priority_list.append(val)
        self.sort_up(len(self.priority_list) - 1)

    def pop(self):
        try:
            value = self.priority_list[1]
        except IndexError:
            raise IndexError("List empty")
        try:
            back_value = self.priority_list.pop()
            self.priority_list[1] = back_value
            self.sort_down(1)
        except IndexError:
            return back_value
        return value

    def peek(self):
        try:
            return self.priority_list[1].val
        except IndexError:
            raise IndexError("List empty")

    def sort_down(self, index):
        while (index * 2) < (len(self.priority_list) - 1):
            max_child = self.max_child(index)
            if self.priority_list[max_child].priority >= self.priority_list[index].priority:
                temp = self.priority_list[index]
                self.priority_list[index] = self.priority_list[max_child]
                self.priority_list[max_child] = temp
            index = max_child

    def sort_up(self, index):
        while self.priority_list[index].priority > self.priority_list[index // 2].priority:
            if index == 1:
                break
            temp = self.priority_list[index]
            self.priority_list[index] = self.priority_list[index // 2]
            self.priority_list[index // 2] = temp
            index = index // 2

    def max_child(self, index):
        if (index * 2 + 1) > (len(self.priority_list) - 1):
            return (index * 2)
        if self.priority_list[index * 2].priority > self.priority_list[index * 2 + 1].priority:
            return (index * 2)
        return (index * 2 + 1)

    insert(1,2,3)