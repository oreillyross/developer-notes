function assert(condition: boolean, message: string) asserts condition {
  if (!condition) {
    throw Error(message);
  }
}

function range(from: number, to: number) {
  
  assert(typeof from === "number" && typeof to === "number", "Range function requires numbers as input") 
  
  const values: number[] = [];
  for (let i = 0; i < to; i++) {
    values.push(i);
  }
  return values;
}

console.log(range("A" as any, "B" as any));
