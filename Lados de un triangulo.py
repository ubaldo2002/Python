perimetro=0
op=int(input("\n1-Equilatero \n2-Isosceles \n3-Escaleno "+
             "\nIngrese la opcion deseada: "))
a=int(input("Digite un lado: "))
b=int(input("Digite un lado: "))
c=int(input("Digite un lado: "))

if a<(b+c) and b<(a+c) and c<(a+b):
  if a==b and b==c:
   print("Triángulo equilátero")
    
  else:
    if( (a!=b) and (a!=c) and (b!=c)):
       print("Triángulo escaleno")
    else:
       print("Triángulo isosceles")
else:
 print("Lo ingresado no son medidas de un triángulo")

perimetro=a+b+c

print("El perímetro del trangulos es: ", str(perimetro))
