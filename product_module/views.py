from django.db.models import Count, Sum
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from utils.http_service import get_client_ip
from .models import Product, ProductCategory, ProductBrand, ProductVisit, ProductGallery, Favorite, ProductComment
from .forms import LaptopSelectionForm
from fuzzywuzzy import process
from fuzzywuzzy import fuzz


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-id']
    paginate_by = 16

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        query = Product.objects.all()
        product: Product = query.order_by('-price').first()
        db_max_price = product.price if product is not None else 0
        context['db_max_price'] = db_max_price
        context['start_price'] = self.request.GET.get('start_price') or 0
        context['end_price'] = self.request.GET.get('end_price') or db_max_price
        return context

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        category_name = self.kwargs.get('cat')
        brand_name = self.kwargs.get('brand')
        request: HttpRequest = self.request
        start_price = request.GET.get('start_price')
        end_price = request.GET.get('end_price')
        if start_price is not None:
            query = query.filter(price__gte=start_price)

        if end_price is not None:
            query = query.filter(price__lte=end_price)

        if brand_name is not None:
            query = query.filter(brand__url_title__iexact=brand_name)

        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)

        sort_by = self.request.GET.get('sort')
        if sort_by == 'cheap':
            return query.order_by('price')
        
        elif sort_by == 'expensive':
            return query.order_by('-price')
        
        elif sort_by == 'latest':
            return query.order_by('-id')
        
        elif sort_by == 'most_bought':
            return query.filter(orderdetail__order__is_paid=True).annotate(order_count=Sum('orderdetail__count')).order_by('-order_count')
        
        elif sort_by == 'most_visit':
            return query.annotate(visit_count=Count('productvisit')).order_by('-visit_count')
        return query


class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        request = self.request
        favorite_product_id = request.session.get("product_favorites")
        context['form'] = LaptopSelectionForm(product_id=self.object.id)
        context['is_favorite'] = favorite_product_id == str(loaded_product.id)
        galleries = list(ProductGallery.objects.filter(product_id=loaded_product.id).all())
        galleries.insert(0, loaded_product)
        context['comments'] = ProductComment.objects.filter(product_id=self.object.id, parent=None).order_by('-create_date').prefetch_related('productcomment_set')
        context['comments_count'] = ProductComment.objects.filter(product_id=self.object.id).count()
        context['product_galleries'] = ProductGallery.objects.all()
        context['related_products'] = Product.objects.filter(brand_id=loaded_product.brand_id).exclude(pk=loaded_product.id).all()[:4]
        user_ip = get_client_ip(self.request)
        user_id = None
        if self.request.user.is_authenticated:
            user_id = self.request.user.id

        has_been_visited = ProductVisit.objects.filter(ip__iexact=user_ip, product_id=loaded_product.id).exists()

        if not has_been_visited:
            new_visit = ProductVisit(ip=user_ip, user_id=user_id, product_id=loaded_product.id)
            new_visit.save()

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = LaptopSelectionForm(request.POST)

        if form.is_valid():
            total_price = form.cleaned_data['color'].price_increase + \
                          form.cleaned_data['ram'].price_increase + \
                          form.cleaned_data['storage'].price_increase + \
                          form.cleaned_data['warranty'].price_increase
            print(total_price)

            return render(request, self.template_name, {'form': form, 'total_price': total_price})

        return self.get(request, *args, **kwargs)


@login_required
def add_to_favorites(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Favorite.objects.get_or_create(user=request.user, product=product)
    return redirect('favorites_list')


class CompareListView(ListView):
    template_name = 'product_module/compare.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-id']
    paginate_by = 16
    products = Product.objects.all()

    def post(self, request):
        selected_products = request.POST.getlist('products')
        request.session['selected_products'] = selected_products[:4]  # maximum 4 product
        return redirect('compare_result')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CompareListView, self).get_context_data()
        query = Product.objects.all()
        product: Product = query.order_by('-price').first()
        return context

    def get_queryset(self):
        query = super(CompareListView, self).get_queryset()
        category_name = self.kwargs.get('cat')
        brand_name = self.kwargs.get('brand')
        request: HttpRequest = self.request

        sort_by = self.request.GET.get('sort')
        if sort_by == 'cheap':
            return query.order_by('price')
        
        elif sort_by == 'expensive':
            return query.order_by('-price')
        
        elif sort_by == 'latest':
            return query.order_by('-id')
        
        elif sort_by == 'most_bought':
            return query.filter(orderdetail__order__is_paid=True).annotate(order_count=Sum('orderdetail__count')).order_by('-order_count')
        
        elif sort_by == 'most_visit':
            return query.annotate(visit_count=Count('productvisit')).order_by('-visit_count')
        return query


def compare_result(request):
    selected_product_ids = request.session.get('selected_products', [])
    products = Product.objects.filter(id__in=selected_product_ids)

    return render(request, 'product_module/compare_results.html', {'products': products})


def fuzzy_search(query, threshold=15):
    products = Product.objects.all()

    titles = products.values_list('title', flat=True)
    matched_titles = process.extract(query, titles, limit=None, scorer=fuzz.token_set_ratio)
    filtered_titles = [(title, score) for title, score in matched_titles if score >= threshold]

    brands = products.values_list('brand', flat=True)
    matched_brands = process.extract(query, brands, limit=None, scorer=fuzz.token_set_ratio)
    filtered_brands = [(brand, score) for brand, score in matched_brands if score >= threshold]

    cpus = products.values_list('cpu', flat=True)
    matched_cpus = process.extract(query, cpus, limit=None, scorer=fuzz.token_set_ratio)
    filtered_cpus = [(cpu, score) for cpu, score in matched_cpus if score >= threshold]

    filtered_products = products.filter(title__in=[title for title, score in filtered_titles]) | products.filter(cpu__in=[cpu for cpu, score in filtered_cpus]) | products.filter(brand__in=[brand for brand, score in filtered_brands])

    product_scores = []
    for product in filtered_products:
        title_score = next((score for title, score in filtered_titles if title == product.title), None)
        brand_score = next((score for brand, score in filtered_brands if brand == product.brand), None)
        cpu_score = next((score for cpu, score in filtered_cpus if cpu == product.cpu), None)

        max_score = max(title_score or 0, cpu_score or 0, brand_score or 0)
        product_scores.append((product, max_score))

    product_scores.sort(key=lambda x: x[1], reverse=True)
    sorted_products = [product for product, score in product_scores]

    print(filtered_products)
    return sorted_products


def search(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = fuzzy_search(query)

    return render(request, 'product_module/product_list.html', {'results': results, 'query': query})


def product_categories_component(request: HttpRequest):
    product_categories = ProductCategory.objects.filter(is_active=True, is_delete=False)
    context = {
        'categories': product_categories
    }
    return render(request, 'product_module/components/product_categories_component.html', context)


def product_brands_component(request: HttpRequest):
    product_brands = ProductBrand.objects.annotate(products_count=Count('product')).filter(is_active=True)
    context = {
        'brands': product_brands
    }
    return render(request, 'product_module/components/product_brands_component.html', context)


def compare_categories_component(request: HttpRequest):
    product_categories = ProductCategory.objects.filter(is_active=True, is_delete=False)
    context = {
        'categories': product_categories
    }
    return render(request, 'product_module/components/compare_categories_component.html', context)


def compare_brands_component(request: HttpRequest):
    product_brands = ProductBrand.objects.annotate(products_count=Count('product')).filter(is_active=True)
    context = {
        'brands': product_brands
    }
    return render(request, 'product_module/components/compare_brands_component.html', context)


def header_brand_component(request: HttpRequest):
    product_brands = ProductBrand.objects.filter(is_active=True)

    return {'brands': product_brands}


def add_product_comment(request: HttpRequest):
    if request.user.is_authenticated:
        product_id = request.GET.get('product_id')
        product_comment = request.GET.get('product_comment')
        parent_id = request.GET.get('parent_id')
        new_comment = ProductComment(product_id=product_id, text=product_comment, user_id=request.user.id, parent_id=parent_id)
        new_comment.save()
        context = {
            'comments': ProductComment.objects.filter(product_id=product_id, parent=None).order_by('-create_date').prefetch_related('productcomment_set'),
            'comments_count': ProductComment.objects.filter(product_id=product_id).count()
        }

        return render(request, 'product_module/components/product_comments_partial.html', context)

    return HttpResponse('response')
