class List:

    def __init__(self):
        self.__head = None

    def set_head(self, head_node):
        self.__head = head_node                         # assign the first element to the list
        self.__head.set_index(0)                        # give it 0-index

    def add_node_at_the_end(self, insert_node):

        list_node = self.__head                         # start with the head of the list

        while list_node.get_next() is not None:         # iterate through the list to the very end
            list_node = list_node.get_next()

        list_node.set_next(insert_node)                 # update the 'next' variable for the last element in the list
        insert_node.set_prev(list_node)                 # set the 'prev' variable for the inserted node

        index = list_node.get_index() + 1               # grab the index of the last element in list and increase it
        insert_node.set_index(index)                    # assign it to the new node

    def add_node_at_the_start(self, insert_node):

        list_node = self.__head

        self.set_head(insert_node)

        self.__head.set_next(list_node)
        list_node.set_prev(self.__head)

        while list_node is not None:                    # update the indices of the rest of the nodes by incrementing
            new_index = list_node.get_index() + 1
            list_node.set_index(new_index)
            list_node = list_node.get_next()

    def add_node_inside(self, insert_node, index):

        list_node = self.__head                         # start with the head of the list

        while list_node.get_index() != index:           # iterate through the list until a specific node met
            list_node = list_node.get_next()

        prev_node_of_the_old_node = list_node.get_prev()
        prev_node_of_the_old_node.set_next(insert_node)

        list_node.set_prev(insert_node)                 # scoot the old node, update 'prev' to point to the inserted one

        insert_node.set_next(list_node)                 # update 'next' for the new node to point to the old one

        insert_node.set_prev(prev_node_of_the_old_node) # update 'prev' for the new node to point to the old's old prev

        index_of_the_old_node = list_node.get_index()   # grab the index of the old node

        insert_node.set_index(index_of_the_old_node)    # and assign it to the new inserted node

        while list_node is not None:                    # update the indices of the rest of the nodes by incrementing
            new_index = list_node.get_index() + 1
            list_node.set_index(new_index)
            list_node = list_node.get_next()

    def delete_node_at_the_end(self):

        if self.__head is None:
            print("Nothing left to delete")
        else:
            list_node = self.__head                     # start with the head of the list

            while list_node.get_next() is not None:     # iterate through the list to the very end
                list_node = list_node.get_next()

            new_last_node = list_node.get_prev()        # update 2nd node's from the end next to None
            new_last_node.set_next(None)

            del list_node                               # remove the last node

    def delete_node_at_the_start(self):

        if self.__head is None:
            print("Nothing left to delete")
        else:
            list_node = self.__head                         # start with the head of the list

            next_node = list_node.get_next()                # grab the second node in the list
            next_node.set_prev(None)                        # set 'prev' to None
            self.set_head(next_node)                        # set this node as the head

            del list_node                                   # delete the old root node

            list_node = self.__head.get_next()              # start with the (new) head + 1 of the list

            while list_node is not None:         # update the indices of the rest of the nodes by decrementing
                new_index = list_node.get_index() - 1
                list_node.set_index(new_index)
                list_node = list_node.get_next()

    def delete_node_inside(self, index):

        if index == 0:
            self.delete_node_at_the_start()
        else:
            list_node = self.__head                     # start with the head of the list

            while list_node.get_index() != index:       # iterate through the list until a specific node met
                list_node = list_node.get_next()

            next_node = list_node.get_next()            # grab the next node of the node we are about to delete
            prev_node = list_node.get_prev()            # grab the previous node of the node we are about to delete

            prev_node.set_next(next_node)               # for the previous node set its 'next' as the next node
            next_node.set_prev(prev_node)               # for the next node set its 'prev' as the prev node

            del list_node

            list_node = self.__head.get_next()          # start with the (new) head + 1 of the list

            while list_node is not None:                # update the indices of the rest of the nodes by decrementing
                new_index = list_node.get_index() - 1
                list_node.set_index(new_index)
                list_node = list_node.get_next()

    def print_list(self):

        if self.__head is None:
            print("The list is empty")
        else:

            list_node = self.__head

            while list_node is not None:
                print(f"{list_node.get_index()}. {list_node.get_value()}")
                list_node = list_node.get_next()
