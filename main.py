
# ArduinoReader -> _AR.read()
import ArduinoReader as _AR
# bd_connector ->  find_user(number) , insert_hr(number,data)
import db_connector as db

# Verify DB
number_active = db.db_check()

if number_active != "":

	print("....Utilizaremos el Numero de celular {} para registrar...".format(number_active))
	_AR.insert_hr_data(number_active)

else:
	print("Escribe el numero con el que deseas registrar la informacion del sensor")
	numero = input()
	_AR.insert_hr_data("whatsapp:+521"+numero)

# para activar ambiente source env/bin/activate 
