from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom 
from report import Report

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # ===============1st img==================
        img1 = Image.open(r"D:\Coding\python\Hotel Management\hotel images\hotel1.png")
        img1 = img1.resize((1550, 140), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbl_img1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lbl_img1.place(x=0, y=0, width=1550, height=140)

        # ===============logo==================
        img2 = Image.open(r"D:\Coding\python\Hotel Management\hotel images\logohotel.png")
        img2 = img2.resize((230, 140), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbl_img2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lbl_img2.place(x=0, y=0, width=230, height=140)

        # ===============title==================
        Ibl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        Ibl_title.place(x=0, y=140, width=1550, height=50)

        #===============main frame==================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        # ===============menu==================
        Ibl_menu=Label(main_frame,text="Menu",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        Ibl_menu.place(x=0, y=0, width=230)

        #===============btn frame==================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0, y=40, width=225, height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)
        
        report_btn=Button(btn_frame,text="REPORT",command=self.Report,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",width=22,command=self.logout,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)

        # ===============right side image==================
        img3 = Image.open(r"D:\Coding\python\Hotel Management\hotel images\slide3.jpg")
        img3 = img3.resize((1300,590), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbl_img3 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lbl_img3.place(x=225, y=0, width=1300, height=590)

        # ===============down images==================
        img4 = Image.open(r"D:\Coding\python\Hotel Management\hotel images\myh.jpg")
        img4 = img4.resize((220, 300), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lbl_img4 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lbl_img4.place(x=0, y=230, width=230, height=210)

        img5 = Image.open(r"D:\Coding\python\Hotel Management\hotel images\food.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lbl_img5 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lbl_img5.place(x=0, y=400, width=230, height=200)



    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)


    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)

    def details_room(self):
        self.new_window = Toplevel(self.root)
        self.app = DetailsRoom(self.new_window)
        
    def Report(self):
        self.new_window = Toplevel(self.root)
        self.app = Report(self.new_window)

    def logout(self):
        self.root.destroy()    





if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
