# Edge
## Abstruct
Edge(Camera) > MiNiFi > NiFi > OS File System

### Camera

#### Check
```
vcgencmd get_camera
```

```
raspistill -o ./picture/camera.jpg
```

#### Daemon
/usr/lib/systemd/system/cameradaemon.service
```
[Unit]
Description=CameraDaemon

[Service]
ExecStart=/opt/camera_daemon.py
Restart=always
Type=forking
PIDFile=/var/run/camera_daemon.pid

[Install]
WantedBy=multi-user.target
```

```
sudo systemctl daemon-reload

sudo systemctl list-unit-files --type=service | grep camera

sudo systemctl enable cameradaemon
sudo systemctl start cameradaemon
sudo systemctl status cameradaemon

sudo systemctl disable cameradaemon
```

### MiNiFi Flow
1. ExecuteProcess
1. GetFile -> To: Image From MiNiFi -> NiFi Flow

### NiFi Flow
1. Image From MiNiFi
1. PutFile
1. (Optional) PutHDFS (or Put HBase?)

## Environment Preparation

### Edge Device - Raspberry Pi

#### OS Install

#### Device Setup

* Raspberry Pi Camera Module V2

#### MiNiFi Setup

```
sudo su -
cd /home/pi

#HortonworksのサイトからMiNiFiのtarファイルをダウンロードする
curl -O http://public-repo-1.hortonworks.com/HDF/3.3.1.0/minifi-0.6.0.3.3.1.0-10-bin.tar.gz
curl -O http://public-repo-1.hortonworks.com/HDF/3.3.1.0/minifi-toolkit-0.6.0.3.3.1.0-10-bin.tar.gz

#ファイル解答し、シンボリックリンクを作成する
tar -zxvf minifi-0.6.0.3.3.1.0-10-bin.tar.gz
tar -zxvf minifi-toolkit-0.6.0.3.3.1.0-10-bin.tar.gz
ln -s minifi-0.6.0.3.3.1.0-10 minifi
ln -s minifi-toolkit-0.6.0.3.3.1.0-10 tool_minifi

#MiNiFiをインストールする
sudo ./minifi/bin/minifi.sh install
#必要に応じてリモートNiFiホストを/etc/hostsに追加する
```

### Operation

```
./minifi/bin/minifi.sh start
./minifi/bin/minifi.sh status
./minifi/bin/minifi.sh stop
```


## Reference

### Camera

PythonでRaspberry Pi カメラを制御する

https://iotdiyclub.net/raspberry-pi-camera-python-1/

### Sensor

MiNiFiでセンサーデータを取得し、NiFiに転送してHDFS、Hiveに書き込む

https://viewse.blogspot.com/2019/06/minifinifihdfshive_5.html

ラズベリーパイで温度・湿度・気圧をまとめて取得！AE-BME280でIC2通信

https://deviceplus.jp/hobby/raspberrypi_entry_039/

ラズパイ+BME280でIoT環境センサー構築(その1)

https://qiita.com/hawk777/items/2b910a81df480268e07e


pythonをデーモン化するメモ

https://qiita.com/croquisdukke/items/9c5d8933496ba6729c78
