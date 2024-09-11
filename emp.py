import random

class Employee:
    
    def __init__(self):
        """
        Description:
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

    def cal_daily_wage(self,wage_per_hour):
        """
        Description:
            Calculates the daily wage based on the employee's attendance.
        Parameters:
            None
        Returns:
            tuple: A tuple containing the daily wage and the number of hours worked.
                   (wage, hours)
        """
        emp_attendance = self.check_attendence()
        match emp_attendance:
            case 1:
                return wage_per_hour * 8, 8
            case 2:
                return wage_per_hour * 4, 4
            case _:
                return 0,0
    
    def cal_monthly_wage(self, wage_per_hour, max_hours, max_days):
        """
        Description:
            Calculates the total wage for the month based on the daily wage calculation.
        Parameters:
            None
        Returns:
            int: The total wage calculated for the employee over the month.
        """
        while self.total_hours < max_hours and self.total_days < max_days:
            
            daily_wage, hours_worked = self.cal_daily_wage(wage_per_hour)
            self.total_wage += daily_wage
            self.total_hours += hours_worked
            self.total_days += 1

        return self.total_wage 
            
class Company:
    def __init__(self, name, wage_per_hour, max_hours, max_days):
        """
        Description:
            Initializes a Company object with the company's name, wage per hour, maximum hours,
            and maximum days for an employee to work.
        Parameters:
            name: The name of the company.
            wage_per_hour: The wage per hour for employees.
            max_hours: The maximum number of hours an employee can work in a month.
            max_days: The maximum number of days an employee can work in a month.
        """
        self.name = name
        self.wage_per_hour = wage_per_hour
        self.max_hours = max_hours
        self.max_days = max_days
        self.employee = Employee()

    def calculate_employee_wage(self):
        """
        Description
            Calculates the employee's total wage for the month using the company's wage per hour,
            maximum hours, and maximum days.
        Returns:
            int: The total monthly wage of the employee.
        """
        return self.employee.cal_monthly_wage(self.wage_per_hour, self.max_hours, self.max_days)


if __name__ == "__main__":

    companies = [
        Company("Company1", 20, 100, 20),
        Company("Company2", 25, 110, 21),
        Company("Company3", 30, 120, 22)
    ]
    
    for company in companies:
        monthly_wage = company.calculate_employee_wage()
        print(f"Monthly wage for an employee in {company.name} is: {monthly_wage}")
