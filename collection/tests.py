from django.test import TestCase

class CollectionTest(TestCase): 
	def test_index(self):
		r = self.client.get('/') 
		
	def test_no_logic_page(self):
		r = self.client.get('/about/') 
		self.assertEqual(r.status_code, 200)
