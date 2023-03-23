 #!/usr/bin/node
function addMeMaybe (number, theFunction) {
  theFunction(number + 1);
}
module.exports.addMeMaybe = addMeMaybe;
