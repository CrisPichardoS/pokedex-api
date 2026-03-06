# 🚀 Pokédex API: Microservicio Contenerizado y Azure Hybrid Cloud

Este proyecto demuestra el ciclo de vida de un microservicio desde el desarrollo local en **Ubuntu 24.04 (WSL2)** hasta su exposición pública.

## 📊 Diagrama de Flujo del Despliegue

```mermaid
graph TD
    A[Código Python/FastAPI] --> B{Dockerize}
    B --> C[Imagen Local: pokedex-api]
    C --> D[Docker Push: Docker Hub]
    D --> E{Azure Cloud Check}
    E -->|Error: Azure Policy| F[Cambio de Región: South Central US]
    F -->|Error: Quota 0| G[Pivot: Local Tunneling]
    G --> H[Ngrok Tunnel]
    H --> I[API Pública Activa]
    
    subgraph "Infraestructura Local (Victus by HP)"
    A
    B
    C
    H
    end
