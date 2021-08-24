class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:

    def __init__(self, data_list=None):
        self.head = None
        if data_list is not None:
            node = Node(data=data_list.pop(0))
            self.head = node
            for element in data_list:
                node.next = Node(data=element)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = list()
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, new_node):
        """
        Insert new_node at head
        """
        new_node.next = self.head
        self.head = new_node

    def add_last(self, new_node):
        """
        Insert new_node at tail
        """

        # If linked list is empty,
        # new node will be the only node in linked list,
        # i.e. head and tail node are the same
        if self.head is None:
            self.head = new_node
            return

        # If linked list is not empty:
        # 1. we need to traverse the whole list until we reach the current last node
        # 2. we add the new node as the next node of the current last node
        for current_node in self:
            pass
        current_node.next = new_node

    def add_after(self, target_node_data, new_node):
        """
        Insert new_node after the node whose data is target_node_data
        """
        if self.head is None:
            raise Exception("Linked list is empty.")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f"Node with data '{target_node_data}' not found.")

    def remove_node(self, target_node_data):
        """
        Remove node whose data is target_node_data
        """

        # If linked list is empty, then raise an exception
        if self.head is None:
            raise Exception("Linked list is empty.")

        # If the node to be removed is the current head,
        # then we want the next node in the list to become the new head
        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        # If list is not empty and node to be removed is not the current head,
        # we traverse the list looking for the node to be removed.
        # If we find it, then we need to update its previous node to point to its next node
        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return

            previous_node = node

        # If we traverse the whole list without finding the node to be removed,
        # then raise an exception
        raise Exception(f"Node with data '{target_node_data}' not found.")
