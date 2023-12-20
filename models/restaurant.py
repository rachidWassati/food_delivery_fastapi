from mongoengine import Document, StringField, BooleanField, ListField, EmailField, FloatField

class Restaurant(Document):
    name= StringField(required= True, max_length= 100)
    ownerName= StringField(required= True, max_length= 100)
    foodTypes= ListField(StringField(), max_length=20, default= [])
    postalcode= StringField(required= True, max_length= 100)
    address= StringField(required= True, max_length= 100)
    phone= StringField(required= True, max_length= 100)
    email= EmailField(required= True, max_length= 100)
    password= StringField(required= True, min_length= 5)
    serviceAvailable= BooleanField(default= False)
    coverImages= ListField(StringField(), max_length=5, default= [])
    rating= FloatField(default= 0.0)