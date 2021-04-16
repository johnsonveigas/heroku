
def ImgId():
    
    
	
    f=open("data.txt","rt")

    content=f.read()
    initial_value=int(content)
    
    
    
    sum=initial_value+1
    
    
    content=content.replace(content,str(sum))
    f.close()

    f=open("data.txt","wt")

    f.write(content)
    
    

    f.close()
    
    return str(initial_value)
    
    
if __name__=="__main__":
	ImgId()