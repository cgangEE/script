#!/usr/bin/expect
set timeout 6000
spawn /usr/bin/ssh -N  -D 7070 -p 1399 boa@23.95.57.193
expect {
	"password:" {
		send "eyo3\r"
	}
}
interact {
	timeout 6000 { send " "}
}
