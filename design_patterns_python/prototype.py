from __future__ import annotations
import copy
from typing import List, Dict


class DataPrototype:
    """Prototype"""

    def __init__(self, data: List[int, List[int]] = None) -> None:
        self.data = data

    def __copy__(self) -> DataPrototype:
        new = self.__class__(copy.copy(self.data))
        new.__dict__.update(self.__dict__)
        return new

    def __deepcopy__(self, memo: Dict = {}) -> DataPrototype:
        new = self.__class__(copy.deepcopy(self.data, memo))
        new.__dict__.update(self.__dict__)
        return new

    def __str__(self) -> str:
        return f'{self.data}'


if __name__ == '__main__':
    data_one = DataPrototype([5, [7, 2], 3])
    print(f'The original elements of "data_one" '
          f'before shallow copying: \n{str(data_one)}')
    copied_color = copy.copy(data_one)
    copied_color.data[1][0] = 12
    print(f'The original elements of "data_one" '
          f'after shallow copying: \n{str(data_one)}')

    data_two = DataPrototype([65, [7, 12], 22])
    print(f'The original elements of "data_two" '
          f'before deep copying: \n{str(data_two)}')
    deepcopied_color = copy.deepcopy(data_one)
    deepcopied_color.data[1][0] = 33
    print(f'The original elements of "data_two" '
          f'after deep copying: \n{str(data_two)}')

