from django.db import models
from account_module.models import User
from product_module.models import Product


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    is_paid = models.BooleanField(verbose_name='نهایی شده/نشده')
    payment_date = models.DateField(null=True, blank=True, verbose_name='تاریخ پرداخت')

    def __str__(self):
        return f"{self.user} ({self.is_paid}) {self.payment_date}"

    def calculate_total_price(self):
        total_amount = 0
        if self.is_paid:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.final_price * order_detail.count
        else:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.product.price * order_detail.count

        return total_amount

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید کاربران'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    color = models.CharField(max_length=50,verbose_name='رنگ', null=True, blank=True)
    ram = models.CharField(max_length=50, verbose_name='رم', null=True, blank=True)
    storage = models.CharField(max_length=50, verbose_name='حافظه', null=True, blank=True)
    warranty = models.CharField(max_length=50, verbose_name='گارانتی', null=True, blank=True)
    final_price = models.IntegerField(null=True, blank=True, verbose_name='قیمت نهایی تکی محصول')
    count = models.IntegerField(verbose_name='تعداد')

    def get_total_price(self):
        return self.count * self.product.price

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = 'جزییات سبد خرید'
        verbose_name_plural = 'لیست جزییات سبدهای خرید'
