"""146. LRU Cache"""


class Node:

    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class DoublyLinkedList:

    def __init__(self):
        self.head = Node("head")
        self.tail = Node("tail")
        self.head.next = self.tail
        self.tail.prev = self.head

    def addToFront(self, key):
        node = self.head
        next_node = node.next
        new_node = Node(key)
        node.next = new_node
        new_node.prev = node
        new_node.next = next_node
        next_node.prev = new_node
        return new_node

    def remove(self, key_node):
        prev_node = key_node.prev
        next_node = key_node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def removeAtBack(self):
        last_node = self.tail.prev
        new_last_node = self.tail.prev.prev
        new_last_node.next = self.tail
        self.tail.prev = new_last_node
        return last_node


class LRUCache:

    """
    - Define double linked list to add and remove the key
    - Add the least used at the end of the linked list and most used at the start of rge linked list
    - Pop the LRU at the back of the list
    - Add the most recently used at the front of the list

    - For get: If the key exists in dictionary, remove it and add to the front of the linkedlist and return the value else return -1
    - For put: If the capacity exceeds, remove the LRU from the back of the linkedlist and remove from dictionary and add the new key to the dictonary and linkedlist

    Time Complexity:O(1)
    Space Complexity:O(n)
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.linked_list = DoublyLinkedList()
        self.dict = {}
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.dict:
            self.linked_list.remove(self.dict[key][0])
            node = self.linked_list.addToFront(key)
            self.dict[key] = (node, self.dict[key][1])
            return self.dict[key][1]

        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.dict:
            node = self.linked_list.remove(self.dict[key][0])
            del self.dict[key]
            self.size -= 1

        if self.size >= self.capacity:
            node = self.linked_list.removeAtBack()
            if node.val in self.dict:
                del self.dict[node.val]
            self.size -= 1

        new_node = self.linked_list.addToFront(key)
        self.dict[key] = (new_node, value)
        self.size += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)