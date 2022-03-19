class Counter:
    def __init__(self, array_list, pointer_):
        self.array = array_list

        self.pointer = pointer_

        self._winner = self.start_play(self.array, self.pointer)

    @staticmethod
    def start_play(array, pointer):
        # if len of array consist of one element => O(1)
        if len(array) == 1:
            return array[-1]

        # if pointer is "1" => return last elem => O(1)
        if pointer == 1:
            return array[-1]

        if len(array) == 2 and pointer == 2:
            return array[0]

        if pointer > 1:
            # point of stopping in the arrray
            point_of_stop = 0

            new_array = array

            while new_array:  # => O(N)

                # if len of array consist of one element => O(1)
                if len(new_array) == 1:
                    return new_array[-1]

                if pointer + point_of_stop > len(new_array):
                    array_for_search_elem = new_array * (pointer + point_of_stop)

                    find_elem = array_for_search_elem.pop(pointer + point_of_stop - 1)

                    point_of_stop = new_array.index(find_elem)
                    new_array.remove(find_elem)
                    continue

                del new_array[point_of_stop + pointer - 1]
                point_of_stop += pointer - 1

    # ----------------------------------------------------------------------------
    @property
    def array(self):
        return self._array

    @array.setter
    def array(self, array_list):
        self.is_valid_array(array_list)
        self._array = array_list

    # ----------------------------------------------------------------------------

    @property
    def pointer(self):
        return self._pointer

    @pointer.setter
    def pointer(self, pointer_):
        self.is_valid_pointer(pointer_)
        self._pointer = pointer_

    # ----------------------------------------------------------------------------
    @property
    def winner(self):
        return self._winner

    # ----------------------------------------------------------------------------
    @staticmethod
    def is_valid_array(array_list):
        if not array_list:
            raise ValueError('Count of gamers must be more than 0. ')

        if not isinstance(array_list, list):
            raise ValueError('First argument of class must be "list" type')

        if list(set(array_list)) != array_list:
            raise ValueError('List of gamers must be uniq')

    @staticmethod
    def is_valid_pointer(pointer):
        if pointer < 1 or not isinstance(pointer, int):
            raise ValueError('Your counter must be more than "0" and '
                             'counter must be "int" type. ')


who_win_1 = Counter([20, 21, 22, 23, 24, 25], 3)  # 20
print(who_win_1.winner)

who_win_2 = Counter([1, 2, 3, 4, 5, 6], 4)  # 5
print(who_win_2.winner)
