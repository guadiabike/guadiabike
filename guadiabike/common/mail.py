# -*- coding: UTF-8-*-
__author__ = 'Antonio'


class MailTemplate(object):

    def __init__(self, title, contenido):
        self.titulo = title
        self.contenido = contenido

    def getMail(self):
        mail = '''
        <html>
        <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>Información Guadiabike BTT</title>
        <style type="text/css">
        #outlook a{padding:0;}
        body{width:100% !important; font-family: Sans-serif; font-size: 10px; color: #333; background-color: #efefef;} .ReadMsgBody{width:100%;} .ExternalClass{width:100%;}
        body{-webkit-text-size-adjust:none;}
        </style>
        </head>

        <body leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" offset="0">

        <div style="font-size: 32px; width: 100%; background-color: #f9540c; color: white; padding-left: 5%; line-height: 2em;">Guadiabike</div>
        <center>
        <div style="background: -webkit-gradient(linear, left top, left bottom, from(#fdfdfd), to(#efefef));">
        <table border="0" width="90%">
            <tr><td style="padding-top: 10px; padding-bottom: 10px; font-size: 24px; "><p>%titulo%</p></td></tr>
            <tr><td>
                <div style="border: 1px solid grey; padding: 20px; background-color: white;">
                    %cuerpo%
                </div>
            </td></tr>
            <tr><td>
                <br>
                <div style="font-size:11px; color:#666666; background-color:#f8f8f8; padding:1px 20px; border-top: 8px solid #f9540c; ">
                <p style="text-align: justify;">El contenido de este correo electrónico, incluidos sus documentos/datos adjuntos, está dirigido única y exclusivamente a su destinatario y podría tener el carácter de confidencial. Si Vd. hubiera recibido este correo electrónico por error en ningún caso deberá revelar, difundir o copiar su contenido rogándole que comunique dicha circunstancia a su remitente por esta misma vía y que proceda a su destrucción de forma inmediata.</p>
                <p style="text-align: justify;">El correo electrónico no es un medio de transmisión infalible, no pudiendo en consecuencia quedar garantizada su seguridad. Por ello, Guadiabike BTT en ningún caso podrá ser considerada responsable de una posible recepción incompleta o incorrecta de este correo electrónico, de cualquier demora en la recepción citada así como de cualquier otra incidencia que pudiera acontecer en relación con este correo electrónico.</p>
                <p style="text-align: justify;">The contents of this message including any attachments are intended solely for the use of the person to whom it is addressed and may be confidential. If you have received this message by error, the disclosing, copying or distributing of it is strictly prohibited. Please notify the aforementioned error to the sender immediately via e-mail and proceed to delete this message from your system.</p>
                <p style="text-align: justify;">Communication via e-mail is not infallible. As a consequence, secure communications cannot be guaranteed. Guadiabike BTT accepts no liability for the possible event of an incomplete or incorrect receipt of this message. Furthermore, Randstad accepts no liability for the delay in the receipt of this message nor any other incident derived from this message.</p>
                </div>
            </td></tr>
        </table>
        </div>

        </center>
        </body>
        </html>'''

        mail = mail.replace('%titulo%', self.titulo)
        mail = mail.replace('%contenido%', self.contenido)

        return mail


class InvitationMail(MailTemplate):

    def __init__(self, nombre, url):
        self.nombre = nombre
        self.url = url
        self.contenido = self.getContenido()

        super(MailTemplate, self).__init__('Invitación en Guadiabike BTT', self.contenido)

    def getContenido(self):
        content = '<p>Hola <b>' + self.nombre + '</b>.<br><br></p>'
        content += '<p>El club <i>Guadiabike BTT</i> le invita a darse de alta en su aplicación web.</p>'
        content += '<p>Pulsa <a href="' + self.url + '">aquí</a> para acceder.</p><br>'
        content += '<p style="font-size: 10px;">Guadiabike BTT</p>'
        content += '<p style="font-size: 10px;">guadiabike.info@gmail.com</p>'

        return content