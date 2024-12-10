
from tkinter import *
import customtkinter


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def change_appearance_mode_event(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)

# Function to calculate BMI and update the labels
def calculate_bmi(event=None):
    height = root.slider_2.get() / 100  # Convert height to meters
    weight = root.slider_kg.get()
    bmi = weight / (height ** 2)

    # Update BMI value label
    root.outcome_label.configure(text=f" {bmi:.1f}")

    # Update live height and weight labels
    root.cm_label.configure(text=f"{root.slider_2.get():.0f} ")
    root.kg_label.configure(text=f"{root.slider_kg.get():.0f} ")

    # Update progress bar and its color based on BMI value
    if bmi < 18.5:
        bmi_progressbar.set(bmi / 40)
        bmi_progressbar.configure(progress_color="orange")
    elif 18.5 <= bmi <= 24.9:
        bmi_progressbar.set(bmi / 40)
        bmi_progressbar.configure(progress_color="green")
    elif 25 <= bmi <= 29.9:
        bmi_progressbar.set(bmi / 40)
        bmi_progressbar.configure(progress_color="orange")
    else:
        bmi_progressbar.set(bmi / 40)
        bmi_progressbar.configure(progress_color="red")

#Root
root = customtkinter.CTk()
root.geometry("700x600")
root.title("My I-BMI.py")

openstack_icon = root.iconbitmap('C:\\Users\\HNS10\\Learning projects\\I-BMI Calculator\\bmi.ico')

#Grid colum system
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure((2, 3), weight=0)
root.grid_rowconfigure((0, 1, 2), weight=1)

# create sidebar frame
root.sidebar_frame = customtkinter.CTkFrame(root, width=140, corner_radius=0)
root.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
root.sidebar_frame.grid_rowconfigure(4, weight=1)

# label
root.logo_label = customtkinter.CTkLabel(root.sidebar_frame, text="Length(cm)",
                                         font= customtkinter.CTkFont(size=24, weight="bold"))
root.logo_label.grid(row=0, column=0, padx=40, pady=(20, 5))
#CM attached to slider2

root.cm_label = customtkinter.CTkLabel(root.sidebar_frame   , font= customtkinter.CTkFont(size=45, weight="bold"))
root.cm_label.grid(row=1, column=0, padx=40, pady=(5, 10))

#Slidebar & progressbar frame
root.slider_2 = customtkinter.CTkSlider(root.sidebar_frame, from_=100, to=240, orientation="vertical")
root.slider_2.grid(row=2, column=0, rowspan=3, padx=(20,10), pady=(10, 10), sticky="ns")
root.slider_2.set(170)  # Default value
root.slider_2.bind("<B1-Motion>", calculate_bmi)

#Appearance mode
root.appearance_mode_label = customtkinter.CTkLabel(root.sidebar_frame, text="Appearance Mode:", anchor="w")
root.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
root.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(root.sidebar_frame, values=[ "Dark","Light"],
                                                               command=change_appearance_mode_event)
root.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))



# create slider and progressbar frame
#BMI result
# Progress bar to visualize the BMI score
bmi_progressbar = customtkinter.CTkProgressBar(root, width=300, height=25)
bmi_progressbar.grid(row=0, column=1, padx=0, pady=(230,10))
bmi_progressbar.set(0.5)  # Initialize with default value


root.outcome_label = customtkinter.CTkLabel(root, font= customtkinter.CTkFont(size=90, weight="bold"))
root.outcome_label.grid(row=0, column=1, padx=20, pady=(1, 5))

root.bmi_label = customtkinter.CTkLabel(root, text="BMI", font= customtkinter.CTkFont(size=40, weight="bold"))
root.bmi_label.grid(row=0, column=1, padx=40, pady=(130, 5))



root.kg_label = customtkinter.CTkLabel(root, text="Weight(kg)",font= customtkinter.CTkFont(size=24, weight="bold"))
root.kg_label.grid(row=0, column=1, padx=40, pady=(410, 5))


root.kg_label = customtkinter.CTkLabel(root, font= customtkinter.CTkFont(size=45 , weight="bold"))
root.kg_label.grid(row=1, column=1, padx=10, pady=(5, 5))

root.slider_kg = customtkinter.CTkSlider(root, from_=20, to=160,)
root.slider_kg.grid(row=3, column=1, columnspan=5, padx=(10, 10), pady=(30, 40), sticky="ns")
root.slider_kg.set(70)  # Default value
root.slider_kg.bind("<B1-Motion>", calculate_bmi)

calculate_bmi()

root.mainloop()
