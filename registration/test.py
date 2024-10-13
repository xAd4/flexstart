from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from registration.models import Profile

User = get_user_model()

class ProfileTests(TestCase):
    
    def setUp(self):
        # Crear usuarios de prueba con perfiles
        self.user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="password123"
        )
        Profile.objects.create(user=self.user)
        
        self.user2 = User.objects.create_user(
            username="testuser2", email="testuser2@example.com", password="password123"
        )
        Profile.objects.create(user=self.user2)
        
        self.client.login(username="testuser", password="password123")

    def test_all_users_have_profiles(self):
        users = User.objects.all()
        for user in users:
            self.assertTrue(Profile.objects.filter(user=user).exists(), f"El usuario {user.username} no tiene un perfil asociado")

    def test_edit_email_view_access(self):
        response = self.client.get(reverse('profile-email'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/profile_edit_email.html')

    def test_edit_email_successful(self):
        new_email = "newemail@example.com"
        response = self.client.post(reverse('profile-email'), {
            'email': new_email,
        })
        self.user.refresh_from_db()  # Refresca el objeto usuario desde la base de datos
        self.assertEqual(self.user.email, new_email)
        self.assertRedirects(response, reverse('profile-demo'))  # Verifica la redirección

    def test_edit_email_duplicate(self):
        # Asegúrate de que el correo del usuario original es 'testuser@example.com'
        self.assertEqual(self.user.email, 'testuser@example.com')

        # Intenta cambiar el email a uno que ya existe
        response = self.client.post(reverse('profile-email'), {
            'email': 'testuser2@example.com',  # Este email ya existe
        }, follow=True)  # Seguir la redirección

        self.user.refresh_from_db()  # Refresca el objeto usuario desde la base de datos
        self.assertEqual(self.user.email, 'testuser@example.com')  # Asegúrate de que el email no cambie
        self.assertContains(response, "Email already exists")  # Verifica el mensaje de error


    def test_edit_email_invalid(self):
        response = self.client.post(reverse('profile-email'), {
            'email': 'invalidemail',  # Email inválido
        })
        self.user.refresh_from_db()
        self.assertNotEqual(self.user.email, 'invalidemail')
        self.assertFormError(response, 'form', 'email', "Enter a valid email address.")  # Verifica el error
