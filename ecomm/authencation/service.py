from .models import Signup
from django.db.models import Q

def validate_password(password, confirmpassword):
    if password == confirmpassword:
        return True
    else:
        return False
    
def user_validtion(email,password):
    obj = Signup.objects.filter(Q(email=email) & Q(password = password)).values()
    print(obj)
    if len(obj)==0:
        return False
    else:
        return True
