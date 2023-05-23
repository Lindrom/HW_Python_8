import datetime

def get_birthdays_per_week(users):
    today = datetime.date.today()
    current_weekday = today.weekday()  # Получаем текущий день недели (0 - понедельник, 6 - воскресенье)
    
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    upcoming_weekdays = weekdays[current_weekday:] + weekdays[:current_weekday]  # Получаем список дней недели с учетом текущего дня
    
    for day in upcoming_weekdays:
        print(day + ':', end=' ')
        
        for user in users:
            birthday = user['birthday'].date()  # Извлекаем дату дня рождения из datetime объекта
            next_birthday = datetime.date(today.year, birthday.month, birthday.day)
            
            if next_birthday >= today:
                days_until_birthday = (next_birthday - today).days
            else:
                next_birthday = datetime.date(today.year + 1, birthday.month, birthday.day)
                days_until_birthday = (next_birthday - today).days
                
            if days_until_birthday < 7 and next_birthday.weekday() == weekdays.index(day):
                print(user['name'], end=', ')
                
        print()

# Пример использования функции
users = [
    {'name': 'Bill', 'birthday': datetime.datetime(2023, 5, 23)},
    {'name': 'Jill', 'birthday': datetime.datetime(2023, 5, 23)},
    {'name': 'Kim', 'birthday': datetime.datetime(2023, 5, 27)},
    {'name': 'Jan', 'birthday': datetime.datetime(2023, 5, 28)},
]

get_birthdays_per_week(users)