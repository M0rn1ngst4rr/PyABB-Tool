import tkinter as tk
import time
import ttkbootstrap as ttkb
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from os import makedirs, getcwd, path
from utils import *

def get_folder_path():
    folder_path = fd.askdirectory()
    tab1_folder_box.delete(0, tk.END)
    tab1_folder_box.insert(0, folder_path)

def rename():
    errored = False
    try:
        pre_path = tab1_folder_box.get()
        pre = tab1_pre_box.get()
        start = int(tab1_start_box.get())
        step = int(tab1_step_box.get())
        p_declare_list = ['    !**********************************************************\n', '    !*            Fuegepunkt-Deklarationen\n', '    !**********************************************************\n']
        r_declare_list = ['    !**********************************************************\n', '    !*            Raumpunkt-Deklarationen\n', '    !**********************************************************\n']
        try:
            mod_Files = getFiles(pre_path)
            for file in mod_Files:
                try:
                    file_path = path.join(pre_path, file)
                    org_file = readfile(file_path)
                    points = getPoints(org_file)
                    coordinates = getCoordiantes(org_file)
                    p_points = getProcessPoints(org_file)
                    unused = findUnused(p_points, points, coordinates)
                    cleaned_up = cleanup(org_file, unused)
                    new_x_file = renameRPoints(cleaned_up, points)
                    x_points = getPoints(new_x_file)
                    new_file = renameRPoints(lines=new_x_file, r_points=x_points,pre=pre,step=step,start=start)
                    new_points = getPoints(new_file)
                    new_coordiantes = getCoordiantes(new_file)
                    test_file = sort(new_file, p_declare_list, r_declare_list, p_points, new_points, new_coordiantes)
                    writeNewFile(pre_path, file, test_file)
                except Exception as e:
                    try:
                        makedirs(f"{getcwd()}/logs")
                    except:
                        pass
                    timestr = time.strftime("%Y%m%d_%H%M%S")
                    with open(f"{getcwd()}/logs/{timestr}_error.txt", 'a') as f:
                        f.write(f"Problem in File: {file} -> {e}\n")
                    mb.showerror(title="Error", message=f"Problem in File: {file} -> {e} \n -> {getcwd()}\\logs\\{timestr}_error.txt")
        except:
            mb.showerror("Error", "Folder not found")
            errored = True
    except Exception as e:
        mb.showerror(title="Error", message=f"Error accured -> {e}")
        errored = True
    if errored == False:
        mb.showinfo(title="Success", message="Done")
    if path.exists(path.join(pre_path, "new")):
        tab1_folder_button.config(state="normal")
    
# Create the main window
main = ttkb.Window(themename="superhero")
main.geometry("800x300")
main.title("ABB-Tool")
#main.iconbitmap("./icon.ico")

# tab_Control
tab_Control = ttkb.Notebook(main)
tab1 = ttkb.Frame(tab_Control)
tab_Control.add(tab1, text='Programmbereinigung')
tab_Control.pack(expand=1, fill="both")

# Tab 1
tab1_Header_lable = ttkb.Label(tab1, text="Roboterprogramm bereinigung")
tab1_folder_box = ttkb.Entry(tab1, width=50)
tab1_folder_box.insert(0, "Folder Path")
tab1_folder_button = ttkb.Button(tab1, text="Browser", command=lambda: get_folder_path())
tab1_start_button = ttkb.Button(tab1, text="Start", command=lambda: rename())
tab1_step_lable = ttkb.Label(tab1, text="Steps")
tab1_step_box = ttkb.Entry(tab1, width=3)
tab1_step_box.insert(0, "10")
tab1_pre_lable = ttkb.Label(tab1, text="Pre")
tab1_pre_box = ttkb.Entry(tab1, width=3)
tab1_pre_box.insert(0, "p")
tab1_start_lable = ttkb.Label(tab1, text="Start")
tab1_start_box = ttkb.Entry(tab1, width=3)
tab1_start_box.insert(0, "10")
tab1_open_folder_button = ttkb.Button(tab1, text="Finished")
tab1_open_folder_button.config(state="disabled")

# Pack the widgets
tab1_Header_lable.pack(anchor=tk.N, side=tk.TOP)
tab1_folder_box.pack(anchor=tk.NW, side=tk.LEFT)
tab1_folder_button.pack(anchor=tk.NW, side=tk.LEFT)
tab1_start_button.pack(anchor=tk.SE, side=tk.RIGHT)
tab1_pre_box.pack(anchor=tk.NE, side=tk.RIGHT)
tab1_pre_lable.pack(anchor=tk.NE, side=tk.RIGHT, pady=5)
tab1_step_box.pack(anchor=tk.NE, side=tk.RIGHT)
tab1_step_lable.pack(anchor=tk.NE, side=tk.RIGHT, pady=5)
tab1_start_box.pack(anchor=tk.NE, side=tk.RIGHT)
tab1_start_lable.pack(anchor=tk.NE, side=tk.RIGHT, pady=5)
tab1_open_folder_button.pack(anchor=tk.SE, side=tk.RIGHT)


if __name__ == "__main__":
    main.mainloop()