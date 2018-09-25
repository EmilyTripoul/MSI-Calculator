import os
import subprocess

javaexec="java" 
javaoption ="-cp"
javacup="/usr/share/java/cup.jar:."
javaClass="Parser"

def addTest(expr, result):
    
    #os.system("java -cp /usr/share/java/cup.jar:. Parser 5")
    resultexpr=subprocess.check_output([javaexec, javaoption, javacup, javaClass, expr]).decode('utf-8')
    
    cleanResult=resultexpr.split('\n')
    if(len(cleanResult)>2):
        print(cleanResult)
    if(cleanResult[-2][2:]==result):
        print('Test OK : %s = %s'%(expr, result))
    else:
        print('Test Failed : %s != %s (%s)'%(expr, result, cleanResult))

if __name__=="__main__":
    addTest("5;", '5.0')
    addTest("5+2;", '7.0')
    addTest("31.2E-2;", '0.312')
    addTest("5*(4+2);", '30.0')
    addTest("5+4*2;", '13.0')
    addTest("5+(-4)*2;", '-3.0')
    addTest("5+sin(-4)*2;", '6.513604990615857')
    addTest("a=5;", '6.513604990615857')
    pass