from django import forms 
from .models import *



class descriptionForm(forms.ModelForm):
    class Meta:
        model = Description
        fields = ('description', 'ecole', 'niveau','classe')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['niveau'].queryset=Niveau.objects.none()
        

        if 'ecole' in self.data:
            try:
                ecole_id=int(self.data.get('ecole'))
                self.fields['niveau'].queryset=Niveau.objects.filter(ecole_id=ecole_id).order_by('name')
              

            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['niveau'].queryset = self.instance.ecole.niveau_set.order_by('name')
            