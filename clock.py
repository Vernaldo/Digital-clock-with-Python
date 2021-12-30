from time import strftime
from tkinter import Label, Tk

#window configuration
window = Tk()
window.title("VR11clock")
window.geometry("200x80")
window.configure(bg="red")  #clock's background
window.resizable(False, False)  #setting a fixed window size

clock_label = Label(
    window, bg="black", fg="orange", font=("Arial", 30, "bold"), relief="flat"
)
clock_label.place(x=10, y=50)


def update_label():
    """updating the clock
       every 30 milliseconds
    """
    current_time = strftime("%H: %M: %S\n %d-%m-%Y ")
    clock_label.configure(text=current_time)
    clock_label.after(80, update_label)
    clock_label.pack(anchor="center")


update_label()
window.mainloop()


