from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from app.models import Car

class CarsList(ListView):
    model = Car
    template_name='car_list.html'

    def get_context_data(self, **kwards):
        context = super(CarsList, self).get_context_data(**kwards)
        selected_filter_options = {'manufacturers': [], 'models': [], 'transmissions': [], 'colors': []}
        selected_filter_options['manufacturers'] = self.request.GET.getlist('manufacturer')
        selected_filter_options['models'] = self.request.GET.getlist('model')
        selected_filter_options['transmissions'] = self.request.GET.getlist('transmission')
        selected_filter_options['colors'] = self.request.GET.getlist('color')
        context['selected_filter_options'] = selected_filter_options
        filter_options = {'manufacturers': [], 'models': [], 'transmissions': [], 'colors': []}
        for car in Car.objects.all():
            if not car.manufacturer in filter_options['manufacturers']:
                filter_options['manufacturers'].append(car.manufacturer)
            if not car.model in filter_options['models']:
                filter_options['models'].append(car.model)
            if not {str(car.transmission): car.get_transmission_display()} in filter_options['transmissions']:
                filter_options['transmissions'].append({str(car.transmission): car.get_transmission_display()})
            if not car.color in filter_options['colors']:
                filter_options['colors'].append(car.color)
        context['filter_options'] = filter_options
        return context

    def get_queryset(self):
        manufacturers = self.request.GET.getlist('manufacturer')
        models = self.request.GET.getlist('model')
        transmissions = self.request.GET.getlist('transmission')
        colors = self.request.GET.getlist('color')
        q_objects_manufacturers = Q()
        q_objects_models = Q()
        q_objects_transmissions = Q()
        q_objects_colors = Q()
        if len(manufacturers) or len(colors) or len(models) or len(transmissions):
            for manufacturer in manufacturers:
                q_objects_manufacturers |= Q(manufacturer=manufacturer)
            for model in models:
                q_objects_models |= Q(model=model)
            for color in colors:
                q_objects_colors |= Q(color=color)
            for transmission in transmissions:
                q_objects_transmissions |= Q(transmission=int(transmission))
        return Car.objects.all().filter((q_objects_manufacturers) & (q_objects_models) & (q_objects_transmissions) & (q_objects_colors))