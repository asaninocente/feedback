# feedback
Start the Python shell

    from reviews.models import Review

Start a new app inside the project app

    python manage.py startapp profiles

Start a shell

    python manage.py shell

> from profiles.models import UserProfile
>
> UserProfile.objects.all()
>
> UserProfile.objects.all()[0].image
>
> UserProfile.objects.all()[0].image.path
>
> UserProfile.objects.all()[0].image.size