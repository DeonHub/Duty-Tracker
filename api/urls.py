from django.urls import include, path, re_path
# from api import context_processors
from rest_framework import routers
from rest_framework import permissions
from . import views
from . import context_processors



router = routers.DefaultRouter()

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Duty Tracker API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)






# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('swag/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', views.Login.as_view(), name="login"),

    path('add-report/<int:pk>', views.AddReport.as_view(), name="add_report"),
    path('add-comment/<int:pk>', views.AddComment.as_view(), name="add_comment"),

    path('add-extra-report/', views.AddExtraWorkReport.as_view(), name="add_extra_report"),
    path('extra-reports/', views.ExtraWorkReport.as_view(), name="extra_report"),

    path('assigned-duties/', views.ViewAssignedTasks.as_view(), name="ViewAssignedTasks"),
    path('member-duties/', views.MemberAssignedDuties.as_view(), name="MemberAssignedDuties"),

    path('subjects/', views.GetSubjects.as_view(), name="subjects"), 


    # path('submitted-duties/', views.ViewSubmittedTasks.as_view(), name="ViewSubmittedTasks"),

    # path('member-submitted-duties/', views.MemberSubmittedTasks.as_view(), name="MemberSubmittedTasks"), 

    re_path('swagger/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # path('list/<int:pk>', views.HeroDetails.as_view(), name="heros"),
    # path('members/', views.members, name="members"),
]