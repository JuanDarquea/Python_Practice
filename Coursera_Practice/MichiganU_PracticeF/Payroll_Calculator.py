# !/usr/bin/env python3
# encoding: utf-8
# Payroll_Calculator.py
try:
    hrs = input("Enter Hours:")
    h = float(hrs)
    rate = input("Enter hourly rate: ")
    r = float(rate)
except Exception as e:
    print(f"Error! - {e}", "\nPlease enter a numeric value\n")
    quit()

if h > 40:
    overtime = float(hrs) - 40
    overtime_rate = float(rate) * 1.5
    pay = (h - overtime) * r
    Opay = overtime * overtime_rate
    Tpay = pay + Opay
    print(Tpay)
#    print("Overtime worked:", overtime)
#    print("Overtime rate:", overtime_rate)
#    print("Salary:", pay)
#    print("Overtime paid:", Opay)
#    print("Total paid:", Tpay)
else:
    pay = (h * r)
    print("Total paid:", pay, "\n")