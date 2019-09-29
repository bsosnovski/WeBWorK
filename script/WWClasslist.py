
#!/usr/bin/env python3
"""
 This Python script takes a list of students from CUNYFirst and produces a classlist file
 which can be used to import many students into WeBWorK quickly.
 Filename: WWclasslist.py
 Author: Bianca Sosnovski, QCC

 INSTRUCTIONS
 From CUNY Portal/CUNYFirst MyInfo download the class roster of students to be added to WeBWorK.
 A CSV file with ID, Last Name, First Name and Emails of students is
 created and saved in the destination of your choice.
 Enter the required information about your course as prompted by the program.
 After the program converts the file, upload the LST file to WeBWork in the File Manager.
 From the Classlist Editor, import users from the file uploaded
"""
#####

import tkinter as tk
from tkinter.ttk import Frame, Button
from tkinter import TOP, LEFT, RIGHT, YES, X, NORMAL, DISABLED
from tkinter import filedialog
from tkinter import messagebox
#from PIL import Image, ImageTk
import os
import csv

def openFile():
    global inputfilename
    inputfilename=filedialog.askopenfilename(title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
    var.set(inputfilename)
    input_button.bind("<Button-1>", show_button(conversion))

#####

def show_button(conversion):
    global convert_button
    convert_button= tk.Button(row, text='CONVERT FILE', state=NORMAL, font = 'Arial 12', height = 2, width = 25,  command=conversion)
    convert_button.config(bg='sky blue')
    convert_button.pack()
    lab1.config(state=DISABLED)
    lab2.config(state=DISABLED)

#####

def conversion():
    entry1=input_entry1.get()
    entry2=input_entry2.get()
    entry3=input_entry3.get()
    entries=(entry1, entry2, entry3)
    filename=input_entry4.get()
    #print(filename)
    WW_Fields(entries)
    outputfilename = 'WW_'+section+'_roster.lst' # must end in ".lst
    try:
        CSV2WW(filename,outputfilename)
        lab1.config(text='\nYOUR WW CLASSLIST FILE IS READY!', state=NORMAL)
        lab2.config(fg='red',text='WW classlist file name: '+outputfilename+'\nWW classlist file location: '+FilePath, state=NORMAL)
    except NameError:
        messagebox.showinfo('Select a File', '\nYOU MUST SELECT A FILE!')
    except:
        messagebox.showerror('Error!!!','YOU DIDN\'T SELECT A FILE WITH EXTENSION CSV!!!')

    convert_button.pack_forget()

#####

def WW_Fields(entries):
    global recitation, course, section, comment, permission, password, status
    # The recitation field will be set to the string below (can be left blank)
    recitation = entries[0]
    # The section field will be set to the string below (can be left blank)
    course = entries[1].strip()
    section = course+'_'+entries[2].strip()
    # The comment field will be set to the string below (can be left blank)
    comment = ''
    permission = '' # empty string sets it to 0, that is, student permission
    password = '' # empty string sets it to studentID
    status = 'C' # C is for current

def CSV2WW(csvFile,lstFile):
    global FilePath
    FilePath=os.path.dirname(csvFile)
    with open(csvFile, 'rt', newline='') as infile:
        reader_object = csv.reader(infile, delimiter=',', quoting=csv.QUOTE_ALL)
        outfile = open(os.path.join(FilePath, lstFile), 'w')

        rownum = 0
        for row in reader_object:
            if rownum > 0: # We have passed the header row
                # Data from the CSV file
                userid= row[0].strip()
                name = row[1].strip()
                email = row[4].strip()
                email = email.replace(" ", "")

                # separate first and last names contained in csv file
                student_names=[x.strip() for x in name.split(',')]
                lastname = student_names[0]
                firstname = student_names[1]

                # login name
                letters = list(firstname)
                initial = letters[0]
                username = initial+lastname
                username = username.lower()
                username = username.replace(" ", "")

                 # The list of columns for 'lineout' are as in http://webwork.maa.org/wiki/Classlist_Files#.VKw0tCvF98E
                lineout = userid+','+lastname+','+firstname+','+status+','+comment+','+section+','+recitation+','+email+','+username+','+password+','+permission
                #print(lineout)
                outfile.write(lineout+'\n')
            rownum = rownum + 1

        outfile.close()

#####


# Main function

root = tk.Tk()
root.title("CUNYFirst2WW Converter")
root.configure(background='sky blue')


instructions = """\n
This is a \"CUNTFirst roster to WeBWorK classlist\" converter.\n
Author: Bianca Sosnovski (QCC) \n\n
INSTRUCTIONS: 
    - From CUNY Portal/ CUNYFirst MyInfo download the class roster of 
    students to be added to WeBWorK.\n
    A CSV file with ID, Last Name, First Name and Emails of the students 
    is created and saved in your computer.\n
    - Enter the required information about your course as prompted below by the program.\n
    - After the file is converted to WeBWorK format, upload the LST file to the File Manager in WeBWorK.\n
    - From the Classlist Editor, import users from the LST file.\n\n
Enter the information below and select the file to convert.\n"""

msg = tk.Message(root, padx=15, text=instructions,font = "Verdana 11 bold", background='sky blue').pack()

stringInput1 = tk.StringVar()
stringInput2 = tk.StringVar()
stringInput3 = tk.StringVar()
var = tk.StringVar()

row = Frame(root)
input_label1 = tk.Label(row, padx=15, width=13, text='Semester and year: ', background='sky blue',anchor='w')
input_entry1 = tk.Entry(row, textvariable=stringInput1)
input_entry1.insert(0,'')
row.pack(side=TOP, fill=X, padx=10, pady=2)
input_label1.pack(side=LEFT)
input_entry1.pack(side=RIGHT, expand=YES, fill=X)
input_entry1.focus()

row = Frame(root)
input_label2 = tk.Label(row, padx=15, width=13, text='Course: ', background='sky blue', anchor='w')
input_entry2 = tk.Entry(row, textvariable=stringInput2)
input_entry2.insert(0,'')
row.pack(side=TOP, fill=X, padx=10, pady=2)
input_label2.pack(side=LEFT)
input_entry2.pack(side=RIGHT, expand=YES, fill=X)

row = Frame(root)
input_label3 = tk.Label(row, padx=15, width=13, text='Section: ', background='sky blue', anchor='w')
input_entry3 = tk.Entry(row, textvariable=stringInput3)
input_entry3.insert(0,'')
row.pack(side=TOP, fill=X, padx=10, pady=2)
input_label3.pack(side=LEFT)
input_entry3.pack(side=RIGHT, expand=YES, fill=X)

row = Frame(root)
input_label4 = tk.Label(row, padx=15, width=13, text='File: ', background='sky blue', anchor='w')
input_entry4 = tk.Entry(row, textvariable=var);
input_entry4.insert(0,'')
input_button = tk.Button(row, text="Browse", width=6, command =openFile)
row.pack(side=TOP, fill=X, padx=10, pady=2)
input_label4.pack(side=LEFT)
input_entry4.pack(side=LEFT,expand=YES, fill=X)
input_button.pack(side=RIGHT, fill=X)


row = Frame(root)
lab1 = tk.Label(root,  padx=5, background='sky blue')
lab2 = tk.Label(root, padx=5, background='sky blue')
row.pack(side=TOP, padx=1, pady=5)
lab1.pack()
lab2.pack()

root.mainloop()
