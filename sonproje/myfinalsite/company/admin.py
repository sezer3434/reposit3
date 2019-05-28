from django.contrib import admin
from .models import  IndustryModel,StreetModel,QuarterModel,DistrictModel,CityModel,AddressModel,OrderModel,CompanyModel,ChainedForeignKey
from .models import  ServiceModel,ContactModel,ChainedForeignKey,EmployeeModel,TaxModel,PriceModel,DepartmentModel,BankModel
from .models import EditToolModel,TechnologyModel
# Register your models here.
admin.site.register(IndustryModel)
admin.site.register(StreetModel)
admin.site.register(QuarterModel)
admin.site.register(DistrictModel)
admin.site.register(CityModel)
admin.site.register(AddressModel)
admin.site.register(OrderModel)
admin.site.register(CompanyModel)
admin.site.register(ContactModel)
admin.site.register(ServiceModel)
admin.site.register(EmployeeModel)
admin.site.register(TaxModel)
admin.site.register(PriceModel)
admin.site.register(DepartmentModel)
admin.site.register(BankModel)
admin.site.register(EditToolModel)
admin.site.register(TechnologyModel)