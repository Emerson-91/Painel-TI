from django import forms
from django.contrib.auth.models import User, Group

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")
    password_confirm = forms.CharField(
        widget=forms.PasswordInput, label="Confirme a senha"
    )
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = User
        fields = ['username', 'first_name',
                  'last_name', 'email', 'password', 'groups']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "As senhas não coincidem.")

        return cleaned_data

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])  # CRIPTOGRAFAR A SENHA
        if commit:
            user.save()
            # Adiciona o usuário aos grupos
            groups = self.cleaned_data.get('groups')
            if groups:
                user.groups.set(groups)
        return user
