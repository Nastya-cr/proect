from django.db import models
from .models import YourModel

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


def registration_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration.html', {'form': form})

class YourModelForm(forms.ModelForm):
    class Meta:
        model = YourModel
        fields = '__all__' 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'your-css-class'}) 

   
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.startswith('?'):
            raise forms.ValidationError("Заголовок не может начинаться с вопросительного знака")
        return title
class Advertisement(models.Model):
    title= models.CharField('заголовок', max_length=128)
    
    description= models.TextField('описание')

    price= models.DecimalField('цена', max_digits=10, decimal_places=2)
   
    
    auction= models.BooleanField('торг', help_text='отметьте,уместен ли торг')
    created_at= models.DateTimeField(auto_now_add=True)

    updated_at= models.DateTimeField(auto_now=True)

    def created_date(self):
        from django.utils import timezone
        if self.created_at == timezone.now().date():
            created_date = self.created_at.strftime("%H:%M:%S")
            return format.html('<span>сегодня в {} </span>', created_date)
        return self.created_at.srtftime("%d.%m.%Y в %H:%M:%S")
    
    
    def get_html_image(self):
        if self.image:
            return format_html(
                'img scr="()" style="max_widh:80px; vax_height:80px"'
                self.image.url
            )