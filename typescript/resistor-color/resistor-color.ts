type Color = typeof COLORS[number]

export const COLORS: string[] = [
  'black',
  'brown',
  'red',
  'orange',
  'yellow',
  'green',
  'blue',
  'violet',
  'grey',
  'white',
]

export const colorCode = (color: Color): number => {
  
return COLORS.indexOf(color)
}


