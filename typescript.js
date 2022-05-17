"use strict";
asserts;
condition;
{
    if (!condition) {
        throw Error(message);
    }
}
function range(from, to) {
    assert(typeof from === "number" && typeof to === "number", "Range function requires numbers as input");
    var values = [];
    for (var i = 0; i < to; i++) {
        values.push(i);
    }
    return values;
}
console.log(range("A", "B"));
