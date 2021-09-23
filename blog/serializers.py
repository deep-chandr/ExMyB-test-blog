from rest_framework import serializers
from blog.models import Blogs



class BlogsSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    liked_users_data=serializers.SerializerMethodField()

    class Meta:
        model = Blogs
        fields = '__all__'

    def get_author(self, instance):
        return {
            'username': instance.author.username,
            'id': instance.author_id,
            'email': instance.author.email
        }

    def get_liked_users_data(self, instance):
        liked_user = []
        for user in instance.liked_users.all():
            liked_user.append({
                'username': user.username,
                'email': user.email,
                'id': user.id
            })
        return liked_user



