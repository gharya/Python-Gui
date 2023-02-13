

import tkinter


def button_pushed():
    label.configure(text=label['text'] + ' Hi!')


root = tkinter.Tk()

root.title('My First Python GUI')
root.configure(width = 400, height = 200, background = 'lightyellow')

label = tkinter.Label(root, text='Hello!', font = ('Helvetica', 24, 'bold'))
#label.pack()
label.place(relx = 0.5, rely = 0.33, anchor = tkinter.CENTER)

button = tkinter.Button(root, text = 'Say Hi',
                        font = ('Helvetica', 24),
                        command = button_pushed)

button.place(relx = 0.5, rely = 0.66, anchor = tkinter.CENTER)



root.mainloop()