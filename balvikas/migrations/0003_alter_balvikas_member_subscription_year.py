# Generated by Django 4.2.7 on 2024-02-24 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balvikas', '0002_alter_balvikas_member_subscription_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balvikas_member_subscription',
            name='Year',
            field=models.IntegerField(choices=[(2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], default=2024, verbose_name='year'),
        ),
    ]
