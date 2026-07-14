# calculate Bonus
def calculate_bonus(base_salary, ratings):
    if ratings==5:
        bonus= base_salary*0.20
    elif ratings==4 or ratings ==3:
        bonus= base_salary*0.10
    elif ratings<3:
        bonus= 0
    return bonus

#calculate taxes based on salary and bonus
def calculate_tax(gross_salary):
    
    if gross_salary>7000:
        tax= gross_salary*0.15
    elif gross_salary>3000 and gross_salary<=7000:
        tax= gross_salary*0.10
    else:
        tax=0
    return tax

def main_hr_app():
    name=input("Enter the employee  name: ").strip().lower()
    department=input("Enter the employee department: ").strip().lower()
    if not name.replace(" ", "").isalpha() or not department.replace(" ", "").isalpha():
        print("Invalid input. Name and department must contain letters only.")
        return
    base_salary=float(input("Enter the employee base salary: "))
    ratings=int(input("Enter the employee performance rating (1-5): "))
    if (ratings<1 or ratings>5) or base_salary<=0:
        print("invalid input. Please enter valid values.")
        return #it will end the program and start over !
    
    # we here have 2 bugs if the user enters a rating less than 1 or greater than 5 or if the user enters a base salary less than or equal to 0, we will handle that with an if statement below
    # the other bug is that if the user didn't enter a string and entered a number instead .

    #.isalpha() is to make sure that the whole word is letters without numbers but there is a catch that if it detects a space it will return false so we will use .replace(" ", "")>>>>> that i new from AI to be honest.
    
    bonus=calculate_bonus(base_salary, ratings)
    gross_salary=bonus+base_salary
    tax=calculate_tax(gross_salary)
    net_salary= gross_salary-tax
    
    print("\n" + "="*40)
    print(f"📃 PAYROLL STATEMENT FOR : {name.upper()}")
    print("="*40)
    print(f"Base Salary: ${base_salary:.2f}")
    print(f"Bonus: ${bonus:.2f}")
    print(f"Gross Salary: ${gross_salary:.2f}")
    print(f"Tax: ${tax:.2f}")
    print("="*40)
    print(f"💰 NET PAYABLE CASH: ${net_salary:.2f}")
    print("="*40)

if __name__ == "__main__":
    main_hr_app()
