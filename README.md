# Mercado Sabanero – Módulo de Liquidación de Compras

## Resumen del Proyecto
**Mercado Sabanero** es el núcleo de lógica de negocio (sin interfaz gráfica ni base de datos) para la liquidación de compras en un e-commerce local de la región sabanera (departamento de Sucre, Colombia). Desarrollado íntegramente bajo la metodología **TDD (Test-Driven Development)**, el módulo se encarga de:

- **Gestión del Carrito (HU-01):** Validación de cantidades por operación (1 a 50) y control de stock acumulado mediante integración simulada con inventario.
- **Cálculo de IVA Diferencial (HU-02):** Aplicación de tarifas del 0%, 5% y 19% sobre valores netos posdescuento con redondeo al peso más cercano.
- **Descuentos por Volumen (HU-03):** Descuentos automáticos escalonados por subtotal (0%, 5% y 10%).
- **Cupones Promocionales (HU-04):** Validación de cupones con vigencia, montos mínimos (ej. `SABANERO10`) y no acumulabilidad (prevalece el mayor porcentaje).
- **Tarifas y Envío Gratis (HU-05):** Cálculo de flete por municipio (Sincelejo, Corozal, Sampués) y envío gratuito para pedidos con IVA $\ge \$150.000$ o cupón `ENVIOGRATIS`.
- **Fidelización y Puntos (HU-06):** 1 punto por cada $1.000 completos (excluyendo el costo de envío) con multiplicador x2 para clientes Oro.

---

## Requisitos Previos
- **Python 3.11** o superior instalado en el sistema.

---

## Guía Paso a Paso para Ejecutar el Proyecto

### 1. Crear el entorno virtual
Abre tu terminal en la carpeta raíz del proyecto y ejecuta:

```bash
python -m venv .venv
```

### 2. Activar el entorno virtual

- **En Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
  *(O en el Símbolo del sistema / CMD: `.venv\Scripts\activate.bat`)*

- **En Windows (Git Bash):**
  ```bash
  source .venv/Scripts/activate
  ```

### 3. Instalar dependencias
Con el entorno virtual activado:
```bash
pip install -r requirements.txt
```
---

## Ejecución de Pruebas y Cobertura

### Todas las pruebas unitarias e integrales
```bash
pytest -v
```
*(O directamente: `source .venv/Scripts/activate`
`pytest -v`)*

### Reporte de cobertura en consola
```bash
pytest --cov=mercado_sabanero --cov-report=term-missing
```

### Generar reporte visual en HTML
```bash
pytest --cov=mercado_sabanero --cov-report=html
```
El reporte detallado se generará en `htmlcov/index.html`.

---

## Estructura del Proyecto
- `mercado_sabanero/` – Lógica del dominio:
  - `carrito.py`: Manejo de ítems y validación de stock.
  - `cupones.py`: Validación y reglas de cupones comerciales.
  - `descuentos.py`: Descuentos por rangos de volumen.
  - `envio.py`: Tarifas de entrega por municipio y reglas de gratuidad.
  - `iva.py`: Cálculo de IVA por línea y tasa correspondiente.
  - `liquidacion.py`: Orquestador principal del proceso de compra.
  - `puntos.py`: Reglas de fidelización de clientes.
  - `modelos.py`, `errores.py`, `redondeo.py`: Entidades base, excepciones de dominio y utilidades.
- `tests/` – Suite de pruebas automatizadas:
  - Pruebas por historia de usuario (`test_hu01_carrito.py` a `test_hu06_puntos.py`).
  - Pruebas de integración completa (`test_liquidacion_integral.py`).