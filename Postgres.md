
#### Default data directory for a local postgres DB
<pre>
/var/lib/postgresql/VERSION/main
</pre>
#### Default installation of Postgres on Ubuntu
<pre>
/usr/lib/postgresql/VERSION/bin
</pre>
#### Default location of conf file 
<pre>  
/etc/postgresql/VERSION/main/postgresql.conf
</pre>

#### Default location of hba conf file
This is the file used for authentication.
USe trust instead of md5 to reset postgres password, google instructions

<pre>
/etc/postgresql/VERSION/main/pg_hba.conf
</pre>

#### Start stop restart DB

<pre>
  pg_ctlcluster 12 main start
</pre>
