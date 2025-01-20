# -*- coding: utf-8 -*-
"""project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14zmPkLw_Yc2-zVuB7p0iK5XBnaG6G_3R
"""

import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import os

def create_csv(filename,headers,rows):
    with open(filename,mode='w',newline='')as file:
        writer=csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"csv file'{filename}'created successfully")
filename="Expense.csv"
headers=["category","amount","date"]
rows=[]

print("1.Log expense")
print("2.Analyze Data")
print("3.Visualization")
print("4.Exit")


def expense():
    category=input("Enter the category(Eg:Food,Travel):")
    amount=float(input("Enter the amount:"))
    date=(input("Enter the date(dd/mm/yyyy):"))
    row=[category,amount,date]
    rows.append(row)

def data():
    if not rows:
        print("No data to analyze. Please log some expenses first.")
        return
    create_csv(filename, headers, rows)
    df = pd.read_csv(filename)
    print("\n--- Expense Data ---")
    print(df)
    total_amount = df["amount"].sum()
    print("\nTotal amount spent:", total_amount)

def visual():
    d=pd.read_csv("Expense.csv")
    category = d.groupby("category")["amount"].sum()
    dateby=d.groupby("date")["amount"].sum()
    choice=input("Enter your preferred graph(1.By category 2.By date):")
    if choice == '1':
        x=np.array(category)
        plt.bar(category.index,category.values,label="Expense by category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.show()
    elif choice == '2':
        x=np.array(dateby)
        plt.plot(dateby.index,dateby.values,label="Expense by Date")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.show()
    else:
        print("Wrong choice!!!")
while(1):
    ch=int(input("Enter your choice:"))
    if ch==1:
        expense()
    elif ch==2:
        data()
    elif ch==3:
        visual()
    elif ch==4:
        print("Thank you!.... Good Bye")
        break
    else:
        print("Wrong choice! Please try again.")