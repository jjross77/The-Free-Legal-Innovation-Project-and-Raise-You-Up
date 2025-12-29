# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:32:18 2024

@author: yyyyyyyyyyyyyyyyyyyy
"""
def create_new_method_dictionary(self,event):
      """ if we wrote the problem manually we will automically save it after a minute"""
      import time
      import re
      # save method
      #self.method_recorded=self.text_box1.get('1.0', 'end')
      #self.method_recorded=re.sub('\n',"",self.problem_recorded)
      #self.method_recorded="?? "+ self.method_recorded
      #time_created =time.time()
      self.method_list_dictionary={}

      
      #self.current_method_step=self.method_recorded

def generate_head_note_for_main_box():
    """erase center box widget but keep buttons in the correct position in the frame """
    button_list=[decrease,increase,decrease,decrease,decrease,decrease,decrease,decrease,decrease,decrease]
    text_list=["1:Conns-Design","2:Steps-Design","Web-Grab","Update-Databases","New-Problem","List-Past-Problems","List-Problems","Record_Problem"]
    for ii, button_type,textt in zip(range(9),button_list,text_list):
        self.button = tk.Button(master=self.frame6, text=textt, fg='white')
        #command=self.highlight_text,
        self.button.grid(row=0, column=ii, sticky="nsew")
        self.button.config(font=('Times New Roman',10),bg='green')
        if textt=="List-Past-Problems":
            self.button.bind("<Button-1>",self.list_past_problems)

        if textt=="List-Problems":
            self.button.bind("<Button-1>",self.list_possble_problems)
            
        if textt=="Record_Problem":
            self.button.bind("<Button-1>",self.record_problem_and_create_problem_dictionary)
            
        if textt=="2:Steps-Design":
            self.button.bind("<Button-1>",self.switch_to_method_window)
    
def upload_problem_web():
    """ access a program to generate a image of the dictiionary we created for the problem in conn design"""
    import networkx as nx
    import matplotlib.pyplot as plt
    from PIL import ImageTk, Image
    self.text_box.destroy()
    self.text_box0.destroy()
    self.text_box01.destroy()
    self.label1.destroy()
    self.label2.destroy()
    self.frame8.destroy()
    G=nx.Graph()
    G.add_nodes_from(self.node_name_list)
    G.add_edges_from(self.edge_map)
    plt.figure(figsize=(15,12),dpi=80)
    nx.draw_networkx(G, with_labels=True, node_color=self.color_map, font_weight='bold',edge_color='#A0CBE2',font_color='black',node_size=100,font_size=8)
    plt.savefig(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Downloads\problem_solving_project\temp_web_folder\web.png',format="PNG",bbox_inches='tight' )
    image = Image.open(r'C:\Users\yyyyyyyyyyyyyyyyyyyy\Downloads\problem_solving_project\temp_web_folder\web.png')
    self.frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
    self.frame.grid(row=0,column=1)
    self.frame.config(bg="white")
    canvass = tk.Canvas(self.frame, bg="white",height=500, width=1000)#1000 # height 600
    # need to modify these to be related to grid somehow
    # like raito of screen
    canvass.grid()
    canvass.update()
    hieght=canvass.winfo_height()
    width=canvass.winfo_width()
    print(hieght)
    print(width)
    resize_image = image.resize((width-70, hieght-130))#width-70, hieght-170 # 150
    # how much to resize by accoidng to width of canvas
    self.photo = ImageTk.PhotoImage(resize_image)
    canvass.create_image(470,190 , image = self.photo) #470,230 # 180
    # location on the screen
    self.frame6.config(bg="white")