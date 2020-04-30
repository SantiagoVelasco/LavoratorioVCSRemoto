package main

import "fmt"

func main() {
	familia := map[string][]int{
		"JuanF":{126,131,123,120} , "Amparo":{151,130}, "Antonio":{110}, "MariaJ":{98,122,115},
		"LisaF":{123,130},"Leonardo":{121,133}, "JavierC":{121,133},"SantiagoA":{123,115},
	}
	miFa := []string{"JuanF","Amparo","Antonio","MariaJ","LisaF","Leonardo","JavierC","SantiagoA"}
	nombre_menos := miFa[0]
	nombre_mas := miFa[0]
	menor := len(familia[nombre_menos])
	mayor := len(familia[nombre_mas])
	for i:= 0; i<len(familia); i++{
		if menor > len(familia[miFa[i]]){
			menor = len(familia[miFa[i]])
			nombre_menos = miFa[i]
		}
		if mayor < len(familia[miFa[i]]){
			mayor = len(familia[miFa[i]])
			nombre_mas = miFa[i]
		}
	}
	fmt.Printf("El miembro de la familia que se ha realizado más exámenes de diabetes es: %s con %d exámenes", nombre_mas, mayor)
	fmt.Printf("\nEl miembro de la familia que se ha realizado menos exámenes de diabetes es: %s con %d exámenes\n", nombre_menos, menor)
	contador := 0
	for llave := range familia{
		suma := 0.0
		for i := 0; i<len(familia[llave]); i++{
			suma = suma + float64(familia[llave][i])
		}
		promedio := suma/float64(len(familia[llave]))
		if promedio > 126{
			contador += 1
			fmt.Printf("\n%s presenta diabetes", llave)
		}
	}
	fmt.Printf("\nEl número de personas que presentan diabetes de la familia es: %d\n", contador)
	for llave := range familia{
		suma := 0.0
		for i := 0; i<len(familia[llave]); i++{
			suma = suma + float64(familia[llave][i])
		}
		promedio := suma/float64(len(familia[llave]))
		if (promedio <= 125)&&(promedio >= 110){
			fmt.Printf("\n%s presenta prediabetes", llave)
		}
	}
}