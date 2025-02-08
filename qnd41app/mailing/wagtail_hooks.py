from wagtail import hooks
from wagtail.admin.menu import MenuItem, SubmenuMenuItem
from django.urls import reverse
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet
from .models import EmailCampaign,Usuario  # Tu modelo de campañas de correo


# === 1️⃣ Definir un Snippet ViewSet para EmailCampaign ===
class EmailCampaignViewSet(SnippetViewSet):
    model = EmailCampaign
    icon = "mail"
    menu_label = "Campañas de Correo"
    menu_name = "email_campaigns"

# Registrar el snippet
register_snippet(EmailCampaignViewSet)


# === 1️⃣ Definir un Snippet ViewSet para EmailCampaign ===
class UsuarioViewSet(SnippetViewSet):
    model = Usuario
    icon = "users"
    menu_label = "Usuarios Whatsapp"
    menu_name = "users_whatsapp"

# Registrar el snippet
register_snippet(UsuarioViewSet)




