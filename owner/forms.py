from django import forms
from django.forms import ModelForm
from owner.models import Books
from customer.models import Orders


class BookForm(ModelForm):
    class Meta:
        model=Books
        exclude=("active_status",)
        widgets={
            "book_name":forms.TextInput(attrs={"class":"form-control"}),
            "author_name":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "copies":forms.NumberInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"})
        }
        # fields="__all__"
    # book_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # author_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # price=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    # copies=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))

    def clean(self):
        cleaned_data=super().clean()
        price=int(cleaned_data.get('price'))
        copies=cleaned_data.get('copies')
        if price<0:
            msg="invalid price"
            self.add_error('price',msg)
        if copies<0:
            msg="invlaid copies"
            self.add_error('copies',msg)

# class BookEdit(forms.Form):
#     book_name = forms.CharField()
#     author = forms.CharField()
#     price = forms.CharField()
#     copies = forms.CharField()

class OrderProcessForm(ModelForm):
    class Meta:
        model=Orders
        fields=["status","expected_delivery_date"]
        widgets={
            "status":forms.Select(attrs={"class":"form-select"}),
            "expected_delivery_date":forms.DateInput(attrs={"class":"form-control","type":"date"})
        }