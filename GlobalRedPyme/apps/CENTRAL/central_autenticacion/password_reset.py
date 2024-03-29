# lib token
from django_rest_passwordreset.serializers import EmailSerializer
from django_rest_passwordreset.models import ResetPasswordToken, clear_expired, get_password_reset_token_expiry_time, \
    get_password_reset_lookup_field
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import get_user_model
# lib email
from apps.config.util import sendEmail
# lib reseteo contraseña
from django_rest_passwordreset.signals import reset_password_token_created
from django.dispatch import receiver
from django.urls import reverse
from ...config import config
from rest_framework.response import Response
from rest_framework import status
# Importar serializers empresa y base de datos empresa
from ...CORP.corp_empresas.models import Empresas
from ...CORP.corp_empresas.serializers import EmpresasSerializer
from ..central_usuarios.models import UsuariosEmpresas
# permisos
from ...CENTRAL.central_roles.models import RolesUsuarios
from ...CENTRAL.central_roles.serializers import ListRolesSerializer
# ObjectId
from bson import ObjectId


def resetPasswordNewUser(emailUsuario):
    try:
        User = get_user_model()
        # asignamos el email mandado
        email = emailUsuario
        # borra los tokens expirados
        password_reset_token_validation_time = get_password_reset_token_expiry_time()
        # datetime.now minus expiry hours
        now_minus_expiry_time = timezone.now() - timedelta(hours=password_reset_token_validation_time)
        # borramos los tokens que han pasado mas de 24 horas
        clear_expired(now_minus_expiry_time)
        # buscamos el email del usuario
        users = User.objects.filter(**{'{}__iexact'.format(get_password_reset_lookup_field()): email})
        active_user_found = False
        # iterate over all users and check if there is any user that is active
        # also check whether the password can be changed (is useable), as there could be users that are not allowed
        # to change their password (e.g., LDAP user)
        for user in users:
            if user.eligible_for_reset():
                active_user_found = True
        # Si no esta el usuario activo No enviamos el email
        if not active_user_found:
            return False
        # last but not least: iterate over all users that are active and can change their password
        # and create a Reset Password Token and send a signal with the created token
        for user in users:
            if user.eligible_for_reset():
                # define the token as none for now
                token = None
                # check if the user already has a token
                if user.password_reset_tokens.all().count() > 0:
                    # yes, already has a token, re-use this token
                    token = user.password_reset_tokens.all()[0]
                else:
                    # no token exists, generate a new token
                    token = ResetPasswordToken.objects.create(
                        user=user,
                        user_agent='ADMINISTRADOR',
                        ip_address='',
                    )
                # send a signal that the password token was created
                # let whoever receives this signal handle sending the email for the password reset
                # reset_password_token_created.send(sender=self.__class__, instance=self, reset_password_token=token)
                if enviarEmailAsignacionPassword(token):
                    return str(token.key)
                return 'Token no generado'
        # done
    except Exception as e:
        return 'Ocurrió un error, Token no generado: {}'.format(e)
    # email


def enviarEmailAsignacionPassword(reset_password_token):
    try:
        # enviar por email
        if reset_password_token.user.tipoUsuario.nombre == 'core':
            url = config.API_FRONT_END_CENTRAL + config.endpointEmailReseteoPassword + "?token=" + reset_password_token.key + "&email=" + reset_password_token.user.email
        elif reset_password_token.user.tipoUsuario.nombre == 'credit':
            url = config.API_FRONT_END_CREDIT + config.endpointEmailReseteoPassword + "?token=" + reset_password_token.key + "&email=" + reset_password_token.user.email
        elif reset_password_token.user.tipoUsuario.nombre == 'corp':
            url = config.API_FRONT_END_CORP_BP + config.endpointEmailReseteoPassword + "?token=" + reset_password_token.key + "&email=" + reset_password_token.user.email
        else:
            url = config.API_FRONT_END + config.endpointEmailAsignacionPassword + "?token=" + reset_password_token.key + "&email=" + reset_password_token.user.email
        # url=config.API_FRONT_END+config.endpointEmailAsignacionPassword+"?token="+reset_password_token.key+"&email="+reset_password_token.user.email
        if reset_password_token.user.tipoUsuario.nombre == 'corp':
            empresa = UsuariosEmpresas.objects.filter(usuario=reset_password_token.user).first()
            empresaSerializer = EmpresasSerializer(Empresas.objects.filter(_id=ObjectId(empresa.empresa_id)).first()).data
            rolesUsuario = RolesUsuarios.objects.filter(usuario=reset_password_token.user, state=1)
            roles = ListRolesSerializer(rolesUsuario, many=True).data
            subject, from_email, to = f"""Creación de Cuenta CORP - {empresaSerializer['nombreEmpresa']}""", "credicompra.bigpuntos@corporacionomniglobal.com", reset_password_token.user.email
            txt_content = f"""
                REGISTRO DE CUENTA
                Estimad@ 
                Usted ha sido registrad@ por {empresaSerializer['nombreEmpresa']} para {roles[0]['descripcion']}
                Para completar su registro Haga click en el siguiente enlace: {url}
                Si el enlace no funciona, copie el siguiente link en una ventana del navegador: {url}
                Atentamente,
                CrediCompra-BigPuntos.
            """
            html_content = f"""
                    <html>
                        <body>
                            <h1>REGISTRO DE CUENTA</h1>
                            Estimad@ 
                            
                            Usted ha sido registrad@ por {empresaSerializer['nombreEmpresa']} para {roles[0]['descripcion']}
                             
                            Para completar su registro Haga click en el siguiente enlace: <a href='{url}'>CLICK AQUÍ</a><br><br>

                            Si el enlace no funciona, copie el siguiente link en una ventana del navegador: {url}<br><br>

                            Atentamente,<br>
                            CrediCompra-BigPuntos.<br>
                        </body>
                    </html>
                    """
        else:
            subject, from_email, to = 'CREACIÓN DE CUENTA CREDICOMPRA-BIG PUNTOS', "credicompra.bigpuntos@corporacionomniglobal.com", reset_password_token.user.email
            txt_content = f"""
                            REGISTRO DE CUENTA
                            Para completar su registro Haga click en el siguiente enlace: {url}
                            Si el enlace no funciona, copie el siguiente link en una ventana del navegador: {url}
                            Atentamente,
                            CrediCompra-BigPuntos.
                    """
            html_content = f"""
                    <html>
                        <body>
                            <h1>REGISTRO DE CUENTA</h1>
                            Para completar su registro Haga click en el siguiente enlace: <a href='{url}'>CLICK AQUÍ</a><br><br>

                            Si el enlace no funciona, copie el siguiente link en una ventana del navegador: {url}<br><br>

                            Atentamente,<br>
                            CrediCompra-BigPuntos.<br>
                        </body>
                    </html>
                    """
        if sendEmail(subject, txt_content, from_email, to, html_content):
            return True
        return False
    except:
        return False


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    try:
        # enviar por email
        # email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
        if reset_password_token.user.tipoUsuario.nombre == 'core':
            url = config.API_FRONT_END_CENTRAL + config.endpointEmailReseteoPassword + "?token=" + reset_password_token.key + "&email=" + reset_password_token.user.email
        elif reset_password_token.user.tipoUsuario.nombre == 'credit':
            url = config.API_FRONT_END_CREDIT + config.endpointEmailReseteoPassword + "?token=" + reset_password_token.key + "&email=" + reset_password_token.user.email
        else:
            url = config.API_FRONT_END + config.endpointEmailAsignacionPassword + "?token=" + reset_password_token.key + "&email=" + reset_password_token.user.email
        subject, from_email, to = 'RESETEO DE CONTRASEÑA DE CREDICOMPRA-BIG PUNTOS', "credicompra.bigpuntos@corporacionomniglobal.com", reset_password_token.user.email
        txt_content = f"""
                RESETEO DE CONTRASEÑA
                
                Para resetear su contraseña de CrediCompra-Big Puntos, Haga click en el siguiente enlace: {url}
                
                En caso de que el enlace no funcione, copie el enlace en una nueva ventana. {url}
                
                Atentamente,
                CrediCompra-BigPuntos.
        """
        html_content = f"""
        <html>
            <body>
                <h1>RESETEO DE CONTRASEÑA</h1>
                
                Para resetear su contraseña de CrediCompra-Big Puntos, Haga click en el siguiente enlace: <a href='{url}'>Clic Aquí!</a><br><br>
                
                En caso de que el enlace no funcione, copie el enlace en una nueva ventana. {url}<br><br>
                
                Atentamente,<br>
                CrediCompra-BigPuntos.<br>
            </body>
        </html>
        """
        sendEmail(subject, txt_content, from_email, to, html_content)

        # enviar por numero de whatsapp
        # numWhatsapp=reset_password_token.user.whatsapp
        # if numWhatsapp:
        #     #aqui codigo de whatsapp
        #     print(numWhatsapp)
        # else:
        #     print('No posee num whatsapp')
    except Exception as e:
        err = {"error": 'Un error ha ocurrido: {}'.format(e)}
        return Response(err, status=status.HTTP_400_BAD_REQUEST)


def enviarEmailCreacionPersona(email):
    try:
        # enviar por email
        subject, from_email, to = 'Creación de usuario Global Red Pymes Personas', "credicompra.bigpuntos@corporacionomniglobal.com", email
        txt_content = """
                Registro de usuario Global Red Pymes Personas
                Felicidades usted se acaba de registrar a la plataforma de Global Red Pymes Personas.
                
                Atentamente,
                Equipo Global Red Pymes Personas.
        """
        html_content = """
        <html>
            <body>
                <h1>Registro de usuario Global Red Pymes Personas</h1>
                Felicidades usted se acaba de registrar a la plataforma de Global Red Pymes Personas.
                <br>
                Atentamente,<br>
                Equipo Global Red Pymes Personas.<br>
            </body>
        </html>
        """
        if sendEmail(subject, txt_content, from_email, to, html_content):
            return True
        return False
    except:
        return False
