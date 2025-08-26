# 🔐 JWT Аутентификация API

Реализована полная система JWT аутентификации для твоего Django DRF приложения.

## 🚀 Доступные эндпоинты

### Регистрация пользователя
```
POST /api/auth/register/
```

**Тело запроса:**
```json
{
    "username": "testuser",
    "email": "test@example.com",
    "password": "securepassword123",
    "password_confirm": "securepassword123",
    "first_name": "Иван",
    "last_name": "Иванов"
}
```

**Ответ (201 Created):**
```json
{
    "message": "Пользователь успешно зарегистрирован",
    "user": {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "first_name": "Иван",
        "last_name": "Иванов"
    },
    "tokens": {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
    }
}
```

### Вход в систему
```
POST /api/auth/login/
```

**Тело запроса:**
```json
{
    "username": "testuser",
    "password": "securepassword123"
}
```

**Ответ (200 OK):**
```json
{
    "message": "Вход выполнен успешно",
    "user": {
        "id": 1,
        "username": "testuser",
        "email": "test@example.com",
        "first_name": "Иван",
        "last_name": "Иванов"
    },
    "tokens": {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
    }
}
```

### Обновление токена
```
POST /api/auth/token/refresh/
```

**Тело запроса:**
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

**Ответ (200 OK):**
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### Профиль пользователя (требует аутентификации)
```
GET /api/auth/profile/
```

**Заголовки:**
```
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

**Ответ (200 OK):**
```json
{
    "id": 1,
    "username": "testuser",
    "email": "test@example.com",
    "first_name": "Иван",
    "last_name": "Иванов",
    "date_joined": "2024-01-01T12:00:00Z",
    "last_login": "2024-01-01T12:00:00Z"
}
```

### Обновление профиля (требует аутентификации)
```
PUT /api/auth/update_profile/
PATCH /api/auth/update_profile/
```

**Заголовки:**
```
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

**Тело запроса (PUT - полное обновление, PATCH - частичное):**
```json
{
    "email": "newemail@example.com",
    "first_name": "Новое Имя",
    "last_name": "Новая Фамилия"
}
```

## ⚙️ Настройки JWT

- **Access Token**: действует 1 час
- **Refresh Token**: действует 7 дней
- **Автоматическое обновление**: refresh токены обновляются при использовании
- **Blacklist**: использованные refresh токены добавляются в черный список

## 🧪 Тестирование

1. Запусти сервер:
```bash
uv run python manage.py runserver
```

2. Протестируй регистрацию:
```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com", 
    "password": "securepassword123",
    "password_confirm": "securepassword123",
    "first_name": "Тест",
    "last_name": "Пользователь"
  }'
```

3. Протестируй вход:
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "password": "securepassword123"
  }'
```

4. Протестируй защищенный эндпоинт:
```bash
curl -X GET http://localhost:8000/api/auth/profile/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## 🔧 Что реализовано

✅ JWT аутентификация с access и refresh токенами  
✅ Регистрация новых пользователей с валидацией  
✅ Вход в систему с проверкой учетных данных  
✅ Получение и обновление профиля пользователя  
✅ Автоматическое обновление токенов  
✅ Защита эндпоинтов через JWT  
✅ Русские сообщения об ошибках  

## 📝 Следующие шаги

Теперь ты можешь:
1. Создать модели для машин и записей
2. Добавить эндпоинты для управления автомобилями
3. Реализовать систему заметок и учета пробега
4. Добавить загрузку фотографий автомобилей
