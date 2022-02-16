from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import ContactList, DeceasedList, DeceasedDetailView, LeaveCondolenceView,  DeceasedGalleryList

urlpatterns = [
    path('contact', ContactList.as_view(), name="contact"),
    path('obituaries', DeceasedList.as_view(), name="obituaries"),
    path('obituaries/<int:deceasedid>', DeceasedDetailView.as_view(), name="obituary"),
    path('obituaries/<int:deceasedid>/condole', LeaveCondolenceView.as_view(), name="condole"),
    path('obituaries/<int:deceasedid>/memories',  DeceasedGalleryList.as_view(), name="memories" )
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)