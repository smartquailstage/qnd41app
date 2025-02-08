import csv
import datetime
from django.contrib import admin
from django.http import HttpResponse
from sbmorders.models import Order, OrderItem, BankTransfer
from .models import SBMStaffItem,SBMTechnologiesItem
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Category,SBMProduct,SBMProductManual,ManualItem, SBMStaffItem,SBMTechnologiesItem
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import ArrayWidget, WysiwygWidget
from unfold.contrib.filters.admin import TextFilter, FieldTextFilter
from django.core.validators import EMPTY_VALUES
from django.utils.translation import gettext_lazy as _
from unfold.contrib.filters.admin import (
    AutocompleteSelectFilter,
    AutocompleteSelectMultipleFilter
)


class CustomTextFilter(TextFilter):
    title = "Categorias de productos"
    parameter_name = "query_param_in_uri"

    def queryset(self, request, queryset):
        if self.value() not in EMPTY_VALUES:
            # Here write custom query
            return queryset.filter(your_field=self.value())

        return queryset


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

        # Display fields in changeform in compressed mode
    compressed_fields = True  # Default: False

    # Warn before leaving unsaved changes in changeform
    warn_unsaved_form = True  # Default: False

    # Preprocess content of readonly fields before render
    readonly_preprocess_fields = {
        "model_field_name": "html.unescape",
        "other_field_name": lambda content: content.strip(),
    }

    # Display submit button in filters
    list_filter_submit = True

    # Display changelist in fullwidth
    list_fullwidth = True

    # Set to False, to enable filter as "sidebar"
    list_filter_sheet = False

    list_filter_submit = True  # Submit button at the bottom of the filter
    list_filter = [
        ("name", FieldTextFilter),
        CustomTextFilter
    ]

    # Position horizontal scrollbar in changelist at the top
    list_horizontal_scrollbar_top = True

    # Dsable select all action in changelist
    list_disable_select_all = True

    # Custom actions
    actions_list = []  # Displayed above the results list
    actions_row = []  # Displayed in a table row in results list
    actions_detail = []  # Displayed at the top of for in object detail
    actions_submit_line = []  # Displayed near save in object detail

    # Changeform templates (located inside the form)
    #change_form_before_template = "some/template.html"
    #change_form_after_template = "some/template.html"

    # Located outside of the form
    #change_form_outer_before_template = "some/template.html"
    #change_form_outer_after_template = "some/template.html"

    # Display cancel button in submit line in changeform
    change_form_show_cancel_button = True # show/hide cancel button in changeform, default: False

    #formfield_overrides = {
    #    models.TextField: {
    #        "widget": WysiwygWidget,
    #    },
    #    ArrayField: {
    #        "widget": ArrayWidget,
    #    }
    #}
 

class SBMStaffItemInline(admin.TabularInline):
    model = SBMStaffItem

class SBMTechnologiesItemInline(admin.TabularInline):
    model = SBMTechnologiesItem


@admin.register(SBMProduct)
class SBMProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [SBMStaffItemInline,SBMTechnologiesItemInline]




@admin.register(SBMTechnologiesItem)
class SBMTechnologiesItemAdmin(admin.ModelAdmin):
    list_display = ['id', ]

@admin.register(SBMStaffItem)
class SBMStaffItemAdmin(admin.ModelAdmin):
    list_display = ['id', ]
 
    




def manual_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(
        reverse('sbmshop:admin_product_manual_pdf', args=[obj.id])))
manual_pdf.short_description = 'Manual' 

class ManualItemInline(admin.TabularInline):
    model = ManualItem
 

@admin.register(SBMProductManual)
class SBMProductManualAdmin(admin.ModelAdmin):
    list_display = ['product', 'category',manual_pdf]
    inlines = [ManualItemInline]






