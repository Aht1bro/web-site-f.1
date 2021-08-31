from PIL import Image

from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *



   
        # if not self.cleaned_data['sd']:
        #     self.cleaned_data['sd_volume_max'] = None
        # return self.cleaned_data




class СвитшотыAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(). __init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
             """<span style="color:red; font-size:14px;">Загружайте изображения с минимальным разрешением {}x{}</span>'
             """.format(
                *Product.MIN_RESOLUTION
        )
    )
    # def clean_image(self):
    #    image = self.cleaned_data['image']
    #    img = Image.open(image)
    #    min_height, min_width = Product.MIN_RESOLUTION
    #    if img.height < min_height or img.width < min_width:
    #         raise ValidationError('Разрешение изображение меньше минимального!')
    #    return image

   
class SweatshirtAdmin(admin.ModelAdmin):

    form = СвитшотыAdminForm

    # change_form_template = 'admin.html'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='sweatshirts'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class HoodieAdmin(admin.ModelAdmin):

    # change_form_template = 'admin.html'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='hoodies'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class T_shirtAdmin(admin.ModelAdmin):

    # change_form_template = 'admin.html'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='t_shirts'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class HeaddressAdmin(admin.ModelAdmin):

    # change_form_template = 'admin.html'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='headdresss'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class ShoeAdmin(admin.ModelAdmin):

    # change_form_template = 'admin.html'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='shoes'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class CoverAdmin(admin.ModelAdmin):

    # change_form_template = 'admin.html'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='covers'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)




admin.site.register(Category)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Sweatshirt, SweatshirtAdmin)
admin.site.register(Hoodie, HoodieAdmin)
admin.site.register(T_shirt, T_shirtAdmin)
admin.site.register(Headdress, HeaddressAdmin)
admin.site.register(Shoe, ShoeAdmin)
admin.site.register(Cover, CoverAdmin)
admin.site.register(Order)
