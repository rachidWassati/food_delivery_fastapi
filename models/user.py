from mongoengine import EmailField, StringField, BooleanField

class User:
    email= EmailField(required= True, max_length= 100, unique= True)
    password= StringField(required= True, min_length= 5)
    disabled= BooleanField(default= False)