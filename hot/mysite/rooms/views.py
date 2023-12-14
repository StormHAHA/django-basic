from django.shortcuts import render
from django.views.generic.base import View
from .models import Room

class RoomView(View):

# rooms output
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, 'rooms/rooms.html', {'rooms_list': rooms})


