from django.forms import ModelForm
from app.models import Users

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = "__all__"

    def __init__(self, *args ,**kwargs):
        super().__init__(*args ,**kwargs)
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})
    