name := "Example Code"

scalaVersion := "2.11.4"

libraryDependencies += "com.lihaoyi" % "ammonite-repl" % "0.3.2" % "test" cross CrossVersion.full

initialCommands in (Test, console) := """ammonite.repl.Repl.run("")"""
