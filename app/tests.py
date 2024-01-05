import json
import unittest
import subprocess

from app import app


class FlaskAPITests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_personal(self):
        response = self.app.get('/personal')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertEqual(data['full_name'], 'Andrei Colhon')
        self.assertEqual(data['phone'], '0746488744')
        self.assertEqual(data['email'], 'andreicolhon28@gmail.com')

    def test_get_experience(self):
        response = self.app.get('/experience')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['company'], 'IBM')
        self.assertEqual(data[0]['job_title'], 'Python Engineer')
        self.assertEqual(data[0]['start_date'], 'August 2022')
        self.assertEqual(data[0]['end_date'], 'Present')
        self.assertEqual(data[1]['company'], 'Broadridge')
        self.assertEqual(data[1]['title'], 'Implementation Engineer')
        self.assertEqual(data[1]['start_date'], 'August 2020')
        self.assertEqual(data[1]['end_date'], 'September 2021')

    def test_get_education(self):
        response = self.app.get('/education')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertEqual(len(data), 2)

    def test_export_cv_command(self):
        result = subprocess.run(['flask', 'export-cv', 'personal_info'], stdout=subprocess.PIPE, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('Andrei Colhon', result.stdout)
        self.assertIn('0746488744', result.stdout)
        self.assertIn('andreicolhon28@gmail.com', result.stdout)

    def test_export_cv_experience_command(self):
        result = subprocess.run(['flask', 'export-cv', 'experience'], stdout=subprocess.PIPE, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('IBM', result.stdout)
        self.assertIn('Python Engineer', result.stdout)
        self.assertIn('August 2022', result.stdout)
        self.assertIn('Present', result.stdout)
        self.assertIn('Implementation Engineer', result.stdout)

    def test_export_cv_education_command(self):
        result = subprocess.run(['flask', 'export-cv', 'education'], stdout=subprocess.PIPE, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn('BBU', result.stdout)
        self.assertIn('High Performance Computing', result.stdout)
        self.assertIn('Rotterdam School of Management', result.stdout)
        self.assertIn('Business Analytics and Management', result.stdout)


if __name__ == '__main__':
    unittest.main()
