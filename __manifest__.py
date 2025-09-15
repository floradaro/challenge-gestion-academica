{
    'name': "Challenge Gestión Académica",
    'version': '1.0.0',
    'sequence': 5,
    'description': """Challenge Gestión Académica""",
    'author': "Florencia Adaro",
    'depends': ['base'],
    'data': [
        'security/groups.xml',
        'security/security.xml',
        'views/alumno.xml',
        'views/programa.xml',
        'views/inscripcion.xml',
        'views/menu.xml',
    ],
    'application': True,
}