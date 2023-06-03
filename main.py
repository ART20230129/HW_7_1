from application import salary
from application.db import people
from datetime import date

def main():
    print(date.today())
    salary.calculate_salary()
    people.get_employees()


if __name__ == '__main__':
    main()

