from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    email_active_code = models.CharField(null=True, blank=True, max_length=100, verbose_name='کد فعالسازی ایمیل')
    phone_number = models.IntegerField(null=True, blank=True, verbose_name='شماره تلفن')
    address = models.TextField(null=True, blank=True, verbose_name='آدرس')
    post_code = models.CharField(null=True, blank=True, max_length=10, verbose_name='کد پستی')
    reset_code = models.CharField(null=True, blank=True, max_length=100, verbose_name='کد بازیابی کلمه عبور')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name != '' and self.last_name != '':
            return self.get_full_name()

        return self.email
