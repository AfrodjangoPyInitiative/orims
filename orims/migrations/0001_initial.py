# Generated by Django 2.0.2 on 2018-07-17 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('systemAdmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_name', models.CharField(max_length=30)),
                ('branch_level', models.CharField(choices=[('main', 'Main Branch'), ('other', 'Other Branch')], default='other', max_length=15)),
                ('registration_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'Branch',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=15)),
                ('office_number', models.CharField(blank=True, max_length=15)),
                ('fax_number', models.CharField(blank=True, max_length=15)),
                ('email_address', models.EmailField(blank=True, max_length=150, null=True)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orims.Branch', verbose_name='Branch')),
            ],
            options={
                'db_table': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.CharField(max_length=512, primary_key=True, serialize=False)),
                ('department_name', models.CharField(max_length=50)),
                ('department_description', models.TextField(max_length=1024, verbose_name='Description')),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orims.Branch', verbose_name='Branch')),
            ],
            options={
                'db_table': 'Department',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=15)),
                ('county', models.CharField(blank=True, max_length=15, null=True)),
                ('sub_county', models.CharField(blank=True, max_length=15, null=True)),
                ('parish', models.CharField(blank=True, max_length=15, null=True)),
                ('town', models.CharField(max_length=15)),
                ('zone', models.CharField(blank=True, max_length=15, null=True)),
                ('plot_no', models.CharField(blank=True, max_length=15, null=True)),
                ('building', models.CharField(blank=True, max_length=15, null=True)),
                ('unique_direction', models.CharField(blank=True, max_length=150, null=True)),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orims.Branch', verbose_name='Branch')),
            ],
            options={
                'db_table': 'Location',
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('office_id', models.CharField(max_length=512, primary_key=True, serialize=False)),
                ('office_name', models.CharField(max_length=50)),
                ('office_description', models.TextField(max_length=1024)),
                ('office_working_time', models.CharField(choices=[('default', 'Standard Working Dime and Days'), ('custom', 'Set Custom Working Time for office')], default='default', max_length=30)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orims.Department', verbose_name='Department')),
            ],
            options={
                'db_table': 'Office',
            },
        ),
        migrations.CreateModel(
            name='ServiceUnit',
            fields=[
                ('unit_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Service Unit ID')),
                ('unit_name', models.CharField(max_length=30, verbose_name='Service Unit name')),
                ('unit_type', models.CharField(choices=[('select', 'Select Type of service unit'), ('min', 'Ministry'), ('org', 'Organization'), ('firm', 'Firm'), ('other', 'Others')], default='select', max_length=15, verbose_name='Service Unit type')),
                ('unit_description', models.TextField(max_length=1024)),
                ('unit_logo', models.FileField(max_length=500, upload_to='uploads/ServiceUnit/logo')),
                ('unit_featured_image', models.FileField(max_length=500, upload_to='uploads/ServiceUnit/logo')),
                ('unit_cover_photo', models.FileField(max_length=500, upload_to='uploads/ServiceUnit/logo')),
                ('system_admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systemAdmin.SystemAdmin', verbose_name='System Administrator')),
            ],
            options={
                'db_table': 'ServiceUnit',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('staff_first_name', models.CharField(max_length=15, verbose_name='First Name')),
                ('staff_last_name', models.CharField(max_length=15, verbose_name='Last Name')),
                ('staff_profile_photo', models.CharField(blank=True, max_length=512, null=True, verbose_name='Profile Photo')),
                ('staff_designation', models.CharField(choices=[('Official', 'Official'), ('receptionist', 'Receptionist'), ('select', 'Select Staff Designation')], default='select', max_length=15, verbose_name='Designation')),
                ('about_staff', models.TextField(blank=True, max_length=512, null=True)),
                ('office_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orims.Office', verbose_name='Office')),
            ],
        ),
        migrations.CreateModel(
            name='WorkingTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_day', models.CharField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday'), ('non', 'Select Week Day')], default='non', max_length=3)),
                ('work_start_time', models.TimeField(default='08:00:00')),
                ('work_end_time', models.TimeField(default='17:00:00')),
                ('office_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orims.Office', verbose_name='Office')),
            ],
            options={
                'db_table': 'WorkingTime',
            },
        ),
        migrations.AddField(
            model_name='branch',
            name='unit_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orims.ServiceUnit', verbose_name='Service unit'),
        ),
    ]
