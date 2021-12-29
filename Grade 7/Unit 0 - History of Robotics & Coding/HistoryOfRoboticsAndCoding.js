// Variables
var TBP_Origins = 'Text-Based programming languages go back to 1943. Officially, the first programming language for computers was Plankalkül. Plankalkül was developed by Konrad Zuse in 1943. Though it was developed back then, the language was never implemented until 1998. So for most, Short Code (formerly Brief Code, proposed by John Mauchly in 1949), Is the first programming language. \n\n' +


'Short code was used to represent mathematical expressions and equations in computers.' +
'William Schmitt first implemented a version of Brief Code in 1949 for the BINAC (Binary Automatic Computer, developed by the Eckert-Mauchly Computer Corporation [EMCC]).  ' +
'However, that version was never debugged or tested. \n\n' + '2 more revised versions of Short Code were created and released between 1950 and 1952. ' +
'The creation of Short Code has directly influenced the creation of intermediate programming languages, as well as the OMNIBAC Symbolic Assembler. As well as indirectly influencing the first programming languages that come after it. '
;

var TBP_First =
'Here is a list of the first 10 unique Text-Based programming languages since 1950\n\n'+

'- Short Code (1950)\n'+
'- ALGAE (1951)\n'+
'- Stanislaus (1951)\n'+
'- Short Merge Generator (1951)\n'+
'- COMPOOL (1952)\n'+
'- Speedcoding (1953)\n'+
'- READ/PRINT (1953)\n'+
'- Laning and Zierler System (1954)\n'+
'- MATRIX MATH (1954)\n'+
'- IPL I (Concept Language) (1954)\n\n'+

'As of 2021, none of these programming languages are in use anymore. However, most of the programming languages listed here were commonly used amongst companies when they were available. Short Code was used by EMCC, SMG was used for apps, and Speedcoding was used by IBM.';

// C Family
var COrigins = 'The Traditional C programming language was developed by Dennis Ritchie in 1972. Ritchie developed C when he was at bell laboratories while he was working for AT&T (American Telephone & Telegraph).\n\n' +
'C was initially developed to overcome the issues of languages such as B, BCPL, and more. Between the years 1972 and 1999, 4 variations of the C language were released. Those being:/n/n' +
'- K&R C (Kernighan & Dennis Ritchie, 1978)\n'+
'- ANSI C (ANSI Committee, 1989)\n'+
'- ANSI/ISO C (Iso Committee, 1990)\n'+
'- C99 (Standardization Committee, 1999)\n'+
'C has also influenced the creation of many more programming languages (such as C++ & C#)';

var CUses = '';

var ChildC = '';



//Literally every button ever
onEvent("TBP", "click", function( ) {
  setScreen("TBP_Screen");
      setText("TBP-TextArea", TBP_Origins);
      setText("dropdown1", "Origins");
});
onEvent("CFamily", "click", function( ) {
  setScreen("CFam-Screen");
  setText("CTextArea", COrigins);
  setText("CDropDown", "Origins");
});
onEvent("HomeButton-TBP", "click", function( ) {
  setScreen("MainScreen");
});
onEvent("Home-CFAM", "click", function( ) {
  setScreen("MainScreen");
});
onEvent("ToCFam", "click", function( ) {
  setScreen("CFam-Screen");
  setText("CTextArea", COrigins);
  setText("CDropDown", "Origins");
});
onEvent("GeneralRobotics", "click", function() {
  setScreen("GeneralRobotics-Screen");
});
onEvent("button8", "click", function() {
  setScreen("GeneralRobotics-Screen");
});
onEvent("Home-GRB", "click", function() {
  setScreen("MainScreen");
});
onEvent("Drones", "click", function() {
  setScreen("DronesScreen");
});
onEvent("ToDrones", "click", function() {
  setScreen("DronesScreen");
});



// Drop down lists
//Text based programming
onEvent("dropdown1", "change", function( ) {
  if (getText("dropdown1") == "Origins") {
    setText("TBP-TextArea", TBP_Origins);
  }});
  
onEvent("dropdown1", "change", function( ) {
  if (getText("dropdown1") == "First Popular Programming Languages") {
    setText("TBP-TextArea", TBP_First);
  }
});

// C Programming
onEvent("CDropDown", "change", function() {
  if (getText("CDropDown", "Origins")) {
    setText("CTextArea", COrigins);
  }
    if (getText("CDropDown", "Uses of C")) {
    setText("CTextArea", CUses);
  }
   if (getText("CDropDown", "Child Languages of C")) {
    setText("CTextArea", ChildC);
  }
});







/*
I tried to make this using the text editor and without using the toolbox
It was not easy
have a good day
*/
