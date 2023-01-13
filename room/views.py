from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Room,Message

import random

def color_scheme(id):
    random_number = random.randint(int(id),16777215)
    hex_number = str(hex(random_number))
    hex_number ='#'+ hex_number[2:]
    return hex_number
# Create your views here.
@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request,'room/rooms.html',{'rooms':rooms})

@login_required
def room(request,slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)
    user_id_list = list(dict.fromkeys(messages.values_list('user__username',flat=True)))
    users_with_messages = User.objects.filter(username__in=user_id_list)
    user_color_scheme = [{
                        'user_id':user.username,
                        'color_scheme':color_scheme(user.id)
    }for user in users_with_messages]

   
    
    return render(request,'room/room.html',{'room':room,'messages':messages,'user_color_scheme':user_color_scheme,'user_id_list':user_id_list})



