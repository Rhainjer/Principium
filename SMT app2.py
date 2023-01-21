from SMT_module import *
permission="YES"
print(
    "WELCOME TO SMT  JAMB/WAEC APP\nYOU CAN USE IT TO PRACTICE FOR JAMB/WAEC STUDENTS \nMAKE A CHOICE  FROM THE OPTIONS BELOW\nSIT BACK AND ENJOY😁💖🎶🎶🐱‍🏍\n\n\n1.JAMB Chemistry_year_1978\n2.JAMB Chemistry_year_1979\n3.JAMB Chemistry_year_1980")
while permission.upper()=="yes".upper():

    try:

        Year = input("Enter (1/2/3) or enter never mind to exit:".upper())
        if Year == "1":
            chemistry_year_1978()
            permission = input("Do you want to re-do it (yes/ Press any key to exit) :\n\n.".upper())
        elif Year == "2":
            chemistry_year_1979()
            permission = input("Do you want to re-do it (yes/ Press any key to exit) :\n\n".upper())
        elif Year == "3":
            chemistry_year_1980()
            permission = input("Do you want to re-do it (yes/ Press any key to exit) :\n\n".upper())
        elif Year.upper() == "never mind".upper():
            permission == "no"
            break

    except Exception:
        Year = input("You must enter your year of interest or enter never mind to exit::".upper())

