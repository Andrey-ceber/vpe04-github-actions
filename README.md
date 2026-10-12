# VPe04 Time Server

Учебный проект к уроку 34 по CI/CD и GitHub Actions. FastAPI-приложение возвращает текущее время, поддерживает часовые пояса и предоставляет health endpoint.

## API

- `GET /` — информация о сервисе.
- `GET /health` — проверка состояния.
- `GET /time` — текущее время UTC.
- `GET /time/{timezone_name}` — время в указанной IANA-зоне, например `/time/Europe/Moscow`.
- `GET /docs` — Swagger UI.

## Локальный запуск

```bash
python -m venv .venv
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

## Docker

```bash
docker build -t vpe04-time-server .
docker run --rm -p 8000:8000 vpe04-time-server
```

## CI/CD

Workflow `.github/workflows/deploy.yml` при каждом push в `main`:

1. запускает тесты;
2. собирает Docker-образ;
3. публикует образ в GitHub Container Registry;
4. подключается к VPS по SSH и обновляет контейнер на порту `8001`;
5. проверяет `/health` после запуска.

Для SSH-деплоя используются GitHub Secrets: `HOST`, `USERNAME`, `SSH_KEY`, `PORT`.
