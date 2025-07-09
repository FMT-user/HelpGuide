from django import forms

class AppSelectForm(forms.Form):
    app = forms.ChoiceField(label="Application", choices=[])

class TopicSelectForm(forms.Form):
    topic = forms.ChoiceField(label="Topic", choices=[])
