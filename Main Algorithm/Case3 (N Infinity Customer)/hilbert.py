# Hilbert Hotel
# Case3 (N × Infinity Customer)
import time
import sys
import tracemalloc

class Customer:
    def __init__(self, name, approach=None):
        self.name = name
        self.approach = approach

    def __str__(self):
        return self.name

class HilbertHotel:
    def __init__(self):
        self.rooms = {}  

    def add_guest(self, all_customer_line_list):
        tracemalloc.start()
        start_time = time.perf_counter()

        max_room = max(self.rooms.keys(), default=0) 

        num_all_customer = sum(len(line[1]) for line in all_customer_line_list)
        new_max_room = max_room + num_all_customer 

        for room in range(max_room, 0, -1):
            if room in self.rooms:  
                self.rooms[room * 2] = self.rooms[room] 
                del self.rooms[room]

        next_room = 1
        for boat_name, line in all_customer_line_list:
            for guest_name in line:
                while next_room in self.rooms: 
                    next_room += 1
                self.rooms[next_room] = Customer(guest_name, approach=boat_name)
                next_room += 1

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Runtime for add_guest: {end_time - start_time:.6f} seconds")
        print(f"Current memory usage: {current} bytes; Peak was {peak} bytes\n")
        print()

    def delete_guest(self, room):
        tracemalloc.start()
        start_time = time.perf_counter()

        if room in self.rooms:
            guest = self.rooms.pop(room)
            print(f"Removed {guest} from Room {room}. Room is now empty.")
        else:
            print(f"Room {room} is already empty or does not exist.")

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Runtime for delete_guest: {end_time - start_time:.6f} seconds")
        print(f"Current memory usage: {current} bytes; Peak was {peak} bytes\n")
        print()


    def search_room_number(self, room):
        tracemalloc.start()
        start_time = time.perf_counter()

        if room in self.rooms:
            guest = self.rooms[room]
            print(f"Room {room} : {guest.name} ({guest.approach})")
        else:
            print(f"Room {room} is empty or does not exist.")

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Runtime for search_room_number: {end_time - start_time:.6f} seconds")
        print(f"Current memory usage: {current} bytes; Peak was {peak} bytes\n")
        print()

    def show_empty_rooms(self):
        tracemalloc.start()
        start_time = time.perf_counter()

        max_room = max(self.rooms.keys()) if self.rooms else 0
        has_empty = False
        print()
        print()
        print("----------- Empty Room -----------")
        for room in range(1, max_room + 1):
            if room not in self.rooms:
                print(f"Room {room}: No Guest")
                has_empty = True
        print("----------------------------------")
        if not has_empty:
            print("No empty rooms available.")

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Runtime for show_empty_rooms: {end_time - start_time:.6f} seconds")
        print(f"Current memory usage: {current} bytes; Peak was {peak} bytes\n")
        print()
        print()
        print()
        print()

    def print_rooms(self):
        tracemalloc.start()
        start_time = time.perf_counter()

        print()
        print()
        print("--------------- Room -------------")
        max_room = max(self.rooms.keys()) if self.rooms else 0
        for room in range(1, max_room + 1):
            if room in self.rooms:
                print(f"Room {room}: {self.rooms[room]}")
            else:
                print(f"Room {room}: Empty Room")
        print("----------------------------------")

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Runtime for print_rooms: {end_time - start_time:.6f} seconds")
        print(f"Current memory usage: {current} bytes; Peak was {peak} bytes\n")
        print()
        print()
        print()
        print()


# Hilbert Hotel Simulation
hotel = HilbertHotel()

all_customer_line_list = [
    ["Bus1", ['A', 'B', 'C', 'D', 'E', 'F', 'G']],
    ["Bus2", ['H', 'I', 'J', 'K']],
    ["Bus3", ['L', 'M']]
]
hotel.add_guest(all_customer_line_list)
hotel.print_rooms()

hotel.search_room_number(1)  
hotel.search_room_number(8) 
hotel.search_room_number(14) 

hotel.delete_guest(1)
hotel.delete_guest(8)
hotel.print_rooms()

hotel.show_empty_rooms()
