import pytest
from unittest.mock import MagicMock, patch
from blog_post_app.api.services import add_profile


@pytest.mark.django_db
@patch("blog_post_app.api.services.Profile.get_user_jwt")
def test_add_profile(mock_get_user_jwt):

    # 1. fake profile (خروجی JWT)
    mock_profile = MagicMock()
    mock_get_user_jwt.return_value = mock_profile

    # 2. fake model instance (خروجی واقعی serializer.save)
    mock_instance = MagicMock()

    # 3. fake serializer
    serializer = MagicMock()
    serializer.save.return_value = mock_instance

    # 4. fake view (self)
    fake_self = MagicMock()
    fake_self.request = "fake_request"

    # 5. اجرای service
    result = add_profile(fake_self, serializer)

    # -------------------------
    # assertions
    # -------------------------

    # بررسی اینکه JWT درست صدا زده شده
    mock_get_user_jwt.assert_called_once_with(
        fake_self,
        "fake_request"
    )

    # بررسی اینکه serializer با profile درست save شده
    serializer.save.assert_called_once_with(
        profile_related=mock_profile
    )

    # بررسی خروجی service
    assert result == mock_instance