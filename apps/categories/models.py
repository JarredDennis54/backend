from django.db import models


# Create your models here.

class Categories(models.Model):
   
    class Meta(object):
        db_table = 'categories'

    name = models.CharField(
        'Name', max_length=50, db_index=True, null=False, blank=False
    )

    
    created_at = models.DateTimeField(
        'Created_at',auto_now_add=True, null=False, blank=False
    )

    updated_at = models.DateTimeField(
        'Updated_at', auto_now_add=True, null=False, blank=False
    )

    def __str__(self):
        return self.name