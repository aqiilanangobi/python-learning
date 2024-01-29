import datetime
open("output.txt","w+")
file=open("output.txt","w+")
file.write("this is a programming language")

file.write(f"\t\tISLAMIC UNIVERSITY IN UGANDA \n\t\t\tKAMPALA campus \n\t\tNAME:\t\tAqiila Nangobi \n\t\tLECTURER:\tMr.walusimbi hakim \n\t\tCOURSE UNIT:Structured programming \n\t\tDATE:\t\t{datetime.date.today()} \n\t\t\t**********end************")
print()