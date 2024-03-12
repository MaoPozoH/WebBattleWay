from contextlib import _RedirectStream
from csv import reader
from django.contrib.auth import login
from django.contrib.auth.models import User
from django import forms
from .models import Tournament, Player

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = '__all__'

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Las contraseñas no coinciden.')

        return cleaned_data

    def post(self, request):
        # Lógica para procesar el formulario después de enviar el método POST
        form = self(request.POST)
        if form.is_valid():
            user = form.save()
            # Realizar acciones adicionales después del registro exitoso
            # Por ejemplo, iniciar sesión automáticamente
            login(request, user)
            return _RedirectStream('home')  # Reemplaza 'home' con la URL deseada después del registro
        else:
            # Manejar el caso cuando el formulario no es válido
            return reader(request, 'registration/registration.html', {'form': form})