import mysql.connector

def DataUpdate(AgencyID,Password):
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="onyxdatabase"
        )
    
    mycursor=mydb.cursor()
    
    sql="select password from agency_user_table where agency_id=AgencyID"
    
    pwd=mycursor.execute(sql)
    
    if (pwd==Password):
        print("Login successful.")
    else:
        print("Login unsuccessful.")
                                                  