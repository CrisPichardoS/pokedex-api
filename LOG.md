# 📓 Bitácora de Implementación: Pokedex API & Azure Hybrid DevOps

Este documento detalla la progresión técnica, los desafíos de infraestructura y las soluciones de seguridad implementadas durante el ciclo de vida de este proyecto.

## 🏗️ Fase 1: Desarrollo y Contenerización
- **Tecnología:** Desarrollo de una API REST utilizando **Python 3.9** y **FastAPI**.
- **Virtualización:** Configuración de entorno local en **Ubuntu 24.04 (WSL2)**.
- **Dockerización:** - Creación de `Dockerfile` optimizado.
    - Gestión de imágenes en **Docker Hub** (`cpichardos/pokedex-api:v1`).
    - Solución de errores de visibilidad de imagen (Public vs Private).

## ☁️ Fase 2: Despliegue en Azure (Troubleshooting)
Se realizaron múltiples intentos de despliegue en **Azure Container Instances (ACI)**, enfrentando y resolviendo retos de nivel corporativo:
- **Gobernanza (Azure Policy):** Identificación y mitigación de errores `RequestDisallowedByAzure` mediante el cambio estratégico de regiones (South Central US).
- **Resource Providers:** Activación manual de proveedores de servicios (`Microsoft.Web` y `Microsoft.ContainerInstance`) vía Azure CLI.
- **Gestión de Cuotas:** Diagnóstico de restricciones de capacidad (Quota: 0) en la suscripción académica de la **Universidad APEC**.

## 🛠️ Fase 3: Solución Híbrida y Conectividad
Ante las restricciones de cuota en la nube, se implementó una arquitectura híbrida:
- **Túneles Seguros:** Implementación de **Ngrok** para exponer el puerto 8000 del contenedor local a una URL pública.
- **Automatización CLI:** Uso de la terminal nativa de Linux para la instalación de dependencias vía **Snap**.

## 🔐 Fase 4: Seguridad y Flujo de Trabajo (Git Ops)
Optimización del flujo de trabajo de desarrollo en la laptop **Victus**:
- **Identidad:** Configuración global de firma de commits para **Cristhian Pichardo**.
- **Autenticación Robusta:** Transición de tokens manuales (PAT) a llaves **SSH (Ed25519)** para comunicación cifrada y automática con GitHub.
- **Higiene de Código:** Implementación de `.gitignore` para eliminar archivos de entorno virtual (`venv`) y optimizar el peso del repositorio.

---
**Cristhian Pichardo** *Ingeniero DevOps en Formación | República Dominicana*