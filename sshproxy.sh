#!/usr/bin/expect
set timeout 60
spawn /usr/bin/ssh -vN  -p 22 tb3974264@106.186.123.46 -D 127.0.0.1:7070


expect {
	"password:" {
		send "508669\r"
	}
}
interact {
	timeout  60{ send " "}
}
