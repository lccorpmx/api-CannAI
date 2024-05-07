import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

class PrediccionPerfilService:
    def __init__(self):
        self.knn_model_perfiles = None
        self.X_train_perfil = None
        self.Y_train_perfil = None

    def cargar_dataset(self):
        # Cargar el dataset desde el archivo CSV
        dataset = pd.read_csv("dts.csv")
        X_perfil=dataset
        
        # Preprocesar el dataset
        X_perfil = X_perfil.drop(columns=['name', 'cluster', 'helps_stress', 'helps_pain', 'helps_depression', 'helps_anxiety', 'helps_insomnia',
                                  'helps_headache', 'helps_ptsd', 'helps_fatigue', 'helps_lackofappetite', 'helps_nausea',
                                  'helps_headaches', 'helps_bipolar_disorder', 'helps_cancer', 'helps_tingly', 'helps_cramps',
                                  'helps_gastrointestinaldisorder', 'helps_inflammation', 'helps_musclespasms', 'helps_eye_pressure',
                                  'helps_migraines', 'helps_asthma', 'helps_anorexia', 'helps_arthritis', 'helps_add/adhd',
                                  'helps_musculardystrophy', 'helps_hypertension', 'helps_glaucoma', 'helps_pms', 'helps_seizures',
                                  'helps_spasticity', 'helps_spinalcordinjury', 'helps_fibromyalgia', 'helps_crohn’sdisease',
                                  'helps_phantomlimbpain', 'helps_epilepsy', 'helps_multiplesclerosis', 'helps_parkinson’s',
                                  'helps_tourette’ssyndrome', 'helps_alzheimer’s', 'helps_hiv/aids', 'helps_tinnitus'])

        Y_perfil = dataset['cluster']
        # Dividir los datos en conjuntos de entrenamiento y prueba
        self.X_train_perfil, _, self.Y_train_perfil, _ = train_test_split(X_perfil, Y_perfil, test_size=0.2, random_state=65)

    def entrenar_modelo_perfiles(self):
        # Entrenar el modelo KNN
        k = 1  # número de vecinos
        self.knn_model_perfiles = KNeighborsClassifier(n_neighbors=k)
        self.knn_model_perfiles.fit(self.X_train_perfil, self.Y_train_perfil)

    def make_prediccion_perfil(self, preferencias_usuario_perfil):
        if self.knn_model_perfiles is None:
            # Si el modelo KNN no está entrenado, entrena el modelo
            self.cargar_dataset()
            self.entrenar_modelo_perfiles()

        # Realizar la predicción utilizando las preferencias del usuario
        preferencias_usuario = [preferencias_usuario_perfil.feeling_relaxed,
                                preferencias_usuario_perfil.feeling_happy,
                                preferencias_usuario_perfil.feeling_euphoric,
                                preferencias_usuario_perfil.feeling_uplifted,
                                preferencias_usuario_perfil.feeling_sleepy,
                                preferencias_usuario_perfil.feeling_hungry,
                                preferencias_usuario_perfil.feeling_talkative,
                                preferencias_usuario_perfil.feeling_creative,
                                preferencias_usuario_perfil.feeling_energetic,
                                preferencias_usuario_perfil.feeling_focused,
                                preferencias_usuario_perfil.feeling_giggly,
                                preferencias_usuario_perfil.feeling_aroused]

        # Hacer la predicción
        perfil_predicho = self.knn_model_perfiles.predict([preferencias_usuario])

        return perfil_predicho[0].item()


class PrediccionCepaService:
    def __init__(self):
        self.knn_model_cepas = None
        self.X_train_cepa = None
        self.Y_train_cepa = None
        self.dataset = None
        self.perfil = None
        
    def cargar_dataset(self):
        self.dataset = pd.read_csv("dts.csv")
        X_byCluster = self.dataset[self.dataset["cluster"] == self.perfil]
        X_cepa = X_byCluster.drop(columns=['name', 'cluster', 'feeling_relaxed', 'feeling_happy', 'feeling_euphoric', 'feeling_uplifted', 'feeling_sleepy', 'feeling_hungry', 'feeling_talkative', 'feeling_creative', 'feeling_energetic', 'feeling_focused', 'feeling_giggly', 'feeling_aroused'])
        Y_cepa = X_byCluster['name']

        # Dividir los datos en conjuntos de entrenamiento y prueba
        self.X_train_cepa, _, self.Y_train_cepa, _ = train_test_split(X_cepa, Y_cepa, test_size=0.2, random_state=65)

    def entrenar_modelo_cepas(self):
        k = 1
        self.knn_model_cepas = KNeighborsClassifier(n_neighbors=k)
        self.knn_model_cepas.fit(self.X_train_cepa, self.Y_train_cepa)
        

        
    def make_prediccion_cepa(self, preferencias_usuario_cepa, prediccionPerfil):
        self.perfil=prediccionPerfil
        self.cargar_dataset()
        self.entrenar_modelo_cepas()

        # Realizar la predicción utilizando las preferencias del usuario
        preferencias_usuario = [preferencias_usuario_cepa.helps_stress,
                                preferencias_usuario_cepa.helps_pain,
                                preferencias_usuario_cepa.helps_depression,
                                preferencias_usuario_cepa.helps_anxiety,
                                preferencias_usuario_cepa.helps_insomnia,
                                preferencias_usuario_cepa.helps_headache,
                                preferencias_usuario_cepa.helps_ptsd,
                                preferencias_usuario_cepa.helps_fatigue,
                                preferencias_usuario_cepa.helps_lackofappetite,
                                preferencias_usuario_cepa.helps_nausea,
                                preferencias_usuario_cepa.helps_headaches,
                                preferencias_usuario_cepa.helps_bipolar_disorder,
                                preferencias_usuario_cepa.helps_cancer,
                                preferencias_usuario_cepa.helps_tingly,
                                preferencias_usuario_cepa.helps_cramps,
                                preferencias_usuario_cepa.helps_gastrointestinaldisorder,
                                preferencias_usuario_cepa.helps_inflammation,
                                preferencias_usuario_cepa.helps_musclespasms,
                                preferencias_usuario_cepa.helps_eye_pressure,
                                preferencias_usuario_cepa.helps_migraines,
                                preferencias_usuario_cepa.helps_asthma,
                                preferencias_usuario_cepa.helps_anorexia,
                                preferencias_usuario_cepa.helps_arthritis,
                                preferencias_usuario_cepa.helps_add_adhd,
                                preferencias_usuario_cepa.helps_musculardystrophy,
                                preferencias_usuario_cepa.helps_hypertension,
                                preferencias_usuario_cepa.helps_glaucoma,
                                preferencias_usuario_cepa.helps_pms,
                                preferencias_usuario_cepa.helps_seizures,
                                preferencias_usuario_cepa.helps_spasticity,
                                preferencias_usuario_cepa.helps_spinalcordinjury,
                                preferencias_usuario_cepa.helps_fibromyalgia,
                                preferencias_usuario_cepa.helps_crohn_s_disease,
                                preferencias_usuario_cepa.helps_phantomlimbpain,
                                preferencias_usuario_cepa.helps_epilepsy,
                                preferencias_usuario_cepa.helps_multiplesclerosis,
                                preferencias_usuario_cepa.helps_parkinson_s,
                                preferencias_usuario_cepa.helps_tourette_ssyndrome,
                                preferencias_usuario_cepa.helps_alzheimer_s,
                                preferencias_usuario_cepa.helps_hiv_aids,
                                preferencias_usuario_cepa.helps_tinnitus]

        # Hacer la predicción
        cepa_predicha = self.knn_model_cepas.predict([preferencias_usuario])[0]
        
        # Obtener los efectos de la cepa predicha
        efectos_cepa = self.dataset[self.dataset['name'] == cepa_predicha].iloc[:, 1:].to_dict(orient='records')[0]


        efectos_cepa_ordenados = {
            "helps_stress": efectos_cepa.get("helps_stress", 0),
            "helps_pain": efectos_cepa.get("helps_pain", 0),
            "helps_depression": efectos_cepa.get("helps_depression", 0),
            "helps_anxiety": efectos_cepa.get("helps_anxiety", 0),
            "helps_insomnia": efectos_cepa.get("helps_insomnia", 0),
            "helps_headache": efectos_cepa.get("helps_headache", 0),
            "helps_ptsd": efectos_cepa.get("helps_ptsd", 0),
            "helps_fatigue": efectos_cepa.get("helps_fatigue", 0),
            "helps_lackofappetite": efectos_cepa.get("helps_lackofappetite", 0),
            "helps_nausea": efectos_cepa.get("helps_nausea", 0),
            "helps_headaches": efectos_cepa.get("helps_headaches", 0),
            "helps_bipolar_disorder": efectos_cepa.get("helps_bipolar_disorder", 0),
            "helps_cancer": efectos_cepa.get("helps_cancer", 0),
            "helps_tingly": efectos_cepa.get("helps_tingly", 0),
            "helps_cramps": efectos_cepa.get("helps_cramps", 0),
            "helps_gastrointestinaldisorder": efectos_cepa.get("helps_gastrointestinaldisorder", 0),
            "helps_inflammation": efectos_cepa.get("helps_inflammation", 0),
            "helps_musclespasms": efectos_cepa.get("helps_musclespasms", 0),
            "helps_eye_pressure": efectos_cepa.get("helps_eye_pressure", 0),
            "helps_migraines": efectos_cepa.get("helps_migraines", 0),
            "helps_asthma": efectos_cepa.get("helps_asthma", 0),
            "helps_anorexia": efectos_cepa.get("helps_anorexia", 0),
            "helps_arthritis": efectos_cepa.get("helps_arthritis", 0),
            "helps_add_adhd": efectos_cepa.get("helps_add_adhd", 0),
            "helps_musculardystrophy": efectos_cepa.get("helps_musculardystrophy", 0),
            "helps_hypertension": efectos_cepa.get("helps_hypertension", 0),
            "helps_glaucoma": efectos_cepa.get("helps_glaucoma", 0),
            "helps_pms": efectos_cepa.get("helps_pms", 0),
            "helps_seizures": efectos_cepa.get("helps_seizures", 0),
            "helps_spasticity": efectos_cepa.get("helps_spasticity", 0),
            "helps_spinalcordinjury": efectos_cepa.get("helps_spinalcordinjury", 0),
            "helps_fibromyalgia": efectos_cepa.get("helps_fibromyalgia", 0),
            "helps_crohn_s_disease": efectos_cepa.get("helps_crohn_s_disease", 0),
            "helps_phantomlimbpain": efectos_cepa.get("helps_phantomlimbpain", 0),
            "helps_epilepsy": efectos_cepa.get("helps_epilepsy", 0),
            "helps_multiplesclerosis": efectos_cepa.get("helps_multiplesclerosis", 0),
            "helps_parkinson_s": efectos_cepa.get("helps_parkinson_s", 0),
            "helps_tourette_ssyndrome": efectos_cepa.get("helps_tourette_ssyndrome", 0),
            "helps_alzheimer_s": efectos_cepa.get("helps_alzheimer_s", 0),
            "helps_hiv_aids": efectos_cepa.get("helps_hiv_aids", 0),
            "helps_tinnitus": efectos_cepa.get("helps_tinnitus", 0)
        }
        
        def calcular_porcentaje_aproximacion(preferencias_usuario, efectos_cepa_ordenados):
            threshold =sum(preferencias_usuario)
            threshold=threshold/100
            diferencia = [max((a * b, 0))/100 for a, b in zip(preferencias_usuario, efectos_cepa_ordenados.values())]
            error = [1 if elemento != 0 else 0 for elemento in diferencia]
            error = sum(error)
            porcentajeAproximacion = (error*100)/threshold
            return porcentajeAproximacion

        porcentaje_aproximacion = calcular_porcentaje_aproximacion(preferencias_usuario, efectos_cepa_ordenados)

        return cepa_predicha, efectos_cepa, porcentaje_aproximacion,  self.perfil
