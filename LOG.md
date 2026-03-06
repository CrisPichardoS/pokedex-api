# 📓 Bitácora de Implementación y Resolución de Incidentes

Este documento detalla la progresión técnica y los obstáculos superados durante el despliegue de la Pokédex API.

## 🛠️ Fase 1: Contenerización y Registro
- **Dockerización:** Creación de imagen base Python 3.9-slim.
- **Docker Hub:** Resolución de errores de visibilidad y nomenclatura mediante `docker tag` y `docker push` exitoso a `cpichardos/pokedex-api:v1`.

## ☁️ Fase 2: Infraestructura en Azure (Troubleshooting)
- **Gobernanza:** Identificación de restricciones por políticas de región (`RequestDisallowedByAzure`).
- **Resource Providers:** Registro manual de proveedores críticos mediante Azure CLI:
  - `Microsoft.Web`
  - `Microsoft.ContainerInstance`
- **Gestión de Cuotas:** Diagnóstico de límite de cuota `0` en la suscripción académica de la Universidad APEC.

## 🚀 Fase 3: Solución Híbrida y Exposición
- **Pivot Técnico:** Ante la restricción de Azure, se implementó un túnel seguro con **Ngrok**.
- **Seguridad:** Configuración de `Personal Access Token` (PAT) para el control de versiones en Git, superando la depreciación de contraseñas de GitHub.

## ✅ Conclusión
Se logró un entorno funcional que combina desarrollo local en **Ubuntu 24.04 (WSL2)** con exposición pública, demostrando resiliencia y capacidad de respuesta ante fallos de proveedores de nube.
