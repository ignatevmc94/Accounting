from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime, date, time
# from datetime import n

if __name__ == '__main__':
    print(calculate_salary(5, 4))
    print(get_employees())
    print(f"Время и дата сейчас - {datetime.now()}")
