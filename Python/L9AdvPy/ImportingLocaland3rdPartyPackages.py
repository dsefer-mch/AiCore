"""
part 1: 3rd party libraries install pandas using conda import pandas into your python script give pandas an alias "pd" upon importing from pandas, import the DataFrame class 
part 2: local imports create a folder called import_challenge and open it in vscode in the folder create 2 files called 'main.py' and 'utils.py' in the utils file, 
create a function called 'greeting' which prints a nice greeting in the utils file, call this function in the main file, import the greeting function from utils and run it notice 
how the function gets run twice? once when the file is imported, and once when we called it directly. 
To stop this, let's put the direct call in an if name equals main block (feel free to look it up if you forget the syntax) 

in this folder, create 2 folders called 'people' and 'sports' in the people folder, create a file with a variable in, that is a list of the names of your group members 
import this list into the main file and print it
 
inside the sports folder, create another 2 folders, called "skiing" and "climbing" in each of these, 

define a simple class which has an initialiser that prints the name of the sport and a method called equipment which prints a the name of the sport 
and a piece of equipment you need to do it try to import a module that does not exist, and handle this error with a try/except block
"""

import pandas as pd
from pandas import DataFrame
