# -*- coding: latin1 -*-
#############################################
#	OGR2Layers Plugin (c)  for Quantum GIS					#
#	(c) Copyright Nicolas BOZON - 2008					#
#	Authors: Nicolas BOZON, Rene-Luc D'HONT, Michael DOUCHIN, Luca DELUCCHI	#
#	Email: nicolas_dot_bozon_at_gmail_dot_com				#
#										#
#############################################
#    OGR2Layers Plugin is licensed under the terms of GNU GPL 2			#
#  	This program is free software; you can redistribute it and/or modify	#
# 	 it under the terms of the GNU General Public License as published by	#
# 	 the Free Software Foundation; either version 2 of the License, or	#
# 	 (at your option) any later version.					#
#	This program is distributed in the hope that it will be useful,		#
#	 but WITHOUT ANY WARRANTY; without even implied warranty of		#
# 	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.			# 
# 	 See the GNU General Public License for more details.			#
#############################################

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import sys
import os
import urllib2

##convert ogr layer to gml
def createOGR(layer,ui,mydir,iface):
    #the number of last tab
    lastTab=ui.tabWidget.count()-1
    if layer and layer.type() == QgsMapLayer.VectorLayer:
	#source of each vector layer (postgres, shapefile path, etc.)
	mysource = layer.source()
	mysource.remove(QRegExp('\|layerid=[\d]+$'))
	#layer name
	myname = layer.name()
	#layer provider (ogr, postgres, etc.)
	myprovider = layer.dataProvider()
	myprovidername = myprovider.name()
	#layer EpsgCrsId projection
	mysrs = myprovider.crs() #layer spatial reference system
	myepsg = mysrs.epsg()
	myproj4 = mysrs.toProj4()
	#read base layer for choose the projection
	mapBaseLayer = ui.mapBaseLayer.currentIndex()
	if (mapBaseLayer) == 0 or (mapBaseLayer) < 3:
	    #wkt for 900913 EPSG
	    mywkt4326 = 'PROJCS["Google Maps Global Mercator",GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.01745329251994328,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]],PROJECTION["Mercator_2SP"],PARAMETER["standard_parallel_1",0],PARAMETER["latitude_of_origin",0],PARAMETER["central_meridian",0],PARAMETER["false_easting",0],PARAMETER["false_northing",0],UNIT["Meter",1],EXTENSION["PROJ4","+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +wktext  +no_defs"],AUTHORITY["EPSG","900913"]]'
	else:
	    #wkt for 4326 EPSG
	    mywkt4326 = 'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EpsgCrsId","7030"]],AUTHORITY["EpsgCrsId","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EpsgCrsId","8901"]],UNIT["degree",0.01745329251994328,AUTHORITY["EpsgCrsId","9122"]],AUTHORITY["EpsgCrsId","4326"]]'
	#destination of file
	mydestpath = os.path.abspath(os.path.join(str(mydir),str(myname)+".gml"))
	
	if (myproj4 != '' ): #process only vector layers with a well known srs
	#use ogr2ogr to create kml file
	    if (str(myprovidername)=="postgres"): #postgresql
		mypglayerinfo = mysource.split('table')[0]
		myogr2ogr = 'ogr2ogr -a_srs EpsgCrsId:'+str(myepsg)+' -t_srs \''+str(mywkt4326)+'\' -overwrite -f "GML" "'+str(mydestpath)+'" PG:"' + str(mypglayerinfo) + '" layer ' + str(myname)
		res=os.popen(myogr2ogr).readlines()
	    elif (str(myprovidername)=="ogr"): #ogr
		myogr2ogr = 'ogr2ogr -a_srs "' + str(myproj4) + '" -t_srs \''+str(mywkt4326)+'\' -overwrite -f "GML" "' + str(mydestpath) + '" "'+ str(mysource) +'" '
		res=os.popen(myogr2ogr).readlines()
	    #elif (str(myprovidername)==""): #grass

	    else: #do nothing and warn the user for unsupportade providers
		QMessageBox.information(iface.mainWindow(),"Information",str("Only postgres and ogr providers are supported") )
		return 0
	    #take the string of textBrowser and add new layer and ogr2ogr string
	    layerString=ui.textBrowser.toHtml()
	    layerString.append("""<b>%s</b> was reprojected correctly with the following string<br /> <small><code>%s</code></small><br /><br />""" % (myname, myogr2ogr))
	    ui.textBrowser.setHtml(layerString)
	    #set the last tab for show the string
	    ui.tabWidget.setCurrentIndex(lastTab)
	    return 1
	else:
	    #message for unknown spatial reference system
	    QMessageBox.information(iface.mainWindow(),"Information","The layer " + str(myname) + " has an unknown spatial reference system." )
	    return 0
    else:
	#message for not supportaded vector
	QMessageBox.information(iface.mainWindow(),"Information",str("Only PostGIS, and OGR data provider layers are supported, GRASS and Spatialite layers are coming") )
	return 0
##FUNCTION FOR WFS LAYER still does not work
def writeWFS(layer,projection,style=True):
    source = layer.source()
    regexVers = QRegExp('\&VERSION=([\d]+\.[\d]+\.[\d]+)')
    regexFeat = QRegExp('\&TYPENAME=([^\&]+$?)')
    regexUrl = QRegExp('^(.+)[\?\&]SERVICE=WFS')
    regexUrlC = QRegExp('^(.+)SERVICE=WFS')
    if regexVers.indexIn(source) > -1:
	version=regexVers.cap(1)
    else:
	QMessageBox.information(self.iface.mainWindow(),"Information",str("WFS is not compatible") )
    if regexFeat.indexIn(source) > -1:
	feature=regexFeat.cap(1)
    else:
	QMessageBox.information(self.iface.mainWindow(),"Information",str("WFS is not compatible") )
    if regexUrl.indexIn(source) > -1:
	url=regexUrl.cap(1)
    else:
	QMessageBox.information(self.iface.mainWindow(),"Information",str("WFS is not compatible") )
    if regexUrlC.indexIn(source) > -1:
	urlC=regexUrlC.cap(1)
	urlCapabilities = ""+urlC+"SERVICE=WFS&VERSION="+version+"&REQUEST=GetCapabilities"
	getCapabilities = urllib2.urlopen(urlCapabilities)
    else:
	QMessageBox.information(self.iface.mainWindow(),"Information",str("WFS is not compatible") )

    #htmlWFS=['map.addLayer(new OpenLayers.Layer.Vector("'+layer.name()+' WFS", {' \
	#'strategies: [new OpenLayers.Strategy.BBOX()],' \
	#'protocol: new OpenLayers.Protocol.WFS({'\
	#'version: "'+version+'",'\
	#'srsName: "EPSG:'+str(layer.srs().epsg())+'", '\
	#'url:  \''+url+'\','\
	#'featureType: "'+feature+'"'\
    #'}),']
    #if style:
	#htmlWFS.append('projection: "'+projection+'",'\
	#'styleMap:"'+layer.name()+'_style"'\
	#'}))\n;'\
	#)
    #else:
	#htmlWFS.append('projection: "'+projection+'",'\
	#'}))\n;'\
	#)

    htmlWFS=['map.addLayer(new OpenLayers.Layer.WFS("'+layer.name()+' WFS", "'+url+'", ' \
	'{typename: "'+feature+'", srsName: "EPSG:'+str(layer.srs().epsg())+'"}, ']
    if style:
	htmlWFS.append('{projection: "'+projection+'", styleMap: "'+layer.name()+'_style"}))\n')
    else:
	htmlWFS.append('{projection: "'+projection+'"}))\n')

    return htmlWFS


###TEST
#from PyQt4.QtCore import *
#from PyQt4.QtGui import *
#from PyQt4.QtXml import *
#from PyQt4.QtXmlPatterns import * 
#import urllib2
#iFace=qgis.utils.iface
#mapcanvas=iFace.mapCanvas()
#string='EPSG'
#for i in range(mapcanvas.layerCount()):
	#source = mapcanvas.layer(i).source()
	#regex = QRegExp('^(.+)SERVICE=WFS')
	#if regex.indexIn(source) > -1:
		#urlC=regex.cap(1)
		#urlCapabilities = ""+str(urlC)+"SERVICE=WFS&VERSION=1.1.0&REQUEST=GetCapabilities"
		##getCapabilities = urllib2.urlopen(urlCapabilities).read()
		##qtXml=QXmlInputSource()
		##qtXml.setData(getCapabilities)
		#qUrl= QUrl(urlCapabilities)
		#query = QXmlQuery()
		#query.setQuery(string, qUrl)
		#outArray = QByteArray()
		#mybuffer = QBuffer(outArray)
		#mybuffer.open(QIODevice.ReadWrite)
		#formatter = QXmlFormatter(query, mybuffer)
		#query.evaluateTo(formatter) 
		#mybuffer.close()
		#print query.isValid()
		#print QString.fromUtf8(outArray.data()) 

		#result=QXmlResultItems()
		#if (query.isValid()) {
			#query.evaluateTo(&result);
			#while (!item.isNull()) {
				#item = result.next();
			#}
			#if (result.hasError())
		#}

		#qtXmlRead=QXmlSimpleReader()
		#print qtXmlRead.parse(qtXml)