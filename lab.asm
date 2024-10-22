INCLUDE Irvine32.inc

.data
    promptN db "Enter the number of integers to sum: ", 0
    promptNum db "Enter an integer: ", 0
    sumMsg db "The sum of the numbers is: ", 0


.code
main PROC
    mov ebx,0
    mov edx, OFFSET promptN 
    call WriteString
	
    
    call ReadDec
    mov ecx, eax   
	qais:
		mov edx, OFFSET promptNum 
		call WriteString
		
		call ReadInt
		add ebx,eax
		
		
		loop qais
    mov edx, OFFSET sumMsg
	call WriteString
	mov eax,ebx
	call WriteInt
	
    exit
main ENDP
END main
