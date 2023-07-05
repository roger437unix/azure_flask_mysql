#!/bin/bash

clear

docker rm banco --force > /dev/null 2>&1

docker run -d --rm --name banco \
-v $(pwd)/banco/database:/var/lib/mysql \
-p 3306:3306 \
-e MYSQL_ROOT_PASSWORD=mysql \
-e MYSQL_DATABASE=banco \
-e MYSQL_USER=tux \
-e MYSQL_PASSWORD=Mud@r123 \
mysql --default-authentication-plugin=mysql_native_password

echo
echo "Digite a senha do usuário Root do Banco ==> mysql"
mysql -uroot -p -h 127.0.0.1 < banco/scrip-mysql.sql
