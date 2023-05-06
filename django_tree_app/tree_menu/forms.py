from django import forms


class AddItemMenuForm(forms.ModelForm):
    class Meta:
        widgets = {
            'label': forms.TextInput(attrs={'size': 20}),
            'parent': forms.TextInput(attrs={'size': 20}),
            'position': forms.TextInput(attrs={'size': 20}),
            'url': forms.TextInput(attrs={'size': 20}),
                   }