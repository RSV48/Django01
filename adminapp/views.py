from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.list import ListView

from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm, ProductEditForm
from authapp.forms import ShopUserRegisterForm, ShopUserEditForm
from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory


class UsersListView(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     title = 'админка/пользователи'
#
#     users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#
#     content = {
#         'title': title,
#         'objects': users_list
#     }
#
#     return render(request, 'adminapp/users.html', content)

class UserCreateView(CreateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin:users')
    form_class = ShopUserAdminEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def user_create(request):
#     if request.method == 'POST':
#         register_form = ShopUserRegisterForm(request.POST, request.FILES)
#         if register_form.is_valid():
#             register_form.save()
#             return HttpResponseRedirect(reverse('admin:users'))
#     else:
#         register_form = ShopUserRegisterForm()
#     content = {
#         'title': 'админка/пользоватиели/регистрация',
#         'form': register_form
#     }
#     return render(request, 'adminapp/user_update.html', content)

class UserUpdateView(UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin:users')
    form_class = ShopUserAdminEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def user_update(request, pk):
#     edit_user = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=request.user)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin:user_update', args=[edit_user.pk]))
#     else:
#         edit_form = ShopUserAdminEditForm(instance=request.user)
#
#     content = {
#         'title': 'админка/пользоватиели/редактирование',
#         'form': edit_form
#     }
#     return render(request, 'adminapp/user_update.html', content)

class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('adminapp:users')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


# @user_passes_test(lambda u: u.is_superuser)
# def user_delete(request, pk):
#     user = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         user.is_active = False
#         user.save()
#         return HttpResponseRedirect(reverse('admin:users'))
#
#     content = {'title': 'адиминка/пользователи/удаление',
#                'user_to_delete': user}
#
#     return render(request, 'adminapp/user_delete.html', content)

class CategoriesListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def categories(request):
#     title = 'админка/категории'
#
#     categories_list = ProductCategory.objects.all()
#
#     content = {
#         'title': title,
#         'objects': categories_list
#     }
#
#     return render(request, 'adminapp/categories.html', content)

class CategoriesCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:categories')
    form_class = ProductCategoryEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def category_create(request):
#     if request.method == 'POST':
#         register_form = ProductCategoryEditForm(request.POST, request.FILES)
#         if register_form.is_valid():
#             register_form.save()
#             return HttpResponseRedirect(reverse('admin:users'))
#     else:
#         register_form = ProductCategoryEditForm()
#     content = {
#         'title': 'админка/категории/новая категория',
#         'form': register_form
#     }
#     return render(request, 'adminapp/category_update.html', content)


class CategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:categories')
    form_class = ProductCategoryEditForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def category_update(request, pk):
#     edit_category = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin:category_update', args=[edit_category.pk]))
#     else:
#         edit_form = ProductCategoryEditForm(instance=edit_category)
#
#     content = {
#         'title': 'админка/категории/редактирование',
#         'form': edit_form
#     }
#     return render(request, 'adminapp/category_update.html', content)

class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('admin:categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def category_delete(request, pk):
#     category = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         category.is_active = False
#         category.save()
#         return HttpResponseRedirect(reverse('admin:categories'))
#
#     content = {'title': 'адиминка/пользователи/удаление',
#                'category_to_delete': category}
#
#     return render(request, 'adminapp/category_delete.html', content)


class ProductsListView(ListView):
    paginate_by = 2
    model = Product
    template_name = 'adminapp/products.html'

    def get_queryset(self):
        return Product.objects.filter(category__pk=self.kwargs['pk']).order_by('name')



    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def products(request, pk):
#     title = 'админка/продукт'
#
#     category = get_object_or_404(ProductCategory, pk=pk)
#     products_list = Product.objects.filter(category__pk=pk).order_by('name')
#
#     content = {
#         'title': title,
#         'category': category,
#         'objects': products_list,
#     }
#
#     return render(request, 'adminapp/products.html', content)

class ProductCreateView(CreateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    form_class = ProductEditForm
    success_url = reverse_lazy('admin:categories')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# def product_create(request, pk):
#     category_item = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         product_form = ProductEditForm(request.POST, request.FILES)
#         if product_form.is_valid():
#             product_form.save()
#             return HttpResponseRedirect(reverse('admin:products'))
#     else:
#         product_form = ProductEditForm()
#     content = {
#         'title': 'админка/продукты/новый продукт',
#         'form': product_form,
#         'category': category_item
#     }
#     return render(request, 'adminapp/product_update.html', content)


class ProductReadView(DetailView):
    model = Product
    template_name = 'adminapp/product_detail.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# def product_read(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     content = {
#         'title': 'админка/продукты',
#         'object': product
#     }
#     return render(request, 'adminapp/product_detail.html', content)


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    form_class = ProductEditForm

    def get_success_url(self):
        category = self.get_object().category_id
        return reverse_lazy('admin:products', kwargs={'pk': category})

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# def product_update(request, pk):
#     product_item = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         edit_form = ProductEditForm(request.POST, request.FILES, instance=product_item)
#         if edit_form.is_valid():
#             product_item.is_active = True
#             edit_form.save()
#             return HttpResponseRedirect(reverse('admin:products', args=[product_item.category.pk]))
#     else:
#         edit_form = ProductEditForm(instance=product_item)
#     content = {
#         'title': 'админка/продукты/изменить продукт',
#         'form': edit_form,
#         'category': product_item.category
#     }
#     return render(request, 'adminapp/product_update.html', content)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'

    def get_success_url(self):
        category = self.get_object().category_id
        return reverse_lazy('admin:products', kwargs={'pk': category})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

# def product_delete(request, pk):
#     product_item = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         product_item.is_active = False
#         product_item.save()
#         return HttpResponseRedirect(reverse('admin:products', args=[product_item.category.pk]))
#
#     content = {
#         'title': 'адиминка/продукты/удаление',
#         'product_to_delete': product_item,
#         'category': product_item.category
#     }
#     return render(request, 'adminapp/product_delete.html', content)
