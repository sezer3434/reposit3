from django.db import models

# Create your models here.
from django.db import models

from smart_selects.db_fields import ChainedForeignKey

########################################################################################################################
#ADDRES & CONTACT
class CityModel(models.Model):
    order = models.IntegerField(verbose_name="Order No")
    name = models.CharField(max_length=255, verbose_name="City")
    coordinates = models.TextField(verbose_name="Coordinate", null=True, blank=True)

    class Meta:
        verbose_name_plural = "1 - Cities"
        verbose_name = "City"
        ordering = ['name']

    def __str__(self):
        return self.name

class DistrictModel(models.Model):
    city = models.ForeignKey(CityModel, verbose_name="City", on_delete=models.CASCADE)
    order = models.IntegerField(verbose_name="Order No")
    name = models.CharField(max_length=255, verbose_name="District")
    coordinates = models.TextField(verbose_name="Coordinate", null=True, blank=True)

    class Meta:
        verbose_name_plural = "2 - Districtes"
        verbose_name = "District"
        ordering = ['city__name', 'name']

    def __str__(self):
        return "{0} - {1}".format(
            self.city.name,
            self.name,
        )

class QuarterModel(models.Model):
    city = models.ForeignKey(CityModel, verbose_name="Quarter", default="", on_delete=models.CASCADE)
    district = models.ForeignKey(DistrictModel, verbose_name="District", null=True, on_delete=models.CASCADE)
    order = models.IntegerField(verbose_name="OrderNo")
    name = models.CharField(max_length=255, verbose_name="Quarter")
    coordinates = models.TextField(verbose_name="Coordinate", null=True, blank=True)

    class Meta:
        verbose_name_plural = "3 - Quarters"
        verbose_name = "Quarter"
        ordering = ['district__name', 'name']

    def __str__(self):
        return "{0} - {1} - {2}".format(
            self.district.city.name,
            self.district.name,
            self.name,
        )

class StreetModel(models.Model):
    city = models.ForeignKey(CityModel, verbose_name="City", null=True, on_delete=models.CASCADE)
    district = models.ForeignKey(DistrictModel, verbose_name='District',on_delete=models.CASCADE)
    quarter = models.ForeignKey(QuarterModel, verbose_name="Quarter",on_delete=models.CASCADE)
    order = models.IntegerField(verbose_name="OrderNo")
    name = models.CharField(max_length=255, verbose_name="Street")

    class Meta:
        verbose_name_plural = "4 - Streets"
        verbose_name = "Street"
        ordering = ['quarter__name', 'name']

    def __str__(self):
        return "{0} - {1} - {2} - {3}".format(
            self.city.name,
            self.district.name,
            self.quarter.name,
            self.name,
        )

class AddressModel(models.Model):
    city = models.ForeignKey(CityModel, verbose_name='City', on_delete=models.DO_NOTHING)
    district = models.ForeignKey(DistrictModel, verbose_name='District', on_delete=models.DO_NOTHING)
    quarter = models.ForeignKey(QuarterModel, verbose_name='Quarter', on_delete=models.CASCADE,default='')
    street = models.ForeignKey(StreetModel, verbose_name='Street', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "Adresses"
        verbose_name = "Address"

    def __str__(self):
        return str(self.street)


class ContactModel(models.Model):
    mobile = models.CharField(max_length=10, verbose_name='Your Mobile')
    email = models.EmailField(verbose_name='E Mail', max_length=100)
    website = models.URLField(verbose_name='Web', max_length=100)

    class Meta:
        verbose_name_plural = 'Contacts'
        verbose_name = 'Contact'

    def __str__(self):
        return str(self.mobile) + '-' + str(self.email)

########################################################################################################################
#COMPANY
class BankModel(models.Model):
    name = models.CharField(verbose_name='Bank Name',max_length=50)
    branch = models.CharField(verbose_name='Branch',max_length=50)
    account = models.TextField(verbose_name='Pay No',max_length=255)

    class Meta:
        verbose_name_plural = 'Bank Contacts'
        verbose_name = 'Bank Contact'

    def __str__(self):
        return self.name + self.branch

class IndustryModel(models.Model):
    parent = models.ForeignKey('company.IndustryModel',verbose_name='Industry',blank=True, null=True,on_delete=models.DO_NOTHING)
    name = models.CharField(verbose_name='Type',max_length=100)

    class Meta:
        verbose_name_plural='Industries'
        verbose_name = 'Industry'

    def __str__(self):
        if self.parent:
            return "{}-{}".format(self.parent.name, self.name)
        else:
            return "{}".format(self.name)


class TaxModel(models.Model):
    administration = models.CharField(verbose_name='Tax Administration',max_length=100)
    taxNo = models.BigIntegerField(verbose_name='Tax No')


    class Meta:
        verbose_name_plural = 'All Tax'
        verbose_name = 'Tax'

    def __str__(self):
        return str(self.taxNo)+ '-'+self.administration


########################################################################################################################
#1------------------------------------------------------------------------
class DepartmentModel(models.Model):
    name = models.CharField(max_length=50,verbose_name='Departmen')
    #fore = models.ForeignKey('employeapp.Manager',on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Departments'
        verbose_name = 'Department'

    def __str__(self):
        return self.name

class CompanyModel(models.Model):
    name    = models.CharField(max_length=50,verbose_name='Company ')
    address = models.ForeignKey(AddressModel,verbose_name='Address',on_delete=models.CASCADE)
    bank    = models.ForeignKey(BankModel,max_length=250,verbose_name='Bank Info',on_delete=models.CASCADE)
    industry = models.ForeignKey(IndustryModel,verbose_name='Industry',on_delete=models.CASCADE)
    tax      = models.ForeignKey(TaxModel,verbose_name='Tax',on_delete=models.CASCADE)
    company_reference= models.IntegerField(verbose_name='Reference')
    #company_logo = models.ImageField('/...')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Firms'
        verbose_name = 'Firm'

########################################################################################################################
#PRICE
class PriceModel(models.Model):
    daily_wage = models.FloatField(verbose_name='Unit Cost')

    class Meta:
        verbose_name_plural='Costs'
        verbose_name = 'Cost'

    def __str__(self):
        return str(self.daily_wage)

########################################################################################################################
#SERVICE
#---------------------------
class EditToolModel(models.Model):
    name = models.CharField(verbose_name='Tool', max_length=100)

    class Meta:
        verbose_name_plural = 'Tools'
        verbose_name = 'Tool'

    def __str__(self):
        return self.name

#---------------------------
class TechnologyModel(models.Model):
    parent = models.ForeignKey('company.TechnologyModel', verbose_name='Parent', blank=True, null=True,
                               on_delete=models.DO_NOTHING)
    name = models.CharField(verbose_name='Technology', max_length=100)

    class Meta:
        verbose_name_plural = 'Technologies'
        verbose_name = 'Technology'

    def __str__(self):
        return self.name

class ServiceModel(models.Model):
    #hizmetin adi
    name = models.CharField(verbose_name='Service',max_length=100)
    technologies = models.ManyToManyField(TechnologyModel,verbose_name='Technologies')
    tools = models.ManyToManyField(EditToolModel, verbose_name='Tools')
    department = models.ForeignKey(DepartmentModel,verbose_name='Department',on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Services'
        verbose_name = 'Service'

    def __str__(self):
        return self.name+' '+str(self.department)

########################################################################################################################
#COMPANY


#9---------OrderModel--------------------------------------------
class OrderModel(models.Model):
    orderType = models.IntegerField(verbose_name='Order type')

    def __str__(self):
        return str(self.orderType)

    class Meta:
        verbose_name_plural='Orders'
        verbose_name = 'Ordre'

#10----------------------------------------------------------------


########################################################################################################################
#------------------------------------------------------------------
class EmployeeModel(models.Model):
    emp_firstname=models.CharField(max_length=50,verbose_name='Fisrt Name')
    emp_lastname=models.CharField(max_length=50,verbose_name='Last Name')
    #her calisan bir veya daha fazla birimde calÄ±sabilir
    department = models.ForeignKey(DepartmentModel,verbose_name='Department',on_delete=models.CASCADE)
    #her calÄ±san sadece bir sirkette calÄ±sabilir
    company    = models.ForeignKey(CompanyModel,on_delete=models.CASCADE,verbose_name='Company')
    #her calisanin calÄ±sma ucreti farkli olsun
    price = models.OneToOneField(PriceModel,on_delete=models.CASCADE,verbose_name='Price')
    service = models.ManyToManyField(ServiceModel,verbose_name='Services')


    class Meta:
        verbose_name_plural='Employees'
        verbose_name = 'Employee'

    def __str__(self):
        return self.emp_firstname+ ' '+self.emp_lastname
