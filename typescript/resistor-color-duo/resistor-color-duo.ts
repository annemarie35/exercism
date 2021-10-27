export function decodedValue(colors: string[]): number {
  interface ColorsMapping {
    [propertyName: string]: string;
  }

  const ColorsValue: ColorsMapping = {
    black: "0",
    brown: "1",
    blue: "6",
    grey: "8",
    yellow: "4",
    violet: "7",
    orange: "3",
    green: "5"
  }
  
  return Number(`${ColorsValue[colors[0]] }${ColorsValue[colors[1]]}`)
}
