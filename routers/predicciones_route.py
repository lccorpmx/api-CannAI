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
    if prediccionCepa[2] == 100:
        return {"Busqueda Perfecta":prediccionCepa}
    elif prediccionCepa[2] > 85:
        return {"Busqueda Casi Perfecta": prediccionCepa}
    elif prediccionCepa[2] > 70:
        return {"Busqueda Acertada": prediccionCepa}
    else:
        
        perfilesRestantes=[0,1,2]
        if prediccionPerfil in perfilesRestantes:
            perfilesRestantes.remove(prediccionPerfil)
        else:
            print("No se encontro el perfil")
            
        prediccionCepa_primeraPosicionPerfil = servicio_PrediccionCepa.make_prediccion_cepa(preferencias_usuario_cepa, perfilesRestantes[0])
        segundaCepa_primeraPosicionPerfil = servicio_PrediccionCepa.make_prediccion_cepa(preferencias_usuario_cepa, perfilesRestantes[1])
        
        if prediccionCepa_primeraPosicionPerfil[2] < 85:
            return {"mensaje": "Busqueda Alterna", "prediccion": prediccionCepa_primeraPosicionPerfil}
        elif segundaCepa_primeraPosicionPerfil[2] < 85:
            return {"mensaje": "Busqueda Alterna", "prediccion": segundaCepa_primeraPosicionPerfil}
        else:
            return {"mensaje": "Se encontraron pocas coincidencias, estos fueron los resultados", "prediccion1": prediccionCepa_primeraPosicionPerfil, "prediccion2": segundaCepa_primeraPosicionPerfil}