docker run -d --restart unless-stopped --name openldap -p 389:389 -v ldap-vol:/app -e DOMAIN="asksunny.com"  -e ORGANIZATION="Ask Sunny Corp" -e PASSWORD="ert456"  mwaeckerlin/openldap

docker run -d --restart unless-stopped -p 7171:80  --name lam --volumes-from lam-volume  --link openldap:ldap  mwaeckerlin/lam
user default password "lam" to change server setting/profile
change security to cn=admin
