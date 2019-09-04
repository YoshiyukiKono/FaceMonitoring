同じLAN内に接続したRaspberry PiのIPアドレスを調べる

https://qiita.com/xshell/items/af4e2ef8d804cd29e38e

brew install arp-scan

sudo arp-scan -l --interface en0

192.168.1.1    bc:5c:dc:ad:5f:ef   (Unknown)
192.168.1.10   b8:27:eb:22:23:08   Rasberry Pi Foundation
192.168.1.100  4f:5c:e2:12:65:cd   (Unknown)
