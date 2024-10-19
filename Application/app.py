import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import ast



# Algorithm 
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

    def get_guest_list(self):
        guest_list = []
        max_room = max(self.rooms.keys()) if self.rooms else 0
        for room in range(1, max_room + 1):
            if room in self.rooms:
                customer = self.rooms[room]
                guest_list.append(f"Room {room}: {customer.name} (Approached by {customer.approach})")
            else:
                guest_list.append(f"Room {room}: Empty")
        return guest_list

    def delete_guest(self, room_number):
        if room_number in self.rooms:
            del self.rooms[room_number]
            return f"Guest in room {room_number} has been deleted."
        else:
            return f"Room {room_number} is already empty or does not exist."

    def search_room_number(self, room_number):
        if room_number in self.rooms:
            customer = self.rooms[room_number]
            return f"Room {room_number}: {customer.name} (Approached by {customer.approach})"
        else:
            return f"Room {room_number} is empty or does not exist."

    def show_empty_rooms(self):
        max_room = max(self.rooms.keys()) if self.rooms else 0
        empty_rooms = [f"Room {room} is empty" for room in range(1, max_room + 1) if room not in self.rooms]
        return empty_rooms if empty_rooms else ["No empty rooms available."]



# Application
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

def open_add_guest_popup():
    popup = tk.Toplevel(root)
    popup.title("Add Guests")
    popup.geometry("600x400+220+130")

    label = tk.Label(popup, text="Enter all_customer_line_list structure:")
    label.pack(pady=10)

    textbox = tk.Text(popup, height=15, width=60)
    textbox.pack(pady=10)

    def submit_guest_data():
        input_text = textbox.get("1.0", tk.END).strip()

        if input_text == "":
            messagebox.showwarning("Input Error", "Input cannot be empty.")
            return

        try:
            all_customer_line_list = ast.literal_eval(input_text)

            flattened = flatten_list(all_customer_line_list)
            hotel.add_guest(flattened)

            messagebox.showinfo("Success", "Guests added successfully!")
            popup.destroy()  

        except (SyntaxError, ValueError):
            messagebox.showerror("Input Error", "Invalid input format. Please enter a valid list structure.")

    submit_button = tk.Button(popup, text="Submit", command=submit_guest_data)
    submit_button.pack(pady=10)

def show_guest_list():
    guest_popup = tk.Toplevel(root)
    guest_popup.title("Guest List")
    guest_popup.geometry("400x700+220+130")

    guest_list = hotel.get_guest_list()

    label = tk.Label(guest_popup, text="Current Guest List:", font=("Arial", 14))
    label.pack(pady=10)

    text_box = tk.Text(guest_popup, height=50, width=50)
    text_box.pack(pady=10)

    for guest in guest_list:
        text_box.insert(tk.END, guest + "\n")

    text_box.config(state=tk.DISABLED)  

def delete_guest_popup():
    popup = tk.Toplevel(root)
    popup.title("Delete Guest")
    popup.geometry("300x200+220+130")

    label = tk.Label(popup, text="Enter Room Number to Delete:")
    label.pack(pady=10)

    room_entry = tk.Entry(popup)
    room_entry.pack(pady=10)

    def submit_delete():
        room_number = int(room_entry.get())
        result = hotel.delete_guest(room_number)
        messagebox.showinfo("Delete Guest", result)
        popup.destroy()

    submit_button = tk.Button(popup, text="Delete", command=submit_delete)
    submit_button.pack(pady=10)

def search_room_popup():
    popup = tk.Toplevel(root)
    popup.title("Search Room")
    popup.geometry("300x200+220+130")

    label = tk.Label(popup, text="Enter Room Number to Search:")
    label.pack(pady=10)

    room_entry = tk.Entry(popup)
    room_entry.pack(pady=10)

    def submit_search():
        room_number = int(room_entry.get())
        result = hotel.search_room_number(room_number)
        messagebox.showinfo("Search Room", result)
        popup.destroy()

    submit_button = tk.Button(popup, text="Search", command=submit_search)
    submit_button.pack(pady=10)

def show_empty_rooms_popup():
    popup = tk.Toplevel(root)
    popup.title("Empty Rooms")
    popup.geometry("400x700+220+130")

    empty_rooms = hotel.show_empty_rooms()

    label = tk.Label(popup, text="Empty Rooms:", font=("Arial", 14))
    label.pack(pady=10)

    text_box = tk.Text(popup, height=50, width=50)
    text_box.pack(pady=10)

    for room in empty_rooms:
        text_box.insert(tk.END, room + "\n")

    text_box.config(state=tk.DISABLED)



# GUI
root = tk.Tk()
root.title("Hilbert Hotel")
root.iconbitmap("Application\Icon\porsche.ico")
root.geometry("1500x800+220+100")
root.minsize(1500, 800)
root.maxsize(1500, 800)

bg_image = Image.open("Application/Background/background.png")
bg_image = bg_image.resize((1500, 800))
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(root, image=bg_photo)
background_label.place(relwidth=1, relheight=1)

reserve_button = tk.Button(root, text="Reserve", command=open_add_guest_popup, width=10, height=2, bg="lightblue", fg="black", font=("Arial", 16))
reserve_button.place(x=400, y=600)

show_guest_button = tk.Button(root, text="Show Guests", command=show_guest_list, width=10, height=2, bg="lightgreen", fg="black", font=("Arial", 16))
show_guest_button.place(x=550, y=600)

delete_guest_button = tk.Button(root, text="Delete Guest", command=delete_guest_popup, width=10, height=2, bg="lightcoral", fg="black", font=("Arial", 16))
delete_guest_button.place(x=700, y=600)

search_room_button = tk.Button(root, text="Search Room", command=search_room_popup, width=10, height=2, bg="lightyellow", fg="black", font=("Arial", 16))
search_room_button.place(x=850, y=600)

show_empty_rooms_button = tk.Button(root, text="Empty Rooms", command=show_empty_rooms_popup, width=10, height=2, bg="lightgray", fg="black", font=("Arial", 16))
show_empty_rooms_button.place(x=1000, y=600)

root.mainloop()