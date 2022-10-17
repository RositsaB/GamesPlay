from django import forms

from games.web.models import Profile, Game


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'category', 'rating', 'max_level', 'image', 'summary')
        labels = {
            'max_level': 'Max Level',
            'image': 'Image URL',
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password', 'first_name', 'last_name', 'picture')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'picture': 'Profile Picture',
        }


class EditGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'category', 'rating', 'max_level', 'image', 'summary')
        labels = {
            'max_level': 'Max Level',
            'image': 'Image URL',
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        Game.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class DeleteGameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Game
        fields = ('title', 'category', 'rating', 'max_level', 'image', 'summary')
        labels = {
            'max_level': 'Max Level',
            'image': 'Image URL',
        }