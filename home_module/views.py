from django.db.models import Count, Sum
from django.shortcuts import render
from django.views.generic.base import TemplateView
from product_module.models import Product, ProductCategory
from order_module.models import Order
from site_module.models import SiteBanner
from site_module.models import SiteSetting, FooterLinkBox, Slider


class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sliders = Slider.objects.filter(is_active=True)
        context['sliders'] = sliders
        context['banners'] = SiteBanner.objects.filter(is_active=True)
        latest_products = Product.objects.filter(is_active=True, is_delete=False).order_by('-id')[:8]
        most_visit_products = Product.objects.filter(is_active=True, is_delete=False).annotate(visit_count=Count('productvisit')).order_by('-visit_count')[:8]
        context['latest_products'] = latest_products
        context['most_visit_products'] = most_visit_products
        categories = list(ProductCategory.objects.annotate(products_count=Count('product_categories')).filter(is_active=True, is_delete=False, products_count__gt=0)[:6])
        categories_products = []
        for category in categories:
            item = {
                'id': category.id,
                'title': category.title,
                'products': list(category.product_categories.all()[:4])
            }
            categories_products.append(item)

        context['categories_products'] = categories_products

        return context


def site_header_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting': setting
    }
    return render(request, 'shared/site_header_component.html', context)


def header_context(request):
    if request.user.is_authenticated:
        current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False, user_id=request.user.id)
    else:
        current_order = 0

    return {'total_items': current_order}


def site_footer_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_link_boxes = FooterLinkBox.objects.all()
    context = {
        'site_setting': setting,
        'footer_link_boxes': footer_link_boxes
    }
    return render(request, 'shared/site_footer_component.html', context)


class AboutView(TemplateView):
    template_name = 'home_module/about_page.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        site_setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = site_setting
        return context