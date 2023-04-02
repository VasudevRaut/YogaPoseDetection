import pyrebase


def getDBObject():
    firebaseConfig = {'apiKey': "AIzaSyA8enqQTw77zGhE9eP8PxgAuvAjSFjkd7c",
      'authDomain': "yoga-c7c88.firebaseapp.com",
      'databaseURL': "https://yoga-c7c88-default-rtdb.firebaseio.com/users",
      'projectId': "yoga-c7c88",
      'storageBucket': "yoga-c7c88.appspot.com",
      'messagingSenderId': "98729005967",
      'appId': "1:98729005967:web:3118d05e9f111d5762b1fa",
      'measurementId': "G-CBRKZMJ879"
        

        }
    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    
    return db


def retrivePass(username):
    firebaseConfig = {'apiKey': "AIzaSyA8enqQTw77zGhE9eP8PxgAuvAjSFjkd7c",
      'authDomain': "yoga-c7c88.firebaseapp.com",
      'databaseURL': "https://yoga-c7c88-default-rtdb.firebaseio.com",
      'projectId': "yoga-c7c88",
      'storageBucket': "yoga-c7c88.appspot.com",
      'messagingSenderId': "98729005967",
      'appId': "1:98729005967:web:3118d05e9f111d5762b1fa",
      'measurementId': "G-CBRKZMJ879"
        

        }
    firebase = pyrebase.initialize_app(firebaseConfig)
    password=''
    db = firebase.database()
    try:
        people = db.child('users').child(username).get()
        
        for i in people.each():
            if(i.key()=='Password'):
                password=i.val()

    except:
        print("UserName not found")
        return "UserName not found"
        
                
    
    return password





def retrivePinfo(username):
    firebaseConfig = {'apiKey': "AIzaSyA8enqQTw77zGhE9eP8PxgAuvAjSFjkd7c",
      'authDomain': "yoga-c7c88.firebaseapp.com",
      'databaseURL': "https://yoga-c7c88-default-rtdb.firebaseio.com",
      'projectId': "yoga-c7c88",
      'storageBucket': "yoga-c7c88.appspot.com",
      'messagingSenderId': "98729005967",
      'appId': "1:98729005967:web:3118d05e9f111d5762b1fa",
      'measurementId': "G-CBRKZMJ879"
        

        }
    ls = []
    firebase = pyrebase.initialize_app(firebaseConfig)
    password=''
    db = firebase.database()
    try:
        people = db.child('users').child(username).get()
        
        for i in people.each():
            ls.append(i.val())

    except:
        print("UserName not found")
        
                
    
    return ls







#------------------------------------------------------------------



def getDBObject2():
    firebaseConfig = {'apiKey': "AIzaSyA8enqQTw77zGhE9eP8PxgAuvAjSFjkd7c",
      'authDomain': "yoga-c7c88.firebaseapp.com",
      'databaseURL': "https://yoga-c7c88-default-rtdb.firebaseio.com/health",
      'projectId': "yoga-c7c88",
      'storageBucket': "yoga-c7c88.appspot.com",
      'messagingSenderId': "98729005967",
      'appId': "1:98729005967:web:3118d05e9f111d5762b1fa",
      'measurementId': "G-CBRKZMJ879"
        

        }
    firebase = pyrebase.initialize_app(firebaseConfig)

    db = firebase.database()
    
    return db







def retriveHealthCounter(uname):
    import datetime
    date1 = datetime.date.today().strftime('%d-%m-%y')
    firebaseConfig = {'apiKey': "AIzaSyA8enqQTw77zGhE9eP8PxgAuvAjSFjkd7c",
      'authDomain': "yoga-c7c88.firebaseapp.com",
      'databaseURL': "https://yoga-c7c88-default-rtdb.firebaseio.com",
      'projectId': "yoga-c7c88",
      'storageBucket': "yoga-c7c88.appspot.com",
      'messagingSenderId': "98729005967",
      'appId': "1:98729005967:web:3118d05e9f111d5762b1fa",
      'measurementId': "G-CBRKZMJ879"
        

        }
    
    firebase = pyrebase.initialize_app(firebaseConfig)
    
    db = firebase.database()
    counter=1
    try:
        people = db.child('health').child(uname).child(date1).get()
        
        for i in people.each():
            counter = counter+1
            

    except:
        print("UserName not found")

    print(counter)
       
        
                
    
    return counter



#-------------------------------------------------------------------------------------------------------
def retriveMobileNOIsPresent(mob):
    firebaseConfig = {'apiKey': "AIzaSyA8enqQTw77zGhE9eP8PxgAuvAjSFjkd7c",
      'authDomain': "yoga-c7c88.firebaseapp.com",
      'databaseURL': "https://yoga-c7c88-default-rtdb.firebaseio.com",
      'projectId': "yoga-c7c88",
      'storageBucket': "yoga-c7c88.appspot.com",
      'messagingSenderId': "98729005967",
      'appId': "1:98729005967:web:3118d05e9f111d5762b1fa",
      'measurementId': "G-CBRKZMJ879"
        

        }
    firebase = pyrebase.initialize_app(firebaseConfig)
    contact=''
    db = firebase.database()
    try:
        people = db.child('users').get()
        #print(people.each())
        
        for i in people.each():
            #print(i.key())
            people1 = db.child('users').child(i.key()).get()
            for j in people1.each():
                #print(j.key())
                if(j.key()=='Contact'):
                    
                    contact=j.val()
                    #print(i.key())
                    #print(contact)
                    return True

        

    except:
        
        return False
        
                
    
    return False

#----------------------------------------------------------------------------
def retriveUserName(mob):
    firebaseConfig = {'apiKey': "AIzaSyA8enqQTw77zGhE9eP8PxgAuvAjSFjkd7c",
      'authDomain': "yoga-c7c88.firebaseapp.com",
      'databaseURL': "https://yoga-c7c88-default-rtdb.firebaseio.com",
      'projectId': "yoga-c7c88",
      'storageBucket': "yoga-c7c88.appspot.com",
      'messagingSenderId': "98729005967",
      'appId': "1:98729005967:web:3118d05e9f111d5762b1fa",
      'measurementId': "G-CBRKZMJ879"
        

        }
    firebase = pyrebase.initialize_app(firebaseConfig)
    contact=''
    db = firebase.database()
    try:
        people = db.child('users').get()
        #print(people.each())
        
        for i in people.each():
            #print(i.key())
            
            people1 = db.child('users').child(i.key()).get()
            for j in people1.each():
                #print(j.key())
                if(j.key()=='Contact'):
                    
                    if mob==j.val():
                        #print(i.key())
                        #print(contact)
                        return i.key()

            
        

    except:
        
        pass
        
                
    
    


#print(retriveUserName('7387579912'))


#retriveMobileNOIsPresent("7387579912")



