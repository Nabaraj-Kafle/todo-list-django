# Generated by Django 5.2.dev20241203141516 on 2025-04-12 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('work', 'Work'), ('grocery', 'Grocery'), ('study', 'Study'), ('other', 'Other')], default='other', max_length=20),
        ),
    ]
