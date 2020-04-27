package main

import (
	"fmt"
	"math"
	"sort"
)
func promedio()[]float64{
	presion_prome := [] float64{110.06, 107.89, 108.45,108.49,
		109.03,110.11,109.87,119.38,119.35,
		116.34,117.73,120.01,118.19,119.53,117.09,
		118.03,118.65,117.47,117.49,109.65,110.44,110.51,107.38,
		109.26,106.18,109.36,106.61,105.16,110.11,105.48,108.37,
		107.59,108.91,108.35,109.57,122.56,124.44,125.97,121.03,
		121.22,122.41,122.15,124.52,123.35,125.76,121.08,122.29,105.42, 110.67,107.73,105.76,107.85}
	return presion_prome
}

func diferencia(presion_prome[]float64)float64{
	long :=len(presion_prome)
	mayor := presion_prome[0]
	menor := presion_prome[0]
	for i := 0; i<long; i++{
		if mayor < presion_prome[i]{
			mayor = presion_prome[i]
		}
		if menor > presion_prome[i]{
			menor = presion_prome[i]
		}
	}
	diferen := mayor - menor
	return diferen
}

func media(presion_prome[]float64)float64{
	long := len(presion_prome)
	var suma float64
	suma = 0
	for i:=0; i<long; i++{
		suma = suma + presion_prome[i]
	}
	prome := suma/52
	return prome
}

func mediana(presion_prome[]float64)float64{
	copia := presion_prome
	sort.Float64s(copia)
	median := (copia[20] + copia[21])/2
	return median
}

func supera_debajo(presion_prome[]float64, prome float64)([]float64, []float64){
	arriba := []float64 {}
	abajo := []float64 {}
	for i:= 0; i<52; i++{
		if presion_prome[i] > prome{
			arriba = append(arriba, presion_prome[i])
		}
		if presion_prome[i] < prome{
			abajo = append(abajo, presion_prome[i])
		}
	}
	return arriba, abajo
}

func temperatura(presion_prome[]float64)[]float64{
	temp_promedio := []float64{}
	for i:= 0; i<52; i++ {
		temp := (presion_prome[i]*510)/(17.16*0.082)
		temp_promedio = append(temp_promedio, temp)
	}
	return temp_promedio
}

func prom_temperatura(temp_promedio[]float64)float64{
	var suma float64
	suma = 0
	for i:= 0; i<52; i++{
		suma = suma + temp_promedio[i]
	}
	promedio_temp := suma/52
	return promedio_temp
}

func desviacion_estandar(temp_promedio[]float64, promedio_temp float64)float64{
	var suma float64
	suma = 0
	for i:= 0; i<52; i++{
		potencia := math.Pow((temp_promedio[i]-promedio_temp), 2.0)
		suma = suma + potencia
	}
	desvi := (suma/52)
	desviacion := math.Sqrt(desvi)
	return desviacion
}

func arriba_temperatura(temp_promedio[]float64, promedio_temp float64)([]float64, []float64){
	temp_arriba := [] float64 {}
	temp_abajo := [] float64 {}
	for i:= 0; i<52; i++{
		if temp_promedio[i] > promedio_temp{
			temp_arriba = append(temp_arriba, temp_promedio[i])
		}
		if temp_promedio[i] < promedio_temp{
			temp_abajo = append(temp_abajo, temp_promedio[i])
		}
	}
	return temp_arriba, temp_abajo
}

func promeTempArriba(temp_arriba[]float64)float64{
	var suma float64
	suma = 0
	for i:=0; i<len(temp_arriba);i++{
		suma = suma + temp_arriba[i]
	}
	prome_temp_arri := suma/24
	return prome_temp_arri
}

func desviacion_temp_arri(temp_arriba[]float64, prome_temp_arri float64)float64{
	var suma float64
	suma = 0
	for i:= 0; i<24; i++{
		potencia := math.Pow((temp_arriba[i]-prome_temp_arri), 2.0)
		suma = suma + potencia
	}
	desvi := (suma/24)
	desvi_temp_arri := math.Sqrt(desvi)
	return desvi_temp_arri
}

func promeTempAbajo(temp_abajo[]float64)float64{
	var suma float64
	suma = 0
	for i:=0; i<len(temp_abajo);i++{
		suma = suma + temp_abajo[i]
	}
	prome_temp_abajo := suma/28
	return prome_temp_abajo
}

func desviacion_temp_abajo(temp_abajo[]float64, prome_temp_abajo float64)float64{
	var suma float64
	suma = 0
	for i:= 0; i<28; i++{
		potencia := math.Pow((temp_abajo[i]-prome_temp_abajo), 2.0)
		suma = suma + potencia
	}
	desvi := (suma/28)
	desvi_temp_abajo := math.Sqrt(desvi)
	return desvi_temp_abajo
}

func main() {
	presion_prome := promedio()
	diferen := diferencia(presion_prome)
	fmt.Printf("La diferencia entre la mayor y menor presión es:%6.2f\n", diferen)
	prome := media(presion_prome)
	fmt.Printf("La media es: %6.2f\n", prome)
	median := mediana(presion_prome)
	fmt.Printf("La mediana es: %6.2f\n", median)
	presion_prome = promedio()
	arriba, abajo := supera_debajo(presion_prome, prome)
	fmt.Print("Las semanas que superan la presión promedio semanal son:\n")
	fmt.Print(arriba)
	fmt.Print("\nLas semanas inferiores a la presión promedio semanal son:\n")
	fmt.Print(abajo)
	temp_promedio := temperatura(presion_prome)
	fmt.Print("\nLa temperatura promedio es:\n")
	fmt.Printf("%6.2f\n", temp_promedio)
	promedio_temp := prom_temperatura(temp_promedio)
	desviacion := desviacion_estandar(temp_promedio, promedio_temp)
	fmt.Printf("La desviación estándar es: %6.2f\n", desviacion)
	temp_arriba, temp_abajo := arriba_temperatura(temp_promedio, promedio_temp)
	fmt.Print("\nLas semanas que superan la temperatura promedio son: \n")
	fmt.Printf("%6.2f\n", temp_arriba)
	fmt.Print("\nLas semanas que son inferiores a la temperatura promedio son: \n")
	fmt.Printf("%6.2f\n", temp_abajo)
	prome_temp_arri := promeTempArriba(temp_arriba)
	desvi_temp_arri := desviacion_temp_arri(temp_arriba, prome_temp_arri)
	fmt.Printf("\nLa desviación estándar de las semanas que superan el promedio de la temperatura es: %6.2f\n", desvi_temp_arri)
	prome_temp_abajo := promeTempAbajo(temp_abajo)
	desvi_temp_abajo := desviacion_temp_abajo(temp_abajo, prome_temp_abajo)
	fmt.Printf("\nLa desviación estándar de las semanas inferiores al promedio de la temperatura es: %6.2f\n", desvi_temp_abajo)
}
