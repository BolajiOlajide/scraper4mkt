package main

type PresetLocations []string

var PRESETS = map[string]PresetLocations{
	"ghana":   PresetLocations{"ghana", "accra", "kumasi", "tema"},
	"nigeria": PresetLocations{"nigeria", "lagos", "kano", "ibadan", "benin%20city", "port%20harcourt", "jos", "ilorin"},
	"egypt":   PresetLocations{"egypt", "cairo", "alexandria", "giza", "port%2Bsaid", "suez", "luxor", "el%2Bmahalla", "asyut", "al%2Bmansurah", "tanda"},
}

func Preset(name string) []string {
	return PRESETS[name]
}
