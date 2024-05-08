import gspread
import tkinter as tk
from tkinter import ttk, messagebox


'''
__Here are the constants__

'''
font_tuple=("Comic Sans MS",16,"bold")
font_tuple_small=("Comic Sans MS",14,"bold")
font_tuple_Big=("Comic Sans MS",16,"bold")

Credentialfile="/Users/achrafcheniti/Desktop/Python projects/Productivity Calculator/Credential.json"

Sa=gspread.service_account(filename=Credentialfile)

Number_of_orders=0


def BatchChecker(String=str):
    global Number_of_orders
    try:
        BatchSpreadSheet=Sa.open(String)
        Email_Sheet=BatchSpreadSheet.worksheet("Email")
        Number_of_orders+=int(Email_Sheet.acell("B4").value[:2])
        return True
    except:
        return False

class ProductivityNumbergetter(tk.Tk):
    
    def Submitfunc(self,):
        global Number_of_orders
    
        if (BatchChecker(self.BatchEntry.get())==True):
            messagebox.showinfo("Update","The number of orders has been retrieved successfuly!")  
        else:
            messagebox.showwarning("Warning","The batch you entered isn't either shared with credentials or isn't a batch!")

    def GetResult(self):
       global Number_of_orders
       messagebox.showinfo("Update",f"Your total number of orders is {Number_of_orders}")
       Number_of_orders=0

    def __init__(self)-> None:
        super().__init__()
        '''__Title and logo__'''
        self.title("Productivity number getter")
        '''__Style__'''
        style_text=ttk.Style()
        style_text.configure("my.TButton", font=font_tuple_small, foreground="green")
        style_text.configure("Big.TButton",font=font_tuple_small,foreground="red")
        style_text.configure("Result.TButton",font=font_tuple_small,foreground="blue")
        '''__Buttons and Entries__'''
        self.MyFrame=ttk.Frame(self,)
        self.MyFrame.pack()
        
        self.BatchEntry=ttk.Entry(self.MyFrame, width=23, font=font_tuple)
        self.BatchEntry.grid(row=0,column=0, padx=10,pady=10)
        
        self.ButtonBatch=ttk.Button(self.MyFrame,text="Submit", style="my.TButton", command=self.Submitfunc)
        self.ButtonBatch.grid(row=0,column=1,padx=5)  
        
        self.ResultButton=ttk.Button(self,text="Get results",style="Result.TButton", command=self.GetResult)  
        self.ResultButton.pack()



if __name__=="__main__":
    App=ProductivityNumbergetter()
    App.mainloop()
        