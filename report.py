import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from data import sales_data, inventory_data, sales_year_data, inventory_month_data



class Report:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")

        plt.rcParams["axes.prop_cycle"] = plt.cycler(
        color=["#4C2A85", "#BE96FF", "#957DAD", "#5E366E", "#A98CCC"])

# Chart 1: Bar chart of sales data
        fig1, ax1 = plt.subplots()
        ax1.bar(sales_data.keys(), sales_data.values())
        ax1.set_title("Sales by Product")
        ax1.set_xlabel("Product")
        ax1.set_ylabel("Sales")

# Chart 2: Horizontal bar chart of inventory data
        fig2, ax2 = plt.subplots()
        ax2.barh(list(inventory_data.keys()), inventory_data.values())
        ax2.set_title("Room Booked")
        ax2.set_xlabel("Rooms")
        ax2.set_ylabel("")


# Chart 3: Line chart of sales by year
        fig3, ax3 = plt.subplots()
        ax3.plot(list(sales_year_data.keys()), list(sales_year_data.values()))
        ax3.set_title("Sales by Year")
        ax3.set_xlabel("Year")
        ax3.set_ylabel("Sales")

# Chart 4: Area chart of inventory by month
        fig4, ax4 = plt.subplots()
        ax4.fill_between(inventory_month_data.keys(), inventory_month_data.values())
        ax4.set_title("Inventory by Month")
        ax4.set_xlabel("Month")
        ax4.set_ylabel("People")

# Set the initial size for a 14-inch screen
        initial_width = 1200
        initial_height = 800
        root.geometry(f"{1550}x{800}")

# Make the window resizable
        root.resizable(True, True)

        side_frame = tk.Frame(root, bg="#4C2A85")
        side_frame.pack(side="left", fill="y")

        label = tk.Label(side_frame, text="Dashboard", bg="#4C2A85", fg="#FFF", font=12)
        label.pack(pady=20, padx=10)

        charts_frame = tk.Frame(root)
        charts_frame.pack()

        upper_frame = tk.Frame(charts_frame)
        upper_frame.pack(fill="both", expand=True)

        canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
        canvas1.draw()
        canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

        canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
        canvas2.draw()
        canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)


        lower_frame = tk.Frame(charts_frame)
        lower_frame.pack(fill="both", expand=True)

        canvas3 = FigureCanvasTkAgg(fig3, lower_frame)
        canvas3.draw()
        canvas3.get_tk_widget().pack(side="left", fill="both", expand=True)

        canvas4 = FigureCanvasTkAgg(fig4, lower_frame)
        canvas4.draw()
        canvas4.get_tk_widget().pack(side="left", fill="both", expand=True)
        
# Create a window and add charts
if __name__=="__main__":
    root=tk.Tk()
    obj=Report(root)
    root.title("Report")
    root.mainloop()  


