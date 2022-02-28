from django.db import models

# Create your models here.
class Entry(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=True)
    second_name = models.CharField(max_length=100, blank=False, null=True)
    matric_no = models.CharField(max_length=100, blank=False, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    lecture_1 = models.BooleanField(default=False)
    lecture_2 = models.BooleanField(default=False)
    lecture_3 = models.BooleanField(default=False)
    lecture_4 = models.BooleanField(default=False)
    lecture_5 = models.BooleanField(default=False)
    lecture_6 = models.BooleanField(default=False)

    def __str__(self):
        return 'Entry #{}'.format(self.id)

    class Meta:
        verbose_name_plural = 'entries'
