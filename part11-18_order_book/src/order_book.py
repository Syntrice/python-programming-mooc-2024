# Write your solution here:


class Task:

    task_number: int = 1

    def __init__(self, description: str, programmer: str, workload: int) -> None:
        self.description: str = description
        self.programmer: str = programmer
        self.workload: int = workload
        self.__is_finished: bool = False
        self.id: int = Task.task_number
        Task.task_number += 1

    def is_finished(self) -> bool:
        return self.__is_finished

    def mark_finished(self) -> None:
        self.__is_finished = True

    def __str__(self) -> str:
        finished_string = "FINISHED" if self.__is_finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {finished_string}"


class OrderBook:

    def __init__(self) -> None:
        self.__orders: dict[int, Task] = {}

    def add_order(self, description: str, programmer: str, workload: int) -> None:
        new_order = Task(description, programmer, workload)

        self.__orders[new_order.id] = new_order

    def all_orders(self) -> list[Task]:
        return list(self.__orders.values())

    def programmers(self) -> list[str]:
        return list(set([order.programmer for order in self.__orders.values()]))

    def mark_finished(self, id: int) -> None:
        if id not in self.__orders:
            raise ValueError(f"no such order with ID '{id}'")
        self.__orders[id].mark_finished()

    def finished_orders(self) -> list[Task]:
        return [order for order in self.__orders.values() if order.is_finished()]

    def unfinished_orders(self) -> list[Task]:
        return [order for order in self.__orders.values() if not order.is_finished()]
    
    def status_of_programmer(self, programmer: str) -> tuple[int, int, int, int]:
        
        finished = [order for order in self.finished_orders() if order.programmer == programmer]
        unfinished = [order for order in self.unfinished_orders() if order.programmer == programmer]
        
        if not (bool(finished) or bool(unfinished)):
            raise ValueError("No such programmer")
        
        finished_hours = sum(order.workload for order in finished)
        
        unfinished_hours = sum(order.workload for order in unfinished)
    
        return (len(finished), len(unfinished), finished_hours, unfinished_hours)


if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)

    orders.mark_finished(1)
    orders.mark_finished(2)

    for order in orders.all_orders():
        print(order)
