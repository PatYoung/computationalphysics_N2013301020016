PROGRAM integral
REAL(KIND=8) :: a,b,h,f,g,s,starttime,endtime
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
    f = 1 / (1 +(a+i*h)**2)
    g = g+f
END DO
CALL SYSTEM_CLOCK(COUNT = clock)	
endtime = clock
s = 4*(h/2)*(1/(1+a**2)+1/(1+b**2)+2*g)
WRITE(*,100) "s =",s
100 FORMAT(1X,A3,F20.17)
WRITE(*,200) "Time = ",endtime - starttime,"ms"
200 FORMAT(1X,A7,F7.1,A2)
END PROGRAM
