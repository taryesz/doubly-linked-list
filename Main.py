from Node import Node
from List import List


def main():

    # head:

    my_list = List()

    head = Node()
    head.set_value('HEAD')

    my_list.set_head(head)

    # add elements at the end:

    element_1 = Node()
    element_1.set_value('A')
    my_list.add_node_at_the_end(element_1)

    element_2 = Node()
    element_2.set_value('B')
    my_list.add_node_at_the_end(element_2)

    element_3 = Node()
    element_3.set_value('C')
    my_list.add_node_at_the_end(element_3)

    # print:

    print("\nAdding to the end of the list:\n")
    my_list.print_list()

    # add elements at the start:

    element_5 = Node()
    element_5.set_value('D')
    my_list.add_node_at_the_start(element_5)

    # print:

    print("\nAdding at the start of the list:\n")
    my_list.print_list()

    # add elements inside:

    element_4 = Node()
    element_4.set_value('INSIDE_A')
    my_list.add_node_inside(element_4, 2)

    # print:

    print("\nAdding inside the list:\n")
    my_list.print_list()

    # delete at the end:

    my_list.delete_node_at_the_end()

    # print:

    print("\nDelete at the end:\n")
    my_list.print_list()

    # delete at the start:

    my_list.delete_node_at_the_start()

    # print:

    print("\nDelete at the start:\n")
    my_list.print_list()

    # delete inside:

    my_list.delete_node_inside(1)

    # print:

    print("\nDelete inside:\n")
    my_list.print_list()


if __name__ == '__main__':
    main()
