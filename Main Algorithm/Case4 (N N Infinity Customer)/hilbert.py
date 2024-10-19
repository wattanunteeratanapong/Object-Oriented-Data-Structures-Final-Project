# Hilbert Hotel
# Case4 (N x N × Infinity Customer)
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

        if not self.rooms:  
            for i, guest_name in enumerate(all_customer_line_list[0][1], start=1):
                guest = Customer(guest_name, approach=all_customer_line_list[0][0]) 
                self.rooms[i] = guest
            all_customer_line_list.pop(0)  
            if all_customer_line_list:
                self.add_guest(all_customer_line_list)  
        else:
            max_room = max(self.rooms.keys()) 
            num_all_customer = sum(len(line[1]) for line in all_customer_line_list)  
            count = max_room + num_all_customer
            line_count = len(all_customer_line_list)

            for room in range(max_room, 0, -1):
                if room <= line_count:
                    self.rooms[room * 2] = self.rooms[room]  
                else:
                    self.rooms[count] = self.rooms[room] 
                    count -= 1
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
            print(f"Removed guest {guest} from Room {room}.")
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
                print(f"Room {room}: Guest {self.rooms[room]}")
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

def flatten_list(nested_list, prefix=''):
    flat_list = []
    
    for item in nested_list:
        if isinstance(item, list) and len(item) > 1:
            if isinstance(item[1], list) and all(isinstance(i, str) for i in item[1]):
                new_prefix = f"{prefix}-{item[0]}" if prefix else item[0]
                flat_list.append([new_prefix, item[1]])
            else:
                new_prefix = f"{prefix}-{item[0]}" if prefix else item[0]
                flat_list.extend(flatten_list(item[1], new_prefix))
        else:
            continue

    return flat_list



# Test Case 1 (2 Layers)
# all_customer_line_list = [
#     ["Airplane1", [
#         ["Boat1", ['A', 'B', 'C', 'D', 'E', 'F', 'G']],
#         ["Boat2", ['H', 'I', 'J', 'K']],
#         ["Boat3", ['L', 'M']]
#     ]],
#     ["Airplane2", [
#         ["Boat4", ['N', 'O', 'P', 'Q', 'R', 'S', 'T']],
#         ["Boat5", ['U', 'V', 'W', 'X']],
#         ["Boat6", ['Y', 'Z']]
#     ]]
# ]

# all_customer_line_list = flatten_list(all_customer_line_list)

# hotel.add_guest(all_customer_line_list)
# hotel.print_rooms()

# hotel.search_room_number(1)  
# hotel.search_room_number(8) 
# hotel.search_room_number(14) 

# hotel.delete_guest(1)
# hotel.delete_guest(8)
# hotel.delete_guest(14)
# hotel.show_empty_rooms()



# Test Case 2 (3 Layers)
# all_customer_line_list = [
#     ["Helicopter1", [
#         ["Airplane1", [["Boat1", ['A', 'B', 'C', 'D', 'E', 'F', 'G']],
#         ["Boat2", ['H', 'I', 'J', 'K']],
#         ["Boat3", ['L', 'M']]]],
#         ["Airplane2", [["Boat4", ['N', 'O', 'P', 'Q', 'R', 'S', 'T']],
#         ["Boat5", ['U', 'V', 'W', 'X']],
#         ["Boat6", ['Y', 'Z']]]]
#     ]],
#     ["Helicopter2", [
#         ["Airplane1", [["Boat1", ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG']],
#         ["Boat2", ['HH', 'II', 'JJ', 'KK']],
#         ["Boat3", ['LL', 'MM']]]],
#         ["Airplane2", [["Boat4", ['NN', 'OO', 'PP', 'QQ', 'RR', 'SS', 'TT']],
#         ["Boat5", ['UU', 'VV', 'WW', 'XX']],
#         ["Boat6", ['YY', 'ZZ']]]]
#     ]]
# ]

# flattened_line_list = flatten_list(all_customer_line_list)

# all_customer_line_list = flatten_list(all_customer_line_list)

# hotel.add_guest(all_customer_line_list)
# hotel.print_rooms()

# hotel.search_room_number(1)  
# hotel.search_room_number(8) 
# hotel.search_room_number(14) 
# hotel.search_room_number(52) 

# hotel.delete_guest(1)
# hotel.delete_guest(8)
# hotel.delete_guest(14)
# hotel.show_empty_rooms()


# Test Case 3 (4 Layers)
all_customer_line_list = [
    ["Carrier1", [
        ["Helicopter1", [
            ["Airplane1", [
                ["Boat1", ['A', 'B', 'C', 'D', 'E', 'F', 'G']],
                ["Boat2", ['H', 'I', 'J', 'K']],
                ["Boat3", ['L', 'M']]
            ]],
            ["Airplane2", [
                ["Boat4", ['N', 'O', 'P', 'Q', 'R', 'S', 'T']],
                ["Boat5", ['U', 'V', 'W', 'X']],
                ["Boat6", ['Y', 'Z']]
            ]]
        ]],
        ["Helicopter2", [
            ["Airplane3", [
                ["Boat7", ['AA', 'BB', 'CC', 'DD']],
                ["Boat8", ['EE', 'FF', 'GG', 'HH']],
                ["Boat9", ['II', 'JJ']]
            ]],
            ["Airplane4", [
                ["Boat10", ['KK', 'LL', 'MM', 'NN', 'OO']],
                ["Boat11", ['PP', 'QQ', 'RR']],
                ["Boat12", ['SS', 'TT']]
            ]]
        ]]
    ]],
    ["Carrier2", [
        ["Helicopter3", [
            ["Airplane5", [
                ["Boat13", ['AAA', 'BBB', 'CCC', 'DDD']],
                ["Boat14", ['EEE', 'FFF', 'GGG', 'HHH']],
                ["Boat15", ['III', 'JJJ']]
            ]],
            ["Airplane6", [
                ["Boat16", ['KKK', 'LLL', 'MMM', 'NNN', 'OOO']],
                ["Boat17", ['PPP', 'QQQ', 'RRR']],
                ["Boat18", ['SSS', 'TTT']]
            ]]
        ]],
        ["Helicopter4", [
            ["Airplane7", [
                ["Boat19", ['AAA1', 'BBB1', 'CCC1', 'DDD1']],
                ["Boat20", ['EEE1', 'FFF1', 'GGG1', 'HHH1']],
                ["Boat21", ['III1', 'JJJ1']]
            ]],
            ["Airplane8", [
                ["Boat22", ['KKK1', 'LLL1', 'MMM1', 'NNN1', 'OOO1']],
                ["Boat23", ['PPP1', 'QQQ1', 'RRR1']],
                ["Boat24", ['SSS1', 'TTT1']]
            ]]
        ]]
    ]]
]

flattened_line_list = flatten_list(all_customer_line_list)

all_customer_line_list = flatten_list(all_customer_line_list)

hotel.add_guest(all_customer_line_list)
hotel.print_rooms()

hotel.search_room_number(1)
hotel.search_room_number(8)
hotel.search_room_number(14)
hotel.search_room_number(52)
hotel.search_room_number(104)

hotel.delete_guest(1)
hotel.delete_guest(8)
hotel.delete_guest(14)
hotel.show_empty_rooms()
