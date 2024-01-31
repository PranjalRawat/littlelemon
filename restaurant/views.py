from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from .models import Menu, Reservation
from .forms import ReservationForm
from datetime import date

# Create your views here.
class AboutView(TemplateView):
    def get(self, request):
        context = {
                    'title': 'Little Lemon',
                    'description': [
                        '''
                            Welcome to Little Lemon Restaurant, where vibrant flavors and cozy ambiance come together to create a delightful dining experience. Nestled in the heart of [City/Town], our charming eatery is a haven for food enthusiasts seeking a taste of culinary excellence in a welcoming setting.
                        ''',
                        '''
                            Step through the doors of Little Lemon, and you'll be greeted by a warm and inviting atmosphere. The décor, adorned with citrus-inspired accents and a palette of cheerful yellows and greens, reflects the restaurant's commitment to fresh, seasonal ingredients and a zest for life.
                        ''',
                        '''
                            Our menu is a celebration of contemporary cuisine infused with a burst of citrusy brilliance. From zesty lemon-infused starters to succulent main courses bursting with flavor, our chefs craft each dish with precision and passion. Indulge in our signature Lemon Zest Chicken, a tender and juicy delight that captures the essence of our culinary philosophy.
                        ''',
                        '''
                            At Little Lemon, we understand the importance of a well-curated dining experience. Our attentive and friendly staff ensures that every guest feels at home, whether it's a casual weekday lunch or a special celebration. The restaurant's cozy seating arrangements and soft lighting create an intimate setting for memorable moments and enjoyable conversations.
                        ''',
                        '''
                            Pair your meal with a selection from our thoughtfully curated beverage menu, featuring refreshing lemonades, craft cocktails, and a carefully chosen wine list. Our bartenders are skilled in creating concoctions that perfectly complement the flavors of our dishes.
                        ''',
                        '''
                            Little Lemon Restaurant is not just a place to eat; it's a destination for those who appreciate the fusion of culinary artistry and a convivial atmosphere. Join us at Little Lemon, where every bite is a burst of sunshine, and every moment is a celebration of the simple joy of good food and great company.
                        '''
                    ]
                }
        return render(request, 'about.html', context)

class HomeView(TemplateView):
    def get(self, request):
        return render(request, 'home.html', {'title': 'Little Lemon'})

class MenuView(TemplateView):
    def get(self, request):
        modelData = Menu.objects.all().order_by('name')
        context = {
            'title': 'Little Lemon',
            'modelData': modelData,
        }
        return render(request, 'menu.html', context)

class MenuItemView(ListView):
    def get(self, request, id):
        modelData = Menu.objects.get(id = id)
        context = {
            'title': 'Little Lemon',
            'modelData': modelData,
        }
        return render(request, 'menuItem.html', context)

class BookView(CreateView):
    template_name = 'book.html'
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy('book')

    def get(self, request):
        modelData = Reservation.objects.filter(date = date.today())
        form_class = ReservationForm
        context = {
            'title': 'Little Lemon',
            'form': form_class,
            'modelData': modelData,
            'today_date': date.today(),
        }
        return render(request, 'book.html', context)
