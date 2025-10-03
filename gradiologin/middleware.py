from starlette.requests import Request
from starlette.responses import RedirectResponse


def add_middleware_redirect(app, app_route,loginPath):
    @app.middleware("http")
    async def check_authentication(request: Request, call_next):
        if request.url.path.startswith(loginPath+'/login') or request.url.path.startswith(loginPath+'/auth'):
            # Skip authentication check for login and authentication routes
            return await call_next(request)

        if request.url.path==f'{app_route}/api/predict' or request.url.path==f'{app_route}/reset':
            return await call_next(request)

        user = request.session.get("user")
        if not user:

            # User is not logged in, redirect to login page
            return RedirectResponse(url=loginPath+"/login")

        return await call_next(request)

