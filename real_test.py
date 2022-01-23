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
        TODO: Write this implementation
        """
        if new_capacity < 0 or new_capacity < self.size:
            return

        new_arr = static_array.StaticArray(new_capacity)

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
        if self.size == self.capacity:

            new_arr = static_array.StaticArray(self.capacity*2)

            for item in range(self.length()):
                new_arr[item] = self[item]

            self.data=new_arr
            self.capacity=self.capacity*2
            self.size+=1

            self[self.size-1]=value

        elif self.is_empty()==True:
            self.size=1
            self[0]=value

        else:
            self.size+=1
            self[self.size-1]=value

        return self

    def insert_at_index(self, index: int, value: object) -> None:
        """
        This method adds a new value at the specified index position in the dynamic array
        """
        if index>=self.capacity or index<0:
            raise DynamicArrayException

        if self.size==self.capacity:
            self.resize(self.capacity*2)

        self.size+=1
        if self[index]!=None:
            for num in range(self.size):
                self[(self.size-1)-num]=self[((self.size-2)-num)]
                if (self.size-2)-num==index:       #if we are at the index that has now been cleared to add new value leave loop
                    break

        self[index]=value


da = DynamicArray([100])
print(da)
da.insert_at_index(0, 200)
print(da)
da.insert_at_index(0, 300)
print(da)
da.insert_at_index(0, 400)
print(da)
da.insert_at_index(3, 500)
print(da)
da.insert_at_index(1, 600)
print(da)