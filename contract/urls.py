from django.urls import path, include
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .views import EmploymentAgreementListCreate, EmploymentAgreementRetrieveUpdateDestroy, EmploymentAgreementSearch, SignupView, LoginView


router = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="Employment Agreement Management API",
        default_version='v1',
        description="""The Employment Agreements API manages CRUD operations (Create, Read, Update, Delete) for employment agreements
          at Gorai Technology Solutions. This microservice handles employee details, roles, compensation, and
            contractual terms efficiently""",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[],
    authentication_classes=[]

)


urlpatterns = [
  path('', include(router.urls)),
  path('employment-agreements/', EmploymentAgreementListCreate.as_view(),
                name="employment-agreements"),
  path('employment-agreements/<int:pk>/', EmploymentAgreementRetrieveUpdateDestroy.as_view(),
                name="employment-agreements-detail"),
  path('employment-agreements/search/', EmploymentAgreementSearch.as_view(), name='employment-agreement-search'),
  path('signup/', SignupView.as_view(), name='signup'),
  path('login/', LoginView.as_view(), name='login'),
  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
 
]