from django import forms
from .models import *


class SliderForm(forms.ModelForm):
    name_uz = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Slicer name uz",
                "class": "form-control"
            }
        ))

    name_ru = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Slicer name ru",
                "class": "form-control"
            }
        ))
    name_en = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Slicer name en",
                "class": "form-control"
            }
        ))
    image = forms.ImageField(
      widget=forms.FileInput()
    )
    description_uz = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "description_uz",
                "class": "form-control"
            }
        ))

    description_ru = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "description_ru",
                "class": "form-control"
            }
        ))
    description_en = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "description_en",
                "class": "form-control"
            }
        ))
    class Meta:
        model = Slider
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    name_uz = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Category name uz",
                "class": "form-control"
            }
        ))

    name_ru = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Category name  ru",
                "class": "form-control"
            }
        ))
    name_en = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Category name en",
                "class": "form-control"
            }
        ))
    image = forms.ImageField(
      widget=forms.FileInput()
    )
    class Meta:
        model = Category
        fields = "__all__"



class BrandForm(forms.ModelForm):
    name_uz = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Brand name uz",
                "class": "form-control"
            }
        ),
        required=False,
        )

    name_ru = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Brand name  ru",
                "class": "form-control"
            }
        ),
        required=False,
        )
    name_en = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Brand name en",
                "class": "form-control"
            }
        ),
        required=False,
        )
    image = forms.ImageField(
      widget=forms.FileInput()
    )
    
    class Meta:
        model = Brand
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    name_uz = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Category name uz",
                "class": "form-control"
            }
        ))

    name_ru = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Category name  ru",
                "class": "form-control"
            }
        ))
    name_en = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Category name en",
                "class": "form-control"
            }
        ))
    image = forms.ImageField(
      widget=forms.FileInput()
    )
    class Meta:
        model = Category
        fields = "__all__"



class TypeForm(forms.ModelForm):
    name_uz = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Type name uz",
                "class": "form-control"
            }
        ),
        required=False,
        )

    name_ru = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Type name  ru",
                "class": "form-control"
            }
        ),
        required=False,
        )
    name_en = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Type name en",
                "class": "form-control"
            }
        ),
        required=False,
        )
    image = forms.ImageField(
      widget=forms.FileInput()
    )
    
    class Meta:
        model = Type
        fields = "__all__"



class ProductForm(forms.ModelForm):
    name_uz = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Mahsulot nomi uz",
                "class": "form-control"
            }
        ),
        required=False,
        )

    name_ru = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Mahsulot nomi  ru",
                "class": "form-control"
            }
        ),
        required=False,
        )
    description_uz = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Mahsulot izohi uz",
                "class": "form-control"
            }
        ),
        required=False,
        )
    description_ru = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Mahsulot izohi ru",
                "class": "form-control"
            }
        ),
        required=False,
        )
    description_en = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Mahsulot izohi en",
                "class": "form-control"
            }
        ),
        required=False,
        )
    category = forms.ModelChoiceField(
        widget=forms.Select(),
        queryset=Category.objects.all())
    brand = forms.ModelChoiceField(queryset=Brand.objects.all())
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=False)
    name_en = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Mahsulot nomi en",
                "class": "form-control"
            }
        ),
        required=False,
        )
    price = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        ),
        required=True,
        )
    characteristic_uz = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Mahsulot xarakteristikasi uz",
                "class": "form-control"
            }
        ),
        required=False,
        )
    characteristic_ru = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Mahsulot xarakteristikasi ru",
                "class": "form-control"
            }
        ),
        required=False,
        )
    characteristic_en = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Mahsulot xarakteristikasi en",
                "class": "form-control"
            }
        ),
        required=False,
        )
    
    class Meta:
        model = Product
        fields = ["name_uz", "name_ru", "name_en", "price", "description_uz", "description_ru", "description_en", "category", "brand", "type", "characteristic_uz", "characteristic_ru", "characteristic_en"]


class ColorForm(forms.ModelForm):
    color_en = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Rang nomi En",
                "class": "form-control"
            }
        ))
    color_uz = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Rang nomi Uz",
                "class": "form-control"
            }
        ))
    color_ru = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Rang nomi Ru",
                "class": "form-control"
            }
        ))
    image1 = forms.ImageField(
      widget=forms.FileInput()
    )

    # product = forms.ModelChoiceField(queryset=Product.objects.all())
    
    class Meta:
        model = Color
        fields = ["color_en", "color_uz", "color_ru", "image1"]
        # fields = "__all__"

