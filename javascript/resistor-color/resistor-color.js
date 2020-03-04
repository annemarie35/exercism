export const COLORS = ["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
export const colorCode = (color) => {
  const colors = {
    black: 0,
    white: 9,
    orange: 3
  }
  return  colors[color]
}
