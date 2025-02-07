from django.urls import path
from rest_framework.routers import SimpleRouter
from booktest.view.userinfo import UserinfoViewSet

router = SimpleRouter()

router.register(r"", UserinfoViewSet)

urlpatterns = [
    # 获取人员信息
    path(
        "get_personnel/<int:personnel_id>/",
        UserinfoViewSet.as_view({"get": "get_personnel"}),
        name="get_personnel",
    ),

    path(
        "building_area/",
        UserinfoViewSet.as_view({"post": "building_area"}),
        name="building_area",
    ),
]

urlpatterns += router.urls
print(urlpatterns)
