# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, datetime

class Viajes(models.Model):
    _name = "viajes"
    

    titulo = fields.Char("Titulo", required=True)
    descripcion = fields.Text("Descripción")
    lugares = fields.One2many("lugares", "id", string="Lugares")
    gastos = fields.Float("Gastos Totales")
    fecha = fields.Date('Fecha', default=lambda *a:datetime.now().strftime('%Y-%m-%d'))

    _sql_constraints=[
        ('name_uniq', 'unique(titulo)','Viaje ya existe!'),
        ('gastos_nonegative','check(gastos >0)','Debes introducir un valor positivo')
    ]

class Lugares(models.Model):
    _name = "lugares"
    _rec_name = "nombre"
    _inherits ={'res.country.state':'provincia'}
    
    nombre = fields.Char('nombre',required=True)
    pais = fields.Many2one('res.country', 'Pais', required=True)
    provincia = fields.Many2one('res.country.state',string="provincia")
    imagen = fields.Binary("Imagen")


