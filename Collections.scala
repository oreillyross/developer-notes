package oreillyross.github.io

class ExampleCollections {

  val spices = Map("Oregano" -> "Italian", "Cardemon" -> "Indian")
  



}

object ExampleCollections extends App {

  spices foreach {
    case (spice, country) => println(s"$spice is from $country")
  }

  
}
