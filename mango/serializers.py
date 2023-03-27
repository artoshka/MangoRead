from rest_framework import serializers


from .models import Manga, Review, CustomUser, Genre, Type


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["id", "profile_img", "username", "nickname", ]


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Review
        fields = ["id", "user", "text", ]


class ReviewCreateSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=2000, required=True)
    manga_id = serializers.IntegerField()

    class Meta:
        model = Review
        fields = ["text", "manga_id"]

    def create(self, validated_data):
        return Review.objects.create(**validated_data)


class MangoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manga
        fields = ["id",  "name", "year", ]


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ["id", "name"]


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = ["id", "name"]


class MangoDetailSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    type = TypeSerializer()

    class Meta:
        model = Manga
        fields = ["id", "name", "year", "description", "genre", "type", ]