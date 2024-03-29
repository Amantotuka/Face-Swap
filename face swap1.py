import cv2
v=cv2.VideoCapture(0)
fd=cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
while(1):
    r,i=v.read()
    j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    f=fd.detectMultiScale(j,1.1,5)
    if(len(f)==2):
        fx1=f[0][0]
        fy1=f[0][1]
        fw1=f[0][2]
        fh1=f[0][3]
        fx2=f[1][0]
        
        fy2=f[1][1]
        fw2=f[1][2]
        fh2=f[1][3]
        fc1=i[fy1:fy1+fw1,fx1:fx1+fh1]
        fc2=i[fy2:fy2+fw2,fx2:fx2+fh2]
        fcc1=fc1.copy()
        fcc2=fc2.copy()
        

        fccc1=cv2.resize(fcc1,(fw2,fh2))
        fccc2=cv2.resize(fcc2,(fw1,fh1))


        i[fy1:fy1+fccc2.shape[1],fx1:fx1+fccc2.shape[0],:]=fccc2
        i[fy2:fy2+fccc1.shape[1],fx2:fx2+fccc1.shape[0],:]=fccc1
        #cv2.imshow('orignal',fc1)
    cv2.imshow('swapped img',i)

    k=cv2.waitKey(5)
    if (k==ord('q')):
       cv2.destroyAllWindows()
       break
        
        
    
