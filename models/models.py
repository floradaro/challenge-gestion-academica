from odoo import models, fields, api #api para decoradores
from odoo.exceptions import ValidationError #Errores personalizados
import re #Expresiones regulares para validar formatos
from datetime import date, timedelta #Para manejar fechas


class Alumno(models.Model):
    _name = 'challenge.alumno' #Identificador único del modelo en Odoo
    _description = 'Información del Alumno'

    nombre = fields.Char(string="Nombre", required=True)
    apellido = fields.Char(string="Apellido", required=True)
    nro_legajo = fields.Char(string="Número de Legajo", required=True, unique=True)
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento")
    email = fields.Char(string="Email")
    telefono = fields.Char(string="Teléfono")
    direccion = fields.Text(string="Dirección")
    pais_id = fields.Many2one('res.country', string="País") #Relación muchos a uno con el modelo de países de Odoo, res.country es el modelo estándar de Odoo para países
    

    @api.constrains('nombre', 'apellido')
    def _check_nombres_validos(self):
        """Valida que nombre y apellido solo contengan letras y espacios"""
        for record in self:
            # Patrón: solo letras, espacios, acentos y caracteres especiales del español
            patron = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$'
            
            if record.nombre and not re.match(patron, record.nombre):
                raise ValidationError("El nombre solo debe contener letras y espacios.")
            
            if record.apellido and not re.match(patron, record.apellido):
                raise ValidationError("El apellido solo debe contener letras y espacios.")

    @api.constrains('email')
    def _check_email_valido(self):
        """Valida que el email tenga formato correcto"""
        for record in self:
            if record.email:
                patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
                if not re.match(patron_email, record.email):
                    raise ValidationError("El formato del email no es válido.")

    @api.constrains('fecha_nacimiento')
    def _check_fecha_nacimiento(self):
        """Valida que la fecha de nacimiento sea lógica"""
        for record in self:
            if record.fecha_nacimiento:
                today = date.today()
                min_date = today - timedelta(days=365 * 120)
                
                if record.fecha_nacimiento > today:
                    raise ValidationError("La fecha de nacimiento no puede ser futura.")
                
                if record.fecha_nacimiento < min_date:
                    raise ValidationError("La fecha de nacimiento no puede ser anterior a 120 años.")

    @api.constrains('telefono')
    def _check_telefono(self):
        """Valida formato del teléfono"""
        for record in self:
            if record.telefono:
                # Acepta números, espacios, guiones, paréntesis y el signo +
                patron_telefono = r'^[\d\s\-\(\)\+]+$'
                if not re.match(patron_telefono, record.telefono):
                    raise ValidationError("El teléfono solo debe contener números, espacios, guiones, paréntesis y el signo +.")
                
    #Validaciones en la base de datos
    _sql_constraints = [
        ('nro_legajo_unique', 'UNIQUE(nro_legajo)', 'El número de legajo ya existe. Debe ser único.')
    ]

class Programa(models.Model):
    _name = 'challenge.programa' #Identificador único del modelo en Odoo
    _description = 'Programa'

    nombre = fields.Char(string="Nombre del Programa", required=True)
    descripcion = fields.Text(string="Descripción")

class Inscripcion(models.Model):
    _name = 'challenge.inscripcion' #Identificador único del modelo en Odoo
    _description = 'Inscripción de Alumno a Programa'

    alumno_id = fields.Many2one('challenge.alumno', string="Alumno_id", required=True) #Relación muchos a uno con Alumnos
    programa_id = fields.Many2one('challenge.programa', string="Programa_id", required=True) #Relación muchos a uno con Programas
    fecha_inscripcion = fields.Date(string="Fecha de inscripción", default=fields.Date.today, readonly=True) #Readonly para que no se pueda modificar

    #Validaciones en la base de datos
    _sql_constraints = [
        ('alumno_programa_unique', 'UNIQUE(alumno_id, programa_id)', 'Este alumno ya está inscripto en este programa.')
    ]