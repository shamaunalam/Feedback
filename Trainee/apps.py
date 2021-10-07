from django.apps import AppConfig


class TraineeConfig(AppConfig):
    name = 'Trainee'

    def ready(self):
        import Trainee.signals