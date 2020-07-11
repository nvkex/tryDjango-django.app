from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget = forms.Textarea)

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        print(email)
        return email

