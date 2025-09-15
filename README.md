# 🎓 Challenge Gestión Académica - Odoo

Sistema de gestión académica desarrollado como challenge técnico utilizando Odoo Framework. Permite administrar alumnos, programas académicos e inscripciones.

## ✨ Características

### 🎯 Funcionalidades Principales
- ✅ **Gestión de Alumnos** - Información del Alumno
- ✅ **Gestión de Programas** - Información de programas académicos
- ✅ **Sistema de Inscripciones** - Relación entre alumnos y programas
- ✅ **EndPoint Público** - Devuelve los resultados en formato JSON
- ✅ **Control de Acceso** - Sistema de grupos y permisos

### 🔧 Características Técnicas
- ✅ **Constraints SQL** - Validaciones a nivel base de datos
- ✅ **Validaciones** - Lógica con `@api.constrains`
- ✅ **Internacionalización** - Soporte para caracteres especiales

## 📁 Estructura del Proyecto

```
challenge_gestion_academica/
├── 📄 __init__.py              # Punto de entrada del módulo
├── 📄 __manifest__.py          # Configuración y metadatos del módulo
├── 📁 controllers/             # Controladores web y API
│   ├── 📄 __init__.py
│   └── 📄 controller.py        # Endpoints REST API
├── 📁 models/                  # Modelos de datos
│   ├── 📄 __init__.py
│   └── 📄 models.py           # Definición de modelos y validaciones
├── 📁 security/               # Configuración de seguridad
│   ├── 📄 groups.xml          # Definición de grupos de usuarios
│   └── 📄 security.xml        # Permisos y reglas de acceso
└── 📁 views/                  # Interfaces de usuario
    ├── 📄 alumno.xml          # Vistas para modelo Alumno
    ├── 📄 programa.xml        # Vistas para modelo Programa
    ├── 📄 inscripcion.xml     # Vistas para modelo Inscripción
    └── 📄 menu.xml           # Estructura de menús
```

## 🔧 Requisitos

### Software Necesario
- **Odoo 17+** (Framework principal)
- **Python 3.8+**
- **PostgreSQL 12+**
- **Git** (para clonación del repositorio)

### Dependencias
- `base` - Módulo base de Odoo

## 🚀 Instalación

### 1. Clonar el Repositorio
```bash
git clone https://github.com/floradaro/challenge-gestion-academica.git
cd challenge-gestion-academica
```

### 2. Copiar al Directorio de Addons
```bash
# Copiar el módulo al directorio addons de Odoo
cp -r challenge_gestion_academica /path/to/odoo/addons/
```

### 3. Actualizar Lista de Aplicaciones
1. Acceder a Odoo como administrador
2. Ir a **Aplicaciones** → **Actualizar Lista de Aplicaciones**
3. Buscar "Challenge Gestión Académica"
4. Hacer clic en **Instalar**

### 4. Configurar Permisos de Usuario
1. Ir a **Configuración** → **Usuarios y Compañías** → **Usuarios**
2. Seleccionar usuario
3. En **Derechos de Acceso**, buscar **"Challenge Odoo"**
4. Asignar grupo apropiado:
   - **Usuario**: Solo lectura y crear inscripciones
   - **Administrador**: Permisos completos

## 📖 Uso

### Navegación Principal
Después de la instalación, encontrarás un nuevo menú **"Challenge"** en la barra lateral con las siguientes opciones:

- 👥 **Alumnos** - Gestión de estudiantes
- 📚 **Programas** - Administración de programas académicos  
- 📝 **Inscripciones** - Relación alumnos-programas

### Flujo de Trabajo Típico
1. **Crear Programas** → Definir programas académicos
2. **Registrar Alumnos** → Dar de alta estudiantes
3. **Gestionar Inscripciones** → Inscribir alumnos a programas
4. **Consultar API** → Obtener datos via endpoints

## 🌐 API Endpoints

### Obtener Alumnos por Programa

#### HTTP (para navegador)
```http
GET /challenge/programa/{programa_id}/alumnos
```

**Ejemplo:**
```bash
curl http://localhost:8069/challenge/programa/1/alumnos
```

### Respuesta de la API
```json
[
  {
    "nombre": "Juan",
    "apellido": "Pérez",
    "fecha_nacimiento": "1995-05-15",
    "nro_legajo": "12345",
    "email": "juan.perez@email.com",
    "telefono": "+54 261 1234567",
    "direccion": "Calle Falsa 123",
    "pais": {
      "id": 11,
      "nombre": "Argentina"
    }
  }
]
```


## 🔐 Sistema de Seguridad

### 👥 Grupos de Usuario
- **Usuario**: Permisos de lectura y creación limitada
- **Administrador**: Permisos completos (CRUD)

### 🛡️ Matriz de Permisos

| Modelo | Usuario | Administrador |
|--------|---------|---------------|
| **Alumno** | 👁️ Leer | 👁️📝➕🗑️ CRUD |
| **Programa** | 👁️ Leer | 👁️📝➕🗑️ CRUD |
| **Inscripción** | 👁️👀➕ Leer/Crear | 👁️📝➕🗑️ CRUD |


## 👩‍💻 Autor

**Florencia Adaro**
- GitHub: [GitHub](https://github.com/floradaro)
- Email: flor.adaro@gmail.com
- LinkedIn: [@floradaro](https://www.linkedin.com/in/floradaro/)

