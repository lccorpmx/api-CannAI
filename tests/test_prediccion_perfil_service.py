import os
import sys

# Agregar la ruta al directorio padre al sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# Ahora puedes importar tu módulo
from services.prediction_cepa import PrediccionPerfilService
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
    preferencias_usuario = {
    "helps_stress": 100,
    "helps_pain": 0,
    "helps_depression": 0,
    "helps_anxiety": 100,
    "helps_insomnia": 0,
    "helps_headache": 0,
    "helps_ptsd": 0,
    "helps_fatigue": 0,
    "helps_lackofappetite": 0,
    "helps_nausea": 0,
    "helps_headaches": 0,
    "helps_bipolar_disorder": 0,
    "helps_cancer": 100,
    "helps_tingly": 0,
    "helps_cramps": 0,
    "helps_gastrointestinaldisorder": 0,
    "helps_inflammation": 0,
    "helps_musclespasms": 0,
    "helps_eye_pressure": 0,
    "helps_migraines": 0,
    "helps_asthma": 0,
    "helps_anorexia": 0,
    "helps_arthritis": 0,
    "helps_add_adhd": 0,
    "helps_musculardystrophy": 0,
    "helps_hypertension": 0,
    "helps_glaucoma": 0,
    "helps_pms": 0,
    "helps_seizures": 0,
    "helps_spasticity": 0,
    "helps_spinalcordinjury": 0,
    "helps_fibromyalgia": 0,
    "helps_crohn_s_disease": 0,
    "helps_phantomlimbpain": 0,
    "helps_epilepsy": 0,
    "helps_multiplesclerosis": 0,
    "helps_parkinson_s": 0,
    "helps_tourette_ssyndrome": 0,
    "helps_alzheimer_s": 0,
    "helps_hiv_aids": 0,
    "helps_tinnitus": 0
    }
    prediccion = servicio.make_prediccion_perfil(preferencias_usuario)
    assert isinstance(prediccion, int)
