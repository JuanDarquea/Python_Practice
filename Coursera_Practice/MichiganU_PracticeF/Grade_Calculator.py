# !/usr/bin/env python3
# encoding: utf-8
# Grade_Calculator.py

try:
    score = float(input("Enter Score: "))
    if 0.0 < score < 1.1:
        if score < 0.6:
            print("F")
        elif 0.7 > score >= 0.6:
            print("D")
        elif 0.8 > score >= 0.7:
            print("C")
        elif 0.9 > score >= 0.8:
            print("B")
        elif score >= 0.9:
            print("A")
    else:
        print(f"Grade out of accepted range")
except Exception as e:
    print(f"Error! - {e}")