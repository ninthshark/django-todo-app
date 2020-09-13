from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        labels = {
            "todo": ""
        }
        fields = ('todo',)

        widgets = {'todo': forms.TextInput(attrs={'class': 'form-control'})}
