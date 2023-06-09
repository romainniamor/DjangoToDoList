# Generated by Django 4.1 on 2023-04-21 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_task_options_alter_task_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='todo.category'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
