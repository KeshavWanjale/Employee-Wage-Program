import random
def check_attendence():
    attendence = random.randint(0,2)
    return attendence

def cal_daily_wage():
    wage_per_hr = 20
    emp_attendance = check_attendence()
    match emp_attendance:
        case 1:
            daily_wage = wage_per_hr * 8
            print(f"Employee was present full day so his daily wage is : {daily_wage}")
        case 2:
            daily_wage = wage_per_hr * 4
            print(f"Employee was present half day so his daily wage is : {daily_wage}")
        case _:
            daily_wage = 0
            print(f"Employee was absent for the day so his daily wage is : {daily_wage}")

if __name__  == "__main__":
    print("Welcome to Employee Wage Program")
    cal_daily_wage()
