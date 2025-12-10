# Python - CRUD API with Software Architecture
**By: Rodrigo Mato**
**Manual QA review**

## Descripción

### Contexto
Este proyecto te introducirá a la arquitectura de software usando Python y FastAPI. Aprenderás a construir un sistema CRUD (Create, Read, Update, Delete) completo aplicando patrones de diseño y principios SOLID.

En este proyecto revisarás y aplicarás:

**Fundamentos Python:**
- Import modules y packages
- Clases y herencia
- Decorators y metaclases
- Context managers
- Async/await patterns

**Arquitectura de Software:**
- Patrón Repository
- Dependency Injection
- Service Layer Pattern
- DTO (Data Transfer Objects)
- Exception Handling

**Desarrollo de APIs:**
- FastAPI framework
- REST API principles
- HTTP status codes
- Request/Response patterns
- API documentation

**Base de Datos:**
- SQLAlchemy ORM
- Database migrations
- Query optimization
- Transaction management

## Recursos

Lee o mira:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)
- [Clean Architecture in Python](https://realpython.com/python-clean-architecture/)
- [Repository Pattern](https://martinfowler.com/eaaCatalog/repository.html)
- [Dependency Injection](https://python-dependency-injector.ets-labs.org/)
- [REST API Best Practices](https://restfulapi.net/)

## Objetivos de Aprendizaje

Al final de este proyecto, serás capaz de explicar sin ayuda de Google:

### General
- Qué es la arquitectura por capas y cómo implementarla
- Cómo separar responsabilidades usando patrones de diseño
- Qué es la inversión de dependencias y por qué es importante
- Cómo diseñar APIs REST profesionales
- Cómo implementar manejo de errores consistente
- Qué son los DTOs y cuándo usarlos
- Cómo estructurar un proyecto de software escalable

### Técnico
- Cómo configurar FastAPI con documentación automática
- Cómo implementar SQLAlchemy con patrón Repository
- Cómo crear middleware personalizado
- Cómo implementar validación de datos con Pydantic
- Cómo escribir tests unitarios para APIs
- Cómo documentar APIs profesionalmente


### Estructura del Proyecto
```
proyecto_crud/
├── README.md
├── requirements.txt
├── run.py
├── main.py
├── core/
│   ├── __init__.py
│   ├── entities/
│   ├── interfaces/
│   ├── dtos/
│   ├── config/
│   └── exceptions/
├── data/
│   ├── __init__.py
│   ├── models/
│   ├── repositories/
│   └── database.py
├── services/
│   ├── __init__.py
│   └── user_service.py
├── api/
│   ├── __init__.py
│   ├── controllers/
│   ├── middleware/
│   └── dependencies.py
└── tests/
    ├── __init__.py
    ├── test_core/
    ├── test_data/
    ├── test_services/
    └── test_api/
```

## Tareas

### 0. Configuración del Entorno
**Obligatorio**

Configura tu entorno de desarrollo para el proyecto.

**Archivos a crear:**
- `requirements.txt`
- `README.md`
- `.gitignore`

**Dependencias requeridas:**
```
fastapi
uvicorn
pydantic
pydantic-settings
sqlalchemy
pytest
pytest-cov
email-validator
```

**Comandos de verificación:**
```bash
# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Verificar instalación
python -c "import fastapi, uvicorn, pydantic, sqlalchemy; print('✅ Dependencias instaladas')"
```

**Repositorio:**
- GitHub repository: `proyecto-crud-arquitectura`
- Archivo: `requirements.txt`, `README.md`

### 1. Capa Core - Entidades de Dominio
**Obligatorio**

Implementa las entidades de dominio que representan los conceptos principales del negocio.

**Archivos a crear:**
- `core/__init__.py`
- `core/entities/__init__.py`
- `core/entities/user.py`

**La entidad User debe:**
- Tener atributos: id, name, email, created_at, updated_at, is_active
- Implementar validaciones de negocio
- Ser independiente de la base de datos
- Tener métodos para activar/desactivar
- Validar formato de email

**Ejemplo de estructura:**
```python
from datetime import datetime
from typing import Optional

class User:
    def __init__(self, name: str, email: str, id: Optional[int] = None):
        # Implementar validaciones y inicialización
        pass

    def activate(self) -> None:
        """Activar usuario"""
        pass

    def deactivate(self) -> None:
        """Desactivar usuario"""
        pass

    def update_email(self, new_email: str) -> None:
        """Actualizar email con validación"""
        pass
```

**Pruebas requeridas:**
```bash
# Ejecutar pruebas
pytest tests/test_core/test_entities/test_user.py -v

# Casos de prueba mínimos:
- test_user_creation
- test_user_validation
- test_email_validation
- test_activate_deactivate
- test_update_methods
```

**Repositorio:**
- Directorio: `core/entities/`
- Archivo: `user.py`

### 2. Capa Core - DTOs (Data Transfer Objects)
**Obligatorio**

Implementa los DTOs para transferir datos entre capas de manera segura.

**Archivos a crear:**
- `core/dtos/__init__.py`
- `core/dtos/user_dtos.py`

**DTOs requeridos:**
- `UserCreateDTO`: Para crear usuarios
- `UserUpdateDTO`: Para actualizar usuarios (campos opcionales)
- `UserResponseDTO`: Para respuestas de API
- `UserListResponseDTO`: Para listados paginados

**Características:**
- Usar Pydantic para validación automática
- Incluir validadores personalizados
- Soportar serialización JSON
- Métodos de conversión desde/hacia entidades

**Ejemplo:**
```python
from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from datetime import datetime

class UserCreateDTO(BaseModel):
    name: str
    email: EmailStr

    @field_validator('name')
    @classmethod
    def validate_name(cls, v):
        # Implementar validación
        pass

class UserResponseDTO(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime
    is_active: bool

    @classmethod
    def from_entity(cls, user: User) -> 'UserResponseDTO':
        # Convertir de entidad a DTO
        pass
```

**Pruebas requeridas:**
```bash
pytest tests/test_core/test_dtos/test_user_dtos.py -v
```

**Repositorio:**
- Directorio: `core/dtos/`
- Archivo: `user_dtos.py`

### 3. Capa Core - Interfaces (Contratos)
**Obligatorio**

Define las interfaces que establecen contratos entre capas.

**Archivos a crear:**
- `core/interfaces/__init__.py`
- `core/interfaces/repositories.py`
- `core/interfaces/services.py`

**Interfaces requeridas:**
- `IUserRepository`: Contrato para acceso a datos
- `IUserService`: Contrato para lógica de negocio

**La interfaz debe usar:**
- `abc.ABC` para clases abstractas
- `@abstractmethod` para métodos obligatorios
- Type hints completos
- Documentación clara

**Ejemplo:**
```python
from abc import ABC, abstractmethod
from typing import List, Optional
from core.entities.user import User
from core.dtos.user_dtos import UserCreateDTO, UserUpdateDTO

class IUserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> User:
        """Guardar usuario"""
        pass

    @abstractmethod
    def find_by_id(self, user_id: int) -> Optional[User]:
        """Buscar usuario por ID"""
        pass

    @abstractmethod
    def find_all(self, page: int, per_page: int) -> List[User]:
        """Listar usuarios con paginación"""
        pass
```

**Repositorio:**
- Directorio: `core/interfaces/`
- Archivos: `repositories.py`, `services.py`

### 4. Capa Core - Excepciones Personalizadas
**Obligatorio**

Implementa un sistema de excepciones jerárquico para manejar errores de manera consistente.

**Archivos a crear:**
- `core/exceptions/__init__.py`
- `core/exceptions/exceptions.py`

**Jerarquía de excepciones:**
```
ApplicationError (base)
├── ValidationError (400)
│   ├── InvalidUserDataError
│   └── InvalidEmailFormatError
├── NotFoundError (404)
│   └── UserNotFoundError
├── DuplicateError (409)
│   ├── DuplicateEmailError
│   └── DuplicateUserError
├── BusinessLogicError (422)
│   └── InvalidUserOperationError
└── InfrastructureError (500)
    ├── DatabaseError
    └── ExternalServiceError
```

**Cada excepción debe:**
- Heredar de la clase base apropiada
- Incluir mensaje descriptivo
- Tener código de estado HTTP asociado
- Proporcionar contexto adicional

**Ejemplo:**
```python
class ApplicationError(Exception):
    """Excepción base para errores de aplicación"""
    def __init__(self, message: str, details: dict = None):
        self.message = message
        self.details = details or {}
        super().__init__(self.message)

class UserNotFoundError(NotFoundError):
    """Usuario no encontrado"""
    def __init__(self, user_id: int):
        message = f"Usuario con ID {user_id} no encontrado"
        details = {"user_id": user_id}
        super().__init__(message, details)
```

**Repositorio:**
- Directorio: `core/exceptions/`
- Archivo: `exceptions.py`

### 5. Capa Data - Modelos de Base de Datos
**Obligatorio**

Implementa los modelos de SQLAlchemy para persistencia de datos.

**Archivos a crear:**
- `data/__init__.py`
- `data/models/__init__.py`
- `data/models/user_model.py`
- `data/database.py`

**El modelo UserModel debe:**
-0o
- Incluir todos los campos necesarios
- Tener índices apropiados
- Incluir constrains de base de datos

**Configuración de base de datos:**
- Soporte para SQLite (desarrollo)
- Configuración por variables de entorno
- Pool de conexiones
- Sesiones con context manager

**Ejemplo:**
```python
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Index
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    is_active = Column(Boolean, default=True, nullable=False, index=True)

    # Índices adicionales
    __table_args__ = (
        Index('ix_users_email_active', 'email', 'is_active'),
    )
```

**Repositorio:**
- Directorio: `data/models/`
- Archivos: `user_model.py`, `database.py`

### 6. Capa Data - Repository Pattern
**Obligatorio**

Implementa el patrón Repository para abstraer el acceso a datos.

**Archivos a crear:**
- `data/repositories/__init__.py`
- `data/repositories/user_repository.py`

**UserRepository debe:**
- Implementar `IUserRepository`
- Manejar todas las operaciones CRUD
- Convertir entre modelos y entidades
- Manejar errores de base de datos
- Incluir métodos de consulta optimizados

**Métodos requeridos:**
```python
class UserRepository(IUserRepository):
    def __init__(self, db_session: Session):
        self._db = db_session

    def save(self, user: User) -> User:
        """Crear o actualizar usuario"""
        pass

    def find_by_id(self, user_id: int) -> Optional[User]:
        """Buscar por ID"""
        pass

    def find_by_email(self, email: str) -> Optional[User]:
        """Buscar por email"""
        pass

    def find_all(self, page: int, per_page: int) -> List[User]:
        """Listar con paginación"""
        pass

    def delete(self, user_id: int) -> bool:
        """Eliminar usuario"""
        pass

    def exists_by_email(self, email: str) -> bool:
        """Verificar si email existe"""
        pass

    def count_total(self) -> int:
        """Contar total de usuarios"""
        pass
```

**Pruebas requeridas:**
```bash
pytest tests/test_data/test_repositories/test_user_repository.py -v
```

**Repositorio:**
- Directorio: `data/repositories/`
- Archivo: `user_repository.py`

### 7. Capa Services - Lógica de Negocio
**Obligatorio**

Implementa los servicios que contienen la lógica de negocio de la aplicación.

**Archivos a crear:**
- `services/__init__.py`
- `services/user_service.py`

**UserService debe:**
- Implementar `IUserService`
- Coordinar operaciones complejas
- Aplicar reglas de negocio
- Manejar transacciones
- Validar lógica de dominio

**Reglas de negocio a implementar:**
- No permitir emails duplicados
- Validar datos antes de persistir
- Registrar actividad de usuarios
- Manejar soft deletes
- Aplicar políticas de actualización

**Ejemplo:**
```python
class UserService(IUserService):
    def __init__(self, user_repository: IUserRepository):
        self._user_repository = user_repository

    def create_user(self, create_dto: UserCreateDTO) -> User:
        """Crear nuevo usuario con validaciones"""
        # 1. Validar que email no existe
        # 2. Crear entidad User
        # 3. Aplicar reglas de negocio
        # 4. Persistir en repositorio
        # 5. Retornar usuario creado
        pass

    def update_user(self, user_id: int, update_dto: UserUpdateDTO) -> User:
        """Actualizar usuario existente"""
        pass

    def get_user(self, user_id: int) -> User:
        """Obtener usuario por ID"""
        pass

    def list_users(self, page: int, per_page: int) -> List[User]:
        """Listar usuarios con paginación"""
        pass

    def deactivate_user(self, user_id: int) -> User:
        """Desactivar usuario (soft delete)"""
        pass
```

**Repositorio:**
- Directorio: `services/`
- Archivo: `user_service.py`

### 8. Capa API - Controladores REST
**Obligatorio**

Implementa los controladores que exponen la funcionalidad vía REST API.

**Archivos a crear:**
- `api/__init__.py`
- `api/controllers/__init__.py`
- `api/controllers/user_controller.py`
- `api/dependencies.py`

**UserController debe:**
- Implementar todos los endpoints REST
- Manejar validación de entrada
- Convertir entre DTOs y respuestas HTTP
- Manejar errores apropiadamente
- Incluir documentación OpenAPI

**Endpoints requeridos:**
```python
@router.post("/", status_code=201, response_model=UserResponseDTO)
async def create_user(user_data: UserCreateDTO) -> UserResponseDTO:
    """Crear nuevo usuario"""
    pass

@router.get("/{user_id}", response_model=UserResponseDTO)
async def get_user(user_id: int) -> UserResponseDTO:
    """Obtener usuario por ID"""
    pass

@router.get("/", response_model=UserListResponseDTO)
async def list_users(page: int = 1, per_page: int = 10) -> UserListResponseDTO:
    """Listar usuarios con paginación"""
    pass

@router.put("/{user_id}", response_model=UserResponseDTO)
async def update_user(user_id: int, user_data: UserUpdateDTO) -> UserResponseDTO:
    """Actualizar usuario completo"""
    pass

@router.patch("/{user_id}", response_model=UserResponseDTO)
async def patch_user(user_id: int, user_data: UserUpdateDTO) -> UserResponseDTO:
    """Actualizar usuario parcial"""
    pass

@router.delete("/{user_id}")
async def delete_user(user_id: int) -> dict:
    """Eliminar usuario"""
    pass

@router.patch("/{user_id}/deactivate", response_model=UserResponseDTO)
async def deactivate_user(user_id: int) -> UserResponseDTO:
    """Desactivar usuario"""
    pass
```

**Repositorio:**
- Directorio: `api/controllers/`
- Archivo: `user_controller.py`

### 9. Dependency Injection y Configuración
**Obligatorio**

Implementa inyección de dependencias y configuración de la aplicación.

**Archivos a crear:**
- `core/config/__init__.py`
- `core/config/settings.py`
- `api/dependencies.py`
- `main.py`

**Settings debe manejar:**
- Variables de entorno
- Configuración de base de datos
- Configuración de logging
- Configuración de API
- Diferentes entornos (dev, test, prod)

**Dependencies debe proveer:**
- Sesiones de base de datos
- Instancias de repositorios
- Instancias de servicios
- Instancias de controladores

**Ejemplo de dependency injection:**
```python
def get_db() -> Generator[Session, None, None]:
    """Proveedor de sesión de base de datos"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_controller(
    db: Session = Depends(get_db)
) -> UserController:
    """Proveedor de user controller con todas sus dependencias"""
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    return UserController(user_service)
```

**Repositorio:**
- Archivos: `core/config/settings.py`, `api/dependencies.py`, `main.py`

### 10. Manejo de Errores y Middleware
**Obligatorio**

Implementa manejo global de errores y middleware personalizado.

**Archivos a crear:**
- `api/middleware/__init__.py`
- `api/middleware/error_handler.py`
- `api/middleware/logging_middleware.py`

**Error handler debe:**
- Capturar todas las excepciones
- Convertir excepciones a respuestas HTTP
- Mapear códigos de estado correctos
- Registrar errores para debugging
- Retornar respuestas consistentes

**Logging middleware debe:**
- Registrar todas las requests
- Medir tiempo de respuesta
- Registrar información de usuario
- Manejar correlation IDs

**Ejemplo de error handler:**
```python
@app.exception_handler(ApplicationError)
async def application_error_handler(request: Request, exc: ApplicationError):
    """Maneja errores de aplicación personalizados"""
    status_code = get_http_status_code(exc)
    return JSONResponse(
        status_code=status_code,
        content={
            "error": True,
            "error_type": type(exc).__name__,
            "message": exc.message,
            "details": exc.details
        }
    )
```

**Repositorio:**
- Directorio: `api/middleware/`
- Archivos: `error_handler.py`, `logging_middleware.py`

### 11. Aplicación Principal y Configuración
**Obligatorio**

Configura la aplicación FastAPI principal con todos sus componentes.

**Archivos a crear:**
- `main.py` - Aplicación FastAPI
- `run.py` - Script de ejecución
- `conftest.py` - Configuración de pruebas

**main.py debe incluir:**
- Configuración de FastAPI
- Registro de routers
- Configuración de middleware
- Configuración de CORS
- Documentación OpenAPI
- Inicialización de base de datos

**run.py debe:**
- Configurar uvicorn
- Manejar argumentos de línea de comandos
- Configurar reload automático
- Manejar diferentes entornos

**Ejemplo de main.py:**
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import get_settings
from core.exceptions import configure_exception_handlers
from api.controllers.user_controller import router as user_router
from data.database import create_tables

settings = get_settings()

app = FastAPI(
    title="CRUD API - Software Architecture",
    description="API RESTful con arquitectura por capas",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configurar exception handlers
configure_exception_handlers(app)

# Registrar routers
app.include_router(user_router)

@app.on_event("startup")
async def startup():
    """Inicializar aplicación"""
    create_tables()
    logger.info("🚀 Aplicación iniciada correctamente")

@app.on_event("shutdown")
async def shutdown():
    """Limpiar recursos"""
    logger.info("⏹️ Aplicación detenida")

@app.get("/")
async def root():
    """Endpoint de salud"""
    return {
        "message": "CRUD API - Software Architecture",
        "version": "1.0.0",
        "docs": "/docs"
    }
```

**Repositorio:**
- Archivos: `main.py`, `run.py`

### 12. Testing Completo
**Obligatorio**

Implementa tests unitarios y de integración para toda la aplicación.

**Archivos a crear:**
```
tests/
├── __init__.py
├── conftest.py
├── test_core/
│   ├── test_entities/
│   │   └── test_user.py
│   ├── test_dtos/
│   │   └── test_user_dtos.py
│   └── test_exceptions/
│       └── test_exceptions.py
├── test_data/
│   ├── test_models/
│   │   └── test_user_model.py
│   └── test_repositories/
│       └── test_user_repository.py
├── test_services/
│   └── test_user_service.py
└── test_api/
    ├── test_controllers/
    │   └── test_user_controller.py
    └── test_integration/
        └── test_user_endpoints.py
```

**Tipos de tests requeridos:**
- **Unit tests**: Cada clase/función individualmente
- **Integration tests**: Interacción entre capas
- **API tests**: Endpoints completos
- **Database tests**: Operaciones de persistencia

**Cobertura mínima por módulo:**
- Core entities: 95%
- DTOs: 90%
- Repositories: 85%
- Services: 90%
- Controllers: 85%

**Ejemplo de test:**
```python
import pytest
from fastapi.testclient import TestClient
from main import app
from core.dtos.user_dtos import UserCreateDTO

client = TestClient(app)

class TestUserEndpoints:
    def test_create_user_success(self):
        """Test crear usuario exitoso"""
        user_data = {
            "name": "Juan Pérez",
            "email": "juan@ejemplo.com"
        }
        response = client.post("/api/v1/users/", json=user_data)

        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Juan Pérez"
        assert data["email"] == "juan@ejemplo.com"
        assert data["is_active"] is True
        assert "id" in data
        assert "created_at" in data

    def test_create_user_duplicate_email(self):
        """Test error al crear usuario con email duplicado"""
        user_data = {
            "name": "Juan Pérez",
            "email": "juan@ejemplo.com"
        }
        # Crear primer usuario
        client.post("/api/v1/users/", json=user_data)

        # Intentar crear segundo usuario con mismo email
        response = client.post("/api/v1/users/", json=user_data)

        assert response.status_code == 409
        data = response.json()
        assert data["error"] is True
        assert "ya existe" in data["message"].lower()
```

**Comandos de testing:**
```bash
# Ejecutar todos los tests
pytest tests/ -v

# Test con cobertura
pytest tests/ --cov=. --cov-report=html

# Test específico
pytest tests/test_api/test_controllers/test_user_controller.py -v

# Test de integración
pytest tests/test_api/test_integration/ -v
```

**Repositorio:**
- Directorio: `tests/`
- Todos los archivos de test

### 13. Documentación y README
**Obligatorio**

Crea documentación completa del proyecto.

**Archivos a crear:**
- `README.md` - Documentación principal
- `ARCHITECTURE.md` - Documentación de arquitectura
- `API.md` - Documentación de API
- `DEPLOYMENT.md` - Guía de despliegue

**README.md debe incluir:**
- Descripción del proyecto
- Instrucciones de instalación
- Guía de uso rápido
- Ejemplos de API
- Comandos de desarrollo
- Arquitectura del proyecto
- Contribución y coding standards

**ARCHITECTURE.md debe explicar:**
- Patrón de arquitectura usado
- Responsabilidad de cada capa
- Flujo de datos
- Principios SOLID aplicados
- Patrones de diseño implementados

**Ejemplo de README.md:**
```markdown
# 🎯 CRUD API - Arquitectura de Software

[![Tests](https://github.com/usuario/proyecto-crud-arquitectura/workflows/Tests/badge.svg)](https://github.com/usuario/proyecto-crud-arquitectura/actions)
[![Coverage](https://codecov.io/gh/usuario/proyecto-crud-arquitectura/branch/main/graph/badge.svg)](https://codecov.io/gh/usuario/proyecto-crud-arquitectura)

Proyecto educativo que demuestra la implementación de un CRUD completo usando arquitectura por capas con FastAPI, SQLAlchemy y Python.

## 🏗️ Arquitectura

```
┌─────────────────┐
│   API Layer    │  ← Controllers, Routes, Middleware
├─────────────────┤
│ Service Layer   │  ← Business Logic, Use Cases
├─────────────────┤
│   Data Layer    │  ← Repositories, Models, Database
├─────────────────┤
│   Core Layer    │  ← Entities, DTOs, Interfaces
└─────────────────┘
```

## 🚀 Instalación Rápida

\`\`\`bash
# Clonar repositorio
git clone https://github.com/usuario/proyecto-crud-arquitectura.git
cd proyecto-crud-arquitectura

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python run.py
\`\`\`

## 📚 Documentación API

Una vez ejecutando, visita:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🧪 Testing

\`\`\`bash
# Ejecutar todos los tests
pytest tests/ -v

# Con cobertura
pytest tests/ --cov=. --cov-report=html
\`\`\`

## 📖 Aprende Más

- [Arquitectura del Proyecto](ARCHITECTURE.md)
- [Documentación de API](API.md)
- [Guía de Despliegue](DEPLOYMENT.md)
```

**Repositorio:**
- Archivos: `README.md`, `ARCHITECTURE.md`, `API.md`, `DEPLOYMENT.md`

### 14. Bonus: Características Avanzadas
**Opcional**

Implementa características adicionales para demostrar conceptos avanzados.

**Características opcionales:**
1. **Autenticación JWT**
   - Login/logout de usuarios
   - Middleware de autenticación
   - Protección de endpoints

2. **Rate Limiting**
   - Limitación de requests por IP
   - Diferentes límites por endpoint
   - Headers informativos

3. **Caching**
   - Cache en memoria para consultas
   - Invalidación automática
   - Redis como backend opcional

4. **Async Processing**
   - Tasks en background
   - Queue processing
   - Celery integration

5. **Monitoring**
   - Health checks
   - Metrics endpoint
   - Structured logging

6. **Database Migrations**
   - Alembic integration
   - Version control de schema
   - Comandos CLI

**Repositorio:**
- Directorio: `extras/`
- Implementación de características adicionales

## Entrega Final

### Estructura Completa
Tu proyecto debe tener exactamente esta estructura:

```
proyecto_crud/
├── README.md
├── ARCHITECTURE.md
├── API.md
├── requirements.txt
├── run.py
├── main.py
├── conftest.py
├── core/
│   ├── __init__.py
│   ├── entities/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── interfaces/
│   │   ├── __init__.py
│   │   ├── repositories.py
│   │   └── services.py
│   ├── dtos/
│   │   ├── __init__.py
│   │   └── user_dtos.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   └── exceptions/
│       ├── __init__.py
│       └── exceptions.py
├── data/
│   ├── __init__.py
│   ├── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user_model.py
│   └── repositories/
│       ├── __init__.py
│       └── user_repository.py
├── services/
│   ├── __init__.py
│   └── user_service.py
├── api/
│   ├── __init__.py
│   ├── dependencies.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── user_controller.py
│   └── middleware/
│       ├── __init__.py
│       ├── error_handler.py
│       └── logging_middleware.py
└── tests/
    ├── __init__.py
    ├── conftest.py
    ├── test_core/
    ├── test_data/
    ├── test_services/
    └── test_api/
```

### Comandos de Verificación

Tu proyecto debe pasar todos estos comandos:

```bash
# 1. Tests completos
pytest tests/ -v
echo "✅ Tests: $?"

# 2. Cobertura mínima
pytest tests/ --cov=. --cov-report=term-missing --cov-fail-under=85
echo "✅ Cobertura: $?"

# 3. Linting
flake8 . --max-line-length=88 --exclude=venv,tests
echo "✅ Linting: $?"

# 4. Type checking
mypy . --ignore-missing-imports
echo "✅ Type hints: $?"

# 5. Aplicación funcional
python3 run.py &
sleep 5
curl http://localhost:8000/ | grep "CRUD API"
echo "✅ Aplicación: $?"

# 6. API completa
curl -X POST http://localhost:8000/api/v1/users/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Test", "email": "test@example.com"}' | grep '"id"'
echo "✅ API CRUD: $?"
```
