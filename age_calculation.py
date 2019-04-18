import datetime


def calc():
    print("Please, enter your birth year.")
    return datetime.date.year - int(input())
