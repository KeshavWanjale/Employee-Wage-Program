import random

class Employee:
    wage_per_ht = 20
    max_hours = 100
    max_days = 20
    
    def __init__(self):
        """Description:
            Initializes an Employee object with the total wage, total hours, and total days set to 0.
        """
        self.total_wage = 0
        self.total_hours = 0
        self.total_days = 0

    def check_attendence(self):
        """
        Description:
            Simulates the employee's attendance for the day.
        Parameters:
            None
        Returns:
            int: A random integer between 0 and 2, where 0 means absent, 
                 1 means full-time attendance, and 2 means part-time attendance.
        """
        return random.randint(0, 2)

    def cal_daily_wage(self):
        """
        Description:
            Calculates the daily wage based on the employee's attendance.
        Parameters:
            None
        Returns:
            tuple: A tuple containing the daily wage and the number of hours worked.
                   (wage, hours)
        """
        wage_per_hr = 20
        emp_attendance = self.check_attendence()
        match emp_attendance:
            case 1:
                return wage_per_hr * 8, 8
            case 2:
                return wage_per_hr * 4, 4
            case _:
                return 0,0

    def cal_monthly_wage(self):
        """
        Description:
            Calculates the total wage for the month based on the daily wage calculation.
        Parameters:
            None
        Returns:
            int: The total wage calculated for the employee over the month.
        """
        while self.total_hours < Employee.max_hours and self.total_days < Employee.max_days:
            
            daily_wage, hours_worked = self.cal_daily_wage()
            self.total_wage += daily_wage
            self.total_hours += hours_worked
            self.total_days += 1

        return self.total_wage 

if __name__ == "__main__":
    emp = Employee()
    monthly_wage = emp.cal_monthly_wage()
    print(f"Monthly wage of the employee is: {monthly_wage}")
