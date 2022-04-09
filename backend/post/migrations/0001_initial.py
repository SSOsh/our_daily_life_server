# Generated by Django 4.0.3 on 2022-04-09 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commentId', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('sequence', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('followId', models.AutoField(primary_key=True, serialize=False)),
                ('follower', models.CharField(max_length=100)),
                ('following', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userName', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('statusMessage', models.CharField(max_length=200)),
                ('picture', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('postId', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=200)),
                ('picture', models.BinaryField()),
                ('userName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.user')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('likeId', models.AutoField(primary_key=True, serialize=False)),
                ('like', models.SmallIntegerField()),
                ('commentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.comment')),
                ('postId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='postId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post'),
        ),
    ]
