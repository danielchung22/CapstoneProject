
import subprocess
import sys

student_id = input("Enter your student id: ")
password = input("Enter your password: ")
query = input("Enter your query: ")
startyear = input("Enter start year: ")
endyear = input("Enter end year: ")

subprocess.call([sys.executable, 'userinput_final.py', student_id, password, query, startyear, endyear])
