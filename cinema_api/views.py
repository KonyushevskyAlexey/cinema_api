from django.http import HttpResponse
from movies.models import Genre  # Импортируем модель Genre

def home_view(request):
    # Получаем все жанры из базы данных
    genres = Genre.objects.all()
    
    # Создаем HTML-код для кнопок жанров
    genre_buttons = ""
    for genre in genres:
        genre_buttons += f"""
        <a href="/api/v1/movies/?genre={genre.id}" class="genre-button">
            {genre.name}
        </a>
        """
    
    return HttpResponse(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cinema API</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f5f5f5;
            }}
            h1 {{
                color: #333;
                text-align: center;
            }}
            .menu {{
                background: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                margin-bottom: 20px;
            }}
            .menu ul {{
                list-style: none;
                padding: 0;
            }}
            .menu li {{
                margin: 10px 0;
            }}
            .menu a {{
                display: block;
                padding: 10px;
                background: #4CAF50;
                color: white;
                text-decoration: none;
                border-radius: 4px;
                transition: background 0.3s;
            }}
            .menu a:hover {{
                background: #45a049;
            }}
            .genres {{
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
                margin-top: 20px;
            }}
            .genre-button {{
                padding: 8px 16px;
                background: #2196F3;
                color: white;
                text-decoration: none;
                border-radius: 4px;
                transition: background 0.3s;
            }}
            .genre-button:hover {{
                background: #0b7dda;
            }}
        </style>
    </head>
    <body>
        <div class="menu">
            <h1>Добро пожаловать в Cinema API!</h1>
            <p>Доступные эндпоинты:</p>
            <ul>
                <li><a href="/api/v1/movies/">Все фильмы</a></li>
                <li><a href="/api/v1/halls/">Залы</a></li>
                <li><a href="/api/v1/screenings/">Сеансы</a></li>
                <li><a href="/api/v1/tickets/">Билеты</a></li>
                <li><a href="/admin/">Админка</a></li>
            </ul>
            
            <div class="genres">
                <p>Фильтровать по жанрам:</p>
                {genre_buttons}
            </div>
        </div>
    </body>
    </html>
    """)
