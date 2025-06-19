from django.core.management.base import BaseCommand, CommandError
from django_fakegen.registry import registry

class Command(BaseCommand):
    help = "Generate smart fake data for any Django model"

    def add_arguments(self, parser):
        parser.add_argument("model_label", type=str, help="app_label.ModelName")
        parser.add_argument(
            "--count", "-c", type=int, default=10, help="Number of instances"
        )

    def handle(self, *args, **options):
        label = options['model_label']
        count = options['count']
        try:
            registry.bulk_generate(label, count)
            self.stdout.write(self.style.SUCCESS(
                f"Successfully created {count} instances for {label}."
            ))
        except LookupError:
            raise CommandError(f"Model '{label}' not found.")
