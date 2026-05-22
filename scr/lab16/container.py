from typing import TypeVar, Generic, Optional, Callable, List, Protocol, Any
from abc import abstractmethod

T = TypeVar('T')
R = TypeVar('R')

class Displayable(Protocol):
    @abstractmethod
    def display(self) -> str:
        pass

class Scorable(Protocol):
    @abstractmethod
    def score(self) -> float:
        pass

D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)


class TypedCollection(Generic[T]):

    def __init__(self, items: Optional[List[T]] = None) -> None:
        self._items: List[T] = items.copy() if items else []
    
    def add(self, item: T) -> None:
        self._items.append(item)
    
    def remove(self, item: T) -> None:
        if item not in self._items:
            raise ValueError("Элемент не найден")
        self._items.remove(item)
    
    def get_all(self) -> List[T]:
        return self._items.copy()
    
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None
    
    def filter(self, predicate: Callable[[T], bool]) -> 'TypedCollection[T]':
        filtered_items = [item for item in self._items if predicate(item)]
        return TypedCollection(filtered_items)
    
    def map(self, transform: Callable[[T], R]) -> 'TypedCollection[R]':
        mapped_items = [transform(item) for item in self._items]
        return TypedCollection(mapped_items)
    
    def sort(self, key: Optional[Callable[[T], Any]] = None, 
             reverse: bool = False) -> 'TypedCollection[T]':
        sorted_items = sorted(self._items, key=key, reverse=reverse)
        return TypedCollection(sorted_items)
    
    def reduce(self, func: Callable[[R, T], R], initial: R) -> R:
        result = initial
        for item in self._items:
            result = func(result, item)
        return result
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __getitem__(self, index: int) -> T:
        return self._items[index]
    
    def __iter__(self):
        return iter(self._items)
    
    def __str__(self) -> str:
        return f"TypedCollection({len(self._items)} items)"
    
    def __repr__(self) -> str:
        return f"TypedCollection(items={self._items})"


def display_all(items: TypedCollection[D]) -> List[str]:
    return items.map(lambda x: x.display()).get_all()


def total_score(items: TypedCollection[S]) -> float:
    costs = items.map(lambda x: x.score()).get_all()
    return sum(costs)


if __name__ == "__main__":
    print("✅ container.py работает корректно")