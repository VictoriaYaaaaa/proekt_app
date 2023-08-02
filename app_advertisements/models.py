from django.db import models

# Create your models here.

class Advertisement(models.Model):
    title = models.CharField("заголовок",max_length=128)
    description=models.TextField("описание")
    price=models.DecimalField("цена",max_digits=10, decimal_places=2)
    auction=models.BooleanField("торг",help_text="Если торг уместен, то True(1), если не уместен - False(0)")
    created_data=models.DateTimeField("дата публикации",auto_now_add=True)
    updated_data=models.DateTimeField("дата обновления",auto_now=True)

    def __str__(self):
        return f'Advertisement(id={self.id}, title={self.title}, price={self.price})'
    
    class Meta:
        db_table="advertisements"
