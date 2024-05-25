from fastapi import APIRouter
from pydantic import BaseModel
from services.prediction_cepa import PrediccionPerfilService
from services.prediction_cepa import PrediccionCepaService


router = APIRouter()


servicio_PrediccionPerfil = PrediccionPerfilService()
servicio_PrediccionCepa = PrediccionCepaService()

class PreferenciasUsuario_Perfil(BaseModel):
    feeling_relaxed: int
    feeling_happy: int
    feeling_euphoric: int
    feeling_uplifted: int
    feeling_sleepy: int
    feeling_hungry: int
    feeling_talkative: int
    feeling_creative:int
    feeling_energetic:int
    feeling_focused: int
    feeling_giggly: int
    feeling_aroused: int
    
class PreferenciasUsuario_Cepa(BaseModel):
    helps_stress: int
    helps_pain: int
    helps_depression: int
    helps_anxiety: int
    helps_insomnia: int
    helps_headache: int
    helps_ptsd: int
    helps_fatigue: int
    helps_lackofappetite: int
    helps_nausea: int
    helps_headaches: int
    helps_bipolar_disorder: int
    helps_cancer: int
    helps_tingly: int
    helps_cramps: int
    helps_gastrointestinaldisorder: int
    helps_inflammation: int
    helps_musclespasms: int
    helps_eye_pressure: int
    helps_migraines: int
    helps_asthma: int
    helps_anorexia: int
    helps_arthritis: int
    helps_add_adhd: int
    helps_musculardystrophy: int
    helps_hypertension: int
    helps_glaucoma: int
    helps_pms: int
    helps_seizures: int
    helps_spasticity: int
    helps_spinalcordinjury: int
    helps_fibromyalgia: int
    helps_crohn_s_disease: int
    helps_phantomlimbpain: int
    helps_epilepsy: int
    helps_multiplesclerosis: int
    helps_parkinson_s: int
    helps_tourette_ssyndrome: int
    helps_alzheimer_s: int
    helps_hiv_aids: int
    helps_tinnitus: int




@router.post("/prediccioncepa")
async def prediccionCepa(preferencias_usuario_perfil: PreferenciasUsuario_Perfil, preferencias_usuario_cepa: PreferenciasUsuario_Cepa):
    prediccionPerfil = servicio_PrediccionPerfil.make_prediccion_perfil(preferencias_usuario_perfil)
    prediccionCepa = servicio_PrediccionCepa.make_prediccion_cepa(preferencias_usuario_cepa, prediccionPerfil)
    cepas=[]
    if prediccionCepa[2] == 100:
        cepas.append(prediccionCepa)
        return {"mensaje": "Prediccion Perfecta", "Cepa":cepas}
    elif prediccionCepa[2] < 100:
        perfilesRestantes = [0, 1, 2]
        if prediccionPerfil in perfilesRestantes:
            perfilesRestantes.remove(prediccionPerfil)
        else:
            print("No se encontró el perfil")
        
        cepas.append(servicio_PrediccionCepa.make_prediccion_cepa(preferencias_usuario_cepa, perfilesRestantes[0]))
        cepas.append(servicio_PrediccionCepa.make_prediccion_cepa(preferencias_usuario_cepa, perfilesRestantes[1]))
    
        return {"mensaje": "Prediccion Secundaria", "Cepa":cepas}
