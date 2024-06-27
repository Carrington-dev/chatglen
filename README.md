# Channels


### Using Uvicorn To Runserver ASGI DJango
```bash
uvicorn chatweb.wsgi:application --reload
# ran but gave an error
daphne chatweb.asgi:channel_layer --port 8888 # to run sockets
daphne -p 8000 your_project_name.asgi:application
python manage.py runserver

```

### Nice Notes
```bash
websocat ws://localhost:8000/ws/chat/carrie/
https://blog.heroku.com/in_deep_with_django_channels_the_future_of_real_time_apps_in_django
# https://blog.heroku.com/in_deep_with_django_channels_the_future_of_real_time_apps_in_django
```