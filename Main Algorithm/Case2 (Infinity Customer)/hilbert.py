# Hilbert Hotel
# Case 2 (∞ Customer)
# Add a new guest by shifting all existing guests odd even rooms up
import time
import sys
import tracemalloc

class HilbertHotel:
    def __init__(self):
        self.rooms = {} 

    def add_guest(self, customer_list):
        tracemalloc.start()
        start_time = time.perf_counter()

        if not self.rooms:  
            for i, guest in enumerate(customer_list, start=1):
                self.rooms[i] = f"{guest}"
        else:
            max_room = max(self.rooms.keys()) 
            count = max_room - len(customer_list) 

            for room in range(max_room, 0, -1):
                if room <= len(customer_list):
                    self.rooms[room * 2] = self.rooms[room]
                    del self.rooms[room]
                else:
                    self.rooms[room * 2 - count] = self.rooms[room]
                    del self.rooms[room]
                    count -= 1  
            self.print_rooms()

            next_room = 1
            for guest in customer_list:
                while next_room in self.rooms:
                    next_room += 1
                self.rooms[next_room] = f"{guest}"
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
            print(f"Removed \"{guest}\" from Room {room}.")
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
            print(f"Found \"{self.rooms[room]}\" in room {room}.")
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
                print(f"Room {room}: No Guest")
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

# First set of customers
customer_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
hotel.add_guest(customer_list)
hotel.print_rooms()

# Second set of customers
customer_list = ['A', 'B', 'C', 'D', 'E']
hotel.add_guest(customer_list)
hotel.print_rooms()

# Third set of customers
customer_list = ['F', 'G']
hotel.add_guest(customer_list)
hotel.print_rooms()

hotel.delete_guest(1)
hotel.delete_guest(2)
hotel.delete_guest(3)
hotel.search_room_number(4)
hotel.search_room_number(1)
hotel.show_empty_rooms()
