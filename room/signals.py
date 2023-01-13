from channels.layers import get_channel_layer
from django.db.models import signals
from asgiref.sync import async_to_sync

from django.contrib.auth.models import User
from .models import Room


def room_info_update(sender, instance, created, **kwargs):
    print("AQUI")
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
            f"room_update_{instance.slug}", 
            {
                "type": "update.room",
                "event": "change", 
                "instance":(instance.slug)
            }
    )    
signals.post_save.connect(receiver=room_info_update, sender=Room)