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
