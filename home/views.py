from django.shortcuts import render
from django.contrib.auth.models import  User
from rest_framework import viewsets,permissions
from .selializers import *
from .models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
# token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
# Create your views here.

class userView(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSeliarizer
    permissions_class=[permissions.IsAuthenticated]

class languageView(viewsets.ModelViewSet):
    queryset=Languages.objects.all()
    serializer_class=LangSeliarizer
    # permissions_class=[permissions.IsAuthenticated]
    
class climateView(viewsets.ModelViewSet):
    queryset=Climate.objects.all()
    serializer_class=ClimatSeliarizer
    permissions_class=[permissions.IsAuthenticated]



class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
      serializer = self.serializer_class(data=request.data,context={'request': request})
      serializer.is_valid(raise_exception=True)
      user = serializer.validated_data['user']
      # auth.login(request,user)
      print(user)
      token, created = Token.objects.get_or_create(user=user)

      return Response({
      'token': token.key,
      'user_id': user.pk,
      'email': user.email,
      'username':user.username,
      'first_name':user.first_name,
      'last_name':user.last_name
      })



@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def taskList(request):
    acount=request.user
    print(acount)
    taskss= Languages.objects.all().order_by('-id')
    serializer =LangSeliarizer(taskss, many=True)

    return Response(serializer.data)