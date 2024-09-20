from django.db import models
from django.urls import reverse
from account_module.models import User



class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def __str__(self):
        return f'( {self.title} - {self.url_title} )'

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ProductBrand(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام برند', db_index=True)
    image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='تصویر برند')
    url_title = models.CharField(max_length=300, verbose_name='نام در url', db_index=True)
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام محصول')
    category = models.ManyToManyField(ProductCategory, related_name='product_categories', verbose_name='دسته بندی ها')
    image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='تصویر محصول')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name='برند', null=True, blank=True)
    price = models.IntegerField(verbose_name='قیمت')
    customization = models.BooleanField(verbose_name='قابل کاستوم شدن', default=False)
    short_description = models.CharField(max_length=360, db_index=True, null=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات اصلی', db_index=True)

    dimensions = models.CharField(max_length=255, verbose_name='ابعاد', null=True, blank=True)
    weight = models.FloatField(verbose_name='وزن (Kg)', null=True, blank=True)

    cpu_processor = models.CharField(max_length=255, verbose_name='سازنده پردازنده', null=True, blank=True)
    cpu = models.CharField(max_length=255, verbose_name='سری پردازنده', null=True, blank=True)
    cpu_model = models.CharField(max_length=255, verbose_name='مدل پردازنده', null=True, blank=True)
    cpu_frequency = models.FloatField(verbose_name='فرکانس کاری پردازنده (GHz)', null=True, blank=True)
    cpu_cache = models.CharField(max_length=255, verbose_name='حافظه‌ی کش (MB)', null=True, blank=True)
    cpu_core = models.CharField(max_length=255, verbose_name='تعداد هسته', null=True, blank=True)
    cpu_info = models.TextField(verbose_name='اطلاعات تکمیلی پردازنده', null=True, blank=True)

    screen_size = models.CharField(max_length=255, verbose_name='ابعاد صفحه‌نمایش', null=True, blank=True)
    resolution = models.CharField(max_length=255, verbose_name='وضوح تصویر', null=True, blank=True)
    panel_type = models.CharField(max_length=255, verbose_name='نوع پنل', null=True, blank=True)
    refresh_rate = models.CharField(max_length=255, verbose_name='نرخ نوسازی تصویر', null=True, blank=True)
    screen_cover = models.CharField(max_length=255, verbose_name='پوشش صفحه نمایش', null=True, blank=True)
    touch_screen = models.BooleanField(verbose_name='صفحه‌نمایش لمسی', default=False)
    additional_display_features = models.TextField(verbose_name='سایر ویژگی‌های نمایشگر', null=True, blank=True)

    ram_type = models.CharField(max_length=255, verbose_name='نوع حافظه‌ی رم', null=True, blank=True)
    ram_bus = models.CharField(max_length=255, verbose_name='باس رم (MHz)', null=True, blank=True)
    ram_upgradable = models.BooleanField(verbose_name='قابلیت ارتقای رم', default=False)

    internal_memory = models.CharField(max_length=255, verbose_name='ظرفیت حافظه داخلی', null=True, blank=True)
    internal_memory_upgradable = models.BooleanField(verbose_name='قابلیت ارتقا حافظه داخلی', default=False)

    gpu_manufacturer = models.CharField(max_length=255, verbose_name='سازنده پردازنده‌ گرافیکی', null=True, blank=True)
    gpu_model = models.CharField(max_length=255, verbose_name='مدل پردازنده‌ گرافیکی', null=True, blank=True)
    gpu_type = models.CharField(max_length=255, verbose_name='نوع پردازنده‌ گرافیکی', null=True, blank=True)
    gpu_memory = models.CharField(max_length=255, verbose_name='حافظه پردازنده‌ گرافیکی', null=True, blank=True)
    gpu_ram_type = models.CharField(max_length=255, verbose_name='نوع رم پردازنده‌ گرافیکی', null=True, blank=True)

    wifi_network = models.BooleanField(verbose_name='شبکه Wi-Fi', default=False)
    wireless_communication_info = models.TextField(verbose_name='توضیحات شبکه Wi-Fi', null=True, blank=True)
    bluetooth = models.BooleanField(verbose_name='بلوتوث', default=False)
    bluetooth_info = models.CharField(max_length=255, verbose_name='توضیحات بلوتوث', null=True, blank=True)
    lan = models.BooleanField(verbose_name='درگاه LAN', default=False)
    usb_3_ports_count = models.PositiveIntegerField(verbose_name='تعداد درگاه USB 3.0 Type A و بالاتر', null=True, blank=True)
    usb_2_ports_count = models.PositiveIntegerField(verbose_name='تعداد درگاه USB 2.0 Type A', null=True, blank=True)
    usb_c_ports_count = models.PositiveIntegerField(verbose_name='تعداد درگاه USB Type C', null=True, blank=True)
    vga_port = models.BooleanField(verbose_name='VGA', default=False)
    hdmi_port = models.BooleanField(verbose_name='HDMI', default=False)
    card_reader = models.BooleanField(verbose_name='درگاه کارت‌خوان', default=False)
    thunderbolt_support = models.BooleanField(verbose_name='پشتیبانی از تاندربولت', default=False)
    headphone_microphone_jack = models.BooleanField(verbose_name='جک هدفون/میکروفن', default=False)
    
    battery = models.CharField(max_length=255, verbose_name='حجم باتری', null=True, blank=True)
    battery_charge = models.CharField(max_length=255, verbose_name='شارژدهی باتری', null=True, blank=True)
    charger_power = models.CharField(max_length=255, verbose_name='توان شارژر', null=True, blank=True)

    speakers_info = models.CharField(max_length=255, verbose_name='اسپیکر', null=True, blank=True)
    webcam = models.BooleanField(verbose_name='وبکم', default=False)
    webcam_description = models.TextField(verbose_name='توضیحات وبکم', null=True, blank=True)
    optical_drive = models.BooleanField(verbose_name='درایو نوری', default=False)
    backlit_keyboard = models.BooleanField(verbose_name='کیبورد با نور پس‌زمینه', default=False)
    fingerprint_sensor = models.BooleanField(verbose_name='حسگر اثر انگشت', default=False)
    
    alternative_name = models.CharField(max_length=255, verbose_name='نام دیگر', null=True, blank=True)

    slug = models.SlugField(null=False, db_index=True, blank=False, max_length=200, unique=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price}) {self.alternative_name}"

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class Color(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    name = models.CharField(max_length=20, verbose_name="رنگ")
    price_increase = models.IntegerField(verbose_name="افزایش قیمت به ازای انتخاب")

    def __str__(self):
        return f'رنگ: {self.name} - افزایش قیمت: {self.price_increase}'

    class Meta:
        verbose_name = 'رنگ محصول'
        verbose_name_plural = 'رنگ های محصولات'

class RAM(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    size = models.CharField(max_length=10, verbose_name="ظرفیت رم")
    price_increase = models.IntegerField(verbose_name="افزایش قیمت به ازای انتخاب")

    def __str__(self):
        return f'رم: {self.size} - افزایش قیمت: {self.price_increase}'

    class Meta:
        verbose_name = 'حافظه رم محصول'
        verbose_name_plural = 'حافظه رم محصولات'

class Storage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول", )
    size = models.CharField(max_length=10, verbose_name="ظرفیت حافظه")
    price_increase = models.IntegerField(verbose_name="افزایش قیمت به ازای انتخاب")

    def __str__(self):
        return f'حافظه: {self.size} - افزایش قیمت: {self.price_increase}'

    class Meta:
        verbose_name = 'حافظه محصول'
        verbose_name_plural = 'حافظه محصولات'

class Warranty(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    duration = models.CharField(max_length=150, verbose_name="گارانتی")
    price_increase = models.IntegerField(verbose_name="افزایش قیمت به ازای انتخاب")
    
    def __str__(self):
        return f'گارانتی: {self.duration} - افزایش قیمت: {self.price_increase}'
        
    class Meta:
        verbose_name = 'گارانتی'
        verbose_name_plural = 'گارانتی ها'


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="کاربر")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصولات مورد علاقه")

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = 'مورد علاقه'
        verbose_name_plural = 'محصولات مورد علاقه'


class ProductTag(models.Model):
    caption = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags')

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'

    def __str__(self):
        return self.caption


class ProductVisit(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='محصول')
    ip = models.CharField(max_length=30, verbose_name='آی پی کاربر')
    user = models.ForeignKey(User, null=True, blank=True, verbose_name='کاربر', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.title} / {self.user}'

    class Meta:
        verbose_name = 'بازدید محصول'
        verbose_name_plural = 'بازدیدهای محصول'


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    image = models.ImageField(upload_to='images/product-gallery', verbose_name='تصویر')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'تصویر گالری'
        verbose_name_plural = 'گالری تصاویر'


class ProductComment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    parent = models.ForeignKey('ProductComment', null=True, blank=True, on_delete=models.CASCADE, verbose_name='والد')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    text = models.TextField(verbose_name='متن نظر')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'
