from odoo import http
from odoo.http import request #Herramientas para manejar requests
import json

class Controller(http.Controller): #Todas las clases de controlador en Odoo deben heredar de http.Controller

    # Versión HTTP para navegador
    @http.route('/challenge/programa/<int:programa_id>/alumnos', type='http', auth='public', methods=['GET'])
    def get_alumnos_por_programa_http(self, programa_id, **kwargs):
        return self._get_alumnos_logic(programa_id)

    # Versión JSON para API
    @http.route('/api/challenge/programa/<int:programa_id>/alumnos', type='json', auth='public', methods=['POST'])
    def get_alumnos_por_programa_json(self, programa_id, **kwargs):
        return self._get_alumnos_logic(programa_id, return_json=False)

    def _get_alumnos_logic(self, programa_id, return_json=True):
        """Lógica común para ambas rutas"""
        inscripciones = request.env['challenge.inscripcion'].sudo().search([('programa_id', '=', programa_id)])

        if not inscripciones.exists():
            error_data = {"error": "No se encontraron inscripciones para el programa con ID {}".format(programa_id)}
            
        #Lo devuelve en el formato correspondiente JSON
            if return_json:
                return request.make_response(
                    json.dumps(error_data, indent=4),
                    headers=[('Content-Type', 'application/json')]
                )
            return error_data

        alumnos = []
        for inscripcion in inscripciones: #Iterar sobre las inscripciones encontradas
            alumno = inscripcion.alumno_id
            alumnos.append({
                'nombre': alumno.nombre,
                'apellido': alumno.apellido,
                'fecha_nacimiento': str(alumno.fecha_nacimiento) if alumno.fecha_nacimiento else None,
                'nro_legajo': alumno.nro_legajo,
                'email': alumno.email,  
                'telefono': alumno.telefono,
                'direccion': alumno.direccion,          
                'pais': {
                    'id': alumno.pais_id.id,
                    'nombre': alumno.pais_id.name
                } if alumno.pais_id else {}
            })
        
        #Lo devuelve en el formato correspondiente JSON
        if return_json:
            return request.make_response(
                json.dumps(alumnos, indent=4, default=str), 
                headers=[('Content-Type', 'application/json')]
            )
        return alumnos