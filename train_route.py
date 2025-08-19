
# Node for Doubly Linked List

class StationNode:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None


# Train Route (Doubly Linked List)

class TrainRoute:
    def __init__(self, circular=False):
        self.head = None
        self.tail = None
        self.circular = circular

    # Add a station
    def add_station(self, name):
        new_station = StationNode(name)
        if not self.head:
            self.head = self.tail = new_station
            if self.circular:
                self.head.next = self.head.prev = self.head
            return
        if self.circular:
            new_station.prev = self.tail
            new_station.next = self.head
            self.tail.next = new_station
            self.head.prev = new_station
            self.tail = new_station
        else:
            new_station.prev = self.tail
            self.tail.next = new_station
            self.tail = new_station

    # Traverse forward
    def traverse_forward(self, steps=5):
        if not self.head:
            print("⚠️ No stations in route")
            return
        print("➡️ Forward Navigation:")
        current = self.head
        count = 0
        while current and count < steps:
            print(f"🚉 {current.name}")
            current = current.next
            count += 1
            if self.circular and current == self.head:
                break

    # Traverse backward
    def traverse_backward(self, steps=5):
        if not self.tail:
            print("⚠️ No stations in route")
            return
        print("⬅️ Backward Navigation:")
        current = self.tail
        count = 0
        while current and count < steps:
            print(f"🚉 {current.name}")
            current = current.prev
            count += 1
            if self.circular and current == self.tail:
                break


# Simulation Example

if __name__ == "__main__":
    print("===== Linear Route Example =====")
    linear_route = TrainRoute(circular=False)
    linear_route.add_station("Station A")
    linear_route.add_station("Station B")
    linear_route.add_station("Station C")
    linear_route.add_station("Station D")

    linear_route.traverse_forward()
    linear_route.traverse_backward()

    print("\n===== Circular Route Example =====")
    circular_route = TrainRoute(circular=True)
    circular_route.add_station("Metro 1")
    circular_route.add_station("Metro 2")
    circular_route.add_station("Metro 3")
    circular_route.add_station("Metro 4")

    circular_route.traverse_forward(6)  # Loop around
    circular_route.traverse_backward(6)
