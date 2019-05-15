from django.test import TestCase
# from .models import DanceGenre

# Create your tests here.
class DanceGenreTest(TestCase):
    
    def testCanCreateDanceGenre(self):
        a = DanceGenre(name="House")
        a.save()
        
        b = DanceGenre.objects.all().get(pk=a.id)
        print(b)
        self.assertEquals(a.name, b.name)
        self.assertEquals(a.id, b.id)