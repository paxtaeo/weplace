from django.conf import settings

def secrets_processor(request):
    return {
        "KAKAOMAP_API_KEY": settings.KAKAOMAP_API_KEY
    }
