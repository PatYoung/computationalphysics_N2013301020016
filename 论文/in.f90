PROGRAM integral
REAL :: a,b,h,f,g,s,starttime,endtime
INTEGER i,n,clock
WRITE(*,*) "Input boundary a ->"
READ(*,*) a
WRITE(*,*) "Input boundary b ->"
READ(*,*) b
WRITE(*,*) "How many parts will it be divided? n ->"
READ(*,*) n
h = (b-a)/n
g = 0
CALL SYSTEM_CLOCK(COUNT = clock)
starttime = clock
DO i=1,(n-1),1
    f = sin(a+i*h)+(a+i*h)**2
    g = g+f
END DO
CALL SYSTEM_CLOCK(COUNT = clock)	
endtime = clock
s = (h/2)*(sin(a)+sin(b)+a**2+b**2+2*g)
WRITE(*,100) "s =",s
100 FORMAT(1X,A3,F10.7)
WRITE(*,200) "Time = ",endtime - starttime,"ms"
200 FORMAT(1X,A7,F5.1,A2)
END PROGRAM
