from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Evento
from .forms import Evento30000Form, Evento20000Form, Evento10000Form, Evento5000Form
from .models import Evento_30000, Evento_20000, Evento_10000, Evento_5000,Subject
from usuarios.models import Profile,DeclaracionVeracidad,Contacts,Legal,Activity
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required
import weasyprint
from django.conf import settings
from pathlib import Path

@login_required
def listar_categorias(request):
    profile = get_object_or_404(Profile, user=request.user)
    actividad = profile.activity
    declaracion = DeclaracionVeracidad.objects.get(user=request.user)
    acepta_terminos_condiciones = declaracion.acepta_terminos_condiciones
    categorias = Subject.objects.all()


    return render(request, 'listar_categorias.html', {'categorias': categorias, 
                                                      'actividad': actividad,
                                                      'acepta_terminos_condiciones': acepta_terminos_condiciones})


@login_required
def evento_30000(request):

    profile = get_object_or_404(Profile, user=request.user)
    actividad = profile.activity
    declaracion = DeclaracionVeracidad.objects.get(user=request.user)
    acepta_terminos_condiciones = declaracion.acepta_terminos_condiciones
    try:
        event = Evento_30000.objects.get(user=request.user)
    except Evento_30000.DoesNotExist:
        event = None

    if request.method == 'POST':
        if event:
            event_30000_form = Evento30000Form(instance=event, data=request.POST)
        else:
            event_30000_form = Evento30000Form(data=request.POST)

        if event_30000_form.is_valid():
            event = event_30000_form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, 'Event updated successfully')
            return redirect('actividades_espacio_publico:evento_success')
        else:
            messages.error(request, 'Error updating your event')
    else:
        event_30000_form = Evento30000Form(instance=event)
    return render(request, 'eventos/30000.html', {'event_30000_form': event_30000_form, 'profile': profile, 'event': event,
                                                   'actividad': actividad,
                                                      'acepta_terminos_condiciones': acepta_terminos_condiciones})


@login_required
def crear_propuesta_evento_30000(request):
    profile = get_object_or_404(Profile, user=request.user)
    actividad = profile.activity
    declaracion = DeclaracionVeracidad.objects.get(user=request.user)
    acepta_terminos_condiciones = declaracion.acepta_terminos_condiciones
    # Obtener el perfil del usuario actual
    profile = get_object_or_404(Profile, user=request.user)
    
    # Verificar si el usuario ya tiene un evento asociado al evento 30000
    try:
        event = Evento_30000.objects.get(user=request.user)
        # Si el usuario ya tiene un evento asociado, redirigirlo a la página de éxito del evento
        return redirect('actividades_espacio_publico:evento_fail')
    except Evento_30000.DoesNotExist:
        # Si el usuario no tiene un evento asociado, continuar con la creación de la propuesta
        pass

    if request.method == 'POST':
        # Crear un formulario de evento 30000 con los datos proporcionados en la solicitud
        evento_30000_form = Evento30000Form(request.POST)
        if evento_30000_form.is_valid():
            # Guardar el evento 30000 asociado al usuario actual
            event = evento_30000_form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, 'Evento 30000 creado exitosamente')
            return redirect('actividades_espacio_publico:evento_success')
        else:
            messages.error(request, 'Error al crear el evento 30000')
    else:
        # Si la solicitud no es POST, mostrar un formulario vacío para crear un nuevo evento 30000
        evento_30000_form = Evento30000Form()
    
    # Renderizar el formulario de evento 30000
    return render(request, 'eventos/crear_propuesta_evento_30000.html', {'evento_30000_form': evento_30000_form, 'profile': profile,'actividad': actividad,
                                                      'acepta_terminos_condiciones': acepta_terminos_condiciones})


@staff_member_required
def admin_evento_30000_pdf(request, profile_id):
    try:
        profile = get_object_or_404(Profile, id=profile_id)
        contacto = get_object_or_404(Contacts, id=profile_id)
        legal = get_object_or_404(Legal, id=profile_id)
        activity = get_object_or_404(Activity, id=profile_id)
        evento = get_object_or_404(Evento_30000, id=profile_id)
        
        html = render_to_string('eventos/pdf_profiles/pdf_30000.html', {'profile': profile, 'contacto':contacto,'legal':legal, 'activity':activity, 'evento':evento})

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="order_{}.pdf"'.format(profile.id)

        # Obtener la ruta completa al archivo CSS usando Path
        css_path = Path(settings.STATIC_ROOT) / 'css' / 'pdf_reports' / 'report.css'

        # Renderizar el PDF
        weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response, stylesheets=[weasyprint.CSS(str(css_path))], presentational_hints=True)
        
        return response
    except Exception as e:
        # Manejar cualquier excepción y devolver una respuesta de error
        return HttpResponse("Ocurrió un error al generar el PDF: {}".format(str(e)), status=500)

@login_required
def evento_20000(request):
    profile = get_object_or_404(Profile, user=request.user)
    actividad = profile.activity
    declaracion = DeclaracionVeracidad.objects.get(user=request.user)
    acepta_terminos_condiciones = declaracion.acepta_terminos_condiciones
    
    try:
        event = Evento_20000.objects.get(user=request.user)
        event_20000_form = Evento20000Form(instance=event)
    except Evento_20000.DoesNotExist:
        event = None
        event_20000_form = Evento20000Form()

    if request.method == 'POST':
        if event:
            event_20000_form = Evento20000Form(instance=event, data=request.POST)
        else:
            event_20000_form = Evento20000Form(data=request.POST)

        if event_20000_form.is_valid():
            event = event_20000_form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, 'Event updated successfully')
            return redirect('actividades_espacio_publico:evento_fail')
        else:
            messages.error(request, 'Error updating your event')

    return render(request, 'eventos/20000.html', {'event_20000_form': event_20000_form, 'profile': profile, 'event': event,
                                                   'actividad': actividad, 'acepta_terminos_condiciones': acepta_terminos_condiciones})


@login_required
def crear_propuesta_evento_20000(request):
    profile = get_object_or_404(Profile, user=request.user)
    actividad = profile.activity
    declaracion = DeclaracionVeracidad.objects.get(user=request.user)
    acepta_terminos_condiciones = declaracion.acepta_terminos_condiciones
    # Obtener el perfil del usuario actual
    profile = get_object_or_404(Profile, user=request.user)
    
    # Verificar si el usuario ya tiene un evento asociado al evento 30000
    try:
        event = Evento_20000.objects.get(user=request.user)
        # Si el usuario ya tiene un evento asociado, redirigirlo a la página de éxito del evento
        return redirect('actividades_espacio_publico:evento_success')
    except Evento_20000.DoesNotExist:
        # Si el usuario no tiene un evento asociado, continuar con la creación de la propuesta
        pass

    if request.method == 'POST':
        # Crear un formulario de evento 30000 con los datos proporcionados en la solicitud
        evento_20000_form = Evento20000Form(request.POST)
        if evento_20000_form.is_valid():
            # Guardar el evento 30000 asociado al usuario actual
            event = evento_20000_form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, 'Evento 30000 creado exitosamente')
            return redirect('actividades_espacio_publico:evento_success')
        else:
            messages.error(request, 'Error al crear el evento 30000')
    else:
        # Si la solicitud no es POST, mostrar un formulario vacío para crear un nuevo evento 30000
        evento_20000_form = Evento20000Form()
    
    # Renderizar el formulario de evento 30000
    return render(request, 'eventos/crear_propuesta_evento_20000.html', {'evento_20000_form': evento_20000_form, 'profile': profile,'actividad': actividad,
                                                      'acepta_terminos_condiciones': acepta_terminos_condiciones})


@staff_member_required
def admin_evento_20000_pdf(request, profile_id):
    try:
        profile = get_object_or_404(Profile, id=profile_id)
        contacto = get_object_or_404(Contacts, id=profile_id)
        legal = get_object_or_404(Legal, id=profile_id)
        activity = get_object_or_404(Activity, id=profile_id)
        evento = get_object_or_404(Evento_30000, id=profile_id)
        
        html = render_to_string('eventos/pdf_profiles/pdf_20000.html', {'profile': profile, 'contacto':contacto,'legal':legal, 'activity':activity, 'evento':evento})

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="order_{}.pdf"'.format(profile.id)

        # Obtener la ruta completa al archivo CSS usando Path
        css_path = Path(settings.STATIC_ROOT) / 'css' / 'pdf_reports' / 'report.css'

        # Renderizar el PDF
        weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response, stylesheets=[weasyprint.CSS(str(css_path))], presentational_hints=True)
        
        return response
    except Exception as e:
        # Manejar cualquier excepción y devolver una respuesta de error
        return HttpResponse("Ocurrió un error al generar el PDF: {}".format(str(e)), status=500)
    




@login_required
def evento_10000(request):
    profile = get_object_or_404(Profile, user=request.user)
    actividad = profile.activity
    declaracion = DeclaracionVeracidad.objects.get(user=request.user)
    acepta_terminos_condiciones = declaracion.acepta_terminos_condiciones
    
    try:
        event = Evento_10000.objects.get(user=request.user)
        event_10000_form = Evento10000Form(instance=event)
    except Evento_10000.DoesNotExist:
        event = None
        event_10000_form = Evento10000Form()

    if request.method == 'POST':
        if event:
            event_10000_form = Evento10000Form(instance=event, data=request.POST)
        else:
            event_10000_form = Evento10000Form(data=request.POST)

        if event_10000_form.is_valid():
            event = event_10000_form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, 'Event updated successfully')
            return redirect('actividades_espacio_publico:evento_success')
        else:
            messages.error(request, 'Error updating your event')

    return render(request, 'eventos/10000.html', {'event_10000_form': event_10000_form, 'profile': profile, 'event': event,
                                                   'actividad': actividad, 'acepta_terminos_condiciones': acepta_terminos_condiciones})


@login_required
def crear_propuesta_evento_10000(request):
    profile = get_object_or_404(Profile, user=request.user)
    actividad = profile.activity
    declaracion = DeclaracionVeracidad.objects.get(user=request.user)
    acepta_terminos_condiciones = declaracion.acepta_terminos_condiciones
    # Obtener el perfil del usuario actual
    profile = get_object_or_404(Profile, user=request.user)
    
    # Verificar si el usuario ya tiene un evento asociado al evento 30000
    try:
        event = Evento_10000.objects.get(user=request.user)
        # Si el usuario ya tiene un evento asociado, redirigirlo a la página de éxito del evento
        return redirect('actividades_espacio_publico:evento_fail')
    except Evento_10000.DoesNotExist:
        # Si el usuario no tiene un evento asociado, continuar con la creación de la propuesta
        pass

    if request.method == 'POST':
        # Crear un formulario de evento 30000 con los datos proporcionados en la solicitud
        evento_10000_form = Evento10000Form(request.POST)
        if evento_10000_form.is_valid():
            # Guardar el evento 30000 asociado al usuario actual
            event = evento_10000_form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, 'Evento 10000 creado exitosamente')
            return redirect('actividades_espacio_publico:evento_success')
        else:
            messages.error(request, 'Error al crear el evento 10000')
    else:
        # Si la solicitud no es POST, mostrar un formulario vacío para crear un nuevo evento 30000
        evento_10000_form = Evento10000Form()
    
    # Renderizar el formulario de evento 30000
    return render(request, 'eventos/crear_propuesta_evento_10000.html', {'evento_10000_form': evento_10000_form, 'profile': profile,'actividad': actividad,
                                                      'acepta_terminos_condiciones': acepta_terminos_condiciones})


@staff_member_required
def admin_evento_10000_pdf(request, profile_id):
    try:
        profile = get_object_or_404(Profile, id=profile_id)
        contacto = get_object_or_404(Contacts, id=profile_id)
        legal = get_object_or_404(Legal, id=profile_id)
        activity = get_object_or_404(Activity, id=profile_id)
        evento = get_object_or_404(Evento_30000, id=profile_id)
        
        html = render_to_string('eventos/pdf_profiles/pdf_10000.html', {'profile': profile, 'contacto':contacto,'legal':legal, 'activity':activity, 'evento':evento})

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="order_{}.pdf"'.format(profile.id)

        # Obtener la ruta completa al archivo CSS usando Path
        css_path = Path(settings.STATIC_ROOT) / 'css' / 'pdf_reports' / 'report.css'

        # Renderizar el PDF
        weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response, stylesheets=[weasyprint.CSS(str(css_path))], presentational_hints=True)
        
        return response
    except Exception as e:
        # Manejar cualquier excepción y devolver una respuesta de error
        return HttpResponse("Ocurrió un error al generar el PDF: {}".format(str(e)), status=500)


@login_required
def evento_5000(request):
    profile = get_object_or_404(Profile, user=request.user)
    actividad = profile.activity
    declaracion = DeclaracionVeracidad.objects.get(user=request.user)
    acepta_terminos_condiciones = declaracion.acepta_terminos_condiciones
    
    try:
        event = Evento_5000.objects.get(user=request.user)
        event_5000_form = Evento5000Form(instance=event)
    except Evento_5000.DoesNotExist:
        event = None
        event_5000_form = Evento5000Form()

    if request.method == 'POST':
        if event:
            event_5000_form = Evento5000Form(instance=event, data=request.POST)
        else:
            event_5000_form = Evento5000Form(data=request.POST)

        if event_5000_form.is_valid():
            event = event_5000_form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, 'Event updated successfully')
            return redirect('actividades_espacio_publico:evento_success')
        else:
            messages.error(request, 'Error updating your event')

    return render(request, 'eventos/5000.html', {'event_5000_form': event_5000_form, 'profile': profile, 'event': event,
                                                   'actividad': actividad, 'acepta_terminos_condiciones': acepta_terminos_condiciones})


@login_required
def crear_propuesta_evento_5000(request):
    profile = get_object_or_404(Profile, user=request.user)
    actividad = profile.activity
    declaracion = DeclaracionVeracidad.objects.get(user=request.user)
    acepta_terminos_condiciones = declaracion.acepta_terminos_condiciones
    # Obtener el perfil del usuario actual
    profile = get_object_or_404(Profile, user=request.user)
    
    # Verificar si el usuario ya tiene un evento asociado al evento 30000
    try:
        event = Evento_5000.objects.get(user=request.user)
        # Si el usuario ya tiene un evento asociado, redirigirlo a la página de éxito del evento
        return redirect('actividades_espacio_publico:evento_fail')
    except Evento_5000.DoesNotExist:
        # Si el usuario no tiene un evento asociado, continuar con la creación de la propuesta
        pass

    if request.method == 'POST':
        # Crear un formulario de evento 30000 con los datos proporcionados en la solicitud
        evento_5000_form = Evento5000Form(request.POST)
        if evento_5000_form.is_valid():
            # Guardar el evento 30000 asociado al usuario actual
            event = evento_5000_form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, 'Evento 5000 creado exitosamente')
            return redirect('actividades_espacio_publico:evento_success')
        else:
            messages.error(request, 'Error al crear el evento 30000')
    else:
        # Si la solicitud no es POST, mostrar un formulario vacío para crear un nuevo evento 30000
        evento_5000_form = Evento5000Form()
    
    # Renderizar el formulario de evento 30000
    return render(request, 'eventos/crear_propuesta_evento_5000.html', {'evento_5000_form': evento_5000_form, 'profile': profile,'actividad': actividad,
                                                      'acepta_terminos_condiciones': acepta_terminos_condiciones})

@staff_member_required
def admin_evento_5000_pdf(request, profile_id):
    try:
        profile = get_object_or_404(Profile, id=profile_id)
        contacto = get_object_or_404(Contacts, id=profile_id)
        legal = get_object_or_404(Legal, id=profile_id)
        activity = get_object_or_404(Activity, id=profile_id)
        evento = get_object_or_404(Evento_30000, id=profile_id)
        
        html = render_to_string('eventos/pdf_profiles/pdf_5000.html', {'profile': profile, 'contacto':contacto,'legal':legal, 'activity':activity, 'evento':evento})

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="order_{}.pdf"'.format(profile.id)

        # Obtener la ruta completa al archivo CSS usando Path
        css_path = Path(settings.STATIC_ROOT) / 'css' / 'pdf_reports' / 'report.css'

        # Renderizar el PDF
        weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response, stylesheets=[weasyprint.CSS(str(css_path))], presentational_hints=True)
        
        return response
    except Exception as e:
        # Manejar cualquier excepción y devolver una respuesta de error
        return HttpResponse("Ocurrió un error al generar el PDF: {}".format(str(e)), status=500)
    


@login_required
def evento_success(request):
    profile = get_object_or_404(Profile, user=request.user)
    actividad = profile.activity
    declaracion = DeclaracionVeracidad.objects.get(user=request.user)
    acepta_terminos_condiciones = declaracion.acepta_terminos_condiciones

    return render(request, 'eventos/evento_success.html', {'profile': profile,
                                                   'actividad': actividad, 'acepta_terminos_condiciones': acepta_terminos_condiciones})



@login_required
def evento_fail(request):
    profile = get_object_or_404(Profile, user=request.user)
    actividad = profile.activity
    declaracion = DeclaracionVeracidad.objects.get(user=request.user)
    acepta_terminos_condiciones = declaracion.acepta_terminos_condiciones

    return render(request, 'eventos/evento_fail.html', {'profile': profile,
                                                   'actividad': actividad, 'acepta_terminos_condiciones': acepta_terminos_condiciones})
