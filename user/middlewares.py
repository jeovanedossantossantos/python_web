
from django.conf import settings
import jwt

class Middlewares():

    def decode(token):
                
        if("Bearer" in token.get("Authorization")):

            des=jwt.decode(token.get("Authorization").split(' ')[1],settings.SECRET_KEY,algorithms=['HS256'])
        
        else:

            des = jwt.decode(token.get("Authorization"),settings.SECRET_KEY,algorithms=['HS256'])
			
        return des["user_id"]

           
