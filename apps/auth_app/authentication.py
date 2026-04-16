import jwt
from datetime import datetime, timedelta
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User


class JWTAuthentication(BaseAuthentication):
    """Custom JWT authentication"""

    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION", "")
        
        if not auth_header.startswith("Bearer "):
            return None

        token = auth_header[7:]  # Remove "Bearer " prefix

        try:
            payload = jwt.decode(
                token,
                settings.JWT_SECRET,
                algorithms=[settings.JWT_ALGORITHM],
            )
            user_id = payload.get("user_id")
            user = User.objects.get(id=user_id)
            return (user, token)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired")
        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid token")
        except User.DoesNotExist:
            raise AuthenticationFailed("User not found")


def generate_jwt_token(user):
    """Generate JWT token for user"""
    payload = {
        "user_id": user.id,
        "username": user.username,
        "exp": datetime.utcnow() + timedelta(hours=settings.JWT_EXPIRATION_HOURS),
        "iat": datetime.utcnow(),
    }

    if hasattr(user, "profile"):
        payload["role"] = user.profile.role

    token = jwt.encode(
        payload,
        settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM,
    )

    return token
