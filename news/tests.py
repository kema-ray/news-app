from django.test import TestCase
from .models import Editor,Article,tags

# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.rachel= Editor(first_name = 'Rachel', last_name ='Oyondi', email ='rachel@moringaschool.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.rachel,Editor))

     # Testing Save Method
    def test_save_method(self):
        self.rachel.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

