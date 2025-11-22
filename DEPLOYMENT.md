# 🚀 Guía de Despliegue - Predictor de Compras E-Commerce

## ✅ Modelo Entrenado
- **Algoritmo**: Logistic Regression
- **Precisión**: 96%
- **Archivo**: modelo.pkl (incluido en el proyecto)

## 🌐 Plataformas de Despliegue Recomendadas

### 1. **Render** (MÁS RECOMENDADO - GRATIS) ⭐
**Por qué es mejor:**
- ✅ Completamente gratis para proyectos pequeños
- ✅ Despliega directamente desde GitHub
- ✅ Muy fácil de usar
- ✅ SSL automático (HTTPS)
- ✅ No necesitas tarjeta de crédito

**Pasos para desplegar:**
1. Crea una cuenta en [render.com](https://render.com)
2. Conecta tu repositorio de GitHub
3. Crea un nuevo "Web Service"
4. Render detectará Flask automáticamente
5. ¡Listo! Tu app estará en línea en minutos

**Configuración necesaria:**
```bash
# Build Command (déjalo vacío, Render lo detecta)
# Start Command:
gunicorn app:app
```

### 2. **Railway** (FÁCIL Y MODERNO) 🚂
**Ventajas:**
- ✅ $5 USD gratis al mes
- ✅ Deploy automático con GitHub
- ✅ Interfaz moderna y simple
- ✅ Base de datos PostgreSQL gratis

**URL**: [railway.app](https://railway.app)

### 3. **Fly.io** (POTENTE Y GRATIS) 🪰
**Ventajas:**
- ✅ 3 aplicaciones gratis
- ✅ Buen rendimiento
- ✅ Deploy con un comando

**URL**: [fly.io](https://fly.io)

### 4. **Vercel** (CON SERVERLESS) ⚡
**Ventajas:**
- ✅ Gratis para proyectos personales
- ✅ Muy rápido
- ✅ Requiere adaptación a serverless

**URL**: [vercel.com](https://vercel.com)

### 5. **Heroku** (CLÁSICO) 💜
**Nota**: Ya no tiene plan gratuito, pero es muy conocido
- Costo: $7 USD/mes
- Muy confiable

---

## 📦 Archivos Necesarios para Deploy

### Para Render/Railway/Heroku:
Necesitas agregar este archivo:

**`gunicorn` en requirements.txt:**
```txt
Flask==3.0.0
scikit-learn==1.7.2
numpy==1.24.4
joblib==1.5.2
pandas==2.3.3
scipy==1.15.3
gunicorn==21.2.0
```

### Opcionalmente, crea `Procfile` (para Heroku):
```
web: gunicorn app:app
```

---

## 🎯 Mi Recomendación: RENDER

### Pasos Detallados para Render:

1. **Prepara tu proyecto:**
   ```bash
   # Asegúrate de tener estos archivos:
   # - app.py
   # - modelo.pkl
   # - requirements.txt (con gunicorn)
   # - templates/
   # - static/
   ```

2. **Sube a GitHub:**
   ```bash
   git add .
   git commit -m "Preparar para deploy"
   git push origin main
   ```

3. **En Render.com:**
   - Click en "New +" → "Web Service"
   - Conecta tu repositorio GitHub
   - Configuración:
     - **Name**: predictor-ecommerce (o el que quieras)
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
   - Click en "Create Web Service"

4. **¡Listo!** Tu app estará en: `https://predictor-ecommerce.onrender.com`

---

## 🔧 Configuración Adicional para Render

Agrega a tu `app.py` al final:

```python
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

---

## 📊 Comparación Rápida

| Plataforma | Gratis | Facilidad | Velocidad Deploy |
|------------|--------|-----------|------------------|
| **Render** | ✅ Sí  | ⭐⭐⭐⭐⭐ | 5-10 min         |
| Railway    | $5/mes | ⭐⭐⭐⭐⭐ | 3-5 min          |
| Fly.io     | ✅ Sí  | ⭐⭐⭐⭐   | 5-10 min         |
| Vercel     | ✅ Sí  | ⭐⭐⭐     | 5-10 min         |
| PythonAnywhere | ✅ Sí | ⭐⭐    | 15-30 min        |

---

## ❓ ¿Por qué NO PythonAnywhere?

- ❌ Configuración manual compleja
- ❌ Problemas con versiones de librerías
- ❌ Interfaz web antigua
- ❌ Más difícil de debuggear
- ✅ Pero... sigue siendo gratis y funcional

---

## 🆘 Solución de Problemas

### Error: "Module not found"
```bash
# Verifica que requirements.txt tenga todas las dependencias
pip freeze > requirements.txt
```

### Error: "Application failed to respond"
```python
# Asegúrate de usar host='0.0.0.0' en app.run()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```

---

## 📞 Recursos

- [Documentación Render](https://render.com/docs)
- [Railway Docs](https://docs.railway.app)
- [Fly.io Docs](https://fly.io/docs)

---

**¡Éxito con tu deploy! 🎉**
