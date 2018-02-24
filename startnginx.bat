cd /d D:\nginx-1.13.7\nginx-1.13.7

start nginx.exe
pause 


REM nginx -s stop 	fast shutdown
REM nginx -s quit 	graceful shutdown
REM nginx -s reload 	changing configuration, starting new worker processes with a new configuration, graceful shutdown of old worker processes
REM nginx -s reopen 	re-opening log files