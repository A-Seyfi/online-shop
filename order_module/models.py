from django.db import models
from account_module.models import User
from product_module.models import Product, Color, RAM, Storage, Warranty



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
                print(type(order_detail.color), order_detail.color)
            for order_detail in self.orderdetail_set.all():
                total_amount += (int(order_detail.final_price) * int(order_detail.count) +
                                 int(order_detail.color.price_increase) + 
                                 int(order_detail.ram.price_increase) + 
                                 int(order_detail.storage.price_increase) + 
                                 int(order_detail.warranty.price_increase))
        else:
            for order_detail in self.orderdetail_set.all():
                total_amount += (order_detail.product.price * order_detail.count +
                                 int(order_detail.color.price_increase) + 
                                 int(order_detail.ram.price_increase) + 
                                 int(order_detail.storage.price_increase) + 
                                 int(order_detail.warranty.price_increase))

        return total_amount

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید کاربران'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, max_length=50,verbose_name='رنگ', null=True, blank=True)
    ram = models.ForeignKey(RAM, on_delete=models.CASCADE, max_length=50, verbose_name='رم', null=True, blank=True)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE, max_length=50, verbose_name='حافظه', null=True, blank=True)
    warranty = models.ForeignKey(Warranty, on_delete=models.CASCADE, max_length=50, verbose_name='گارانتی', null=True, blank=True)
    final_price = models.IntegerField(null=True, blank=True, verbose_name='قیمت نهایی تکی محصول')
    count = models.IntegerField(verbose_name='تعداد')

    def get_total_price(self):
        return self.count * self.product.price

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = 'جزییات سبد خرید'
        verbose_name_plural = 'لیست جزییات سبدهای خرید'
