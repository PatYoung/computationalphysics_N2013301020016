SUBROUTINE init_random_seed()
    INTEGER :: i, n, clock
    INTEGER, ALLOCATABLE :: seed(:)
    CALL RANDOM_SEED(size = n)
    ALLOCATE(seed(n))
    CALL SYSTEM_CLOCK(COUNT = clock)
    seed = clock + 37 * (/(i - 1, i = 1, n)/)
    CALL RANDOM_SEED(put = seed)
    DEALLOCATE(seed)
END SUBROUTINE init_random_seed

PROGRAM main
    IMPLICIT NONE
    REAL :: a,b,c,d,f,r,m,s,l
    REAL :: pi,starttime,endtime
    INTEGER :: i,j,n,z,clock
    CALL init_random_seed()
    WRITE(*,*) "n ->(n < 10000000)"
    READ(*,*) n
    m = 0.0
    CALL SYSTEM_CLOCK(COUNT = clock)	
	starttime = clock
    DO i = 1,n,1
        CALL RANDOM_NUMBER(a)
        CALL RANDOM_NUMBER(b)
       	c = -2 + 4 * a
		d = -1 + 6 * b
		f = c ** 2 + sin(c)
        IF (f > 0) THEN
		IF (d > 0) THEN
			IF (d < f) THEN
				m = m + 1
			END IF
		END IF
        END IF
        IF (f < 0) THEN
		IF (d < 0) THEN
			IF (d > f) THEN
				m = m - 1
			END IF
		END IF
        END IF		
		
        pi = m / i * 24
        IF (i == n/10000) THEN
            WRITE(*,"(A8,I9,A5,F9.6)") "When i =",n/10000,"pi =",pi
        END IF
        IF (i == n/1000) THEN
            WRITE(*,"(A8,I9,A5,F9.6)") "When i =",n/1000,"pi =",pi
        END IF
        IF (i == n/100) THEN
            WRITE(*,"(A8,I9,A5,F9.6)") "When i =",n/100,"pi =",pi
        END IF
        IF (i == n/10) THEN
            WRITE(*,"(A8,I9,A5,F9.6)") "When i =",n/10,"pi =",pi
        END IF 
        IF (i == n) THEN
            WRITE(*,"(A8,I9,A5,F9.6)") "When i =",n,"pi =",pi
        END IF
    END DO
	CALL SYSTEM_CLOCK(COUNT = clock)	
	endtime = clock
	WRITE(*,100) "Time = ",endtime-starttime,"ms"
100 FORMAT(1X,A7,F5.1,A2)
	
END PROGRAM
