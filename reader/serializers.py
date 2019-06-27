from .models import User, Passage, Album, Collect
from rest_framework import serializers

# 名字随意
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # 对应类名
        model = User
        # 各个字段，其中_id是默认id字段
        fields = ('ID', 'Password', 'Plan')
class PassageSerializer(serializers.ModelSerializer):
    class Meta:
        # 对应类名
        model = Passage
        # 各个字段，其中_id是默认id字段
        fields = ('Name', 'Econtent', 'Ccontent','From')
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        # 对应类名
        model = Album

        # 各个字段，其中_id是默认id字段
        fields = ('Name', 'Pnum','Img')
class CollectSerializer(serializers.ModelSerializer):
    class Meta:
        # 对应类名
        model = Collect

        # 各个字段，其中_id是默认id字段
        #Pname是专辑名字
        fields = ('ID', 'Pname')