from django import forms

from.models import Booking

class Dateinput(forms.DateInput):
    input_type = 'date'    
    

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        
        widgets={
            'booking_date':Dateinput(),
        }
        
        labels ={
            'p_name':'patient Name',
            'p_phone':'phone number',
            'p_email':'Email',
            'dep_name':'Department Name',
            'doc_name':'Doctors Name',
            'booking_date':'Booking Date',
        }
# class contactForm(forms.ModelForm)
    # class Meta        