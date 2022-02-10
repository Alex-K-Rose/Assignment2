# Name: Alexander Rose
# OSU Email: rosea2@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date: 1/31/2022
# Description: Part 2 of Assignment two building out methods for Bag class which
# will use a DynamicArray object as its underlying data storage container and
# will make use of some DynamicArray methods for its' own methods.

from dynamic_array import *

class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.length()) + " elements. ["
        out += ', '.join([str(self.da.get_at_index(_))
                          for _ in range(self.da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        This method adds a new element to the bag
        """
        self.da.append(value)

    def remove(self, value: object) -> bool:
        """
        This method removes any one element from the bag that matches the provided value
        object.
        """
        for item in range(self.size()):
            if self.da[item]==value:
                self.da.remove_at_index(item)
                return True

        return False

    def count(self, value: object) -> int:
        """
        This method returns the number of elements in the bag that match the provided value
        object.
        """
        count=0
        for item in range(self.size()):
            if value==self.da[item]:
                count+=1

        return count

    def clear(self) -> None:
        """
        This method clears the contents of the bag
        """
        self.da=DynamicArray() #abandon original array

    def equal(self, second_bag: object) -> bool:
        """
        This method compares the contents of a bag with the content of a second bag provided as a
        parameter. The method returns True if the bags are equal (have the same number of
        elements and contain the same elements without regards to the order of elements).
        Otherwise, it returns False
        """
        if self.size()==0 and second_bag.size()==0:
            return True
        elif self.size() != second_bag.size():
            return False

        bag_copy1=Bag(self) #copy bags and set a counter to 0
        bag_copy2=Bag(second_bag)
        replacement_count=0

        for item1 in range(self.size()): #compare each item in bag1 to bag2 if equal to each other and not None set equal to None
            for item2 in range(second_bag.size()):
                if bag_copy1.da[item1]==bag_copy2.da[item2] and bag_copy1.da[item1] != None :
                    bag_copy1.da[item1]=None
                    bag_copy2.da[item2]=None
                    replacement_count+=1   #count how many items have been replaced

        if replacement_count==self.size() and replacement_count==second_bag.size(): #if number of replacements is equal to size all elements have been replaced
            return True

        else:
            return False


    def __iter__(self):
        """
        This method enables the Bag to iterate across itself.
        """
        self.index = 0

        return self

    def __next__(self):
        """
        This method will return the next item in the Bag, based on the current location of the
        iterator
        """
        try:
            value = self.da[self.index]

        except DynamicArrayException:
            raise StopIteration

        self.index = self.index + 1
        return value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)


    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)


    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))


    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)


    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))


    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)

