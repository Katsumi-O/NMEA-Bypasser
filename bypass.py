#51C4E3#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bypasser.py
#  
#  Copyright 2014 ogasawara <ogasawara@ThinkCentre>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from math import modf
import commands
import serial

ser = serial.Serial('/dev/ttyAMA0',9600, timeout=1)
ser.open()

def main():

	nmea_messages = ser.readline()
	nmea = nmea_messages.split(',')
	#NMEAメッセージから必要な一文を抽出する
	while nmea[0] != '$GPGGA':
		nmea_messages = ser.readline()
		nmea = nmea_messages.split(',')

	print nmea_messages
	#緯度・経度をそれぞれLng,Latに格納
	Lng = nmea[2]	#緯度
	Lat = nmea[4]	#経度
	#ダサいけど、度分秒表記から度表記に変更する処理を関数化せずにべた書き
	#緯度
	decimal, integer = modf(float(Lng)/100.0)
	converted_Lng = integer+ decimal / 60.0 * 100.0
	#経度
	decimal, integer = modf(float(Lat)/100.0)
	converted_Lat = integer + decimal / 60.0 * 100.0
	
	#ここでシェルスクリプトをPythonから実行する
	#この段階ではSQLのクリエを実行して住所を取得するところまで
	#なぜだかjsayにリダイレクトできない
	cmd1 = commands.getoutput('sed "s/@@@@/'+ str(converted_Lat) + ' ' + str(converted_Lng) +'/g" ./get_adress.sql|psql -At postgis')
	print cmd1
	cmd2 = commands.getoutput('jsay ' + cmd1)
	print cmd2
	#
	return 0
	
	
if __name__ == '__main__':
	main()
