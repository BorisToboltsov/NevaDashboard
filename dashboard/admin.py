from django.contrib import admin
from .models import CatalogName, CatalogData, Contact, RegistrySendingTravelAgency, RegistryTransportOrganizations, RegistryFoodOrganizations, RegistryHotels, RegistryMuseum, Group, GroupMuseum, GroupHotel, GroupTransport, GroupFood

# Register your models here.

admin.site.register(CatalogName)
admin.site.register(CatalogData)
admin.site.register(Contact)
admin.site.register(RegistrySendingTravelAgency)
admin.site.register(RegistryTransportOrganizations)
admin.site.register(RegistryFoodOrganizations)
admin.site.register(RegistryHotels)
admin.site.register(RegistryMuseum)
# admin.site.register(EmployeeData)
admin.site.register(Group)
admin.site.register(GroupMuseum)
admin.site.register(GroupHotel)
admin.site.register(GroupTransport)
admin.site.register(GroupFood)
