# Generated by Django 3.0 on 2020-08-20 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DebugTalks',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('id', models.AutoField(help_text='id主键', primary_key=True, serialize=False, verbose_name='id主键')),
                ('name', models.CharField(default='debugtalk.py', help_text='debugtalk文件名称', max_length=200, verbose_name='debugtalk文件名称')),
                ('debugtalk', models.TextField(default='#debugtalk.py', help_text='debugtalk.py文件', null=True)),
                ('project', models.OneToOneField(help_text='所属项目', on_delete=django.db.models.deletion.CASCADE, related_name='debugtalks', to='projects.Projects')),
            ],
            options={
                'verbose_name': 'debugtalk.py文件',
                'verbose_name_plural': 'debugtalk.py文件',
                'db_table': 'tb_debugtalks',
            },
        ),
    ]
