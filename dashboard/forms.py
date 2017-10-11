from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms
from models import Manufacture


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class ManufactureForm(forms.ModelForm):
    
    start_date = forms.DateField(label="Enter Start Date", widget=forms.TextInput(attrs={'class':'datepicker'}))
    end_date = forms.DateField(label="End End Date", widget=forms.TextInput(attrs={'class':'datepicker'}))
    warehouse1 = forms.CharField(max_length=250, label="Asset1", required=False)
    store1 = forms.DecimalField(max_digits=5, decimal_places=2, label= "weight for Asset1", required=False)
    warehouse2 = forms.CharField(max_length=250,label="Asset2", required=False)
    store2 = forms.DecimalField(max_digits=5, decimal_places=2, label= "weight for Asset2", required=False)
    warehouse3 = forms.CharField(max_length=250,label="Asset3", required=False)
    store3 = forms.DecimalField(max_digits=5, decimal_places=2, label= "weight for Asset3", required=False,)
    warehouse4 = forms.CharField(max_length=250,label="Asset4", required=False)
    store4 = forms.DecimalField(max_digits=5, decimal_places=2, label= "weight for Asset4", required=False)
    warehouse5 = forms.CharField(max_length=250,label="Asset5", required=False)
    store5 = forms.DecimalField(max_digits=5, decimal_places=2, label= "weight for Asset5", required=False)
    warehouse6 = forms.CharField(max_length=250,label="Asset6", required=False)
    store6 = forms.DecimalField(max_digits=5, decimal_places=2, label= "weight for Asset6", required=False)
    warehouse7 = forms.CharField(max_length=250,label="Asset7", required=False)
    store7 = forms.DecimalField(max_digits=5, decimal_places=2, label= "weight for Asset7", required=False)
    warehouse8 = forms.CharField(max_length=250,label="Asset8", required=False)
    store8 = forms.DecimalField(max_digits=5, decimal_places=2, label= "weight for Asset8", required=False)
    warehouse9 = forms.CharField(max_length=250,label="Asset9", required=False)
    store9 = forms.DecimalField(max_digits=5, decimal_places=2,label= "weight for Asset9", required=False)
    warehouse10 = forms.CharField(max_length=250,label="Asset10", required=False)
    store10 = forms.DecimalField(max_digits=5, decimal_places=2, label= "weight for Asset10", required=False)
    warehouse10 = forms.CharField(max_length=250,label="Asset10", required=False)
    store10 = forms.DecimalField(max_digits=5, decimal_places=2, label= "weight for Asset10", required=False)
    warehouse11 = forms.CharField(max_length=250,label="Asset11", required=False)
    store11 = forms.DecimalField(max_digits=5, decimal_places=2, label= "weight for Asset11", required=False)
    warehouse12 = forms.CharField(max_length=250,label="Asset12", required=False)
    store12 = forms.DecimalField(max_digits=5, decimal_places=2, label= "weight for Asset12", required=False)
    warehouse13 = forms.CharField(max_length=250,label="Asset13", required=False)
    store13 = forms.DecimalField(max_digits=5, decimal_places=2, label= "weight for Asset13", required=False)
    warehouse14 = forms.CharField(max_length=250,label="Asset14", required=False)
    store14 = forms.DecimalField(max_digits=5, decimal_places=2, label= "weight for Asset14", required=False)
    warehouse15 = forms.CharField(max_length=250,label="Asset15", required=False)
    store15 = forms.DecimalField(max_digits=5, decimal_places=2, label= "weight for Asset15", required=False)
    like = forms.ChoiceField(choices=Manufacture.CHOICES, widget=forms.RadioSelect())
    
    class Meta:
        
        model = Manufacture

        fields = ('start_date','end_date','warehouse1','store1','warehouse2', 'store2','warehouse3','store3','warehouse4', 'store4','warehouse5','store5','warehouse6', 'store6','warehouse7','store7','warehouse8','store8', 'warehouse9','store9','warehouse10', 'store10','warehouse11','store11','warehouse12', 'store12','warehouse13','store13','warehouse14', 'store14','warehouse15', 'store15','like')
    
    def clean_store1(self):
        store1 = self.cleaned_data['store1'] 
        if (store1 != 100 and store1 != None):               
            raise forms.ValidationError(u'This field is Must be 100.')            
        return store1
    def clean_store2(self):
        store2 = self.cleaned_data['store2'] 
        if (store2 != 100 and store2 != None):                
            raise forms.ValidationError(u'This field is Must be 100.')            
        return store2
    def clean_store3(self):
        store3 = self.cleaned_data['store3'] 
        if (store3 != 100 and store3 != None):                
            raise forms.ValidationError(u'This field is Must be 100.')            
        return store3
    def clean_store4(self):
        store4 = self.cleaned_data['store4'] 
        if (store4 != 100 and store4 != None):                
            raise forms.ValidationError(u'This field is Must be 100.')            
        return store4
    def clean_store5(self):
        store5 = self.cleaned_data['store5'] 
        if (store5 != 100 and store5 != None):               
            raise forms.ValidationError(u'This field is Must be 100.')            
        return store5
    def clean_store6(self):
        store6 = self.cleaned_data['store6'] 
        if (store6 != 100 and store6 != None):                
            raise forms.ValidationError(u'This field is Must be 100.')            
        return store6
    def clean_store7(self):
        store7 = self.cleaned_data['store7'] 
        if (store7 != 100 and store7 != None):              
            raise forms.ValidationError(u'This field is Must be 100.')            
        return store7
    def clean_store8(self):
        store8 = self.cleaned_data['store8'] 
        if (store8 != 100 and store8 != None):              
            raise forms.ValidationError(u'This field is Must be 100.')            
        return store8
    def clean_store9(self):
        store9 = self.cleaned_data['store9'] 
        if (store9 != 100 and store9 != None):                
            raise forms.ValidationError(u'This field is Must be 100.')            
        return store9
    def clean_store10(self):
        store10 = self.cleaned_data['store10'] 
        if (store10 != 100 and store10 != None):                
            raise forms.ValidationError(u'This field is Must be 100.')            
        return store10
    def clean_store11(self):
        store11 = self.cleaned_data['store11'] 
        if (store11 != 100 and store11 != None):               
            raise forms.ValidationError(u'This field is Must be 100.')            
        return store11
    def clean_store12(self):
        store12 = self.cleaned_data['store12'] 
        if (store12 != 100 and store12 != None):               
            raise forms.ValidationError(u'This field is Must be 100.')            
        return store12
    def clean_store13(self):
        store13 = self.cleaned_data['store13'] 
        if (store13 != 100 and store13 != None):                
            raise forms.ValidationError(u'This field is Must be 100.')            
        return store13
    def clean_store14(self):
        store14 = self.cleaned_data['store14'] 
        if (store14 != 100 and store14 != None):               
            raise forms.ValidationError(u'This field is Must be 100.')            
        return store14
    def clean_store15(self):
        store15 = self.cleaned_data['store15'] 
        if (store15 != 100 and store15 != None):              
            raise forms.ValidationError(u'This field is Must be 100.')            
        return store15
