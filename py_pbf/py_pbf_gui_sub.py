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
import py_pbf_helper
import os

class ProgBar:
    '''
    progressbar helper class
    @params: tkinter.object
    '''
    def __init__(self,tkobj):
        self.frame = ttk.Frame(tkobj)
        self.progbar = ttk.Progressbar(self.frame,mode="indeterminate")
        self.progress = ttk.Label(self.frame,text="Searching...",style="progress.TLabel")
        self.abort_btn = ttk.Button(self.frame,text="Abort",command=self.abort)
        self.hint = ttk.Label(self.frame,text="sends SIGQUIT (-3) signal to %i (terminates application)" %(os.getpid()),style="progress.TLabel")

    def run(self,setuprun=False):
        '''
        exec run() with True to skip start of progbar
        '''
        self.frame.pack()
        self.progbar.pack()
        self.progress.pack()
        self.abort_btn.pack()
        self.hint.pack()
        if setuprun == False: self.progbar.start(interval=75)

    def abort(self):
        cmd = ["kill","-3",str(os.getpid())]
        with py_pbf_helper.RunCmdSimple(cmd) as sh:
            self.stop()

    def stop(self):
        self.progbar.stop()
        self.frame.destroy()

class TopTextWindow:
    '''
    toplevel text window helper class
    @params: tkinter.object, string, string, string, string, dict
    '''
    def __init__(self, tkobj, output, conf_file, pac_conf_file, cmd, config):
        self.top = tk.Toplevel(tkobj)
        self.text = "<<< = %s\n>>> = %s\n" %(conf_file,pac_conf_file)
        self.text += output+"\n"
        self.text += "\ncommand was\n%s" %(cmd)
        self._create_text_view(config)

    def _create_text_view(self,gui_style):
        # seperate frame for dismiss button else scrollbar get messed up
        frame_txt = ttk.Frame(self.top)
        frame_btn = ttk.Frame(self.top)
        frame_txt.pack(expand=True,fill=tk.BOTH)
        frame_btn.pack(expand=True,fill=tk.BOTH)
        txt_scrolly=ttk.Scrollbar(frame_txt)
        txt_scrollx=ttk.Scrollbar(frame_txt, orient=tk.HORIZONTAL)
        txt = tk.Text(frame_txt,width=gui_style["text"]["text_sizes"][0],height=gui_style["text"]["text_sizes"][1],bg=gui_style["text"]["background"],fg=gui_style["text"]["foreground"],font=gui_style["text"]["font"],selectbackground=gui_style["text"]["selectbackground"],selectforeground=gui_style["text"]["selectforeground"],xscrollcommand=txt_scrollx.set,yscrollcommand=txt_scrolly.set,wrap=tk.NONE)
        txt_scrolly.config(command=txt.yview)
        txt_scrollx.config(command=txt.xview)
        txt.insert("0.0",self.text)
        txt.bind("<Key>", lambda evt: self._handle_keypress(evt))
        
        dismiss_button = ttk.Button(frame_btn, text="Dismiss", command=self.top.destroy)
        dismiss_button.bind("<Key>", lambda evt: self._handle_keypress(evt,True))
        
        txt_scrollx.pack(side=tk.BOTTOM,fill=tk.X)
        txt_scrolly.pack(side=tk.RIGHT,fill=tk.Y)
        txt.pack(side=tk.LEFT,fill=tk.BOTH,expand=1)
        dismiss_button.pack()
        dismiss_button.focus_set()

    def _handle_keypress(self,event,isbutton=False):
        if isbutton:
            if event.keysym == "Return": # or event.keysym == "Escape":
                event.widget.invoke() # press button
            if event.keysym == "Escape":
                self.top.destroy()
        else: # text output
            if event.keysym == "Prior" or event.keysym == "Next" or event.keysym == "Up" or event.keysym == "Down" or event.keysym == "Left" or event.keysym == "Right" or event.char == '\x03':
                return(None)
            elif event.char == '\x1b': # escape
                self.top.destroy() # get 
            else:
                return("break")

class TopCbWindow:
    '''
    toplevel checkbox window helper class
    @params: tkinter.object, list, string, string, dict
    '''
    def __init__(self, tkobj, lb_entries, el_key, el_search, config):
        # TODO: maybe just pass terminal config instead of whole config
        self.master = tkobj
        self.term = [config["terminal"], config["terminal_execute_flag"]]
        self.element_key_str = el_key
        self.element_search_str = el_search
        self._create_delete_view(lb_entries)

    def _create_delete_view(self,entries):
        top = tk.Toplevel(self.master)
        frame_txt = ttk.Frame(top)
        #frame_txt.bind("<Key>", lambda evt: self._handle_keypress(evt,top))
        frame_btn = ttk.Frame(top)
        frame_txt.pack(expand=True,fill=tk.BOTH)
        frame_btn.pack(fill=tk.X)

        dismiss_button = ttk.Button(frame_btn, text="Dismiss", command=top.destroy)
        dismiss_button.bind("<Key>", lambda evt: self._handle_keypress(evt,top,True))
        
        if len(entries) == 0:
            txt = ttk.Label(frame_txt,text="No files")
            txt.pack()
        else:
            delete_button = ttk.Button(frame_btn,text="Delete",command=lambda : self._delete_files(top))
            delete_button.bind("<Key>", lambda evt: self._handle_keypress(evt,top,True))
            self.selected_files = []
            count = 0
            for entry in entries:
                self.selected_files.append(tk.StringVar())
                cb = ttk.Checkbutton(frame_txt,text=entry,variable=self.selected_files[count],onvalue=entry,offvalue=' ')
                cb.bind("<Key>", lambda evt: self._handle_keypress(evt,top))
                cb.pack(anchor = "w")
                count += 1
            delete_button.pack()
        dismiss_button.pack()
        dismiss_button.focus_set()
        

    def _delete_files(self,top):
        cmd = [self.term[0],self.term[1],"sudo","rm"]+[i.get() for i in self.selected_files]
        # get action from last pressed Show Files button
        _g = (v for i,j in self.master.children['!frame'].children.items() for k,v in j.children.items() if self.element_key_str in k and self.element_search_str in v["text"])
        btn_action = list(_g)[0]
        sh = py_pbf_helper.RunThCmdSimple()
        #TODO: test if with subshell=True xterm could be killed if exit on main gui is clicked
        sh.setup(cmd)
        sh.start()
        def update():
            if sh.get_result() is None:
                top.after(250, update)
            else:
                # TEST
                #result = sh.get_result()
                #print(result)
                sh.stop()
                try:
                    btn_action.invoke() # press Show Files button
                except UnboundLocalError: # should not happen
                    print("couldnt set action. Button '%s' not found" %self.element_search_str)
                finally:
                    top.destroy() # quit window
        # exec update shortly after shell window closed
        top.after(250, update)

    def _handle_keypress(self,event,obj,isbutton=False):
        if isbutton:
            if event.keysym == "Return": # or event.keysym == "Escape":
                event.widget.invoke() # press button
            if event.keysym == "Escape":
                obj.destroy()
        else: # frame or cb entry
            if event.char == '\x1b': # escape
                obj.destroy() # get
