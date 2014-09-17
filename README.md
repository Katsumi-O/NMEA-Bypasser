NMEA-Bypasser
=============

Raspberry Pi で製作するGIS用のスクリプトたち
@meketenさんの作成された手乗りGISを作ってみた際に、作成したスクリプト。
meketenさんの作成されたGISデータベースの作り方は、本人のブログにて公開されている。（http://d.hatena.ne.jp/meketen/）

bypass.pyを起動すればRaspberry PiのGPIOポートのRxdからNMEAメッセージを読み取り、SQLデータベースに問い合わせをする。
その際、実行結果をOpenJtalkを使ってしゃべらせるためにリダイレクトしている。

jsayは（/usr/local/bin/）に配置し、実行権を与えて使用する。

@meketenさんに感謝。
