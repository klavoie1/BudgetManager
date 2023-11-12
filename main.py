import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

# Setting up database
con = sqlite3.connect("budget.db")
cur = con.cursor()

cur.execute(
    """CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                description TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL
            )"""
)


con.commit()