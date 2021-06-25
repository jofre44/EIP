import pywebio
from pywebio.input import *
from pywebio.output import *

def bmi():

    put_text("Actividad con PywebIO")
    put_text("Alumno: Jose Sepulveda")

    bmi_list= [
        [16, 'Muy por debajo del peso ideal'],
        [18.5, 'Por debajo del peso ideal'],
        [25, 'En peso ideal'],
        [30, 'En sobre peso'],
        [35, 'En sobre peso severo'],
        [40, 'Obeso']
    ]

    def popup_funct(value, char):
        if value == 16:
            text= """Comer el doble de calorías y hacer ejericios para ganar fuerza. Aumentar el consumo de calorías porgresivamente"""
        elif value == 18.5:
            text= "Comer 1.5 más de calorías y hacer ejericios para ganar fuerza"
        elif value == 25:
            text= "Comer mejor calidad de calorías y hacer ejercicios de tonificación para definir"
        elif value == 30:
            text= "Comer un 10% menos de calorías y hacer ejericios de musculación y cardio"
        elif value == 35:
            text= "Comer un 25% menos de calorías y hacer ejericios de musculación y cardio"
        elif value == 40:
            text= """Comer un 40% menos de calorías y hacer ejericios de alta intensidad y musculación. Disminuir el consumo de calorías progresivamente"""        
        elif value == 41:
            text= """Comer un 60% menos de calorías y hacer ejericios de alta intensidad y musculación. Disminuir el consumo de calorías progresivamente"""
        popup(char, text)               

    heigh = input("Ingresa tu estatura (en cm): ", type=FLOAT)
    weight = input("Ingresa tu peso (en kg): ", type=FLOAT)

    bmi_value = weight / ((heigh / 100) **2)

    for value, char in bmi_list:
        if bmi_value < value:
            text_aux = f"Tu BMI es: {round(bmi_value,2)}, estas {char.lower()}"
            break
        elif bmi_value > 40:
            text_aux = f"Tu BMI es: {round(bmi_value,2)}, estas severamente obeso"

    put_text(text_aux)
    put_collapse("Tabla de referencia", [
        put_table([
            ['BMI Máximo', 'Descripción', 'Sugerencia'],
            [bmi_list[0][0],bmi_list[0][1], put_buttons(["Ver"], onclick=lambda _: popup_funct(bmi_list[0][0], bmi_list[0][1]))],
            [bmi_list[1][0],bmi_list[1][1], put_buttons(["Ver"], onclick=lambda _: popup_funct(bmi_list[1][0], bmi_list[1][1]))],
            [bmi_list[2][0],bmi_list[2][1], put_buttons(["Ver"], onclick=lambda _: popup_funct(bmi_list[2][0], bmi_list[2][1]))],
            [bmi_list[3][0],bmi_list[3][1], put_buttons(["Ver"], onclick=lambda _: popup_funct(bmi_list[3][0], bmi_list[3][1]))],
            [bmi_list[4][0],bmi_list[4][1], put_buttons(["Ver"], onclick=lambda _: popup_funct(bmi_list[4][0], bmi_list[4][1]))],
            [bmi_list[5][0],bmi_list[5][1], put_buttons(["Ver"], onclick=lambda _: popup_funct(bmi_list[5][0], bmi_list[5][1]))],
            ['Superior a 40', 'Severamente obeso', put_buttons(["Ver"], onclick=lambda x: popup_funct(41, 'Severamente obeso'))]
        ]),
        ], open=True)

    checkbox("Terminar análisis", options=['Ya has revisado los resultados?'])

    

    

    

    

if __name__ == '__main__':
    pywebio.start_server(bmi, port=80, debug=True)