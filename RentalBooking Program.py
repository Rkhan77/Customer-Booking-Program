from statistics import mean

import numpy as np

def verifyinput(prompt, display_error, datatype):
    global numinput
    while True:
        response = input(prompt)
        try:
            if datatype == int:
                numinput = int(response)
        except ValueError:
            print(display_error)
            continue
        return numinput



def verifynums(prompt, display_error='Error! Please try again (NUMBERS ONLY!)'):
    return verifyinput(prompt, display_error, int)



def inputstr(prompt):
    while True:
        name = input(prompt)
        if name.strip().isdigit():
            print('Please input letters (A-Z) only!.')
        else:
            return name



def summeryh(prompt):
    print(prompt.center(50))



def heading(prompt):
    wlcmsg = prompt
    print("#" * 50)
    print('#' + wlcmsg.center(48) + '#')
    print('#' * 50)



cus_nfo = []
lic_nfo = []
hired_days = []
rental_paid = []

heading("Rental/Booking Program")

COUNTER = 3
for i in range(COUNTER):

    cusname = inputstr('Enter Customer first name and last name: ')
    cus_nfo.append(cusname)
    np.save('names', cus_nfo)
    licno = input('Enter the licence number for ' + cusname.title() + ': ')
    lic_nfo.append(licno)
    np.save('license', lic_nfo)
    no_days = verifynums('Enter the number of days hire for {}: '.format(cusname.capitalize()))
    hired_days.append(no_days)
    np.save('days', hired_days)

    D_RATE = 34.50
    RATE1 = 30.50
    RATE2 = 22.50
    rental = 0

    if no_days <= 3:
        cal1 = D_RATE * no_days
        rental += cal1

    if no_days > 3 and no_days <= 7:
        cal2 = 3 * D_RATE + (no_days - 3) * RATE1
        rental += cal2

    if no_days > 7:
        cal3 = 3 * D_RATE + 4 * RATE1 + (no_days - 7) * RATE2
        rental += cal3

    rental_paid.append(rental)
    np.save('rental', rental_paid)
    print('\n')

    heading('Summary of Hire')
    print("Customer name: ", cusname.title())
    print("Licence Number: {} {} {}".format(licno[0:3], licno[3:6], licno[6:9]))
    drate = "{:.2f}".format(no_days)
    print('Number of days: {} days '.format(drate))
    frate = "{:.2f}".format(rental)
    print('The Rental is ${} AUD'.format(frate), '\n')

heading('Statistics of Hire Activities' '\n')
summeryh('-----------------------')
bit_range = hired_days.count(4)
print('number of hire days less then 4 days: ', bit_range)
mid_range = [i for i in hired_days if i > 3 and i < 7]
cnt_midrange = len(mid_range)
print('Number of day hired between 4 to 7 days: ', cnt_midrange)
hi_range = [i for i in hired_days if i > 7]
cnt_hirange = len(hi_range)
print('number of days hired more than 7 days: ', cnt_hirange, '\n')
avg_days = mean(hired_days)
f_days = "{:.2f}".format(round(avg_days, 2))
print('the average hired days is {} days'.format(f_days))
f_sum = "{:.2f}".format(sum(rental_paid))
print('the total rental received is ${} AUD '.format(f_sum))
heading('TASKS COMPLETED')
