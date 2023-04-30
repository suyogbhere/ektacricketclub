# Generated by Django 4.1.5 on 2023-02-09 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Birthday_Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.ImageField(upload_to='Birthday_photo')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=50)),
                ('Subject', models.CharField(max_length=200)),
                ('Message', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Cricket_Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Discription', models.CharField(blank=True, max_length=200)),
                ('Photo', models.ImageField(upload_to='Ekta_Boys_photo')),
            ],
        ),
        migrations.CreateModel(
            name='Cultural_photo_upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.ImageField(upload_to='Cultural_photo')),
                ('Discription', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Educational_photo_upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.ImageField(upload_to='Educational_photo')),
                ('Discription', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EktaMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Social_photo_upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.ImageField(upload_to='Social_photo')),
                ('Discription', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ekta_Member_Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subscription', models.IntegerField()),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Year', models.IntegerField(choices=[(1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)], default=2023, verbose_name='year')),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ekta.ektamember')),
            ],
        ),
    ]