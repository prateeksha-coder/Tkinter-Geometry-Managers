import tkinter as tk

root = tk.Tk()

# Label with spacing
tk.Label(root, text="Hello").pack(padx=20, pady=10)

# Button with spacing
tk.Button(root, text="Click Me").pack(padx=30, pady=20)

root.mainloop()