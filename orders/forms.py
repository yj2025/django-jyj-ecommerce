from django import forms

from orders.models import ShippingAddress



# dev_25
class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = "__all_"
        exclude = ["user"]