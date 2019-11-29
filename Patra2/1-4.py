#spell check on thread and recommendation in status bar
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
# from tkinter import a
import threading
import time
from modularfileclass.showline import LineMain #line number
from modularfileclass.COpypasteSelct import StationaryFunction
from modularfileclass.Spellcheck1 import Spellcheck
from difflib import get_close_matches # for spelling recommendation

from modularfileclass.Findandrplace import FindReplaceFunctions

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
        box_title = "This is a Patra 2.00"
        box_meage = "This is a basic test editor project For Course O.S. 2019\nCOE17B020 COE17B024 CED17I047"
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

        print("you are status bar thread ")
        print(threading.current_thread())
        print("ok")
        label = tk.Label(self.parent.textarea , textvariable = self.status , fg = "black" , bg = "lightgrey",anchor = 'sw',font = font_specs)
        label.pack(side = tk.BOTTOM , fill = tk.BOTH)


    def update_status(self,*args):
        if isinstance(args[0],bool):
            self.status.set(" You just saved your ass !")
        # elif isinstance(args[0],list):
        #     self.status.set("The misspelled words rec "+args[0])
        else:
            print("check which key")
            self.status.set("Patra - 0.1 contain   !")
    def update_status1(self,*args1):
        print("in update status")
        # for i in args1:
        #     print(i)
        #     print("cocunut")
        # print(*args1)
        # stri1 = args1[0].split("\n")
        # print()
        # string1_torecomend = ""
        # for i in args1[0]:
        #     string1_torecomend += i
        #     string1_torecomend + "  "
        # self.status.set("Spelling recommendation "+string1_torecomend)
        self.status.set(args1)

        print("chec this again")
        #update spell correct


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
class Patra:
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

        print("you are main thread? in class ")
        print(threading.current_thread())
        print("ok1")

    def rum(self,master):
        master.title("Untitle - No Name")
        master.geometry("1200x700")



        font_specs = ("ubuntu",18)

        self.master = master # access master in Child class Menubar

        self.filename = None


        self.textarea = tk.Text(master,font = font_specs)
        self.textarea.tag_configure("sel",background = "skyblue") # experiment added selection background color

        self.scroll = tk.Scrollbar(master,command = self.textarea.yview)
        self.textarea.configure(yscrollcommand = self.scroll.set)
        self.textarea.pack(side = tk.LEFT,fill = tk.BOTH,expand = True)
        self.scroll.pack(side = tk.RIGHT,fill = tk.Y)

        self.menubar = Menubar(self)  # gone in init
        self.statusbar = Statubar(self)
        self.commandbar = Command(self)

        # extra features
        # linenumber
        # copy paste select undo redo
        self.textarea.storeobj = {}     #//required fro copypaste select as object that can be passed as function naem
        self.Line = LineMain(self.textarea)
        self.copypasteselect = StationaryFunction(self.textarea)


        # self.spellcheck2 = Spellcheck(self.textarea)
        self.spellcheck2 = Spellcheck(self.textarea,self.statusbar) #update statusbar in case spell error


        self.bind_shortcuts()

        FindReplaceFunctions(self.textarea)




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
        # self.__init__(master)




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



#
# class LineNumberCanvas(tk.Canvas):
#     def __init__(self, *args, **kwargs):
#         tk.Canvas.__init__(self, *args, **kwargs)
#         self.text_widget = None
#         self.breakpoints = []
#
#     def connect(self,text_widget):
#         self.text_widget = text_widget
#
#     def re_render(self):
#         """Re-render the line canvas"""
#         self.delete('all') # To prevent drawing over the previous canvas
#
#         temp = self.text_widget.index("@0,0")
#         while True :
#             dline= self.text_widget.dlineinfo(temp)
#             if dline is None:
#                 break
#             y = dline[1]
#             x = dline[0]
#             linenum = str(temp).split(".")[0]
#
#             id = self.create_text(2,y,anchor="nw", text=linenum)
#
#             if int(linenum) in self.breakpoints:
#                 x1,y1,x2,y2 = self.bbox(id)
#                 self.create_oval(x1,y1,x2,y2,fill='red')
#                 self.tag_raise(id)
#
#             temp = self.text_widget.index("%s+1line" % temp)
#
#     def get_breakpoint_number(self,event):
#          if self.find_withtag('current'):
#             i = self.find_withtag('current')[0]
#             linenum = int(self.itemcget(i,'text'))
#
#             if linenum in self.breakpoints:
#                 self.breakpoints.remove(linenum)
#             else:
#                 self.breakpoints.append(linenum)
#             self.re_render()
#
#
#
# class LineMain:
#     def __init__(self, text):
#         self.text = text
#         self.master = text.master
#         self.mechanise()
#         self._set_()
#         self.binding_keys()
#
#     def mechanise(self):
#         self.text.tk.eval('''
#             proc widget_interceptor {widget command args} {
#
#                 set orig_call [uplevel [linsert $args 0 $command]]
#
#               if {
#                     ([lindex $args 0] == "insert") ||
#                     ([lindex $args 0] == "delete") ||
#                     ([lindex $args 0] == "replace") ||
#                     ([lrange $args 0 2] == {mark set insert}) ||
#                     ([lrange $args 0 1] == {xview moveto}) ||
#                     ([lrange $args 0 1] == {xview scroll}) ||
#                     ([lrange $args 0 1] == {yview moveto}) ||
#                     ([lrange $args 0 1] == {yview scroll})} {
#
#                     event generate  $widget <<Changed>>
#                 }
#
#                 #return original command
#                 return $orig_call
#             }
#             ''')
#         self.text.tk.eval('''
#             rename {widget} new
#             interp alias {{}} ::{widget} {{}} widget_interceptor {widget} new
#         '''.format(widget=str(self.text)))
#         return
#
#
#     def binding_keys(self):
#         for key in ['<Down>','<Up>',"<<Changed>>","<Configure>"]:
#             self.text.bind(key, self.changed)
#         self.linenumbers.bind('<Button-1>',self.linenumbers.get_breakpoint_number)
#         return
#
#     def changed(self, event):
#         self.linenumbers.re_render()
#         #print "render"
#         return
#
#
#     def _set_(self):
#         self.linenumbers = LineNumberCanvas(self.master, width=30)
#         self.linenumbers.connect(self.text)
#         self.linenumbers.pack(side="left", fill="y")
#         return







if __name__== "__main__":
    master = tk.Tk()
    pt = Patra(master)
    print("you are main thread? the main fucntion ")
    print(threading.current_thread())
    print("ok1")
    master.mainloop()
    # master.
