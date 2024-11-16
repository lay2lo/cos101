print('WELCOME TO PHYSICS FORMULAR CLASS')


print('''here is the list of available formulas

1 power
2 average speed
3 electric current
4 work done
5 potential energy ''')

print('''
to learn power press A

to learn average speed press B

to learn electric current press C

to learn work done press D

to learn potential energy press E ''')


def calculate_power():
    work_done=int(input('enter your work done '))
    time_taken=int(input('enter your time taken '))
    power= work_done/time_taken
    print(power)





def calculate_average_speed():
    distance=int(input('enter your distance '))
    time=int(input('enter your time '))
    average_speed= distance/time
    print(average_speed)




def calculate_electric_current():
    quantity_of_charge=int(input('enter your quantity of charge '))
    time=int(input('enter your time '))
    electric_current=quantity_of_charge/time
    print(electric_current)


def calculate_work_done():
    force=int(input('enter your force '))
    distance=int(input('enter your distance '))
    work_done=force*distance
    print(work_done)




def calculate_potential_energy():
    mass=int(input('enter your mass '))
    acceleration_due_to_gravity=int(input('enter your acceleration due to gravity '))
    height=int(input('enter your height '))
    potential_energy=mass*acceleration_due_to_gravity*height
    print(potential_energy)



choice=(input('what will you like to learn '))

if choice== 'A' or choice== 'a':
   calculate_power()

elif choice== 'B' or choice== 'b':
    calculate_average_speed()

elif choice== 'C' or choice == 'c':
    calculate_electric_current()

elif choice== 'D' or choice == 'd':
    calculate_work_done()

elif choice== 'E'or choice== 'e':
    calculate_potential_energy()

else:
    print("invalid choice. please enter an alphabet between A to E")









