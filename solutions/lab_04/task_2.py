class StepRangeIterator:
    def __init__(self, step_range: "StepRange") -> None:
        self._step_range = step_range
        self._current: int | None = step_range.start

    def __iter__(self) -> "StepRangeIterator":
        return self

    def __next__(self) -> int:
        if self._current is None:
            raise StopIteration
        value = self._current
        sr = self._step_range
        if sr.step > 0 and value >= sr.stop:
            self._current = None
            raise StopIteration
        if sr.step < 0 and value <= sr.stop:
            self._current = None
            raise StopIteration
        self._current = value + sr.step
        return value

class StepRange:
    def __init__(self, start: int, stop: int, step: int) -> None:
        if step == 0:
            raise ValueError("Шаг не может быть нулевым")
        self.start: int = start
        self.stop: int = stop
        self.step: int = step

    def __iter__(self) -> StepRangeIterator:
        return StepRangeIterator(self)

    def __len__(self) -> int:
        if self.step > 0:
            if self.start >= self.stop:
                return 0
            return (self.stop - self.start - 1) // self.step + 1
        else:
            if self.start <= self.stop:
                return 0
            return (self.start - self.stop - 1) // (-self.step) + 1

    def __contains__(self, value: int) -> bool:
        if self.step > 0:
            if value < self.start or value >= self.stop:
                return False
        else:
            if value > self.start or value <= self.stop:
                return False
        return (value - self.start) % self.step == 0

    def __repr__(self) -> str:
        return f"StepRange({self.start}, {self.stop}, {self.step})"


if __name__ == "__main__":
    print("=== Тестовые случаи ===")
    print(f"list(StepRange(0, 5, 1)) -> {list(StepRange(0, 5, 1))}")
    print(f"list(StepRange(5, 0, -1)) -> {list(StepRange(5, 0, -1))}")
    print(f"list(StepRange(0, 0, 1)) -> {list(StepRange(0, 0, 1))}")
    print(f"list(StepRange(0, 5, -1)) -> {list(StepRange(0, 5, -1))}")
    print("\n=== Два итератора ===")
    sr = StepRange(0, 10, 1)
    it_a = iter(sr)
    it_b = iter(sr)
    print("Поочерёдные вызовы next(): ")
    for i in range(6):
        try:
            a_val = next(it_a)
        except StopIteration:
            a_val = "StopIteration"
        try:
            b_val = next(it_b)
        except StopIteration:
            b_val = "StopIteration"
        print(f"шаг {i}: it_a -> {a_val}, it_b -> {b_val}")

    print("\n=== Практическое расширение ===")
    print("=== Сравнение __contains__() и обхода диапазона ===")
    big_range = StepRange(0, 10000000, 1)
    value = 9999999

    res_contains = value in big_range
    print(f"{value} in big_range через __contains__(): {res_contains}, операций - 1")

    found = False
    ops = 0
    for val in big_range:
        ops += 1
        if val == value:
            found = True
            break
    print(f"Операций в полном обходе: {ops}")