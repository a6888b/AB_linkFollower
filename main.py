#! /usr/local/bin/python3.10
from  src.model import model_base as m 
from  src.view import view_base as v 
from  src.controller import controller_base as c 

"""
    FAIRE UN SCRIPT QUI SUIS UN LIEN EST QUI SUIS LES LIEN QUI EST DANS LE LIEN
    TOUT CA C'EST RECURSIF, EN MVC
    LES LIENS SONT ENREGISTREZ DANS UN FICHIER EN JSON
    LES CLEF C'EST LE SITE QUI CONTIENT LE LIEN EST SONT LIEN 
    
    1: lui donner un lien
    2: il liste tout les liens qui sont dans la page 
    3: il identifie les liens qui appartient a cette page
    4: il parcour les liens est ainsi de suite 
"""

controller = c.ControllerBase(m.ModelBase, v.ViewBase)

if not controller.requests_link('https://mail.google.com/mail/u/0/#inbox') is None: 
    print('lien ok')