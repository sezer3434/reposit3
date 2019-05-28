# Generated by Django 2.2.1 on 2019-05-28 11:33

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Adres',
                'verbose_name_plural': 'Adresler',
            },
        ),
        migrations.CreateModel(
            name='BankModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Banka')),
                ('branch', models.CharField(max_length=50, verbose_name='Sube')),
                ('account', models.TextField(max_length=255, verbose_name='Hesap No')),
            ],
            options={
                'verbose_name': 'Banka Hesabi',
                'verbose_name_plural': 'Banka Hesaplari',
            },
        ),
        migrations.CreateModel(
            name='CityModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name='Siparis')),
                ('name', models.CharField(max_length=255, verbose_name='Sehir Ad')),
                ('value', models.CharField(blank=True, max_length=255, verbose_name='Deger')),
                ('coordinates', models.TextField(blank=True, null=True, verbose_name='Koordinat')),
            ],
            options={
                'verbose_name': 'Sehir',
                'verbose_name_plural': '1 - Sehirler',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Sirket ')),
                ('company_reference', models.IntegerField(verbose_name='Referans')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.AddressModel', verbose_name='Adres')),
                ('bank', models.ForeignKey(max_length=250, on_delete=django.db.models.deletion.CASCADE, to='company.BankModel', verbose_name='Banka Hesap')),
            ],
            options={
                'verbose_name': 'Sirket',
                'verbose_name_plural': 'Sirketler',
            },
        ),
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.FloatField(max_length=10, verbose_name='Birim Fiyat')),
                ('email', models.EmailField(max_length=100, verbose_name='E posta')),
                ('website', models.URLField(max_length=100, verbose_name='web')),
            ],
            options={
                'verbose_name': 'iletisim',
                'verbose_name_plural': 'iletisim Bilgileri',
            },
        ),
        migrations.CreateModel(
            name='DepartmentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Departmen')),
            ],
            options={
                'verbose_name': 'Departman',
                'verbose_name_plural': 'Departmanlar',
            },
        ),
        migrations.CreateModel(
            name='DistrictModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name='Siparis')),
                ('name', models.CharField(max_length=255, verbose_name='Ilce')),
                ('value', models.CharField(max_length=255, null=True, verbose_name='Deger')),
                ('coordinates', models.TextField(blank=True, null=True, verbose_name='Koordinat')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.CityModel', verbose_name='City')),
            ],
            options={
                'verbose_name': 'Ilce',
                'verbose_name_plural': '2 - Ilceler',
                'ordering': ['city__name', 'name'],
            },
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderType', models.IntegerField(verbose_name='Teklif tipi')),
            ],
            options={
                'verbose_name': 'Teklif',
                'verbose_name_plural': 'Teklifler',
            },
        ),
        migrations.CreateModel(
            name='PriceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_wage', models.FloatField(verbose_name='Birim Fiyat')),
            ],
            options={
                'verbose_name': 'Fiyat',
                'verbose_name_plural': 'Fiyatlar',
            },
        ),
        migrations.CreateModel(
            name='QuarterModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name='Siparis')),
                ('name', models.CharField(max_length=255, verbose_name='Mahalle')),
                ('coordinates', models.TextField(blank=True, null=True, verbose_name='Kordinat')),
                ('city', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='company.CityModel', verbose_name='Sehir')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.DistrictModel', verbose_name='İlce')),
            ],
            options={
                'verbose_name': 'Mahalle',
                'verbose_name_plural': '3 - Mahalleler',
                'ordering': ['district__name', 'name'],
            },
        ),
        migrations.CreateModel(
            name='TaxModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administration', models.CharField(max_length=100, verbose_name='Vergi Dairesi')),
                ('taxNo', models.BigIntegerField(verbose_name='Vergi No')),
            ],
            options={
                'verbose_name': 'Vergi',
                'verbose_name_plural': 'Vergi Bilgileri',
            },
        ),
        migrations.CreateModel(
            name='StreetModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name='Siparis')),
                ('name', models.CharField(max_length=255, verbose_name='Sokak')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.CityModel', verbose_name='City')),
                ('district', smart_selects.db_fields.ChainedForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.DistrictModel', verbose_name='ilce')),
                ('quarter', smart_selects.db_fields.ChainedForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.QuarterModel', verbose_name='Mahalle')),
            ],
            options={
                'verbose_name': 'Sokak',
                'verbose_name_plural': '4 - Sokaklar',
                'ordering': ['quarter__name', 'name'],
            },
        ),
        migrations.CreateModel(
            name='ServiceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Hizmet')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.DepartmentModel', verbose_name='Departman')),
            ],
            options={
                'verbose_name': 'Hizmet',
                'verbose_name_plural': 'Hizmetler',
            },
        ),
        migrations.CreateModel(
            name='IndustryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Sektor Adi')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='company.IndustryModel', verbose_name='Ana Sektor')),
            ],
            options={
                'verbose_name': 'Sektor',
                'verbose_name_plural': 'Sektorler',
            },
        ),
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_firstname', models.CharField(max_length=50, verbose_name='Ad')),
                ('emp_lastname', models.CharField(max_length=50, verbose_name='Soyad')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.CompanyModel', verbose_name='Sirket')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.DepartmentModel', verbose_name='Departman')),
                ('price', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='company.PriceModel', verbose_name='Ucret')),
                ('service', models.ManyToManyField(to='company.ServiceModel', verbose_name='Service/Hizmet')),
            ],
            options={
                'verbose_name': 'Calisan',
                'verbose_name_plural': 'Calisanlar',
            },
        ),
        migrations.AddField(
            model_name='companymodel',
            name='industry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.IndustryModel'),
        ),
        migrations.AddField(
            model_name='companymodel',
            name='tax',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.TaxModel', verbose_name='Vergi Dairesi'),
        ),
        migrations.AddField(
            model_name='addressmodel',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company.CityModel', verbose_name='IL'),
        ),
        migrations.AddField(
            model_name='addressmodel',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company.DistrictModel', verbose_name='ILCE'),
        ),
        migrations.AddField(
            model_name='addressmodel',
            name='quarter',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='company.QuarterModel', verbose_name='MAHALLE'),
        ),
        migrations.AddField(
            model_name='addressmodel',
            name='street',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company.StreetModel', verbose_name='SOKAK'),
        ),
    ]
