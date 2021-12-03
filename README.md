# habittracker
Small habittracker app. Used through the command line

Setup a virtual enviroment with (pip install virtualenv) virtualenv venv 
And activate it .\venv\Scripts\activate
Install the setup.py with: pip install .
to setup the database run the database.py script and afterwards you can load in example data by running the exampledata.py script
call the habittracker with the command done
afterwards it should look like this:

![image](https://user-images.githubusercontent.com/93149648/144574513-0dd2c90e-bf05-4c5e-a513-351bed281ee5.png)


returnhabits() > returns all habits 

longeststreak(name) > returns the longest streak of a specific habit

returnstreak(name) > returns the current streak of a specific habit

sameperiodicity(periodicity) > returns all habits with the named periodicity

delete(name) > deletes a specific habit

check(name) > checks a specific habit

newhabit(name, periodicity) > creates a new habit



