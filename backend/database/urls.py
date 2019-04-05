from dejavu_base.urls import base_development_routes
from dejavu_base.urls import base_admin_routes
from dejavu_base.urls import base_api_routes
from dejavu_base.urls import base_login_routes
from dejavu_base.urls import base_spa_routes

from database import __version__
from .api import api_router


context = {
    'version': __version__,
    'project_name': 'database',
}


urlpatterns = (
    base_development_routes() +
    base_login_routes(context) +
    base_admin_routes() +
    base_api_routes(api_router) +
    base_spa_routes(context, private=False)
)
