# combpartpy
I plan to combine the main Python program written in an appropriate split
------------------------------------------
### info
I haven't looked at it in detail, so I may have misunderstood, but  
I found a tool for a similar purpose that looks very functional and excellent, so I will describe it 😙  
https://github.com/yamenk-gribaudo/pymerger  

I will return to the description of my program  
### Usage  
rename your separated main program files   
*****.part0~99.py  
put this combpartpy.py same directory and run  
this program create combined copy those files in one and run the program.  
part0 is basefile,[from] and [import] contents of other files are not copied  

note  
It's not a well-designed program,  
so if you're unlucky, it may break unexpectedly :o  


Cases where comments are made into multiple lines by line breaks  
If there is a 'from' or 'import' at the beginning of the line,  
it is difficult and it is not handled well.  
It's like being in the ohmain.part2.py of sample
