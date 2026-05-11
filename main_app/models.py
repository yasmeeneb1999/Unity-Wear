from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ClothingItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    phone_number = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    category = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    image = models.URLField()
    is_available = models.BooleanField(default=True)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="clothing_items"
    )

    def __str__(self):
        return self.title


class Request(models.Model):
    clothing_item = models.ForeignKey(
        ClothingItem, on_delete=models.CASCADE, related_name="requests"
    )
    requester = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="requests_sent"
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request for {self.clothing_item.title}"


class Message(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages_sent"
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages_received"
    )

    clothing_item = models.ForeignKey(
        ClothingItem, on_delete=models.CASCADE, related_name="messages"
    )

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username}"
