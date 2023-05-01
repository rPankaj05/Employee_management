from django import forms


class FeedbackForm(forms.Form):
    email=forms.EmailField(label="Enter your email",max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    name = forms.CharField(label="Enter your name", max_length=100 ,widget=forms.TextInput(attrs={'class': "form-control"}))
    feedback=forms.CharField(label="Your Feedback",widget=forms.Textarea(attrs={'class':'form-control'}))


 