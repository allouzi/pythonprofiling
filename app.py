from flask import Flask
import os, time

app = Flask(__name__)
num = 1

def firstMethod():
    secondMethod() #Calling secondMethod
    return "I am done here"

def secondMethod():
    thirdMethod(2.5) #Calling thirdMethod 
    for loop in range(1): #CPU time spent
        for index in range(121474838):
            num * index
    thirdMethod(5) #Calling thirdMethod again

def thirdMethod(n):
    time.sleep(n) #Sleep

@app.route("/")
def home():  
    result = firstMethod()
    return "%s!" %result

if __name__ == '__main__':
    app.run()
