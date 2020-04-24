package main

import (
	"fmt"
	"math/rand"
	"time"
)

func generador(a, b int) [4][12]int {
	rand.Seed(time.Now().UnixNano())
	var v [4][12]int
	for i := 0; i < 4; i++ {
		for p := 0; p < 12; p++ {
			v[i][p] = rand.Intn(b-a) + a
		}
	}
	return v
}
func imprimir(a [4][12]int) {
	mes := [2]string{"            ", "Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic"}
	Ciudad := [4]string{"Bucaramanga ", "Floridablanca", "Giròn        ", "Piedecuesta  "}
	f := len(Ciudad)
	for p := 0; p < f; p++ {
		fmt.Println(mes)
		fmt.Println(Ciudad[p], a[p])
	}
}
func restador(a [4][12]int, b [4][12]int) [4][12]int {
	var re [4][12]int
	for r := 0; r < 4; r++ {
		for p := 0; p < 12; p++ {
			re[r][p] = a[r][p] - b[r][p]
		}

	}
	return re
}
func generador3D(ingresos[4][12]int,egresos[4][12]int)(ingresos3D[4][4][12]int,egresos3D[4][4][12]int){
	a := [4]int{90,81,74,67}
	b := [4]int{162,147,133,120}
	for p := 0 ; p<4 ;p++{
		for r :=0 ;r<4;r++{
			for t :=0 ;t<12;t++{
				o := b[p]
				i := a[p]
				ingresos3D[p][r][t] = rand.Intn(o-i) + i
			}
		}
	}
	c := [4]int{56,53,50,47}
	d :=[4]int{122,115,109,103}
	for g:= 0 ; g<4 ; g++{
		for h:=0 ;h<4;h++{
			for j :=0 ;j<12;j++{
				egresos3D[g][h][j] = rand.Intn(d[g]-c[g]) + c[g]
			}
		}
	}
	return egresos3D,ingresos3D
}
func imprimir3D (b[4][12]int,a[4][4][12]int,c string)(){
	d := 2019
	fmt.Print(c , "del año ",d , "\n")
	imprimir(b)
	for y:=0 ; y<4 ; y++ {
		d = d-1
		fmt.Print(c , "del año ",d , "\n")
		f := a[y]
		imprimir(f)
	}
}
func calcula_ganancias(ingresos3D[4][4][12]int,egresos3D[4][4][12]int)(ganancias3D[4][4][12]int){
	for r :=0;r<4;r++{
	g := ingresos3D[r]
	h := egresos3D[r]
	ganancias3D[r] = restador(g,h)
	}
	return ganancias3D
}
func main() {
	ingresos := generador(100, 180)
	fmt.Print("Ingresos \n")
	imprimir(ingresos)
	egresos := generador(60, 130)
	fmt.Print("egresos \n")
	imprimir(egresos)
	ganancias := restador(ingresos, egresos)
	fmt.Print("Ganacias \n")
	imprimir(ganancias)
	Ingresos3D,egresos3D:=generador3D(ingresos,egresos)
	imprimir3D(ingresos,Ingresos3D,"Los ingresos ")
	imprimir3D(egresos,egresos3D,"Los egresos ")
	ganancias3D := calcula_ganancias(Ingresos3D,egresos3D)
	imprimir3D(ganancias,ganancias3D,"Las ganacias ")
}
