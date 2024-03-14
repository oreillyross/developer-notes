# Go programming 

## Testing

### Code coverage

There is a command you can run which will give you a pretty html output highlighting which of your code statements are covered (in green) and which of your code statements are not (in red)

The command to run is a go command and run in your terminal

`shell

go test -coverprofile=coverage.out && go tool cover -html=coverage.out

`
