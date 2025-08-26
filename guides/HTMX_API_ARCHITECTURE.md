# 🏗 HTMX + DRF API Архитектура

Переработали проект на **единую API-ориентированную архитектуру** где веб-интерфейс работает через твои DRF endpoints.

## 🎯 **Новая архитектура**

```
┌─ Frontend (HTMX + JavaScript) ─┐    ┌─ Backend (Django DRF) ─┐
│                                 │    │                        │
│ • JWT в localStorage            │◄──►│ • JWT Authentication   │
│ • HTMX requests + Bearer token │    │ • API ViewSets         │
│ • Alpine.js для состояния      │    │ • Сериализаторы        │
│ • Минимальные HTML templates   │    │ • Permissions          │
│ • JavaScript API helpers       │    │ • Единое API для всех  │
└─────────────────────────────────┘    └────────────────────────┘
```

## ✅ **Что изменилось**

### **Было (гибридный подход):**
- Веб → Session-based auth + Django views  
- API → JWT auth + DRF ViewSets

### **Стало (единый подход):**
- Веб → JWT auth + DRF API + HTMX
- Мобильные → JWT auth + DRF API + нативные запросы

## 🔧 **Компоненты системы**

### **1. База (`templates/base/api_base.html`)**
- **JWT управление** в localStorage
- **Alpine.js store** для состояния аутентификации  
- **HTMX настройки** для автоматической передачи токенов
- **API helpers** (`window.api.*`) для работы с DRF
- **Глобальные утилиты** (сообщения, обработка ошибок)

### **2. Аутентификация**
- **`/login/`** → `api_login.html` → `/api/auth/api/login/`
- **`/register/`** → `api_register.html` → `/api/auth/api/register/`
- **Автоматический редирект** на основе наличия токена
- **Обработка ошибок 401** с автоматическим logout

### **3. Dashboard**
- **`/dashboard/`** → `api_dashboard.html` 
- **Загрузка профиля** через `/api/auth/api/profile/`
- **Редактирование профиля** через `/api/auth/api/update_profile/`
- **Статистика** (заготовка для будущих API)

## 🚀 **Ключевые возможности**

### **JWT Token Management**
```javascript
// Автоматическая передача токенов в HTMX
document.addEventListener('htmx:configRequest', function(evt) {
    const token = getAuthToken();
    if (token) {
        evt.detail.headers['Authorization'] = 'Bearer ' + token;
    }
});

// Обработка истечения токенов
document.addEventListener('htmx:responseError', function(evt) {
    if (evt.detail.xhr.status === 401) {
        // Автоматический logout и редирект
        localStorage.removeItem('access_token');
        window.location.href = '/login/';
    }
});
```

### **API Helpers**
```javascript
// Удобные функции для работы с API
window.api.get('/api/cars/')
window.api.post('/api/cars/', carData)
window.api.put('/api/cars/1/', updateData)
window.api.delete('/api/cars/1/')
```

### **Reactive UI с Alpine.js**
```javascript
// Состояние аутентификации
function authStore() {
    return {
        isAuthenticated: false,
        user: null,
        async fetchUserProfile() { ... },
        logout() { ... }
    }
}
```

## 📋 **Преимущества новой архитектуры**

### ✅ **Единообразие**
- **Одни и те же API endpoints** для веба и мобильных приложений
- **Единая логика валидации** в DRF сериализаторах
- **Одинаковые права доступа** через DRF permissions

### ✅ **Масштабируемость**
- **Легко добавить мобильное приложение** - API уже готово
- **Микросервисная архитектура** - фронтенд отделен от бэкенда
- **API-first подход** - можно легко менять фронтенд

### ✅ **Современность**
- **SPA-like опыт** с HTMX без сложности React/Vue
- **JWT токены** - industry standard
- **RESTful API** - стандартный подход

### ✅ **Простота разработки**
- **Меньше Django views** - только API endpoints
- **Переиспользование логики** между веб и мобильными
- **Лучшее разделение ответственности**

## 🔄 **Текущие эндпоинты**

### **HTML Views** (минимальные)
```
GET  /           → redirect to dashboard
GET  /login/     → api_login.html
GET  /register/  → api_register.html  
GET  /dashboard/ → api_dashboard.html
```

### **API Endpoints** (основная логика)
```
POST /api/auth/api/login/          → JWT login
POST /api/auth/api/register/       → JWT register
GET  /api/auth/api/profile/        → get user profile
PATCH /api/auth/api/update_profile/ → update user profile
POST /api/auth/token/refresh/      → refresh JWT token
```

## 📱 **Пример использования**

### **Регистрация пользователя**
1. Пользователь заполняет форму в `api_register.html`
2. JavaScript отправляет POST `/api/auth/api/register/`
3. Получает JWT токены и сохраняет в localStorage
4. Редиректит на dashboard

### **Загрузка профиля**
1. `api_dashboard.html` загружается в браузере
2. Alpine.js проверяет наличие токена в localStorage  
3. Делает GET `/api/auth/api/profile/` с Bearer токеном
4. Отображает данные пользователя

### **Обработка ошибок**
1. Если токен истек - API возвращает 401
2. HTMX автоматически ловит ошибку
3. JavaScript очищает localStorage и редиректит на login

## 🚀 **Следующие шаги**

Теперь можно добавлять новый функционал **только через API**:

1. **Создать модели** автомобилей (Car, Note, Expense)
2. **DRF ViewSets** для CRUD операций  
3. **HTMX шаблоны** для отображения данных
4. **JavaScript** для интерактивности

Каждая новая фича будет работать **одинаково** для веба и будущих мобильных приложений!

---

🎉 **Архитектура готова!** Единый API-подход обеспечивает консистентность и масштабируемость.
