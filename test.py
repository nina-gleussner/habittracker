import sqlite3


# test if longest_streak is always bigger than the current streak
def test1():
    conn = sqlite3.connect('habittracker.db')
    c = conn.cursor()
    c.execute("SELECT streak FROM habits")
    new_streak = c.fetchall()
    c.execute("SELECT longest_streak FROM habits")
    longest_streak = c.fetchall()
    conn.commit()
    conn.close()
    # the following where test to see if the code works
    # for i in new_streak:
        # print(i)
    # for i in longest_streak:
        #print(i)
    list1 = [i[0] for i in new_streak]
    list2 = [i[0] for i in longest_streak]
    # the following where test to see if the code works
    # print(list1)
    # print(list2)
    # for i, n in zip(list1, list2):
        # print(i, "<=", n)
    for i, n in zip(list1, list2):
        assert i <= n
