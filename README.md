# MSLM716 BLE Reverse Engineering

Projeto de engenharia reversa para envio de texto e mensagens personalizadas para a smartband MSLM716 via Bluetooth Low Energy (BLE) em Python.

## Hardware
- **Dispositivo:** Smartband MSLM716
- **SoC/Chipset:** Telink TLSR8266
- **App Oficial:** FitPro

## Mapeamento GATT Identificado
- **Serviço de Comunicação:** `0xFFE0` / `0xFEE7`
- **Característica de Escrita (Write):** `0xFFE1` / `0xFEC7`
- **Característica de Notificação:** `0xFFE2`

## Status do Projeto
- [x] Mapeamento de serviços e características via nRF Connect
- [x] Conexão estabelecida via Python (`bleak`)
- [ ] Captura do pacote de handshake/sincronização de hora
- [ ] Exibição bem-sucedida de texto customizado na tela
