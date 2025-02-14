from blog.models import Category
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help ="This Command inserts post data"

    def handle(self, *args:any,**options:any):
        
        #Delete Existing Data
        Category.objects.all().delete()

        categories = [
            'Education',
            'Technology',
            'Commerce',
            'Entertainment'
        ]


        
        for category in categories:
            Category.objects.create(name=category)

        self.stdout.write(self.style.SUCCESS("Completed inserting data"))