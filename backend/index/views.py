from django.shortcuts import render
from django.http import Http404, request
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status 

from .serializers import ContactSerializer, DeceasedSerializer, DeceasedGallerySerializer, CondolenceSerializer
from .models import Contact, Deceased, DeceasedGallery, CondolenceNotes



# Create your views here.
class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class DeceasedList(APIView):
    def get(self, request, format=None):
        deceased_people = Deceased.objects.all()
        serializer = DeceasedSerializer(deceased_people, many=True, context={"request": request})
        return Response(serializer.data)


class DeceasedDetailView(APIView):
    def get_object(self, request, deceasedid, format=None):
        try:
            return Deceased.objects.get(deceasedid=deceasedid)
        except Deceased.DoesNotExist:
            raise Http404


    def get(self, request, deceasedid, format=None):
        deceased_person = self.get_object(request, deceasedid=deceasedid)
        serializer = DeceasedSerializer(deceased_person, context={"request": request})
        return Response(serializer.data)

class DeceasedGalleryList(APIView):

    def get(self, request, deceasedid):
        memories =DeceasedGallery.objects.filter(deceasedid=deceasedid)
        serializer = DeceasedGallerySerializer(memories, many=True, context={"request": request})
        return Response(serializer.data)
    
   
class LeaveCondolenceView(generics.CreateAPIView):
    serializer_class = CondolenceSerializer

    def post(self, request, deceasedid):
        condoled_by = request.data.get("condoled_by")
        message = request.data.get('message')
        # deceased = request.data.get('deceasedid').firstname.value()
        # print("Te deceased is ", deceased)
        data = {'message': message, 'deceasedid': deceasedid, 'condoled_by': condoled_by}
        serializer = CondolenceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request, deceasedid):
    #     condolences = CondolenceNotes.objects.filter(deceasedid=deceasedid)
    #     serializer = CondolenceSerializer(condolences, many=True)
    #     return Response(serializer.data)
    

















































    # def post(self, request):
    #     serializer = CondolenceSerializer(data=request.data)
    #     if serializer.is_valid():
    #         created_instance = serializer.create(validated_data=request.data)
    #         created_instance.save()
    #         return Response({"message": "Message sent"},status=status.HTTP_200_OK)

    # def get(self, request):
    #     notes = CondolenceNotes.objects.all()
    #     serializer = CondolenceSerializer(notes, many=True)
    #     return Response(serializer.data)