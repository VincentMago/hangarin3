from django.core.management.base import BaseCommand
from hangarincore.models import Category, Priority, Task, SubTask, Note
from faker import Faker
from django.utils import timezone
import random

class Command(BaseCommand):
    help = "Populate initial data for Hangarin app"

    def handle(self, *args, **kwargs):
        fake = Faker()

        categories = ["Work", "School", "Personal", "Finance", "Projects"]
        for c in categories:
            Category.objects.get_or_create(name=c)

        priorities = ["High", "Medium", "Low", "Critical", "Optional"]
        for p in priorities:
            Priority.objects.get_or_create(name=p)

        all_categories = list(Category.objects.all())
        all_priorities = list(Priority.objects.all())

        for _ in range(10):
            task = Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                category=random.choice(all_categories),
                priority=random.choice(all_priorities),
            )

            for _ in range(2):
                SubTask.objects.create(
                    title=fake.sentence(nb_words=3),
                    status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                    parent_task=task,
                )

            Note.objects.create(
                task=task,
                content=fake.paragraph(nb_sentences=2),
            )

        self.stdout.write(self.style.SUCCESS("Successfully populated initial data"))
