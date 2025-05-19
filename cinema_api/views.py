from django.http import HttpResponse
from movies.models import Genre  
from django.conf import settings
import os

def home_view(request):
    genres = Genre.objects.all()
    
    genre_buttons = ""
    for genre in genres:
        genre_buttons += f"""
        <a href="/api/v1/movies/?genre={genre.id}" class="genre-button">
            {genre.name}
        </a>
        """
    
    image_path = os.path.join(settings.STATIC_URL, 'images/cinema.jpg')
    
    return HttpResponse(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cinema API</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                max-width: 1000px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f0f2f5;
            }}
            .header {{
                text-align: center;
                margin-bottom: 30px;
            }}
            .header img {{
                width: 100%;
                max-height: 300px;
                object-fit: cover;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            }}
            h1 {{
                color: #2c3e50;
                margin-top: 20px;
            }}
            .container {{
                display: flex;
                gap: 30px;
            }}
            .menu {{
                flex: 1;
                background: white;
                padding: 25px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }}
            .menu ul {{
                list-style: none;
                padding: 0;
            }}
            .menu li {{
                margin: 15px 0;
            }}
            .menu a {{
                display: block;
                padding: 12px 15px;
                background: #3498db;
                color: white;
                text-decoration: none;
                border-radius: 6px;
                transition: all 0.3s;
                font-weight: 500;
            }}
            .menu a:hover {{
                background: #2980b9;
                transform: translateY(-2px);
            }}
            .genres {{
                margin-top: 30px;
            }}
            .genres-title {{
                color: #2c3e50;
                margin-bottom: 15px;
                font-size: 1.2em;
            }}
            .genre-buttons {{
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
            }}
            .genre-button {{
                padding: 8px 16px;
                background: #2ecc71;
                color: white;
                text-decoration: none;
                border-radius: 20px;
                transition: all 0.3s;
                font-size: 0.9em;
            }}
            .genre-button:hover {{
                background: #27ae60;
                transform: scale(1.05);
            }}
            .admin-link {{
                background: #e74c3c !important;
            }}
            .admin-link:hover {{
                background: #c0392b !important;
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <img src="{image_path}" alt="Cinema Background">
            <h1>Добро пожаловать в Cinema API</h1>
        </div>
        
        <div class="container">
            <div class="menu">
                <p>Доступные эндпоинты:</p>
                <ul>
                    <li><a href="/api/v1/movies/">Все фильмы</a></li>
                    <li><a href="/api/v1/halls/">Кинозалы</a></li>
                    <li><a href="/api/v1/screenings/">Сеансы</a></li>
                    <li><a href="/api/v1/tickets/">Билеты</a></li>
                    <li><a href="/admin/" class="admin-link">Панель администратора</a></li>
                </ul>
                
                <div class="genres">
                    <div class="genres-title">Фильтровать по жанрам:</div>
                    <div class="genre-buttons">
                        {genre_buttons}
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """)
