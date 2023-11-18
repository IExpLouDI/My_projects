import tkinter
from tkinter.filedialog import askopenfilename


def open_file():
    file_path = askopenfilename()
    if file_path:
        pass
    pass


windows = tkinter.Tk(screenName='Create Insert Script')
windows.geometry('400x300')

but_load_file = tkinter.Button(text='Load File', command=lambda: open_file())
but_load_file.pack()
windows.mainloop()
