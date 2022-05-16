from datetime import datetime, timedelta, date
from collections import defaultdict
from typing import Any

users = [{'name': 'Alex', 'birthday': datetime(year=1986, month=5, day=24)},
         {'name': 'Yulia', 'birthday': datetime(year=1986, month=5, day=22)},
         {'name': 'Martin', 'birthday': datetime(year=2012, month=5, day=19)},
         {'name': 'Amelia', 'birthday': datetime(year=2015, month=5, day=21)}]


def get_birthdays_per_week(list_of_bd):
    # find the date of the next Saturday, if generated in any workday of the week
    if date.today().weekday() >= 5:
        print ('Birthday list for the next week can be generated Monday to Friday only.')
    else:
        next_saturday = date.today() + timedelta(days=(5 - date.today().weekday()))

        # find the month/days for which the birthdays should be checked for the next week's BD calendar
        next_sat = next_saturday.strftime('%m%d')
        next_sun = (next_saturday + timedelta(days=1)).strftime('%m%d')
        next_mon = (next_saturday + timedelta(days=2)).strftime('%m%d')
        next_tue = (next_saturday + timedelta(days=3)).strftime('%m%d')
        next_wed = (next_saturday + timedelta(days=4)).strftime('%m%d')
        next_thu = (next_saturday + timedelta(days=5)).strftime('%m%d')
        next_fri = (next_saturday + timedelta(days=6)).strftime('%m%d')

        birthdays_per_week: defaultdict[Any, list] = defaultdict(list)
        for user in list_of_bd:
            # Compare the next week's birthday calendar (above)
            # to the actual birthdays of the people and sort by the days when the BD will be celebrated
            user_bd = user['birthday'].strftime('%m%d')
            if user_bd == next_sat or user_bd == next_sun or user_bd == next_mon:
                birthdays_per_week['Monday'].append(user['name'])
            elif user_bd == next_tue:
                birthdays_per_week['Tuesday'].append(user['name'])
            elif user_bd == next_wed:
                birthdays_per_week['Wednesday'].append(user['name'])
            elif user_bd == next_thu:
                birthdays_per_week['Thursday'].append(user['name'])
            elif user_bd == next_fri:
                birthdays_per_week['Friday'].append(user['name'])
            else:
                continue
        # sort the dictionary by the days of the week
        sorted_birthdays_per_week = {key: value for key, value in sorted(birthdays_per_week.items())}

        # formats the dictionary to nice looking strings.
        # But how to end this function with the return statement instead of print?
        for k, v in sorted_birthdays_per_week.items():
            print (k + ': ' + ','.join(v))


get_birthdays_per_week(users)
