from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms.widgets import DateInput
from aplicacion.models import User,Course




class SignUpForm(forms.ModelForm):
	class Meta:
		model = User

		fields = ('id','name','email','password','language','birthdate','profile_pic')

		labels = {
		    'name': _('Nombre'),
		    'password': _('Contraseña'),
		    'language': _('Idioma'),
		    'birthdate': _('Fecha de nacimiento'),
		    'profile_pic': _('Foto de perfil'),
		}

		widgets = {
		    'password': forms.PasswordInput(),
		    'birthdate': DateInput(attrs={'type': 'date'})
		}

		help_texts = {
		    'name': _('Escribe tu nombre'),
		}
		error_messages = {
		    'name': {
		        'max_length': _("El nombre es demasiado largo."),
		    },
		}

class CrearClaseForm(forms.ModelForm):
      
      class Meta:
        model = Course
        exclude = ['teacher']
        fields = ('id','title','description','level')
        widgets = {
          #'teacher' : forms.Select(attrs={'class' : 'form-control'}),
          'title' : forms.TextInput(attrs = {'class' : 'form-control','placeholder' : 'Escribe el nombre de la clase' }),
          'description' : forms.Textarea(attrs={'class' : 'form-control'}),
          'level' : forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Escribe el nivel de la clase' }),

        }

        labels = {
            #'teacher': _('Profesor'),
            'title': _('Titulo'),
            'description': _('Descripcion'),
            'level': _('Nivel'),
        }

