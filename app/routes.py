from dataclasses import dataclass
from fastapi import FastAPI


@dataclass(frozen=True)
class Routes:
    """Базовый класс подключения роутов."""

    routers: tuple

    def register_routes(self, app: FastAPI):
        """Метод подключения роутов."""

        for router in self.routers:
            app.include_router(router)
