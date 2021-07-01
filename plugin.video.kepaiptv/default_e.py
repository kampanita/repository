# coding=utf-8
# -*- coding: utf-8 -*-
#------------------------------------------------------------
# KepaIPTV - XBMC Add-on by Kepa
# Version 2.1 (26.04.2021)
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Gracias a la librería plugintools de Jesús y a torete (www.mimediacenter.info)
import os
import sys
try:
    from urllib.request import urlopen
    import urllib.request as urllib2
    from urllib.parse import urlparse
    import urllib.parse as urllib_
    import urllib.error
except:
    from urllib import urlopen    
    from urlparse import urlparse
    import urllib as urllib_
    import urllib2
import re
import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
import plugintools
import unicodedata
import requests
import shutil
import base64
import time
import random

PY3=False
if sys.version_info[0] >= 3: PY3 = True; unicode = str; unichr = chr; long = int
addon = xbmcaddon.Addon()
addonname = '[LOWERCASE][CAPITALIZE][COLOR white]kepa[COLOR white]iptv[/CAPITALIZE][/LOWERCASE][/COLOR]'
icon = addon.getAddonInfo('icon')
myaddon = xbmcaddon.Addon("plugin.video.kepaiptv")
#px={"http": "http://14.139.189.213:3128"}
px=''
local_file=xbmc.translatePath('special://home/addons/plugin.video.kepaiptv/proxy.dat')

## Fotos
thmb_nada='https://static.thenounproject.com/png/409659-200.png'
thmb_ver_canales='https://f318b49c-a-62cb3a1a-s-sites.googlegroups.com/site/almacenkampanita/icon.jpg?attachauth=ANoY7cp7d8onHhHZiRfZP9uhd6nLdUfqocQLHn72B5jn3DxeHF_-HUx9G4UKxu7-HGGhnc8qhYQn8V0d1XB7uy6m5IetTdfQdw8yzGWavPYx229l8SR3VbxbomPnjCBcTPKNNtTR1A8RURvEGp6TNbXLVaUum2BZM3uChUxKkfVYNlzGFl4MdZcPRb9zYPgq7oFql5aW4FINttVbZ9Y-ogMnyMVSUd5ATw%3D%3D&attredirects=0'
thmb_cambio_servidor='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbF_teVdXBpT8s-D8go4LQRnYiDpP5k5YgNQ&usqp=CAU'
thmb_cambio_mac='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStWUTJmL6MbeaZUngkk1AnFS0kIsHFqUiSqbKayR-W2BGIoL8ov3E4Tf6Q_MpYpHTIUPs&usqp=CAU'
thmb_carga_servidores='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRup-gZATZL0rtNpZkg8UiKuOM-DmEY4az5Xq8arVwVM9IHXARs_RDjOt-R3PgV37rN1ts&usqp=CAU'
thmb_guarda_servidores='https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Gnome-document-save.svg/1024px-Gnome-document-save.svg.png'
thmb_nuevo_servidor='https://icons.iconarchive.com/icons/custom-icon-design/pretty-office-9/256/new-file-icon.png'
thmb_guia='https://static.vecteezy.com/system/resources/previews/000/567/906/non_2x/vector-tv-icon.jpg'
fanny="https://i.ytimg.com/vi/_7bFXWNfXTY/maxresdefault.jpg"
fanart_guia="http://www.panoramaaudiovisual.com/wp-content/uploads/2012/01/EPG-Toshiba-Smart-Tv-web.png"
def run():
    #
    
    # Get params
           
    params = plugintools.get_params()
    
    if params.get("action") is None:
        if PY3==False:
            xbmc.executebuiltin('Container.SetViewMode(51)')        
        
        main_list(params)
    else:
       if PY3==False:
           xbmc.executebuiltin('Container.SetViewMode(51)') 
       action = params.get("action")
       url = params.get("url")
       exec (action+"(params)")

    plugintools.close_item_list()

def cambia_fondo():

    foto = xbmc.translatePath('special://home/addons/plugin.video.kepaiptv/fondo.jpg')    
    if not xbmc.getCondVisibility('Skin.String(CustomBackgroundPath)'):      
        xbmc.executebuiltin('Skin.Reset(CustomBackgroundPath)')
        xbmc.executebuiltin('Skin.SetBool(UseCustomBackground,True)')   
        xbmc.executebuiltin('Skin.SetString(CustomBackgroundPath,'+foto+')')
        xbmc.executebuiltin('ReloadSkin()')
    
def main_list(params):
    proxy=params.get('extra')
    import shutil,xbmc  
    try:
        addon_path3 = xbmc.translatePath('special://home/cache').decode('utf-8')
        shutil.rmtree(addon_path3, ignore_errors=True) 
    except:
        pass
    
    cambia_fondo()
        
    escogido=myaddon.getSetting('escogido')
    mac=myaddon.getSetting('mac2')
    


    plugintools.log("kepaiptv.main_list ")    
    plugintools.add_item(action="", thumbnail=thmb_nada,title="[COLOR gray]Ver Canales----------------------------------------------------------------------------[/COLOR]",folder= False )
    plugintools.add_item(action="ver_canales",    title="[COLOR red]i[COLOR white]P[COLOR green]TV[COLOR white] CHaNNeLS[/COLOR]",thumbnail=thmb_ver_canales,fanart="https://i.ytimg.com/vi/_7bFXWNfXTY/maxresdefault.jpg",folder= True )            

    plugintools.add_item(action="", thumbnail=thmb_nada,title="[COLOR gray]Config Actual--------------------------------------------------------------------------[/COLOR]",folder= False )
    plugintools.add_item(action="cambio_servidor",    title="[COLOR white]SERVER ACTUAL:   [COLOR springgreen]"+escogido+" [/COLOR]",thumbnail=thmb_cambio_servidor,fanart="https://www.zooplus.es/magazine/wp-content/uploads/2018/04/fotolia_169457098.jpg",folder= True )               
    plugintools.add_item(action="cambio_mac",         title="[COLOR white]MAC ACTUAL      :   [COLOR springgreen]"+mac+' [/COLOR]',thumbnail=thmb_cambio_mac,fanart="https://www.miwuki.com/wp-content/uploads/2016/11/gatito-830x623-300x225.jpg",folder= True )    
    plugintools.add_item(action="", thumbnail=thmb_nada,title="[COLOR gray]fichero Local--------------------------------------------------------------------------[/COLOR]",folder= False )
    plugintools.add_item(action="carga_servidores",    title="[COLOR skyblue]Lista Fichero Local[/COLOR]",extra='Local' ,thumbnail=thmb_carga_servidores,fanart="https://www.zooplus.es/magazine/wp-content/uploads/2018/04/fotolia_169457098.jpg",folder= True )
    plugintools.add_item(action="nuevo_server_file", extra="Local" , title="[COLOR springgreen]Nuevo servidor Fichero Local[/COLOR]",thumbnail=thmb_nuevo_servidor,folder= False )
    plugintools.add_item(action="", thumbnail=thmb_nada,title="[COLOR gray]fichero Internet-----------------------------------------------------------------------[/COLOR]",folder= False )
    plugintools.add_item(action="carga_servidores",    title="[COLOR skyblue]Lista (Fichero bajado Internet)[/COLOR]",extra='Internet' ,thumbnail=thmb_carga_servidores,fanart="https://www.zooplus.es/magazine/wp-content/uploads/2018/04/fotolia_169457098.jpg",folder= True )         
    plugintools.add_item(action="nuevo_server", title="[COLOR springgreen]Nuevo servidor Pastebin[/COLOR]",thumbnail=thmb_nuevo_servidor,folder= False )
    plugintools.add_item(action="guarda_servidores",    title="[COLOR crimson]Guardar Servidores desde Internet a Fichero[/COLOR]",extra='Internet' ,thumbnail=thmb_guarda_servidores,fanart="https://www.zooplus.es/magazine/wp-content/uploads/2018/04/fotolia_169457098.jpg",folder= False )     
    plugintools.add_item(action="", thumbnail=thmb_nada,title="[COLOR gray]-------------------------------------------------------------------------[/COLOR]",folder= False )
    plugintools.add_item(action="guiatv",url="https://www.formulatv.com/programacion/movistarplus/",title="[COLOR blue]Guia de TV[/COLOR] - (Gracias Javi R)", thumbnail=thmb_guia,fanart="http://www.panoramaaudiovisual.com/wp-content/uploads/2012/01/EPG-Toshiba-Smart-Tv-web.png",folder= True )     
    plugintools.add_item(action="", thumbnail=thmb_nada,title="[COLOR gray]-------------------------------------------------------------------------[/COLOR]",folder= False )

def ver_canales(params):
    
    if myaddon.getSetting('prx')=="true":
        px={"https:":"http://"+get_proxy()}  
    else:
        px=''
    
    thumbnail = params.get("thumbnail")
    
    mac=myaddon.getSetting('mac2')
    portal=myaddon.getSetting('portal2')
    escogido=myaddon.getSetting('escogido')
    s=''
    usuario = ''
  
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0","cookie": "mac="+mac+"; stb_lang=es; timezone=Europe/spain"}
    url=portal+'portal.php?type=stb&action=handshake&JsHttpRequest=1-xml'
        
    source=''
    
    try:
        source = requests.Session()
        if px=='':
            source=requests.get(url, headers=headers).content
        else:
            source=requests.get(url, headers=headers,proxies=px).content
            
    except:
    
        xbmc.executebuiltin('XBMC.Notification( e: No se puede conectar con SERVIDOR: ' + escogido +', Exception: '+portal+' '+mac+ ', 8000)')            
    
    if source =='':
        xbmc.executebuiltin('XBMC.Notification( s: No se puede conectar con SERVIDOR: ' + escogido +', Source nulo '+str(source)+ ', 8000)')  
        xbmc.log('ERROR conectando al servidor: '+str(source)+' : '+str(url))
        xbmc.executebuiltin('Action(Back)')
        #return(params)
    
    token=''
    try:
        token=re.findall('token":"(.*?)"', str(source) )[0] 
    except:       
        xbmc.executebuiltin('XBMC.Notification(No token: No se puede conectar con SERVIDOR: ' + escogido +', '+str(source)+ ', 8000)')  
        xbmc.log('ERROR conectando al servidor: '+str(source)+' : #'+str(url)+'#')
        xbmc.executebuiltin('Action(Back)')
        #return(params)
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0","cookie": "mac="+str(mac)+"; stb_lang=es; timezone=Europe/spain","Authorization": "Bearer "+token}
    url=portal+'portal.php?type=stb&action=get_profile&JsHttpRequest=1-xml'
    source=""
    
    usuario=''
    
    source = requests.Session()           
    if px=='':
        source=requests.get(url, headers=headers).content
    else:
        source=requests.get(url, headers=headers,proxies=px).content
    
    passs=''
    usuario=''
    typee=''
            
    payload={"login":usuario,"password":passs,"stb_type":typee}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0","cookie": "mac="+mac+"; stb_lang=es; timezone=Europe/spain","Authorization": "Bearer "+token}
    url=portal+'portal.php?type=itv&action=get_genres&JsHttpRequest=1-xml'
        
    source=''
    
    s = requests.Session()                
    #source=s.post(url, headers=headers,data=payload).text
    source=s.post(url, headers=headers,data=payload).content.decode('ascii','ignore')
    if source!='':
        
        data = plugintools.find_multiple_matches(source,'("id":"\d+.*?".*?"title":".*?",")')   
        pr0n=myaddon.getSetting('pr0n')  
        plugintools.add_item(title='[COLOR gray]-=========================-[/COLOR]',folder=False, isPlayable=False)   
        plugintools.add_item(action='cambio_mac',title='[COLOR orange]ACTUAL [ '+escogido+' # '+mac+' ][/COLOR]',folder=False, isPlayable=False)
        plugintools.add_item(title='[COLOR gray]-=========================-[/COLOR]',folder=False, isPlayable=False) 
        for generos in data: 
            
            patron=plugintools.find_single_match(generos,'"id":"(\d+.*?)".*?"title":"(.*?)"') 
            titulo=patron[1]
            ids=patron[0]
                        
            tit=colorea(titulo)
            
            if  not('adult' in titulo.lower() and pr0n=="false"):                            
                plugintools.add_item(action="paginar_canales", title=tit, thumbnail = params.get("thumbnail"), fanart= params.get("thumbnail"),plot=token,page=mac,extra=portal,url=ids,folder=True)                         
            
    else:
        xbmc.executebuiltin('XBMC.Notification([COLOR red]Problema '+str(s)+'[COLOR white]'+escogido+'[/COLOR],[COLOR white]'+portal+' '+mac+'[/COLOR], 10000)')            
        xbmc.executebuiltin('Action(Back)')
        xbmc.executebuiltin('Content.Refresh()')
        
def cambio_servidor(params):
    
    server2=myaddon.getSetting('ser')
    escogido=myaddon.getSetting('escogido')
    portal= myaddon.getSetting('portal2')
    mac= myaddon.getSetting('mac2')
    dialog = xbmcgui.Dialog()
    
    
    lists=myaddon.getSetting('lista').split(',')
    lista_servidores=myaddon.getSetting('lista_servidores').split(',')
    
    lista_servidores_2 = urllib2.urlopen(urllib2.Request("https://pastebin.com/raw/a38wUnQf")).read().split(',')
    
    lists=lists+lista_servidores_2
    lista_servidores=lista_servidores+lista_servidores_2
    
    retorno = dialog.select('[COLOR blue]Servidor ACTUAL: [/COLOR]'+str(escogido), lista_servidores)
        
        #if retorno<>-1:
        #xbmc.executebuiltin('XBMC.Notification(Lista,'+lista_servidores[retorno]+',8000)')
        
    dialog = xbmcgui.Dialog()    
        
    if str(retorno)!='-1':   
        server2=lists[retorno]
        escogido=lista_servidores[retorno]
        if 1==1: #try:     
            
            mac1 = str(urllib2.urlopen(urllib2.Request("https://pastebin.com/raw/"+server2)).read())
            xbmc.log(server2)
            xbmc.log(escogido)
            xbmc.log(mac1)
            mac=""
            mac=re.findall('(00:.*?79:.*?........)', mac1)            
            portal=re.findall('portal"(.*?)"', mac1.lower())[0]
            maclista=''
            random.seed()
            
            while maclista == '' or not maclista:
                maclista = random.choice(mac)
        
            mac=maclista                
            myaddon.setSetting('mac2',mac)
            myaddon.setSetting('portal2',portal)
            myaddon.setSetting('ser',server2)
            myaddon.setSetting('escogido',escogido)
        else:
        #except:
            xbmc.executebuiltin('XBMC.Notification( Error abriendo: ' + str(escogido) +', '+str(portal)+' '+str(mac)+ ', 8000)')               
            xbmc.executebuiltin('Action(Back)')        
    else:
        xbmc.executebuiltin('Action(Back)')        

    xbmc.executebuiltin('Content.refresh')
    ver_canales(params)        


def cambio_mac(params):
    
    try:
        server2 = myaddon.getSetting('ser')
        macant= myaddon.getSetting('mac2')
        escogido= myaddon.getSetting('escogido')
    except:
        server2='pfducjrm'
    if escogido=='Fichero_LOCAL':
        xbmc.executebuiltin('XBMC.Notification(Fichero Local, El fichero LOCAL funciona con MAC unica. Seleccionar otra linea de LOCAL si quieres cambiar de MAC , 8000)')                        
        xbmc.executebuiltin('Content.Refresh')
        xbmc.executebuiltin('Action(Back)')
    
    else:

        try:    
            mac1 = str(urllib2.urlopen(urllib2.Request("https://pastebin.com/raw/"+server2)).read())
            mac=""
            mac=re.findall('(00:.*?79:.*?........)', mac1)
            portal=re.findall('portal"(.*?)"', mac1.lower())[0]
            dialog = xbmcgui.Dialog()
            ret = dialog.select('[COLOR blue]ACTUAL MAC: [/COLOR][ '+str(escogido)+' # '+str(macant)+' ]', ['[COLOR red]CAMBIAR[/COLOR]', '[COLOR white]CONTINUAR CON [COLOR green]'+macant+'[/COLOR]'])
            lists = ['si','no']
    
            categorias= lists[ret]
                
            if 'si' in categorias:
                newmac=''
            
                selectable="[COLOR red]Prueba fortuna con una Random[/COLOR]"
                for mc in mac:                                    
                        selectable=selectable+','+str(mc)
                
                lista_macs=selectable.split(",")
                ret=dialog.select('[COLOR blue]Selecciona una MAC:[/COLOR]',lista_macs)

                if ret==1:
                    random.seed()
                    while newmac == '' or not newmac:
                        newmac = random.choice(mac)                      
                else:
                    if ret==-1:
                        newmac=macant
                    else:
                        newmac=mac[ret-1]

                if newmac!=macant:
                        myaddon.setSetting('mac2',newmac)
                        xbmc.executebuiltin('XBMC.Notification( Obtenida nueva MAC, ' +newmac+ ', 8000)')                        
    
        except:
                xbmc.executebuiltin('XBMC.Notification( Error obteniendo nueva MAC, Continuamos con' +macant+ ', 8000)')    
                xbmc.executebuiltin('Action(Back)')        

        xbmc.executebuiltin('Content.refresh')
        ver_canales(params)


def paginar_canales(params):
    
    ids = params.get("url")
    portal = params.get("extra")
    mac = params.get("page")
    token = params.get("plot")
    title=params.get('title')
    tit=title.replace('mintcream','blue')
    plugintools.add_item( title=tit, thumbnail = fanny, fanart=fanny ,folder=False,isPlayable=False )   
    for i in range(1,7):
        vpagina=str(i*10)
        pagina=str(i)
        plugintools.add_item(action="canal_por_pagina", title=" [COLOR white]Página: "+pagina+"[/COLOR]", thumbnail = vpagina, fanart=fanny ,plot=token,page=mac,extra=portal,url=ids,folder=True )   
    
    plugintools.add_item( action="todos_los_canales", title="[COLOR red]Listado Completo (puede tardar)[/COLOR]", thumbnail = vpagina, fanart=fanny ,plot=token,page=mac,extra=portal,url=ids,folder=True )   

def canal_por_pagina(params):
    
    
    if myaddon.getSetting('prx')=="true":
        px={"https:":"http://"+get_proxy()}  
    else:
        px=''
    
    vpagina = params.get("thumbnail")
    ids = params.get("url")
    portal = params.get("extra")
    mac = params.get("page")
    token = params.get("plot")
    headers = '{"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0","cookie": "mac="'+mac+'"; stb_lang=es; timezone=Europe/spain","Authorization": "Bearer "'+token+'}'
    
    #server = plugintools.find_single_match(portal,'http.*?//(.*?):.*?/') 
    #import socket    
    #servidor= socket.gethostbyname(server) 
    #portal=portal.replace(server,servidor)
    
    pn=int(vpagina)-9  
    count=int(vpagina);pn=pn;data=[]
    while pn <= int(count):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0","cookie": "mac="+mac+"; stb_lang=es; timezone=Europe/spain","Authorization": "Bearer "+token}
        if px=='':
            page=portal+'portal.php?type=itv&action=get_ordered_list&genre='+ids+'&force_ch_link_check=&fav=0&sortby=number&hd=0&p='+str(pn)+'&JsHttpRequest=1-xml';source=requests.get(page, headers=headers).content.decode('ascii','ignore')
        else:
            page=portal+'portal.php?type=itv&action=get_ordered_list&genre='+ids+'&force_ch_link_check=&fav=0&sortby=number&hd=0&p='+str(pn)+'&JsHttpRequest=1-xml';source=requests.get(page, headers=headers,proxies=px).content.decode('ascii','ignore')
        
        data +=re.findall('("id":".*?","name":".*?".*?"ch_id":".*?")',str(source));pn +=1
        
    url=data
    
    guardar_favs=myaddon.getSetting('favs')
    favoritos = xbmc.translatePath('special://home/userdata/favourites.xml')
    
    pr0n=myaddon.getSetting('pr0n')
    plugintools.add_item(title='[COLOR white]-_________________________-[/COLOR]',folder=False, isPlayable=False)   
    plugintools.add_item(action='cambio_mac',title='[COLOR orange]ACTUAL [ '+myaddon.getSetting('escogido')+' # '+mac+' ][/COLOR]',folder=False, isPlayable=False)   
    plugintools.add_item(title='[COLOR white]-_________________________-[/COLOR]',folder=False, isPlayable=False)   
    
    
    if guardar_favs=="true":
        try:			
            f = open(favoritos,'r')
            favoritoss = f.read()
            f.close()
        except:			
            f = open(favoritos,'w+')
            f.write('</favourites>')
            f.close()
            
    head='[COLOR red]Obteniendo lista de canales[/COLOR]'
    pb  = xbmcgui.DialogProgress()
    pb.create(head,'')   
    i=0
    for generos in url: 
        i=i+1
        patron = plugintools.find_single_match(generos,'"id":".*?","name":"(.*?)".*?"ch_id":"(.*?)"')
        canal=patron[1]
        titulo=patron[0]
        
        tit=colorea(titulo)
        pb.update(i,'Canal '+tit) 
        if  not('adult' in titulo.lower() and pr0n=="false"):    
            
                  
            plugintools.add_item(action="reproduce_canal",extra=portal,url=canal,page=mac,plot=params.get("plot"),title=tit, thumbnail = params.get("thumbnail"), fanart= fanny,folder=False,  isPlayable = True ) 
            
            if guardar_favs=="true":
                cmd='plugin://plugin.video.kepaiptv/?action=reproduce_canal'+'&title='+urllib.quote(titulo,safe='')+'&url='+str(canal)+'&thumbnail=10'+'&plot='+urllib.quote(token,safe='')+'&extra='+urllib.quote(portal,safe='')+'&page='+urllib.quote(mac,safe='')
                try:
                    if not canal in unicode(favoritoss, 'utf-8'):
                        favourite(titulo,'10',cmd)
                except:
                    pass
    pb.close()
    
def todos_los_canales(params):
    if myaddon.getSetting('prx')=="true":
        px={"https:":"http://"+get_proxy()}  
    else:
        px=''
    
    vpagina = params.get("thumbnail")
    ids = params.get("url")
    portal = params.get("extra")
    mac = params.get("page")
    token = params.get("plot")
    
    guardar_favs=myaddon.getSetting('favs')
    favoritos = xbmc.translatePath('special://home/userdata/favourites.xml')
    if guardar_favs=="true":
        try:
            f = open(favoritos,'r');favs = f.read();f.close()
        except:
            f = open(favoritos,'w+');f.write('</favourites>');f.close()
   
    pr0n=myaddon.getSetting('pr0n')
    plugintools.add_item(title='[COLOR gray]-=========================-[/COLOR]',folder=False, isPlayable=False)   
    plugintools.add_item(action='cambio_mac',title='[COLOR blue]ACTUAL [ '+myaddon.getSetting('escogido')+' ][/COLOR]',folder=False, isPlayable=False)   
    plugintools.add_item(title='[COLOR gray]-=========================-[/COLOR]',folder=False, isPlayable=False)   
    head='[COLOR red]Obteniendo lista de canales[/COLOR]'
    pb  = xbmcgui.DialogProgressBG()    
    pb.create(head,'')        
    progreso=0
      
    for i in range(1,5):
        vpagina=i*10
        pagina=str(i)
        
        headers = '{"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0","cookie": "mac="'+mac+'"; stb_lang=es; timezone=Europe/spain","Authorization": "Bearer "'+token+'}'
    
        pn=vpagina-9  
        count=i*10;pn=pn;data=[]
        while pn <= count:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0","cookie": "mac="+mac+"; stb_lang=es; timezone=Europe/spain","Authorization": "Bearer "+token}
            if px=='':
                page=portal+'portal.php?type=itv&action=get_ordered_list&genre='+ids+'&force_ch_link_check=&fav=0&sortby=number&hd=0&p='+str(pn)+'&JsHttpRequest=1-xml';source=requests.get(page, headers=headers).content.decode('ascii','ignore')
            else:    
                page=portal+'portal.php?type=itv&action=get_ordered_list&genre='+ids+'&force_ch_link_check=&fav=0&sortby=number&hd=0&p='+str(pn)+'&JsHttpRequest=1-xml';source=requests.get(page, headers=headers,proxies=px).content.decode('ascii','ignore')
            
            data +=re.findall('("id":".*?","name":".*?".*?"ch_id":".*?")',str(source));pn +=1

        url=data
        total=len(data)
        c=1 
        for generos in url: 
            
            patron = plugintools.find_single_match(generos,'"id":".*?","name":"(.*?)".*?"ch_id":"(.*?)"')
            canal=patron[1]
            titulo=patron[0]

            tit=colorea(titulo)

            if  not('adult' in titulo.lower() and pr0n=="false"):                                    
            
                plugintools.add_item(action="reproduce_canal",extra=portal,url=canal,page=mac,plot=params.get("plot"),title='Pag:'+str(i)+'-'+tit, thumbnail = params.get("thumbnail"), fanart= fanny,folder=False,  isPlayable = True )                                                 
                
                if guardar_favs=="true":
                    cmd='plugin://plugin.video.kepaiptv/?action=reproduce_canal'+'&title='+urllib.quote(titulo,safe='')+'&url='+str(canal)+'&thumbnail=10'+'&plot='+urllib.quote(token,safe='')+'&extra='+urllib.quote(portal,safe='')+'&page='+urllib.quote(mac,safe='')
                    try:
                        if not canal in unicode(favs, 'utf-8'):
                            favourite(titulo,'10',cmd)
                    except:
                        pass

            progreso=str(int(round((c/total)*100)))                
            pb.update(int(progreso),heading=head+' '+progreso+'%',message='Cargando canal '+tit+' de pagina '+str(i)+' '+str(c)+'/'+str(total))    
            c=c+1
                

    pb.close()

def colorea(titulo):

    if  'spain' in titulo.lower() or 'esp' in titulo.lower() or 'EU -ES' in titulo or 'spanish' in titulo.lower():               
        color='darkorange'                                             
    else:
        if 'crime' in titulo.lower():
            color='springgreen'
        else:
            if 'axn' in titulo.lower()  or 'accion' in titulo.lower() or 'estrenos'  in titulo.lower() or 'historia'  in titulo.lower() or 'odisea'  in titulo.lower() or 'discovery'  in titulo.lower():
                    color='deeppink'
            else:        
                if 'adult' in titulo.lower() or 'xxx' in titulo.lower() or 'porn' in titulo.lower():
                    color='red'
                else:
                    color='mintcream'
    
    return '[COLOR '+color+']'+titulo+'[/COLOR]'

def reproduce_canal(params):
    if myaddon.getSetting('prx')=="true":
        px={"https:":"http://"+get_proxy()}  
    else:
        px=''
    
    
    s=''
    canal = params.get("url")
    portal = params.get("extra")
    mac = params.get("page")
    token = params.get("plot")
   
    headers =headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0","cookie": "mac="+mac+"; stb_lang=es; timezone=Europe/spain","Authorization": "Bearer "+token}
    url=portal+'portal.php?type=itv&action=create_link&cmd=http://localhost/ch/'+canal+'_&series=&forced_storage=undefined&disable_ad=0&download=0&JsHttpRequest=1-xml'

    try:       
        if px=='':
            source=requests.get(url, headers=headers).text
        else:
            source=requests.get(url, headers=headers,proxies=px).text
        
        fuente=re.findall('"cmd":"ffmpeg (.*?)"',source )[0]
        fuente= fuente.replace("\\", "")
        
        url=fuente
    
        plugintools.play_resolved_url(url)
    except:
        xbmc.executebuiltin('XBMC.Notification(Error reproduciendo, ' +str(url)+ ', 8000)')            
     
    
def favourite(name,thumb,cmd):
    result = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "Favourites.AddFavourite", "params": {"title":"%s", "type":"media", "path":"%s", "thumbnail":"%s"}, "id": 1}' % (name, cmd, thumb))

def linkdirecto(params):
    url = params.get("url")    
    plugintools.play_resolved_url(url)      


def carga_servidores(params):
    donde=str(params.get('extra'))
    head='[COLOR red]Cargando lista de canales [/COLOR]'+str(donde)
    pb  = xbmcgui.DialogProgressBG()    
    pb.create(head,'')     
    
    fichero = xbmc.translatePath('special://home/userdata/addon_data/plugin.video.kepaiptv/'+donde+'_servers.dat')

    try:
        f=open(fichero,'r')        
        servidores=f.readlines()
        lineas=len(servidores)
    except:
        f=open(fichero,'w+')        
        f.close()
        f=open(fichero,'r')        
        servidores=f.readlines()
        lineas=len(servidores)
        xbmc.executebuiltin('XBMC.Notification([COLOR red]No existia fichero Origen[/COLOR] , fichero: '+str(donde)+', 8000)')          
        xbmc.executebuiltin('Action(Back)')
    i=1
    lista_nombres=''
    lista_macs=''
    selectable=''
    #colors=['red','green','orange','blue','pink','chocolate','darkorange','magenta']
    for servidor in servidores:
        try:      

            mac=re.findall('#(00:.*?79:.*?........)', servidor)            
            portal=re.findall('portal"(.*?)"', servidor.lower())
            if portal:
                
                pb.update(int(round(i/lineas)*100),head,str(servidor))
                  
                #color=random.choice(colors)
                if i % 2 == 0:
                    color='white'
                else:
                    color='red'    

                if lista_nombres=='':
                    lista_nombres=portal[0]
                    lista_macs=mac[0]
                    selectable='[COLOR '+color+']'+str(i)+'::'+portal[0]+'#'+mac[0]+'[/COLOR]'
                else:
                    lista_nombres=lista_nombres+','+portal[0]
                    lista_macs=lista_macs+','+mac[0]
                    selectable=selectable+',[COLOR '+color+']'+str(i)+'::'+portal[0]+'#'+mac[0]+'[/COLOR]'
                i+=1   
        except:
            xbmc.executebuiltin('XBMC.Notification([COLOR red]ERROR[/COLOR] obteniendo datos , SERVIDOR: '+str(servidor)+', 8000)')               
                           
    f.close()
    pb.close()
    
    dialog = xbmcgui.Dialog()    
    select_one=selectable.split(',')
    retorno = dialog.select('[COLOR blue]Selecciona PORTAL+MAC[/COLOR]', select_one)
    
    
    if str(retorno)=='-1':   
        xbmc.executebuiltin('Action(Back)')   
        #xbmc.executebuiltin('XBMC.Notification([COLOR red][/COLOR] obteniendo datos , SERVIDOR: '+str(server2)+', 8000)')                   
    else:
        l_n=lista_nombres.split(',')
        l_m=lista_macs.split(',')
        
        server2=str(l_n[retorno])
        mac2=str(l_m[retorno])
        
        myaddon.setSetting('mac2',mac2)
        myaddon.setSetting('portal2',server2)
        myaddon.setSetting('escogido','Fichero_LOCAL')
        myaddon.setSetting('ser',server2)
        
        # xbmc.executebuiltin('XBMC.Notification([COLOR red]Cancelo[/COLOR] Cancelado , No se ha escogido un servidor, 8000)')                   
    xbmc.executebuiltin('Content.refresh')    
    ver_canales(params)      
        

def guarda_servidores(params):
    donde=str(params.get('extra'))    
    head='[COLOR red]Guardando canales [/COLOR]'
    pb  = xbmcgui.DialogProgressBG()    
    pb.create(head,'') 
    lists=myaddon.getSetting('lista').split(',')
    lista_servidores_2 = urllib2.urlopen(urllib2.Request("https://pastebin.com/raw/a38wUnQf")).read().split(',')
    lists=lists+lista_servidores_2
    
    
    cuantos=len(lists)
    
    lista_servidores=myaddon.getSetting('lista_servidores').split(',')
    lista_servidores=lista_servidores+lista_servidores_2
    
    fichero = xbmc.translatePath('special://home/userdata/addon_data/plugin.video.kepaiptv/'+donde+'_servers.dat')        
    f=open(fichero,'w')            
    i=1
    for servidor in lists:
        try:      
            percent=str(int(round(100*i/cuantos)))
            # xbmc.executebuiltin('XBMC.Notification([COLOR red]Leyendo servidor[/COLOR] , SERVIDOR: '+str(servidor)+' '+str(i)+'/'+str(cuantos)+' '+percent+'%, 8000)')          
            mac1 = str(urllib2.urlopen(urllib2.Request("https://pastebin.com/raw/"+servidor)).read())
            
            pb.update(int(percent),head,str(percent)+'% '+str(lista_servidores[i]))
            macs=""
            macs=re.findall('(00:.*?79:.*?........)', mac1)            
            portal=re.findall('portal"(.*?)"', mac1.lower())[0]
            for mac in macs:
                f.write('portal"'+str(portal)+'"#'+str(mac)+'\n')
                
        except:
            # xbmc.executebuiltin('XBMC.Notification([COLOR red]ERROR[/COLOR] obteniendo datos , SERVIDOR: '+str(servidor)+', 8000)')               
            xbmc.log('Error obteniendo datos del SERVIDOR: '+str(servidor))
            pass
        i=i+1     
    f.close()
    pb.close()
    xbmc.executebuiltin('XBMC.Notification([COLOR red]Fichero de datos de '+donde+'[/COLOR] , Se ha guardado el fichero de datos de servidores en Local , 8000)')          
    
    xbmc.executebuiltin('Content.refresh')
    #xbmc.executebuiltin("Action(Back)")
    #main_list(params)

def nuevo_server(params):
   
    keyboard = xbmc.Keyboard("","Servidor Pastebin:")
    keyboard.doModal()
    if (keyboard.isConfirmed()):
        server = keyboard.getText()
        keyboard = xbmc.Keyboard("","Nombre Servidor:")
        keyboard.doModal()
        if (keyboard.isConfirmed()):        
            name= keyboard.getText()
            lista=myaddon.getSetting('lista')+','+str(server)
            myaddon.setSetting('lista',lista)
            myaddon.setSetting('lista_servidores',myaddon.getSetting('lista_servidores')+','+name)
            xbmc.executebuiltin('XBMC.Notification([COLOR red]Servidor PASTEBIN[/COLOR] , Se ha guardado el nuevo servidor de Pastebin, 8000)')          

def nuevo_server_file(params):
    donde = params.get('extra')
    fichero = xbmc.translatePath('special://home/userdata/addon_data/plugin.video.kepaiptv/'+donde+'_servers.dat')        
    keyboard = xbmc.Keyboard("","Servidor:")
    keyboard.doModal()
    if (keyboard.isConfirmed()):
        server = keyboard.getText()
        keyboard = xbmc.Keyboard("","Puerto:")
        keyboard.doModal()
        if (keyboard.isConfirmed()):        
            puerto=keyboard.getText()
            keyboard = xbmc.Keyboard("","MAC:")
            keyboard.doModal()
            if (keyboard.isConfirmed()):        
                mac= keyboard.getText()                
                f=open(fichero,'a')
                f.write('portal"'+server+':'+puerto+'/"'+'#'+mac+'\n')
                f.close()
                xbmc.executebuiltin('XBMC.Notification([COLOR red]Servidor FICHERO_LOCAL[/COLOR] , Se ha guardado el nuevo servidor en el fichero LOCAL de servidores, 8000)')

def guiatv ( params ):
    url = params.get("url")  
    
    header = [ ]
    header.append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    
    url = read_url.strip ( )    
    
    matches = re.findall(r'(?s)class="cadena">.*?<a href="([^"]+)" title="Programación ([^"]+)".*?|<div class="(ahora)">\s*(.*?)<.*?|<div class="luego">\s*<span class="date">(\d+:\d+)<\/span>\s*([^<]+)|<div class="mastarde">\s*<span class="date">(\d+:\d+)<\/span>\s*([^<]+)\s*|<span class="remain"><\/span>\s*<a class="mas" href="([^"]+)"><span>(Parrilla completa)<\/span',url)
    
    for url, channel, nowhour, now, laterhour, later, morelaterhour, morelater, url2, completed in matches:
        nowhour = "\x20" +nowhour
        if url:
            url = url
        else:
            if url2:
                url = url2    
        title = "[B][COLOR snow]" + channel + "[/COLOR][/B]\x20" +' -'+"[COLOR red]"+nowhour+"[/COLOR]" + "\x20" +"[I]"+now+' '+laterhour + "\x20" +later+ morelaterhour +' '+morelater + "[/I][B][COLOR orange]" + completed + "[/COLOR][/B]"
        if url:
            plugintools.add_item ( action = "parse_guiatv" , title = title, url = url, thumbnail=thmb_guia, fanart=fanart_guia, folder = True)
        else:
            plugintools.add_item ( action = "" , title = title, url = url, thumbnail=thmb_guia, fanart=fanart_guia, folder = False)

def parse_guiatv ( params ):
    
    url = params.get("url")  
    header = [ ]
    header . append ( [ "User-Agent" , "Mozilla/5.0 (Windows NT 10.0; rv:75.0) Gecko/20100101 Firefox/75.0" ] )
    read_url , read_header = plugintools . read_body_and_headers ( url , headers = header )
    url = read_url . strip ( )    
    matches = re.findall(r'{"@context":"[^"]+","@type":"Event","name":"(\d+:\d+ - [^"]+)","description":"([^"]+)"',url)
    for title, desc in matches: 
        plugintools . add_item ( action = "" , title = title.decode('utf-8'), url = url, thumbnail=thmb_guia, fanart=fanart_guia,folder = False)


def get_proxy():   
    #intento leer del fichero local el proxy
         #si existe el fichero, leo el proxy y lo preebo
              #si funciona, devuelvo el proxy
              #si no funciona, busco otro y pruebo hasta encontrar uno valido.

    #si no existe el fichero, lo creo y busco un proxy para guardarlo
    try:
        
        #fichero_local=open(local_file,'r')
        #my_proxy=fichero_local.read()
        #fichero_local.close()
        my_proxy=myaddon.getSetting('proxy')
        if test_proxy(my_proxy)==True:
            #xbmc.executebuiltin('Notification(Proxy test ok, [COLOR green]OK[/COLOR]: '+my_proxy+',10) ')
            return my_proxy
        else:
            #xbmc.executebuiltin('Notification(Proxy test ko, [COLOR red]KO[/COLOR]: '+my_proxy+',10) ')
            my_proxy=coge_proxy()
            return my_proxy    
    except:
        #xbmc.executebuiltin('Notification(Local file ko, [COLOR red]Buscando un nuevo proxy[/COLOR]: ,1000) ')
        my_proxy=coge_proxy()
        return my_proxy    
 
def guarda_proxy(my_proxy):       
        #fichero_local=open(local_file,'w+')
        #fichero_local.write(my_proxy)
        #fichero_local.close()
        myaddon.setSetting('proxy',my_proxy)
        #xbmc.executebuiltin('Notification(Proxy saved ok, [COLOR green]Guardado en local [/COLOR]: '+my_proxy+',500) ')
        #print("Guardo Fichero "+str(my_proxy))

def coge_proxy():
    #print("Buscando proxy")
    #Leo desde proxyscape la lista diaria de proxys gratis
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3","Upgrade-Insecure-Requests": "1"} 
    lista_proxys='https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all' 
    de = requests.get(lista_proxys,headers=headers).text
    #Cojo todos los proxys del listado con expresion regular, lo guardo en el array lista_proxyes
    lista_proxyes= re.findall('(\d+.*?:\d+).*?\n',de)   
    
    #miro a ver cuantos proxys se ha traido en la lista
    numero_proxyes = len(lista_proxyes)
    #print("hay "+str(numero_proxyes)+" para probar")
    #Inicializo el contador de intentos a 1
    numero_intentos=1
    
    #inicializo el valor del proxy a devolver a nulo
    mi_proxy=''
    head='[COLOR red]Buscando Proxy[/COLOR]'
    pb  = xbmcgui.DialogProgressBG()    
    pb.create(head,'') 
    max_intentos=round((numero_proxyes-1)/10)
    #Realizo un bucle de intentos, hasta que haya probado con todos, o haya encontrado uno valido 
    while numero_intentos < max_intentos:    
        de='-'    
        my_proxy=random.choice(lista_proxyes)
        if test_proxy(my_proxy)==False:          
            numero_intentos=numero_intentos+1    
            msg="Intento "+str(numero_intentos)+" de "+str(max_intentos)+ " ("+str(my_proxy)+")"
            percent=int(numero_intentos/max_intentos*100)
            pb.update(percent,head,str(percent)+'% '+msg)                        
            #xbmc.executebuiltin('Notification(Buscando proxy,'+msg+',2000)')
        else:
            guarda_proxy(my_proxy)
            break
    
    pb.close()    
    return my_proxy

def test_proxy(my_proxy):
    
    url = 'https://cuevana3.io/'        
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3","Upgrade-Insecure-Requests": "1"} 
    test_proxy = {"https": "http://"+my_proxy}               
    try:
        de = requests.get(url, proxies=test_proxy, headers=headers,timeout=7).text            
        #Si ha encontrado el texto "cuevana" dentro del cuerpo html de la pagina, es que el proxy ha funcionado
        #porque ha conseguido traerse la pagina
        if 'cuevana' in de:                            
        
            return True
        else:
             
            return False           
    except:
        
        # test_proxy = {"http": "http://"+my_proxy}               
        
        # try:
        #     de = requests.get(url, proxies=test_proxy, headers=headers,timeout=8).text            
        #     #Si ha encontrado el texto "cuevana" dentro del cuerpo html de la pagina, es que el proxy ha funcionado
        #     #porque ha conseguido traerse la pagina
        #     if 'cuevana' in de:                                
        
        #         return True
        #     else:           
        #         return False
        # except:
        
        return False

run()
