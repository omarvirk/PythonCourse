import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

word = input("Enter Word: ")

cursor = con.cursor()
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
result = cursor.fetchall()
if result:
    for res in result:
        print (res)
else:
    temp_query = cursor.execute("SELECT * FROM Dictionary")
    temp_result = cursor.fetchall()
    it = iter(temp_result) 
    res_dict = dict(zip(it, it))
    print (res_dict.items())
    if len(get_close_matches(word, res_dict.keys() )) > 0:
        match = get_close_matches(word, res_dict.keys()[0])
        get_ans = ("Did you mean {}. If Yes please enter Y or press any key to exit. " .format(match) )
        if get_ans == 'Y':
            print (match)
    else:
        print("No word found")