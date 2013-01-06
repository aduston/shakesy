from django.core.management.base import BaseCommand
from experiment_1 import models

class Command(BaseCommand):
    def handle(self, *args, **options):
        char_a = models.Character(
            name="A",
            title="Mr. A",
            description="Mr. A is cool")
        char_a.save()
        char_b = models.Character(
            name="B",
            title="Mr. B",
            description="Mr. B is cool")
        char_b.save()
        models.ContemporarySubtitle(
            text="a a a a a aaaa",
            character=char_a,
            start_time=1.3).save()
        models.ContemporarySubtitle(
            text="bbbba ba ba ba a aaaa",
            character=char_b,
            start_time=2.3).save()
