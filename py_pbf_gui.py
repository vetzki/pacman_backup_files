# cython: language_level=3

"""
pacman_backup_files: show pacnew and pacsave files
Copyright (C) 2019 Vetter Michael

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import tkinter as tk
import tkinter.ttk as ttk
import os
import py_pbf_helper
import py_pbf_gui_sub as guihelper

# TEST
#import time

class MainGui:
    '''
    main gui class
    @params: config, theme
    '''
    def __init__(self,config,theme):     
        self.master = tk.Tk()
        self.master.title("pacman backup files")
        try:
            icon = tk.PhotoImage(file=config["gui"]["window_icon"])
            self.master.tk.call('wm', 'iconphoto', self.master._w,icon)
        except tk.TclError as e:
            print(e)
        self.config = config
        self.selected_file = tk.StringVar()
        self.pacfile = str()
        self.theme = theme
        # keep sanitry and add additional config var for tk_styles
        self.config_tk = config["gui"]["tk_styles"][self.theme]

    def _configure_styles(self):
        s = ttk.Style()
        if self.theme == "default":
            # skip
            pass
        else:
            # create theme first
            s.theme_create(self.theme)
        # apply theme
        s.theme_settings(self.theme,self.config["gui"]["ttk_styles"][self.theme])
        s.theme_use(self.theme)

    def _bind_return_to_btns(self):
        # bind Return
        return([ v.bind("<Return>",v["command"]) for i,j in self.main_frame.children.items() for k,v in j.children.items() if "!button" in k ])
        
    def _create_frame(self):
        self.main_frame = ttk.Frame(self.master,style="mainframe.TFrame")
        self.frame_btns = ttk.Frame(self.main_frame)
        self.frame_text = ttk.Frame(self.main_frame)
        self.frame_listbox = ttk.Frame(self.main_frame)
        self.frame_action_btns = ttk.Frame(self.main_frame)

    def _create_buttons(self):
        self.refresh_pacnew_btn = ttk.Button(self.frame_btns,text="Show .pacnew files",command=lambda : self._get_entries(".pacnew"))
        self.refresh_pacsav_btn = ttk.Button(self.frame_btns,text="Show .pacsave files",command=lambda : self._get_entries(".pacsave"))
        self.quit_btn = ttk.Button(self.frame_btns,text="Exit",command=self._quit)
        self.show_diff_btn = ttk.Button(self.frame_action_btns,text="Show diff",command=self._show_diff)
        self.open_in_editor_btn = ttk.Button(self.frame_action_btns,text="Open in Editor",command=self._open_editor)
        self.delete_files_btn = ttk.Button(self.frame_action_btns,text="Delete files",command=self._on_delete)
        
    def _create_textbox(self):
        self.path_t_lbl = ttk.Label(self.frame_text,text="Search Path")
        self.editor_t_lbl = ttk.Label(self.frame_action_btns,text="Editor")
        self.orig_file_t_lbl = ttk.Label(self.frame_action_btns,text="File")
        self.path_t = ttk.Entry(self.frame_text,width=self.config["gui"]["path_line_width"])
        self.path_t.insert("0",self.config["path"])
        self.editor_t = ttk.Entry(self.frame_action_btns,width=self.config["gui"]["editor_line_width"])
        self.editor_t.insert("0",self.config["editor"])
        self.orig_file_t = ttk.Entry(self.frame_action_btns,width=self.config["gui"]["file_line_width"])
        self.tb_entries_scrolly=ttk.Scrollbar(self.frame_listbox)
        self.tb_entries = tk.Listbox(self.frame_listbox,width=self.config_tk["listbox"]["listbox_sizes"][0],height=self.config_tk["listbox"]["listbox_sizes"][1],bg=self.config_tk["listbox"]["background"],fg=self.config_tk["listbox"]["foreground"],font=self.config_tk["listbox"]["font"],selectbackground=self.config_tk["listbox"]["selectbackground"],selectforeground=self.config_tk["listbox"]["selectforeground"],highlightcolor=self.config_tk["listbox"]["selectbackground"],yscrollcommand=self.tb_entries_scrolly.set)
        self.tb_entries.bind("<<ListboxSelect>>", self._on_lb_select)
        self.tb_entries.bind("<Key>", lambda evt: "break" if evt.keysym=="Prior" or evt.keysym=="Next" else None) # disable PageUp/ PageDown Buttons
        self.tb_entries_scrolly.config(command=self.tb_entries.yview)

    def _on_lb_select(self,val):
        try:
            sender = val.widget
            idx = sender.curselection()
            # activate entry (avoids issue with "black dotted border" )
            sender.activate(idx)
            value = sender.get(idx)
            ce = py_pbf_helper.Match(value,self.pacfile)
            value_repl = value.replace(self.pacfile,"") if ce.check_ending() is False else ce.strip_ending()
            self.selected_file.set(value)
            self.orig_file_t.delete(0, tk.END)
            self.orig_file_t.insert(0,value_repl)
        except tk.TclError:
            return
    """
    TODO:
    def _updater(self):
        pass
    """

    def _get_entries(self,pac_file):
        # reset self.selected_file and self.orig_file_t
        self.selected_file.set("")
        self.orig_file_t.delete(0,tk.END)
        self.pacfile = pac_file
        f = py_pbf_helper.GetFiles()
        f.setup(self.path_t.get(),pac_file,False)
        f.start()
        pb = guihelper.ProgBar(self.frame_text)
        pb.run()
        # TEST
        #t1 = time.time()
        # unset quit btn
        self.quit_btn.config(command=False)
        self.tb_entries.delete(first=0,last=tk.END)
        def update():
            if f.get_result() is None:
                self.master.after(250,update)
            else:
                pb.stop()
                # TEST
                #print("search took {}".format(time.time()-t1))
                # reassign quit button
                self.quit_btn.config(command=self._quit)
                [self.tb_entries.insert(tk.END,i) for i in f.files]
                #for i in f.files:
                #    self.tb_entries.insert(tk.END,i)
        self.master.after(100, update)
    
    def _on_delete(self):
        guihelper.TopCbWindow(self.master,self.tb_entries.get(0,self.tb_entries.size()),'!button',"Show "+self.pacfile+" files",self.config)
        pass

    def _packelements(self):
        self.main_frame.pack(expand=True,fill=tk.BOTH)
        self.frame_btns.pack()
        self.frame_text.pack()
        self.frame_listbox.pack(fill=tk.BOTH,expand=True)
        self.frame_action_btns.pack()
        self.refresh_pacnew_btn.pack(side=tk.LEFT)
        self.refresh_pacsav_btn.pack(side=tk.LEFT)
        self.quit_btn.pack(side=tk.RIGHT)
        self.path_t_lbl.pack(side=tk.TOP)
        self.path_t.pack(side=tk.TOP)
        self.tb_entries_scrolly.pack(side=tk.RIGHT,fill=tk.Y,pady=self.config_tk["listbox"]["pady"])
        self.tb_entries.pack(padx=self.config_tk["listbox"]["padx"],pady=self.config_tk["listbox"]["pady"],fill=tk.BOTH,expand=1)
        self.orig_file_t_lbl.pack(side=tk.LEFT)
        self.orig_file_t.pack(side=tk.LEFT)
        self.show_diff_btn.pack(side=tk.LEFT)
        self.delete_files_btn.pack(side=tk.LEFT)
        self.open_in_editor_btn.pack(side=tk.LEFT)
        self.editor_t.pack(side=tk.RIGHT)
        self.editor_t_lbl.pack(side=tk.RIGHT)
        # bind buttons to return key after pack
        self._bind_return_to_btns()
    
    def _set_window_minsize(self):
        # set minsize after pack all elements including possible progress_bar
        # run once at start to get minsize with progress_bar frame
        pb = guihelper.ProgBar(self.frame_text)
        pb.run(True) # no need to start progress_bar
        # now geometry() returns valid size/placement
        self.master.update()
        pb.stop()
        self.master.minsize(self.master.winfo_width(), self.master.winfo_height())

    def __enter__(self):
        self._configure_styles()
        self._create_frame()
        self._create_buttons()
        self._create_textbox()
        self._packelements()
        self._set_window_minsize()
        return(self)

    def _show_diff(self):
        selected_file = self.selected_file.get()
        orig_file = self.orig_file_t.get()       
        # check readable
        readable = py_pbf_helper.is_readable(selected_file)
        if readable:
            with py_pbf_helper.RunCmdSimple(["diff",orig_file,selected_file],True) as sh:
                    guihelper.TopTextWindow(self.master,sh.res.stdout.decode(),orig_file,selected_file,sh.cmd,self.config_tk)
        elif readable is False:
            guihelper.TopTextWindow(self.master,"files not readable",orig_file,selected_file,False,self.config_tk)
        else: # exception occured
            guihelper.TopTextWindow(self.master,"Exception:\n"+readable,orig_file,selected_file,False,self.config_tk)

    def _open_editor(self):
        editor = self.editor_t.get()
        try:
            if py_pbf_helper.get_current_environment()["EDITOR"] != editor:
                os.putenv("EDITOR",editor)
        except KeyError:
            # no EDITOR variable set
            os.putenv("EDITOR",editor)
        cmd = [self.config["terminal"],self.config["terminal_execute_flag"],self.config["terminal_edit_cmd"],self.selected_file.get(),self.orig_file_t.get()]
        # run threaded else mainloop is blocked (and windows not shown)
        sh = py_pbf_helper.RunThCmdSimple()
        self.subshell = True
        sh.setup(cmd)
        # returncode is always 0, dont rely on that
        sh.start()
        def update():
            if sh.get_result() is None:
                self.master.after(250, update)
            else:
                sh.stop()
                self.subshell = False
        self.master.after(250, update)

    def init_gui(self):
        self.__enter__()
        self.run()

    def _quit(self):
        try:
            if self.subshell:
                cmd = ["killall","-3",self.config["editor"]]
                with py_pbf_helper.RunCmdSimple(cmd,False) as sh:
                    sh.res
        except AttributeError:
            # self.subshell not set
            pass
        finally:
            exit()

    def run(self):
        self.master.mainloop()

    def __exit__(self,t,val,tb):
        del self
