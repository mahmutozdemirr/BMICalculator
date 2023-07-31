import tkinter

bmi_window = tkinter.Tk()
bmi_window.title("BMI Calculator")
bmi_window.config(padx=80, pady=80)

def calculate_bmi():
    height = height_input.get()
    weight = weight_input.get()

    if weight == "" or height == "":
        resul_label.config(text="Enter both weight and height")
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            result_string = write_result(bmi)
            resul_label.config(text=result_string)
        except:
            resul_label.config(text="Enter a valid number")


#arayüz
bmi_label_weight = tkinter.Label(text="Enter Your Weight (kg)")
bmi_label_weight.pack()

weight_input = tkinter.Entry(width=10)
weight_input.pack()


bmi_label_height = tkinter.Label(text="Enter Your Height (cm)")
bmi_label_height.pack()

height_input = tkinter.Entry(width=10)
height_input.pack()

calculate_button = tkinter.Button(text="Calculate", command=calculate_bmi)
calculate_button.pack()

resul_label = tkinter.Label()
resul_label.pack()

def write_result(bmi):
    resul_string = f"Your BMI is: {round(bmi,2)}. You are "
    if bmi <= 16:
        resul_string += "severly thin!"
    elif 16 < bmi <= 17:
        resul_string += "moderately thin!"
    elif 17 < bmi <= 18.5:
        resul_string += "mild thin!"
    elif 18.5 < bmi <= 25:
        resul_string += "normal"
    elif 25 < bmi <= 30:
        resul_string += "overweight"
    elif 30 < bmi <= 35:
        resul_string += "obese class 1"
    elif 35 < bmi <= 40:
        resul_string += "obese class 2"
    else:
        resul_string += "obese class 3"
    return resul_string


bmi_window.mainloop()

