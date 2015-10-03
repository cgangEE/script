#!/usr/bin/expect
set timeout 60
spawn /usr/bin/ssh -vN -p 12342 boa@208.110.83.242 -D 127.0.0.1:7070


expect {
	"password:" {
		send "eyo3\r"
	}
}
interact {
	timeout  60{ send " "}
}
