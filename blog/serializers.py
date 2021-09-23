from rest_framework import serializers
from blog.models import Blogs



class BlogsSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Blogs
        fields = '__all__'

    def get_author(self, instance):
        return {
            'username': instance.author.username,
            'id': instance.author_id,
            'email': instance.author.email
        }


