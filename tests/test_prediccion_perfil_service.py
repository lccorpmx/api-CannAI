import os
import sys
import pytest

# Agregar la ruta al directorio padre al sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# Ahora puedes importar tu módulo
from services.prediction_cepa import PrediccionPerfilService
from routers.predicciones_route import PreferenciasUsuario_Perfil

def test_cargar_dataset():
    servicio = PrediccionPerfilService()
    servicio.cargar_dataset()
    assert servicio.X_train_perfil is not None
    assert servicio.Y_train_perfil is not None

def test_entrenar_modelo_perfiles():
    servicio = PrediccionPerfilService()
    servicio.cargar_dataset()
    servicio.entrenar_modelo_perfiles()
    assert servicio.knn_model_perfiles is not None

def test_make_prediccion_perfil():
    servicio = PrediccionPerfilService()
    servicio.cargar_dataset()
    servicio.entrenar_modelo_perfiles()
    
    preferencias_usuario_perfil = PreferenciasUsuario_Perfil(
            feeling_relaxed = 0,
            feeling_happy = 0,
            feeling_euphoric = 0,
            feeling_uplifted = 0,
            feeling_sleepy = 0,
            feeling_hungry = 0,
            feeling_talkative = 0,
            feeling_creative = 0,
            feeling_energetic = 0,
            feeling_focused = 0,
            feeling_giggly = 0,
            feeling_aroused = 0,
    )
    
    prediccion = servicio.make_prediccion_perfil(preferencias_usuario_perfil)
    assert isinstance(prediccion, int)
