import mysql.connector 
   #Create the connection object 
myconn = mysql.connector.connect(host = "localhost", user = "root",  
    passwd = "") 
    
print(myconn)