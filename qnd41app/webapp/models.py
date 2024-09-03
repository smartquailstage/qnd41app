import datetime
from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils.functional import cached_property
from django.http import Http404
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
)
from wagtail.models import Page, Orderable
from wagtail.snippets.models import register_snippet
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.fields import StreamField, RichTextField
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.search import index
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.images.models import Image

# Modelo para los campos del formulario de la página de inicio
class ConsultasHome(AbstractFormField):
    page = ParentalKey('Home', on_delete=models.CASCADE, related_name='form_fields')

# Modelo para la página de inicio
class Home(AbstractEmailForm):
    template = "webapp/home/home.html"

    # Campos de texto para banners
    banner_title4 = RichTextField(blank=True, verbose_name='Título de galería-1')
    TS_info1 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Subtítulo info')
    info1 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Info')

    banner_title5 = RichTextField(blank=True, verbose_name='Título de galería-2')
    TS_info2 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Subtítulo-2 info')
    info2 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Info-2')

    banner_title6 = RichTextField(blank=True, verbose_name='Título de galería-3')
    TS_info3 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Subtítulo-3 info')
    info3 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Info-3')

    banner_title7 = RichTextField(blank=True, verbose_name='Título de galería-4')
    TS_info4 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Subtítulo-4 info')
    info4 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Info-4')

    banner_title8 = RichTextField(blank=True, verbose_name='Título de galería-5')
    TS_info5 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Subtítulo-5 info')
    info5 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Info-5')

    banner_title9 = RichTextField(blank=True, verbose_name='Título de galería-6')
    TS_info6 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Subtítulo-6 info')
    info6 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Info-6')

    # Campos de texto para banners de callout
    banner_title10 = RichTextField(blank=True, verbose_name='Mejoramos')
    info7 = models.CharField(max_length=150, null=True, blank=True, verbose_name='IT Business Analytics')
    info8 = models.CharField(max_length=150, null=True, blank=True, verbose_name='IT Business Cloud DevOps')
    info9 = models.CharField(max_length=150, null=True, blank=True, verbose_name='IT Business Media')

    # Campos de productos
    product_1 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Producto-1')
    product_description_1 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Descripción Producto-1')

    product_2 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Producto-2')
    product_description_2 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Descripción Producto-2')

    product_3 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Producto-3')
    product_description_3 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Descripción Producto-3')

    product_4 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Producto-4')
    product_description_4 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Descripción Producto-4')

    product_5 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Producto-5')
    product_description_5 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Descripción Producto-5')

    product_6 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Producto-6')
    product_description_6 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Descripción Producto-6')

    # Campos de contador
    numero_coffe = models.IntegerField(null=True, blank=True)
    numero_experiencia = models.IntegerField(null=True, blank=True)
    numero_horas = models.IntegerField(null=True, blank=True)
    numero_wins = models.IntegerField(null=True, blank=True)

    # Campos del equipo
    team_1 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Equipo-1')
    team_descrp_1 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Descripción Equipo-1')

    team_2 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Equipo-2')
    team_descrp_2 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Descripción Equipo-2')

    team_3 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Equipo-3')
    team_descrp_3 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Descripción Equipo-3')

    team_4 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Equipo-4')
    team_descrp_4 = models.CharField(max_length=150, null=True, blank=True, verbose_name='Descripción Equipo-4')

    # Campos adicionales
    banner_title = models.CharField(max_length=150, null=True, blank=True, verbose_name='Título de llamada a la acción')
    slogan = models.CharField(max_length=150, null=True, blank=True, verbose_name='Slogan')
    slogan_descriptcion = models.CharField(max_length=150, null=True, blank=True, verbose_name='Descripción del Slogan')
    custom_title = models.CharField(max_length=100, blank=True, null=True, help_text="Reescribe el Título de la publicación")
    consulta = RichTextField(blank=True, verbose_name='Mensaje para consulta')
    thank_you_text = RichTextField(blank=True)

    # Paneles de administración
    content_panels = AbstractEmailForm.content_panels + Page.content_panels + [
        # Panel de sliders
        FieldPanel('banner_title4'),
        FieldPanel('TS_info1'),
        FieldPanel('info1'),
        FieldPanel('banner_title5'),
        FieldPanel('TS_info2'),
        FieldPanel('info2'),
        FieldPanel('banner_title6'),
        FieldPanel('TS_info3'),
        FieldPanel('info3'),
        FieldPanel('banner_title7'),
        FieldPanel('TS_info4'),
        FieldPanel('info4'),
        FieldPanel('banner_title8'),
        FieldPanel('TS_info5'),
        FieldPanel('info5'),
        FieldPanel('banner_title9'),
        FieldPanel('TS_info6'),
        FieldPanel('info6'),
        FieldPanel('banner_title10'),
        FieldPanel('info7'),
        FieldPanel('info8'),
        FieldPanel('info9'),

        # Paneles de productos
        FieldPanel('product_1'),
        FieldPanel('product_description_1'),
        FieldPanel('product_2'),
        FieldPanel('product_description_2'),
        FieldPanel('product_3'),
        FieldPanel('product_description_3'),
        FieldPanel('product_4'),
        FieldPanel('product_description_4'),
        FieldPanel('product_5'),
        FieldPanel('product_description_5'),
        FieldPanel('product_6'),
        FieldPanel('product_description_6'),

        # Paneles de contador
        FieldPanel('numero_coffe'),
        FieldPanel('numero_experiencia'),
        FieldPanel('numero_horas'),
        FieldPanel('numero_wins'),

        # Paneles del equipo
        FieldPanel('team_1'),
        FieldPanel('team_descrp_1'),
        FieldPanel('team_2'),
        FieldPanel('team_descrp_2'),
        FieldPanel('team_3'),
        FieldPanel('team_descrp_3'),
        FieldPanel('team_4'),
        FieldPanel('team_descrp_4'),

        # Paneles adicionales
        FieldPanel('banner_title'),
        FieldPanel('slogan'),
        FieldPanel('slogan_descriptcion'),
        FieldPanel('consulta'),
        FieldPanel('custom_title'),
        FieldPanel('thank_you_text'),

        # Paneles de formulario
        InlinePanel('galleria', label="Imagen de Fondo Banner"),
        InlinePanel('form_fields', label="Campos del formulario"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], heading="Email")
    ]

# Modelo para la galería de la página de inicio
class GaleriaHome(Orderable):
    page = ParentalKey(Home, on_delete=models.CASCADE, related_name='galleria')
    logo = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Logotipo SmartQuail')
    profile_pic = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Foto de perfil')
    image = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 1')
    image_2 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 2')
    image_3 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 3')
    image_4 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 4')
    image_5 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 5')
    image_6 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 6')
    image_7 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 7')
    image_8 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 8')
    image_9 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 9')
    image_10 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 10')
    image_11 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 11')
    image_12 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 11')
    image_13 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 11')
    image_14 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 11')
    image_15 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 11')
    image_16 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 11')
    image_17 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 11')
    image_18 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 11')
    image_19 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 11')
    image_20 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 11')
    image_21 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 11')
    image_22 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 11')
    image_23 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 11')
    image_24 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 11')
    image_25 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 11')
    image_26 = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+', verbose_name='Imagen Slide Banner 11')

    # Paneles de administración para la galería
    panels = [
        FieldPanel('logo'),
        FieldPanel('profile_pic'),
        FieldPanel('image'),
        FieldPanel('image_2'),
        FieldPanel('image_3'),
        FieldPanel('image_4'),
        FieldPanel('image_5'),
        FieldPanel('image_6'),
        FieldPanel('image_7'),
        FieldPanel('image_8'),
        FieldPanel('image_9'),
        FieldPanel('image_10'),
        FieldPanel('image_11'),
        FieldPanel('image_12'),
        FieldPanel('image_13'),
        FieldPanel('image_14'),
        FieldPanel('image_15'),
        FieldPanel('image_16'),
        FieldPanel('image_17'),
        FieldPanel('image_18'),
        FieldPanel('image_19'),
        FieldPanel('image_20'),
        FieldPanel('image_21'),
        FieldPanel('image_22'),
        FieldPanel('image_23'),
        FieldPanel('image_24'),
        FieldPanel('image_25'),
        FieldPanel('image_26'),

    ]

@register_setting
class SocialMediaSettings(BaseSiteSetting):
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    pinterest = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("facebook"),
                FieldPanel("twitter"),
                FieldPanel("instagram"),
                FieldPanel("youtube"),
                FieldPanel("pinterest"),
                FieldPanel("linkedin"),
            ],
            heading="Configuración de Redes Sociales"
        )
    ]


class info(Page):
    # Empieza Barner de Inicio
    template = "webapp/info.html"
    #cliente_Navbar = RichTextField(blank=True,verbose_name='Cliente-url')
    
   # banner_title1 = RichTextField(blank=True,verbose_name='Titulo del primer banner ')
   # banner_info1 = RichTextField(blank=True,verbose_name='Informacion del primer banner ')
   # banner_title2 = RichTextField(blank=True,verbose_name='Titulo del segundo banner ')
   # banner_info2 = RichTextField(blank=True,verbose_name='Informacion del segundo banner ')
   # banner_title3 = RichTextField(blank=True,verbose_name='Titulo del tercer banner ')
   # banner_info3 = RichTextField(blank=True,verbose_name='Informacion del tercer banner ')

    # Empieza Banner de sliders
    bio2 = RichTextField(blank=True,verbose_name='Frase relevante primer parrafo')
    bio3 = RichTextField(blank=True,verbose_name='Frase relevante segundo parrafo')
    author_name = models.CharField(max_length=150, null=True, blank=True,verbose_name='Nombre de autor')
    business_title = models.CharField(max_length=150, null=True, blank=True,verbose_name='Titulo de autor en el negocio')
    business_activiy = models.CharField(max_length=150, null=True, blank=True,verbose_name='Actividad de autor en el negocio')
    business_experience = models.CharField(max_length=150, null=True, blank=True,verbose_name='años de experiencia de autor en el negocio')
    updated = models.CharField(max_length=150, null=True, blank=True,verbose_name='Fecha de ultima actualización')

    banner_title4 = RichTextField(blank=True,verbose_name='Titulo de galeria-1 ')
    TS_info1 = models.CharField(max_length=150, null=True, blank=True,verbose_name='project_info')
    TS_info2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='project_info2')
    TS_info3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='project2_info')
    info3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='project2_info2')

    TS_info4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='project3_info')
    info4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='project3_info2')
    TS_info5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='project4_info')
    info5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='project4_info2')


    banner_title9 = RichTextField(blank=True,verbose_name='Titulo de parrafo')
    TS_info6 = models.CharField(max_length=350, null=True, blank=True,verbose_name='Subtitulo de parrafo')
    info_title9 = RichTextField(blank=True,verbose_name='Texto')

    banner_title10 = RichTextField(blank=True,verbose_name='Titulo de parrafo-2')
    TS_info7 = models.CharField(max_length=350, null=True, blank=True,verbose_name='Subtitulo de parrafo-2')
    info_title10 = RichTextField(blank=True,verbose_name='Texto-2')

    banner_title11 = RichTextField(blank=True,verbose_name='Titulo de parrafo-3')
    TS_info8 = models.CharField(max_length=350, null=True, blank=True,verbose_name='Subtitulo de parrafo-3')
    info_title11 = RichTextField(blank=True,verbose_name='Texto-3')
    info_title12 = RichTextField(blank=True,verbose_name='Descripcion de producto')

    banner_title13 = RichTextField(blank=True,verbose_name='Titulo de parrafo-3')
    info_title13 = RichTextField(blank=True,verbose_name='Descripcion de producto')
    banner_title14 = RichTextField(blank=True,verbose_name='Titulo de parrafo-3')
    info_title14 = RichTextField(blank=True,verbose_name='Descripcion de producto')

    banner_title15 = RichTextField(blank=True,verbose_name='Titulo de parrafo-3')
    info_title15 = RichTextField(blank=True,verbose_name='Descripcion de producto')


    link1 = RichTextField(blank=True,verbose_name='link-para empezar proyecto')
    link2 = RichTextField(blank=True,verbose_name='link-para contactos')

    banner_title12 = RichTextField(blank=True,verbose_name='invitacion a contactarnos')


    custom_title = models.CharField(max_length=100,blank=True,null=True,help_text="Reescribe el  Titulo de la publicacion ")


    
    # Campos de consulta

    consulta= RichTextField(blank=True,verbose_name='Mensaje para que nos consulten por el formulario')
    thank_you_text = RichTextField(blank=True)
    # galeria de imagenes barner de presentacion

    content_panels = AbstractEmailForm.content_panels + Page.content_panels + [


    #Panel sliders
        FieldPanel('bio2', classname="full"),
        FieldPanel('bio3', classname="full"),

        FieldPanel('author_name', classname="full"),
        FieldPanel('business_title', classname="full"),
        FieldPanel('business_activiy', classname="full"),
        FieldPanel('business_experience', classname="full"),
        FieldPanel('updated', classname="full"),

        FieldPanel('banner_title4', classname="full"),
        FieldPanel('TS_info1', classname="full"),
        FieldPanel('TS_info2', classname="full"),
        FieldPanel('TS_info3', classname="full"),
        FieldPanel('info3', classname="full"),
        FieldPanel('TS_info4', classname="full"),
        FieldPanel('info4', classname="full"),
        FieldPanel('TS_info5', classname="full"),
        FieldPanel('info5', classname="full"),
        FieldPanel('banner_title9', classname="full"),
        FieldPanel('TS_info6', classname="full"),
        FieldPanel('info_title9', classname="full"),
        FieldPanel('banner_title10', classname="full"),
        FieldPanel('TS_info7', classname="full"),
        FieldPanel('info_title10', classname="full"),
        FieldPanel('banner_title11', classname="full"),
        FieldPanel('info_title11', classname="full"),
        FieldPanel('banner_title12', classname="full"),
        FieldPanel('info_title12', classname="full"),
        FieldPanel('banner_title13', classname="full"),
        FieldPanel('info_title13', classname="full"),
        FieldPanel('banner_title14', classname="full"),
        FieldPanel('info_title14', classname="full"),
        FieldPanel('banner_title15', classname="full"),
        FieldPanel('info_title15', classname="full"),
        FieldPanel('TS_info8', classname="full"),
        
        FieldPanel('link1', classname="full"),
        FieldPanel('link2', classname="full"),
   
#panel 
        FieldPanel('consulta', classname="full"),
        InlinePanel('galleria_3', label="Imagen de Fondo Barner"),
#Panel capo de noticas
        FieldPanel("custom_title"),
    ]

class GaleriadeImagenes(Orderable):
    page = ParentalKey(info, on_delete=models.CASCADE, related_name='galleria_3')
    banner_background = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Backgound en slide')
    logo_slide = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo en slide')
    logo = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo en texto ')
    profile_pic = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto de perfil')
    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 1')
    image_1 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 1')
    image_2_2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 1')
    image_2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 2')
    image_3_3 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 1')

    image_3 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 3')
    image_4_4 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 1')
    image_4 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 4')


    panels = [
        FieldPanel('banner_background'),
        FieldPanel('logo_slide'),
        FieldPanel('logo'),
        FieldPanel('profile_pic'),
        FieldPanel('image'),
        FieldPanel('image_2'),
        FieldPanel('image_3'),
        FieldPanel('image_4'),
        FieldPanel('image_1'),
        FieldPanel('image_2_2'),
        FieldPanel('image_3_3'),
        FieldPanel('image_4_4'),
    ]

@register_setting
class GlobalLinksSettings(BaseSiteSetting):
    contacus = models.URLField(blank=True,null=True,help_text="")
    start_project_SBM = models.URLField(blank=True,null=True,help_text="")
    start_project_SBL = models.URLField(blank=True,null=True,help_text="")
    start_project_SBA = models.URLField(blank=True,null=True,help_text="")
    start_project_SBT = models.URLField(blank=True,null=True,help_text="")


    panels = [
        MultiFieldPanel(
            [
            FieldPanel("contacus"),
            FieldPanel("start_project_SBM"),
            FieldPanel("start_project_SBL"),
            FieldPanel("start_project_SBA"),  
            FieldPanel("start_project_SBT"),         
            ]
        ,heading= "Global Links Settings")
    ]


class createitbusiness(Page):
    # Empieza Barner de Inicio
    template = "webapp/createitbusiness/createitbusiness.html"
    #cliente_Navbar = RichTextField(blank=True,verbose_name='Cliente-url')
    
   # banner_title1 = RichTextField(blank=True,verbose_name='Titulo del primer banner ')
   # banner_info1 = RichTextField(blank=True,verbose_name='Informacion del primer banner ')
   # banner_title2 = RichTextField(blank=True,verbose_name='Titulo del segundo banner ')
   # banner_info2 = RichTextField(blank=True,verbose_name='Informacion del segundo banner ')
   # banner_title3 = RichTextField(blank=True,verbose_name='Titulo del tercer banner ')
   # banner_info3 = RichTextField(blank=True,verbose_name='Informacion del tercer banner ')

    # Empieza Banner de sliders
    bio = RichTextField(blank=True,verbose_name='reseña bibliografica')

    banner_title4 = RichTextField(blank=True,verbose_name='Titulo de galeria-1 ')
    TS_info1 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Subtitulo info')
    info1 = models.CharField(max_length=150, null=True, blank=True,verbose_name='info')
    banner_title5 = RichTextField(blank=True,verbose_name='Titulo de galeria-2  ')
    TS_info2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Subtitulo-2 info')
    info2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='info-2')
    banner_title6 = RichTextField(blank=True,verbose_name='Titulo de galeria-3  ')
    TS_info3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Subtitulo-3 info')
    info3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='info-3')
    banner_title7 = RichTextField(blank=True,verbose_name='Titulo de galeria-4  ')
    TS_info4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Subtitulot-4 info')
    info4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='info-4')
    banner_title8 = RichTextField(blank=True,verbose_name='Titulo de galeria-5  ')
    TS_info5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Subtitulo-5 info')
    info5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='info-5')
    banner_title9 = RichTextField(blank=True,verbose_name='Titulo de galeria-6  ')
    TS_info6 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Subtitulo-6 info')
    info6 = models.CharField(max_length=150, null=True, blank=True,verbose_name='info-6')


    # Empieza Banner de callout
    banner_title10 = RichTextField(blank=True,verbose_name='we improve')
    info7 = models.CharField(max_length=150, null=True, blank=True,verbose_name='IT business analytics')
    info8 = models.CharField(max_length=150, null=True, blank=True,verbose_name='IT business cloud DevOps')
    info9 = models.CharField(max_length=150, null=True, blank=True,verbose_name='IT business Media')
    
    # Empieza Banner de Products

  
    product_1 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Product-1')
    product_description_1 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Descripcion Product-1')
    product_2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Product-2')
    product_description_2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Descripcion Product-2')
    product_3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Product-3')
    product_description_3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Descripcion Product-3')
    product_4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Product-4')
    product_description_4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Descripcion Product-4')
    product_5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Product-5')
    product_description_5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Descripcion Product-5')
    product_6 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Product-6')
    product_description_6 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Descripcion Product-6')
    # Banner contador
    numero_coffe = models.IntegerField( null=True)
    numero_experiencia =  models.IntegerField( null=True)
    numero_horas = models.IntegerField( null=True)
    numero_wins = models.IntegerField(null=True)


    team_1 = models.CharField(max_length=150, null=True, blank=True,verbose_name='team-1')
    team_descrp_1 = models.CharField(max_length=150, null=True, blank=True,verbose_name='team descripcion-1')
    team_2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='team-2')
    team_descrp_2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='team descripcion-2')
    team_3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='team-3')
    team_descrp_3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='team descripcion-3')
    team_4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='team-4')
    team_descrp_4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='team descripcion-4')

    banner_title = models.CharField(max_length=150, null=True, blank=True,verbose_name='Call Action Title')
    slogan = models.CharField(max_length=150, null=True, blank=True,verbose_name='slogan')
    slogan_descriptcion = models.CharField(max_length=150, null=True, blank=True,verbose_name='slogan Description')
    


    custom_title = models.CharField(max_length=100,blank=True,null=True,help_text="Reescribe el  Titulo de la publicacion ")


    
    # Campos de consulta

    consulta= RichTextField(blank=True,verbose_name='Mensaje para que nos consulten por el formulario')
    thank_you_text = RichTextField(blank=True)
    # galeria de imagenes barner de presentacion

    content_panels = Page.content_panels + [


    #Panel sliders
        FieldPanel('bio', classname="full"),
        FieldPanel('banner_title4', classname="full"),
        FieldPanel('TS_info1', classname="full"),
        FieldPanel('info1', classname="full"),
        FieldPanel('banner_title5', classname="full"),
        FieldPanel('TS_info2', classname="full"),
        FieldPanel('info2', classname="full"),
        FieldPanel('banner_title6', classname="full"),
        FieldPanel('TS_info3', classname="full"),
        FieldPanel('info3', classname="full"),
        FieldPanel('banner_title7', classname="full"),
        FieldPanel('TS_info4', classname="full"),
        FieldPanel('info4', classname="full"),
        FieldPanel('banner_title8', classname="full"),
        FieldPanel('TS_info5', classname="full"),
        FieldPanel('info5', classname="full"),
        FieldPanel('banner_title9', classname="full"),
        FieldPanel('TS_info6', classname="full"),
        FieldPanel('info6', classname="full"),
        FieldPanel('banner_title10', classname="full"),
        FieldPanel('info7', classname="full"),
        FieldPanel('info8', classname="full"),
        FieldPanel('info9', classname="full"),


        FieldPanel('product_1', classname="full"),
        FieldPanel('product_description_1', classname="full"),
        FieldPanel('product_2', classname="full"),
        FieldPanel('product_description_2', classname="full"),
        FieldPanel('product_3', classname="full"),
        FieldPanel('product_description_3', classname="full"),
        FieldPanel('product_4', classname="full"),
        FieldPanel('product_description_4', classname="full"),
        FieldPanel('product_5', classname="full"),
        FieldPanel('product_description_5', classname="full"),
        FieldPanel('product_6', classname="full"),
        FieldPanel('product_description_6', classname="full"),
        FieldPanel('numero_coffe', classname="full"),
        FieldPanel('numero_experiencia', classname="full"),
        FieldPanel('numero_horas', classname="full"),
        FieldPanel('numero_wins', classname="full"),
        FieldPanel('team_1', classname="full"),
        FieldPanel('team_descrp_1', classname="full"),
        FieldPanel('team_2', classname="full"),
        FieldPanel('team_descrp_2', classname="full"),
        FieldPanel('team_3', classname="full"),
        FieldPanel('team_descrp_3', classname="full"),
        FieldPanel('team_4', classname="full"),
        FieldPanel('team_descrp_4', classname="full"),
        FieldPanel('banner_title', classname="full"),
        FieldPanel('slogan', classname="full"),
        FieldPanel('slogan_descriptcion', classname="full"),


#panel 
        FieldPanel('consulta', classname="full"),

        InlinePanel('galleria_contacus', label="Imagen de Fondo Barner"),
        FieldPanel('thank_you_text', classname="full"),
#Panel capo de noticas
        FieldPanel("custom_title"),
    ]
class Galeriacreateitbusiness(Orderable):
    page = ParentalKey(createitbusiness, on_delete=models.CASCADE, related_name='galleria_contacus')
    logo = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo SmartQuail')
    profile_pic = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto de perfil')
    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 1')
    image_2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 2')
    image_3 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 3')
    image_4 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 4')
    image_5 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 5')
    image_6 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 6')
    image_7 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen product 1')
    image_8 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen product 2')
    image_9 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen product 3')
    image_10 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen product 4')
    image_11 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen product 5')
    image_12 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen product 6')
    image_13 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen team 1')
    image_14 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen team 2')
    image_15 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen team 3')
    image_16 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen team 4')
    image_17 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='logo_parther')
    image_18 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='logo_parther')
    image_19 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='logo_parther')
    image_20 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='logo_parther')
    image_21 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='logo_parther')
    image_22 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='logo_parther')
    image_23 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='logo_parther')
    image_24 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='logo_parther')
    image_25 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='logo_parther')
    image_26 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='logo_parther')

    panels = [
        FieldPanel('logo'),
        FieldPanel('profile_pic'),
        FieldPanel('image'),
        FieldPanel('image_2'),
        FieldPanel('image_3'),
        FieldPanel('image_4'),
        FieldPanel('image_5'),
        FieldPanel('image_6'),
        FieldPanel('image_7'),
        FieldPanel('image_8'),
        FieldPanel('image_9'),
        FieldPanel('image_10'),
        FieldPanel('image_11'),
        FieldPanel('image_12'),
        FieldPanel('image_13'),
        FieldPanel('image_14'),
        FieldPanel('image_15'),
        FieldPanel('image_16'),
        FieldPanel('image_17'),
        FieldPanel('image_18'),
        FieldPanel('image_19'),
        FieldPanel('image_20'),
        FieldPanel('image_21'),
        FieldPanel('image_22'),
        FieldPanel('image_23'),
        FieldPanel('image_24'),
        FieldPanel('image_25'),
        FieldPanel('image_26'),
    ]


class consultas(AbstractFormField):
    page = ParentalKey('smartbusinessmedia', on_delete=models.CASCADE, related_name='form_fields')

class smartbusinessmedia(AbstractEmailForm):
    # Empieza Barner de Inicio
    template = "webapp/products/smartbusinessmedia/index/smartbusinesmedia.html"
    #cliente_Navbar = RichTextField(blank=True,verbose_name='Cliente-url')
    
   # banner_title1 = RichTextField(blank=True,verbose_name='Titulo del primer banner ')
   # banner_info1 = RichTextField(blank=True,verbose_name='Informacion del primer banner ')
   # banner_title2 = RichTextField(blank=True,verbose_name='Titulo del segundo banner ')
   # banner_info2 = RichTextField(blank=True,verbose_name='Informacion del segundo banner ')
   # banner_title3 = RichTextField(blank=True,verbose_name='Titulo del tercer banner ')
   # banner_info3 = RichTextField(blank=True,verbose_name='Informacion del tercer banner ')

    # Empieza Banner de sliders
    bio = RichTextField(blank=True,verbose_name='rseña bibliografica')

    banner_title4 = RichTextField(blank=True,verbose_name='Titulo de galeria-1 ')
    TS_info1 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Subtitulo info')
    info1 = models.CharField(max_length=150, null=True, blank=True,verbose_name='info')
    banner_title5 = RichTextField(blank=True,verbose_name='Titulo de galeria-2  ')
    TS_info2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Subtitulo-2 info')
    info2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='info-2')
    banner_title6 = RichTextField(blank=True,verbose_name='Titulo de galeria-3  ')
    TS_info3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Subtitulo-3 info')
    info3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='info-3')
    banner_title7 = RichTextField(blank=True,verbose_name='Titulo de galeria-4  ')
    TS_info4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Subtitulot-4 info')
    info4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='info-4')
    banner_title8 = RichTextField(blank=True,verbose_name='Titulo de galeria-5  ')
    TS_info5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Subtitulo-5 info')
    info5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='info-5')
    banner_title9 = RichTextField(blank=True,verbose_name='Titulo de galeria-6  ')
    TS_info6 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Subtitulo-6 info')
    info6 = models.CharField(max_length=150, null=True, blank=True,verbose_name='info-6')


    # Empieza Banner de callout
    banner_title10 = RichTextField(blank=True,verbose_name='we improve')
    info7 = models.CharField(max_length=150, null=True, blank=True,verbose_name='IT business analytics')
    info8 = models.CharField(max_length=150, null=True, blank=True,verbose_name='IT business cloud DevOps')
    info9 = models.CharField(max_length=150, null=True, blank=True,verbose_name='IT business Media')
    
    # Empieza Banner de Products

  
    product_1 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Product-1')
    product_description_1 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Descripcion Product-1')
    product_2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Product-2')
    product_description_2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Descripcion Product-2')
    product_3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Product-3')
    product_description_3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Descripcion Product-3')
    product_4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Product-4')
    product_description_4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Descripcion Product-4')
    product_5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Product-5')
    product_description_5 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Descripcion Product-5')
    product_6 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Product-6')
    product_description_6 = models.CharField(max_length=150, null=True, blank=True,verbose_name='Descripcion Product-6')
    # Banner contador
    numero_coffe = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    numero_experiencia = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    numero_horas = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    numero_wins = models.DecimalField(max_digits=10, decimal_places=2,null=True)


    team_1 = models.CharField(max_length=150, null=True, blank=True,verbose_name='team-1')
    team_descrp_1 = models.CharField(max_length=150, null=True, blank=True,verbose_name='team descripcion-1')
    team_2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='team-2')
    team_descrp_2 = models.CharField(max_length=150, null=True, blank=True,verbose_name='team descripcion-2')
    team_3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='team-3')
    team_descrp_3 = models.CharField(max_length=150, null=True, blank=True,verbose_name='team descripcion-3')
    team_4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='team-4')
    team_descrp_4 = models.CharField(max_length=150, null=True, blank=True,verbose_name='team descripcion-4')

    banner_title = models.CharField(max_length=150, null=True, blank=True,verbose_name='Call Action Title')
    slogan = models.CharField(max_length=150, null=True, blank=True,verbose_name='slogan')
    slogan_descriptcion = models.CharField(max_length=150, null=True, blank=True,verbose_name='slogan Description')
    


    custom_title = models.CharField(max_length=100,blank=True,null=True,help_text="Reescribe el  Titulo de la publicacion ")


    
    # Campos de consulta

    consulta= RichTextField(blank=True,verbose_name='Mensaje para que nos consulten por el formulario')
    thank_you_text = RichTextField(blank=True)
    # galeria de imagenes barner de presentacion

    content_panels = AbstractEmailForm.content_panels + Page.content_panels + [


    #Panel sliders
        FieldPanel('bio', classname="full"),
        FieldPanel('banner_title4', classname="full"),
        FieldPanel('TS_info1', classname="full"),
        FieldPanel('info1', classname="full"),
        FieldPanel('banner_title5', classname="full"),
        FieldPanel('TS_info2', classname="full"),
        FieldPanel('info2', classname="full"),
        FieldPanel('banner_title6', classname="full"),
        FieldPanel('TS_info3', classname="full"),
        FieldPanel('info3', classname="full"),
        FieldPanel('banner_title7', classname="full"),
        FieldPanel('TS_info4', classname="full"),
        FieldPanel('info4', classname="full"),
        FieldPanel('banner_title8', classname="full"),
        FieldPanel('TS_info5', classname="full"),
        FieldPanel('info5', classname="full"),
        FieldPanel('banner_title9', classname="full"),
        FieldPanel('TS_info6', classname="full"),
        FieldPanel('info6', classname="full"),
        FieldPanel('banner_title10', classname="full"),
        FieldPanel('info7', classname="full"),
        FieldPanel('info8', classname="full"),
        FieldPanel('info9', classname="full"),


        FieldPanel('product_1', classname="full"),
        FieldPanel('product_description_1', classname="full"),
        FieldPanel('product_2', classname="full"),
        FieldPanel('product_description_2', classname="full"),
        FieldPanel('product_3', classname="full"),
        FieldPanel('product_description_3', classname="full"),
        FieldPanel('product_4', classname="full"),
        FieldPanel('product_description_4', classname="full"),
        FieldPanel('product_5', classname="full"),
        FieldPanel('product_description_5', classname="full"),
        FieldPanel('product_6', classname="full"),
        FieldPanel('product_description_6', classname="full"),
        FieldPanel('numero_coffe', classname="full"),
        FieldPanel('numero_experiencia', classname="full"),
        FieldPanel('numero_horas', classname="full"),
        FieldPanel('numero_wins', classname="full"),
        FieldPanel('team_1', classname="full"),
        FieldPanel('team_descrp_1', classname="full"),
        FieldPanel('team_2', classname="full"),
        FieldPanel('team_descrp_2', classname="full"),
        FieldPanel('team_3', classname="full"),
        FieldPanel('team_descrp_3', classname="full"),
        FieldPanel('team_4', classname="full"),
        FieldPanel('team_descrp_4', classname="full"),
        FieldPanel('banner_title', classname="full"),
        FieldPanel('slogan', classname="full"),
        FieldPanel('slogan_descriptcion', classname="full"),


#panel 
        FieldPanel('consulta', classname="full"),

        InlinePanel('galleria_2', label="Imagen de Fondo Barner"),
        InlinePanel('form_fields', label="consultas"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
#Panel capo de noticas
        FieldPanel("custom_title"),
    ]



class GaleriadeImagenesSBM(Orderable):
    page = ParentalKey(smartbusinessmedia, on_delete=models.CASCADE, related_name='galleria_2')
    logo = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Logotipo SmartQuail')
    profile_pic = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Foto de perfil')
    image = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 1')
    image_2 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 2')
    image_3 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 3')
    image_4 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 4')
    image_5 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 5')
    image_6 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen Slide Banner 6')
    image_7 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen product 1')
    image_8 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen product 2')
    image_9 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen product 3')
    image_10 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen product 4')
    image_11 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen product 5')
    image_12 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen product 6')
    image_13 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen team 1')
    image_14 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen team 2')
    image_15 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen team 3')
    image_16 = models.ForeignKey('wagtailimages.Image',null=True,blank=True,on_delete=models.SET_NULL,related_name='+',verbose_name='Imagen team 4')

    panels = [
        FieldPanel('logo'),
        FieldPanel('profile_pic'),
        FieldPanel('image'),
        FieldPanel('image_2'),
        FieldPanel('image_3'),
        FieldPanel('image_4'),
        FieldPanel('image_5'),
        FieldPanel('image_6'),
        FieldPanel('image_7'),
        FieldPanel('image_8'),
        FieldPanel('image_9'),
        FieldPanel('image_10'),
        FieldPanel('image_11'),
        FieldPanel('image_12'),
        FieldPanel('image_13'),
        FieldPanel('image_14'),
        FieldPanel('image_15'),
        FieldPanel('image_16'),
    ]

