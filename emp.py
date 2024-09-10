import random
def check_attendence():
    attendence = random.randint(0,2)
    return attendence

def cal_daily_wage():
    wage_per_hr = 20
    emp_attendance = check_attendence()
    # returning tuples daily_wage, hours worked
    match emp_attendance:
        case 1:
            return wage_per_hr * 8, 8
        case 2:
            return wage_per_hr * 4, 4
        case _:
            return 0,0

def cal_monthly_wage():
    total_wage = 0
    total_hours = 0
    total_days = 0
    max_hours = 100
    max_days = 20
    
    while total_hours < max_hours and total_days < max_days:
        #getting the tuples daily_wage, hours_worked
        daily_wage, hours_worked = cal_daily_wage()
        total_wage += daily_wage
        total_hours += hours_worked
        total_days += 1
    
    return total_wage #, total_hours,total_days

if __name__  == "__main__":
    print("Welcome to Employee Wage Program")
    print(f"Monthly wage of the employee is: {cal_monthly_wage()}")
