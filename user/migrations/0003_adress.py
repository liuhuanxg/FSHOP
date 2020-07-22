# Generated by Django 2.1.8 on 2019-12-24 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20191213_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25, verbose_name='收货人姓名')),
                ('userphone', models.CharField(max_length=20, verbose_name='收货人电话')),
                ('address', models.CharField(max_length=255, verbose_name='详细地址')),
                ('isdefault', models.BooleanField(default=0, verbose_name='是否默认地址')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='买家')),
            ],
            options={
                'verbose_name_plural': '收获地址',
                'verbose_name': '收获地址',
            },
        ),
    ]