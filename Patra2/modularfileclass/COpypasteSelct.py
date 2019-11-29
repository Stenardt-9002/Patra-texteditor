#
import tkinter as Tkinter

class StationaryFunction:
    def __init__(self, text):
        self.text = text
        self.create_binding_keys()
        self.binding_functions_config()
        self.join_function_with_main_stream()


    def join_function_with_main_stream(self):
        self.text.storeobj['Copy']   =  self.copy
        self.text.storeobj['Cut']    =  self.cut
        self.text.storeobj['Paste']  =  self.paste
        self.text.storeobj['Undo']   =  self.undo
        self.text.storeobj['Redo']   =  self.redo
        self.text.storeobj['SelectAll']=self.select_all
        self.text.storeobj['DeselectAll']=self.deselect_all
        return

    def binding_functions_config(self):
        self.text.tag_configure("sel", background="skyblue")
        self.text.configure(undo=True,autoseparators=True, maxundo=-1)
        return

    def copy(self, event=None):
        self.text.event_generate("<<Copy>>")
        return

    def paste(self, event=None):
        self.text.event_generate("<<Paste>>")
        return

    def cut(self, event=None):
        self.text.event_generate("<<Cut>>")
        return

    def undo(self, event=None):
        self.text.event_generate("<<Undo>>")
        return

    def redo(self, event=None):
        self.text.event_generate("<<Redo>>")
        return

    def create_binding_keys(self):
        for key in ["<Control-a>","<Control-A>"]:
            self.text.master.bind(key, self.select_all)
        for key in ["<Button-1>","<Return>"]:
            self.text.master.bind(key, self.deselect_all)

        return

    def select_all(self, event=None):
        self.text.tag_add("sel",'1.0','end')
        return


    def deselect_all(self, event=None):
        self.text.tag_remove("sel",'1.0','end')
        return




# class StationaryFunction:
#
#     def __init__(self, text):
#         self.text = text
#         self.create_binding_keys()
#         self.binding_functions_config()
#         self.join_function_with_main_stream()
#
#
#     def join_function_with_main_stream(self):
#         self.text.storeobj['Copy']   =  self.copy
#         self.text.storeobj['Cut']    =  self.cut
#         self.text.storeobj['Paste']  =  self.paste
#         self.text.storeobj['SelectAll']=self.select_all
#         self.text.storeobj['DeselectAll']=self.deselect_all
#         return
#
#     def binding_functions_config(self):
#         self.text.tag_configure("sel", background="skyblue")
#         return
#
#     def copy(self, event):
#         self.text.event_generate("<<Copy>>")
#         return
#
#     def paste(self, event):
#         self.text.event_generate("<<Paste>>")
#         return
#
#     def cut(self, event):
#         self.text.event_generate("<<Cut>>")
#         return
#
#     def create_binding_keys(self):
#         for key in ["<Control-a>","<Control-A>"]:
#             self.text.master.bind(key, self.select_all)
#         for key in ["<Button-1>","<Return>"]:
#             self.text.master.bind(key, self.deselect_all)
#         return
#
#     def select_all(self, event):
#         self.text.tag_add("sel",'1.0','end')
#         return
#
#
#     def deselect_all(self, event):
#         self.text.tag_remove("sel",'1.0','end')
#         return
#
# # if __name__ == '__main__':
# #     root = Tkinter.Tk()
# #     pad = Tkinter.Text(root,wrap='none')
# #     pad.storeobj = {}
# #     StationeryFunctions(pad)
# #     pad.pack()
# #     root.mainloop()
