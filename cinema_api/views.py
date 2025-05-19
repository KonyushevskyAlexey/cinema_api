from django.http import HttpResponse

def home_view(request):
    return HttpResponse("""
        <h1>Добро пожаловать в Cinema API!</h1>
        <p>Доступные эндпоинты:</p>
        <ul>
            <li><a href="/api/v1/movies/">Фильмы</a></li>
            <li><a href="/api/v1/halls/">Залы</a></li>
            <li><a href="/api/v1/screenings/">Сеансы</a></li>
            <li><a href="/api/v1/tickets/">Билеты</a></li>
            <li><a href="/admin/">Админка</a></li>
        </ul>
    """)
