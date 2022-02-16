from rest_framework import fields, serializers
from django.shortcuts import get_object_or_404

from .models import Contact, Deceased, DeceasedGallery, CondolenceNotes


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('firstname', 'lastname', 'email', 'phone', 'subject', 'message')

    def get_photo_url(self, deceased):
        request = self.context.get('request')
        photo_url = deceased.photo.url
        return request.build_absolute_uri(photo_url)

class DeceasedGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeceasedGallery
        exclude = ('id', 'deceasedid')

    def get_images_url(self, deceasedid):
        request = self.context.get('request')
        images_url = deceasedid.image.url
        return request.build_absolute_uri(images_url)

    def get_photo_url(self, deceased):
        request = self.context.get('request')
        photo_url = deceased.photo.url
        return request.build_absolute_uri(photo_url)

class CondolenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = CondolenceNotes
        fields = ( '__all__')
    

class DeceasedSerializer(serializers.ModelSerializer):
    condolences = serializers.StringRelatedField(many=True)
    image_gallery = serializers.StringRelatedField(many=True)
    class Meta:
        model = Deceased
        fields = ('__all__')
















    
    # def create(self, validated_data):
    #     condolences_notes = validated_data.filter(condolences='condolences')
    #     deceased = Deceased.objects.create(**validated_data)
    #     for note in condolences_notes:
    #         CondolenceNotes.objects.create(deceased='deceased', **note)
    #     return deceased
