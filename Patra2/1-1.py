import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
# from tkinter import a
import threading
import time


class Menubar:

    def __init__(self,parent):
        font_specs = ("ubuntu",14)
        menubar = tk.Menu(parent.master,font = font_specs) #passing the window
        parent.master.config(menu = menubar)

        file_dropdown = tk.Menu(menubar,font = font_specs,tearoff = 0) # tearoff so that you dont take menu withyourself
        file_dropdown.add_command(label = "New File",accelerator = "Ctrl+N",command = parent.new_file)
        file_dropdown.add_command(label = "Open File",accelerator = "Ctrl+O",command = parent.open_file)
        file_dropdown.add_command(label = "Save File",accelerator = "Ctrl+S",command = parent.save)
        file_dropdown.add_command(label = "Save Ass",accelerator = "Ctrl+shift+S",command = parent.saveas )
        file_dropdown.add_separator()
        file_dropdown.add_command(label = "Exit",command = parent.master.destroy)

        menubar.add_cascade(label = "Basic", menu = file_dropdown)


        Utilies_dropdown = tk.Menu(menubar,font = font_specs,tearoff = 0) # tearoff so that you dont take menu withyourself
        Utilies_dropdown.add_command(label = "Size")







        about_dropdown = tk.Menu(menubar,font = font_specs,tearoff = 0)
        about_dropdown.add_command(label = "Source code",command = self.show_abtmenu)
        about_dropdown.add_separator()
        about_dropdown.add_command(label = "About",command = self.sour_cecoed)

        menubar.add_cascade(label = "About", menu = about_dropdown)

    def show_abtmenu(self):
        box_title = "This is a Patra 1.01"
        box_meage = "Multithreading is still pending"
        messagebox.showinfo(box_title,box_meage)

    def sour_cecoed(self):
        box_title = "Currently a private project"
        box_meage = "Not yet available"
        messagebox.showinfo(box_title, box_meage)


class Statubar(threading.Thread):
    parent = None
    def __init__(self,parent):
        # self.status = tk.StringVar()
        # self.status.set("Patra - 0.1 contain")
        # font_specs = ("ubuntu", 14)
        #
        #
        # label = tk.Label(parent.textarea , textvariable = self.status , fg = "black" , bg = "lightgrey",anchor = 'sw',font = font_specs)
        # label.pack(side = tk.BOTTOM , fill = tk.BOTH)
        self.parent = parent
        threading.Thread.__init__(self)

        self.start()


    def run(self):
        self.status = tk.StringVar()
        self.status.set("Patra - 0.1 contain")
        font_specs = ("ubuntu", 14)

        print("you are testing thread ")
        print(threading.current_thread())
        print("ok")
        label = tk.Label(self.parent.textarea , textvariable = self.status , fg = "black" , bg = "lightgrey",anchor = 'sw',font = font_specs)
        label.pack(side = tk.BOTTOM , fill = tk.BOTH)


    def update_status(self,*args):
        if isinstance(args[0],bool):
            self.status.set(" You just saved your ass !")
        else:
            print("check which key")
            self.status.set("Patra - 0.1 contain   !")


class Command:
    def __init__(self,parent):
        self.status = tk.StringVar()
        self.status.set("Commands")
        font_specs = ("ubuntu", 14)


        label = tk.Label(parent.textarea , textvariable = self.status , fg = "black" , bg = "lightgrey",anchor = 'sw',font = font_specs)
        label.pack(side = tk.BOTTOM , fill = tk.BOTH)



    def set_mode(self,*args):
        print("COmmand mode reached")
        print(args[0].char)
        self.status.set("Still pending and input has to be taken and stopped in main text")
        pass















#parent class
class Pytest:
    def __init__(self,master):


        # master.title("Untitle - No Name")
        # master.geometry("1200x700")
        #
        #
        #
        # font_specs = ("ubuntu",18)
        #
        # self.master = master # access master in Child class Menubar
        #
        # self.filename = None
        #
        #
        # self.textarea = tk.Text(master,font = font_specs)
        # self.scroll = tk.Scrollbar(master,command = self.textarea.yview)
        # self.textarea.configure(yscrollcommand = self.scroll.set)
        # self.textarea.pack(side = tk.LEFT,fill = tk.BOTH,expand = True)
        # self.scroll.pack(side = tk.RIGHT,fill = tk.Y)
        #
        # self.menubar = Menubar(self)  # gone in init
        # self.statusbar = Statubar(self)
        # self.commandbar = Command(self)
        #
        # self.bind_shortcuts()

        self.rum(master)

        print("you are main thread? i nclass ")
        print(threading.current_thread())
        print("ok1")

    def rum(self,master):
        master.title("Untitle - No Name")
        master.geometry("1200x700")



        font_specs = ("ubuntu",18)

        self.master = master # access master in Child class Menubar

        self.filename = None


        self.textarea = tk.Text(master,font = font_specs)
        self.scroll = tk.Scrollbar(master,command = self.textarea.yview)
        self.textarea.configure(yscrollcommand = self.scroll.set)
        self.textarea.pack(side = tk.LEFT,fill = tk.BOTH,expand = True)
        self.scroll.pack(side = tk.RIGHT,fill = tk.Y)

        self.menubar = Menubar(self)  # gone in init
        self.statusbar = Statubar(self)
        self.commandbar = Command(self)

        self.bind_shortcuts()




    def set_window_title(self,name = None):
        if name:
            # self.filename = nme
            self.master.title(name+ " -Patra1.01")
        else:
            self.master.title("Untitled "+ " -Patra1.01")






    def new_file(self,*args):
        print("rteached new")
        print(*args)
        print("above is keybind")
        self.textarea.delete(1.0, tk.END)  # clear shit
        self.filename = None
        self.set_window_title()
        self.__init__(master)




    def open_file(self,*args):
        print("open")
        print(*args)
        print("above is keybind")
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"),
                       ("Text Files", "*.txt"),
                       ("Python Scripts", "*.py"),
                       ("Markdown Documents", "*.md"),
                       ("JavaScript Files", "*.js"),
                       ("HTML Documents", "*.html"),
                       ("CSS Documents", "*.css")])
        if self.filename:
            self.textarea.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())
            self.set_window_title(self.filename)

    def save(self,*args):
        print("Ok")
        print(*args)
        print("above is keybind")
        if self.filename:
            try:

                txtara_contn = self.textarea.get(1.0,tk.END)
                with open(self.filename,"w") as g1:
                    g1.write(txtara_contn)
                self.statusbar.update_status(True)
            except Exception as e:
                print(e)

        else:
            self.saveas()



    def saveas(self,*args):

        print("bnirht")
        try:
            new_file1 = filedialog.asksaveasfilename(
                initialfile = "Noname.txt",
                defaultextension=".txt",
                filetypes=[("All Files", "*.*"), ("Text Files", "*.txt"), ("Python Files", "*.py"), ("C Files", "*.c"),
                           ("C++ Files", "*.cpp")],

            )
            textarea_contnt = self.textarea.get(1.0,tk.END) #get what over you wrote
            with open(new_file1,"w") as f1:
                f1.write(textarea_contnt)
            self.filename = new_file1
            self.statusbar.update_status(True)

            self.set_window_title(self.filename)




        except Exception as e:
            print(e)



    def bind_shortcuts(self):
        self.textarea.bind('<Control-n>',self.new_file)
        self.textarea.bind('<Control-o>',self.open_file)
        self.textarea.bind('<Control-s>',self.save)
        self.textarea.bind('<Control-S>',self.saveas)
        self.textarea.bind('<Escape>', self.commandbar.set_mode) #comand mode experimentation
        self.textarea.bind('<Key>',self.statusbar.update_status)








if __name__== "__main__":
    master = tk.Tk()
    pt = Pytest(master)
    print("you are main thread? not in class ")
    print(threading.current_thread())
    print("ok1")
    master.mainloop()
    # master.
