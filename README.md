# Proyecto Django – Entrega 3

Este proyecto es una aplicación web desarrollada con Django 5.2.7, creada como parte del curso / práctica personal. Incluye la estructura básica de un proyecto funcional con vistas, templates y configuración lista para extender, la idea que me surgio fue armar una app donde los usuarios puedan registrase, recomendar y buscar peliculas segun genero.

El objetivo del proyecto es demostrar el uso de:
- Modelos
- Vistas
- Templates
- Formularios
- Rutas (URLs)
- Admin de Django


** Tecnologías utilizadas

- Django 5.2.7
- asgiref 3.10.0
- sqlparse 0.5.3
- tzdata 2025.2
- Python 3.10+


** Requisitos previos
Tener instalado:
- Python 3.10 o superior
- pip (incluido en Python)
- virtualenv (opcional pero recomendado)
- Git

Base de datos:
- Por defecto, SQLite3

**Clonar el repositorio 
```bash
git clone https://github.com/juliantaddei1-arch/JulianTaddei-Entrega3.git
cd JulianTaddei-final

** Crear y activar el entorno virtual:

python -m venv venv
.\venv\Scripts\Activate.ps1

** Instalar depedencias:

pip install -r requirements.txt

**Estructura del proyecto:
JulianTaddei-Final/
├── manage.py
├── requirements.txt
├── seguimiento/           
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── Incio/                 
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    └── templates/

Enlace de video :
https://drive.google.com/file/d/1fDGsUM9iTIyLxw6sEqU_WeAiCwBORB0H/view?usp=sharing