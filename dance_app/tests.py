from django.test import TestCase
from .models import DanceGenre

# Create your tests here.
class DanceGenreTest(TestCase):
    
    def testCanCreateDanceGenre(self):
        a = DanceGenre(name="House")
        print("a = ", a)
        print("a.name = ", a.name)
        a.save()
        
        b = DanceGenre.objects.all().get(pk=a.id)
        print("b = ", b)
        print("b.name = ", b.name)
        print("a.id = ", a.id)
        print("b.id = ", b.id)
        self.assertEquals(a.name, b.name)
        self.assertEquals(a.id, b.id)