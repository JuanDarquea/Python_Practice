# !/usr/bin/env python3
# encoding: utf-8
# Payroll_Calculator.py

def computepay(h, r):
    if h > 40:
        overtime = h - 40
        overtime_rate = r * 1.5
        pay = (h - overtime) * r
        Opay = overtime * overtime_rate
        Tpay = pay + Opay
        print("Pay:", Tpay, "\n")
    #    print("Overtime worked:", overtime)
    #    print("Overtime rate:", overtime_rate)
    #    print("Salary:", pay)
    #    print("Overtime paid:", Opay)
    #    print("Total paid:", Tpay)
    else:
        pay = (h * r)
        print("Total paid:", pay, "\n")

try:
    hrs = input("Enter Hours:")
    h = float(hrs)
    rate = input("Enter hourly rate: ")
    r = float(rate)
except Exception as e:
    print(f"Error! - {e}", "\nPlease enter a numeric value\n")
    quit()

computepay(h, r)