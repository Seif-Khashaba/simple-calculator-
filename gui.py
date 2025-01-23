import tkinter as tk
from logic import calculation, last_answer, evaluate_expression, convert_decimal_fraction

text_result = None
calculation = ""
last_answer = ""

def init_gui(root):
    global text_result
    root.geometry("300x400")
    text_result = tk.Text(root, height=2, width=40, font=("Arial", 24))
    text_result.grid(columnspan=100)
    create_buttons(root)

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation, last_answer
    result = evaluate_expression(calculation)
    if result != "Error":
        calculation = result
        last_answer = result
    else:
        calculation = ""
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation if calculation else "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

def delete_last_character():
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def decimal_fraction():
    global calculation
    result = convert_decimal_fraction(calculation)
    if result != "Error":
        calculation = result
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    else:
        clear_field()
        text_result.insert(1.0, "Error")

def percentage():
    global calculation
    try:
        if calculation.endswith("%"):
            calculation = str(eval(calculation) * 100)
        else:
            calculation += "*100"
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def insert_last_answer():
    global last_answer, calculation
    if last_answer != "":
        calculation += last_answer
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

def create_buttons(root):
    
    btn_1=tk.Button(root,text="1",command=lambda:add_to_calculation(1),width=5,font=("Arial", 14 ))
    btn_1.grid(row=2,column=1)
    btn_2=tk.Button(root,text="2",command=lambda:add_to_calculation(2),width=5,font=("Arial", 14 ))
    btn_2.grid(row=2,column=2)
    btn_3=tk.Button(root,text="3",command=lambda:add_to_calculation(3),width=5,font=("Arial", 14 ))
    btn_3.grid(row=2,column=3)
    btn_4=tk.Button(root,text="4",command=lambda:add_to_calculation(4),width=5,font=("Arial", 14 ))
    btn_4.grid(row=3,column=1)
    btn_5=tk.Button(root,text="5",command=lambda:add_to_calculation(5),width=5,font=("Arial", 14 ))
    btn_5.grid(row=3,column=2)
    btn_6=tk.Button(root,text="6",command=lambda:add_to_calculation(6),width=5,font=("Arial", 14 ))
    btn_6.grid(row=3,column=3)
    btn_7=tk.Button(root,text="7",command=lambda:add_to_calculation(7),width=5,font=("Arial", 14 ))
    btn_7.grid(row=4,column=1)
    btn_8=tk.Button(root,text="8",command=lambda:add_to_calculation(8),width=5,font=("Arial", 14 ))
    btn_8.grid(row=4,column=2)
    btn_9=tk.Button(root,text="9",command=lambda:add_to_calculation(9),width=5,font=("Arial", 14 ))
    btn_9.grid(row=4,column=3)
    btn_0=tk.Button(root,text="0",command=lambda:add_to_calculation(0),width=5,font=("Arial", 14 ))
    btn_0.grid(row=5,column=2)
    btn_plus=tk.Button(root,text="+",command=lambda:add_to_calculation("+"),width=5,font=("Arial", 14 ))
    btn_plus.grid(row=2,column=4)
    btn_minus=tk.Button(root,text="-",command=lambda:add_to_calculation("-"),width=5,font=("Arial", 14 ))
    btn_minus.grid(row=3,column=4)
    btn_multiple=tk.Button(root,text="x",command=lambda:add_to_calculation("x"),width=5,font=("Arial", 14 ))
    btn_multiple.grid(row=4,column=4)
    btn_divide=tk.Button(root,text="/",command=lambda:add_to_calculation("/"),width=5,font=("Arial", 14 ))
    btn_divide.grid(row=5,column=4)
    btn_open=tk.Button(root,text="(",command=lambda:add_to_calculation("("),width=5,font=("Arial", 14 ))
    btn_open.grid(row=5,column=1)
    btn_close=tk.Button(root,text=")",command=lambda:add_to_calculation(")"),width=5,font=("Arial", 14 ))
    btn_close.grid(row=5,column=3)
    btn_dott=tk.Button(root,text=".",command=lambda:add_to_calculation("."),width=5,font=("Arial", 14 ))
    btn_dott.grid(row=6,column=3)
    btn_sin=tk.Button(root,text="sin",command=lambda:add_to_calculation("sin("),width=5,font=("Arial", 14 ))
    btn_sin.grid(row=7,column=1)
    btn_cos=tk.Button(root,text="cos",command=lambda:add_to_calculation("cos("),width=5,font=("Arial", 14 ))
    btn_cos.grid(row=7,column=2)
    btn_tan=tk.Button(root,text="tan",command=lambda:add_to_calculation("tan("),width=5,font=("Arial", 14 ))
    btn_tan.grid(row=7,column=3)
    btn_equql=tk.Button(root,text="=",command=evaluate_calculation,width=5,font=("Arial", 14 ))
    btn_equql.grid(row=6,column=4)
    btn_clear=tk.Button(root,text="C",command=clear_field,width=12,font=("Arial", 14 ))
    btn_clear.grid(row=9,column=1,columnspan=2)
    btn_delete=tk.Button(root,text="del",command=delete_last_character,width=5,font=("Arial", 14 ))
    btn_delete.grid(row=8,column=4)
    btn_sqrt = tk.Button(root, text="√", command=lambda: add_to_calculation("√("), width=5, font=("Arial", 14))
    btn_sqrt.grid(row=7, column=4)  
    btn_power = tk.Button(root, text="^", command=lambda: add_to_calculation("^"), width=5, font=("Arial", 14))
    btn_power.grid(row=8, column=1)
    btn_ln = tk.Button(root, text="ln", command=lambda: add_to_calculation("ln("), width=5, font=("Arial", 14))
    btn_ln.grid(row=8, column=2)
    btn_e = tk.Button(root, text="e", command=lambda: add_to_calculation("e"), width=5, font=("Arial", 14))
    btn_e.grid(row=8, column=3)
    btn_decimal_fraction = tk.Button(root, text="S↔D", command=decimal_fraction, width=5, font=("Arial", 14))
    btn_decimal_fraction.grid(row=9, column=3)
    btn_pi = tk.Button(root, text="π", command=lambda: add_to_calculation("pi"), width=5, font=("Arial", 14))
    btn_pi.grid(row=6, column=1)
    btn_percentage = tk.Button(root, text="%", command=percentage, width=5, font=("Arial", 14))
    btn_percentage.grid(row=6, column=2)
    btn_ans = tk.Button(root, text="Ans", command=insert_last_answer, width=5, font=("Arial", 14))
    btn_ans.grid(row=9, column=4) 

    root.mainloop()