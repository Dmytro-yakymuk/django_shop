from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.http import HttpResponse, JsonResponse

from .models import Product, Category, Image
from .forms import ReviewForm

class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'product/home.html', {"products": products})


# 3 спосіб вивести всі категорії
class CategoryGetAll():
    def get_categories(self):
        return Category.objects.all()

class ImagesGetRoot():
    def get_image_root(self):
        return Image.objects.filter('root').value('name')


class ProductListView(CategoryGetAll, ListView):
    model = Product
    queryset = Product.objects.all()

    # 1 спосіб виввести всі категорії
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context



class ProductFilterView(CategoryGetAll, ListView):
    def get_queryset(self):
        queryset = Product.objects.filter(category__in=self.request.GET.getlist("category"))
        return queryset

class JsonProductFilterView(ListView):

    def get_queryset(self):
        # queryset = Product.objects.filter(
        #     Q(category__in=self.request.GET.getlist("category")) |
        #     "price" >= self.request.GET.getlist("price1") &
        #     "price" <= self.request.GET.getlist("price2")
        # ).distinct().values("id", "name", "slug", "price")
        queryset = Product.objects.filter(
            Q(category__in=self.request.GET.getlist("category"))
        ).distinct().values("id", "name", "slug", "price")
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({"products": queryset}, safe=False)

class ProductDetailView(DetailView):
    model = Product
    slug_field = "slug"


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.product = product
            form.save()

        return redirect(product.get_absolute_url())
