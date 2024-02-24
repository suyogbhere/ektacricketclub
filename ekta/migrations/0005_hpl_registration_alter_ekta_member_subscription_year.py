# Generated by Django 4.2.7 on 2024-02-24 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ekta', '0004_annual_function_alter_annual_meeting_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hpl_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=200)),
                ('DOB', models.DateField(max_length=100)),
                ('contact', models.CharField(blank=True, max_length=50)),
                ('player_skill', models.CharField(choices=[('फलंदाज', 'फलंदाज'), ('गोलंदाज', 'गोलंदाज'), ('अष्टपैलू', 'अष्टपैलू'), ('यष्टिरक्षक', 'यष्टिरक्षक')], max_length=100)),
                ('t_shirt_Size', models.IntegerField()),
                ('money_status', models.CharField(choices=[('PAID', 'PAID'), ('UNPAID', 'UNPAID')], default='UNPAID', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='ekta_member_subscription',
            name='Year',
            field=models.IntegerField(choices=[(2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)], default=2024, verbose_name='year'),
        ),
    ]