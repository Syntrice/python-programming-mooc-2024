# Write your solution here
# If you use the classes made in the previous exercise, copy them here


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

        finished = [
            order for order in self.finished_orders() if order.programmer == programmer
        ]
        unfinished = [
            order
            for order in self.unfinished_orders()
            if order.programmer == programmer
        ]

        if not (bool(finished) or bool(unfinished)):
            raise ValueError("No such programmer")

        finished_hours = sum(order.workload for order in finished)

        unfinished_hours = sum(order.workload for order in unfinished)

        return (len(finished), len(unfinished), finished_hours, unfinished_hours)


class OrderBookApplication:

    def __init__(self) -> None:
        self.orders = OrderBook()

    def add_order(self) -> None:
        description = input("description: ")
        
        try:
            programmer, workload = input("programmer and workload estimate: ").split(" ")
        except:
            print("erroneous input")
            return
        
            
        if not workload.isnumeric():
            print("erroneous input")
            return

        
        self.orders.add_order(description, programmer, int(workload))
        print("added!")

    def list_finished_tasks(self) -> None:
        finished_orders = self.orders.finished_orders()

        if len(finished_orders) == 0:
            print("no finished tasks")
            return
        
        for order in finished_orders:
            print(order)

    def list_unfinished_tasks(self) -> None:
        unfinished_orders = self.orders.unfinished_orders()

        if len(unfinished_orders) == 0:
            print("no unfinished tasks")
            return
        
        for order in unfinished_orders:
            print(order)

    def mark_finished(self) -> None:
        id = input("id: ")
        
        if not id.isnumeric():
            print("erroneous input")
            return
        
        id = int(id)
        
        if id > Task.task_number:
            print("erroneous input")
            return
        
        self.orders.mark_finished(id)
        print("marked as finished")
        

    def programmers(self) -> None:
        try:
            programmers = self.orders.programmers()
        except ValueError:
            print("erroneous input")
            return
        
        for order in programmers:
            print(order)
        

    def programmer_status(self) -> None:
        programmer = input("programmer: ")
        try:
            programmer_data = self.orders.status_of_programmer(programmer)
        except:
            print("erroneous input")
            return
            
            
        print(f"tasks: finished {programmer_data[0]} not finished {programmer_data[1]}, hours: done {programmer_data[2]} scheduled {programmer_data[3]}")

    def print_help(self) -> None:
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")
        print("")

    def execute(self) -> None:

        self.print_help()

        while True:

            command = input("command: ")

            match command:

                case "0":
                    break
                case "1":
                    self.add_order()
                case "2":
                    self.list_finished_tasks()
                case "3":
                    self.list_unfinished_tasks()
                case "4":
                    self.mark_finished()
                case "5":
                    self.programmers()
                case "6":
                    self.programmer_status()


application = OrderBookApplication()
application.execute()
