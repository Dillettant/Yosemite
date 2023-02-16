#!/usr/bin/env python3
import urllib.request
import json
import time

import tkinter as tk
from tkinter import messagebox

def create_alter(date):
    # Create a tkinter window object
    root = tk.Tk()

    # Hide the main window
    root.withdraw()

    # Show the alert message box
    messagebox.showinfo("Alert", "Found remaining tickets for {}.".format(date))

    # Exit the program
    root.destroy()

def get_remaining_ticket(date):
    url = "https://www.recreation.gov/api/timedentry/availability/facility/10086745?date={}".format(date)

    fp = urllib.request.urlopen(url)
    mybytes = fp.read()

    data = mybytes.decode("utf8")
    fp.close()

    data = data[1:-2]
    json_data = json.loads(data)
    
    threshold_tickets_remaining = json_data['booking_windows']['SECONDARY']['advanced_sales_details']['threshold_tickets_remaining']
    if threshold_tickets_remaining:
        create_alter(date)
    else:
        print("Remaining tickets {} for {}.".format(threshold_tickets_remaining, date))

while True:
    for date in ["2023-02-18", "2023-02-19"]:
        get_remaining_ticket(date)
    time.sleep(5)