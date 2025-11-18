# test/test_auth.py
import pytest
import sys
import os


from microservicios.authentication.app import auth  # Asegúrate de que esta ruta sea correcta
from flask import Flask, jsonify
from microservicios.authentication.app.services import login_user  # Ajusta esta importación según tu lógica
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
# Aquí puedes configurar tu app de Flask si no tienes una instancia global
@pytest.fixture
def client():
    app = Flask(__name__)
    
    # Configura tu app si es necesario
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'supersecretkey'  # Si tienes una clave secreta
    
    # Registrar las rutas o blueprints de tu app
    app.register_blueprint(auth)  # Asegúrate de que el blueprint esté registrado correctamente
    
    with app.test_client() as client:
        yield client

# Test: Verificar que la ruta de login responde
def test_login_route_exists(client):
    """Test que verifica si la ruta de login responde correctamente"""
    response = client.get('/auth/login')  # Reemplaza con la ruta real de tu login
    assert response.status_code == 200  # Asegúrate de que la respuesta sea exitosa

# Test: Verificar que el login funciona correctamente con credenciales válidas
def test_login_valid_credentials(client):
    """Test para verificar el inicio de sesión con credenciales válidas"""
    
    # Datos de login de prueba (ajusta estos valores según tus necesidades)
    valid_data = {
        'username': 'valid_user',
        'password': 'valid_password'  # Asegúrate de tener estas credenciales registradas en tu base de datos de pruebas
    }
    
    # Suponiendo que tu endpoint de login es un POST
    response = client.post('/auth/login', json=valid_data)  # Ajusta la ruta y método HTTP
    assert response.status_code == 200  # Verifica que la respuesta sea exitosa
    assert 'token' in response.json  # Asegúrate de que la respuesta contenga un token

# Test: Verificar login con credenciales inválidas
def test_login_invalid_credentials(client):
    """Test para verificar el inicio de sesión con credenciales inválidas"""
    
    # Datos de login inválidos
    invalid_data = {
        'username': 'invalid_user',
        'password': 'invalid_password'
    }
    
    response = client.post('/auth/login', json=invalid_data)
    assert response.status_code == 401  # Debe devolver un error 401 (no autorizado)
    assert 'message' in response.json  # Asegúrate de que haya un mensaje de error

# Test: Verificar si un usuario no autenticado no puede acceder a una ruta protegida
def test_access_protected_route_without_token(client):
    """Test para verificar el acceso a una ruta protegida sin un token"""
    response = client.get('/protected/resource')  # Ruta protegida
    assert response.status_code == 401  # Debe devolver un error 401 (sin autorización)
    assert 'message' in response.json  # Asegúrate de que haya un mensaje de error

# Test: Verificar si el token JWT es validado correctamente
def test_jwt_token_validation(client):
    """Test para verificar la validación de un JWT"""
    
    # Suponiendo que tu función de login genera un token JWT
    token = 'example.jwt.token'  # Obtén un token válido de alguna forma
    
    response = client.get('/protected/resource', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200  # Si el token es válido, el acceso debe ser concedido

# Test de ejemplo para verificar la respuesta de la API
def test_api_response(client):
    """Test para verificar la respuesta general de la API"""
    response = client.get('/api/status')  # Ruta de estado (ajusta según tu API)
    assert response.status_code == 200  # Verifica que la API responda correctamente
    assert response.json == {'status': 'ok'}  # Ajusta según la respuesta esperada
