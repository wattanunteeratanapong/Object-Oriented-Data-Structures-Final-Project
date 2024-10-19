# Hilbert Hotel
# Case 1 (N Customer)
# Add a new guest by shifting all existing guests one room up
import time
import sys
import tracemalloc

class HilbertHotel:
    def __init__(self):
        self.rooms = {}  

    def add_guest(self, guest):
        tracemalloc.start()
        start_time = time.perf_counter()

        max_room = max(self.rooms.keys()) if self.rooms else 0
        for room in range(max_room, 0, -1):
            self.rooms[room + 1] = self.rooms[room]
        self.rooms[1] = guest

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Guest \"{guest}\" has been added to the hotel.")
        print(f"Runtime for add_guest: {end_time - start_time:.6f} seconds")
        print(f"Current memory usage: {current} bytes; Peak was {peak} bytes\n")
        print()

    def delete_guest(self, room):
        tracemalloc.start()
        start_time = time.perf_counter()

        if room in self.rooms:
            guest = self.rooms.pop(room)
            print(f"Removed guest \"{guest}\" from Room {room}.")
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
            print(f"Guest \"{self.rooms[room]}\" is in Room {room}.")
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
        for room in range(1, max_room + 1):
            if room not in self.rooms:
                print(f"Room {room}: No Guest")
                has_empty = True
        if not has_empty:
            print("No empty rooms available.")

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Runtime for show_empty_rooms: {end_time - start_time:.6f} seconds")
        print(f"Current memory usage: {current} bytes; Peak was {peak} bytes\n")
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
                print(f"Room {room}: Guest {self.rooms[room]}")
            else:
                print(f"Room {room}: No Guest")
        print("----------------------------------")
        print()

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Runtime for print_rooms: {end_time - start_time:.6f} seconds")
        print(f"Current memory usage: {current} bytes; Peak was {peak} bytes\n")
        print()


# Hilbert Hotel Simulation
hotel = HilbertHotel()

hotel.add_guest('Alice')
hotel.add_guest('Bob')
hotel.add_guest('Charlie')
hotel.print_rooms()

hotel.add_guest('Ping Ping')
hotel.add_guest('Porsche')
hotel.add_guest('Tart')
hotel.add_guest('Tee')
hotel.print_rooms()

hotel.search_room_number(3)
hotel.delete_guest(2)
hotel.delete_guest(4)
hotel.print_rooms()
hotel.show_empty_rooms()
