from django.db import models
from django.contrib import admin
from django.utils.html import format_html 
from django.contrib.auth import get_user_model

# Create your models here.

User=get_user_model()

class Advertisement(models.Model):
    title = models.CharField("заголовок",max_length=128)
    description=models.TextField("описание")
    price=models.DecimalField("цена",max_digits=10, decimal_places=2)
    auction=models.BooleanField("торг",help_text="Если торг уместен, то True(1), если не уместен - False(0)")
    created_data=models.DateTimeField("дата публикации",auto_now_add=True)
    updated_data=models.DateTimeField("дата обновления",auto_now=True)
    user=models.ForeignKey(User, verbose_name='пользователь',on_delete=models.CASCADE,null=True)
    image=models.ImageField("фото",upload_to='advertisements/')
    
    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'
    
    def created_date(self):
        from django.utils import timezone
        if self.created_data.date()==timezone.now().date():
            created_time=self.created_data.time().strftime("%H:%M:%S")
            return format_html('<span style="color:orange;font-weight:bold;">Сегодня в {}</span>',created_time)
        return self.created_data.strftime("%d.%m.%Y в %H:%M:%S")

    def updated_date(self):
        from django.utils import timezone
        if self.updated_data.date()==timezone.now().date():
            updated_time=self.updated_data.time().strftime("%H:%M:%S")
            return format_html('<span style="color:blue;font-weight:bold;">Сегодня в {}</span>',updated_time)
        return self.updated_data.strftime("%d.%m.%Y в %H:%M:%S")    
        
    class Meta:
        db_table="advertisements"
