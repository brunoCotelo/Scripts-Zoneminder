#!/bin/bash

#Comando para atualizar o sistema.
apt-get update
#Comando para instalar o banco de dados.
apt -y install mysql-server
#Instalar Tasksel e Lamp-server.
apt-get -y install tasksel
tasksel install lamp-server
#Instalar repositorio do ZM.
add-apt-repository -y ppa:iconnor/zoneminder-1.34 
#Configuracao do MySQL.
rm /etc/mysql/my.cnf
cp /etc/mysql/mysql.conf.d/mysqld.cnf /etc/mysql/my.cnf
#Comando para adicionar o sql_mode.
echo "sql_mode = NO_ENGINE_SUBSTITUTION" >> /etc/mysql/my.cnf
#Reiniciar o MySQL.
systemctl restart mysql
#Instalar o ZM.
apt-get -y install zoneminder
#Configurar o ZM com os comandos do MySQL. Substitua o 'SuaSenha' pela senha do seu usuario root
mysql -uroot -p'SuaSenha' < /usr/share/zoneminder/db/zm_create.sql
mysql -uroot -p'SuaSenha' -e "grant lock tables,alter,drop,select,insert,update,delete,create,
index,alter routine,create routine, trigger,execute on zm.* to 
'zmuser'@localhost identified by 'zmpass';"
#Atribuindo as permissoes.
chmod 740 /etc/zm/zm.conf
chown root:www-data /etc/zm/zm.conf
chown -R www-data:www-data /usr/share/zoneminder/
#Configurar Apache.
a2enmod cgi
a2enmod rewrite
a2enconf zoneminder
#Comando para melhorar o desempenho do cache.
a2enmod expires
a2enmod headers
#Habilitar e iniciar o ZM.
systemctl enable zoneminder
systemctl start zoneminder
#Editar a timezone.
sed -i 's+;date.timezone =+date.timezone = America/Sao_Paulo+g' /etc/php/7.2/apache2/php.ini 
#Reiniciar o Apache.
systemctl reload apache2
