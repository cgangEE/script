#!/usr/bin/expect
set timeout 60
spawn /usr/bin/ssh -D 7070 54c7316ffcf933bba900007a@www.sharingbook.cn


expect {
	"password:" {
		send "508669\r"
	}
}
interact {
	timeout  60{ send " "}
}
