# from rest_framework import serializers
# from .models import Chat, Post

# class PostSerializer(serializers.ModelSerializer):

#     def create(self, data):
#         post = Post(**data)
#         post.save()
#         return post
#     class Meta:
#         model = Post
#         fields = ('id', 'language', 'text', 'created_at')

# class ChatSerializer(serializers.ModelSerializer):

#     def create(self, data):
#         chat = Chat(**data)
#         chat.save()
#         return chat
#     class Meta:
#         model = Chat
#         fields = ('id', 'name', 'created_at')
