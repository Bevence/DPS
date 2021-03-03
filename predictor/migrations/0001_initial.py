# Generated by Django 2.2.2 on 2020-11-25 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(max_length=6)),
                ('polyuria', models.CharField(max_length=3)),
                ('polydipsia', models.CharField(max_length=3)),
                ('weight_loss', models.CharField(max_length=3)),
                ('weakness', models.CharField(max_length=3)),
                ('polyphagia', models.CharField(max_length=3)),
                ('genital_thrush', models.CharField(max_length=3)),
                ('visual_blurring', models.CharField(max_length=3)),
                ('irritability', models.CharField(max_length=3)),
                ('partial_paresis', models.CharField(max_length=3)),
                ('muscle_stiffness', models.CharField(max_length=3)),
                ('alopecia', models.CharField(max_length=3)),
                ('result_random_forest', models.CharField(max_length=10)),
                ('result_decision_tree', models.CharField(max_length=10)),
                ('result_naive_bayes', models.CharField(max_length=10)),
                ('result_knn', models.CharField(max_length=10)),
                ('result_logistic_regression', models.CharField(max_length=10)),
                ('result_svm', models.CharField(max_length=10)),
            ],
        ),
    ]
