Create a key

	openssl genrsa -aes256 -out server.key 2048

Create the request

	openssl req -sha256 -subj "/C=GB/ST=State/L=City/O=Company/OU=IT Security Team/CN=*.vbox.dev" -new -key server.key -out server.csr

Copy the key and remove the password

	cp server.key server.key.org
	openssl rsa -in server.key.org -out server.key

Sign the request

	openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt

As one command

	openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -sha256 -subj "/C=GB/ST=State/L=City/O=Company/OU=IT Security Team/CN=*.vbox.dev" -keyout server.key -out server.crt
