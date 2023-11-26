import json
import os
import pickle
from dataclasses import dataclass
import base64

from django.http import HttpResponse, JsonResponse
from django.utils.safestring import mark_safe

from security.models import User


def unsafe_users(request, user_id):
    """SQL injection"""

    users = User.objects.raw("SELECT * FROM security_user WHERE id = %s", [user_id])
    user_list = [f"User {user.id} {user.name}" for user in users]
    return HttpResponse("\n".join(user_list))
