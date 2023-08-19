from django.db import models

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