def greet():
    print("hello world")

def greet(name):
    print(f"hello {name}")

def add(a,b):
    print(f"the sum = {a+b}")

def get_user_info():
    return "sumit",40,"shrestha"


def greet(name:str) -> str:
    return f"hello {name} "


def validate_user(name:str, age:int, email:str):
    if not name:
        return {'success':False,"error" : "Name is required"}
    if not 0 <= age <= 150:
        return {"success":False, 'error' :"Invalid age"}
    if '@' not in email:
        return{"success":False,"error":"Invalid email"}

    return {
        'success' :True,
        "user": {
            'name' :name,
            'age' : age,
            'email' : email 
        }
    }

result = validate_user("sumit",30,"sumit@gmail.com")
if result['success']:
    print(result['user'])