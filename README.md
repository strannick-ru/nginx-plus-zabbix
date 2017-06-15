Nginx Plus позволяет получить текущий статус в виде [файла в формате JSON].
Информация, выдаваемая этим json-файлом, делится на два типа:

1. касающаяся сервера в целом
2. касающаяся upstreams

Если о состоянии сервера в целом вопросов не возникает, то с апстримами несколько сложнее.
Поскольку количество апстримов и их пиров заранее неизвестно, имеет смысл определять их динамически с помощью низкоуровневых [запросов заббикса (LLD)].

Для разбора json из Nginx используется скрипт **nginx-stats.py**
Для того, чтобы выяснить, сколько апстримов и пиров есть у сервера, используется скрипт автообнаружения **nginx-discovery.py**

Чтобы мониторинг заработал, нужно сделать следующее:

1.  разместить скрипты в /etc/zabbix/scripts/
2.  добавить UserParameter в zabbix-agent
```echo 'UserParameter=nginx.stat.[*],/etc/zabbix/scripts/nginx-stats.py $1 $2 $3 $4 $5 $6' > /etc/zabbix/zabbix_agentd.d/userparameter_nginx_plus.conf
echo 'UserParameter=nginx.discovery,/etc/zabbix/scripts/nginx-discovery.py' >> /etc/zabbix/zabbix_agentd.d/userparameter_nginx_plus.conf```
3.  перезапустить zabbix-agent
4.  импортировать шаблон Zabbix
5.  присоединить шаблон Template App Nginx Plus к узлу сети
6.  проверить наличие свежих данных

![] ![][1] На этом настройка мониторинга для Nginx Plus завершена.

  [файла в формате JSON]: http://demo.nginx.com/status
  [запросов заббикса (LLD)]: https://www.zabbix.com/documentation/3.2/ru/manual/discovery/low_level_discovery
  []: https://habrastorage.org/web/906/566/cb5/906566cb546c43c289fb8c408bb58706.png
  [1]: https://habrastorage.org/web/a90/7e4/b3b/a907e4b3b4994a14b0bb51f6467bc034.png
