from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import PostSerializer
from .models import Post
from .permissions import IsAuthOrReadOnly

# Create your views here.
# for the GET, POST
class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
