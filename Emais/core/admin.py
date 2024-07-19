from django.contrib import admin
from .models import Product
from patient.models import PatientProfile
from doctor.models import DoctorProfile
from administrator.models import AdministratorProfile

admin.site.site_header="My Django App"
admin.site.site_title="Title of Django"
admin.site.site_header="My admin"

class ProductAdmin(admin.ModelAdmin):
  list_display=('name', 'price','description')
  search_fields=("name",)
  list_editable=('price','description')
  actions=('make_zero',)

  def make_zero(self, request, queryset):
    queryset.update(price=0)

admin.site.register(Product, ProductAdmin)

admin.site.register(PatientProfile)
admin.site.register(DoctorProfile)
admin.site.register(AdministratorProfile)