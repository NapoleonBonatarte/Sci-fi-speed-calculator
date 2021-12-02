###
# Author: Tyler Windemuth
# description: This is a simple calculator that allows someone to enter in
#              an initial velocity, acceleration(average) and time. This program
#              will then tell the user how fast the object is travelling in the by the
#              end of the allotted period.

def period_calculator(period):
    '''
    Mainly sorts user input into a computer readable format
    :param period: string that the user entered for time.
    :return: total number of seconds of acceleration.
    '''
    final_period = 0
    years = 0
    months = 0
    days = 0
    hours = 0
    minute = 0
    seconds = 0
    temp = ''
    for i in period:
        temp += i
        if i.lower() == 'y':
            years = temp.split('y')
            years = years[0][0:len(years[0])]
            years = float(years) * 31536000
            temp = ''
        elif i.lower() == 'm':
            months = temp.split('m')
            months = months[0][0:len(months[0])]
            months = float(months) * 2628288
            temp = ''
        elif i.lower() == 'd':
            days = temp.split('d')
            days = days[0][0:len(days[0])]
            days = float(days) * 86400
            temp = ''
        elif i.lower() == 'h':
            hours = temp.split('h')
            hours = hours[0][0:len(hours[0])]
            hours = float(hours) * 3600
            temp = ''
        else:
            try:
                seconds = int(period)
            except:
                print(end='')
    final_period = (years + months + days + hours + minute + seconds)
    return final_period


def distance_calculator(initial_speed, final_acceleration, final_period):
    distance = initial_speed * final_period + ((final_acceleration * final_period)**2)/2
    return distance  # value in meters





def main():
    initial_speed = float(input('Enter initial speed in m/s:\n'))
    acceleration = input('Enter acceleration in m/s (or use g, Ie: 10g):\n')
    period = input('Enter time accelerating(years:y, months: mo, days: d,'
                   ' hours: h, (seconds are blank):\n')
    final_acceleration = 0
    final_period = period_calculator(period)
    acceleration = acceleration.split(' ')
    for i in acceleration:  # determines if user is using m/s or Gs as measurement.
        if i[len(i)-1].lower() == 'g':
            final_acceleration = i[0:len(i)-1]
            final_acceleration = float(final_acceleration) * 9.80665
        else:
            final_acceleration = int(i)




    ending_speed = initial_speed + (final_acceleration * final_period)
    g_force = final_acceleration / 9.80665

    # output
    print(f'\nEnd Speed: {ending_speed} m/s')
    print(f'End Speed: {ending_speed * 2.237} mph')
    print(f'End Speed: {ending_speed * 3.6} kph\n')
    print(f'Speed in percentage of speed of light: {round((ending_speed / 299792458)*100,4)}%')
    print(f'{round((ending_speed / 299792458),2)} times the speed of light\n')
    print(f'G-force: {g_force}')
    if input('\nWould you like to find distance travelled? (y/n)').lower() == 'y':
        distance = distance_calculator(initial_speed, final_acceleration, final_period)
        print(f'\nKilometers travelled: {distance/10000}')
        print(f'Miles traveled: {distance/16090}')
        print(f'AU travelled: {distance/1496000000000}')
        print(f'Light years travelled: {distance/94610000000000000}')
    if input('\nEnter Q to quit').lower() == 'q':
        exit('Have a nice day!')


main()
