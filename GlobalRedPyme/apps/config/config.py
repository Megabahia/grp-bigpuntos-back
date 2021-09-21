PRODUCTION=False

#VARIABLES GLOBALES
endpointEmailAsignacionPassword="/auth/usuario/asignacionPassword/"
endpointEmailReseteoPassword="/auth/usuario/reseteoPassword/"

#VARIABLES VARIAN DE ACUERDO A PRODUCCION O DESARROLLO
if PRODUCTION:
    # URL BACK END
    API_BACK_END = '209.145.61.41:8000/'
    #URL FRONT END
    API_FRONT_END="209.145.61.41:4200"
    #TIEMPO DE EXPIRACION DE TOKEN (EN SEGUNDOS)
    TOKEN_EXPIRED_AFTER_SECONDS = 86400
    #NOMBRE KEYWORK TOKEN
    TOKEN_KEYWORD= 'Bearer'
    # This will display email in Console.
    EMAIL_HOST = ''
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_PORT = ''
    #CORS
    CORS_ALLOWED_ORIGINS = [
        "http://209.145.61.41:4200",
        "http://127.0.0.1:4200"
    ]
    #databases
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'vittoria_adm',
            'USER': 'usr_maintainer',
            'PASSWORD': 'Tc2;1EE{DBE^oN',
            'HOST': '209.145.61.41',
            'PORT': 3306
        },
        'vittoria_mdm_db': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'vittoria_mdm',
            'USER': 'usr_maintainer',
            'PASSWORD': 'Tc2;1EE{DBE^oN',
            'HOST': '209.145.61.41',
            'PORT': 3306
        }
    }
else:
    # URL BACK END
    API_BACK_END = 'http://127.0.0.1:8000/'
    #URL FRONT END
    API_FRONT_END="localhost:4200"
    #TIEMPO DE EXPIRACION DE TOKEN (EN SEGUNDOS)
    TOKEN_EXPIRED_AFTER_SECONDS = 86400
    #NOMBRE KEYWORK TOKEN
    TOKEN_KEYWORD= 'Bearer'
    # This will display email in Console.
    EMAIL_HOST = 'smtp.mailtrap.io'
    EMAIL_HOST_USER = 'f464f6bf1e30a6'
    EMAIL_HOST_PASSWORD = '1f662090e649b0'
    EMAIL_PORT = '2525'
    #CORS
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:4200",
        "http://127.0.0.1:4200"
    ]
    #databases
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'grp_central',
            'ENFORCE_SCHEMA': False,
        },
        'grp_personas_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_personas',
            'ENFORCE_SCHEMA': False,
        },
        'grp_core_db': {
            'ENGINE': 'djongo',
            'NAME': 'grp_core',
            'ENFORCE_SCHEMA': False,
        }
    }
