export function isLeap(year: number): boolean {
  const isDivisibleBy4 = year % 4 === 0
  const isDivisableBy100 = year % 100 === 0
  const isDivisableBy400 = year % 400 === 0

  return (isDivisibleBy4 && !isDivisableBy100) || isDivisableBy400
}
