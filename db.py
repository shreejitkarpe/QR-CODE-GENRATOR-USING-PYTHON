import mysql.connector
#step1=call connect() and create object of conect()=connection object x
x=mysql.connector.connect(host='localhost',
                        username='root',
                        password='shreejit6557',
                        database='qrcode_db')

if x:
    print("connection stablish successfully")
    
else:
    print("please try again ")  
#step2:create a cursor object=y   
y=x.cursor()   
#step3: execute sql query for creating a table
def create_table():   
    y.execute("create table if not exists qrinfo(person_name text,mobile_number text,Address text,course_name text,post_date date)")
def add_record(a,b,c,d,e) :  #there are 5 colums so 5 parameter  
    y.execute("insert into qrinfo(person_name,mobile_number,Address,course_name,post_date) \
              values(%s,%s,%s,%s,%s)" ,(a,b,c,d,e))
# step 4: commit()   
    x.commit() 
def view_all_records() :
    y.execute("select * from qrinfo") 
    data=y.fetchall()
    return data
def view_updade():
    y.execute("select distinct person_name from qrinfo") 
    data=y.fetchall()
    return data
def get_person(x):
    y.execute('select * from qrinfo where person_name="{}"'.format(x)) 
    data=y.fetchall()
    return data
def update(a,b,z,n):
    y.execute('update qrinfo set mobile_number=%s,course_name=%s,post_date=%s where person_name=%s'
                ,(a,b,z,n))
    x.commit()
    data=y.fetchall()
    return data
def delete(person) :
    y.execute('delete from qrinfo where person_name="{}"'.format(person))
    x.commit()
    
    
    
    
    
    
    