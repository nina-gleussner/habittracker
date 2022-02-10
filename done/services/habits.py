from datetime import date
from datetime import datetime
import sqlite3


class Habit:
    def __init__(self, name, periodicity, start_date=date.today(),
                 last_checked=date.today(), streak=1, longest_streak=1):
        self.name = name
        # periodicity has to be a number
        self.periodicity = int(periodicity)
        self.start_date = start_date
        self.last_checked = last_checked
        # streak has to be a number
        self.streak = int(streak)
        # longest streak has to be a number
        self.longest_streak = int(longest_streak)
        # save habits automaticly into the database with the save_habit function
        self.save_habit(self.name, self.periodicity, self.start_date,
                        self.last_checked, self.streak, self.longest_streak)

    # save habit in database
    def save_habit(self, name, periodicity, start_date,
                   last_checked, streak, longest_streak):
        conn = sqlite3.connect('habittracker.db')
        c = conn.cursor()
        c.execute("INSERT OR IGNORE INTO habits VALUES (?,?,?,?,?,?)",
                  (self.name, self.periodicity, self.start_date,
                   self.last_checked, self.streak, self.longest_streak))
        conn.commit()
        conn.close()


# check habits as done and updates records
def check_habit(name):
    conn = sqlite3.connect('habittracker.db')
    c = conn.cursor()
    c.execute("SELECT periodicity FROM habits WHERE name =:s", {"s": name})
    periodicity = c.fetchone()
    periodicity = periodicity[0]
    c.execute("SELECT last_checked FROM habits WHERE name=:s", {"s": name})
    last_checked = c.fetchone()
    last_checked = last_checked[0]
    datetime_object = datetime.strptime(last_checked, '%Y-%m-%d')
    today = datetime.today()
    # how many days have passed since the last check
    t = today - datetime_object
    d = t.days
    # tests if you check your habits already
    if d == 0:
        print(f"You already checked of {name} today")
    else:
        if d > periodicity:
            # updating the database
            # streak begins again at 1 since the the check-off was to late
            c.execute("UPDATE habits SET last_checked =:d, streak = 1 WHERE name =:s",
                      {"d": date.today(), "s": name})
        else:
            # updating the database if you were in time
            c.execute("UPDATE habits SET last_checked =:d, streak = streak + 1 WHERE name =:s",
                      {"d": date.today(), "s": name})
            c.execute("SELECT streak FROM habits WHERE name=:s", {"s": name})
            new_streak = c.fetchone()
            new_streak = new_streak[0]
            c.execute("SELECT longest_streak FROM habits WHERE name=:s", {"s": name})
            longest_streak = c.fetchone()
            longest_streak = longest_streak[0]
            # updating the longest streak if current streak is longer
            if new_streak > longest_streak:
                c.execute("UPDATE habits SET longest_streak =:t WHERE name=:s",
                          {"t": new_streak}, {"s": name})

    conn.commit()
    conn.close()


# delete an existing habit from the database
def delete_habit(name):
    conn = sqlite3.connect('habittracker.db')
    c = conn.cursor()
    c.execute("DELETE from habits WHERE name =:s", {"s": name})
    print(f"You deleted {name} succesfully")
    conn.commit()
    conn.close()
