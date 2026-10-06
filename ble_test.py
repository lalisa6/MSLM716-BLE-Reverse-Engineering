import asyncio
from bleak import BleakClient

# Endereço MAC do relógio MSLM716
DEVICE_MAC = "BA:03:54:17:5D:33"

# Característica GATT de escrita (UUID 0xFFE1)
CHAR_WRITE_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

# Pacotes hexadecimais para teste de engenharia reversa
# CD00020C01 -> Comando 'Find Band' (Procurar Pulseira)
# AB000DFF020148656C6C6F -> Notificação Push com o texto "Hello"
HEX_PAYLOAD = "CD00020C01"

async def main():
    print(f"A conectar ao dispositivo {DEVICE_MAC}...")
    
    async with BleakClient(DEVICE_MAC) as client:
        if client.is_connected:
            print("Conexão estabelecida com sucesso!")
            
            # Converte a string hexadecimal em bytes brutos
            payload_bytes = bytes.fromhex(HEX_PAYLOAD)
            
            print(f"A enviar pacote: {HEX_PAYLOAD}")
            await client.write_gatt_char(CHAR_WRITE_UUID, payload_bytes, response=False)
            print("Pacote enviado! A aguardar resposta da tela...")
        else:
            print("Falha ao conectar ao dispositivo.")

if __name__ == "__main__":
    asyncio.run(main())
