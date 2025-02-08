from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.fields import StreamField, RichTextField



class Usuario(models.Model):
    telefono = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    historial = models.TextField(default="")  # Guardamos el historial del usuario

    def __str__(self):
        return f"{self.nombre or 'Usuario'} ({self.telefono})"


class Mensaje(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensaje = models.TextField()
    respuesta = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.usuario.telefono} en {self.timestamp}"



class EmailCampaign(models.Model):
    subject = models.CharField("Asunto", max_length=255)
    recipient = models.EmailField("Destinatario")
    message = RichTextField("Mensaje")
    send_date = models.DateTimeField("Fecha de envío")
    sent = models.BooleanField("Enviado", default=False)

    panels = [
        FieldPanel("subject"),
        FieldPanel("recipient"),
        FieldPanel("message"),
        FieldPanel("send_date"),
        FieldPanel("sent"),
    ]

    def __str__(self):
        return f"{self.subject} ({'Enviado' if self.sent else 'Pendiente'})"
