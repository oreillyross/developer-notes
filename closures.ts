function counter_constructor() {
  let counter = 0;

  function up() {
    counter += 1;
    return counter;
  }
  function down() {
    counter -= 1;
    return counter;
  }
  function print(){
    console.log(counter)
  }

  return Object.freeze({ up, down, print });


}


const counter = counter_constructor()
counter.print()
counter.up()
counter.print()
counter.up()
counter.print()
counter.down()
counter.print()