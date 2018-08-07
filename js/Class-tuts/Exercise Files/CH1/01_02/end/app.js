class Car {
    constructor(doors, engine, color) {
        this.doors = doors;
        this.engine = engine;
        this.color = color;
    }

    carStats() {
        return `This car has ${this.doors} doors, a ${this.engine} engine and a beautiful ${this.color} color!`;
    }
    toString(){
      return this.doors + ", "+this.engine + ", "+this.color ;
    }
}

function doX() {
  var cx5 = new Car( 4, 'V6', 'grey');
  //document.getElementByName("header1").innerHTML = cx5;
  //document.getElementByName("header2").innerHTML = cx5.carStats();
  document.querySelector(".header").innerHTML = cx5; 
  //console.log(cx5);
  //console.log(cx5.carStats());

}
var cx5 = new Car( 4, 'V6', 'grey');
//console.log();
console.log(cx5);
console.log(cx5.carStats());
doX();
