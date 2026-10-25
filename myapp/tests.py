
from datetime import date
from django.test import TestCase
from myapp.models import Student


class StudentModelTest(TestCase):

    def test_student_creation(self):
        student = Student.objects.create(
            name="Test Student",
            age=22,
            dob=date(2004, 6, 15),
            email="test@example.com",
            place="Bengaluru"
        )

        self.assertEqual(student.name, "Test Student")
        self.assertEqual(student.age, 22)
        self.assertEqual(student.place, "Bengaluru")
        self.assertEqual(Student.objects.count(), 1)
    
    def test_student_retrieval(self):
        Student.objects.create(
            name="Ananya",
            age=21,
            dob=date(2005, 3, 10),
            email="ananya@example.com",
            place="Mysuru"
        )

        student = Student.objects.get(name="Ananya")

        self.assertEqual(student.email, "ananya@example.com")
        self.assertEqual(student.place, "Mysuru")
    
    def test_student_update(self):
        student = Student.objects.create(
            name="Ananya",
            age=21,
            dob=date(2005, 3, 10),
            email="ananya@example.com",
            place="Mysuru"
        )

        student.name = "Ananya Sharma"
        student.place = "Bengaluru"
        student.save()

        updated_student = Student.objects.get(id=student.id)

        self.assertEqual(updated_student.name, "Ananya Sharma")
        self.assertEqual(updated_student.place, "Bengaluru")

    
    def test_student_delete(self):
        student = Student.objects.create(
            name="Rahul",
            age=22,
            dob=date(2004, 5, 10),
            email="rahul@example.com",
            place="Bengaluru"
        )

        student_id = student.id

        # Delete the student
        student.delete()

        # Verify the student no longer exists
        self.assertFalse(
            Student.objects.filter(id=student_id).exists()
        )

        # Verify the database is empty
        self.assertEqual(Student.objects.count(), 0)

    
class StudentViewTest(TestCase):

    def test_dashboard_page_loads(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(
            response,
            'myapp/index.html'
        )
    
    def test_add_student(self):
        student_data = {
            'name': 'Priya',
            'age': 21,
            'dob': '2005-03-10',
            'email': 'priya@example.com',
            'place': 'Bengaluru'
        }

        response = self.client.post(
            '/insert/',
            data=student_data
        )

        self.assertEqual(response.status_code, 302)

        self.assertTrue(
            Student.objects.filter(
                name='Priya'
            ).exists()
        )
    
    def test_update_student(self):
        student = Student.objects.create(
            name="Priya",
            age=21,
            dob=date(2005, 3, 10),
            email="priya@example.com",
            place="Mysuru"
        )

        updated_data = {
            'name': 'Priya Sharma',
            'age': 22,
            'dob': '2005-03-10',
            'email': 'priya@example.com',
            'place': 'Bengaluru'
        }

        response = self.client.post(
            f'/update/{student.id}',
            data=updated_data
        )

        self.assertEqual(response.status_code, 302)

        student.refresh_from_db()

        self.assertEqual(student.name, 'Priya Sharma')
        self.assertEqual(student.age, 22)
        self.assertEqual(student.place, 'Bengaluru')

    
    def test_delete_requires_post(self):
        student = Student.objects.create(
            name="Rahul",
            age=22,
            dob=date(2004, 5, 10),
            email="rahul@example.com",
            place="Bengaluru"
        )

        # Opening the confirmation page must not delete
        response = self.client.get(
            f'/delete/{student.id}'
        )

        self.assertEqual(response.status_code, 200)

        self.assertTrue(
            Student.objects.filter(id=student.id).exists()
        )

        # Confirming deletion with POST should delete
        response = self.client.post(
            f'/delete/{student.id}'
        )

        self.assertEqual(response.status_code, 302)

        self.assertFalse(
            Student.objects.filter(id=student.id).exists()
        )

class StudentSearchTests(TestCase):

    def test_search_by_name(self):
        Student.objects.create(
            name="Aarav Sharma",
            age=22,
            dob=date(2004, 3, 15),
            email="aarav@example.com",
            place="Bengaluru"
        )

        response = self.client.get("/", {"q": "Aarav"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Aarav Sharma")
        self.assertEqual(response.context["matching_students"], 1)
    
    def test_sort_students_by_name_descending(self):
        Student.objects.create(
            name="Aarav",
            age=22,
            dob=date(2004, 3, 15),
            email="aarav@example.com",
            place="Bengaluru"
        )

        Student.objects.create(
            name="Zoya",
            age=23,
            dob=date(2003, 5, 20),
            email="zoya@example.com",
            place="Mysuru"
        )

        response = self.client.get("/", {"sort": "name_desc"})

        students = list(response.context["stud"])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(students[0].name, "Zoya")
        self.assertEqual(students[1].name, "Aarav")

    
    def test_student_pagination(self):
        for i in range(1, 7):
            Student.objects.create(
                name=f"Student {i}",
                age=20 + i,
                dob=date(2004, 1, 1),
                email=f"student{i}@example.com",
                place="Bengaluru"
            )

        response = self.client.get("/", {"page": 1})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["stud"]), 5)
        self.assertEqual(response.context["total_students"], 6)

        response = self.client.get("/", {"page": 2})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["stud"]), 1)
        self.assertEqual(response.context["page_obj"].number, 2)
