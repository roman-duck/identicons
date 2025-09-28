import unittest
import identidock

class TestCase(unittest.TestCase):
    def setUp(self):
        identidock.app.config['TESTING'] = True
        self.app = identidock.app.test_client()

    def test_get_main_page(self):
        response = self.app.post('/', data=dict(name='Test User'))
        assert response.status_code == 200
        assert 'Hello' in str(response.data)
        assert 'Test User' in str(response.data)

    def test_html_escaping(self):
        response = self.app.post('/', data=dict(name='"><b>TEST</b><!--'))
        assert '<b>' not in str(response.data)

if __name__ == '__main__':
    unittest.main()
