from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label="Email")
    subject =forms.CharField(required=False)
    category = forms.ChoiceField(choices=[('web designing', 'Web Designing'), ('web scraping', 'Web Scraping'),
                                          ])
    message = forms.CharField(widget=forms.Textarea)
