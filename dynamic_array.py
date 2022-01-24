# Name: Alexander Rose
# OSU Email: rosea2@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date: 1/31/2022
# Description: The DynamicArray class will use a StaticArray object as its
# underlying data storage container and will provide many methods similar to those we
# are used to using when working with Python lists.

import static_array
from static_array import *

class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/" + str(self.capacity) + ' ['
        out += ', '.join([str(self.data[_]) for _ in range(self.size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self.data[self.index]
        except StaticArrayException:
            raise StopIteration
        self.index = self.index + 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        return self.data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self.size:
            raise DynamicArrayException
        self.data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.size

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        This method changes the capacity of the underlying storage for the array elements.
        """

        if new_capacity==0:
            return self

        if new_capacity < 0 or new_capacity < self.size:
            return

        new_arr = static_array.StaticArray(new_capacity) #static array with larger capacity to base current dynamic array off of

        for item in range(self.length()):
            new_arr[item] = self[item]

        self.data = new_arr
        self.capacity = new_capacity

        return self

    def append(self, value: object) -> None:
        """
        This method adds a new value at the end of the dynamic array.
        If the array is full the capacity is doubled before adding the new value
        """
        if self.size == self.capacity: #double capacity and copy over values from old underlying static array to the new one

            new_arr = static_array.StaticArray(self.capacity * 2)

            for item in range(self.length()):
                new_arr[item] = self[item]

            self.data = new_arr
            self.capacity = self.capacity * 2
            self.size += 1

            self[self.size - 1] = value

        elif self.is_empty() == True: #if array is empty, add 1 to size and insert at begining of array
            self.size = 1
            self[0] = value

        else:
            self.size += 1
            self[self.size - 1] = value

        return self

    def insert_at_index(self, index: int, value: object) -> None:
        """
        This method adds a new value at the specified index position in the dynamic array
        """
        if index > self.capacity or index < 0:
            raise DynamicArrayException

        if self.size == self.capacity: #Double capacity
            self.resize(self.capacity * 2)

        if index<self.size+1:     #add one to size
            self.size += 1

        if self[index] != None:
            for num in range(self.size):
                self[(self.size - 1) - num] = self[((self.size - 2) - num)] #every item after index to be inserted is shifted up one
                if (self.size - 2) - num == index:  # if we are at the index that has now been cleared to add new value, leave loop
                    break

        self[index] = value

    def remove_at_index(self, index: int) -> None:
        """
        This method removes the element at the specified index from the dynamic array
        """
        if index<0 or index>=self.size:
            raise DynamicArrayException

        if self.size<(self.capacity/4) and self.capacity>10: #set static array capacity if current size is 1/4th of capacity
            if (self.size * 2)>=10:
                new_arr = static_array.StaticArray(self.size * 2)

                for item in range(self.length()):
                    new_arr[item] = self[item]

                self.data = new_arr
                self.capacity = self.size * 2

            elif (self.size * 2)<10:
                new_arr = static_array.StaticArray(10) #if size*2 is less than 10 give new static array capacity 10

                for item in range(self.length()):
                    new_arr[item] = self[item]

                self.data = new_arr
                self.capacity = 10

        if index==self.size-1: #if given index is last item in dynamic array
            self[index]=None

        else:
            for num in range(self.length()-index):
                if (num+index) == self.length()-1:  # if we are at the end of the dynamic array leave loop
                    break
                self[num+index] = self[num+index+1]

        self.size-=1


    def slice(self, start_index: int, size: int) -> object:
        """
        This method returns a new Dynamic Array object that contains the requested number of
        elements from the original array starting with the element located at the requested start
        index.
        """
        if start_index < 0 or start_index >= self.size or size<0:
            raise DynamicArrayException

        if size==0:
            return DynamicArray([])

        static_slice= StaticArray(size)

        for item in range(size):
            if self[item+start_index]==None: #catching if there are not enough elements between start and end of requested slice
                raise DynamicArrayException
            else:
                static_slice[item]=self[item+start_index] #building static array

        dynamic_slice = DynamicArray()

        for item in range(static_slice.length()):
            dynamic_slice.append(static_slice[item])   #populating dynamic array with values in static

        return dynamic_slice


    def merge(self, second_da: object) -> None:
        """
        This method takes another Dynamic Array object as a parameter, and appends all elements
        from this other array onto the current one.
        """
        if second_da.length()==0:
            return

        for item in range(second_da.length()):
            self.append(second_da[item])

    def map(self, map_func) -> object:
        """
        This method creates a new Dynamic Array where the value of each element is derived by
        applying a given map_func to the corresponding value from the original array
        """
        new_arr=DynamicArray()
        new_arr.size=self.size
        new_arr.capacity=self.capacity
        new_arr.data= StaticArray(new_arr.capacity) #build out new array with all attributes of passed in array except it is empty

        for item in range(self.length()):
            new_arr[item]=map_func(self[item])

        return new_arr

    def filter(self, filter_func) -> object:
        """
        This method creates a new Dynamic Array populated only with those elements from the
        original array for which filter_func returns True.
        """
        new_arr=DynamicArray()

        for item in range(self.length()):
            if filter_func(self[item])==True: #apply filter to all values in original array
                new_arr.append(self[item])
            else:
                continue

        return new_arr

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        This method sequentially applies the reduce_func to all elements of the Dynamic Array and
        returns the resulting value.
        """
        if self.is_empty()==True:
            return initializer

        if initializer==None:
            reduction=self[0]
            for item in range(self.length()-1):
                reduction+=reduce_func(0, self[item+1])  # apply filter to all values in original array

        else:
            reduction=initializer
            for item in range(self.length()):
                reduction+=reduce_func(0, self[item])  # apply filter to all values in original array

        return reduction


def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """
    a standalone function outside of the Dynamic Array class that receives a
    DynamicArray that is sorted in order, either non-descending or non-ascending. The function
    will return a tuple containing (in this order) a DynamicArray comprising the mode
    (most-occurring) values in the array, and an integer that represents the highest frequency
    (how many times they appear)
    """
    second_count = 0  # tracks the number of times a different value that occurs more than once occurs
    second = 0  # a different value that occurs more than once occurs
    first = 0  # a value that occurs more than once occurs
    first_count = 0  # tracks the number of times a value that occurs more than once occurs
    count_arr=DynamicArray()
    count_to_beat=0

    for num in range(arr.length()):

        if arr.length() == 1:
            first_count = 1
            first = arr[0]
            break

        if second_count > first_count:  # if number of second multiple occuring value surpasses first, switch and reset second
            count_to_beat=first_count
            first_count = second_count
            first = second
            second_count = 0
            second = 0

        if num < (arr.length() - 1):  # if not at end of array start tracking multiple occuring numbers
            if arr[num] == arr[
                num + 1] and first == 0:  # if current number equals next and first is blank this is the new first
                first_count = 1
                first = arr[num]

            elif arr[num] == arr[num + 1] and arr[
                num] == first:  # if current number equals next and it equals first add to first
                first_count += 1

            elif arr[num] == arr[num + 1] and arr[
                num] != first and second == 0:  # if current number equals next but is not first this is new second
                second_count = 1
                second = arr[num]

            elif arr[num] == arr[num + 1] and arr[
                num] == second:  # if current number equals next and it equals second add to second
                second_count += 1

            elif arr[num] == arr[num + 1] and arr[num] != first and arr[num] != second:
                second_count = 1  # if current number equals next and it does not equal second or first reset second
                second = arr[num]

            elif num != 0:
                if arr[num] == arr[num - 1] and arr[num] != arr[num + 1] and arr[
                    num] == first:  # if current number equals previous and does not equal next and it equals first add to first
                    first_count += 1
                    count_arr.append(first)
                    count_to_beat=first_count

                elif arr[num] == arr[num - 1] and arr[num] != arr[num + 1] and arr[
                    num] == second:  # if current number equals previous and does not equal next it equals second add to second
                    second_count += 1
                    if second_count==count_to_beat:
                        count_arr.append(second)
                        second_count = 0
                        second = 0

                    elif second_count > first_count:  # if number of second multiple occuring value surpasses first, switch and reset second
                        count_to_beat = second_count
                        first_count = second_count
                        first = second
                        second_count = 0
                        second = 0

                        for item in range(count_arr.length()):
                            count_arr.remove_at_index(item)

                        count_arr.append(first)
        else:  # if at end of array
            if arr[num] == arr[num - 1] and arr[num] == first:
                first_count += 1
                count_arr.append(first)

            elif arr[num] == arr[num - 1] and arr[num] == second:
                second_count += 1

            if second_count == count_to_beat:
                count_arr.append(second)

            elif second_count > first_count:  # if number of second multiple occuring value surpasses first, switch and reset second
                count_to_beat = second_count
                first_count = second_count
                first = second
                second_count = 0
                second = 0

                for item in range(count_arr.length()):
                    count_arr.remove_at_index(item)

                count_arr.append(first)

    if first_count == 0 and first == 0:  # if original arr is one element long
        first_count = 1
        first = arr[0]

    return (count_arr, first_count)

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.resize(8)
    print(da.size, da.capacity, da.data)
    da.resize(2)
    print(da.size, da.capacity, da.data)
    da.resize(0)
    print(da.size, da.capacity, da.data)


    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)


    print("\n# append - example 1")
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.append(1)
    print(da.size, da.capacity, da.data)
    print(da)


    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)


    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.size)
    print(da.capacity)


    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)


    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)


    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)


    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.size, da.capacity)
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)


    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.size, da.capacity)
    [da.append(1) for i in range(100)]          # step 1 - add 100 elements
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 3 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 4 - remove 1 element
    print(da.size, da.capacity)
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 6 - remove 1 element
    print(da.size, da.capacity)
    da.remove_at_index(0)                       # step 7 - remove 1 element
    print(da.size, da.capacity)

    for i in range(14):
        print("Before remove_at_index(): ", da.size, da.capacity, end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.size, da.capacity)


    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)


    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")


    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)


    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)


    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))


    print("\n# map example 2")
    def double(value):
        return value * 2

    def square(value):
        return value ** 2

    def cube(value):
        return value ** 3

    def plus_one(value):
        return value + 1

    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))


    print("\n# filter example 1")
    def filter_a(e):
        return e > 10

    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))


    print("\n# filter example 2")
    def is_long_word(word, length):
        return len(word) > length

    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))


    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 4, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot", "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
