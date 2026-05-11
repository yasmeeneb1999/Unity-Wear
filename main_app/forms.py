from django import forms
from .models import ClothingItem, Request, Message


class ClothingItemForm(forms.ModelForm):
    class Meta:
        model = ClothingItem
        fields = [
            "title",
            "description",
            "phone_number",
            "size",
            "category",
            "condition",
            "image",
            "is_available",
        ]

        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "class": "custom-textarea",
                }
            )
        }


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = [
            "message",
        ]
        widgets = {
            "message": forms.Textarea(
                attrs={
                    "rows": 5,
                    "class": "custom-textarea",
                }
            )
        }


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            "content",
        ]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 5,
                    "class": "custom-textarea",
                }
            )
        }
