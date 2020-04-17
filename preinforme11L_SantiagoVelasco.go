package main



import (

	"fmt"

)

func famili()([4][8]string){

	fami := [4][8]string {{"Juan","Amparao","Antonio","Maria","Lisa","Leonardo","Javier","Santiago"},

		{"M","F","M","F","F","M","M","M"},

		{"SI","SI","SI","NO","NO","SI","NO","SI"},

		{"1","2","1","NA","NA","1","NA","1"}}

	return fami

}

func contiene(){

	fa := famili()

	c := 0

	f := len(fa[0])

	for p := 0; p < f ; p++ {

		co := fa[2][p]

		if co == "SI" {

			c = c + 1

			fmt.Println(fa[0][p]," Salio positivo para diabestes de tipo ",fa[3][p])

		}

	}

	fmt.Println("El numero de personas con diabetes en la familia es ", c )

}

func genero(){

	fa := famili()

	f := len(fa[0])

	CM := 0

	CF := 0

	for p := 0 ; p < f ; p++ {

		co := fa[2][p]

		if co == "SI" {

			g := fa[1][p]

			if g == "M" {

				CM = CM + 1

			} else {

				CF = CF + 1

			}

		}

	}

	if CM == CF {

		fmt.Println("Los dos generos son iguales de propensos")

	} else {

		if CF < CM {

			fmt.Println("Es más propenso el género masculino a contraer la enfermedad")

		} else {

			fmt.Println("Es más propenso el género femenino a contraer la enfermedad")

		}

	}

}

func tipo(){

	fa := famili()

	f := len(fa[0])

	T1 := 0

	T2 := 0

	for p := 0 ; p < f ; p++ {

		co := fa[2][p]

		if co == "SI" {

			g := fa[3][p]

			if g == "1" {

				T1 = T1 + 1

			} else {

				T2 = T2 + 1

			}

		}

	}

	fmt.Print("El numero de casos de diabetes en la familia de tipo 1 es ",T1, "\n")

	fmt.Print("El numero de casos de diabetes en la familia de tipo 2 es ",T2, "\n")

	if T1 == T2 {

		fmt.Println("Los dos tipos son iguales de propensos")

	} else {

		if T2 < T1 {

			fmt.Println("Es más propenso el tipo 1 de diabetes en la familia")

		} else {

			fmt.Println("Es más propenso el tipo 1 de diabetes en la familia")

		}

	}

}

func main() {

	fa := famili()

	fmt.Println(fa)

	contiene()

	genero()

	tipo()

}