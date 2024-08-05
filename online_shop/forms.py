from django import forms

from online_shop.models import Comment, Order,Product


#
# class CommentForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     body = forms.CharField(widget=forms.Textarea)

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = ['name','email','body']
        exclude = ('product',)

    def clean_email(self):
        email = self.data.get('email')
        if Comment.objects.filter(email=email).exists():
            raise forms.ValidationError(f'This {email} is already used')
        return email

    # def clean_body(self):
    #     negative_message = ['']
    #     body = self.data.get('body')
    #     if negative_message in body.split(' '):
    #         raise
    #     return body


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('product',)


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'