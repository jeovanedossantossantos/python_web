
from django.conf import settings
import jwt

class Middlewares():

    def decode(token):
       
        if("Bearer" in token.get("token")):
            
            des=jwt.decode(token.get("token").split(' ')[1],settings.SECRET_KEY,algorithms=['HS256'])
        
        else:

            des = jwt.decode(token.get("token"),settings.SECRET_KEY,algorithms=['HS256'])
			
        return des["user_id"]

           
