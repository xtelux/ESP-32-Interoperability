import paho.mqtt.client as mqtt
host = "127.0.0.1"
port = 1883
topik = "test/topic"

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"Berhasil terhubung. Status {rc}")
        client.subscribe(topik)
        print(f"Topic : {topik}\n")
    else:
        print(f"Gagal terhubung")

def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    print(f"Pesan diterima. Topik : {msg.topic} | Pesan : {payload}")

def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message
    print(f"Server : {host}:{port}")
    client.connect(host, port, 60)
    client.loop_forever()

if __name__ == "__main__":
    main()
