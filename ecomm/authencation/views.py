from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SignupSerializer
from .service import validate_password, user_validtion

class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data)
        flag = validate_password(serializer.data.get('password'),serializer.data.get('confirm_password'))
        if flag==True:
            serializer.save()
            return Response({"status":200, "error":False, "message":"Data saved successfully"})
        else:
            return Response({"status":400, "error":True, "message":"Password and confirm password is not same"})


class LoginView(APIView):
    # get data from user  email password
    # check that user email and password exist in our db
    # if exist -->login
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        flag = user_validtion(email,password)
        if flag==True:
            return Response({"status":200, "error": False, "message":"logged in succesfully"})
        else:
            return Response({"status":404, "error": True, "message":"User is not valid"})

