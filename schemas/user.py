from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    email: str = Field(default= None)
    password: str = Field(default= None)
    disabled: bool = Field(default= False)

    class Config:
        the_schema = {
            "user_demo" : {
                "email" : "rachid@gmail.com",
                "password": "qwerty",
                "disabled": False
            }
        }

class UserLoginSchema(BaseModel):
    email: str = Field(default= None)
    password: str = Field(default= None)

    class Config:
        the_schema = {
            "user_login_demo" : {
                "email" : "rachid@gmail.com",
                "password": "qwerty"
            }
        }