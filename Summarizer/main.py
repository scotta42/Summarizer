import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import Frame
import Summarize as summarize
import extract_entities as ex_entities
import fact_extraction as fact_ex
import redact_text as redact_x

root = Tk()
root.title("Edit, Summarize, and Tokenize Text with SpaCy")
root.geometry("850x650")
text = " "


# Read only 'r'
# Read and Write 'r+' (beginning of file)
# Write Only 'w' (over-written)
# Write and Read 'w+' (over written)
# Append Only 'a' (end of file)
# Append and Read 'a+' (end of file)


def sample_txt():
    text_file = open("london.txt", 'r')
    text = text_file.read()
    my_text.insert(END, text)
    text_file.close()


def open_txt():
    text_file = filedialog.askopenfilename(initialdir="C:/Users/")
    text_file = open(text_file, 'r')
    file_location = text_file
    readtext = text_file.read()
    # messagebox.showerror(title="ReadFileError", message="File Type not Accepted")
    my_text.insert(END, readtext)
    global text
    text = readtext
    text_file.close()


def save_txt():
    # text_file = open("NewSavedTxt.txt", 'w')
    text_file = filedialog.asksaveasfilename(initialdir="C:/Users/", filetypes=(
                ("Text files", "*.txt"),
                ("Prolog files", "*.pl *.pro"),
                ("All files", "*.*"),
            ))
    text_file = open(text_file, 'w')
    text_file.write(my_text.get(1.0, END))
    text_file.close()


def save_file_as(file_path=None):
    # If there is no file path specified, prompt the user with a dialog which
    # allows him/her to select where they want to save the file
    if file_path is None:
        file_path = filedialog.asksaveasfilename(
            filetypes=(
                ("Text files", "*.txt"),
                ("Prolog files", "*.pl *.pro"),
                ("All files", "*.*"),
            )
        )

    try:
        # Write the Prolog rule editor contents to the file location
        text = open(file_path, "w")
        text.write(my_text.get(1.0, END))
        # text.file_path = file_path
        return "saved"

    except FileNotFoundError:
        return "cancelled"


def summary():
    fact_extract_hide()
    show_widget(second_text)
    second_text.delete('1.0', END)
    second_text.insert(END, summarize.summarize(text))


def extract_entity():
    fact_extract_hide()
    show_widget(second_text)
    second_text.delete('1.0', END)
    entity_list = ex_entities.extract(text)
    for entity in entity_list:
        second_text.insert(END, entity+"\n")


def fact_extract():
    show_widget(second_text)
    second_text.delete('1.0', END)
    subject = fact_text.get('1.0', END)
    if(fact_text != "Enter a Subject") or (len(subject) > 3):
        fact_list = fact_ex.fact_extract(text, fact_text.get('1.0', END))
        print(fact_text)
        for fact in fact_list:
            second_text.insert(END, fact+"\n")


def redact():
    fact_extract_hide()
    show_widget(second_text)
    second_text.delete('1.0', END)
    second_text.insert(END, redact_x.redact(text))


def fact_extract_hide():
    hide_widget(fact_text)
    hide_widget(go_button)


def fact_extract_show():
    show_widget(fact_text)
    show_widget(go_button)


def hide_widget(widget):
    widget.pack_forget()


def show_widget(widget):
    widget.pack()


bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM, pady=20)

my_text = Text(bottom_frame, width=65, height=10, font=("Helvetica", 16))
my_text.pack(side=TOP, pady=20)
second_text = Text(bottom_frame, width=65, height=10, font=("Helvetica", 16))
second_text.pack(side=BOTTOM)
hide_widget(second_text)
open_button = Button(root, text="Open Text File", command=open_txt)
open_button.pack(side=LEFT, pady=0)
save_button = Button(root, text="Save Text File", command=save_txt)
save_button.pack(side=LEFT, pady=0)
summarize_button = Button(root, text="Summarize Text", command=summary)
summarize_button.pack(side=LEFT, pady=0)
extract_button = Button(root, text="Extract Entities", command=extract_entity)
extract_button.pack(side=LEFT, pady=0)
redact_button = Button(root, text="Redact Text", command=redact)
redact_button.pack(side=LEFT, pady=0)
fact_button = Button(root, text="Extract Facts", command=fact_extract)
fact_button.pack(side=LEFT, pady=0)
fact_label = Label(root, text="Facts on London")
fact_label.pack(side=LEFT, pady=0)
fact_text = Text(root, width=15, height=1, font=("Helvetica", 16))
fact_text.pack(side=LEFT, pady=0)
fact_text.insert(END, "Enter a Subject")
go_button = Button(root, text="GO", command=fact_extract)
go_button.pack(side=LEFT, pady=0)
hide_widget(fact_text)
hide_widget(go_button)

root.mainloop()
