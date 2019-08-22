# Dataflow

## NiFi

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
### NiFi Flow
#### NiFi
'Input Port' to 'PutFile' Processor
#### MiNiFi
'GetFile' Processor to 'Remote Process Group'

Note: 'Remote Input Host' (nifi.remote.input.host) must be the same as the host of URLs for 'Remote Process Group'

## Reference

MiNiFiでRaspberryPiのカメラを制御し、写真をNiFiにアップロード、Hadoopに保存

https://qiita.com/zz22394/items/de66b286748831042fa1

Using MiniFi to read data from a Sense HAT on a Raspberry Pi 3

https://community.cloudera.com/t5/Community-Articles/Using-MiniFi-to-read-data-from-a-Sense-HAT-on-a-Raspberry-Pi/ta-p/244536
