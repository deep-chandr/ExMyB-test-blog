from django.http import HttpResponse

from rest_framework import generics
from blog.models import Blogs, UserToken
from blog.utils import check_auth
from blogapplication.drf_utils import Response
from django.contrib.auth.models import User
from blog.serializers import BlogsSerializer
from django.contrib.auth import authenticate
import random 
import string
from rest_framework.decorators import api_view


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")




@api_view(('POST', ))
def login(request, *args, **kwargs):
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        return Response(msg= 'Incomplete data')
    
    user = authenticate(username=username, password=password)
    if user is not None:
        # A backend authenticated the credentials
        token = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
        token = UserToken.objects.create(user=user, token=token, is_valid=True)
        return Response(token.token, msg='Logged In')
    else:
        # No backend authenticated the credentials
        return Response(None, msg='Invalid credentials')


class Logout(generics.RetrieveUpdateAPIView):

    def put(self, request, *args, **kwargs):
        UserToken.objects.filter(user=request.user, is_valid=False)
        return Response(True)




class BlogsList(generics.ListCreateAPIView):
    queryset = Blogs.objects.all().order_by('-id')
    serializer_class = BlogsSerializer

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        is_superuser = user.is_superuser
        print('request.user: ', user)
        if is_superuser:
            # return all
            return Blogs.objects.all().order_by('-id')

        # return filtered
        return Blogs.objects.filter(author_id=user.id).order_by('-id')


    def get(self, request, *args, **kwargs):
        user = check_auth(request)
        if not user:
            return Response('Invalid Authorization')

        qs = self.get_queryset()
        return Response(BlogsSerializer(qs, many=True).data)




class BlogsDetail(generics.RetrieveUpdateAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializer

    def get_object(self):
        blog_id = self.kwargs['blog_id']
        return Blogs.objects.get(id=blog_id)


    def put(self, request, blog_id, *args, **kwargs):
        user = check_auth(request)
        if not user:
            return Response('Invalid Authorization. Login to continue')

        data = request.data
        blog = self.get_object()
        if 'like' in data:
            blog.liked_users.add(request.user)
            blog.save()

        return Response(BlogsSerializer(blog).data)


