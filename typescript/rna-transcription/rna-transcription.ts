export function toRna(dnaStrand: string): string {
  interface DnAToRnaMapping {
    [propertyName: string]: string;
  }
  const dnAToRnaMapping: DnAToRnaMapping = {
    G: "C",
    C: "G",
    T: "A",
    A: "U"
  }

  for (let dna of dnaStrand) {
    console.log('dna', dna)
    if (!(dna in dnAToRnaMapping)){
      throw new Error('Invalid input DNA.')
    }
  }


  return dnaStrand.replace(/C|G|T|A/g, dna =>  dnAToRnaMapping[dna]
  )
}
