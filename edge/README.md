# Edge

Edge(Camera) > MiNiFi > NiFi > OS File System

## Environment Preparation

### Edge Device - Raspberry Pi

#### OS Install

#### Device Setup

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

#### NiFi Setup

```
wget http://ftp.jaist.ac.jp/pub/apache/nifi/1.9.2/nifi-1.9.2-bin.tar.gz
tar xvf nifi-1.9.2-bin.tar.gz
vi 
```

nifi.properties
```
nifi.sensitive.props.key=<password>
```

nifi.service
```
[Unit]
Description=Apache nifi daemon

[Service]
Type=forking
User=apache
Environment=JAVA_HOME=/usr/java/default
ExecStart=/opt/nifi-1.8.0/bin/nifi.sh start
ExecStop=/opt/nifi-1.8.0/bin/nifi.sh stop

[Install]
WantedBy=multi-user.target
```

## Reference

MiNiFiでセンサーデータを取得し、NiFiに転送してHDFS、Hiveに書き込む

https://viewse.blogspot.com/2019/06/minifinifihdfshive_5.html

ラズベリーパイで温度・湿度・気圧をまとめて取得！AE-BME280でIC2通信

https://deviceplus.jp/hobby/raspberrypi_entry_039/

ラズパイ+BME280でIoT環境センサー構築(その1)

https://qiita.com/hawk777/items/2b910a81df480268e07e


pythonをデーモン化するメモ

https://qiita.com/croquisdukke/items/9c5d8933496ba6729c78
