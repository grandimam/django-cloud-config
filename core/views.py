import json
from core.models import ConfigVersion

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def config_refresh(request):
    """Handle the webhook that triggers config refresh."""
    if request.method == 'POST':
        payload = json.loads(request.body)
        config_name = payload.get('config_name')
        environment_name = payload.get('environment_name')
        version = payload.get('version')
        try:
            config_version = ConfigVersion.objects.get(
                config__name=config_name,
                environment__name=environment_name,
                version=version
            )
            config_version.refresh()
            return JsonResponse({"status": "success", "message": "Configuration refreshed"})
        except ConfigVersion.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Config version not found"}, status=404)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=400)
