

class ExampleCollections {

  



}

object ExampleCollections extends App {

 
  val spices = Map("Oregano" -> "Italy", "Cardemon" -> "India")

  // foreach on maps
  
  spices.foreach {
    case (spice, country) => println(s"$spice is from $country")
  }

   
  // one can loop over any Traversable
  
  val fruits = List("apples", "pears", "peaches")

  for (f <- fruits) {
    
    println(s"$f")
    val F = f.toUpperCase
    println(s"$F")

  }

  // use zipWithIndex when you need a loop counteri. use view to create a lazy view on original list

  for ((f, count) <- fruits.view.zipWithIndex) {
    println(s"$count is an $f")
  }

 // another way using Streams or a range also works well for a defined range
 
 for ((f, count) <- fruits.zip(Stream from 5)) 
    println(s"$count is an $f")


// Sorting an existing map by key or value

// given a basic immutable map.
val grades = Map("Kim" -> 90, "Al" -> 85, "Jim" -> 24, "Emma" -> 45)

// sort the map by key from low to high
import scala.collection.immutable.ListMap

val x = ListMap(grades.toSeq.sortBy(_._1):_*)

// or use sortwith to sort keys by ascending or descending order

val y = ListMap(grades.toSeq.sortWith(_._1 < _._1): _*) 


}
