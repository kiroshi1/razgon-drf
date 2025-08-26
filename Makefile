.PHONY: run lint

# Запуск приложения
run:
	uv run python manage.py runserver

# Проверка линтером Ruff
lint:
	uv run ruff check .
