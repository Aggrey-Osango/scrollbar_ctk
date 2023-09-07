import customtkinter as ctk
# import tkinter as tk

ctk.set_appearance_mode ("light")
ctk.set_default_color_theme ("blue")

# App initialization
app = ctk.CTk()
app.geometry("600x520")
app.title ("Helium Notes")

# Frame Initialization
frame = ctk.CTkFrame (master = app, width = 590, height = 510, corner_radius = 10)
frame.pack(padx=10, pady=10)

# TextBox Initialization
tbox = ctk.CTkTextbox (master = frame, width = 400, height = 200,
                       scrollbar_button_color = "purple")

tbox.grid(row = 0, column = 0, sticky ="nsew")

def save ():
    print(tbox.get(index1 = "0.0", index2 = "end"))


# Button Command
btn_01 = ctk.CTkButton(master = frame, text = "Save", command = save)
btn_01.grid(padx=5, pady=5)

# Adding a label obj to the frame
lbl_01 = ctk.CTkLabel (master = frame, width = 50,text = "Name",
                       bg_color = ("white", "grey75"), corner_radius = 10)

lbl_01.grid(padx=5, pady=5)

if __name__ == '__main__':
    app.mainloop ()