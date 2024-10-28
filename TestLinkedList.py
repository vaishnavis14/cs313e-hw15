#  File: TestLinkedList.py

#  Description: Writing functions for linked lists.

#  Student Name: Vaishnavi Sathiyamoorthy

#  Student UT EID: vs25229

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 10/29/2022

#  Date Last Modified: 10/31/2022


class Link(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class LinkedList(object):
    # create a linked list
    # you may add other attributes
    def __init__(self):
        self.first = None

    # get number of links
    def get_num_links(self):
        current = self.first
        if current == None:
            return 0
        else:
            count = 0
            while current.next != None:
                count += 1
                current = current.next
            return count

    # add an item at the beginning of the list
    def insert_first(self, data):
        new_link = Link(data)
        new_link.next = self.first
        self.first = new_link

    # add an item at the end of a list
    def insert_last(self, data):
        new_link = Link(data)
        current = self.first
        # if the linked list is empty
        if current == None:
            self.first = new_link
            return

        while current.next != None:
            current = current.next
        current.next = new_link

    # add an item in an ordered list in ascending order
    # assume that the list is already sorted
    def insert_in_order(self, data):
        if self.first == None or data < self.first.data:
            self.insert_first(data)
        else:
            current = self.first
            inserted = False
            while current.next != None:
                if current.next.data > data:
                    new_link = Link(data, current.next)
                    current.next = new_link
                    inserted = True
                    break
                current = current.next
            if not inserted:
                self.insert_last(data)

    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        if self.first == None:
            return None
        else:
            current = self.first
            while current != None:
                if current.data == data:
                    return data
                current = current.next
            return None

    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        if self.first == None:
            return None
        else:
            current = self.first
            while current != None:
                if current.data == data:
                    return data
                current = current.next
            return None

    # Delete and return the first occurrence of a Link containing data
    # from an unordered list or None if not found
    def delete_link(self, data):
        if self.find_unordered(data) == None:
            return None
        else:
            current = self.first
            if current.data == data:
                self.first = self.first.next
            else:
                while current.next.data != data and current.next != None:
                    current = current.next
                delete = current.next
                current.next = delete.next
                return delete.data

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        current = self.first
        string = ""
        if current == None:
            return string
        while current != None:
            for i in range(10):
                if i == 9:
                    string += str(current.data) + "  " + "\n"
                elif current.next == None:
                    string += str(current.data)
                else:
                    string += str(current.data) + "  "
                current = current.next
                if current == None:
                    break
        return string


    # Copy the contents of a list and return new list
    # do not change the original list
    def copy_list(self):
        cp = LinkedList()
        current = self.first
        while current != None:
            cp.insert_last(current.data)
            current = current.next
        return cp

    # Reverse the contents of a list and return new list
    # do not change the original list
    def reverse_list(self):
        rev = LinkedList()
        current = self.first
        while current != None:
            rev.insert_first(current.data)
            current = current.next
        return rev

    # Sort the contents of a list in ascending order and return new list
    # do not change the original list
    def sort_list(self):
        sort_lst = LinkedList()
        current = self.first
        for i in range(self.get_num_links() + 1):
            sort_lst.insert_in_order(current.data)
            current = current.next
        return sort_lst

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        current = self.first
        if current == None:
            return None
        while current.next != None:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    # Return True if a list is empty or False otherwise
    def is_empty(self):
        if self.first == None:
            return True
        return False

    # Merge two sorted lists and return new list in ascending order
    # do not change the original lists

    def merge_list(self, other):
        sorted_merge_lst = LinkedList()
        current = self.first
        if current != None:
            for i in range(self.get_num_links() + 1):
                sorted_merge_lst.insert_in_order(current.data)
                current = current.next
        current = other.first
        if current != None:
            for i in range(other.get_num_links() + 1):
                sorted_merge_lst.insert_in_order(current.data)
                current = current.next
        return sorted_merge_lst



    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):
        if self.get_num_links() != other.get_num_links():
            return False
        elif self.is_empty() and other.is_empty():
            return True
        else:
            lst1 = self.first
            lst2 = other.first
            for i in range(self.get_num_links() + 1):
                if lst1.data != lst2.data:
                    return False
                lst1 = lst1.next
                lst2 = lst2.next
            return True

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    # do not change the original list
    def remove_duplicates(self):
        new_lst = LinkedList()
        current = self.first
        if current == None:
            return new_lst
        for i in range(self.get_num_links()):
            if new_lst.find_ordered(current.data) == None:
                new_lst.insert_last(current.data)
            current = current.next
        return new_lst



def main():
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    # Test method insert_last()
    llst = LinkedList()
    llst.insert_first(0)
    llst.insert_last(1)
    llst.insert_last(2)
    llst.insert_last(3)
    llst.insert_last(4)
    llst.insert_first(5)
    llst.insert_last(6)
    llst.insert_last(7)
    llst.insert_last(8)
    llst.insert_last(9)
    print(llst.is_equal(llst))

    # Test method insert_in_order()
    llst.insert_in_order(4.5)

    # Test method get_num_links()
    print(llst.get_num_links())

    # Test method find_unordered()
    # Consider two cases - data is there, data is not there
    print(llst.find_unordered(7))
    print(llst.find_unordered(25))

    # Test method find_ordered()
    # Consider two cases - data is there, data is not there
    print(llst.find_ordered(7))
    print(llst.find_ordered(25))

    # Test method delete_link()
    # Consider two cases - data is there, data is not there
    print(llst.delete_link(7))
    print(llst.delete_link(25))

    # Test method copy_list()
    print(llst.copy_list())

    # Test method reverse_list()
    print(llst.reverse_list())

    # Test method sort_list()
    print(llst.sort_list())

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    print(llst.is_sorted())
    llst2 = LinkedList()
    llst2.insert_first(0)
    llst2.insert_first(1)
    print(llst2.is_sorted())

    # Test method is_empty()
    print(llst.is_empty())

    # Test method merge_list()
    print(llst.merge_list(llst2))

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    print(llst.is_equal(llst2))
    llst3 = LinkedList()
    llst3.insert_first(0)
    llst3.insert_first(1)
    print(llst2.is_equal(llst3))

    # Test remove_duplicates()
    print(llst2.remove_duplicates())


if __name__ == "__main__":
    main()
