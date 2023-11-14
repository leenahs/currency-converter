import tkinter as tk

class RoundedRectangleFrame(tk.Canvas):
    def __init__(self, master=None, cnf={}, **kwargs):
        super().__init__(master, cnf, **kwargs)

        self.rounded_rect = None
        self.update_rounded_rectangle()

    def update_rounded_rectangle(self):
        # Delete the existing rounded rectangle (if any)
        if self.rounded_rect:
            self.delete(self.rounded_rect)

        # Get the dimensions of the canvas
        width = self.winfo_reqwidth()
        height = self.winfo_reqheight()

        # Set the radius for rounded corners
        corner_radius = 20

        # Create a rounded rectangle
        self.rounded_rect = self.create_polygon(
            corner_radius, 0,
            width - corner_radius, 0,
            width, corner_radius,
            width, height - corner_radius,
            width - corner_radius, height,
            corner_radius, height,
            0, height - corner_radius,
            0, corner_radius,
            fill=self.cget("bg"),
            outline="black",  # Change the outline color if needed
            width=2  # Change the width of the border if needed
        )

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x200")

    rounded_frame = RoundedRectangleFrame(root, width=300, height=200, bg="lightblue")
    rounded_frame.pack(padx=20, pady=20)

    label = tk.Label(rounded_frame, text="Hello, Rounded Frame!", font=("Arial", 12))
    label.place(relx=0.5, rely=0.5, anchor="center")

    root.mainloop()
