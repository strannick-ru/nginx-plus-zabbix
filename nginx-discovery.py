#! /usr/bin/python2
# -*- coding: utf-8 -*-
# parse json from nginx again
# we need to make /another/ json for zabbix
# warning: this script not send any values to Zabbiz, only upstreams and peers names.
# this script doing just one thing - make json for zabbix with right format
# unfortunately, json.dumps gives a slightly different format

import json, re, urllib

# parse json from nginx to dict data
url="http://demo.nginx.com/status"
response = urllib.urlopen(url)
data = json.loads(response.read())

# forming json for LLD zabbix where {#UPSTREAM} - upstream's name
# {#NODE_IP} - peer's IP address

result="{\n\"data\":[\n"
for i in sorted(data['upstreams'].keys()):
        ip_data = dict([[v['server'],v] for v in data['upstreams'][i]['peers']])
        for j in sorted(ip_data.keys()):
                result = result + "{\n"
                result = result + "\"{#UPSTREAM}\":\""+str(i)+"\",\n"
                result = result + "\"{#NODE_IP}\":\""+str(j)+"\"\n"
                result = result + "},\n"

result = re.sub("},\n$", "", result) + "}]\n}\n"
print result
