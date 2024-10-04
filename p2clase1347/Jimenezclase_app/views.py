from django.shortcuts import render
from django.http import HttpResponse

def hola(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hola</title>
        <style>
            body {
                display: flex;
                height: 100vh;
                background-color: #f0f8ff;
                font-family: 'Arial', sans-serif;
                margin: 0;
            }
            .mensaje {
                background-color: #ffffff;
                border-radius: 10px;
                padding: 20px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
                text-align: center;
                font-size: 24px;
                color: #333;
            }
        </style>
    </head>
    <body>
        <div class="mensaje">
            soy Elmasperronaqui
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)
def minovia(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hola</title>
        <style>
            body {
                display: flex;
                height: 100vh;
                background-color: #f0f8ff;
                font-family: 'Arial', sans-serif;
                margin: 0;
            }
            .mensaje {
                background-color: #ffffff;
                border-radius: 10px;
                padding: 20px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
                text-align: center;
                font-size: 24px;
                color: #333;
            }
        </style>
    </head>
    <body>
        <class="mensaje">
            donde andas mayra?💋
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)
