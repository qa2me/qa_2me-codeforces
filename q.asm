include irvine32.inc

.data
list dword 10 dup(0)
maxi dword 0
mini dword 1000000
.code

main PROC
	call readint 
	mov ecx,eax
	mov esi,0
	loopi:
		call readint
		mov list[esi],eax
		cmp eax,maxi
		jg foundbig
		cmp eax,mini
		jl foundsmaller
		reloop:
			loop loopi
			
			mov eax,maxi
			call writeint
			call crlf
			mov eax ,mini
			call writeint 
			call crlf
			ret
		foundbig:
			mov maxi,eax
			jmp reloop
		foundsmaller:
			mov mini ,eax
			jmp reloop
	
	
main ENDP

end main