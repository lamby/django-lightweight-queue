from setuptools import setup

setup(
    name='django-lightweight-queue',
    packages=(
        'django_lightweight_queue',
        'django_lightweight_queue.management',
        'django_lightweight_queue.management.commands',
    )
)
