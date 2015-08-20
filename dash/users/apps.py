from django.apps import AppConfig


class DashUsersConfig(AppConfig):
    name = "dash.users"
    label = "dash_users"  # avoid conflict with smartmin.users
