import aiohttp.web

import virtool.analyses.api
import virtool.indexes.api
import virtool.routes


async def startup_routes(app: aiohttp.web.Application):
    """Add routes to jobs API."""
    for routes in virtool.routes.ROUTES:
        app.add_routes(routes.jobs_api)
