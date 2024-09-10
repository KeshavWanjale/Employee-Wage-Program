import random
def check_attendence():
    attendence = random.randint(0,2)
    return attendence

def cal_daily_wage():
    wage_per_hr = 20
    emp_attendance = check_attendence()
    match emp_attendance:
        case 1:
            return wage_per_hr * 8
        case 2:
            return wage_per_hr * 4
        case _:
            return 0

def cal_monthly_wage():
    total_wage = 0
    tota_days = 20
    for i in range(tota_days):
        total_wage += cal_daily_wage()
    return total_wage

if __name__  == "__main__":
    print("Welcome to Employee Wage Program")
    print(f"Monthly wage of the employee is: {cal_monthly_wage()}")
