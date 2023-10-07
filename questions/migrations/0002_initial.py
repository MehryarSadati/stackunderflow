# Generated by Django 4.1.4 on 2023-09-28 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("questions", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="downvoters",
            field=models.ManyToManyField(
                related_name="downvoted_questions", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="tags",
            field=models.ManyToManyField(to="questions.tag"),
        ),
        migrations.AddField(
            model_name="question",
            name="upvoters",
            field=models.ManyToManyField(
                related_name="upvoted_questions", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="question",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="answer",
            name="downvoters",
            field=models.ManyToManyField(
                related_name="downvoted_answers", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="answer",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="questions.question"
            ),
        ),
        migrations.AddField(
            model_name="answer",
            name="upvoters",
            field=models.ManyToManyField(
                related_name="upvoted_answers", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="answer",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
